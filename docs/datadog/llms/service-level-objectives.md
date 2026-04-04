# Source: https://docs.datadoghq.com/api/latest/service-level-objectives.md

---
title: Service Level Objectives
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > API Reference > Service Level Objectives
---

[Service Level Objectives](https://docs.datadoghq.com/monitors/service_level_objectives/#configuration) (or SLOs) are a key part of the site reliability engineering toolkit. SLOs provide a framework for defining clear targets around application performance, which ultimately help teams provide a consistent customer experience, balance feature development with platform stability, and improve communication with internal and external users.

## Create an SLO object{% #create-an-slo-object %}

{% tab title="v1" %}

| Datadog site      | API endpoint                                  |
| ----------------- | --------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v1/slo |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v1/slo |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v1/slo      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v1/slo      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v1/slo     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v1/slo |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v1/slo |

### Overview

Create a service level objective object. This endpoint requires the `slos_write` permission.

OAuth apps require the `slos_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#service-level-objectives) to access this endpoint.

### Request

#### Body Data (required)

Service level objective request object.

{% tab title="Model" %}

| Parent field         | Field                                  | Type            | Description                                                                                                                                                                                                                                                                                                             |
| -------------------- | -------------------------------------- | --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                      | description                            | string          | A user-defined description of the service level objective.                                                                                                                                                                                                                                                              | Always included in service level objective responses (but may be `null`). Optional in create/update requests.                                                                                                       |
|                      | groups                                 | [string]        | A list of (up to 100) monitor groups that narrow the scope of a monitor service level objective.                                                                                                                                                                                                                        | Included in service level objective responses if it is not empty. Optional in create/update requests for monitor service level objectives, but may only be used when then length of the `monitor_ids` field is one. |
|                      | monitor_ids                            | [integer]       | A list of monitor IDs that defines the scope of a monitor service level objective. **Required if type is `monitor`**.                                                                                                                                                                                                   |
|                      | name [*required*]                 | string          | The name of the service level objective object.                                                                                                                                                                                                                                                                         |
|                      | query                                  | object          | A count-based (metric) SLO query. This field is superseded by `sli_specification` but is retained for backwards compatibility. Note that Datadog only allows the sum by aggregator to be used because this will sum up all request counts instead of averaging them, or taking the max or min of all of those requests. |
| query                | denominator [*required*]          | string          | A Datadog metric query for total (valid) events.                                                                                                                                                                                                                                                                        |
| query                | numerator [*required*]            | string          | A Datadog metric query for good events.                                                                                                                                                                                                                                                                                 |
|                      | sli_specification                      |  <oneOf>   | A generic SLI specification. This is used for time-slice and count-based (metric) SLOs only.                                                                                                                                                                                                                            |
| sli_specification    | Option 1                               | object          | A time-slice SLI specification.                                                                                                                                                                                                                                                                                         |
| Option 1             | time_slice [*required*]           | object          | The time-slice condition, composed of 3 parts: 1. the metric timeseries query, 2. the comparator, and 3. the threshold. Optionally, a fourth part, the query interval, can be provided.                                                                                                                                 |
| time_slice           | comparator [*required*]           | enum            | The comparator used to compare the SLI value to the threshold. Allowed enum values: `>,>=,<,<=`                                                                                                                                                                                                                         |
| time_slice           | query [*required*]                | object          | The queries and formula used to calculate the SLI value.                                                                                                                                                                                                                                                                |
| query                | formulas [*required*]             | [object]        | A list that contains exactly one formula, as only a single formula may be used in a time-slice SLO.                                                                                                                                                                                                                     |
| formulas             | formula [*required*]              | string          | The formula string, which is an expression involving named queries.                                                                                                                                                                                                                                                     |
| query                | queries [*required*]              | [ <oneOf>] | A list of queries that are used to calculate the SLI value.                                                                                                                                                                                                                                                             |
| queries              | Option 1                               | object          | A formula and functions metrics query.                                                                                                                                                                                                                                                                                  |
| Option 1             | aggregator                             | enum            | The aggregation methods available for metrics queries. Allowed enum values: `avg,min,max,sum,last,area,l2norm,percentile`                                                                                                                                                                                               |
| Option 1             | cross_org_uuids                        | [string]        | The source organization UUID for cross organization queries. Feature in Private Beta.                                                                                                                                                                                                                                   |
| Option 1             | data_source [*required*]          | enum            | Data source for metrics queries. Allowed enum values: `metrics`                                                                                                                                                                                                                                                         |
| Option 1             | name [*required*]                 | string          | Name of the query for use in formulas.                                                                                                                                                                                                                                                                                  |
| Option 1             | query [*required*]                | string          | Metrics query definition.                                                                                                                                                                                                                                                                                               |
| Option 1             | semantic_mode                          | enum            | Semantic mode for metrics queries. This determines how metrics from different sources are combined or displayed. Allowed enum values: `combined,native`                                                                                                                                                                 |
| time_slice           | query_interval_seconds                 | enum            | The interval used when querying data, which defines the size of a time slice. Two values are allowed: 60 (1 minute) and 300 (5 minutes). If not provided, the value defaults to 300 (5 minutes). Allowed enum values: `60,300`                                                                                          |
| time_slice           | threshold [*required*]            | double          | The threshold value to which each SLI value will be compared.                                                                                                                                                                                                                                                           |
| sli_specification    | Option 2                               | object          | A metric SLI specification.                                                                                                                                                                                                                                                                                             |
| Option 2             | count [*required*]                | object          | A count-based (metric) SLI specification, composed of three parts: the good events formula, the total events formula, and the underlying queries.                                                                                                                                                                       |
| count                | good_events_formula [*required*]  | object          | A formula that specifies how to combine the results of multiple queries.                                                                                                                                                                                                                                                |
| good_events_formula  | formula [*required*]              | string          | The formula string, which is an expression involving named queries.                                                                                                                                                                                                                                                     |
| count                | queries [*required*]              | [ <oneOf>] |
| queries              | Option 1                               | object          | A formula and functions metrics query.                                                                                                                                                                                                                                                                                  |
| Option 1             | aggregator                             | enum            | The aggregation methods available for metrics queries. Allowed enum values: `avg,min,max,sum,last,area,l2norm,percentile`                                                                                                                                                                                               |
| Option 1             | cross_org_uuids                        | [string]        | The source organization UUID for cross organization queries. Feature in Private Beta.                                                                                                                                                                                                                                   |
| Option 1             | data_source [*required*]          | enum            | Data source for metrics queries. Allowed enum values: `metrics`                                                                                                                                                                                                                                                         |
| Option 1             | name [*required*]                 | string          | Name of the query for use in formulas.                                                                                                                                                                                                                                                                                  |
| Option 1             | query [*required*]                | string          | Metrics query definition.                                                                                                                                                                                                                                                                                               |
| Option 1             | semantic_mode                          | enum            | Semantic mode for metrics queries. This determines how metrics from different sources are combined or displayed. Allowed enum values: `combined,native`                                                                                                                                                                 |
| count                | total_events_formula [*required*] | object          | A formula that specifies how to combine the results of multiple queries.                                                                                                                                                                                                                                                |
| total_events_formula | formula [*required*]              | string          | The formula string, which is an expression involving named queries.                                                                                                                                                                                                                                                     |
|                      | tags                                   | [string]        | A list of tags associated with this service level objective. Always included in service level objective responses (but may be empty). Optional in create/update requests.                                                                                                                                               |
|                      | target_threshold                       | double          | The target threshold such that when the service level indicator is above this threshold over the given timeframe, the objective is being met.                                                                                                                                                                           |
|                      | thresholds [*required*]           | [object]        | The thresholds (timeframes and associated targets) for this service level objective object.                                                                                                                                                                                                                             |
| thresholds           | target [*required*]               | double          | The target value for the service level indicator within the corresponding timeframe.                                                                                                                                                                                                                                    |
| thresholds           | target_display                         | string          | A string representation of the target that indicates its precision. It uses trailing zeros to show significant decimal places (for example `98.00`).                                                                                                                                                                    | Always included in service level objective responses. Ignored in create/update requests.                                                                                                                            |
| thresholds           | timeframe [*required*]            | enum            | The SLO time window options. Note that "custom" is not a valid option for creating or updating SLOs. It is only used when querying SLO history over custom timeframes. Allowed enum values: `7d,30d,90d,custom`                                                                                                         |
| thresholds           | warning                                | double          | The warning value for the service level objective.                                                                                                                                                                                                                                                                      |
| thresholds           | warning_display                        | string          | A string representation of the warning target (see the description of the `target_display` field for details).                                                                                                                                                                                                          | Included in service level objective responses if a warning target exists. Ignored in create/update requests.                                                                                                        |
|                      | timeframe                              | enum            | The SLO time window options. Note that "custom" is not a valid option for creating or updating SLOs. It is only used when querying SLO history over custom timeframes. Allowed enum values: `7d,30d,90d,custom`                                                                                                         |
|                      | type [*required*]                 | enum            | The type of the service level objective. Allowed enum values: `metric,monitor,time_slice`                                                                                                                                                                                                                               |
|                      | warning_threshold                      | double          | The optional warning threshold such that when the service level indicator is below this value for the given threshold, but above the target threshold, the objective appears in a "warning" state. This value must be greater than the target threshold.                                                                |

{% /tab %}

{% tab title="Example" %}
#####

```json
{
  "type": "metric",
  "description": "Metric SLO using sli_specification",
  "name": "Example-Service-Level-Objective",
  "sli_specification": {
    "count": {
      "good_events_formula": {
        "formula": "query1 - query2"
      },
      "total_events_formula": {
        "formula": "query1"
      },
      "queries": [
        {
          "data_source": "metrics",
          "name": "query1",
          "query": "sum:httpservice.hits{*}.as_count()"
        },
        {
          "data_source": "metrics",
          "name": "query2",
          "query": "sum:httpservice.errors{*}.as_count()"
        }
      ]
    }
  },
  "tags": [
    "env:prod",
    "type:count"
  ],
  "thresholds": [
    {
      "target": 99.0,
      "target_display": "99.0",
      "timeframe": "7d",
      "warning": 99.5,
      "warning_display": "99.5"
    }
  ],
  "timeframe": "7d",
  "target_threshold": 99.0,
  "warning_threshold": 99.5
}
```

#####

```json
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

#####

```json
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

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
A response with one or more service level objective.

| Parent field         | Field                                  | Type            | Description                                                                                                                                                                                                                                                                                                                                                                   |
| -------------------- | -------------------------------------- | --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                      | data                                   | [object]        | An array of service level objective objects.                                                                                                                                                                                                                                                                                                                                  |
| data                 | created_at                             | int64           | Creation timestamp (UNIX time in seconds)                                                                                                                                                                                                                                                                                                                                     | Always included in service level objective responses.                                                                                                                                                               |
| data                 | creator                                | object          | Object describing the creator of the shared element.                                                                                                                                                                                                                                                                                                                          |
| creator              | email                                  | string          | Email of the creator.                                                                                                                                                                                                                                                                                                                                                         |
| creator              | handle                                 | string          | Handle of the creator.                                                                                                                                                                                                                                                                                                                                                        |
| creator              | name                                   | string          | Name of the creator.                                                                                                                                                                                                                                                                                                                                                          |
| data                 | description                            | string          | A user-defined description of the service level objective.                                                                                                                                                                                                                                                                                                                    | Always included in service level objective responses (but may be `null`). Optional in create/update requests.                                                                                                       |
| data                 | groups                                 | [string]        | A list of (up to 100) monitor groups that narrow the scope of a monitor service level objective.                                                                                                                                                                                                                                                                              | Included in service level objective responses if it is not empty. Optional in create/update requests for monitor service level objectives, but may only be used when then length of the `monitor_ids` field is one. |
| data                 | id                                     | string          | A unique identifier for the service level objective object.                                                                                                                                                                                                                                                                                                                   | Always included in service level objective responses.                                                                                                                                                               |
| data                 | modified_at                            | int64           | Modification timestamp (UNIX time in seconds)                                                                                                                                                                                                                                                                                                                                 | Always included in service level objective responses.                                                                                                                                                               |
| data                 | monitor_ids                            | [integer]       | A list of monitor ids that defines the scope of a monitor service level objective. **Required if type is `monitor`**.                                                                                                                                                                                                                                                         |
| data                 | monitor_tags                           | [string]        | The union of monitor tags for all monitors referenced by the `monitor_ids` field. Always included in service level objective responses for monitor-based service level objectives (but may be empty). Ignored in create/update requests. Does not affect which monitors are included in the service level objective (that is determined entirely by the `monitor_ids` field). |
| data                 | name [*required*]                 | string          | The name of the service level objective object.                                                                                                                                                                                                                                                                                                                               |
| data                 | query                                  | object          | A count-based (metric) SLO query. This field is superseded by `sli_specification` but is retained for backwards compatibility. Note that Datadog only allows the sum by aggregator to be used because this will sum up all request counts instead of averaging them, or taking the max or min of all of those requests.                                                       |
| query                | denominator [*required*]          | string          | A Datadog metric query for total (valid) events.                                                                                                                                                                                                                                                                                                                              |
| query                | numerator [*required*]            | string          | A Datadog metric query for good events.                                                                                                                                                                                                                                                                                                                                       |
| data                 | sli_specification                      |  <oneOf>   | A generic SLI specification. This is used for time-slice and count-based (metric) SLOs only.                                                                                                                                                                                                                                                                                  |
| sli_specification    | Option 1                               | object          | A time-slice SLI specification.                                                                                                                                                                                                                                                                                                                                               |
| Option 1             | time_slice [*required*]           | object          | The time-slice condition, composed of 3 parts: 1. the metric timeseries query, 2. the comparator, and 3. the threshold. Optionally, a fourth part, the query interval, can be provided.                                                                                                                                                                                       |
| time_slice           | comparator [*required*]           | enum            | The comparator used to compare the SLI value to the threshold. Allowed enum values: `>,>=,<,<=`                                                                                                                                                                                                                                                                               |
| time_slice           | query [*required*]                | object          | The queries and formula used to calculate the SLI value.                                                                                                                                                                                                                                                                                                                      |
| query                | formulas [*required*]             | [object]        | A list that contains exactly one formula, as only a single formula may be used in a time-slice SLO.                                                                                                                                                                                                                                                                           |
| formulas             | formula [*required*]              | string          | The formula string, which is an expression involving named queries.                                                                                                                                                                                                                                                                                                           |
| query                | queries [*required*]              | [ <oneOf>] | A list of queries that are used to calculate the SLI value.                                                                                                                                                                                                                                                                                                                   |
| queries              | Option 1                               | object          | A formula and functions metrics query.                                                                                                                                                                                                                                                                                                                                        |
| Option 1             | aggregator                             | enum            | The aggregation methods available for metrics queries. Allowed enum values: `avg,min,max,sum,last,area,l2norm,percentile`                                                                                                                                                                                                                                                     |
| Option 1             | cross_org_uuids                        | [string]        | The source organization UUID for cross organization queries. Feature in Private Beta.                                                                                                                                                                                                                                                                                         |
| Option 1             | data_source [*required*]          | enum            | Data source for metrics queries. Allowed enum values: `metrics`                                                                                                                                                                                                                                                                                                               |
| Option 1             | name [*required*]                 | string          | Name of the query for use in formulas.                                                                                                                                                                                                                                                                                                                                        |
| Option 1             | query [*required*]                | string          | Metrics query definition.                                                                                                                                                                                                                                                                                                                                                     |
| Option 1             | semantic_mode                          | enum            | Semantic mode for metrics queries. This determines how metrics from different sources are combined or displayed. Allowed enum values: `combined,native`                                                                                                                                                                                                                       |
| time_slice           | query_interval_seconds                 | enum            | The interval used when querying data, which defines the size of a time slice. Two values are allowed: 60 (1 minute) and 300 (5 minutes). If not provided, the value defaults to 300 (5 minutes). Allowed enum values: `60,300`                                                                                                                                                |
| time_slice           | threshold [*required*]            | double          | The threshold value to which each SLI value will be compared.                                                                                                                                                                                                                                                                                                                 |
| sli_specification    | Option 2                               | object          | A metric SLI specification.                                                                                                                                                                                                                                                                                                                                                   |
| Option 2             | count [*required*]                | object          | A count-based (metric) SLI specification, composed of three parts: the good events formula, the total events formula, and the underlying queries.                                                                                                                                                                                                                             |
| count                | good_events_formula [*required*]  | object          | A formula that specifies how to combine the results of multiple queries.                                                                                                                                                                                                                                                                                                      |
| good_events_formula  | formula [*required*]              | string          | The formula string, which is an expression involving named queries.                                                                                                                                                                                                                                                                                                           |
| count                | queries [*required*]              | [ <oneOf>] |
| queries              | Option 1                               | object          | A formula and functions metrics query.                                                                                                                                                                                                                                                                                                                                        |
| Option 1             | aggregator                             | enum            | The aggregation methods available for metrics queries. Allowed enum values: `avg,min,max,sum,last,area,l2norm,percentile`                                                                                                                                                                                                                                                     |
| Option 1             | cross_org_uuids                        | [string]        | The source organization UUID for cross organization queries. Feature in Private Beta.                                                                                                                                                                                                                                                                                         |
| Option 1             | data_source [*required*]          | enum            | Data source for metrics queries. Allowed enum values: `metrics`                                                                                                                                                                                                                                                                                                               |
| Option 1             | name [*required*]                 | string          | Name of the query for use in formulas.                                                                                                                                                                                                                                                                                                                                        |
| Option 1             | query [*required*]                | string          | Metrics query definition.                                                                                                                                                                                                                                                                                                                                                     |
| Option 1             | semantic_mode                          | enum            | Semantic mode for metrics queries. This determines how metrics from different sources are combined or displayed. Allowed enum values: `combined,native`                                                                                                                                                                                                                       |
| count                | total_events_formula [*required*] | object          | A formula that specifies how to combine the results of multiple queries.                                                                                                                                                                                                                                                                                                      |
| total_events_formula | formula [*required*]              | string          | The formula string, which is an expression involving named queries.                                                                                                                                                                                                                                                                                                           |
| data                 | tags                                   | [string]        | A list of tags associated with this service level objective. Always included in service level objective responses (but may be empty). Optional in create/update requests.                                                                                                                                                                                                     |
| data                 | target_threshold                       | double          | The target threshold such that when the service level indicator is above this threshold over the given timeframe, the objective is being met.                                                                                                                                                                                                                                 |
| data                 | thresholds [*required*]           | [object]        | The thresholds (timeframes and associated targets) for this service level objective object.                                                                                                                                                                                                                                                                                   |
| thresholds           | target [*required*]               | double          | The target value for the service level indicator within the corresponding timeframe.                                                                                                                                                                                                                                                                                          |
| thresholds           | target_display                         | string          | A string representation of the target that indicates its precision. It uses trailing zeros to show significant decimal places (for example `98.00`).                                                                                                                                                                                                                          | Always included in service level objective responses. Ignored in create/update requests.                                                                                                                            |
| thresholds           | timeframe [*required*]            | enum            | The SLO time window options. Note that "custom" is not a valid option for creating or updating SLOs. It is only used when querying SLO history over custom timeframes. Allowed enum values: `7d,30d,90d,custom`                                                                                                                                                               |
| thresholds           | warning                                | double          | The warning value for the service level objective.                                                                                                                                                                                                                                                                                                                            |
| thresholds           | warning_display                        | string          | A string representation of the warning target (see the description of the `target_display` field for details).                                                                                                                                                                                                                                                                | Included in service level objective responses if a warning target exists. Ignored in create/update requests.                                                                                                        |
| data                 | timeframe                              | enum            | The SLO time window options. Note that "custom" is not a valid option for creating or updating SLOs. It is only used when querying SLO history over custom timeframes. Allowed enum values: `7d,30d,90d,custom`                                                                                                                                                               |
| data                 | type [*required*]                 | enum            | The type of the service level objective. Allowed enum values: `metric,monitor,time_slice`                                                                                                                                                                                                                                                                                     |
| data                 | warning_threshold                      | double          | The optional warning threshold such that when the service level indicator is below this value for the given threshold, but above the target threshold, the objective appears in a "warning" state. This value must be greater than the target threshold.                                                                                                                      |
|                      | errors                                 | [string]        | An array of error messages. Each endpoint documents how/whether this field is used.                                                                                                                                                                                                                                                                                           |
|                      | metadata                               | object          | The metadata object containing additional information about the list of SLOs.                                                                                                                                                                                                                                                                                                 |
| metadata             | page                                   | object          | The object containing information about the pages of the list of SLOs.                                                                                                                                                                                                                                                                                                        |
| page                 | total_count                            | int64           | The total number of resources that could be retrieved ignoring the parameters and filters in the request.                                                                                                                                                                                                                                                                     |
| page                 | total_filtered_count                   | int64           | The total number of resources that match the parameters and filters in the request. This attribute can be used by a client to determine the total number of pages.                                                                                                                                                                                                            |

{% /tab %}

{% tab title="Example" %}

```json
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

{% /tab %}

{% /tab %}

{% tab title="400" %}
Bad Request
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
                          \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/slo" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "type": "metric",
  "description": "Metric SLO using sli_specification",
  "name": "Example-Service-Level-Objective",
  "sli_specification": {
    "count": {
      "good_events_formula": {
        "formula": "query1 - query2"
      },
      "total_events_formula": {
        "formula": "query1"
      },
      "queries": [
        {
          "data_source": "metrics",
          "name": "query1",
          "query": "sum:httpservice.hits{*}.as_count()"
        },
        {
          "data_source": "metrics",
          "name": "query2",
          "query": "sum:httpservice.errors{*}.as_count()"
        }
      ]
    }
  },
  "tags": [
    "env:prod",
    "type:count"
  ],
  "thresholds": [
    {
      "target": 99.0,
      "target_display": "99.0",
      "timeframe": "7d",
      "warning": 99.5,
      "warning_display": "99.5"
    }
  ],
  "timeframe": "7d",
  "target_threshold": 99.0,
  "warning_threshold": 99.5
}
EOF

