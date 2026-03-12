# Source: https://docs.statsig.com/data-warehouse-ingestion/data_mapping.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Data Mapping

## Overview

Statsig requires certain data schema in order for proper processing. We support 3 different types of datasets to be ingested into our platform:

1. Custom Events
2. Precomputed Metrics
3. Exposure Events

During setup, we will ask you to map columns in your data output to fields Statsig expects and run a small sample query to make sure that there aren't any basic issues with data types, the mapping, or the base query itself.

Please note that we will cast fields into the appropriate type. For example, Statsig accepts string IDs, but it is okay to leave an ID field as an integer.

***

### Custom Events

Events that are emitted by your application to measure the ongoing impact of your features and experiments.

#### Required

| Column      | Description                            | Format/Rules                                                                      |
| ----------- | -------------------------------------- | --------------------------------------------------------------------------------- |
| timestamp   | The unix time your event was logged at | BIGINT. please cast timestamps into epoch time in seconds                         |
| event\_name | The name of the event                  | STRING/VARCHAR. Not null. Length \< 128 characters                                |
| unit\_id    | Unique unit identifier                 | STRING/VARCHAR. User ID, Stable ID, etc. The same event row can have multiple IDs |

#### Optional

| Column          | Description                      | Rules                                                                                                            |
| --------------- | -------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| event\_value    | The value of the event           | STRING/VARCHAR. Length \< 128 characters. Statsig will detect numeric values                                     |
| event\_metadata | Metadata columns about the event | (MANY) STRING:STRING. Statsig will generate a metadata json field from however many metadata columns you provide |
| metadata\_json  | Metadata json about the event    | JSON STRING. Statsig will unpack this json 1 level deep. Nested values will be stored as strings                 |

<br />

An example dataset for events might look like this:

| unit\_id | visit\_id | event    | timestamp  | value | metadata\_blob                                             | user\_type        |
| -------- | --------- | -------- | ---------- | ----- | ---------------------------------------------------------- | ----------------- |
| 331444   |           | click    | 1676484875 |       | `{"click_target": "exit_details_button"}`                  | power\_user       |
| 331444   |           | click    | 1676484860 |       | `{"click_target": "open_details_button"}`                  | power\_user       |
| 265113   |           | click    | 1676484333 |       | `{"click_target": "button", "button_color": "green"}`      | churn\_risk\_user |
| 445332   | aeeer43d  | visit    | 1676483821 |       | `{"page": "landing_page"}`                                 | new\_user         |
| 224448   |           | checkout | 1676482222 | 33.22 | `{"product_id": "11eefj", "product_category": "clothing"}` | power\_user       |

Note that:

* One user can send multiple of the same event, with or without any changes in metadata. Statsig will aggregate these together.
* You can send metadata in both of a json-formatted (only one-level deep) string, and/or pull in fields from columns. You can use metadata and values to generate custom metrics in the console, like sum(value) where "product\_category"="clothing".
* You can send multiple IDs on a single event. For example, the visit above would could for both user and visit level metrics/experiments. During the mapping flow you tell us which unit types your different IDs correspond to in statsig.

***

<br />

### Precomputed Metrics

Precomputed metrics are a powerful way to leverage statsig for experiment results. Use these to send complex metrics and metrics that require delays due to attribution windows or long baking periods.

Precomputed metrics in statsig are expected to be calculated at a user-day granularity.

#### Required

| Column        | Description                                                                                                                     | Format/Rules                                                                                                                                                     |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| unit\_id      | The unique user identifier this metric is for. This might not necessarily be a user\_id - it could be a custom\_id of some kind | STRING                                                                                                                                                           |
| id\_type      | The id\_type the unit\_id represents.                                                                                           | STRING. A valid ID type from your project                                                                                                                        |
| date          | Date of the daily metric                                                                                                        | DATE or ISOFORMATTED STRING. The date of the metric value for the unit\_id provided                                                                              |
| metric\_name  | The name of the metric                                                                                                          | STRING (Not null). Length \< 128 characters                                                                                                                      |
| metric\_value | A numeric value for the metric                                                                                                  | DOUBLE/NUMERIC. Metric value <br /><b>OR</b><br /> Both of numerator/denominator need to be provided for Statsig to process the metric.                          |
| numerator     | Numerator for metric calculation                                                                                                | DOUBLE/NUMERIC. If present along with a denominator in any record, the metric will be treated as ratio and only calculated for users with non-null denominators. |
| denominator   | Denominator for metric calculation                                                                                              | DOUBLE/NUMERIC. If present along with a numerator in any record, the metric will be treated as ratio and only calculated for users with non-null denominators.   |

<br />

An example dataset for metrics might look like this:

| unit\_id | unit\_type | date       | metric\_name              | metric\_value | numerator | denominator |
| -------- | ---------- | ---------- | ------------------------- | ------------- | --------- | ----------- |
| 331444   | user\_id   | 2023-02-13 | clicks                    | 2             |           |             |
| aeeer43d | visit\_id  | 2023-02-13 | visits                    | 1             |           |             |
| 224448   | user\_id   | 2023-02-13 | checkout\_rate            |               | 2         | 15          |
| 224448   | user\_id   | 2023-02-13 | clothing\_checkout\_value | 33.22         |           |             |

Note that:

* In this dataset, unit types are in different rows from each other
* Metrics can either have a value or a numerator/denominator pair. We will calculate any metric with numerator/denominator pair as a ratio metric. Ratio takes priority over value; if you provide all 3 fields, we will assume it is a ratio metric.
* For users with null values, we will infer 0 for metric\_value, and exclude null value users for ratio metrics.

***

<br />

### Exposure Events

<Note>
  Exposure event import is deprecated. If this is an important use case, see [Statsig Warehouse Native](https://www.statsig.com/blog/announcing-statsig-warehouse-native), available to Enterprise Customers
</Note>

Exposure events are generated by your assignment tool, when it assigns your users to a certain variant of an experiment (e.g., show ad vs. hide ad).

#### Required

| Column     | Description                                 | Format/Rules                                                                      |
| ---------- | ------------------------------------------- | --------------------------------------------------------------------------------- |
| timestamp  | The unix time your event was logged at      | BIGINT. please cast timestamps into timezoneless unix time                        |
| experiment | Your experiment identifier                  | STRING/VARCHAR. Not null. Length \< 128 characters                                |
| group\_id  | Unique identifier for the experiment groups | STRING/VARCHAR. Not null.                                                         |
| unit\_id   | Unique user identifier                      | STRING/VARCHAR. User ID, Stable ID, etc. The same event row can have multiple IDs |

#### Optional

| Column         | Description                   | Rules                                                                                            |
| -------------- | ----------------------------- | ------------------------------------------------------------------------------------------------ |
| metadata\_json | Metadata json about the event | JSON STRING. Statsig will unpack this json 1 level deep. Nested values will be stored as strings |


Built with [Mintlify](https://mintlify.com).