#####
                          \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/slo" \
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

#####
                          \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/slo" \
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

#####

```go
// Create a new metric SLO object using sli_specification returns "OK" response

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
        Description: *datadog.NewNullableString(datadog.PtrString("Metric SLO using sli_specification")),
        Name:        "Example-Service-Level-Objective",
        SliSpecification: &datadogV1.SLOSliSpec{
            SLOCountSpec: &datadogV1.SLOCountSpec{
                Count: datadogV1.SLOCountDefinition{
                    GoodEventsFormula: datadogV1.SLOFormula{
                        Formula: "query1 - query2",
                    },
                    TotalEventsFormula: datadogV1.SLOFormula{
                        Formula: "query1",
                    },
                    Queries: []datadogV1.SLODataSourceQueryDefinition{
                        datadogV1.SLODataSourceQueryDefinition{
                            FormulaAndFunctionMetricQueryDefinition: &datadogV1.FormulaAndFunctionMetricQueryDefinition{
                                DataSource: datadogV1.FORMULAANDFUNCTIONMETRICDATASOURCE_METRICS,
                                Name:       "query1",
                                Query:      "sum:httpservice.hits{*}.as_count()",
                            }},
                        datadogV1.SLODataSourceQueryDefinition{
                            FormulaAndFunctionMetricQueryDefinition: &datadogV1.FormulaAndFunctionMetricQueryDefinition{
                                DataSource: datadogV1.FORMULAANDFUNCTIONMETRICDATASOURCE_METRICS,
                                Name:       "query2",
                                Query:      "sum:httpservice.errors{*}.as_count()",
                            }},
                    },
                },
            }},
        Tags: []string{
            "env:prod",
            "type:count",
        },
        Thresholds: []datadogV1.SLOThreshold{
            {
                Target:         99.0,
                TargetDisplay:  datadog.PtrString("99.0"),
                Timeframe:      datadogV1.SLOTIMEFRAME_SEVEN_DAYS,
                Warning:        datadog.PtrFloat64(99.5),
                WarningDisplay: datadog.PtrString("99.5"),
            },
        },
        Timeframe:        datadogV1.SLOTIMEFRAME_SEVEN_DAYS.Ptr(),
        TargetThreshold:  datadog.PtrFloat64(99.0),
        WarningThreshold: datadog.PtrFloat64(99.5),
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

#####

```go
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

#####

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// Create a new metric SLO object using sli_specification returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.ServiceLevelObjectivesApi;
import com.datadog.api.client.v1.model.FormulaAndFunctionMetricDataSource;
import com.datadog.api.client.v1.model.FormulaAndFunctionMetricQueryDefinition;
import com.datadog.api.client.v1.model.SLOCountDefinition;
import com.datadog.api.client.v1.model.SLOCountSpec;
import com.datadog.api.client.v1.model.SLODataSourceQueryDefinition;
import com.datadog.api.client.v1.model.SLOFormula;
import com.datadog.api.client.v1.model.SLOListResponse;
import com.datadog.api.client.v1.model.SLOSliSpec;
import com.datadog.api.client.v1.model.SLOThreshold;
import com.datadog.api.client.v1.model.SLOTimeframe;
import com.datadog.api.client.v1.model.SLOType;
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
            .description("Metric SLO using sli_specification")
            .name("Example-Service-Level-Objective")
            .sliSpecification(
                new SLOSliSpec(
                    new SLOCountSpec()
                        .count(
                            new SLOCountDefinition()
                                .goodEventsFormula(new SLOFormula().formula("query1 - query2"))
                                .totalEventsFormula(new SLOFormula().formula("query1"))
                                .queries(
                                    Arrays.asList(
                                        new SLODataSourceQueryDefinition(
                                            new FormulaAndFunctionMetricQueryDefinition()
                                                .dataSource(
                                                    FormulaAndFunctionMetricDataSource.METRICS)
                                                .name("query1")
                                                .query("sum:httpservice.hits{*}.as_count()")),
                                        new SLODataSourceQueryDefinition(
                                            new FormulaAndFunctionMetricQueryDefinition()
                                                .dataSource(
                                                    FormulaAndFunctionMetricDataSource.METRICS)
                                                .name("query2")
                                                .query("sum:httpservice.errors{*}.as_count()")))))))
            .tags(Arrays.asList("env:prod", "type:count"))
            .thresholds(
                Collections.singletonList(
                    new SLOThreshold()
                        .target(99.0)
                        .targetDisplay("99.0")
                        .timeframe(SLOTimeframe.SEVEN_DAYS)
                        .warning(99.5)
                        .warningDisplay("99.5")))
            .timeframe(SLOTimeframe.SEVEN_DAYS)
            .targetThreshold(99.0)
            .warningThreshold(99.5);

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

#####

```java
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

#####

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"
#####

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python-legacy) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python "example.py"
#####

```python
"""
Create a new metric SLO object using sli_specification returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.service_level_objectives_api import ServiceLevelObjectivesApi
from datadog_api_client.v1.model.formula_and_function_metric_data_source import FormulaAndFunctionMetricDataSource
from datadog_api_client.v1.model.formula_and_function_metric_query_definition import (
    FormulaAndFunctionMetricQueryDefinition,
)
from datadog_api_client.v1.model.service_level_objective_request import ServiceLevelObjectiveRequest
from datadog_api_client.v1.model.slo_count_definition import SLOCountDefinition
from datadog_api_client.v1.model.slo_count_spec import SLOCountSpec
from datadog_api_client.v1.model.slo_formula import SLOFormula
from datadog_api_client.v1.model.slo_threshold import SLOThreshold
from datadog_api_client.v1.model.slo_timeframe import SLOTimeframe
from datadog_api_client.v1.model.slo_type import SLOType

body = ServiceLevelObjectiveRequest(
    type=SLOType.METRIC,
    description="Metric SLO using sli_specification",
    name="Example-Service-Level-Objective",
    sli_specification=SLOCountSpec(
        count=SLOCountDefinition(
            good_events_formula=SLOFormula(
                formula="query1 - query2",
            ),
            total_events_formula=SLOFormula(
                formula="query1",
            ),
            queries=[
                FormulaAndFunctionMetricQueryDefinition(
                    data_source=FormulaAndFunctionMetricDataSource.METRICS,
                    name="query1",
                    query="sum:httpservice.hits{*}.as_count()",
                ),
                FormulaAndFunctionMetricQueryDefinition(
                    data_source=FormulaAndFunctionMetricDataSource.METRICS,
                    name="query2",
                    query="sum:httpservice.errors{*}.as_count()",
                ),
            ],
        ),
    ),
    tags=[
        "env:prod",
        "type:count",
    ],
    thresholds=[
        SLOThreshold(
            target=99.0,
            target_display="99.0",
            timeframe=SLOTimeframe.SEVEN_DAYS,
            warning=99.5,
            warning_display="99.5",
        ),
    ],
    timeframe=SLOTimeframe.SEVEN_DAYS,
    target_threshold=99.0,
    warning_threshold=99.5,
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ServiceLevelObjectivesApi(api_client)
    response = api_instance.create_slo(body=body)

    print(response)
```

#####

```python
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

#####

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby-legacy) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```ruby
# Create a new metric SLO object using sli_specification returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::ServiceLevelObjectivesAPI.new

body = DatadogAPIClient::V1::ServiceLevelObjectiveRequest.new({
  type: DatadogAPIClient::V1::SLOType::METRIC,
  description: "Metric SLO using sli_specification",
  name: "Example-Service-Level-Objective",
  sli_specification: DatadogAPIClient::V1::SLOCountSpec.new({
    count: DatadogAPIClient::V1::SLOCountDefinition.new({
      good_events_formula: DatadogAPIClient::V1::SLOFormula.new({
        formula: "query1 - query2",
      }),
      total_events_formula: DatadogAPIClient::V1::SLOFormula.new({
        formula: "query1",
      }),
      queries: [
        DatadogAPIClient::V1::FormulaAndFunctionMetricQueryDefinition.new({
          data_source: DatadogAPIClient::V1::FormulaAndFunctionMetricDataSource::METRICS,
          name: "query1",
          query: "sum:httpservice.hits{*}.as_count()",
        }),
        DatadogAPIClient::V1::FormulaAndFunctionMetricQueryDefinition.new({
          data_source: DatadogAPIClient::V1::FormulaAndFunctionMetricDataSource::METRICS,
          name: "query2",
          query: "sum:httpservice.errors{*}.as_count()",
        }),
      ],
    }),
  }),
  tags: [
    "env:prod",
    "type:count",
  ],
  thresholds: [
    DatadogAPIClient::V1::SLOThreshold.new({
      target: 99.0,
      target_display: "99.0",
      timeframe: DatadogAPIClient::V1::SLOTimeframe::SEVEN_DAYS,
      warning: 99.5,
      warning_display: "99.5",
    }),
  ],
  timeframe: DatadogAPIClient::V1::SLOTimeframe::SEVEN_DAYS,
  target_threshold: 99.0,
  warning_threshold: 99.5,
})
p api_instance.create_slo(body)
```

#####

```ruby
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

#####

```ruby
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```rust
// Create a new metric SLO object using sli_specification returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_service_level_objectives::ServiceLevelObjectivesAPI;
use datadog_api_client::datadogV1::model::FormulaAndFunctionMetricDataSource;
use datadog_api_client::datadogV1::model::FormulaAndFunctionMetricQueryDefinition;
use datadog_api_client::datadogV1::model::SLOCountDefinition;
use datadog_api_client::datadogV1::model::SLOCountSpec;
use datadog_api_client::datadogV1::model::SLODataSourceQueryDefinition;
use datadog_api_client::datadogV1::model::SLOFormula;
use datadog_api_client::datadogV1::model::SLOSliSpec;
use datadog_api_client::datadogV1::model::SLOThreshold;
use datadog_api_client::datadogV1::model::SLOTimeframe;
use datadog_api_client::datadogV1::model::SLOType;
use datadog_api_client::datadogV1::model::ServiceLevelObjectiveRequest;

#[tokio::main]
async fn main() {
    let body = ServiceLevelObjectiveRequest::new(
        "Example-Service-Level-Objective".to_string(),
        vec![SLOThreshold::new(99.0, SLOTimeframe::SEVEN_DAYS)
            .target_display("99.0".to_string())
            .warning(99.5 as f64)
            .warning_display("99.5".to_string())],
        SLOType::METRIC,
    )
    .description(Some("Metric SLO using sli_specification".to_string()))
    .sli_specification(SLOSliSpec::SLOCountSpec(Box::new(SLOCountSpec::new(
        SLOCountDefinition::new(
            SLOFormula::new("query1 - query2".to_string()),
            vec![
                SLODataSourceQueryDefinition::FormulaAndFunctionMetricQueryDefinition(Box::new(
                    FormulaAndFunctionMetricQueryDefinition::new(
                        FormulaAndFunctionMetricDataSource::METRICS,
                        "query1".to_string(),
                        "sum:httpservice.hits{*}.as_count()".to_string(),
                    ),
                )),
                SLODataSourceQueryDefinition::FormulaAndFunctionMetricQueryDefinition(Box::new(
                    FormulaAndFunctionMetricQueryDefinition::new(
                        FormulaAndFunctionMetricDataSource::METRICS,
                        "query2".to_string(),
                        "sum:httpservice.errors{*}.as_count()".to_string(),
                    ),
                )),
            ],
            SLOFormula::new("query1".to_string()),
        ),
    ))))
    .tags(vec!["env:prod".to_string(), "type:count".to_string()])
    .target_threshold(99.0 as f64)
    .timeframe(SLOTimeframe::SEVEN_DAYS)
    .warning_threshold(99.5 as f64);
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

#####

```rust
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

#####

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
#####

```typescript
/**
 * Create a new metric SLO object using sli_specification returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.ServiceLevelObjectivesApi(configuration);

const params: v1.ServiceLevelObjectivesApiCreateSLORequest = {
  body: {
    type: "metric",
    description: "Metric SLO using sli_specification",
    name: "Example-Service-Level-Objective",
    sliSpecification: {
      count: {
        goodEventsFormula: {
          formula: "query1 - query2",
        },
        totalEventsFormula: {
          formula: "query1",
        },
        queries: [
          {
            dataSource: "metrics",
            name: "query1",
            query: "sum:httpservice.hits{*}.as_count()",
          },
          {
            dataSource: "metrics",
            name: "query2",
            query: "sum:httpservice.errors{*}.as_count()",
          },
        ],
      },
    },
    tags: ["env:prod", "type:count"],
    thresholds: [
      {
        target: 99.0,
        targetDisplay: "99.0",
        timeframe: "7d",
        warning: 99.5,
        warningDisplay: "99.5",
      },
    ],
    timeframe: "7d",
    targetThreshold: 99.0,
    warningThreshold: 99.5,
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

#####

```typescript
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

#####

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"
{% /tab %}

## Search for SLOs{% #search-for-slos %}

{% tab title="v1" %}

| Datadog site      | API endpoint                                        |
| ----------------- | --------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v1/slo/search |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v1/slo/search |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v1/slo/search      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v1/slo/search      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v1/slo/search     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v1/slo/search |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v1/slo/search |

### Overview

Get a list of service level objective objects for your organization. This endpoint requires the `slos_read` permission.

OAuth apps require the `slos_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#service-level-objectives) to access this endpoint.

### Arguments

#### Query Strings

| Name           | Type    | Description                                                                                                                        |
| -------------- | ------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| query          | string  | The query string to filter results based on SLO names. Some examples of queries include `service:<service-name>` and `<slo-name>`. |
| page[size]     | integer | The number of files to return in the response `[default=10]`.                                                                      |
| page[number]   | integer | The identifier of the first page to return. This parameter is used for the pagination feature `[default=0]`.                       |
| include_facets | boolean | Whether or not to return facet information in the response `[default=false]`.                                                      |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
A search SLO response containing results from the search query.

| Parent field               | Field                       | Type      | Description                                                                                                                                                                                                                                    |
| -------------------------- | --------------------------- | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                            | data                        | object    | Data from search SLO response.                                                                                                                                                                                                                 |
| data                       | attributes                  | object    | Attributes                                                                                                                                                                                                                                     |
| attributes                 | facets                      | object    | Facets                                                                                                                                                                                                                                         |
| facets                     | all_tags                    | [object]  | All tags associated with an SLO.                                                                                                                                                                                                               |
| all_tags                   | count                       | int64     | Count                                                                                                                                                                                                                                          |
| all_tags                   | name                        | string    | Facet                                                                                                                                                                                                                                          |
| facets                     | creator_name                | [object]  | Creator of an SLO.                                                                                                                                                                                                                             |
| creator_name               | count                       | int64     | Count                                                                                                                                                                                                                                          |
| creator_name               | name                        | string    | Facet                                                                                                                                                                                                                                          |
| facets                     | env_tags                    | [object]  | Tags with the `env` tag key.                                                                                                                                                                                                                   |
| env_tags                   | count                       | int64     | Count                                                                                                                                                                                                                                          |
| env_tags                   | name                        | string    | Facet                                                                                                                                                                                                                                          |
| facets                     | service_tags                | [object]  | Tags with the `service` tag key.                                                                                                                                                                                                               |
| service_tags               | count                       | int64     | Count                                                                                                                                                                                                                                          |
| service_tags               | name                        | string    | Facet                                                                                                                                                                                                                                          |
| facets                     | slo_type                    | [object]  | Type of SLO.                                                                                                                                                                                                                                   |
| slo_type                   | count                       | int64     | Count                                                                                                                                                                                                                                          |
| slo_type                   | name                        | double    | Facet                                                                                                                                                                                                                                          |
| facets                     | target                      | [object]  | SLO Target                                                                                                                                                                                                                                     |
| target                     | count                       | int64     | Count                                                                                                                                                                                                                                          |
| target                     | name                        | double    | Facet                                                                                                                                                                                                                                          |
| facets                     | team_tags                   | [object]  | Tags with the `team` tag key.                                                                                                                                                                                                                  |
| team_tags                  | count                       | int64     | Count                                                                                                                                                                                                                                          |
| team_tags                  | name                        | string    | Facet                                                                                                                                                                                                                                          |
| facets                     | timeframe                   | [object]  | Timeframes of SLOs.                                                                                                                                                                                                                            |
| timeframe                  | count                       | int64     | Count                                                                                                                                                                                                                                          |
| timeframe                  | name                        | string    | Facet                                                                                                                                                                                                                                          |
| attributes                 | slos                        | [object]  | SLOs                                                                                                                                                                                                                                           |
| slos                       | data                        | object    | A service level objective ID and attributes.                                                                                                                                                                                                   |
| data                       | attributes                  | object    | A service level objective object includes a service level indicator, thresholds for one or more timeframes, and metadata (`name`, `description`, and `tags`).                                                                                  |
| attributes                 | all_tags                    | [string]  | A list of tags associated with this service level objective. Always included in service level objective responses (but may be empty).                                                                                                          |
| attributes                 | created_at                  | int64     | Creation timestamp (UNIX time in seconds)                                                                                                                                                                                                      | Always included in service level objective responses.                                                         |
| attributes                 | creator                     | object    | The creator of the SLO                                                                                                                                                                                                                         |
| creator                    | email                       | string    | Email of the creator.                                                                                                                                                                                                                          |
| creator                    | id                          | int64     | User ID of the creator.                                                                                                                                                                                                                        |
| creator                    | name                        | string    | Name of the creator.                                                                                                                                                                                                                           |
| attributes                 | description                 | string    | A user-defined description of the service level objective.                                                                                                                                                                                     | Always included in service level objective responses (but may be `null`). Optional in create/update requests. |
| attributes                 | env_tags                    | [string]  | Tags with the `env` tag key.                                                                                                                                                                                                                   |
| attributes                 | groups                      | [string]  | A list of (up to 100) monitor groups that narrow the scope of a monitor service level objective. Included in service level objective responses if it is not empty.                                                                             |
| attributes                 | modified_at                 | int64     | Modification timestamp (UNIX time in seconds)                                                                                                                                                                                                  | Always included in service level objective responses.                                                         |
| attributes                 | monitor_ids                 | [integer] | A list of monitor ids that defines the scope of a monitor service level objective.                                                                                                                                                             |
| attributes                 | name                        | string    | The name of the service level objective object.                                                                                                                                                                                                |
| attributes                 | overall_status              | [object]  | calculated status and error budget remaining.                                                                                                                                                                                                  |
| overall_status             | error                       | string    | Error message if SLO status or error budget could not be calculated.                                                                                                                                                                           |
| overall_status             | error_budget_remaining      | double    | Remaining error budget of the SLO in percentage.                                                                                                                                                                                               |
| overall_status             | indexed_at                  | int64     | timestamp (UNIX time in seconds) of when the SLO status and error budget were calculated.                                                                                                                                                      |
| overall_status             | raw_error_budget_remaining  | object    | Error budget remaining for an SLO.                                                                                                                                                                                                             |
| raw_error_budget_remaining | unit                        | string    | Error budget remaining unit.                                                                                                                                                                                                                   |
| raw_error_budget_remaining | value                       | double    | Error budget remaining value.                                                                                                                                                                                                                  |
| overall_status             | span_precision              | int64     | The amount of decimal places the SLI value is accurate to.                                                                                                                                                                                     |
| overall_status             | state                       | enum      | State of the SLO. Allowed enum values: `breached,warning,ok,no_data`                                                                                                                                                                           |
| overall_status             | status                      | double    | The status of the SLO.                                                                                                                                                                                                                         |
| overall_status             | target                      | double    | The target of the SLO.                                                                                                                                                                                                                         |
| overall_status             | timeframe                   | enum      | The SLO time window options. Note that "custom" is not a valid option for creating or updating SLOs. It is only used when querying SLO history over custom timeframes. Allowed enum values: `7d,30d,90d,custom`                                |
| attributes                 | query                       | object    | A metric-based SLO. **Required if type is `metric`**. Note that Datadog only allows the sum by aggregator to be used because this will sum up all request counts instead of averaging them, or taking the max or min of all of those requests. |
| query                      | denominator                 | string    | A Datadog metric query for total (valid) events.                                                                                                                                                                                               |
| query                      | metrics                     | [string]  | Metric names used in the query's numerator and denominator. This field will return null and will be implemented in the next version of this endpoint.                                                                                          |
| query                      | numerator                   | string    | A Datadog metric query for good events.                                                                                                                                                                                                        |
| attributes                 | service_tags                | [string]  | Tags with the `service` tag key.                                                                                                                                                                                                               |
| attributes                 | slo_type                    | enum      | The type of the service level objective. Allowed enum values: `metric,monitor,time_slice`                                                                                                                                                      |
| attributes                 | status                      | object    | Status of the SLO's primary timeframe.                                                                                                                                                                                                         |
| status                     | calculation_error           | string    | Error message if SLO status or error budget could not be calculated.                                                                                                                                                                           |
| status                     | error_budget_remaining      | double    | Remaining error budget of the SLO in percentage.                                                                                                                                                                                               |
| status                     | indexed_at                  | int64     | timestamp (UNIX time in seconds) of when the SLO status and error budget were calculated.                                                                                                                                                      |
| status                     | raw_error_budget_remaining  | object    | Error budget remaining for an SLO.                                                                                                                                                                                                             |
| raw_error_budget_remaining | unit                        | string    | Error budget remaining unit.                                                                                                                                                                                                                   |
| raw_error_budget_remaining | value                       | double    | Error budget remaining value.                                                                                                                                                                                                                  |
| status                     | sli                         | double    | The current service level indicator (SLI) of the SLO, also known as 'status'. This is a percentage value from 0-100 (inclusive).                                                                                                               |
| status                     | span_precision              | int64     | The number of decimal places the SLI value is accurate to.                                                                                                                                                                                     |
| status                     | state                       | enum      | State of the SLO. Allowed enum values: `breached,warning,ok,no_data`                                                                                                                                                                           |
| attributes                 | team_tags                   | [string]  | Tags with the `team` tag key.                                                                                                                                                                                                                  |
| attributes                 | thresholds                  | [object]  | The thresholds (timeframes and associated targets) for this service level objective object.                                                                                                                                                    |
| thresholds                 | target [*required*]    | double    | The target value for the service level indicator within the corresponding timeframe.                                                                                                                                                           |
| thresholds                 | target_display              | string    | A string representation of the target that indicates its precision. It uses trailing zeros to show significant decimal places (for example `98.00`).                                                                                           | Always included in service level objective responses. Ignored in create/update requests.                      |
| thresholds                 | timeframe [*required*] | enum      | The SLO time window options. Allowed enum values: `7d,30d,90d`                                                                                                                                                                                 |
| thresholds                 | warning                     | double    | The warning value for the service level objective.                                                                                                                                                                                             |
| thresholds                 | warning_display             | string    | A string representation of the warning target (see the description of the `target_display` field for details).                                                                                                                                 | Included in service level objective responses if a warning target exists. Ignored in create/update requests.  |
| data                       | id                          | string    | A unique identifier for the service level objective object.                                                                                                                                                                                    | Always included in service level objective responses.                                                         |
| data                       | type                        | string    | The type of the object, must be `slo`.                                                                                                                                                                                                         |
| data                       | type                        | string    | Type of service level objective result.                                                                                                                                                                                                        |
|                            | links                       | object    | Pagination links.                                                                                                                                                                                                                              |
| links                      | first                       | string    | Link to last page.                                                                                                                                                                                                                             |
| links                      | last                        | string    | Link to first page.                                                                                                                                                                                                                            |
| links                      | next                        | string    | Link to the next page.                                                                                                                                                                                                                         |
| links                      | prev                        | string    | Link to previous page.                                                                                                                                                                                                                         |
| links                      | self                        | string    | Link to current page.                                                                                                                                                                                                                          |
|                            | meta                        | object    | Searches metadata returned by the API.                                                                                                                                                                                                         |
| meta                       | pagination                  | object    | Pagination metadata returned by the API.                                                                                                                                                                                                       |
| pagination                 | first_number                | int64     | The first number.                                                                                                                                                                                                                              |
| pagination                 | last_number                 | int64     | The last number.                                                                                                                                                                                                                               |
| pagination                 | next_number                 | int64     | The next number.                                                                                                                                                                                                                               |
| pagination                 | number                      | int64     | The page number.                                                                                                                                                                                                                               |
| pagination                 | prev_number                 | int64     | The previous page number.                                                                                                                                                                                                                      |
| pagination                 | size                        | int64     | The size of the response.                                                                                                                                                                                                                      |
| pagination                 | total                       | int64     | The total number of SLOs in the response.                                                                                                                                                                                                      |
| pagination                 | type                        | string    | Type of pagination.                                                                                                                                                                                                                            |

{% /tab %}

{% tab title="Example" %}

```json
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

{% /tab %}

{% /tab %}

{% tab title="400" %}
Bad Request
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
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/slo/search" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"
#####

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
#####

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"
{% /tab %}

## Get all SLOs{% #get-all-slos %}

{% tab title="v1" %}

| Datadog site      | API endpoint                                 |
| ----------------- | -------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v1/slo |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v1/slo |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v1/slo      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v1/slo      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v1/slo     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v1/slo |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v1/slo |

### Overview

Get a list of service level objective objects for your organization. This endpoint requires the `slos_read` permission.

OAuth apps require the `slos_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#service-level-objectives) to access this endpoint.

### Arguments

#### Query Strings

| Name          | Type    | Description                                                                |
| ------------- | ------- | -------------------------------------------------------------------------- |
| ids           | string  | A comma separated list of the IDs of the service level objectives objects. |
| query         | string  | The query string to filter results based on SLO names.                     |
| tags_query    | string  | The query string to filter results based on a single SLO tag.              |
| metrics_query | string  | The query string to filter results based on SLO numerator and denominator. |
| limit         | integer | The number of SLOs to return in the response.                              |
| offset        | integer | The specific offset to use as the beginning of the returned response.      |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
A response with one or more service level objective.

| Parent field         | Field                                  | Type            | Description                                                                                                                                                                                                                                                                                                                                                                   |
| -------------------- | -------------------------------------- | --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                      | data                                   | [object]        | An array of service level objective objects.                                                                                                                                                                                                                                                                                                                                  |
| data                 | created_at                             | int64           | Creation timestamp (UNIX time in seconds)                                                                                                                                                                                                                                                                                                                                     | Always included in service level objective responses.                                                                                                                                                               |
| data                 | creator                                | object          | Object describing the creator of the shared element.                                                                                                                                                                                                                                                                                                                          |
| creator              | email                                  | string          | Email of the creator.                                                                                                                                                                                                                                                                                                                                                         |
| creator              | handle                                 | string          | Handle of the creator.                                                                                                                                                                                                                                                                                                                                                        |
| creator              | name                                   | string          | Name of the creator.                                                                                                                                                                                                                                                                                                                                                          |
| data                 | description                            | string          | A user-defined description of the service level objective.                                                                                                                                                                                                                                                                                                                    | Always included in service level objective responses (but may be `null`). Optional in create/update requests.                                                                                                       |
| data                 | groups                                 | [string]        | A list of (up to 100) monitor groups that narrow the scope of a monitor service level objective.                                                                                                                                                                                                                                                                              | Included in service level objective responses if it is not empty. Optional in create/update requests for monitor service level objectives, but may only be used when then length of the `monitor_ids` field is one. |
| data                 | id                                     | string          | A unique identifier for the service level objective object.                                                                                                                                                                                                                                                                                                                   | Always included in service level objective responses.                                                                                                                                                               |
| data                 | modified_at                            | int64           | Modification timestamp (UNIX time in seconds)                                                                                                                                                                                                                                                                                                                                 | Always included in service level objective responses.                                                                                                                                                               |
| data                 | monitor_ids                            | [integer]       | A list of monitor ids that defines the scope of a monitor service level objective. **Required if type is `monitor`**.                                                                                                                                                                                                                                                         |
| data                 | monitor_tags                           | [string]        | The union of monitor tags for all monitors referenced by the `monitor_ids` field. Always included in service level objective responses for monitor-based service level objectives (but may be empty). Ignored in create/update requests. Does not affect which monitors are included in the service level objective (that is determined entirely by the `monitor_ids` field). |
| data                 | name [*required*]                 | string          | The name of the service level objective object.                                                                                                                                                                                                                                                                                                                               |
| data                 | query                                  | object          | A count-based (metric) SLO query. This field is superseded by `sli_specification` but is retained for backwards compatibility. Note that Datadog only allows the sum by aggregator to be used because this will sum up all request counts instead of averaging them, or taking the max or min of all of those requests.                                                       |
| query                | denominator [*required*]          | string          | A Datadog metric query for total (valid) events.                                                                                                                                                                                                                                                                                                                              |
| query                | numerator [*required*]            | string          | A Datadog metric query for good events.                                                                                                                                                                                                                                                                                                                                       |
| data                 | sli_specification                      |  <oneOf>   | A generic SLI specification. This is used for time-slice and count-based (metric) SLOs only.                                                                                                                                                                                                                                                                                  |
| sli_specification    | Option 1                               | object          | A time-slice SLI specification.                                                                                                                                                                                                                                                                                                                                               |
| Option 1             | time_slice [*required*]           | object          | The time-slice condition, composed of 3 parts: 1. the metric timeseries query, 2. the comparator, and 3. the threshold. Optionally, a fourth part, the query interval, can be provided.                                                                                                                                                                                       |
| time_slice           | comparator [*required*]           | enum            | The comparator used to compare the SLI value to the threshold. Allowed enum values: `>,>=,<,<=`                                                                                                                                                                                                                                                                               |
| time_slice           | query [*required*]                | object          | The queries and formula used to calculate the SLI value.                                                                                                                                                                                                                                                                                                                      |
| query                | formulas [*required*]             | [object]        | A list that contains exactly one formula, as only a single formula may be used in a time-slice SLO.                                                                                                                                                                                                                                                                           |
| formulas             | formula [*required*]              | string          | The formula string, which is an expression involving named queries.                                                                                                                                                                                                                                                                                                           |
| query                | queries [*required*]              | [ <oneOf>] | A list of queries that are used to calculate the SLI value.                                                                                                                                                                                                                                                                                                                   |
| queries              | Option 1                               | object          | A formula and functions metrics query.                                                                                                                                                                                                                                                                                                                                        |
| Option 1             | aggregator                             | enum            | The aggregation methods available for metrics queries. Allowed enum values: `avg,min,max,sum,last,area,l2norm,percentile`                                                                                                                                                                                                                                                     |
| Option 1             | cross_org_uuids                        | [string]        | The source organization UUID for cross organization queries. Feature in Private Beta.                                                                                                                                                                                                                                                                                         |
| Option 1             | data_source [*required*]          | enum            | Data source for metrics queries. Allowed enum values: `metrics`                                                                                                                                                                                                                                                                                                               |
| Option 1             | name [*required*]                 | string          | Name of the query for use in formulas.                                                                                                                                                                                                                                                                                                                                        |
| Option 1             | query [*required*]                | string          | Metrics query definition.                                                                                                                                                                                                                                                                                                                                                     |
| Option 1             | semantic_mode                          | enum            | Semantic mode for metrics queries. This determines how metrics from different sources are combined or displayed. Allowed enum values: `combined,native`                                                                                                                                                                                                                       |
| time_slice           | query_interval_seconds                 | enum            | The interval used when querying data, which defines the size of a time slice. Two values are allowed: 60 (1 minute) and 300 (5 minutes). If not provided, the value defaults to 300 (5 minutes). Allowed enum values: `60,300`                                                                                                                                                |
| time_slice           | threshold [*required*]            | double          | The threshold value to which each SLI value will be compared.                                                                                                                                                                                                                                                                                                                 |
| sli_specification    | Option 2                               | object          | A metric SLI specification.                                                                                                                                                                                                                                                                                                                                                   |
| Option 2             | count [*required*]                | object          | A count-based (metric) SLI specification, composed of three parts: the good events formula, the total events formula, and the underlying queries.                                                                                                                                                                                                                             |
| count                | good_events_formula [*required*]  | object          | A formula that specifies how to combine the results of multiple queries.                                                                                                                                                                                                                                                                                                      |
| good_events_formula  | formula [*required*]              | string          | The formula string, which is an expression involving named queries.                                                                                                                                                                                                                                                                                                           |
| count                | queries [*required*]              | [ <oneOf>] |
| queries              | Option 1                               | object          | A formula and functions metrics query.                                                                                                                                                                                                                                                                                                                                        |
| Option 1             | aggregator                             | enum            | The aggregation methods available for metrics queries. Allowed enum values: `avg,min,max,sum,last,area,l2norm,percentile`                                                                                                                                                                                                                                                     |
| Option 1             | cross_org_uuids                        | [string]        | The source organization UUID for cross organization queries. Feature in Private Beta.                                                                                                                                                                                                                                                                                         |
| Option 1             | data_source [*required*]          | enum            | Data source for metrics queries. Allowed enum values: `metrics`                                                                                                                                                                                                                                                                                                               |
| Option 1             | name [*required*]                 | string          | Name of the query for use in formulas.                                                                                                                                                                                                                                                                                                                                        |
| Option 1             | query [*required*]                | string          | Metrics query definition.                                                                                                                                                                                                                                                                                                                                                     |
| Option 1             | semantic_mode                          | enum            | Semantic mode for metrics queries. This determines how metrics from different sources are combined or displayed. Allowed enum values: `combined,native`                                                                                                                                                                                                                       |
| count                | total_events_formula [*required*] | object          | A formula that specifies how to combine the results of multiple queries.                                                                                                                                                                                                                                                                                                      |
| total_events_formula | formula [*required*]              | string          | The formula string, which is an expression involving named queries.                                                                                                                                                                                                                                                                                                           |
| data                 | tags                                   | [string]        | A list of tags associated with this service level objective. Always included in service level objective responses (but may be empty). Optional in create/update requests.                                                                                                                                                                                                     |
| data                 | target_threshold                       | double          | The target threshold such that when the service level indicator is above this threshold over the given timeframe, the objective is being met.                                                                                                                                                                                                                                 |
| data                 | thresholds [*required*]           | [object]        | The thresholds (timeframes and associated targets) for this service level objective object.                                                                                                                                                                                                                                                                                   |
| thresholds           | target [*required*]               | double          | The target value for the service level indicator within the corresponding timeframe.                                                                                                                                                                                                                                                                                          |
| thresholds           | target_display                         | string          | A string representation of the target that indicates its precision. It uses trailing zeros to show significant decimal places (for example `98.00`).                                                                                                                                                                                                                          | Always included in service level objective responses. Ignored in create/update requests.                                                                                                                            |
| thresholds           | timeframe [*required*]            | enum            | The SLO time window options. Note that "custom" is not a valid option for creating or updating SLOs. It is only used when querying SLO history over custom timeframes. Allowed enum values: `7d,30d,90d,custom`                                                                                                                                                               |
| thresholds           | warning                                | double          | The warning value for the service level objective.                                                                                                                                                                                                                                                                                                                            |
| thresholds           | warning_display                        | string          | A string representation of the warning target (see the description of the `target_display` field for details).                                                                                                                                                                                                                                                                | Included in service level objective responses if a warning target exists. Ignored in create/update requests.                                                                                                        |
| data                 | timeframe                              | enum            | The SLO time window options. Note that "custom" is not a valid option for creating or updating SLOs. It is only used when querying SLO history over custom timeframes. Allowed enum values: `7d,30d,90d,custom`                                                                                                                                                               |
| data                 | type [*required*]                 | enum            | The type of the service level objective. Allowed enum values: `metric,monitor,time_slice`                                                                                                                                                                                                                                                                                     |
| data                 | warning_threshold                      | double          | The optional warning threshold such that when the service level indicator is below this value for the given threshold, but above the target threshold, the objective appears in a "warning" state. This value must be greater than the target threshold.                                                                                                                      |
|                      | errors                                 | [string]        | An array of error messages. Each endpoint documents how/whether this field is used.                                                                                                                                                                                                                                                                                           |
|                      | metadata                               | object          | The metadata object containing additional information about the list of SLOs.                                                                                                                                                                                                                                                                                                 |
| metadata             | page                                   | object          | The object containing information about the pages of the list of SLOs.                                                                                                                                                                                                                                                                                                        |
| page                 | total_count                            | int64           | The total number of resources that could be retrieved ignoring the parameters and filters in the request.                                                                                                                                                                                                                                                                     |
| page                 | total_filtered_count                   | int64           | The total number of resources that match the parameters and filters in the request. This attribute can be used by a client to determine the total number of pages.                                                                                                                                                                                                            |

{% /tab %}

{% tab title="Example" %}

```json
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

{% /tab %}

{% /tab %}

{% tab title="400" %}
Bad Request
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

{% tab title="404" %}
Not Found
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
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/slo" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```ruby
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby-legacy) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"
#####

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python-legacy) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python "example.py"
#####

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
#####

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"
{% /tab %}

## Update an SLO{% #update-an-slo %}

{% tab title="v1" %}

| Datadog site      | API endpoint                                          |
| ----------------- | ----------------------------------------------------- |
| ap1.datadoghq.com | PUT https://api.ap1.datadoghq.com/api/v1/slo/{slo_id} |
| ap2.datadoghq.com | PUT https://api.ap2.datadoghq.com/api/v1/slo/{slo_id} |
| app.datadoghq.eu  | PUT https://api.datadoghq.eu/api/v1/slo/{slo_id}      |
| app.ddog-gov.com  | PUT https://api.ddog-gov.com/api/v1/slo/{slo_id}      |
| app.datadoghq.com | PUT https://api.datadoghq.com/api/v1/slo/{slo_id}     |
| us3.datadoghq.com | PUT https://api.us3.datadoghq.com/api/v1/slo/{slo_id} |
| us5.datadoghq.com | PUT https://api.us5.datadoghq.com/api/v1/slo/{slo_id} |

### Overview

Update the specified service level objective object. This endpoint requires the `slos_write` permission.

OAuth apps require the `slos_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#service-level-objectives) to access this endpoint.

### Arguments

#### Path Parameters

| Name                     | Type   | Description                                   |
| ------------------------ | ------ | --------------------------------------------- |
| slo_id [*required*] | string | The ID of the service level objective object. |

### Request

#### Body Data (required)

The edited service level objective request object.

{% tab title="Model" %}

| Parent field         | Field                                  | Type            | Description                                                                                                                                                                                                                                                                                                                                                                   |
| -------------------- | -------------------------------------- | --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                      | created_at                             | int64           | Creation timestamp (UNIX time in seconds)                                                                                                                                                                                                                                                                                                                                     | Always included in service level objective responses.                                                                                                                                                               |
|                      | creator                                | object          | Object describing the creator of the shared element.                                                                                                                                                                                                                                                                                                                          |
| creator              | email                                  | string          | Email of the creator.                                                                                                                                                                                                                                                                                                                                                         |
| creator              | handle                                 | string          | Handle of the creator.                                                                                                                                                                                                                                                                                                                                                        |
| creator              | name                                   | string          | Name of the creator.                                                                                                                                                                                                                                                                                                                                                          |
|                      | description                            | string          | A user-defined description of the service level objective.                                                                                                                                                                                                                                                                                                                    | Always included in service level objective responses (but may be `null`). Optional in create/update requests.                                                                                                       |
|                      | groups                                 | [string]        | A list of (up to 100) monitor groups that narrow the scope of a monitor service level objective.                                                                                                                                                                                                                                                                              | Included in service level objective responses if it is not empty. Optional in create/update requests for monitor service level objectives, but may only be used when then length of the `monitor_ids` field is one. |
|                      | id                                     | string          | A unique identifier for the service level objective object.                                                                                                                                                                                                                                                                                                                   | Always included in service level objective responses.                                                                                                                                                               |
|                      | modified_at                            | int64           | Modification timestamp (UNIX time in seconds)                                                                                                                                                                                                                                                                                                                                 | Always included in service level objective responses.                                                                                                                                                               |
|                      | monitor_ids                            | [integer]       | A list of monitor ids that defines the scope of a monitor service level objective. **Required if type is `monitor`**.                                                                                                                                                                                                                                                         |
|                      | monitor_tags                           | [string]        | The union of monitor tags for all monitors referenced by the `monitor_ids` field. Always included in service level objective responses for monitor-based service level objectives (but may be empty). Ignored in create/update requests. Does not affect which monitors are included in the service level objective (that is determined entirely by the `monitor_ids` field). |
|                      | name [*required*]                 | string          | The name of the service level objective object.                                                                                                                                                                                                                                                                                                                               |
|                      | query                                  | object          | A count-based (metric) SLO query. This field is superseded by `sli_specification` but is retained for backwards compatibility. Note that Datadog only allows the sum by aggregator to be used because this will sum up all request counts instead of averaging them, or taking the max or min of all of those requests.                                                       |
| query                | denominator [*required*]          | string          | A Datadog metric query for total (valid) events.                                                                                                                                                                                                                                                                                                                              |
| query                | numerator [*required*]            | string          | A Datadog metric query for good events.                                                                                                                                                                                                                                                                                                                                       |
|                      | sli_specification                      |  <oneOf>   | A generic SLI specification. This is used for time-slice and count-based (metric) SLOs only.                                                                                                                                                                                                                                                                                  |
| sli_specification    | Option 1                               | object          | A time-slice SLI specification.                                                                                                                                                                                                                                                                                                                                               |
| Option 1             | time_slice [*required*]           | object          | The time-slice condition, composed of 3 parts: 1. the metric timeseries query, 2. the comparator, and 3. the threshold. Optionally, a fourth part, the query interval, can be provided.                                                                                                                                                                                       |
| time_slice           | comparator [*required*]           | enum            | The comparator used to compare the SLI value to the threshold. Allowed enum values: `>,>=,<,<=`                                                                                                                                                                                                                                                                               |
| time_slice           | query [*required*]                | object          | The queries and formula used to calculate the SLI value.                                                                                                                                                                                                                                                                                                                      |
| query                | formulas [*required*]             | [object]        | A list that contains exactly one formula, as only a single formula may be used in a time-slice SLO.                                                                                                                                                                                                                                                                           |
| formulas             | formula [*required*]              | string          | The formula string, which is an expression involving named queries.                                                                                                                                                                                                                                                                                                           |
| query                | queries [*required*]              | [ <oneOf>] | A list of queries that are used to calculate the SLI value.                                                                                                                                                                                                                                                                                                                   |
| queries              | Option 1                               | object          | A formula and functions metrics query.                                                                                                                                                                                                                                                                                                                                        |
| Option 1             | aggregator                             | enum            | The aggregation methods available for metrics queries. Allowed enum values: `avg,min,max,sum,last,area,l2norm,percentile`                                                                                                                                                                                                                                                     |
| Option 1             | cross_org_uuids                        | [string]        | The source organization UUID for cross organization queries. Feature in Private Beta.                                                                                                                                                                                                                                                                                         |
| Option 1             | data_source [*required*]          | enum            | Data source for metrics queries. Allowed enum values: `metrics`                                                                                                                                                                                                                                                                                                               |
| Option 1             | name [*required*]                 | string          | Name of the query for use in formulas.                                                                                                                                                                                                                                                                                                                                        |
| Option 1             | query [*required*]                | string          | Metrics query definition.                                                                                                                                                                                                                                                                                                                                                     |
| Option 1             | semantic_mode                          | enum            | Semantic mode for metrics queries. This determines how metrics from different sources are combined or displayed. Allowed enum values: `combined,native`                                                                                                                                                                                                                       |
| time_slice           | query_interval_seconds                 | enum            | The interval used when querying data, which defines the size of a time slice. Two values are allowed: 60 (1 minute) and 300 (5 minutes). If not provided, the value defaults to 300 (5 minutes). Allowed enum values: `60,300`                                                                                                                                                |
| time_slice           | threshold [*required*]            | double          | The threshold value to which each SLI value will be compared.                                                                                                                                                                                                                                                                                                                 |
| sli_specification    | Option 2                               | object          | A metric SLI specification.                                                                                                                                                                                                                                                                                                                                                   |
| Option 2             | count [*required*]                | object          | A count-based (metric) SLI specification, composed of three parts: the good events formula, the total events formula, and the underlying queries.                                                                                                                                                                                                                             |
| count                | good_events_formula [*required*]  | object          | A formula that specifies how to combine the results of multiple queries.                                                                                                                                                                                                                                                                                                      |
| good_events_formula  | formula [*required*]              | string          | The formula string, which is an expression involving named queries.                                                                                                                                                                                                                                                                                                           |
| count                | queries [*required*]              | [ <oneOf>] |
| queries              | Option 1                               | object          | A formula and functions metrics query.                                                                                                                                                                                                                                                                                                                                        |
| Option 1             | aggregator                             | enum            | The aggregation methods available for metrics queries. Allowed enum values: `avg,min,max,sum,last,area,l2norm,percentile`                                                                                                                                                                                                                                                     |
| Option 1             | cross_org_uuids                        | [string]        | The source organization UUID for cross organization queries. Feature in Private Beta.                                                                                                                                                                                                                                                                                         |
| Option 1             | data_source [*required*]          | enum            | Data source for metrics queries. Allowed enum values: `metrics`                                                                                                                                                                                                                                                                                                               |
| Option 1             | name [*required*]                 | string          | Name of the query for use in formulas.                                                                                                                                                                                                                                                                                                                                        |
| Option 1             | query [*required*]                | string          | Metrics query definition.                                                                                                                                                                                                                                                                                                                                                     |
| Option 1             | semantic_mode                          | enum            | Semantic mode for metrics queries. This determines how metrics from different sources are combined or displayed. Allowed enum values: `combined,native`                                                                                                                                                                                                                       |
| count                | total_events_formula [*required*] | object          | A formula that specifies how to combine the results of multiple queries.                                                                                                                                                                                                                                                                                                      |
| total_events_formula | formula [*required*]              | string          | The formula string, which is an expression involving named queries.                                                                                                                                                                                                                                                                                                           |
|                      | tags                                   | [string]        | A list of tags associated with this service level objective. Always included in service level objective responses (but may be empty). Optional in create/update requests.                                                                                                                                                                                                     |
|                      | target_threshold                       | double          | The target threshold such that when the service level indicator is above this threshold over the given timeframe, the objective is being met.                                                                                                                                                                                                                                 |
|                      | thresholds [*required*]           | [object]        | The thresholds (timeframes and associated targets) for this service level objective object.                                                                                                                                                                                                                                                                                   |
| thresholds           | target [*required*]               | double          | The target value for the service level indicator within the corresponding timeframe.                                                                                                                                                                                                                                                                                          |
| thresholds           | target_display                         | string          | A string representation of the target that indicates its precision. It uses trailing zeros to show significant decimal places (for example `98.00`).                                                                                                                                                                                                                          | Always included in service level objective responses. Ignored in create/update requests.                                                                                                                            |
| thresholds           | timeframe [*required*]            | enum            | The SLO time window options. Note that "custom" is not a valid option for creating or updating SLOs. It is only used when querying SLO history over custom timeframes. Allowed enum values: `7d,30d,90d,custom`                                                                                                                                                               |
| thresholds           | warning                                | double          | The warning value for the service level objective.                                                                                                                                                                                                                                                                                                                            |
| thresholds           | warning_display                        | string          | A string representation of the warning target (see the description of the `target_display` field for details).                                                                                                                                                                                                                                                                | Included in service level objective responses if a warning target exists. Ignored in create/update requests.                                                                                                        |
|                      | timeframe                              | enum            | The SLO time window options. Note that "custom" is not a valid option for creating or updating SLOs. It is only used when querying SLO history over custom timeframes. Allowed enum values: `7d,30d,90d,custom`                                                                                                                                                               |
|                      | type [*required*]                 | enum            | The type of the service level objective. Allowed enum values: `metric,monitor,time_slice`                                                                                                                                                                                                                                                                                     |
|                      | warning_threshold                      | double          | The optional warning threshold such that when the service level indicator is below this value for the given threshold, but above the target threshold, the objective appears in a "warning" state. This value must be greater than the target threshold.                                                                                                                      |

{% /tab %}

{% tab title="Example" %}

```json
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

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
A response with one or more service level objective.

| Parent field         | Field                                  | Type            | Description                                                                                                                                                                                                                                                                                                                                                                   |
| -------------------- | -------------------------------------- | --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                      | data                                   | [object]        | An array of service level objective objects.                                                                                                                                                                                                                                                                                                                                  |
| data                 | created_at                             | int64           | Creation timestamp (UNIX time in seconds)                                                                                                                                                                                                                                                                                                                                     | Always included in service level objective responses.                                                                                                                                                               |
| data                 | creator                                | object          | Object describing the creator of the shared element.                                                                                                                                                                                                                                                                                                                          |
| creator              | email                                  | string          | Email of the creator.                                                                                                                                                                                                                                                                                                                                                         |
| creator              | handle                                 | string          | Handle of the creator.                                                                                                                                                                                                                                                                                                                                                        |
| creator              | name                                   | string          | Name of the creator.                                                                                                                                                                                                                                                                                                                                                          |
| data                 | description                            | string          | A user-defined description of the service level objective.                                                                                                                                                                                                                                                                                                                    | Always included in service level objective responses (but may be `null`). Optional in create/update requests.                                                                                                       |
| data                 | groups                                 | [string]        | A list of (up to 100) monitor groups that narrow the scope of a monitor service level objective.                                                                                                                                                                                                                                                                              | Included in service level objective responses if it is not empty. Optional in create/update requests for monitor service level objectives, but may only be used when then length of the `monitor_ids` field is one. |
| data                 | id                                     | string          | A unique identifier for the service level objective object.                                                                                                                                                                                                                                                                                                                   | Always included in service level objective responses.                                                                                                                                                               |
| data                 | modified_at                            | int64           | Modification timestamp (UNIX time in seconds)                                                                                                                                                                                                                                                                                                                                 | Always included in service level objective responses.                                                                                                                                                               |
| data                 | monitor_ids                            | [integer]       | A list of monitor ids that defines the scope of a monitor service level objective. **Required if type is `monitor`**.                                                                                                                                                                                                                                                         |
| data                 | monitor_tags                           | [string]        | The union of monitor tags for all monitors referenced by the `monitor_ids` field. Always included in service level objective responses for monitor-based service level objectives (but may be empty). Ignored in create/update requests. Does not affect which monitors are included in the service level objective (that is determined entirely by the `monitor_ids` field). |
| data                 | name [*required*]                 | string          | The name of the service level objective object.                                                                                                                                                                                                                                                                                                                               |
| data                 | query                                  | object          | A count-based (metric) SLO query. This field is superseded by `sli_specification` but is retained for backwards compatibility. Note that Datadog only allows the sum by aggregator to be used because this will sum up all request counts instead of averaging them, or taking the max or min of all of those requests.                                                       |
| query                | denominator [*required*]          | string          | A Datadog metric query for total (valid) events.                                                                                                                                                                                                                                                                                                                              |
| query                | numerator [*required*]            | string          | A Datadog metric query for good events.                                                                                                                                                                                                                                                                                                                                       |
| data                 | sli_specification                      |  <oneOf>   | A generic SLI specification. This is used for time-slice and count-based (metric) SLOs only.                                                                                                                                                                                                                                                                                  |
| sli_specification    | Option 1                               | object          | A time-slice SLI specification.                                                                                                                                                                                                                                                                                                                                               |
| Option 1             | time_slice [*required*]           | object          | The time-slice condition, composed of 3 parts: 1. the metric timeseries query, 2. the comparator, and 3. the threshold. Optionally, a fourth part, the query interval, can be provided.                                                                                                                                                                                       |
| time_slice           | comparator [*required*]           | enum            | The comparator used to compare the SLI value to the threshold. Allowed enum values: `>,>=,<,<=`                                                                                                                                                                                                                                                                               |
| time_slice           | query [*required*]                | object          | The queries and formula used to calculate the SLI value.                                                                                                                                                                                                                                                                                                                      |
| query                | formulas [*required*]             | [object]        | A list that contains exactly one formula, as only a single formula may be used in a time-slice SLO.                                                                                                                                                                                                                                                                           |
| formulas             | formula [*required*]              | string          | The formula string, which is an expression involving named queries.                                                                                                                                                                                                                                                                                                           |
| query                | queries [*required*]              | [ <oneOf>] | A list of queries that are used to calculate the SLI value.                                                                                                                                                                                                                                                                                                                   |
| queries              | Option 1                               | object          | A formula and functions metrics query.                                                                                                                                                                                                                                                                                                                                        |
| Option 1             | aggregator                             | enum            | The aggregation methods available for metrics queries. Allowed enum values: `avg,min,max,sum,last,area,l2norm,percentile`                                                                                                                                                                                                                                                     |
| Option 1             | cross_org_uuids                        | [string]        | The source organization UUID for cross organization queries. Feature in Private Beta.                                                                                                                                                                                                                                                                                         |
| Option 1             | data_source [*required*]          | enum            | Data source for metrics queries. Allowed enum values: `metrics`                                                                                                                                                                                                                                                                                                               |
| Option 1             | name [*required*]                 | string          | Name of the query for use in formulas.                                                                                                                                                                                                                                                                                                                                        |
| Option 1             | query [*required*]                | string          | Metrics query definition.                                                                                                                                                                                                                                                                                                                                                     |
| Option 1             | semantic_mode                          | enum            | Semantic mode for metrics queries. This determines how metrics from different sources are combined or displayed. Allowed enum values: `combined,native`                                                                                                                                                                                                                       |
| time_slice           | query_interval_seconds                 | enum            | The interval used when querying data, which defines the size of a time slice. Two values are allowed: 60 (1 minute) and 300 (5 minutes). If not provided, the value defaults to 300 (5 minutes). Allowed enum values: `60,300`                                                                                                                                                |
| time_slice           | threshold [*required*]            | double          | The threshold value to which each SLI value will be compared.                                                                                                                                                                                                                                                                                                                 |
| sli_specification    | Option 2                               | object          | A metric SLI specification.                                                                                                                                                                                                                                                                                                                                                   |
| Option 2             | count [*required*]                | object          | A count-based (metric) SLI specification, composed of three parts: the good events formula, the total events formula, and the underlying queries.                                                                                                                                                                                                                             |
| count                | good_events_formula [*required*]  | object          | A formula that specifies how to combine the results of multiple queries.                                                                                                                                                                                                                                                                                                      |
| good_events_formula  | formula [*required*]              | string          | The formula string, which is an expression involving named queries.                                                                                                                                                                                                                                                                                                           |
| count                | queries [*required*]              | [ <oneOf>] |
| queries              | Option 1                               | object          | A formula and functions metrics query.                                                                                                                                                                                                                                                                                                                                        |
| Option 1             | aggregator                             | enum            | The aggregation methods available for metrics queries. Allowed enum values: `avg,min,max,sum,last,area,l2norm,percentile`                                                                                                                                                                                                                                                     |
| Option 1             | cross_org_uuids                        | [string]        | The source organization UUID for cross organization queries. Feature in Private Beta.                                                                                                                                                                                                                                                                                         |
| Option 1             | data_source [*required*]          | enum            | Data source for metrics queries. Allowed enum values: `metrics`                                                                                                                                                                                                                                                                                                               |
| Option 1             | name [*required*]                 | string          | Name of the query for use in formulas.                                                                                                                                                                                                                                                                                                                                        |
| Option 1             | query [*required*]                | string          | Metrics query definition.                                                                                                                                                                                                                                                                                                                                                     |
| Option 1             | semantic_mode                          | enum            | Semantic mode for metrics queries. This determines how metrics from different sources are combined or displayed. Allowed enum values: `combined,native`                                                                                                                                                                                                                       |
| count                | total_events_formula [*required*] | object          | A formula that specifies how to combine the results of multiple queries.                                                                                                                                                                                                                                                                                                      |
| total_events_formula | formula [*required*]              | string          | The formula string, which is an expression involving named queries.                                                                                                                                                                                                                                                                                                           |
| data                 | tags                                   | [string]        | A list of tags associated with this service level objective. Always included in service level objective responses (but may be empty). Optional in create/update requests.                                                                                                                                                                                                     |
| data                 | target_threshold                       | double          | The target threshold such that when the service level indicator is above this threshold over the given timeframe, the objective is being met.                                                                                                                                                                                                                                 |
| data                 | thresholds [*required*]           | [object]        | The thresholds (timeframes and associated targets) for this service level objective object.                                                                                                                                                                                                                                                                                   |
| thresholds           | target [*required*]               | double          | The target value for the service level indicator within the corresponding timeframe.                                                                                                                                                                                                                                                                                          |
| thresholds           | target_display                         | string          | A string representation of the target that indicates its precision. It uses trailing zeros to show significant decimal places (for example `98.00`).                                                                                                                                                                                                                          | Always included in service level objective responses. Ignored in create/update requests.                                                                                                                            |
| thresholds           | timeframe [*required*]            | enum            | The SLO time window options. Note that "custom" is not a valid option for creating or updating SLOs. It is only used when querying SLO history over custom timeframes. Allowed enum values: `7d,30d,90d,custom`                                                                                                                                                               |
| thresholds           | warning                                | double          | The warning value for the service level objective.                                                                                                                                                                                                                                                                                                                            |
| thresholds           | warning_display                        | string          | A string representation of the warning target (see the description of the `target_display` field for details).                                                                                                                                                                                                                                                                | Included in service level objective responses if a warning target exists. Ignored in create/update requests.                                                                                                        |
| data                 | timeframe                              | enum            | The SLO time window options. Note that "custom" is not a valid option for creating or updating SLOs. It is only used when querying SLO history over custom timeframes. Allowed enum values: `7d,30d,90d,custom`                                                                                                                                                               |
| data                 | type [*required*]                 | enum            | The type of the service level objective. Allowed enum values: `metric,monitor,time_slice`                                                                                                                                                                                                                                                                                     |
| data                 | warning_threshold                      | double          | The optional warning threshold such that when the service level indicator is below this value for the given threshold, but above the target threshold, the objective appears in a "warning" state. This value must be greater than the target threshold.                                                                                                                      |
|                      | errors                                 | [string]        | An array of error messages. Each endpoint documents how/whether this field is used.                                                                                                                                                                                                                                                                                           |
|                      | metadata                               | object          | The metadata object containing additional information about the list of SLOs.                                                                                                                                                                                                                                                                                                 |
| metadata             | page                                   | object          | The object containing information about the pages of the list of SLOs.                                                                                                                                                                                                                                                                                                        |
| page                 | total_count                            | int64           | The total number of resources that could be retrieved ignoring the parameters and filters in the request.                                                                                                                                                                                                                                                                     |
| page                 | total_filtered_count                   | int64           | The total number of resources that match the parameters and filters in the request. This attribute can be used by a client to determine the total number of pages.                                                                                                                                                                                                            |

{% /tab %}

{% tab title="Example" %}

```json
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

{% /tab %}

{% /tab %}

{% tab title="400" %}
Bad Request
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

{% tab title="404" %}
Not Found
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
                          \# Path parametersexport slo_id="CHANGE_ME"\# Curl commandcurl -X PUT "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/slo/${slo_id}" \
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

#####

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"
#####

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
#####

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"
{% /tab %}

## Get an SLO's details{% #get-an-slos-details %}

{% tab title="v1" %}

| Datadog site      | API endpoint                                          |
| ----------------- | ----------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v1/slo/{slo_id} |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v1/slo/{slo_id} |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v1/slo/{slo_id}      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v1/slo/{slo_id}      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v1/slo/{slo_id}     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v1/slo/{slo_id} |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v1/slo/{slo_id} |

### Overview

Get a service level objective object. This endpoint requires the `slos_read` permission.

OAuth apps require the `slos_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#service-level-objectives) to access this endpoint.

### Arguments

#### Path Parameters

| Name                     | Type   | Description                                   |
| ------------------------ | ------ | --------------------------------------------- |
| slo_id [*required*] | string | The ID of the service level objective object. |

#### Query Strings

| Name                      | Type    | Description                                          |
| ------------------------- | ------- | ---------------------------------------------------- |
| with_configured_alert_ids | boolean | Get the IDs of SLO monitors that reference this SLO. |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
A service level objective response containing a single service level objective.

| Parent field         | Field                                  | Type            | Description                                                                                                                                                                                                                                                                                                                                                             |
| -------------------- | -------------------------------------- | --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                      | data                                   | object          | A service level objective object includes a service level indicator, thresholds for one or more timeframes, and metadata (`name`, `description`, `tags`, etc.).                                                                                                                                                                                                         |
| data                 | configured_alert_ids                   | [integer]       | A list of SLO monitors IDs that reference this SLO. This field is returned only when `with_configured_alert_ids` parameter is true in query.                                                                                                                                                                                                                            |
| data                 | created_at                             | int64           | Creation timestamp (UNIX time in seconds)                                                                                                                                                                                                                                                                                                                               | Always included in service level objective responses.                                                                                                                                                               |
| data                 | creator                                | object          | Object describing the creator of the shared element.                                                                                                                                                                                                                                                                                                                    |
| creator              | email                                  | string          | Email of the creator.                                                                                                                                                                                                                                                                                                                                                   |
| creator              | handle                                 | string          | Handle of the creator.                                                                                                                                                                                                                                                                                                                                                  |
| creator              | name                                   | string          | Name of the creator.                                                                                                                                                                                                                                                                                                                                                    |
| data                 | description                            | string          | A user-defined description of the service level objective.                                                                                                                                                                                                                                                                                                              | Always included in service level objective responses (but may be `null`). Optional in create/update requests.                                                                                                       |
| data                 | groups                                 | [string]        | A list of (up to 20) monitor groups that narrow the scope of a monitor service level objective.                                                                                                                                                                                                                                                                         | Included in service level objective responses if it is not empty. Optional in create/update requests for monitor service level objectives, but may only be used when then length of the `monitor_ids` field is one. |
| data                 | id                                     | string          | A unique identifier for the service level objective object.                                                                                                                                                                                                                                                                                                             | Always included in service level objective responses.                                                                                                                                                               |
| data                 | modified_at                            | int64           | Modification timestamp (UNIX time in seconds)                                                                                                                                                                                                                                                                                                                           | Always included in service level objective responses.                                                                                                                                                               |
| data                 | monitor_ids                            | [integer]       | A list of monitor ids that defines the scope of a monitor service level objective. **Required if type is `monitor`**.                                                                                                                                                                                                                                                   |
| data                 | monitor_tags                           | [string]        | The union of monitor tags for all monitors referenced by the `monitor_ids` field. Always included in service level objective responses for monitor service level objectives (but may be empty). Ignored in create/update requests. Does not affect which monitors are included in the service level objective (that is determined entirely by the `monitor_ids` field). |
| data                 | name                                   | string          | The name of the service level objective object.                                                                                                                                                                                                                                                                                                                         |
| data                 | query                                  | object          | The metric query used to define a count-based SLO as the ratio of good events to total events.                                                                                                                                                                                                                                                                          |
| query                | denominator [*required*]          | string          | A Datadog metric query for total (valid) events.                                                                                                                                                                                                                                                                                                                        |
| query                | numerator [*required*]            | string          | A Datadog metric query for good events.                                                                                                                                                                                                                                                                                                                                 |
| data                 | sli_specification                      |  <oneOf>   | A generic SLI specification. This is currently used for time-slice and count-based (metric) SLOs only.                                                                                                                                                                                                                                                                  |
| sli_specification    | Option 1                               | object          | A time-slice SLI specification.                                                                                                                                                                                                                                                                                                                                         |
| Option 1             | time_slice [*required*]           | object          | The time-slice condition, composed of 3 parts: 1. the metric timeseries query, 2. the comparator, and 3. the threshold. Optionally, a fourth part, the query interval, can be provided.                                                                                                                                                                                 |
| time_slice           | comparator [*required*]           | enum            | The comparator used to compare the SLI value to the threshold. Allowed enum values: `>,>=,<,<=`                                                                                                                                                                                                                                                                         |
| time_slice           | query [*required*]                | object          | The queries and formula used to calculate the SLI value.                                                                                                                                                                                                                                                                                                                |
| query                | formulas [*required*]             | [object]        | A list that contains exactly one formula, as only a single formula may be used in a time-slice SLO.                                                                                                                                                                                                                                                                     |
| formulas             | formula [*required*]              | string          | The formula string, which is an expression involving named queries.                                                                                                                                                                                                                                                                                                     |
| query                | queries [*required*]              | [ <oneOf>] | A list of queries that are used to calculate the SLI value.                                                                                                                                                                                                                                                                                                             |
| queries              | Option 1                               | object          | A formula and functions metrics query.                                                                                                                                                                                                                                                                                                                                  |
| Option 1             | aggregator                             | enum            | The aggregation methods available for metrics queries. Allowed enum values: `avg,min,max,sum,last,area,l2norm,percentile`                                                                                                                                                                                                                                               |
| Option 1             | cross_org_uuids                        | [string]        | The source organization UUID for cross organization queries. Feature in Private Beta.                                                                                                                                                                                                                                                                                   |
| Option 1             | data_source [*required*]          | enum            | Data source for metrics queries. Allowed enum values: `metrics`                                                                                                                                                                                                                                                                                                         |
| Option 1             | name [*required*]                 | string          | Name of the query for use in formulas.                                                                                                                                                                                                                                                                                                                                  |
| Option 1             | query [*required*]                | string          | Metrics query definition.                                                                                                                                                                                                                                                                                                                                               |
| Option 1             | semantic_mode                          | enum            | Semantic mode for metrics queries. This determines how metrics from different sources are combined or displayed. Allowed enum values: `combined,native`                                                                                                                                                                                                                 |
| time_slice           | query_interval_seconds                 | enum            | The interval used when querying data, which defines the size of a time slice. Two values are allowed: 60 (1 minute) and 300 (5 minutes). If not provided, the value defaults to 300 (5 minutes). Allowed enum values: `60,300`                                                                                                                                          |
| time_slice           | threshold [*required*]            | double          | The threshold value to which each SLI value will be compared.                                                                                                                                                                                                                                                                                                           |
| sli_specification    | Option 2                               | object          | A metric SLI specification.                                                                                                                                                                                                                                                                                                                                             |
| Option 2             | count [*required*]                | object          | A count-based (metric) SLI specification, composed of three parts: the good events formula, the total events formula, and the underlying queries.                                                                                                                                                                                                                       |
| count                | good_events_formula [*required*]  | object          | A formula that specifies how to combine the results of multiple queries.                                                                                                                                                                                                                                                                                                |
| good_events_formula  | formula [*required*]              | string          | The formula string, which is an expression involving named queries.                                                                                                                                                                                                                                                                                                     |
| count                | queries [*required*]              | [ <oneOf>] |
| queries              | Option 1                               | object          | A formula and functions metrics query.                                                                                                                                                                                                                                                                                                                                  |
| Option 1             | aggregator                             | enum            | The aggregation methods available for metrics queries. Allowed enum values: `avg,min,max,sum,last,area,l2norm,percentile`                                                                                                                                                                                                                                               |
| Option 1             | cross_org_uuids                        | [string]        | The source organization UUID for cross organization queries. Feature in Private Beta.                                                                                                                                                                                                                                                                                   |
| Option 1             | data_source [*required*]          | enum            | Data source for metrics queries. Allowed enum values: `metrics`                                                                                                                                                                                                                                                                                                         |
| Option 1             | name [*required*]                 | string          | Name of the query for use in formulas.                                                                                                                                                                                                                                                                                                                                  |
| Option 1             | query [*required*]                | string          | Metrics query definition.                                                                                                                                                                                                                                                                                                                                               |
| Option 1             | semantic_mode                          | enum            | Semantic mode for metrics queries. This determines how metrics from different sources are combined or displayed. Allowed enum values: `combined,native`                                                                                                                                                                                                                 |
| count                | total_events_formula [*required*] | object          | A formula that specifies how to combine the results of multiple queries.                                                                                                                                                                                                                                                                                                |
| total_events_formula | formula [*required*]              | string          | The formula string, which is an expression involving named queries.                                                                                                                                                                                                                                                                                                     |
| data                 | tags                                   | [string]        | A list of tags associated with this service level objective. Always included in service level objective responses (but may be empty). Optional in create/update requests.                                                                                                                                                                                               |
| data                 | target_threshold                       | double          | The target threshold such that when the service level indicator is above this threshold over the given timeframe, the objective is being met.                                                                                                                                                                                                                           |
| data                 | thresholds                             | [object]        | The thresholds (timeframes and associated targets) for this service level objective object.                                                                                                                                                                                                                                                                             |
| thresholds           | target [*required*]               | double          | The target value for the service level indicator within the corresponding timeframe.                                                                                                                                                                                                                                                                                    |
| thresholds           | target_display                         | string          | A string representation of the target that indicates its precision. It uses trailing zeros to show significant decimal places (for example `98.00`).                                                                                                                                                                                                                    | Always included in service level objective responses. Ignored in create/update requests.                                                                                                                            |
| thresholds           | timeframe [*required*]            | enum            | The SLO time window options. Note that "custom" is not a valid option for creating or updating SLOs. It is only used when querying SLO history over custom timeframes. Allowed enum values: `7d,30d,90d,custom`                                                                                                                                                         |
| thresholds           | warning                                | double          | The warning value for the service level objective.                                                                                                                                                                                                                                                                                                                      |
| thresholds           | warning_display                        | string          | A string representation of the warning target (see the description of the `target_display` field for details).                                                                                                                                                                                                                                                          | Included in service level objective responses if a warning target exists. Ignored in create/update requests.                                                                                                        |
| data                 | timeframe                              | enum            | The SLO time window options. Note that "custom" is not a valid option for creating or updating SLOs. It is only used when querying SLO history over custom timeframes. Allowed enum values: `7d,30d,90d,custom`                                                                                                                                                         |
| data                 | type                                   | enum            | The type of the service level objective. Allowed enum values: `metric,monitor,time_slice`                                                                                                                                                                                                                                                                               |
| data                 | warning_threshold                      | double          | The optional warning threshold such that when the service level indicator is below this value for the given threshold, but above the target threshold, the objective appears in a "warning" state. This value must be greater than the target threshold.                                                                                                                |
|                      | errors                                 | [string]        | An array of error messages. Each endpoint documents how/whether this field is used.                                                                                                                                                                                                                                                                                     |

{% /tab %}

{% tab title="Example" %}

```json
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

{% tab title="404" %}
Not found
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
                  \# Path parametersexport slo_id="CHANGE_ME"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/slo/${slo_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# Get an SLO's details returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::ServiceLevelObjectivesAPI.new

# there is a valid "slo" in the system
SLO_DATA_0_ID = ENV["SLO_DATA_0_ID"]
p api_instance.get_slo(SLO_DATA_0_ID)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```ruby
# This is not currently available for the Ruby API.
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby-legacy) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"
#####

```python
from datadog import initialize, api

options = {
    'api_key': '<DATADOG_API_KEY>',
    'app_key': '<DATADOG_APPLICATION_KEY>'
}

slo_id = '<YOUR_SLO_ID>'

initialize(**options)

api.ServiceLevelObjective.get(slo_id)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python-legacy) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python "example.py"
#####

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
#####

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"
{% /tab %}

## Delete an SLO{% #delete-an-slo %}

{% tab title="v1" %}

| Datadog site      | API endpoint                                             |
| ----------------- | -------------------------------------------------------- |
| ap1.datadoghq.com | DELETE https://api.ap1.datadoghq.com/api/v1/slo/{slo_id} |
| ap2.datadoghq.com | DELETE https://api.ap2.datadoghq.com/api/v1/slo/{slo_id} |
| app.datadoghq.eu  | DELETE https://api.datadoghq.eu/api/v1/slo/{slo_id}      |
| app.ddog-gov.com  | DELETE https://api.ddog-gov.com/api/v1/slo/{slo_id}      |
| app.datadoghq.com | DELETE https://api.datadoghq.com/api/v1/slo/{slo_id}     |
| us3.datadoghq.com | DELETE https://api.us3.datadoghq.com/api/v1/slo/{slo_id} |
| us5.datadoghq.com | DELETE https://api.us5.datadoghq.com/api/v1/slo/{slo_id} |

### Overview

Permanently delete the specified service level objective object.

If an SLO is used in a dashboard, the `DELETE /v1/slo/` endpoint returns a 409 conflict error because the SLO is referenced in a dashboard.
This endpoint requires the `slos_write` permission.
OAuth apps require the `slos_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#service-level-objectives) to access this endpoint.

### Arguments

#### Path Parameters

| Name                     | Type   | Description                            |
| ------------------------ | ------ | -------------------------------------- |
| slo_id [*required*] | string | The ID of the service level objective. |

#### Query Strings

| Name  | Type   | Description                                                                                         |
| ----- | ------ | --------------------------------------------------------------------------------------------------- |
| force | string | Delete the monitor even if it's referenced by other resources (for example SLO, composite monitor). |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
A response list of all service level objective deleted.

| Parent field         | Field     | Type     | Description                                                                      |
| -------------------- | --------- | -------- | -------------------------------------------------------------------------------- |
|                      | data      | [string] | An array containing the ID of the deleted service level objective object.        |
|                      | errors    | object   | An dictionary containing the ID of the SLO as key and a deletion error as value. |
| additionalProperties | <any-key> | string   | Error preventing the SLO deletion.                                               |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [],
  "errors": {
    "<any-key>": "string"
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

{% tab title="404" %}
Not found
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

{% tab title="409" %}
Conflict
{% tab title="Model" %}
A response list of all service level objective deleted.

| Parent field         | Field     | Type     | Description                                                                      |
| -------------------- | --------- | -------- | -------------------------------------------------------------------------------- |
|                      | data      | [string] | An array containing the ID of the deleted service level objective object.        |
|                      | errors    | object   | An dictionary containing the ID of the SLO as key and a deletion error as value. |
| additionalProperties | <any-key> | string   | Error preventing the SLO deletion.                                               |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [],
  "errors": {
    "<any-key>": "string"
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
                  \# Path parametersexport slo_id="CHANGE_ME"\# Curl commandcurl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/slo/${slo_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# Delete an SLO returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::ServiceLevelObjectivesAPI.new

# there is a valid "slo" in the system
SLO_DATA_0_ID = ENV["SLO_DATA_0_ID"]
p api_instance.delete_slo(SLO_DATA_0_ID)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```ruby
require 'dogapi'

api_key = '<DATADOG_API_KEY>'
app_key = '<DATADOG_APPLICATION_KEY>'
slo_id  = '<YOUR_SLO_ID>'

dog = Dogapi::Client.new(api_key, app_key)

dog.delete_service_level_objective(slo_id)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby-legacy) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"
#####

```python
from datadog import initialize, api

options = {
    'api_key': '<DATADOG_API_KEY>',
    'app_key': '<DATADOG_APPLICATION_KEY>'
}

slo_id = '<YOUR_SLO_ID>'

initialize(**options)

api.ServiceLevelObjective.delete(slo_id)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python-legacy) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python "example.py"
#####

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
#####

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"
{% /tab %}

## Get an SLO's history{% #get-an-slos-history %}

{% tab title="v1" %}

| Datadog site      | API endpoint                                                  |
| ----------------- | ------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v1/slo/{slo_id}/history |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v1/slo/{slo_id}/history |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v1/slo/{slo_id}/history      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v1/slo/{slo_id}/history      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v1/slo/{slo_id}/history     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v1/slo/{slo_id}/history |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v1/slo/{slo_id}/history |

### Overview

Get a specific SLO's history, regardless of its SLO type.

The detailed history data is structured according to the source data type. For example, metric data is included for event SLOs that use the metric source, and monitor SLO types include the monitor transition history.

**Note:** There are different response formats for event based and time based SLOs. Examples of both are shown.
This endpoint requires the `slos_read` permission.
OAuth apps require the `slos_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#service-level-objectives) to access this endpoint.

### Arguments

#### Path Parameters

| Name                     | Type   | Description                                   |
| ------------------------ | ------ | --------------------------------------------- |
| slo_id [*required*] | string | The ID of the service level objective object. |

#### Query Strings

| Name                      | Type    | Description                                                                                                                                                                    |
| ------------------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| from_ts [*required*] | integer | The `from` timestamp for the query window in epoch seconds.                                                                                                                    |
| to_ts [*required*]   | integer | The `to` timestamp for the query window in epoch seconds.                                                                                                                      |
| target                    | number  | The SLO target. If `target` is passed in, the response will include the remaining error budget and a timeframe value of `custom`.                                              |
| apply_correction          | boolean | Defaults to `true`. If any SLO corrections are applied and this parameter is set to `false`, then the corrections will not be applied and the SLI values will not be affected. |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
A service level objective history response.

| Parent field         | Field                           | Type     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| -------------------- | ------------------------------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                      | data                            | object   | An array of service level objective objects.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| data                 | from_ts                         | int64    | The `from` timestamp in epoch seconds.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| data                 | group_by                        | [string] | For `metric` based SLOs where the query includes a group-by clause, this represents the list of grouping parameters.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | This is not included in responses for `monitor` based SLOs.                                                  |
| data                 | groups                          | [object] | For grouped SLOs, this represents SLI data for specific groups.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | This is not included in the responses for `metric` based SLOs.                                               |
| groups               | error_budget_remaining          | object   | A mapping of threshold `timeframe` to the remaining error budget.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| additionalProperties | <any-key>                       | double   | Remaining error budget.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| groups               | errors                          | [object] | An array of error objects returned while querying the history data for the service level objective.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| errors               | error_message [*required*] | string   | A message with more details about the error.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| errors               | error_type [*required*]    | string   | Type of the error.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| groups               | group                           | string   | For groups in a grouped SLO, this is the group name.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| groups               | history                         | [array]  | The state transition history for the monitor. It is represented as an array of pairs. Each pair is an array containing the timestamp of the transition as an integer in Unix epoch format in the first element, and the state as an integer in the second element. An integer value of `0` for state means uptime, `1` means downtime, and `2` means no data. Periods of no data are counted either as uptime or downtime depending on monitor settings. See [SLO documentation](https://docs.datadoghq.com/service_management/service_level_objectives/monitor/#missing-data) for detailed information.                                                                                       |
| groups               | monitor_modified                | int64    | For `monitor` based SLOs, this is the last modified timestamp in epoch seconds of the monitor.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| groups               | monitor_type                    | string   | For `monitor` based SLOs, this describes the type of monitor.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| groups               | name                            | string   | For groups in a grouped SLO, this is the group name. For monitors in a multi-monitor SLO, this is the monitor name.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| groups               | precision                       | double   | **DEPRECATED**: The amount of decimal places the SLI value is accurate to for the given from `&&` to timestamp. Use `span_precision` instead.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| groups               | preview                         | boolean  | For `monitor` based SLOs, when `true` this indicates that a replay is in progress to give an accurate uptime calculation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| groups               | sli_value                       | double   | The current SLI value of the SLO over the history window.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| groups               | span_precision                  | double   | The amount of decimal places the SLI value is accurate to for the given from `&&` to timestamp.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| groups               | uptime                          | double   | **DEPRECATED**: Use `sli_value` instead.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| data                 | monitors                        | [object] | For multi-monitor SLOs, this represents SLI data for specific monitors.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | This is not included in the responses for `metric` based SLOs.                                               |
| monitors             | error_budget_remaining          | object   | A mapping of threshold `timeframe` to the remaining error budget.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| additionalProperties | <any-key>                       | double   | Remaining error budget.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| monitors             | errors                          | [object] | An array of error objects returned while querying the history data for the service level objective.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| errors               | error_message [*required*] | string   | A message with more details about the error.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| errors               | error_type [*required*]    | string   | Type of the error.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| monitors             | group                           | string   | For groups in a grouped SLO, this is the group name.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| monitors             | history                         | [array]  | The state transition history for the monitor. It is represented as an array of pairs. Each pair is an array containing the timestamp of the transition as an integer in Unix epoch format in the first element, and the state as an integer in the second element. An integer value of `0` for state means uptime, `1` means downtime, and `2` means no data. Periods of no data are counted either as uptime or downtime depending on monitor settings. See [SLO documentation](https://docs.datadoghq.com/service_management/service_level_objectives/monitor/#missing-data) for detailed information.                                                                                       |
| monitors             | monitor_modified                | int64    | For `monitor` based SLOs, this is the last modified timestamp in epoch seconds of the monitor.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| monitors             | monitor_type                    | string   | For `monitor` based SLOs, this describes the type of monitor.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| monitors             | name                            | string   | For groups in a grouped SLO, this is the group name. For monitors in a multi-monitor SLO, this is the monitor name.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| monitors             | precision                       | double   | **DEPRECATED**: The amount of decimal places the SLI value is accurate to for the given from `&&` to timestamp. Use `span_precision` instead.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| monitors             | preview                         | boolean  | For `monitor` based SLOs, when `true` this indicates that a replay is in progress to give an accurate uptime calculation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| monitors             | sli_value                       | double   | The current SLI value of the SLO over the history window.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| monitors             | span_precision                  | double   | The amount of decimal places the SLI value is accurate to for the given from `&&` to timestamp.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| monitors             | uptime                          | double   | **DEPRECATED**: Use `sli_value` instead.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| data                 | overall                         | object   | An object that holds an SLI value and its associated data. It can represent an SLO's overall SLI value. This can also represent the SLI value for a specific monitor in multi-monitor SLOs, or a group in grouped SLOs.                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| overall              | error_budget_remaining          | object   | A mapping of threshold `timeframe` to the remaining error budget.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| additionalProperties | <any-key>                       | double   | Remaining error budget.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| overall              | errors                          | [object] | An array of error objects returned while querying the history data for the service level objective.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| errors               | error_message [*required*] | string   | A message with more details about the error.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| errors               | error_type [*required*]    | string   | Type of the error.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| overall              | group                           | string   | For groups in a grouped SLO, this is the group name.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| overall              | history                         | [array]  | The state transition history for `monitor` or `time-slice` SLOs. It is represented as an array of pairs. Each pair is an array containing the timestamp of the transition as an integer in Unix epoch format in the first element, and the state as an integer in the second element. An integer value of `0` for state means uptime, `1` means downtime, and `2` means no data. Periods of no data count as uptime in time-slice SLOs, while for monitor SLOs, no data is counted either as uptime or downtime depending on monitor settings. See [SLO documentation](https://docs.datadoghq.com/service_management/service_level_objectives/monitor/#missing-data) for detailed information. |
| overall              | monitor_modified                | int64    | For `monitor` based SLOs, this is the last modified timestamp in epoch seconds of the monitor.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| overall              | monitor_type                    | string   | For `monitor` based SLOs, this describes the type of monitor.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| overall              | name                            | string   | For groups in a grouped SLO, this is the group name. For monitors in a multi-monitor SLO, this is the monitor name.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| overall              | precision                       | object   | A mapping of threshold `timeframe` to number of accurate decimals, regardless of the from && to timestamp.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| additionalProperties | <any-key>                       | double   | The number of accurate decimals.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| overall              | preview                         | boolean  | For `monitor` based SLOs, when `true` this indicates that a replay is in progress to give an accurate uptime calculation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| overall              | sli_value                       | double   | The current SLI value of the SLO over the history window.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| overall              | span_precision                  | double   | The amount of decimal places the SLI value is accurate to for the given from `&&` to timestamp.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| overall              | uptime                          | double   | **DEPRECATED**: Use `sli_value` instead.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| data                 | series                          | object   | A `metric` based SLO history response.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | This is not included in responses for `monitor` based SLOs.                                                  |
| series               | denominator [*required*]   | object   | A representation of `metric` based SLO timeseries for the provided queries. This is the same response type from `batch_query` endpoint.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| denominator          | count [*required*]         | int64    | Count of submitted metrics.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| denominator          | metadata                        | object   | Query metadata.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| metadata             | aggr                            | string   | **DEPRECATED**: Query aggregator function.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| metadata             | expression                      | string   | **DEPRECATED**: Query expression.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| metadata             | metric                          | string   | **DEPRECATED**: Query metric used.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| metadata             | query_index                     | int64    | **DEPRECATED**: Query index from original combined query.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| metadata             | scope                           | string   | **DEPRECATED**: Query scope.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| metadata             | unit                            | [object] | An array of metric units that contains up to two unit objects. For example, bytes represents one unit object and bytes per second represents two unit objects. If a metric query only has one unit object, the second array element is null.                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| unit                 | family                          | string   | The family of metric unit, for example `bytes` is the family for `kibibyte`, `byte`, and `bit` units.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| unit                 | id                              | int64    | The ID of the metric unit.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| unit                 | name                            | string   | The unit of the metric, for instance `byte`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| unit                 | plural                          | string   | The plural Unit of metric, for instance `bytes`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| unit                 | scale_factor                    | double   | The scale factor of metric unit, for instance `1.0`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| unit                 | short_name                      | string   | A shorter and abbreviated version of the metric unit, for instance `B`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| denominator          | sum [*required*]           | double   | Total sum of the query.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| denominator          | values [*required*]        | [number] | The query values for each metric.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| series               | interval [*required*]      | int64    | The aggregated query interval for the series data. It's implicit based on the query time window.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| series               | message                         | string   | Optional message if there are specific query issues/warnings.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| series               | numerator [*required*]     | object   | A representation of `metric` based SLO timeseries for the provided queries. This is the same response type from `batch_query` endpoint.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| numerator            | count [*required*]         | int64    | Count of submitted metrics.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| numerator            | metadata                        | object   | Query metadata.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| metadata             | aggr                            | string   | **DEPRECATED**: Query aggregator function.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| metadata             | expression                      | string   | **DEPRECATED**: Query expression.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| metadata             | metric                          | string   | **DEPRECATED**: Query metric used.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| metadata             | query_index                     | int64    | **DEPRECATED**: Query index from original combined query.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| metadata             | scope                           | string   | **DEPRECATED**: Query scope.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| metadata             | unit                            | [object] | An array of metric units that contains up to two unit objects. For example, bytes represents one unit object and bytes per second represents two unit objects. If a metric query only has one unit object, the second array element is null.                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| unit                 | family                          | string   | The family of metric unit, for example `bytes` is the family for `kibibyte`, `byte`, and `bit` units.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| unit                 | id                              | int64    | The ID of the metric unit.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| unit                 | name                            | string   | The unit of the metric, for instance `byte`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| unit                 | plural                          | string   | The plural Unit of metric, for instance `bytes`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| unit                 | scale_factor                    | double   | The scale factor of metric unit, for instance `1.0`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| unit                 | short_name                      | string   | A shorter and abbreviated version of the metric unit, for instance `B`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| numerator            | sum [*required*]           | double   | Total sum of the query.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| numerator            | values [*required*]        | [number] | The query values for each metric.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| series               | query [*required*]         | string   | The combined numerator and denominator query CSV.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| series               | res_type [*required*]      | string   | The series result type. This mimics `batch_query` response type.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| series               | resp_version [*required*]  | int64    | The series response version type. This mimics `batch_query` response type.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| series               | times [*required*]         | [number] | An array of query timestamps in EPOCH milliseconds.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| data                 | thresholds                      | object   | mapping of string timeframe to the SLO threshold.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| additionalProperties | <any-key>                       | object   | SLO thresholds (target and optionally warning) for a single time window.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| <any-key>            | target [*required*]        | double   | The target value for the service level indicator within the corresponding timeframe.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| <any-key>            | target_display                  | string   | A string representation of the target that indicates its precision. It uses trailing zeros to show significant decimal places (for example `98.00`).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Always included in service level objective responses. Ignored in create/update requests.                     |
| <any-key>            | timeframe [*required*]     | enum     | The SLO time window options. Note that "custom" is not a valid option for creating or updating SLOs. It is only used when querying SLO history over custom timeframes. Allowed enum values: `7d,30d,90d,custom`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| <any-key>            | warning                         | double   | The warning value for the service level objective.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| <any-key>            | warning_display                 | string   | A string representation of the warning target (see the description of the `target_display` field for details).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Included in service level objective responses if a warning target exists. Ignored in create/update requests. |
| data                 | to_ts                           | int64    | The `to` timestamp in epoch seconds.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| data                 | type                            | enum     | The type of the service level objective. Allowed enum values: `metric,monitor,time_slice`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| data                 | type_id                         | enum     | A numeric representation of the type of the service level objective (`0` for monitor, `1` for metric). Always included in service level objective responses. Ignored in create/update requests. Allowed enum values: `0,1,2`                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                      | errors                          | [object] | A list of errors while querying the history data for the service level objective.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| errors               | error                           | string   | Human readable error.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |

{% /tab %}

{% tab title="Example" %}

```json
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

{% /tab %}

{% /tab %}

{% tab title="400" %}
Bad Request
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

{% tab title="404" %}
Not Found
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
                  \# Path parametersexport slo_id="CHANGE_ME"\# Required query argumentsexport from_ts="CHANGE_ME"export to_ts="CHANGE_ME"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/slo/${slo_id}/history?from_ts=${from_ts}&to_ts=${to_ts}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# Get an SLO's history returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::ServiceLevelObjectivesAPI.new

# there is a valid "slo" in the system
SLO_DATA_0_ID = ENV["SLO_DATA_0_ID"]
p api_instance.get_slo_history(SLO_DATA_0_ID, (Time.now + -1 * 86400).to_i, Time.now.to_i)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```ruby
require 'dogapi'

api_key = '<DATADOG_API_KEY>'
app_key = '<DATADOG_APPLICATION_KEY>'
slo_id  = '<YOUR_SLO_ID>'

dog = Dogapi::Client.new(api_key, app_key)

to_ts = 1_571_320_613
from_ts = to_ts - 60 * 60 * 24 * 30

dog.get_service_level_objective_history(slo_id, from_ts, to_ts)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby-legacy) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"
#####

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python-legacy) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python "example.py"
#####

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
#####

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"
{% /tab %}

## Get Corrections For an SLO{% #get-corrections-for-an-slo %}

{% tab title="v1" %}

| Datadog site      | API endpoint                                                      |
| ----------------- | ----------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v1/slo/{slo_id}/corrections |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v1/slo/{slo_id}/corrections |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v1/slo/{slo_id}/corrections      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v1/slo/{slo_id}/corrections      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v1/slo/{slo_id}/corrections     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v1/slo/{slo_id}/corrections |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v1/slo/{slo_id}/corrections |

### Overview

Get corrections applied to an SLO This endpoint requires the `slos_read` permission.

OAuth apps require the `slos_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#service-level-objectives) to access this endpoint.

### Arguments

#### Path Parameters

| Name                     | Type   | Description                                   |
| ------------------------ | ------ | --------------------------------------------- |
| slo_id [*required*] | string | The ID of the service level objective object. |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
A list of SLO correction objects.

| Parent field | Field                | Type     | Description                                                                                                                                              |
| ------------ | -------------------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
|              | data                 | [object] | The list of SLO corrections objects.                                                                                                                     |
| data         | attributes           | object   | The attribute object associated with the SLO correction.                                                                                                 |
| attributes   | category             | enum     | Category the SLO correction belongs to. Allowed enum values: `Scheduled Maintenance,Outside Business Hours,Deployment,Other`                             |
| attributes   | created_at           | int64    | The epoch timestamp of when the correction was created at.                                                                                               |
| attributes   | creator              | object   | Object describing the creator of the shared element.                                                                                                     |
| creator      | email                | string   | Email of the creator.                                                                                                                                    |
| creator      | handle               | string   | Handle of the creator.                                                                                                                                   |
| creator      | name                 | string   | Name of the creator.                                                                                                                                     |
| attributes   | description          | string   | Description of the correction being made.                                                                                                                |
| attributes   | duration             | int64    | Length of time (in seconds) for a specified `rrule` recurring SLO correction.                                                                            |
| attributes   | end                  | int64    | Ending time of the correction in epoch seconds.                                                                                                          |
| attributes   | modified_at          | int64    | The epoch timestamp of when the correction was modified at.                                                                                              |
| attributes   | modifier             | object   | Modifier of the object.                                                                                                                                  |
| modifier     | email                | string   | Email of the Modifier.                                                                                                                                   |
| modifier     | handle               | string   | Handle of the Modifier.                                                                                                                                  |
| modifier     | name                 | string   | Name of the Modifier.                                                                                                                                    |
| attributes   | rrule                | string   | The recurrence rules as defined in the iCalendar RFC 5545. The supported rules for SLO corrections are `FREQ`, `INTERVAL`, `COUNT`, `UNTIL` and `BYDAY`. |
| attributes   | slo_id               | string   | ID of the SLO that this correction applies to.                                                                                                           |
| attributes   | start                | int64    | Starting time of the correction in epoch seconds.                                                                                                        |
| attributes   | timezone             | string   | The timezone to display in the UI for the correction times (defaults to "UTC").                                                                          |
| data         | id                   | string   | The ID of the SLO correction.                                                                                                                            |
| data         | type                 | enum     | SLO correction resource type. Allowed enum values: `correction`                                                                                          |
|              | meta                 | object   | Object describing meta attributes of response.                                                                                                           |
| meta         | page                 | object   | Pagination object.                                                                                                                                       |
| page         | total_count          | int64    | Total count.                                                                                                                                             |
| page         | total_filtered_count | int64    | Total count of elements matched by the filter.                                                                                                           |

{% /tab %}

{% tab title="Example" %}

```json
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

{% /tab %}

{% /tab %}

{% tab title="400" %}
Bad Request
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

{% tab title="404" %}
Not Found
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
                  \# Path parametersexport slo_id="CHANGE_ME"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/slo/${slo_id}/corrections" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# Get Corrections For an SLO returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::ServiceLevelObjectivesAPI.new

# there is a valid "slo" in the system
SLO_DATA_0_ID = ENV["SLO_DATA_0_ID"]
p api_instance.get_slo_corrections(SLO_DATA_0_ID)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"
#####

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
#####

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"
{% /tab %}

## Check if SLOs can be safely deleted{% #check-if-slos-can-be-safely-deleted %}

{% tab title="v1" %}

| Datadog site      | API endpoint                                            |
| ----------------- | ------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v1/slo/can_delete |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v1/slo/can_delete |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v1/slo/can_delete      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v1/slo/can_delete      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v1/slo/can_delete     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v1/slo/can_delete |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v1/slo/can_delete |

### Overview

Check if an SLO can be safely deleted. For example, assure an SLO can be deleted without disrupting a dashboard. This endpoint requires the `slos_read` permission.

OAuth apps require the `slos_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#service-level-objectives) to access this endpoint.

### Arguments

#### Query Strings

| Name                  | Type   | Description                                                                |
| --------------------- | ------ | -------------------------------------------------------------------------- |
| ids [*required*] | string | A comma separated list of the IDs of the service level objectives objects. |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
A service level objective response containing the requested object.

| Parent field         | Field     | Type     | Description                                           |
| -------------------- | --------- | -------- | ----------------------------------------------------- |
|                      | data      | object   | An array of service level objective objects.          |
| data                 | ok        | [string] | An array of SLO IDs that can be safely deleted.       |
|                      | errors    | object   | A mapping of SLO id to it's current usages.           |
| additionalProperties | <any-key> | string   | Description of the service level objective reference. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "ok": []
  },
  "errors": {
    "<any-key>": "string"
  }
}
```

{% /tab %}

{% /tab %}

{% tab title="400" %}
Bad Request
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

{% tab title="409" %}
Conflict
{% tab title="Model" %}
A service level objective response containing the requested object.

| Parent field         | Field     | Type     | Description                                           |
| -------------------- | --------- | -------- | ----------------------------------------------------- |
|                      | data      | object   | An array of service level objective objects.          |
| data                 | ok        | [string] | An array of SLO IDs that can be safely deleted.       |
|                      | errors    | object   | A mapping of SLO id to it's current usages.           |
| additionalProperties | <any-key> | string   | Description of the service level objective reference. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "ok": []
  },
  "errors": {
    "<any-key>": "string"
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
                  \# Required query argumentsexport ids="id1, id2, id3"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/slo/can_delete?ids=${ids}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# Check if SLOs can be safely deleted returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::ServiceLevelObjectivesAPI.new
p api_instance.check_can_delete_slo("ids")
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```ruby
require 'dogapi'

api_key = '<DATADOG_API_KEY>'
app_key = '<DATADOG_APPLICATION_KEY>'

dog = Dogapi::Client.new(api_key, app_key)

slo_ids = ['<YOUR_SLO_ID>']
dog.can_delete_service_level_objective(slo_ids)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby-legacy) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"
#####

```python
from datadog import initialize, api

options = {
    'api_key': '<DATADOG_API_KEY>',
    'app_key': '<DATADOG_APPLICATION_KEY>'
}

slo_ids = ['<YOUR_SLO_ID>']

initialize(**options)

api.ServiceLevelObjective.can_delete(slo_ids)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python-legacy) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python "example.py"
#####

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
#####

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"
{% /tab %}

## Bulk Delete SLO Timeframes{% #bulk-delete-slo-timeframes %}

{% tab title="v1" %}

| Datadog site      | API endpoint                                              |
| ----------------- | --------------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v1/slo/bulk_delete |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v1/slo/bulk_delete |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v1/slo/bulk_delete      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v1/slo/bulk_delete      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v1/slo/bulk_delete     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v1/slo/bulk_delete |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v1/slo/bulk_delete |

### Overview

Delete (or partially delete) multiple service level objective objects.

This endpoint facilitates deletion of one or more thresholds for one or more service level objective objects. If all thresholds are deleted, the service level objective object is deleted as well.
This endpoint requires the `slos_write` permission.
OAuth apps require the `slos_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#service-level-objectives) to access this endpoint.

### Request

#### Body Data (required)

Delete multiple service level objective objects request body.

{% tab title="Model" %}

| Field     | Type     | Description                     |
| --------- | -------- | ------------------------------- |
| <any-key> | [string] | An array of all SLO timeframes. |

{% /tab %}

{% tab title="Example" %}

```json
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

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}

The bulk partial delete service level objective object endpoint response.

This endpoint operates on multiple service level objective objects, so it may be partially successful. In such cases, the "data" and "error" fields in this response indicate which deletions succeeded and failed.

| Parent field | Field                       | Type     | Description                                                                                                                                                                                  |
| ------------ | --------------------------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|              | data                        | object   | An array of service level objective objects.                                                                                                                                                 |
| data         | deleted                     | [string] | An array of service level objective object IDs that indicates which objects that were completely deleted.                                                                                    |
| data         | updated                     | [string] | An array of service level objective object IDs that indicates which objects that were modified (objects for which at least one threshold was deleted, but that were not completely deleted). |
|              | errors                      | [object] | Array of errors object returned.                                                                                                                                                             |
| errors       | id [*required*]        | string   | The ID of the service level objective object associated with this error.                                                                                                                     |
| errors       | message [*required*]   | string   | The error message.                                                                                                                                                                           |
| errors       | timeframe [*required*] | enum     | The timeframe of the threshold associated with this error or "all" if all thresholds are affected. Allowed enum values: `7d,30d,90d,all`                                                     |

{% /tab %}

{% tab title="Example" %}

```json
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

{% /tab %}

{% /tab %}

{% tab title="400" %}
Bad Request
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
                  \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/slo/bulk_delete" \
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

#####

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```ruby
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby-legacy) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"
#####

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python-legacy) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python "example.py"
#####

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
#####

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"
{% /tab %}

## Create a new SLO report{% #create-a-new-slo-report %}

{% tab title="v2" %}
**Note**: This feature is in private beta. To request access, use the request access form in the [Service Level Objectives](https://docs.datadoghq.com/service_management/service_level_objectives/#slo-csv-export) docs.
| Datadog site      | API endpoint                                         |
| ----------------- | ---------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/slo/report |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/slo/report |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/slo/report      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/slo/report      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/slo/report     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/slo/report |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/slo/report |

### Overview

Create a job to generate an SLO report. The report job is processed asynchronously and eventually results in a CSV report being available for download.

Check the status of the job and download the CSV report using the returned `report_id`.
This endpoint requires the `slos_read` permission.
OAuth apps require the `slos_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#service-level-objectives) to access this endpoint.

### Request

#### Body Data (required)

Create SLO report job request body.

{% tab title="Model" %}

| Parent field | Field                        | Type   | Description                                                                                                                                         |
| ------------ | ---------------------------- | ------ | --------------------------------------------------------------------------------------------------------------------------------------------------- |
|              | data [*required*]       | object | The data portion of the SLO report request.                                                                                                         |
| data         | attributes [*required*] | object | The attributes portion of the SLO report request.                                                                                                   |
| attributes   | from_ts [*required*]    | int64  | The `from` timestamp for the report in epoch seconds.                                                                                               |
| attributes   | interval                     | enum   | The frequency at which report data is to be generated. Allowed enum values: `daily,weekly,monthly`                                                  |
| attributes   | query [*required*]      | string | The query string used to filter SLO results. Some examples of queries include `service:<service-name>` and `slo-name`.                              |
| attributes   | timezone                     | string | The timezone used to determine the start and end of each interval. For example, weekly intervals start at 12am on Sunday in the specified timezone. |
| attributes   | to_ts [*required*]      | int64  | The `to` timestamp for the report in epoch seconds.                                                                                                 |

{% /tab %}

{% tab title="Example" %}

```json
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

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
The SLO report response.

| Parent field | Field | Type   | Description                                  |
| ------------ | ----- | ------ | -------------------------------------------- |
|              | data  | object | The data portion of the SLO report response. |
| data         | id    | string | The ID of the report job.                    |
| data         | type  | string | The type of ID.                              |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "id": "dc8d92aa-e0af-11ee-af21-1feeaccaa3a3",
    "type": "report_id"
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
Forbidden
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
                          \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/slo/report" \
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

#####

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"
#####

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
#####

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"
{% /tab %}

## Get SLO report status{% #get-slo-report-status %}

{% tab title="v2" %}
**Note**: This feature is in private beta. To request access, use the request access form in the [Service Level Objectives](https://docs.datadoghq.com/service_management/service_level_objectives/#slo-csv-export) docs.
| Datadog site      | API endpoint                                                           |
| ----------------- | ---------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/slo/report/{report_id}/status |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/slo/report/{report_id}/status |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/slo/report/{report_id}/status      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/slo/report/{report_id}/status      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/slo/report/{report_id}/status     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/slo/report/{report_id}/status |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/slo/report/{report_id}/status |

### Overview

Get the status of the SLO report job.

OAuth apps require the `slos_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#service-level-objectives) to access this endpoint.

### Arguments

#### Path Parameters

| Name                        | Type   | Description               |
| --------------------------- | ------ | ------------------------- |
| report_id [*required*] | string | The ID of the report job. |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
The SLO report status response.

| Parent field | Field      | Type   | Description                                                                                                 |
| ------------ | ---------- | ------ | ----------------------------------------------------------------------------------------------------------- |
|              | data       | object | The data portion of the SLO report status response.                                                         |
| data         | attributes | object | The attributes portion of the SLO report status response.                                                   |
| attributes   | status     | enum   | The status of the SLO report job. Allowed enum values: `in_progress,completed,completed_with_errors,failed` |
| data         | id         | string | The ID of the report job.                                                                                   |
| data         | type       | string | The type of ID.                                                                                             |

{% /tab %}

{% tab title="Example" %}

```json
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
Forbidden
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
                  \# Path parametersexport report_id="CHANGE_ME"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/slo/report/${report_id}/status" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"
#####

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
#####

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"
{% /tab %}

## Get SLO report{% #get-slo-report %}

{% tab title="v2" %}
**Note**: This feature is in private beta. To request access, use the request access form in the [Service Level Objectives](https://docs.datadoghq.com/service_management/service_level_objectives/#slo-csv-export) docs.
| Datadog site      | API endpoint                                                             |
| ----------------- | ------------------------------------------------------------------------ |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/slo/report/{report_id}/download |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/slo/report/{report_id}/download |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/slo/report/{report_id}/download      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/slo/report/{report_id}/download      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/slo/report/{report_id}/download     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/slo/report/{report_id}/download |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/slo/report/{report_id}/download |

### Overview

Download an SLO report. This can only be performed after the report job has completed.

Reports are not guaranteed to exist indefinitely. Datadog recommends that you download the report as soon as it is available.

OAuth apps require the `slos_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#service-level-objectives) to access this endpoint.

### Arguments

#### Path Parameters

| Name                        | Type   | Description               |
| --------------------------- | ------ | ------------------------- |
| report_id [*required*] | string | The ID of the report job. |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}

| Field | Type | Description |
| ----- | ---- | ----------- |

{% /tab %}

{% tab title="Example" %}

```json
{}
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
Forbidden
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
                  \# Path parametersexport report_id="CHANGE_ME"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/slo/report/${report_id}/download" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# Get SLO report returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.get_slo_report".to_sym] = true
end
api_instance = DatadogAPIClient::V2::ServiceLevelObjectivesAPI.new
p api_instance.get_slo_report("9fb2dc2a-ead0-11ee-a174-9fe3a9d7627f")
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```go
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"
#####

```rust
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
#####

```typescript
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

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"
{% /tab %}

## Get SLO status{% #get-slo-status %}

{% tab title="v2" %}
**Note**: This endpoint is in public beta and it's subject to change. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
| Datadog site      | API endpoint                                                 |
| ----------------- | ------------------------------------------------------------ |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/slo/{slo_id}/status |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/slo/{slo_id}/status |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/slo/{slo_id}/status      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/slo/{slo_id}/status      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/slo/{slo_id}/status     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/slo/{slo_id}/status |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/slo/{slo_id}/status |

### Overview

Get the status of a Service Level Objective (SLO) for a given time period.

This endpoint returns the current SLI value, error budget remaining, and other status information for the specified SLO.
This endpoint requires the `slos_read` permission.
OAuth apps require the `slos_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#service-level-objectives) to access this endpoint.

### Arguments

#### Path Parameters

| Name                     | Type   | Description        |
| ------------------------ | ------ | ------------------ |
| slo_id [*required*] | string | The ID of the SLO. |

#### Query Strings

| Name                      | Type    | Description                                                                               |
| ------------------------- | ------- | ----------------------------------------------------------------------------------------- |
| from_ts [*required*] | integer | The starting timestamp for the SLO status query in epoch seconds.                         |
| to_ts [*required*]   | integer | The ending timestamp for the SLO status query in epoch seconds.                           |
| disable_corrections       | boolean | Whether to exclude correction windows from the SLO status calculation. Defaults to false. |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
The SLO status response.

| Parent field               | Field                                        | Type   | Description                                                              |
| -------------------------- | -------------------------------------------- | ------ | ------------------------------------------------------------------------ |
|                            | data [*required*]                       | object | The data portion of the SLO status response.                             |
| data                       | attributes [*required*]                 | object | The attributes of the SLO status.                                        |
| attributes                 | error_budget_remaining [*required*]     | double | The percentage of error budget remaining.                                |
| attributes                 | raw_error_budget_remaining [*required*] | object | The raw error budget remaining for the SLO.                              |
| raw_error_budget_remaining | unit [*required*]                       | string | The unit of the error budget (for example, `seconds`, `requests`).       |
| raw_error_budget_remaining | value [*required*]                      | double | The numeric value of the remaining error budget.                         |
| attributes                 | sli [*required*]                        | double | The current Service Level Indicator (SLI) value as a percentage.         |
| attributes                 | span_precision [*required*]             | int64  | The precision of the time span in seconds.                               |
| attributes                 | state [*required*]                      | string | The current state of the SLO (for example, `breached`, `warning`, `ok`). |
| data                       | id [*required*]                         | string | The ID of the SLO.                                                       |
| data                       | type [*required*]                       | enum   | The type of the SLO status resource. Allowed enum values: `slo_status`   |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "error_budget_remaining": 99.5,
      "raw_error_budget_remaining": {
        "unit": "seconds",
        "value": 86400.5
      },
      "sli": 99.95,
      "span_precision": 2,
      "state": "ok"
    },
    "id": "00000000-0000-0000-0000-000000000000",
    "type": "slo_status"
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
Forbidden
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

{% tab title="404" %}
Not Found
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
                  \# Path parametersexport slo_id="00000000-0000-0000-0000-000000000000"\# Required query argumentsexport from_ts="1.69090187e+09"export to_ts="1.70680307e+09"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/slo/${slo_id}/status?from_ts=${from_ts}&to_ts=${to_ts}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
Get SLO status returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.service_level_objectives_api import ServiceLevelObjectivesApi

configuration = Configuration()
configuration.unstable_operations["get_slo_status"] = True
with ApiClient(configuration) as api_client:
    api_instance = ServiceLevelObjectivesApi(api_client)
    response = api_instance.get_slo_status(
        slo_id="00000000-0000-0000-0000-000000000000",
        from_ts=1690901870,
        to_ts=1706803070,
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
#####

```ruby
# Get SLO status returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.get_slo_status".to_sym] = true
end
api_instance = DatadogAPIClient::V2::ServiceLevelObjectivesAPI.new
p api_instance.get_slo_status("00000000-0000-0000-0000-000000000000", 1690901870, 1706803070)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
#####

```go
// Get SLO status returns "OK" response

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
    configuration.SetUnstableOperationEnabled("v2.GetSloStatus", true)
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewServiceLevelObjectivesApi(apiClient)
    resp, r, err := api.GetSloStatus(ctx, "00000000-0000-0000-0000-000000000000", 1690901870, 1706803070, *datadogV2.NewGetSloStatusOptionalParameters())

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `ServiceLevelObjectivesApi.GetSloStatus`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `ServiceLevelObjectivesApi.GetSloStatus`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
#####

```java
// Get SLO status returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.ServiceLevelObjectivesApi;
import com.datadog.api.client.v2.model.SloStatusResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.getSloStatus", true);
    ServiceLevelObjectivesApi apiInstance = new ServiceLevelObjectivesApi(defaultClient);

    try {
      SloStatusResponse result =
          apiInstance.getSloStatus(
              "00000000-0000-0000-0000-000000000000", 1690901870L, 1706803070L);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServiceLevelObjectivesApi#getSloStatus");
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
// Get SLO status returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_service_level_objectives::GetSloStatusOptionalParams;
use datadog_api_client::datadogV2::api_service_level_objectives::ServiceLevelObjectivesAPI;

#[tokio::main]
async fn main() {
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.GetSloStatus", true);
    let api = ServiceLevelObjectivesAPI::with_config(configuration);
    let resp = api
        .get_slo_status(
            "00000000-0000-0000-0000-000000000000".to_string(),
            1690901870,
            1706803070,
            GetSloStatusOptionalParams::default(),
        )
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
 * Get SLO status returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.getSloStatus"] = true;
const apiInstance = new v2.ServiceLevelObjectivesApi(configuration);

const params: v2.ServiceLevelObjectivesApiGetSloStatusRequest = {
  sloId: "00000000-0000-0000-0000-000000000000",
  fromTs: 1690901870,
  toTs: 1706803070,
};

apiInstance
  .getSloStatus(params)
  .then((data: v2.SloStatusResponse) => {
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
