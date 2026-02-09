# Source: https://docs.datadoghq.com/api/latest/monitors

# Monitors
[Monitors](https://docs.datadoghq.com/monitors) allow you to watch a metric or check that you care about and notifies your team when a defined threshold has exceeded.
For more information, see [Creating Monitors](https://docs.datadoghq.com/monitors/create/types/).
**Note:** `curl` commands require [url encoding](https://curl.se/docs/url-syntax.html).
## [Create a monitor](https://docs.datadoghq.com/api/latest/monitors/#create-a-monitor)
  * [v1 (latest)](https://docs.datadoghq.com/api/latest/monitors/#create-a-monitor-v1)


POST https://api.ap1.datadoghq.com/api/v1/monitorhttps://api.ap2.datadoghq.com/api/v1/monitorhttps://api.datadoghq.eu/api/v1/monitorhttps://api.ddog-gov.com/api/v1/monitorhttps://api.datadoghq.com/api/v1/monitorhttps://api.us3.datadoghq.com/api/v1/monitorhttps://api.us5.datadoghq.com/api/v1/monitor
### Overview
Create a monitor using the specified options.
#### [Monitor Types](https://docs.datadoghq.com/api/latest/monitors/#monitor-types)
The type of monitor chosen from:
  * anomaly: `query alert`
  * APM: `query alert` or `trace-analytics alert`
  * composite: `composite`
  * custom: `service check`
  * forecast: `query alert`
  * host: `service check`
  * integration: `query alert` or `service check`
  * live process: `process alert`
  * logs: `log alert`
  * metric: `query alert`
  * network: `service check`
  * outlier: `query alert`
  * process: `service check`
  * rum: `rum alert`
  * SLO: `slo alert`
  * watchdog: `event-v2 alert`
  * event-v2: `event-v2 alert`
  * audit: `audit alert`
  * error-tracking: `error-tracking alert`
  * database-monitoring: `database-monitoring alert`
  * network-performance: `network-performance alert`
  * cloud cost: `cost alert`


**Notes** :
  * Synthetic monitors are created through the Synthetics API. See the [Synthetics API](https://docs.datadoghq.com/api/latest/synthetics/) documentation for more information.
  * Log monitors require an unscoped App Key.


#### [Query Types](https://docs.datadoghq.com/api/latest/monitors/#query-types)
##### [Metric Alert Query](https://docs.datadoghq.com/api/latest/monitors/#metric-alert-query)
Example: `time_aggr(time_window):space_aggr:metric{tags} [by {key}] operator #`
  * `time_aggr`: avg, sum, max, min, change, or pct_change
  * `time_window`: `last_#m` (with `#` between 1 and 10080 depending on the monitor type) or `last_#h`(with `#` between 1 and 168 depending on the monitor type) or `last_1d`, or `last_1w`
  * `space_aggr`: avg, sum, min, or max
  * `tags`: one or more tags (comma-separated), or *
  * `key`: a ‘key’ in key:value tag syntax; defines a separate alert for each tag in the group (multi-alert)
  * `operator`: <, <=, >, >=, ==, or !=
  * `#`: an integer or decimal number used to set the threshold


If you are using the `_change_` or `_pct_change_` time aggregator, instead use `change_aggr(time_aggr(time_window), timeshift):space_aggr:metric{tags} [by {key}] operator #` with:
  * `change_aggr` change, pct_change
  * `time_aggr` avg, sum, max, min [Learn more](https://docs.datadoghq.com/monitors/create/types/#define-the-conditions)
  * `time_window` last_#m (between 1 and 2880 depending on the monitor type), last_#h (between 1 and 48 depending on the monitor type), or last_#d (1 or 2)
  * `timeshift` #m_ago (5, 10, 15, or 30), #h_ago (1, 2, or 4), or 1d_ago


Use this to create an outlier monitor using the following query: `avg(last_30m):outliers(avg:system.cpu.user{role:es-events-data} by {host}, 'dbscan', 7) > 0`
##### [Service Check Query](https://docs.datadoghq.com/api/latest/monitors/#service-check-query)
Example: `"check".over(tags).last(count).by(group).count_by_status()`
  * `check` name of the check, for example `datadog.agent.up`
  * `tags` one or more quoted tags (comma-separated), or “*”. for example: `.over("env:prod", "role:db")`; `over` cannot be blank.
  * `count` must be at greater than or equal to your max threshold (defined in the `options`). It is limited to 100. For example, if you’ve specified to notify on 1 critical, 3 ok, and 2 warn statuses, `count` should be at least 3.
  * `group` must be specified for check monitors. Per-check grouping is already explicitly known for some service checks. For example, Postgres integration monitors are tagged by `db`, `host`, and `port`, and Network monitors by `host`, `instance`, and `url`. See [Service Checks](https://docs.datadoghq.com/api/latest/service-checks/) documentation for more information.


##### [Event Alert Query](https://docs.datadoghq.com/api/latest/monitors/#event-alert-query)
**Note:** The Event Alert Query has been replaced by the Event V2 Alert Query. For more information, see the [Event Migration guide](https://docs.datadoghq.com/service_management/events/guides/migrating_to_new_events_features/).
##### [Event V2 Alert Query](https://docs.datadoghq.com/api/latest/monitors/#event-v2-alert-query)
Example: `events(query).rollup(rollup_method[, measure]).last(time_window) operator #`
  * `query` The search query - following the [Log search syntax](https://docs.datadoghq.com/logs/search_syntax/).
  * `rollup_method` The stats roll-up method - supports `count`, `avg` and `cardinality`.
  * `measure` For `avg` and cardinality `rollup_method` - specify the measure or the facet name you want to use.
  * `time_window` #m (between 1 and 2880), #h (between 1 and 48).
  * `operator` `<`, `<=`, `>`, `>=`, `==`, or `!=`.
  * `#` an integer or decimal number used to set the threshold.


##### [Process Alert Query](https://docs.datadoghq.com/api/latest/monitors/#process-alert-query)
Example: `processes(search).over(tags).rollup('count').last(timeframe) operator #`
  * `search` free text search string for querying processes. Matching processes match results on the [Live Processes](https://docs.datadoghq.com/infrastructure/process/?tab=linuxwindows) page.
  * `tags` one or more tags (comma-separated)
  * `timeframe` the timeframe to roll up the counts. Examples: 10m, 4h. Supported timeframes: s, m, h and d
  * `operator` <, <=, >, >=, ==, or !=
  * `#` an integer or decimal number used to set the threshold


##### [Logs Alert Query](https://docs.datadoghq.com/api/latest/monitors/#logs-alert-query)
Example: `logs(query).index(index_name).rollup(rollup_method[, measure]).last(time_window) operator #`
  * `query` The search query - following the [Log search syntax](https://docs.datadoghq.com/logs/search_syntax/).
  * `index_name` For multi-index organizations, the log index in which the request is performed.
  * `rollup_method` The stats roll-up method - supports `count`, `avg` and `cardinality`.
  * `measure` For `avg` and cardinality `rollup_method` - specify the measure or the facet name you want to use.
  * `time_window` #m (between 1 and 2880), #h (between 1 and 48).
  * `operator` `<`, `<=`, `>`, `>=`, `==`, or `!=`.
  * `#` an integer or decimal number used to set the threshold.


##### [Composite Query](https://docs.datadoghq.com/api/latest/monitors/#composite-query)
Example: `12345 && 67890`, where `12345` and `67890` are the IDs of non-composite monitors
  * `name` [_required_ , _default_ = **dynamic, based on query**]: The name of the alert.
  * `message` [_required_ , _default_ = **dynamic, based on query**]: A message to include with notifications for this monitor. Email notifications can be sent to specific users by using the same ‘@username’ notation as events.
  * `tags` [_optional_ , _default_ = **empty list**]: A list of tags to associate with your monitor. When getting all monitor details via the API, use the `monitor_tags` argument to filter results by these tags. It is only available via the API and isn’t visible or editable in the Datadog UI.


##### [SLO Alert Query](https://docs.datadoghq.com/api/latest/monitors/#slo-alert-query)
Example: `error_budget("slo_id").over("time_window") operator #`
  * `slo_id`: The alphanumeric SLO ID of the SLO you are configuring the alert for.
  * `time_window`: The time window of the SLO target you wish to alert on. Valid options: `7d`, `30d`, `90d`.
  * `operator`: `>=` or `>`


##### [Audit Alert Query](https://docs.datadoghq.com/api/latest/monitors/#audit-alert-query)
Example: `audits(query).rollup(rollup_method[, measure]).last(time_window) operator #`
  * `query` The search query - following the [Log search syntax](https://docs.datadoghq.com/logs/search_syntax/).
  * `rollup_method` The stats roll-up method - supports `count`, `avg` and `cardinality`.
  * `measure` For `avg` and cardinality `rollup_method` - specify the measure or the facet name you want to use.
  * `time_window` #m (between 1 and 2880), #h (between 1 and 48).
  * `operator` `<`, `<=`, `>`, `>=`, `==`, or `!=`.
  * `#` an integer or decimal number used to set the threshold.


##### [CI Pipelines Alert Query](https://docs.datadoghq.com/api/latest/monitors/#ci-pipelines-alert-query)
Example: `ci-pipelines(query).rollup(rollup_method[, measure]).last(time_window) operator #`
  * `query` The search query - following the [Log search syntax](https://docs.datadoghq.com/logs/search_syntax/).
  * `rollup_method` The stats roll-up method - supports `count`, `avg`, and `cardinality`.
  * `measure` For `avg` and cardinality `rollup_method` - specify the measure or the facet name you want to use.
  * `time_window` #m (between 1 and 2880), #h (between 1 and 48).
  * `operator` `<`, `<=`, `>`, `>=`, `==`, or `!=`.
  * `#` an integer or decimal number used to set the threshold.


##### [CI Tests Alert Query](https://docs.datadoghq.com/api/latest/monitors/#ci-tests-alert-query)
Example: `ci-tests(query).rollup(rollup_method[, measure]).last(time_window) operator #`
  * `query` The search query - following the [Log search syntax](https://docs.datadoghq.com/logs/search_syntax/).
  * `rollup_method` The stats roll-up method - supports `count`, `avg`, and `cardinality`.
  * `measure` For `avg` and cardinality `rollup_method` - specify the measure or the facet name you want to use.
  * `time_window` #m (between 1 and 2880), #h (between 1 and 48).
  * `operator` `<`, `<=`, `>`, `>=`, `==`, or `!=`.
  * `#` an integer or decimal number used to set the threshold.


##### [Error Tracking Alert Query](https://docs.datadoghq.com/api/latest/monitors/#error-tracking-alert-query)
“New issue” example: `error-tracking(query).source(issue_source).new().rollup(rollup_method[, measure]).by(group_by).last(time_window) operator #` “High impact issue” example: `error-tracking(query).source(issue_source).impact().rollup(rollup_method[, measure]).by(group_by).last(time_window) operator #`
  * `query` The search query - following the [Log search syntax](https://docs.datadoghq.com/logs/search_syntax/).
  * `issue_source` The issue source - supports `all`, `browser`, `mobile` and `backend` and defaults to `all` if omitted.
  * `rollup_method` The stats roll-up method - supports `count`, `avg`, and `cardinality` and defaults to `count` if omitted.
  * `measure` For `avg` and cardinality `rollup_method` - specify the measure or the facet name you want to use.
  * `group by` Comma-separated list of attributes to group by - should contain at least `issue.id`.
  * `time_window` #m (between 1 and 2880), #h (between 1 and 48).
  * `operator` `<`, `<=`, `>`, `>=`, `==`, or `!=`.
  * `#` an integer or decimal number used to set the threshold.


**Database Monitoring Alert Query**
Example: `database-monitoring(query).rollup(rollup_method[, measure]).last(time_window) operator #`
  * `query` The search query - following the [Log search syntax](https://docs.datadoghq.com/logs/search_syntax/).
  * `rollup_method` The stats roll-up method - supports `count`, `avg`, and `cardinality`.
  * `measure` For `avg` and cardinality `rollup_method` - specify the measure or the facet name you want to use.
  * `time_window` #m (between 1 and 2880), #h (between 1 and 48).
  * `operator` `<`, `<=`, `>`, `>=`, `==`, or `!=`.
  * `#` an integer or decimal number used to set the threshold.


**Network Performance Alert Query**
Example: `network-performance(query).rollup(rollup_method[, measure]).last(time_window) operator #`
  * `query` The search query - following the [Log search syntax](https://docs.datadoghq.com/logs/search_syntax/).
  * `rollup_method` The stats roll-up method - supports `count`, `avg`, and `cardinality`.
  * `measure` For `avg` and cardinality `rollup_method` - specify the measure or the facet name you want to use.
  * `time_window` #m (between 1 and 2880), #h (between 1 and 48).
  * `operator` `<`, `<=`, `>`, `>=`, `==`, or `!=`.
  * `#` an integer or decimal number used to set the threshold.


**Cost Alert Query**
Example: `formula(query).timeframe_type(time_window).function(parameter) operator #`
  * `query` The search query - following the [Log search syntax](https://docs.datadoghq.com/logs/search_syntax/).
  * `timeframe_type` The timeframe type to evaluate the cost - for `forecast` supports `current` - for `change`, `anomaly`, `threshold` supports `last`
  * `time_window` - supports daily roll-up e.g. `7d`
  * `function` - [optional, defaults to `threshold` monitor if omitted] supports `change`, `anomaly`, `forecast`
  * `parameter` Specify the parameter of the type
    * for `change`:
      * supports `relative`, `absolute`
      * [optional] supports `#`, where `#` is an integer or decimal number used to set the threshold
    * for `anomaly`:
      * supports `direction=both`, `direction=above`, `direction=below`
      * [optional] supports `threshold=#`, where `#` is an integer or decimal number used to set the threshold
  * `operator`
    * for `threshold` supports `<`, `<=`, `>`, `>=`, `==`, or `!=`
    * for `change` supports `>`, `<`
    * for `anomaly` supports `>=`
    * for `forecast` supports `>`
  * `#` an integer or decimal number used to set the threshold.

This endpoint requires the `monitors_write` permission.
OAuth apps require the `monitors_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#monitors) to access this endpoint.
### Request
#### Body Data (required)
Create a monitor request body.
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


Field
Type
Description
assets
[object]
The list of monitor assets tied to a monitor, which represents key links for users to take action on monitor alerts (for example, runbooks).
category [_required_]
enum
Indicates the type of asset this entity represents on a monitor. Allowed enum values: `runbook`
name [_required_]
string
Name for the monitor asset
resource_key
string
Represents the identifier of the internal Datadog resource that this asset represents. IDs in this field should be passed in as strings.
resource_type
enum
Type of internal Datadog resource associated with a monitor asset. Allowed enum values: `notebook`
url [_required_]
string
URL link for the asset. For links with an internal resource type set, this should be the relative path to where the Datadog domain is appended internally. For external links, this should be the full URL path.
created
date-time
Timestamp of the monitor creation.
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
deleted
date-time
Whether or not the monitor is deleted. (Always `null`)
draft_status
enum
Indicates whether the monitor is in a draft or published state.
`draft`: The monitor appears as Draft and does not send notifications. `published`: The monitor is active and evaluates conditions and notify as configured.
This field is in preview. The draft value is only available to customers with the feature enabled. Allowed enum values: `draft,published`
default: `published`
id
int64
ID of this monitor.
matching_downtimes
[object]
A list of active v1 downtimes that match this monitor.
end
int64
POSIX timestamp to end the downtime.
id [_required_]
int64
The downtime ID.
scope
[string]
The scope(s) to which the downtime applies. Must be in `key:value` format. For example, `host:app2`. Provide multiple scopes as a comma-separated list like `env:dev,env:prod`. The resulting downtime applies to sources that matches ALL provided scopes (`env:dev` **AND** `env:prod`).
start
int64
POSIX timestamp to start the downtime.
message
string
A message to include with notifications for this monitor.
modified
date-time
Last timestamp when the monitor was edited.
multi
boolean
Whether or not the monitor is broken down on different groups.
name
string
The monitor name.
options
object
List of options associated with your monitor.
aggregation
object
Type of aggregation performed in the monitor query.
group_by
string
Group to break down the monitor on.
metric
string
Metric name used in the monitor.
type
string
Metric type used in the monitor.
device_ids
[string]
**DEPRECATED** : IDs of the device the Synthetics monitor is running on.
enable_logs_sample
boolean
Whether or not to send a log sample when the log monitor triggers.
enable_samples
boolean
Whether or not to send a list of samples when the monitor triggers. This is only used by CI Test and Pipeline monitors.
escalation_message
string
We recommend using the [is_renotify](https://docs.datadoghq.com/monitors/notify/?tab=is_alert#renotify), block in the original message instead. A message to include with a re-notification. Supports the `@username` notification we allow elsewhere. Not applicable if `renotify_interval` is `None`.
evaluation_delay
int64
Time (in seconds) to delay evaluation, as a non-negative integer. For example, if the value is set to `300` (5min), the timeframe is set to `last_5m` and the time is 7:00, the monitor evaluates data from 6:50 to 6:55. This is useful for AWS CloudWatch and other backfilled metrics to ensure the monitor always has data during evaluation.
group_retention_duration
string
The time span after which groups with missing data are dropped from the monitor state. The minimum value is one hour, and the maximum value is 72 hours. Example values are: "60m", "1h", and "2d". This option is only available for APM Trace Analytics, Audit Trail, CI, Error Tracking, Event, Logs, and RUM monitors.
groupby_simple_monitor
boolean
**DEPRECATED** : Whether the log alert monitor triggers a single alert or multiple alerts when any group breaches a threshold. Use `notify_by` instead.
include_tags
boolean
A Boolean indicating whether notifications from this monitor automatically inserts its triggering tags into the title.
**Examples**
  * If `True`, `[Triggered on {host:h1}] Monitor Title`
  * If `False`, `[Triggered] Monitor Title`


default: `true`
locked
boolean
**DEPRECATED** : Whether or not the monitor is locked (only editable by creator and admins). Use `restricted_roles` instead.
min_failure_duration
int64
How long the test should be in failure before alerting (integer, number of seconds, max 7200).
min_location_failed
int64
The minimum number of locations in failure at the same time during at least one moment in the `min_failure_duration` period (`min_location_failed` and `min_failure_duration` are part of the advanced alerting rules - integer, >= 1).
default: `1`
new_group_delay
int64
Time (in seconds) to skip evaluations for new groups.
For example, this option can be used to skip evaluations for new hosts while they initialize.
Must be a non negative integer.
new_host_delay
int64
**DEPRECATED** : Time (in seconds) to allow a host to boot and applications to fully start before starting the evaluation of monitor results. Should be a non negative integer.
Use new_group_delay instead.
default: `300`
no_data_timeframe
int64
The number of minutes before a monitor notifies after data stops reporting. Datadog recommends at least 2x the monitor timeframe for query alerts or 2 minutes for service checks. If omitted, 2x the evaluation timeframe is used for query alerts, and 24 hours is used for service checks.
notification_preset_name
enum
Toggles the display of additional content sent in the monitor notification. Allowed enum values: `show_all,hide_query,hide_handles,hide_all`
default: `show_all`
notify_audit
boolean
A Boolean indicating whether tagged users is notified on changes to this monitor.
notify_by
[string]
Controls what granularity a monitor alerts on. Only available for monitors with groupings. For instance, a monitor grouped by `cluster`, `namespace`, and `pod` can be configured to only notify on each new `cluster` violating the alert conditions by setting `notify_by` to `["cluster"]`. Tags mentioned in `notify_by` must be a subset of the grouping tags in the query. For example, a query grouped by `cluster` and `namespace` cannot notify on `region`. Setting `notify_by` to `["*"]` configures the monitor to notify as a simple-alert.
notify_no_data
boolean
A Boolean indicating whether this monitor notifies when data stops reporting. Defaults to `false`.
on_missing_data
enum
Controls how groups or monitors are treated if an evaluation does not return any data points. The default option results in different behavior depending on the monitor query type. For monitors using Count queries, an empty monitor evaluation is treated as 0 and is compared to the threshold conditions. For monitors using any query type other than Count, for example Gauge, Measure, or Rate, the monitor shows the last known status. This option is only available for APM Trace Analytics, Audit Trail, CI, Error Tracking, Event, Logs, and RUM monitors. Allowed enum values: `default,show_no_data,show_and_notify_no_data,resolve`
renotify_interval
int64
The number of minutes after the last notification before a monitor re-notifies on the current status. It only re-notifies if it’s not resolved.
renotify_occurrences
int64
The number of times re-notification messages should be sent on the current status at the provided re-notification interval.
renotify_statuses
[string]
The types of monitor statuses for which re-notification messages are sent. Default: **null** if `renotify_interval` is **null**. If `renotify_interval` is set, defaults to renotify on `Alert` and `No Data`.
require_full_window
boolean
A Boolean indicating whether this monitor needs a full window of data before it’s evaluated. We highly recommend you set this to `false` for sparse metrics, otherwise some evaluations are skipped. Default is false. This setting only applies to metric monitors.
scheduling_options
object
Configuration options for scheduling.
custom_schedule
object
Configuration options for the custom schedule. **This feature is in private beta.**
recurrences
[object]
Array of custom schedule recurrences.
rrule
string
Defines the recurrence rule (RRULE) for a given schedule.
start
string
Defines the start date and time of the recurring schedule.
timezone
string
Defines the timezone the schedule runs on.
evaluation_window
object
Configuration options for the evaluation window. If `hour_starts` is set, no other fields may be set. Otherwise, `day_starts` and `month_starts` must be set together.
day_starts
string
The time of the day at which a one day cumulative evaluation window starts.
hour_starts
int32
The minute of the hour at which a one hour cumulative evaluation window starts.
month_starts
int32
The day of the month at which a one month cumulative evaluation window starts.
timezone
string
The timezone of the time of the day of the cumulative evaluation window start.
silenced
object
**DEPRECATED** : Information about the downtime applied to the monitor. Only shows v1 downtimes.
<any-key>
int64
UTC epoch timestamp in seconds when the downtime for the group expires.
synthetics_check_id
string
**DEPRECATED** : ID of the corresponding Synthetic check.
threshold_windows
object
Alerting time window options.
recovery_window
string
Describes how long an anomalous metric must be normal before the alert recovers.
trigger_window
string
Describes how long a metric must be anomalous before an alert triggers.
thresholds
object
List of the different monitor threshold available.
critical
double
The monitor `CRITICAL` threshold.
critical_recovery
double
The monitor `CRITICAL` recovery threshold.
ok
double
The monitor `OK` threshold.
unknown
double
The monitor UNKNOWN threshold.
warning
double
The monitor `WARNING` threshold.
warning_recovery
double
The monitor `WARNING` recovery threshold.
timeout_h
int64
The number of hours of the monitor not reporting data before it automatically resolves from a triggered state. The minimum allowed value is 0 hours. The maximum allowed value is 24 hours.
variables
[ <oneOf>]
List of requests that can be used in the monitor query. **This feature is currently in beta.**
Option 1
object
A formula and functions events query.
compute [_required_]
object
Compute options.
aggregation [_required_]
enum
Aggregation methods for event platform queries. Allowed enum values: `count,cardinality,median,pc75,pc90,pc95,pc98,pc99,sum,min,max,avg`
interval
int64
A time interval in milliseconds.
metric
string
Measurable attribute to compute.
data_source [_required_]
enum
Data source for event platform-based queries. Allowed enum values: `rum,ci_pipelines,ci_tests,audit,events,logs,spans,database_queries,network`
group_by
[object]
Group by options.
facet [_required_]
string
Event facet.
limit
int64
Number of groups to return.
sort
object
Options for sorting group by results.
aggregation [_required_]
enum
Aggregation methods for event platform queries. Allowed enum values: `count,cardinality,median,pc75,pc90,pc95,pc98,pc99,sum,min,max,avg`
metric
string
Metric used for sorting group by results.
order
enum
Direction of sort. Allowed enum values: `asc,desc`
default: `desc`
indexes
[string]
An array of index names to query in the stream. Omit or use `[]` to query all indexes at once.
name [_required_]
string
Name of the query for use in formulas.
search
object
Search options.
query [_required_]
string
Events search string.
Option 2
object
A formula and functions cost query.
aggregator
enum
Aggregation methods for metric queries. Allowed enum values: `avg,sum,max,min,last,area,l2norm,percentile,stddev`
data_source [_required_]
enum
Data source for cost queries. Allowed enum values: `metrics,cloud_cost,datadog_usage`
name [_required_]
string
Name of the query for use in formulas.
query [_required_]
string
The monitor query.
Option 3
object
A formula and functions data quality query.
data_source [_required_]
enum
Data source for data quality queries. Allowed enum values: `data_quality_metrics`
filter [_required_]
string
Filter expression used to match on data entities. Uses Aastra query syntax.
group_by
[string]
Optional grouping fields for aggregation.
measure [_required_]
string
The data quality measure to query. Common values include: `bytes`, `cardinality`, `custom`, `freshness`, `max`, `mean`, `min`, `nullness`, `percent_negative`, `percent_zero`, `row_count`, `stddev`, `sum`, `uniqueness`. Additional values may be supported.
monitor_options
object
Monitor configuration options for data quality queries.
crontab_override
string
Crontab expression to override the default schedule.
custom_sql
string
Custom SQL query for the monitor.
custom_where
string
Custom WHERE clause for the query.
group_by_columns
[string]
Columns to group results by.
model_type_override
enum
Override for the model type used in anomaly detection. Allowed enum values: `freshness,percentage,any`
name [_required_]
string
Name of the query for use in formulas.
schema_version
string
Schema version for the data quality query.
scope
string
Optional scoping expression to further filter metrics. Uses metrics filter syntax. This is useful when an entity has been configured to emit metrics with additional tags.
overall_state
enum
The different states your monitor can be in. Allowed enum values: `Alert,Ignored,No Data,OK,Skipped,Unknown,Warn`
priority
int64
Integer from 1 (high) to 5 (low) indicating alert severity.
query [_required_]
string
The monitor query.
restricted_roles
[string]
A list of unique role identifiers to define which roles are allowed to edit the monitor. The unique identifiers for all roles can be pulled from the [Roles API](https://docs.datadoghq.com/api/latest/roles/#list-roles) and are located in the `data.id` field. Editing a monitor includes any updates to the monitor configuration, monitor deletion, and muting of the monitor for any amount of time. You can use the [Restriction Policies API](https://docs.datadoghq.com/api/latest/restriction-policies/) to manage write authorization for individual monitors by teams and users, in addition to roles.
state
object
Wrapper object with the different monitor states.
groups
object
Dictionary where the keys are groups (comma separated lists of tags) and the values are the list of groups your monitor is broken down on.
<any-key>
object
Monitor state for a single group.
last_nodata_ts
int64
Latest timestamp the monitor was in NO_DATA state.
last_notified_ts
int64
Latest timestamp of the notification sent for this monitor group.
last_resolved_ts
int64
Latest timestamp the monitor group was resolved.
last_triggered_ts
int64
Latest timestamp the monitor group triggered.
name
string
The name of the monitor.
status
enum
The different states your monitor can be in. Allowed enum values: `Alert,Ignored,No Data,OK,Skipped,Unknown,Warn`
tags
[string]
Tags associated to your monitor.
type [_required_]
enum
The type of the monitor. For more information about `type`, see the [monitor options](https://docs.datadoghq.com/monitors/guide/monitor_api_options/) docs. Allowed enum values: `composite,event alert,log alert,metric alert,process alert,query alert,rum alert,service check,synthetics alert,trace-analytics alert,slo alert,event-v2 alert,audit alert,ci-pipelines alert,ci-tests alert,error-tracking alert,database-monitoring alert,network-performance alert,cost alert,data-quality alert`
#####  Create a Cost Monitor returns "OK" response
```
{
  "name": "Example Monitor",
  "type": "cost alert",
  "query": "formula(\"exclude_null(query1)\").last(\"7d\").anomaly(direction=\"above\", threshold=10) >= 5",
  "message": "some message Notify: @hipchat-channel",
  "tags": [
    "test:examplemonitor",
    "env:ci"
  ],
  "priority": 3,
  "options": {
    "thresholds": {
      "critical": 5,
      "warning": 3
    },
    "variables": [
      {
        "data_source": "cloud_cost",
        "query": "sum:aws.cost.net.amortized.shared.resources.allocated{aws_product IN (amplify ,athena, backup, bedrock ) } by {aws_product}.rollup(sum, 86400)",
        "name": "query1",
        "aggregator": "sum"
      }
    ],
    "include_tags": true
  }
}
```

Copy
#####  Create a Data Quality monitor returns "OK" response
```
{
  "name": "Example-Monitor",
  "type": "data-quality alert",
  "query": "formula(\"query1\").last(\"5m\") > 100",
  "message": "Data quality alert triggered",
  "tags": [
    "test:examplemonitor",
    "env:ci"
  ],
  "priority": 3,
  "options": {
    "thresholds": {
      "critical": 100
    },
    "variables": [
      {
        "name": "query1",
        "data_source": "data_quality_metrics",
        "measure": "row_count",
        "filter": "search for column where `database:production AND table:users`",
        "group_by": [
          "entity_id"
        ]
      }
    ]
  }
}
```

Copy
#####  Create a RUM formula and functions monitor returns "OK" response
```
{
  "name": "Example-Monitor",
  "type": "rum alert",
  "query": "formula(\"query2 / query1 * 100\").last(\"15m\") >= 0.8",
  "message": "some message Notify: @hipchat-channel",
  "tags": [
    "test:examplemonitor",
    "env:ci"
  ],
  "priority": 3,
  "options": {
    "thresholds": {
      "critical": 0.8
    },
    "variables": [
      {
        "data_source": "rum",
        "name": "query2",
        "search": {
          "query": ""
        },
        "indexes": [
          "*"
        ],
        "compute": {
          "aggregation": "count"
        },
        "group_by": []
      },
      {
        "data_source": "rum",
        "name": "query1",
        "search": {
          "query": "status:error"
        },
        "indexes": [
          "*"
        ],
        "compute": {
          "aggregation": "count"
        },
        "group_by": []
      }
    ]
  }
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/monitors/#CreateMonitor-200-v1)
  * [400](https://docs.datadoghq.com/api/latest/monitors/#CreateMonitor-400-v1)
  * [403](https://docs.datadoghq.com/api/latest/monitors/#CreateMonitor-403-v1)
  * [429](https://docs.datadoghq.com/api/latest/monitors/#CreateMonitor-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


Object describing a monitor.
Field
Type
Description
assets
[object]
The list of monitor assets tied to a monitor, which represents key links for users to take action on monitor alerts (for example, runbooks).
category [_required_]
enum
Indicates the type of asset this entity represents on a monitor. Allowed enum values: `runbook`
name [_required_]
string
Name for the monitor asset
resource_key
string
Represents the identifier of the internal Datadog resource that this asset represents. IDs in this field should be passed in as strings.
resource_type
enum
Type of internal Datadog resource associated with a monitor asset. Allowed enum values: `notebook`
url [_required_]
string
URL link for the asset. For links with an internal resource type set, this should be the relative path to where the Datadog domain is appended internally. For external links, this should be the full URL path.
created
date-time
Timestamp of the monitor creation.
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
deleted
date-time
Whether or not the monitor is deleted. (Always `null`)
draft_status
enum
Indicates whether the monitor is in a draft or published state.
`draft`: The monitor appears as Draft and does not send notifications. `published`: The monitor is active and evaluates conditions and notify as configured.
This field is in preview. The draft value is only available to customers with the feature enabled. Allowed enum values: `draft,published`
default: `published`
id
int64
ID of this monitor.
matching_downtimes
[object]
A list of active v1 downtimes that match this monitor.
end
int64
POSIX timestamp to end the downtime.
id [_required_]
int64
The downtime ID.
scope
[string]
The scope(s) to which the downtime applies. Must be in `key:value` format. For example, `host:app2`. Provide multiple scopes as a comma-separated list like `env:dev,env:prod`. The resulting downtime applies to sources that matches ALL provided scopes (`env:dev` **AND** `env:prod`).
start
int64
POSIX timestamp to start the downtime.
message
string
A message to include with notifications for this monitor.
modified
date-time
Last timestamp when the monitor was edited.
multi
boolean
Whether or not the monitor is broken down on different groups.
name
string
The monitor name.
options
object
List of options associated with your monitor.
aggregation
object
Type of aggregation performed in the monitor query.
group_by
string
Group to break down the monitor on.
metric
string
Metric name used in the monitor.
type
string
Metric type used in the monitor.
device_ids
[string]
**DEPRECATED** : IDs of the device the Synthetics monitor is running on.
enable_logs_sample
boolean
Whether or not to send a log sample when the log monitor triggers.
enable_samples
boolean
Whether or not to send a list of samples when the monitor triggers. This is only used by CI Test and Pipeline monitors.
escalation_message
string
We recommend using the [is_renotify](https://docs.datadoghq.com/monitors/notify/?tab=is_alert#renotify), block in the original message instead. A message to include with a re-notification. Supports the `@username` notification we allow elsewhere. Not applicable if `renotify_interval` is `None`.
evaluation_delay
int64
Time (in seconds) to delay evaluation, as a non-negative integer. For example, if the value is set to `300` (5min), the timeframe is set to `last_5m` and the time is 7:00, the monitor evaluates data from 6:50 to 6:55. This is useful for AWS CloudWatch and other backfilled metrics to ensure the monitor always has data during evaluation.
group_retention_duration
string
The time span after which groups with missing data are dropped from the monitor state. The minimum value is one hour, and the maximum value is 72 hours. Example values are: "60m", "1h", and "2d". This option is only available for APM Trace Analytics, Audit Trail, CI, Error Tracking, Event, Logs, and RUM monitors.
groupby_simple_monitor
boolean
**DEPRECATED** : Whether the log alert monitor triggers a single alert or multiple alerts when any group breaches a threshold. Use `notify_by` instead.
include_tags
boolean
A Boolean indicating whether notifications from this monitor automatically inserts its triggering tags into the title.
**Examples**
  * If `True`, `[Triggered on {host:h1}] Monitor Title`
  * If `False`, `[Triggered] Monitor Title`


default: `true`
locked
boolean
**DEPRECATED** : Whether or not the monitor is locked (only editable by creator and admins). Use `restricted_roles` instead.
min_failure_duration
int64
How long the test should be in failure before alerting (integer, number of seconds, max 7200).
min_location_failed
int64
The minimum number of locations in failure at the same time during at least one moment in the `min_failure_duration` period (`min_location_failed` and `min_failure_duration` are part of the advanced alerting rules - integer, >= 1).
default: `1`
new_group_delay
int64
Time (in seconds) to skip evaluations for new groups.
For example, this option can be used to skip evaluations for new hosts while they initialize.
Must be a non negative integer.
new_host_delay
int64
**DEPRECATED** : Time (in seconds) to allow a host to boot and applications to fully start before starting the evaluation of monitor results. Should be a non negative integer.
Use new_group_delay instead.
default: `300`
no_data_timeframe
int64
The number of minutes before a monitor notifies after data stops reporting. Datadog recommends at least 2x the monitor timeframe for query alerts or 2 minutes for service checks. If omitted, 2x the evaluation timeframe is used for query alerts, and 24 hours is used for service checks.
notification_preset_name
enum
Toggles the display of additional content sent in the monitor notification. Allowed enum values: `show_all,hide_query,hide_handles,hide_all`
default: `show_all`
notify_audit
boolean
A Boolean indicating whether tagged users is notified on changes to this monitor.
notify_by
[string]
Controls what granularity a monitor alerts on. Only available for monitors with groupings. For instance, a monitor grouped by `cluster`, `namespace`, and `pod` can be configured to only notify on each new `cluster` violating the alert conditions by setting `notify_by` to `["cluster"]`. Tags mentioned in `notify_by` must be a subset of the grouping tags in the query. For example, a query grouped by `cluster` and `namespace` cannot notify on `region`. Setting `notify_by` to `["*"]` configures the monitor to notify as a simple-alert.
notify_no_data
boolean
A Boolean indicating whether this monitor notifies when data stops reporting. Defaults to `false`.
on_missing_data
enum
Controls how groups or monitors are treated if an evaluation does not return any data points. The default option results in different behavior depending on the monitor query type. For monitors using Count queries, an empty monitor evaluation is treated as 0 and is compared to the threshold conditions. For monitors using any query type other than Count, for example Gauge, Measure, or Rate, the monitor shows the last known status. This option is only available for APM Trace Analytics, Audit Trail, CI, Error Tracking, Event, Logs, and RUM monitors. Allowed enum values: `default,show_no_data,show_and_notify_no_data,resolve`
renotify_interval
int64
The number of minutes after the last notification before a monitor re-notifies on the current status. It only re-notifies if it’s not resolved.
renotify_occurrences
int64
The number of times re-notification messages should be sent on the current status at the provided re-notification interval.
renotify_statuses
[string]
The types of monitor statuses for which re-notification messages are sent. Default: **null** if `renotify_interval` is **null**. If `renotify_interval` is set, defaults to renotify on `Alert` and `No Data`.
require_full_window
boolean
A Boolean indicating whether this monitor needs a full window of data before it’s evaluated. We highly recommend you set this to `false` for sparse metrics, otherwise some evaluations are skipped. Default is false. This setting only applies to metric monitors.
scheduling_options
object
Configuration options for scheduling.
custom_schedule
object
Configuration options for the custom schedule. **This feature is in private beta.**
recurrences
[object]
Array of custom schedule recurrences.
rrule
string
Defines the recurrence rule (RRULE) for a given schedule.
start
string
Defines the start date and time of the recurring schedule.
timezone
string
Defines the timezone the schedule runs on.
evaluation_window
object
Configuration options for the evaluation window. If `hour_starts` is set, no other fields may be set. Otherwise, `day_starts` and `month_starts` must be set together.
day_starts
string
The time of the day at which a one day cumulative evaluation window starts.
hour_starts
int32
The minute of the hour at which a one hour cumulative evaluation window starts.
month_starts
int32
The day of the month at which a one month cumulative evaluation window starts.
timezone
string
The timezone of the time of the day of the cumulative evaluation window start.
silenced
object
**DEPRECATED** : Information about the downtime applied to the monitor. Only shows v1 downtimes.
<any-key>
int64
UTC epoch timestamp in seconds when the downtime for the group expires.
synthetics_check_id
string
**DEPRECATED** : ID of the corresponding Synthetic check.
threshold_windows
object
Alerting time window options.
recovery_window
string
Describes how long an anomalous metric must be normal before the alert recovers.
trigger_window
string
Describes how long a metric must be anomalous before an alert triggers.
thresholds
object
List of the different monitor threshold available.
critical
double
The monitor `CRITICAL` threshold.
critical_recovery
double
The monitor `CRITICAL` recovery threshold.
ok
double
The monitor `OK` threshold.
unknown
double
The monitor UNKNOWN threshold.
warning
double
The monitor `WARNING` threshold.
warning_recovery
double
The monitor `WARNING` recovery threshold.
timeout_h
int64
The number of hours of the monitor not reporting data before it automatically resolves from a triggered state. The minimum allowed value is 0 hours. The maximum allowed value is 24 hours.
variables
[ <oneOf>]
List of requests that can be used in the monitor query. **This feature is currently in beta.**
Option 1
object
A formula and functions events query.
compute [_required_]
object
Compute options.
aggregation [_required_]
enum
Aggregation methods for event platform queries. Allowed enum values: `count,cardinality,median,pc75,pc90,pc95,pc98,pc99,sum,min,max,avg`
interval
int64
A time interval in milliseconds.
metric
string
Measurable attribute to compute.
data_source [_required_]
enum
Data source for event platform-based queries. Allowed enum values: `rum,ci_pipelines,ci_tests,audit,events,logs,spans,database_queries,network`
group_by
[object]
Group by options.
facet [_required_]
string
Event facet.
limit
int64
Number of groups to return.
sort
object
Options for sorting group by results.
aggregation [_required_]
enum
Aggregation methods for event platform queries. Allowed enum values: `count,cardinality,median,pc75,pc90,pc95,pc98,pc99,sum,min,max,avg`
metric
string
Metric used for sorting group by results.
order
enum
Direction of sort. Allowed enum values: `asc,desc`
default: `desc`
indexes
[string]
An array of index names to query in the stream. Omit or use `[]` to query all indexes at once.
name [_required_]
string
Name of the query for use in formulas.
search
object
Search options.
query [_required_]
string
Events search string.
Option 2
object
A formula and functions cost query.
aggregator
enum
Aggregation methods for metric queries. Allowed enum values: `avg,sum,max,min,last,area,l2norm,percentile,stddev`
data_source [_required_]
enum
Data source for cost queries. Allowed enum values: `metrics,cloud_cost,datadog_usage`
name [_required_]
string
Name of the query for use in formulas.
query [_required_]
string
The monitor query.
Option 3
object
A formula and functions data quality query.
data_source [_required_]
enum
Data source for data quality queries. Allowed enum values: `data_quality_metrics`
filter [_required_]
string
Filter expression used to match on data entities. Uses Aastra query syntax.
group_by
[string]
Optional grouping fields for aggregation.
measure [_required_]
string
The data quality measure to query. Common values include: `bytes`, `cardinality`, `custom`, `freshness`, `max`, `mean`, `min`, `nullness`, `percent_negative`, `percent_zero`, `row_count`, `stddev`, `sum`, `uniqueness`. Additional values may be supported.
monitor_options
object
Monitor configuration options for data quality queries.
crontab_override
string
Crontab expression to override the default schedule.
custom_sql
string
Custom SQL query for the monitor.
custom_where
string
Custom WHERE clause for the query.
group_by_columns
[string]
Columns to group results by.
model_type_override
enum
Override for the model type used in anomaly detection. Allowed enum values: `freshness,percentage,any`
name [_required_]
string
Name of the query for use in formulas.
schema_version
string
Schema version for the data quality query.
scope
string
Optional scoping expression to further filter metrics. Uses metrics filter syntax. This is useful when an entity has been configured to emit metrics with additional tags.
overall_state
enum
The different states your monitor can be in. Allowed enum values: `Alert,Ignored,No Data,OK,Skipped,Unknown,Warn`
priority
int64
Integer from 1 (high) to 5 (low) indicating alert severity.
query [_required_]
string
The monitor query.
restricted_roles
[string]
A list of unique role identifiers to define which roles are allowed to edit the monitor. The unique identifiers for all roles can be pulled from the [Roles API](https://docs.datadoghq.com/api/latest/roles/#list-roles) and are located in the `data.id` field. Editing a monitor includes any updates to the monitor configuration, monitor deletion, and muting of the monitor for any amount of time. You can use the [Restriction Policies API](https://docs.datadoghq.com/api/latest/restriction-policies/) to manage write authorization for individual monitors by teams and users, in addition to roles.
state
object
Wrapper object with the different monitor states.
groups
object
Dictionary where the keys are groups (comma separated lists of tags) and the values are the list of groups your monitor is broken down on.
<any-key>
object
Monitor state for a single group.
last_nodata_ts
int64
Latest timestamp the monitor was in NO_DATA state.
last_notified_ts
int64
Latest timestamp of the notification sent for this monitor group.
last_resolved_ts
int64
Latest timestamp the monitor group was resolved.
last_triggered_ts
int64
Latest timestamp the monitor group triggered.
name
string
The name of the monitor.
status
enum
The different states your monitor can be in. Allowed enum values: `Alert,Ignored,No Data,OK,Skipped,Unknown,Warn`
tags
[string]
Tags associated to your monitor.
type [_required_]
enum
The type of the monitor. For more information about `type`, see the [monitor options](https://docs.datadoghq.com/monitors/guide/monitor_api_options/) docs. Allowed enum values: `composite,event alert,log alert,metric alert,process alert,query alert,rum alert,service check,synthetics alert,trace-analytics alert,slo alert,event-v2 alert,audit alert,ci-pipelines alert,ci-tests alert,error-tracking alert,database-monitoring alert,network-performance alert,cost alert,data-quality alert`
```
{
  "assets": [
    {
      "category": "runbook",
      "name": "Monitor Runbook",
      "resource_key": "12345",
      "resource_type": "string",
      "url": "/notebooks/12345"
    }
  ],
  "created": "2019-09-19T10:00:00.000Z",
  "creator": {
    "email": "string",
    "handle": "string",
    "name": "string"
  },
  "deleted": "2019-09-19T10:00:00.000Z",
  "draft_status": "string",
  "id": "integer",
  "matching_downtimes": [
    {
      "end": 1412792983,
      "id": 1625,
      "scope": [
        "env:staging"
      ],
      "start": 1412792983
    }
  ],
  "message": "string",
  "modified": "2019-09-19T10:00:00.000Z",
  "multi": false,
  "name": "My monitor",
  "options": {
    "aggregation": {
      "group_by": "host",
      "metric": "metrics.name",
      "type": "count"
    },
    "device_ids": [],
    "enable_logs_sample": false,
    "enable_samples": false,
    "escalation_message": "string",
    "evaluation_delay": "integer",
    "group_retention_duration": "string",
    "groupby_simple_monitor": false,
    "include_tags": false,
    "locked": false,
    "min_failure_duration": "integer",
    "min_location_failed": "integer",
    "new_group_delay": "integer",
    "new_host_delay": "integer",
    "no_data_timeframe": "integer",
    "notification_preset_name": "string",
    "notify_audit": false,
    "notify_by": [],
    "notify_no_data": false,
    "on_missing_data": "string",
    "renotify_interval": "integer",
    "renotify_occurrences": "integer",
    "renotify_statuses": [],
    "require_full_window": false,
    "scheduling_options": {
      "custom_schedule": {
        "recurrences": [
          {
            "rrule": "FREQ=WEEKLY;BYDAY=MO,TU,WE,TH,FR",
            "start": "2023-08-31T16:30:00",
            "timezone": "Europe/Paris"
          }
        ]
      },
      "evaluation_window": {
        "day_starts": "04:00",
        "hour_starts": 0,
        "month_starts": 1,
        "timezone": "Europe/Paris"
      }
    },
    "silenced": {
      "<any-key>": "integer"
    },
    "synthetics_check_id": "string",
    "threshold_windows": {
      "recovery_window": "string",
      "trigger_window": "string"
    },
    "thresholds": {
      "critical": "number",
      "critical_recovery": "number",
      "ok": "number",
      "unknown": "number",
      "warning": "number",
      "warning_recovery": "number"
    },
    "timeout_h": "integer",
    "variables": [
      {
        "compute": {
          "aggregation": "avg",
          "interval": 60000,
          "metric": "@duration"
        },
        "data_source": "rum",
        "group_by": [
          {
            "facet": "status",
            "limit": 10,
            "sort": {
              "aggregation": "avg",
              "metric": "string",
              "order": "string"
            }
          }
        ],
        "indexes": [
          "days-3",
          "days-7"
        ],
        "name": "query_errors",
        "search": {
          "query": "service:query"
        }
      }
    ]
  },
  "overall_state": "string",
  "priority": "integer",
  "query": "avg(last_5m):sum:system.net.bytes_rcvd{host:host0} > 100",
  "restricted_roles": [],
  "state": {
    "groups": {
      "<any-key>": {
        "last_nodata_ts": "integer",
        "last_notified_ts": "integer",
        "last_resolved_ts": "integer",
        "last_triggered_ts": "integer",
        "name": "string",
        "status": "string"
      }
    }
  },
  "tags": [],
  "type": "query alert"
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


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
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


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
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/monitors/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/monitors/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/monitors/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/monitors/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/monitors/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/monitors/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/monitors/?code-lang=typescript)
  * [Python [legacy]](https://docs.datadoghq.com/api/latest/monitors/?code-lang=python-legacy)
  * [Ruby [legacy]](https://docs.datadoghq.com/api/latest/monitors/?code-lang=ruby-legacy)


#####  Create a Cost Monitor returns "OK" response
Copy
```
                          ## json-request-body
# 
  
# Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/monitor" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "message": "You may need to add web hosts if this is consistently high.",
  "name": "Bytes received on host0",
  "options": {
    "no_data_timeframe": 20,
    "notify_no_data": true
  },
  "query": "avg(last_5m):sum:system.net.bytes_rcvd{host:host0} \u003e 100",
  "tags": [
    "app:webserver",
    "frontend"
  ],
  "type": "query alert"
}
EOF  

                        
```

#####  Create a Data Quality monitor returns "OK" response
Copy
```
                          ## json-request-body
# 
  
# Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/monitor" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "message": "You may need to add web hosts if this is consistently high.",
  "name": "Bytes received on host0",
  "options": {
    "no_data_timeframe": 20,
    "notify_no_data": true
  },
  "query": "avg(last_5m):sum:system.net.bytes_rcvd{host:host0} \u003e 100",
  "tags": [
    "app:webserver",
    "frontend"
  ],
  "type": "query alert"
}
EOF  

                        
```

#####  Create a RUM formula and functions monitor returns "OK" response
Copy
```
                          ## json-request-body
# 
  
# Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/monitor" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "message": "You may need to add web hosts if this is consistently high.",
  "name": "Bytes received on host0",
  "options": {
    "no_data_timeframe": 20,
    "notify_no_data": true
  },
  "query": "avg(last_5m):sum:system.net.bytes_rcvd{host:host0} \u003e 100",
  "tags": [
    "app:webserver",
    "frontend"
  ],
  "type": "query alert"
}
EOF  

                        
```

#####  Create a Cost Monitor returns "OK" response 
```
// Create a Cost Monitor returns "OK" response

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
	body := datadogV1.Monitor{
		Name:    datadog.PtrString("Example Monitor"),
		Type:    datadogV1.MONITORTYPE_COST_ALERT,
		Query:   `formula("exclude_null(query1)").last("7d").anomaly(direction="above", threshold=10) >= 5`,
		Message: datadog.PtrString("some message Notify: @hipchat-channel"),
		Tags: []string{
			"test:examplemonitor",
			"env:ci",
		},
		Priority: *datadog.NewNullableInt64(datadog.PtrInt64(3)),
		Options: &datadogV1.MonitorOptions{
			Thresholds: &datadogV1.MonitorThresholds{
				Critical: datadog.PtrFloat64(5),
				Warning:  *datadog.NewNullableFloat64(datadog.PtrFloat64(3)),
			},
			Variables: []datadogV1.MonitorFormulaAndFunctionQueryDefinition{
				datadogV1.MonitorFormulaAndFunctionQueryDefinition{
					MonitorFormulaAndFunctionCostQueryDefinition: &datadogV1.MonitorFormulaAndFunctionCostQueryDefinition{
						DataSource: datadogV1.MONITORFORMULAANDFUNCTIONCOSTDATASOURCE_CLOUD_COST,
						Query:      "sum:aws.cost.net.amortized.shared.resources.allocated{aws_product IN (amplify ,athena, backup, bedrock ) } by {aws_product}.rollup(sum, 86400)",
						Name:       "query1",
						Aggregator: datadogV1.MONITORFORMULAANDFUNCTIONCOSTAGGREGATOR_SUM.Ptr(),
					}},
			},
			IncludeTags: datadog.PtrBool(true),
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV1.NewMonitorsApi(apiClient)
	resp, r, err := api.CreateMonitor(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `MonitorsApi.CreateMonitor`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `MonitorsApi.CreateMonitor`:\n%s\n", responseContent)
}

```

Copy
#####  Create a RUM formula and functions monitor returns "OK" response 
```
// Create a RUM formula and functions monitor returns "OK" response

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
	body := datadogV1.Monitor{
		Name:    datadog.PtrString("Example-Monitor"),
		Type:    datadogV1.MONITORTYPE_RUM_ALERT,
		Query:   `formula("query2 / query1 * 100").last("15m") >= 0.8`,
		Message: datadog.PtrString("some message Notify: @hipchat-channel"),
		Tags: []string{
			"test:examplemonitor",
			"env:ci",
		},
		Priority: *datadog.NewNullableInt64(datadog.PtrInt64(3)),
		Options: &datadogV1.MonitorOptions{
			Thresholds: &datadogV1.MonitorThresholds{
				Critical: datadog.PtrFloat64(0.8),
			},
			Variables: []datadogV1.MonitorFormulaAndFunctionQueryDefinition{
				datadogV1.MonitorFormulaAndFunctionQueryDefinition{
					MonitorFormulaAndFunctionEventQueryDefinition: &datadogV1.MonitorFormulaAndFunctionEventQueryDefinition{
						DataSource: datadogV1.MONITORFORMULAANDFUNCTIONEVENTSDATASOURCE_RUM,
						Name:       "query2",
						Search: &datadogV1.MonitorFormulaAndFunctionEventQueryDefinitionSearch{
							Query: "",
						},
						Indexes: []string{
							"*",
						},
						Compute: datadogV1.MonitorFormulaAndFunctionEventQueryDefinitionCompute{
							Aggregation: datadogV1.MONITORFORMULAANDFUNCTIONEVENTAGGREGATION_COUNT,
						},
						GroupBy: []datadogV1.MonitorFormulaAndFunctionEventQueryGroupBy{},
					}},
				datadogV1.MonitorFormulaAndFunctionQueryDefinition{
					MonitorFormulaAndFunctionEventQueryDefinition: &datadogV1.MonitorFormulaAndFunctionEventQueryDefinition{
						DataSource: datadogV1.MONITORFORMULAANDFUNCTIONEVENTSDATASOURCE_RUM,
						Name:       "query1",
						Search: &datadogV1.MonitorFormulaAndFunctionEventQueryDefinitionSearch{
							Query: "status:error",
						},
						Indexes: []string{
							"*",
						},
						Compute: datadogV1.MonitorFormulaAndFunctionEventQueryDefinitionCompute{
							Aggregation: datadogV1.MONITORFORMULAANDFUNCTIONEVENTAGGREGATION_COUNT,
						},
						GroupBy: []datadogV1.MonitorFormulaAndFunctionEventQueryGroupBy{},
					}},
			},
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV1.NewMonitorsApi(apiClient)
	resp, r, err := api.CreateMonitor(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `MonitorsApi.CreateMonitor`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `MonitorsApi.CreateMonitor`:\n%s\n", responseContent)
}

```

Copy
#####  Create a ci-pipelines formula and functions monitor returns "OK" response 
```
// Create a ci-pipelines formula and functions monitor returns "OK" response

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
	body := datadogV1.Monitor{
		Name:    datadog.PtrString("Example-Monitor"),
		Type:    datadogV1.MONITORTYPE_CI_PIPELINES_ALERT,
		Query:   `formula("query1 / query2 * 100").last("15m") >= 0.8`,
		Message: datadog.PtrString("some message Notify: @hipchat-channel"),
		Tags: []string{
			"test:examplemonitor",
			"env:ci",
		},
		Priority: *datadog.NewNullableInt64(datadog.PtrInt64(3)),
		Options: &datadogV1.MonitorOptions{
			Thresholds: &datadogV1.MonitorThresholds{
				Critical: datadog.PtrFloat64(0.8),
			},
			Variables: []datadogV1.MonitorFormulaAndFunctionQueryDefinition{
				datadogV1.MonitorFormulaAndFunctionQueryDefinition{
					MonitorFormulaAndFunctionEventQueryDefinition: &datadogV1.MonitorFormulaAndFunctionEventQueryDefinition{
						DataSource: datadogV1.MONITORFORMULAANDFUNCTIONEVENTSDATASOURCE_CI_PIPELINES,
						Name:       "query1",
						Search: &datadogV1.MonitorFormulaAndFunctionEventQueryDefinitionSearch{
							Query: "@ci.status:error",
						},
						Indexes: []string{
							"*",
						},
						Compute: datadogV1.MonitorFormulaAndFunctionEventQueryDefinitionCompute{
							Aggregation: datadogV1.MONITORFORMULAANDFUNCTIONEVENTAGGREGATION_COUNT,
						},
						GroupBy: []datadogV1.MonitorFormulaAndFunctionEventQueryGroupBy{},
					}},
				datadogV1.MonitorFormulaAndFunctionQueryDefinition{
					MonitorFormulaAndFunctionEventQueryDefinition: &datadogV1.MonitorFormulaAndFunctionEventQueryDefinition{
						DataSource: datadogV1.MONITORFORMULAANDFUNCTIONEVENTSDATASOURCE_CI_PIPELINES,
						Name:       "query2",
						Search: &datadogV1.MonitorFormulaAndFunctionEventQueryDefinitionSearch{
							Query: "",
						},
						Indexes: []string{
							"*",
						},
						Compute: datadogV1.MonitorFormulaAndFunctionEventQueryDefinitionCompute{
							Aggregation: datadogV1.MONITORFORMULAANDFUNCTIONEVENTAGGREGATION_COUNT,
						},
						GroupBy: []datadogV1.MonitorFormulaAndFunctionEventQueryGroupBy{},
					}},
			},
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV1.NewMonitorsApi(apiClient)
	resp, r, err := api.CreateMonitor(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `MonitorsApi.CreateMonitor`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `MonitorsApi.CreateMonitor`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Create a Cost Monitor returns "OK" response 
```
// Create a Cost Monitor returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.MonitorsApi;
import com.datadog.api.client.v1.model.Monitor;
import com.datadog.api.client.v1.model.MonitorFormulaAndFunctionCostAggregator;
import com.datadog.api.client.v1.model.MonitorFormulaAndFunctionCostDataSource;
import com.datadog.api.client.v1.model.MonitorFormulaAndFunctionCostQueryDefinition;
import com.datadog.api.client.v1.model.MonitorFormulaAndFunctionQueryDefinition;
import com.datadog.api.client.v1.model.MonitorOptions;
import com.datadog.api.client.v1.model.MonitorThresholds;
import com.datadog.api.client.v1.model.MonitorType;
import java.util.Arrays;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    MonitorsApi apiInstance = new MonitorsApi(defaultClient);

    Monitor body =
        new Monitor()
            .name("Example Monitor")
            .type(MonitorType.COST_ALERT)
            .query(
                """
formula("exclude_null(query1)").last("7d").anomaly(direction="above", threshold=10) >= 5
""")
            .message("some message Notify: @hipchat-channel")
            .tags(Arrays.asList("test:examplemonitor", "env:ci"))
            .priority(3L)
            .options(
                new MonitorOptions()
                    .thresholds(new MonitorThresholds().critical(5.0).warning(3.0))
                    .variables(
                        Collections.singletonList(
                            new MonitorFormulaAndFunctionQueryDefinition(
                                new MonitorFormulaAndFunctionCostQueryDefinition()
                                    .dataSource(MonitorFormulaAndFunctionCostDataSource.CLOUD_COST)
                                    .query(
                                        "sum:aws.cost.net.amortized.shared.resources.allocated{aws_product"
                                            + " IN (amplify ,athena, backup, bedrock ) } by"
                                            + " {aws_product}.rollup(sum, 86400)")
                                    .name("query1")
                                    .aggregator(MonitorFormulaAndFunctionCostAggregator.SUM))))
                    .includeTags(true));

    try {
      Monitor result = apiInstance.createMonitor(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MonitorsApi#createMonitor");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}

```

Copy
#####  Create a RUM formula and functions monitor returns "OK" response 
```
// Create a RUM formula and functions monitor returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.MonitorsApi;
import com.datadog.api.client.v1.model.Monitor;
import com.datadog.api.client.v1.model.MonitorFormulaAndFunctionEventAggregation;
import com.datadog.api.client.v1.model.MonitorFormulaAndFunctionEventQueryDefinition;
import com.datadog.api.client.v1.model.MonitorFormulaAndFunctionEventQueryDefinitionCompute;
import com.datadog.api.client.v1.model.MonitorFormulaAndFunctionEventQueryDefinitionSearch;
import com.datadog.api.client.v1.model.MonitorFormulaAndFunctionEventsDataSource;
import com.datadog.api.client.v1.model.MonitorFormulaAndFunctionQueryDefinition;
import com.datadog.api.client.v1.model.MonitorOptions;
import com.datadog.api.client.v1.model.MonitorThresholds;
import com.datadog.api.client.v1.model.MonitorType;
import java.util.Arrays;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    MonitorsApi apiInstance = new MonitorsApi(defaultClient);

    Monitor body =
        new Monitor()
            .name("Example-Monitor")
            .type(MonitorType.RUM_ALERT)
            .query("""
formula("query2 / query1 * 100").last("15m") >= 0.8
""")
            .message("some message Notify: @hipchat-channel")
            .tags(Arrays.asList("test:examplemonitor", "env:ci"))
            .priority(3L)
            .options(
                new MonitorOptions()
                    .thresholds(new MonitorThresholds().critical(0.8))
                    .variables(
                        Arrays.asList(
                            new MonitorFormulaAndFunctionQueryDefinition(
                                new MonitorFormulaAndFunctionEventQueryDefinition()
                                    .dataSource(MonitorFormulaAndFunctionEventsDataSource.RUM)
                                    .name("query2")
                                    .search(
                                        new MonitorFormulaAndFunctionEventQueryDefinitionSearch()
                                            .query(""))
                                    .indexes(Collections.singletonList("*"))
                                    .compute(
                                        new MonitorFormulaAndFunctionEventQueryDefinitionCompute()
                                            .aggregation(
                                                MonitorFormulaAndFunctionEventAggregation.COUNT))),
                            new MonitorFormulaAndFunctionQueryDefinition(
                                new MonitorFormulaAndFunctionEventQueryDefinition()
                                    .dataSource(MonitorFormulaAndFunctionEventsDataSource.RUM)
                                    .name("query1")
                                    .search(
                                        new MonitorFormulaAndFunctionEventQueryDefinitionSearch()
                                            .query("status:error"))
                                    .indexes(Collections.singletonList("*"))
                                    .compute(
                                        new MonitorFormulaAndFunctionEventQueryDefinitionCompute()
                                            .aggregation(
                                                MonitorFormulaAndFunctionEventAggregation
                                                    .COUNT))))));

    try {
      Monitor result = apiInstance.createMonitor(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MonitorsApi#createMonitor");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}

```

Copy
#####  Create a ci-pipelines formula and functions monitor returns "OK" response 
```
// Create a ci-pipelines formula and functions monitor returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.MonitorsApi;
import com.datadog.api.client.v1.model.Monitor;
import com.datadog.api.client.v1.model.MonitorFormulaAndFunctionEventAggregation;
import com.datadog.api.client.v1.model.MonitorFormulaAndFunctionEventQueryDefinition;
import com.datadog.api.client.v1.model.MonitorFormulaAndFunctionEventQueryDefinitionCompute;
import com.datadog.api.client.v1.model.MonitorFormulaAndFunctionEventQueryDefinitionSearch;
import com.datadog.api.client.v1.model.MonitorFormulaAndFunctionEventsDataSource;
import com.datadog.api.client.v1.model.MonitorFormulaAndFunctionQueryDefinition;
import com.datadog.api.client.v1.model.MonitorOptions;
import com.datadog.api.client.v1.model.MonitorThresholds;
import com.datadog.api.client.v1.model.MonitorType;
import java.util.Arrays;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    MonitorsApi apiInstance = new MonitorsApi(defaultClient);

    Monitor body =
        new Monitor()
            .name("Example-Monitor")
            .type(MonitorType.CI_PIPELINES_ALERT)
            .query("""
formula("query1 / query2 * 100").last("15m") >= 0.8
""")
            .message("some message Notify: @hipchat-channel")
            .tags(Arrays.asList("test:examplemonitor", "env:ci"))
            .priority(3L)
            .options(
                new MonitorOptions()
                    .thresholds(new MonitorThresholds().critical(0.8))
                    .variables(
                        Arrays.asList(
                            new MonitorFormulaAndFunctionQueryDefinition(
                                new MonitorFormulaAndFunctionEventQueryDefinition()
                                    .dataSource(
                                        MonitorFormulaAndFunctionEventsDataSource.CI_PIPELINES)
                                    .name("query1")
                                    .search(
                                        new MonitorFormulaAndFunctionEventQueryDefinitionSearch()
                                            .query("@ci.status:error"))
                                    .indexes(Collections.singletonList("*"))
                                    .compute(
                                        new MonitorFormulaAndFunctionEventQueryDefinitionCompute()
                                            .aggregation(
                                                MonitorFormulaAndFunctionEventAggregation.COUNT))),
                            new MonitorFormulaAndFunctionQueryDefinition(
                                new MonitorFormulaAndFunctionEventQueryDefinition()
                                    .dataSource(
                                        MonitorFormulaAndFunctionEventsDataSource.CI_PIPELINES)
                                    .name("query2")
                                    .search(
                                        new MonitorFormulaAndFunctionEventQueryDefinitionSearch()
                                            .query(""))
                                    .indexes(Collections.singletonList("*"))
                                    .compute(
                                        new MonitorFormulaAndFunctionEventQueryDefinitionCompute()
                                            .aggregation(
                                                MonitorFormulaAndFunctionEventAggregation
                                                    .COUNT))))));

    try {
      Monitor result = apiInstance.createMonitor(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MonitorsApi#createMonitor");
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

#####  Create a monitor returns "OK" response
```
from datadog import initialize, api

options = {
    'api_key': '<DATADOG_API_KEY>',
    'app_key': '<DATADOG_APPLICATION_KEY>'
}

initialize(**options)

# Create a new monitor
monitor_options = {
    "notify_no_data": True,
    "no_data_timeframe": 20
}
tags = ["app:webserver", "frontend"]
api.Monitor.create(
    type="query alert",
    query="avg(last_5m):sum:system.net.bytes_rcvd{host:host0} > 100",
    name="Bytes received on host0",
    message="We may need to add web hosts if this is consistently high.",
    tags=tags,
    options=monitor_options
)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python-legacy) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python "example.py"


```

#####  Create a Cost Monitor returns "OK" response 
```
"""
Create a Cost Monitor returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.monitors_api import MonitorsApi
from datadog_api_client.v1.model.monitor import Monitor
from datadog_api_client.v1.model.monitor_formula_and_function_cost_aggregator import (
    MonitorFormulaAndFunctionCostAggregator,
)
from datadog_api_client.v1.model.monitor_formula_and_function_cost_data_source import (
    MonitorFormulaAndFunctionCostDataSource,
)
from datadog_api_client.v1.model.monitor_formula_and_function_cost_query_definition import (
    MonitorFormulaAndFunctionCostQueryDefinition,
)
from datadog_api_client.v1.model.monitor_options import MonitorOptions
from datadog_api_client.v1.model.monitor_thresholds import MonitorThresholds
from datadog_api_client.v1.model.monitor_type import MonitorType

body = Monitor(
    name="Example Monitor",
    type=MonitorType.COST_ALERT,
    query='formula("exclude_null(query1)").last("7d").anomaly(direction="above", threshold=10) >= 5',
    message="some message Notify: @hipchat-channel",
    tags=[
        "test:examplemonitor",
        "env:ci",
    ],
    priority=3,
    options=MonitorOptions(
        thresholds=MonitorThresholds(
            critical=5.0,
            warning=3.0,
        ),
        variables=[
            MonitorFormulaAndFunctionCostQueryDefinition(
                data_source=MonitorFormulaAndFunctionCostDataSource.CLOUD_COST,
                query="sum:aws.cost.net.amortized.shared.resources.allocated{aws_product IN (amplify ,athena, backup, bedrock ) } by {aws_product}.rollup(sum, 86400)",
                name="query1",
                aggregator=MonitorFormulaAndFunctionCostAggregator.SUM,
            ),
        ],
        include_tags=True,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MonitorsApi(api_client)
    response = api_instance.create_monitor(body=body)

    print(response)

```

Copy
#####  Create a RUM formula and functions monitor returns "OK" response 
```
"""
Create a RUM formula and functions monitor returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.monitors_api import MonitorsApi
from datadog_api_client.v1.model.monitor import Monitor
from datadog_api_client.v1.model.monitor_formula_and_function_event_aggregation import (
    MonitorFormulaAndFunctionEventAggregation,
)
from datadog_api_client.v1.model.monitor_formula_and_function_event_query_definition import (
    MonitorFormulaAndFunctionEventQueryDefinition,
)
from datadog_api_client.v1.model.monitor_formula_and_function_event_query_definition_compute import (
    MonitorFormulaAndFunctionEventQueryDefinitionCompute,
)
from datadog_api_client.v1.model.monitor_formula_and_function_event_query_definition_search import (
    MonitorFormulaAndFunctionEventQueryDefinitionSearch,
)
from datadog_api_client.v1.model.monitor_formula_and_function_events_data_source import (
    MonitorFormulaAndFunctionEventsDataSource,
)
from datadog_api_client.v1.model.monitor_options import MonitorOptions
from datadog_api_client.v1.model.monitor_thresholds import MonitorThresholds
from datadog_api_client.v1.model.monitor_type import MonitorType

body = Monitor(
    name="Example-Monitor",
    type=MonitorType.RUM_ALERT,
    query='formula("query2 / query1 * 100").last("15m") >= 0.8',
    message="some message Notify: @hipchat-channel",
    tags=[
        "test:examplemonitor",
        "env:ci",
    ],
    priority=3,
    options=MonitorOptions(
        thresholds=MonitorThresholds(
            critical=0.8,
        ),
        variables=[
            MonitorFormulaAndFunctionEventQueryDefinition(
                data_source=MonitorFormulaAndFunctionEventsDataSource.RUM,
                name="query2",
                search=MonitorFormulaAndFunctionEventQueryDefinitionSearch(
                    query="",
                ),
                indexes=[
                    "*",
                ],
                compute=MonitorFormulaAndFunctionEventQueryDefinitionCompute(
                    aggregation=MonitorFormulaAndFunctionEventAggregation.COUNT,
                ),
                group_by=[],
            ),
            MonitorFormulaAndFunctionEventQueryDefinition(
                data_source=MonitorFormulaAndFunctionEventsDataSource.RUM,
                name="query1",
                search=MonitorFormulaAndFunctionEventQueryDefinitionSearch(
                    query="status:error",
                ),
                indexes=[
                    "*",
                ],
                compute=MonitorFormulaAndFunctionEventQueryDefinitionCompute(
                    aggregation=MonitorFormulaAndFunctionEventAggregation.COUNT,
                ),
                group_by=[],
            ),
        ],
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MonitorsApi(api_client)
    response = api_instance.create_monitor(body=body)

    print(response)

```

Copy
#####  Create a ci-pipelines formula and functions monitor returns "OK" response 
```
"""
Create a ci-pipelines formula and functions monitor returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.monitors_api import MonitorsApi
from datadog_api_client.v1.model.monitor import Monitor
from datadog_api_client.v1.model.monitor_formula_and_function_event_aggregation import (
    MonitorFormulaAndFunctionEventAggregation,
)
from datadog_api_client.v1.model.monitor_formula_and_function_event_query_definition import (
    MonitorFormulaAndFunctionEventQueryDefinition,
)
from datadog_api_client.v1.model.monitor_formula_and_function_event_query_definition_compute import (
    MonitorFormulaAndFunctionEventQueryDefinitionCompute,
)
from datadog_api_client.v1.model.monitor_formula_and_function_event_query_definition_search import (
    MonitorFormulaAndFunctionEventQueryDefinitionSearch,
)
from datadog_api_client.v1.model.monitor_formula_and_function_events_data_source import (
    MonitorFormulaAndFunctionEventsDataSource,
)
from datadog_api_client.v1.model.monitor_options import MonitorOptions
from datadog_api_client.v1.model.monitor_thresholds import MonitorThresholds
from datadog_api_client.v1.model.monitor_type import MonitorType

body = Monitor(
    name="Example-Monitor",
    type=MonitorType.CI_PIPELINES_ALERT,
    query='formula("query1 / query2 * 100").last("15m") >= 0.8',
    message="some message Notify: @hipchat-channel",
    tags=[
        "test:examplemonitor",
        "env:ci",
    ],
    priority=3,
    options=MonitorOptions(
        thresholds=MonitorThresholds(
            critical=0.8,
        ),
        variables=[
            MonitorFormulaAndFunctionEventQueryDefinition(
                data_source=MonitorFormulaAndFunctionEventsDataSource.CI_PIPELINES,
                name="query1",
                search=MonitorFormulaAndFunctionEventQueryDefinitionSearch(
                    query="@ci.status:error",
                ),
                indexes=[
                    "*",
                ],
                compute=MonitorFormulaAndFunctionEventQueryDefinitionCompute(
                    aggregation=MonitorFormulaAndFunctionEventAggregation.COUNT,
                ),
                group_by=[],
            ),
            MonitorFormulaAndFunctionEventQueryDefinition(
                data_source=MonitorFormulaAndFunctionEventsDataSource.CI_PIPELINES,
                name="query2",
                search=MonitorFormulaAndFunctionEventQueryDefinitionSearch(
                    query="",
                ),
                indexes=[
                    "*",
                ],
                compute=MonitorFormulaAndFunctionEventQueryDefinitionCompute(
                    aggregation=MonitorFormulaAndFunctionEventAggregation.COUNT,
                ),
                group_by=[],
            ),
        ],
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MonitorsApi(api_client)
    response = api_instance.create_monitor(body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Create a monitor returns "OK" response
```
require 'dogapi'

api_key = '<DATADOG_API_KEY>'
app_key = '<DATADOG_APPLICATION_KEY>'

dog = Dogapi::Client.new(api_key, app_key)

# Create a new monitor
options = {
  'notify_no_data' => true,
  'no_data_timeframe' => 20
}
tags = ['app:webserver', 'frontend']
dog.monitor(
  'query alert',
  'avg(last_5m):sum:system.net.bytes_rcvd{host:host0} > 100',
  name: 'Bytes received on host0',
  message: 'We may need to add web hosts if this is consistently high.',
  tags: tags,
  options: options
)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby-legacy) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Create a Cost Monitor returns "OK" response 
```
# Create a Cost Monitor returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::MonitorsAPI.new

body = DatadogAPIClient::V1::Monitor.new({
  name: "Example Monitor",
  type: DatadogAPIClient::V1::MonitorType::COST_ALERT,
  query: 'formula("exclude_null(query1)").last("7d").anomaly(direction="above", threshold=10) >= 5',
  message: "some message Notify: @hipchat-channel",
  tags: [
    "test:examplemonitor",
    "env:ci",
  ],
  priority: 3,
  options: DatadogAPIClient::V1::MonitorOptions.new({
    thresholds: DatadogAPIClient::V1::MonitorThresholds.new({
      critical: 5,
      warning: 3,
    }),
    variables: [
      DatadogAPIClient::V1::MonitorFormulaAndFunctionCostQueryDefinition.new({
        data_source: DatadogAPIClient::V1::MonitorFormulaAndFunctionCostDataSource::CLOUD_COST,
        query: "sum:aws.cost.net.amortized.shared.resources.allocated{aws_product IN (amplify ,athena, backup, bedrock ) } by {aws_product}.rollup(sum, 86400)",
        name: "query1",
        aggregator: DatadogAPIClient::V1::MonitorFormulaAndFunctionCostAggregator::SUM,
      }),
    ],
    include_tags: true,
  }),
})
p api_instance.create_monitor(body)

```

Copy
#####  Create a RUM formula and functions monitor returns "OK" response 
```
# Create a RUM formula and functions monitor returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::MonitorsAPI.new

body = DatadogAPIClient::V1::Monitor.new({
  name: "Example-Monitor",
  type: DatadogAPIClient::V1::MonitorType::RUM_ALERT,
  query: 'formula("query2 / query1 * 100").last("15m") >= 0.8',
  message: "some message Notify: @hipchat-channel",
  tags: [
    "test:examplemonitor",
    "env:ci",
  ],
  priority: 3,
  options: DatadogAPIClient::V1::MonitorOptions.new({
    thresholds: DatadogAPIClient::V1::MonitorThresholds.new({
      critical: 0.8,
    }),
    variables: [
      DatadogAPIClient::V1::MonitorFormulaAndFunctionEventQueryDefinition.new({
        data_source: DatadogAPIClient::V1::MonitorFormulaAndFunctionEventsDataSource::RUM,
        name: "query2",
        search: DatadogAPIClient::V1::MonitorFormulaAndFunctionEventQueryDefinitionSearch.new({
          query: "",
        }),
        indexes: [
          "*",
        ],
        compute: DatadogAPIClient::V1::MonitorFormulaAndFunctionEventQueryDefinitionCompute.new({
          aggregation: DatadogAPIClient::V1::MonitorFormulaAndFunctionEventAggregation::COUNT,
        }),
        group_by: [],
      }),
      DatadogAPIClient::V1::MonitorFormulaAndFunctionEventQueryDefinition.new({
        data_source: DatadogAPIClient::V1::MonitorFormulaAndFunctionEventsDataSource::RUM,
        name: "query1",
        search: DatadogAPIClient::V1::MonitorFormulaAndFunctionEventQueryDefinitionSearch.new({
          query: "status:error",
        }),
        indexes: [
          "*",
        ],
        compute: DatadogAPIClient::V1::MonitorFormulaAndFunctionEventQueryDefinitionCompute.new({
          aggregation: DatadogAPIClient::V1::MonitorFormulaAndFunctionEventAggregation::COUNT,
        }),
        group_by: [],
      }),
    ],
  }),
})
p api_instance.create_monitor(body)

```

Copy
#####  Create a ci-pipelines formula and functions monitor returns "OK" response 
```
# Create a ci-pipelines formula and functions monitor returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::MonitorsAPI.new

body = DatadogAPIClient::V1::Monitor.new({
  name: "Example-Monitor",
  type: DatadogAPIClient::V1::MonitorType::CI_PIPELINES_ALERT,
  query: 'formula("query1 / query2 * 100").last("15m") >= 0.8',
  message: "some message Notify: @hipchat-channel",
  tags: [
    "test:examplemonitor",
    "env:ci",
  ],
  priority: 3,
  options: DatadogAPIClient::V1::MonitorOptions.new({
    thresholds: DatadogAPIClient::V1::MonitorThresholds.new({
      critical: 0.8,
    }),
    variables: [
      DatadogAPIClient::V1::MonitorFormulaAndFunctionEventQueryDefinition.new({
        data_source: DatadogAPIClient::V1::MonitorFormulaAndFunctionEventsDataSource::CI_PIPELINES,
        name: "query1",
        search: DatadogAPIClient::V1::MonitorFormulaAndFunctionEventQueryDefinitionSearch.new({
          query: "@ci.status:error",
        }),
        indexes: [
          "*",
        ],
        compute: DatadogAPIClient::V1::MonitorFormulaAndFunctionEventQueryDefinitionCompute.new({
          aggregation: DatadogAPIClient::V1::MonitorFormulaAndFunctionEventAggregation::COUNT,
        }),
        group_by: [],
      }),
      DatadogAPIClient::V1::MonitorFormulaAndFunctionEventQueryDefinition.new({
        data_source: DatadogAPIClient::V1::MonitorFormulaAndFunctionEventsDataSource::CI_PIPELINES,
        name: "query2",
        search: DatadogAPIClient::V1::MonitorFormulaAndFunctionEventQueryDefinitionSearch.new({
          query: "",
        }),
        indexes: [
          "*",
        ],
        compute: DatadogAPIClient::V1::MonitorFormulaAndFunctionEventQueryDefinitionCompute.new({
          aggregation: DatadogAPIClient::V1::MonitorFormulaAndFunctionEventAggregation::COUNT,
        }),
        group_by: [],
      }),
    ],
  }),
})
p api_instance.create_monitor(body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Create a Cost Monitor returns "OK" response 
```
// Create a Cost Monitor returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_monitors::MonitorsAPI;
use datadog_api_client::datadogV1::model::Monitor;
use datadog_api_client::datadogV1::model::MonitorFormulaAndFunctionCostAggregator;
use datadog_api_client::datadogV1::model::MonitorFormulaAndFunctionCostDataSource;
use datadog_api_client::datadogV1::model::MonitorFormulaAndFunctionCostQueryDefinition;
use datadog_api_client::datadogV1::model::MonitorFormulaAndFunctionQueryDefinition;
use datadog_api_client::datadogV1::model::MonitorOptions;
use datadog_api_client::datadogV1::model::MonitorThresholds;
use datadog_api_client::datadogV1::model::MonitorType;

#[tokio::main]
async fn main() {
    let body =
        Monitor::new(
            r#"formula("exclude_null(query1)").last("7d").anomaly(direction="above", threshold=10) >= 5"#.to_string(),
            MonitorType::COST_ALERT,
        )
            .message("some message Notify: @hipchat-channel".to_string())
            .name("Example Monitor".to_string())
            .options(
                MonitorOptions::new()
                    .include_tags(true)
                    .thresholds(MonitorThresholds::new().critical(5.0 as f64).warning(Some(3.0 as f64)))
                    .variables(
                        vec![
                            MonitorFormulaAndFunctionQueryDefinition::MonitorFormulaAndFunctionCostQueryDefinition(
                                Box::new(
                                    MonitorFormulaAndFunctionCostQueryDefinition::new(
                                        MonitorFormulaAndFunctionCostDataSource::CLOUD_COST,
                                        "query1".to_string(),
                                        "sum:aws.cost.net.amortized.shared.resources.allocated{aws_product IN (amplify ,athena, backup, bedrock ) } by {aws_product}.rollup(sum, 86400)".to_string(),
                                    ).aggregator(MonitorFormulaAndFunctionCostAggregator::SUM),
                                ),
                            )
                        ],
                    ),
            )
            .priority(Some(3))
            .tags(vec!["test:examplemonitor".to_string(), "env:ci".to_string()]);
    let configuration = datadog::Configuration::new();
    let api = MonitorsAPI::with_config(configuration);
    let resp = api.create_monitor(body).await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}

```

Copy
#####  Create a RUM formula and functions monitor returns "OK" response 
```
// Create a RUM formula and functions monitor returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_monitors::MonitorsAPI;
use datadog_api_client::datadogV1::model::Monitor;
use datadog_api_client::datadogV1::model::MonitorFormulaAndFunctionEventAggregation;
use datadog_api_client::datadogV1::model::MonitorFormulaAndFunctionEventQueryDefinition;
use datadog_api_client::datadogV1::model::MonitorFormulaAndFunctionEventQueryDefinitionCompute;
use datadog_api_client::datadogV1::model::MonitorFormulaAndFunctionEventQueryDefinitionSearch;
use datadog_api_client::datadogV1::model::MonitorFormulaAndFunctionEventsDataSource;
use datadog_api_client::datadogV1::model::MonitorFormulaAndFunctionQueryDefinition;
use datadog_api_client::datadogV1::model::MonitorOptions;
use datadog_api_client::datadogV1::model::MonitorThresholds;
use datadog_api_client::datadogV1::model::MonitorType;

#[tokio::main]
async fn main() {
    let body =
        Monitor::new(r#"formula("query2 / query1 * 100").last("15m") >= 0.8"#.to_string(), MonitorType::RUM_ALERT)
            .message("some message Notify: @hipchat-channel".to_string())
            .name("Example-Monitor".to_string())
            .options(
                MonitorOptions::new()
                    .thresholds(MonitorThresholds::new().critical(0.8 as f64))
                    .variables(
                        vec![
                            MonitorFormulaAndFunctionQueryDefinition::MonitorFormulaAndFunctionEventQueryDefinition(
                                Box::new(
                                    MonitorFormulaAndFunctionEventQueryDefinition::new(
                                        MonitorFormulaAndFunctionEventQueryDefinitionCompute::new(
                                            MonitorFormulaAndFunctionEventAggregation::COUNT,
                                        ),
                                        MonitorFormulaAndFunctionEventsDataSource::RUM,
                                        "query2".to_string(),
                                    )
                                        .group_by(vec![])
                                        .indexes(vec!["*".to_string()])
                                        .search(
                                            MonitorFormulaAndFunctionEventQueryDefinitionSearch::new("".to_string()),
                                        ),
                                ),
                            ),
                            MonitorFormulaAndFunctionQueryDefinition::MonitorFormulaAndFunctionEventQueryDefinition(
                                Box::new(
                                    MonitorFormulaAndFunctionEventQueryDefinition::new(
                                        MonitorFormulaAndFunctionEventQueryDefinitionCompute::new(
                                            MonitorFormulaAndFunctionEventAggregation::COUNT,
                                        ),
                                        MonitorFormulaAndFunctionEventsDataSource::RUM,
                                        "query1".to_string(),
                                    )
                                        .group_by(vec![])
                                        .indexes(vec!["*".to_string()])
                                        .search(
                                            MonitorFormulaAndFunctionEventQueryDefinitionSearch::new(
                                                "status:error".to_string(),
                                            ),
                                        ),
                                ),
                            )
                        ],
                    ),
            )
            .priority(Some(3))
            .tags(vec!["test:examplemonitor".to_string(), "env:ci".to_string()]);
    let configuration = datadog::Configuration::new();
    let api = MonitorsAPI::with_config(configuration);
    let resp = api.create_monitor(body).await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}

```

Copy
#####  Create a ci-pipelines formula and functions monitor returns "OK" response 
```
// Create a ci-pipelines formula and functions monitor returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_monitors::MonitorsAPI;
use datadog_api_client::datadogV1::model::Monitor;
use datadog_api_client::datadogV1::model::MonitorFormulaAndFunctionEventAggregation;
use datadog_api_client::datadogV1::model::MonitorFormulaAndFunctionEventQueryDefinition;
use datadog_api_client::datadogV1::model::MonitorFormulaAndFunctionEventQueryDefinitionCompute;
use datadog_api_client::datadogV1::model::MonitorFormulaAndFunctionEventQueryDefinitionSearch;
use datadog_api_client::datadogV1::model::MonitorFormulaAndFunctionEventsDataSource;
use datadog_api_client::datadogV1::model::MonitorFormulaAndFunctionQueryDefinition;
use datadog_api_client::datadogV1::model::MonitorOptions;
use datadog_api_client::datadogV1::model::MonitorThresholds;
use datadog_api_client::datadogV1::model::MonitorType;

#[tokio::main]
async fn main() {
    let body =
        Monitor::new(
            r#"formula("query1 / query2 * 100").last("15m") >= 0.8"#.to_string(),
            MonitorType::CI_PIPELINES_ALERT,
        )
            .message("some message Notify: @hipchat-channel".to_string())
            .name("Example-Monitor".to_string())
            .options(
                MonitorOptions::new()
                    .thresholds(MonitorThresholds::new().critical(0.8 as f64))
                    .variables(
                        vec![
                            MonitorFormulaAndFunctionQueryDefinition::MonitorFormulaAndFunctionEventQueryDefinition(
                                Box::new(
                                    MonitorFormulaAndFunctionEventQueryDefinition::new(
                                        MonitorFormulaAndFunctionEventQueryDefinitionCompute::new(
                                            MonitorFormulaAndFunctionEventAggregation::COUNT,
                                        ),
                                        MonitorFormulaAndFunctionEventsDataSource::CI_PIPELINES,
                                        "query1".to_string(),
                                    )
                                        .group_by(vec![])
                                        .indexes(vec!["*".to_string()])
                                        .search(
                                            MonitorFormulaAndFunctionEventQueryDefinitionSearch::new(
                                                "@ci.status:error".to_string(),
                                            ),
                                        ),
                                ),
                            ),
                            MonitorFormulaAndFunctionQueryDefinition::MonitorFormulaAndFunctionEventQueryDefinition(
                                Box::new(
                                    MonitorFormulaAndFunctionEventQueryDefinition::new(
                                        MonitorFormulaAndFunctionEventQueryDefinitionCompute::new(
                                            MonitorFormulaAndFunctionEventAggregation::COUNT,
                                        ),
                                        MonitorFormulaAndFunctionEventsDataSource::CI_PIPELINES,
                                        "query2".to_string(),
                                    )
                                        .group_by(vec![])
                                        .indexes(vec!["*".to_string()])
                                        .search(
                                            MonitorFormulaAndFunctionEventQueryDefinitionSearch::new("".to_string()),
                                        ),
                                ),
                            )
                        ],
                    ),
            )
            .priority(Some(3))
            .tags(vec!["test:examplemonitor".to_string(), "env:ci".to_string()]);
    let configuration = datadog::Configuration::new();
    let api = MonitorsAPI::with_config(configuration);
    let resp = api.create_monitor(body).await;
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

#####  Create a Cost Monitor returns "OK" response 
```
/**
 * Create a Cost Monitor returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.MonitorsApi(configuration);

const params: v1.MonitorsApiCreateMonitorRequest = {
  body: {
    name: "Example Monitor",
    type: "cost alert",
    query: `formula("exclude_null(query1)").last("7d").anomaly(direction="above", threshold=10) >= 5`,
    message: "some message Notify: @hipchat-channel",
    tags: ["test:examplemonitor", "env:ci"],
    priority: 3,
    options: {
      thresholds: {
        critical: 5,
        warning: 3,
      },
      variables: [
        {
          dataSource: "cloud_cost",
          query:
            "sum:aws.cost.net.amortized.shared.resources.allocated{aws_product IN (amplify ,athena, backup, bedrock ) } by {aws_product}.rollup(sum, 86400)",
          name: "query1",
          aggregator: "sum",
        },
      ],
      includeTags: true,
    },
  },
};

apiInstance
  .createMonitor(params)
  .then((data: v1.Monitor) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));

```

Copy
#####  Create a RUM formula and functions monitor returns "OK" response 
```
/**
 * Create a RUM formula and functions monitor returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.MonitorsApi(configuration);

const params: v1.MonitorsApiCreateMonitorRequest = {
  body: {
    name: "Example-Monitor",
    type: "rum alert",
    query: `formula("query2 / query1 * 100").last("15m") >= 0.8`,
    message: "some message Notify: @hipchat-channel",
    tags: ["test:examplemonitor", "env:ci"],
    priority: 3,
    options: {
      thresholds: {
        critical: 0.8,
      },
      variables: [
        {
          dataSource: "rum",
          name: "query2",
          search: {
            query: "",
          },
          indexes: ["*"],
          compute: {
            aggregation: "count",
          },
          groupBy: [],
        },
        {
          dataSource: "rum",
          name: "query1",
          search: {
            query: "status:error",
          },
          indexes: ["*"],
          compute: {
            aggregation: "count",
          },
          groupBy: [],
        },
      ],
    },
  },
};

apiInstance
  .createMonitor(params)
  .then((data: v1.Monitor) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));

```

Copy
#####  Create a ci-pipelines formula and functions monitor returns "OK" response 
```
/**
 * Create a ci-pipelines formula and functions monitor returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.MonitorsApi(configuration);

const params: v1.MonitorsApiCreateMonitorRequest = {
  body: {
    name: "Example-Monitor",
    type: "ci-pipelines alert",
    query: `formula("query1 / query2 * 100").last("15m") >= 0.8`,
    message: "some message Notify: @hipchat-channel",
    tags: ["test:examplemonitor", "env:ci"],
    priority: 3,
    options: {
      thresholds: {
        critical: 0.8,
      },
      variables: [
        {
          dataSource: "ci_pipelines",
          name: "query1",
          search: {
            query: "@ci.status:error",
          },
          indexes: ["*"],
          compute: {
            aggregation: "count",
          },
          groupBy: [],
        },
        {
          dataSource: "ci_pipelines",
          name: "query2",
          search: {
            query: "",
          },
          indexes: ["*"],
          compute: {
            aggregation: "count",
          },
          groupBy: [],
        },
      ],
    },
  },
};

apiInstance
  .createMonitor(params)
  .then((data: v1.Monitor) => {
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
## [Monitors search](https://docs.datadoghq.com/api/latest/monitors/#monitors-search)
  * [v1 (latest)](https://docs.datadoghq.com/api/latest/monitors/#monitors-search-v1)


GET https://api.ap1.datadoghq.com/api/v1/monitor/searchhttps://api.ap2.datadoghq.com/api/v1/monitor/searchhttps://api.datadoghq.eu/api/v1/monitor/searchhttps://api.ddog-gov.com/api/v1/monitor/searchhttps://api.datadoghq.com/api/v1/monitor/searchhttps://api.us3.datadoghq.com/api/v1/monitor/searchhttps://api.us5.datadoghq.com/api/v1/monitor/search
### Overview
Search and filter your monitors details. This endpoint requires the `monitors_read` permission.
OAuth apps require the `monitors_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#monitors) to access this endpoint.
### Arguments
#### Query Strings
Name
Type
Description
query
string
After entering a search query in your [Manage Monitor page](https://app.datadoghq.com/monitors/manage) use the query parameter value in the URL of the page as value for this parameter. Consult the dedicated [manage monitor documentation](https://docs.datadoghq.com/monitors/manage/#find-the-monitors) page to learn more.
The query can contain any number of space-separated monitor attributes, for instance `query="type:metric status:alert"`.
page
integer
Page to start paginating from.
per_page
integer
Number of monitors to return per page.
sort
string
String for sort order, composed of field and sort order separate by a comma, for example `name,asc`. Supported sort directions: `asc`, `desc`. Supported fields:
  * `name`
  * `status`
  * `tags`


### Response
  * [200](https://docs.datadoghq.com/api/latest/monitors/#SearchMonitors-200-v1)
  * [400](https://docs.datadoghq.com/api/latest/monitors/#SearchMonitors-400-v1)
  * [403](https://docs.datadoghq.com/api/latest/monitors/#SearchMonitors-403-v1)
  * [429](https://docs.datadoghq.com/api/latest/monitors/#SearchMonitors-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


The response from a monitor search.
Field
Type
Description
counts
object
The counts of monitors per different criteria.
muted
[object]
Search facets.
count
int64
The number of found monitors with the listed value.
name
The facet value.
status
[object]
Search facets.
count
int64
The number of found monitors with the listed value.
name
The facet value.
tag
[object]
Search facets.
count
int64
The number of found monitors with the listed value.
name
The facet value.
type
[object]
Search facets.
count
int64
The number of found monitors with the listed value.
name
The facet value.
metadata
object
Metadata about the response.
page
int64
The page to start paginating from.
page_count
int64
The number of pages.
per_page
int64
The number of monitors to return per page.
total_count
int64
The total number of monitors.
monitors
[object]
The list of found monitors.
classification
string
Classification of the monitor.
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
id
int64
ID of the monitor.
last_triggered_ts
int64
Latest timestamp the monitor triggered.
metrics
[string]
Metrics used by the monitor.
name
string
The monitor name.
notifications
[object]
The notification triggered by the monitor.
handle
string
The email address that received the notification.
name
string
The username receiving the notification
org_id
int64
The ID of the organization.
quality_issues
[string]
Quality issues detected with the monitor.
query
string
The monitor query.
scopes
[string]
The scope(s) to which the downtime applies, for example `host:app2`. Provide multiple scopes as a comma-separated list, for example `env:dev,env:prod`. The resulting downtime applies to sources that matches ALL provided scopes (that is `env:dev AND env:prod`), NOT any of them.
status
enum
The different states your monitor can be in. Allowed enum values: `Alert,Ignored,No Data,OK,Skipped,Unknown,Warn`
tags
[string]
Tags associated with the monitor.
type
enum
The type of the monitor. For more information about `type`, see the [monitor options](https://docs.datadoghq.com/monitors/guide/monitor_api_options/) docs. Allowed enum values: `composite,event alert,log alert,metric alert,process alert,query alert,rum alert,service check,synthetics alert,trace-analytics alert,slo alert,event-v2 alert,audit alert,ci-pipelines alert,ci-tests alert,error-tracking alert,database-monitoring alert,network-performance alert,cost alert,data-quality alert`
```
{
  "counts": {
    "muted": [
      {
        "count": 3,
        "name": false
      },
      {
        "count": 3,
        "name": true
      }
    ],
    "status": [
      {
        "count": 4,
        "name": "No Data"
      },
      {
        "count": 2,
        "name": "OK"
      }
    ],
    "tag": [
      {
        "count": 6,
        "name": "service:cassandra"
      }
    ],
    "type": [
      {
        "count": 6,
        "name": "metric"
      }
    ]
  },
  "metadata": {
    "page": 0,
    "page_count": 6,
    "per_page": 30,
    "total_count": 6
  },
  "monitors": [
    {
      "classification": "metric",
      "creator": {
        "handle": "john@datadoghq.com",
        "name": "John Doe"
      },
      "id": 2699850,
      "last_triggered_ts": null,
      "metrics": [
        "system.cpu.user"
      ],
      "name": "Cassandra CPU is high on {{host.name}} in {{availability-zone.name}}",
      "notifications": [
        {
          "handle": "jane@datadoghq.com",
          "name": "Jane Doe"
        }
      ],
      "org_id": 1234,
      "quality_issues": [
        "broken_at_handle",
        "noisy_monitor"
      ],
      "scopes": [
        "!availability-zone:us-east-1c",
        "name:cassandra"
      ],
      "status": "No Data",
      "tags": [
        "service:cassandra"
      ],
      "type": "query alert"
    }
  ]
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


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
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


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
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/monitors/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/monitors/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/monitors/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/monitors/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/monitors/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/monitors/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/monitors/?code-lang=typescript)
  * [Ruby [legacy]](https://docs.datadoghq.com/api/latest/monitors/?code-lang=ruby-legacy)
  * [Python [legacy]](https://docs.datadoghq.com/api/latest/monitors/?code-lang=python-legacy)


#####  Monitors search
Copy
```
                  # Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/monitor/search" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Monitors search
```
"""
Monitors search returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.monitors_api import MonitorsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MonitorsApi(api_client)
    response = api_instance.search_monitors()

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Monitors search
```
# Monitors search returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::MonitorsAPI.new
p api_instance.search_monitors()

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Monitors search
```
require 'dogapi'

api_key = '<DATADOG_API_KEY>'
app_key = '<DATADOG_APPLICATION_KEY>'

dog = Dogapi::Client.new(api_key, app_key)

# Search monitors
dog.search_monitors

# Examples of possible query parameters:
# dog.search_monitors(query="id:7100311")
# dog.search_monitors(query="title:foo metric:system.core.idle status:Alert")

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby-legacy) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Monitors search
```
// Monitors search returns "OK" response

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
	api := datadogV1.NewMonitorsApi(apiClient)
	resp, r, err := api.SearchMonitors(ctx, *datadogV1.NewSearchMonitorsOptionalParameters())

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `MonitorsApi.SearchMonitors`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `MonitorsApi.SearchMonitors`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Monitors search
```
// Monitors search returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.MonitorsApi;
import com.datadog.api.client.v1.model.MonitorSearchResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    MonitorsApi apiInstance = new MonitorsApi(defaultClient);

    try {
      MonitorSearchResponse result = apiInstance.searchMonitors();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MonitorsApi#searchMonitors");
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

#####  Monitors search
```
from datadog import initialize, api

options = {
	'api_key': '<DATADOG_API_KEY>',
	'app_key': '<DATADOG_APPLICATION_KEY>'
}

initialize(**options)

# Search monitors
api.Monitor.search()

# Examples of possible query parameters:
# api.Monitor.search(query="id:7100311")
# api.Monitor.search(query="title:foo metric:system.core.idle status:Alert")

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python-legacy) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python "example.py"


```

#####  Monitors search
```
// Monitors search returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_monitors::MonitorsAPI;
use datadog_api_client::datadogV1::api_monitors::SearchMonitorsOptionalParams;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = MonitorsAPI::with_config(configuration);
    let resp = api
        .search_monitors(SearchMonitorsOptionalParams::default())
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

#####  Monitors search
```
/**
 * Monitors search returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.MonitorsApi(configuration);

apiInstance
  .searchMonitors()
  .then((data: v1.MonitorSearchResponse) => {
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
## [Unmute a monitor](https://docs.datadoghq.com/api/latest/monitors/#unmute-a-monitor)
  * [v1 (latest)](https://docs.datadoghq.com/api/latest/monitors/#unmute-a-monitor-v1)


POST https://api.ap1.datadoghq.com/api/v1/monitor/{monitor_id}/unmutehttps://api.ap2.datadoghq.com/api/v1/monitor/{monitor_id}/unmutehttps://api.datadoghq.eu/api/v1/monitor/{monitor_id}/unmutehttps://api.ddog-gov.com/api/v1/monitor/{monitor_id}/unmutehttps://api.datadoghq.com/api/v1/monitor/{monitor_id}/unmutehttps://api.us3.datadoghq.com/api/v1/monitor/{monitor_id}/unmutehttps://api.us5.datadoghq.com/api/v1/monitor/{monitor_id}/unmute
### Overview
Unmute the specified monitor. This endpoint requires the `monitors_write` permission.
OAuth apps require the `monitors_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#monitors) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
monitor_id [_required_]
integer
The id of the monitor
#### Query Strings
Name
Type
Description
scope
string
The scope to apply the mute to. For example, if your alert is grouped by `{host}`, you might mute `host:app1`.
all_scopes
boolean
Clear muting across all scopes. Default is `false`.
### Response
  * [200](https://docs.datadoghq.com/api/latest/monitors/#UnmuteMonitor-200-v1)
  * [400](https://docs.datadoghq.com/api/latest/monitors/#UnmuteMonitor-400-v1)
  * [401](https://docs.datadoghq.com/api/latest/monitors/#UnmuteMonitor-401-v1)
  * [404](https://docs.datadoghq.com/api/latest/monitors/#UnmuteMonitor-404-v1)
  * [429](https://docs.datadoghq.com/api/latest/monitors/#UnmuteMonitor-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


Object describing a monitor.
Field
Type
Description
assets
[object]
The list of monitor assets tied to a monitor, which represents key links for users to take action on monitor alerts (for example, runbooks).
category [_required_]
enum
Indicates the type of asset this entity represents on a monitor. Allowed enum values: `runbook`
name [_required_]
string
Name for the monitor asset
resource_key
string
Represents the identifier of the internal Datadog resource that this asset represents. IDs in this field should be passed in as strings.
resource_type
enum
Type of internal Datadog resource associated with a monitor asset. Allowed enum values: `notebook`
url [_required_]
string
URL link for the asset. For links with an internal resource type set, this should be the relative path to where the Datadog domain is appended internally. For external links, this should be the full URL path.
created
date-time
Timestamp of the monitor creation.
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
deleted
date-time
Whether or not the monitor is deleted. (Always `null`)
draft_status
enum
Indicates whether the monitor is in a draft or published state.
`draft`: The monitor appears as Draft and does not send notifications. `published`: The monitor is active and evaluates conditions and notify as configured.
This field is in preview. The draft value is only available to customers with the feature enabled. Allowed enum values: `draft,published`
default: `published`
id
int64
ID of this monitor.
matching_downtimes
[object]
A list of active v1 downtimes that match this monitor.
end
int64
POSIX timestamp to end the downtime.
id [_required_]
int64
The downtime ID.
scope
[string]
The scope(s) to which the downtime applies. Must be in `key:value` format. For example, `host:app2`. Provide multiple scopes as a comma-separated list like `env:dev,env:prod`. The resulting downtime applies to sources that matches ALL provided scopes (`env:dev` **AND** `env:prod`).
start
int64
POSIX timestamp to start the downtime.
message
string
A message to include with notifications for this monitor.
modified
date-time
Last timestamp when the monitor was edited.
multi
boolean
Whether or not the monitor is broken down on different groups.
name
string
The monitor name.
options
object
List of options associated with your monitor.
aggregation
object
Type of aggregation performed in the monitor query.
group_by
string
Group to break down the monitor on.
metric
string
Metric name used in the monitor.
type
string
Metric type used in the monitor.
device_ids
[string]
**DEPRECATED** : IDs of the device the Synthetics monitor is running on.
enable_logs_sample
boolean
Whether or not to send a log sample when the log monitor triggers.
enable_samples
boolean
Whether or not to send a list of samples when the monitor triggers. This is only used by CI Test and Pipeline monitors.
escalation_message
string
We recommend using the [is_renotify](https://docs.datadoghq.com/monitors/notify/?tab=is_alert#renotify), block in the original message instead. A message to include with a re-notification. Supports the `@username` notification we allow elsewhere. Not applicable if `renotify_interval` is `None`.
evaluation_delay
int64
Time (in seconds) to delay evaluation, as a non-negative integer. For example, if the value is set to `300` (5min), the timeframe is set to `last_5m` and the time is 7:00, the monitor evaluates data from 6:50 to 6:55. This is useful for AWS CloudWatch and other backfilled metrics to ensure the monitor always has data during evaluation.
group_retention_duration
string
The time span after which groups with missing data are dropped from the monitor state. The minimum value is one hour, and the maximum value is 72 hours. Example values are: "60m", "1h", and "2d". This option is only available for APM Trace Analytics, Audit Trail, CI, Error Tracking, Event, Logs, and RUM monitors.
groupby_simple_monitor
boolean
**DEPRECATED** : Whether the log alert monitor triggers a single alert or multiple alerts when any group breaches a threshold. Use `notify_by` instead.
include_tags
boolean
A Boolean indicating whether notifications from this monitor automatically inserts its triggering tags into the title.
**Examples**
  * If `True`, `[Triggered on {host:h1}] Monitor Title`
  * If `False`, `[Triggered] Monitor Title`


default: `true`
locked
boolean
**DEPRECATED** : Whether or not the monitor is locked (only editable by creator and admins). Use `restricted_roles` instead.
min_failure_duration
int64
How long the test should be in failure before alerting (integer, number of seconds, max 7200).
min_location_failed
int64
The minimum number of locations in failure at the same time during at least one moment in the `min_failure_duration` period (`min_location_failed` and `min_failure_duration` are part of the advanced alerting rules - integer, >= 1).
default: `1`
new_group_delay
int64
Time (in seconds) to skip evaluations for new groups.
For example, this option can be used to skip evaluations for new hosts while they initialize.
Must be a non negative integer.
new_host_delay
int64
**DEPRECATED** : Time (in seconds) to allow a host to boot and applications to fully start before starting the evaluation of monitor results. Should be a non negative integer.
Use new_group_delay instead.
default: `300`
no_data_timeframe
int64
The number of minutes before a monitor notifies after data stops reporting. Datadog recommends at least 2x the monitor timeframe for query alerts or 2 minutes for service checks. If omitted, 2x the evaluation timeframe is used for query alerts, and 24 hours is used for service checks.
notification_preset_name
enum
Toggles the display of additional content sent in the monitor notification. Allowed enum values: `show_all,hide_query,hide_handles,hide_all`
default: `show_all`
notify_audit
boolean
A Boolean indicating whether tagged users is notified on changes to this monitor.
notify_by
[string]
Controls what granularity a monitor alerts on. Only available for monitors with groupings. For instance, a monitor grouped by `cluster`, `namespace`, and `pod` can be configured to only notify on each new `cluster` violating the alert conditions by setting `notify_by` to `["cluster"]`. Tags mentioned in `notify_by` must be a subset of the grouping tags in the query. For example, a query grouped by `cluster` and `namespace` cannot notify on `region`. Setting `notify_by` to `["*"]` configures the monitor to notify as a simple-alert.
notify_no_data
boolean
A Boolean indicating whether this monitor notifies when data stops reporting. Defaults to `false`.
on_missing_data
enum
Controls how groups or monitors are treated if an evaluation does not return any data points. The default option results in different behavior depending on the monitor query type. For monitors using Count queries, an empty monitor evaluation is treated as 0 and is compared to the threshold conditions. For monitors using any query type other than Count, for example Gauge, Measure, or Rate, the monitor shows the last known status. This option is only available for APM Trace Analytics, Audit Trail, CI, Error Tracking, Event, Logs, and RUM monitors. Allowed enum values: `default,show_no_data,show_and_notify_no_data,resolve`
renotify_interval
int64
The number of minutes after the last notification before a monitor re-notifies on the current status. It only re-notifies if it’s not resolved.
renotify_occurrences
int64
The number of times re-notification messages should be sent on the current status at the provided re-notification interval.
renotify_statuses
[string]
The types of monitor statuses for which re-notification messages are sent. Default: **null** if `renotify_interval` is **null**. If `renotify_interval` is set, defaults to renotify on `Alert` and `No Data`.
require_full_window
boolean
A Boolean indicating whether this monitor needs a full window of data before it’s evaluated. We highly recommend you set this to `false` for sparse metrics, otherwise some evaluations are skipped. Default is false. This setting only applies to metric monitors.
scheduling_options
object
Configuration options for scheduling.
custom_schedule
object
Configuration options for the custom schedule. **This feature is in private beta.**
recurrences
[object]
Array of custom schedule recurrences.
rrule
string
Defines the recurrence rule (RRULE) for a given schedule.
start
string
Defines the start date and time of the recurring schedule.
timezone
string
Defines the timezone the schedule runs on.
evaluation_window
object
Configuration options for the evaluation window. If `hour_starts` is set, no other fields may be set. Otherwise, `day_starts` and `month_starts` must be set together.
day_starts
string
The time of the day at which a one day cumulative evaluation window starts.
hour_starts
int32
The minute of the hour at which a one hour cumulative evaluation window starts.
month_starts
int32
The day of the month at which a one month cumulative evaluation window starts.
timezone
string
The timezone of the time of the day of the cumulative evaluation window start.
silenced
object
**DEPRECATED** : Information about the downtime applied to the monitor. Only shows v1 downtimes.
<any-key>
int64
UTC epoch timestamp in seconds when the downtime for the group expires.
synthetics_check_id
string
**DEPRECATED** : ID of the corresponding Synthetic check.
threshold_windows
object
Alerting time window options.
recovery_window
string
Describes how long an anomalous metric must be normal before the alert recovers.
trigger_window
string
Describes how long a metric must be anomalous before an alert triggers.
thresholds
object
List of the different monitor threshold available.
critical
double
The monitor `CRITICAL` threshold.
critical_recovery
double
The monitor `CRITICAL` recovery threshold.
ok
double
The monitor `OK` threshold.
unknown
double
The monitor UNKNOWN threshold.
warning
double
The monitor `WARNING` threshold.
warning_recovery
double
The monitor `WARNING` recovery threshold.
timeout_h
int64
The number of hours of the monitor not reporting data before it automatically resolves from a triggered state. The minimum allowed value is 0 hours. The maximum allowed value is 24 hours.
variables
[ <oneOf>]
List of requests that can be used in the monitor query. **This feature is currently in beta.**
Option 1
object
A formula and functions events query.
compute [_required_]
object
Compute options.
aggregation [_required_]
enum
Aggregation methods for event platform queries. Allowed enum values: `count,cardinality,median,pc75,pc90,pc95,pc98,pc99,sum,min,max,avg`
interval
int64
A time interval in milliseconds.
metric
string
Measurable attribute to compute.
data_source [_required_]
enum
Data source for event platform-based queries. Allowed enum values: `rum,ci_pipelines,ci_tests,audit,events,logs,spans,database_queries,network`
group_by
[object]
Group by options.
facet [_required_]
string
Event facet.
limit
int64
Number of groups to return.
sort
object
Options for sorting group by results.
aggregation [_required_]
enum
Aggregation methods for event platform queries. Allowed enum values: `count,cardinality,median,pc75,pc90,pc95,pc98,pc99,sum,min,max,avg`
metric
string
Metric used for sorting group by results.
order
enum
Direction of sort. Allowed enum values: `asc,desc`
default: `desc`
indexes
[string]
An array of index names to query in the stream. Omit or use `[]` to query all indexes at once.
name [_required_]
string
Name of the query for use in formulas.
search
object
Search options.
query [_required_]
string
Events search string.
Option 2
object
A formula and functions cost query.
aggregator
enum
Aggregation methods for metric queries. Allowed enum values: `avg,sum,max,min,last,area,l2norm,percentile,stddev`
data_source [_required_]
enum
Data source for cost queries. Allowed enum values: `metrics,cloud_cost,datadog_usage`
name [_required_]
string
Name of the query for use in formulas.
query [_required_]
string
The monitor query.
Option 3
object
A formula and functions data quality query.
data_source [_required_]
enum
Data source for data quality queries. Allowed enum values: `data_quality_metrics`
filter [_required_]
string
Filter expression used to match on data entities. Uses Aastra query syntax.
group_by
[string]
Optional grouping fields for aggregation.
measure [_required_]
string
The data quality measure to query. Common values include: `bytes`, `cardinality`, `custom`, `freshness`, `max`, `mean`, `min`, `nullness`, `percent_negative`, `percent_zero`, `row_count`, `stddev`, `sum`, `uniqueness`. Additional values may be supported.
monitor_options
object
Monitor configuration options for data quality queries.
crontab_override
string
Crontab expression to override the default schedule.
custom_sql
string
Custom SQL query for the monitor.
custom_where
string
Custom WHERE clause for the query.
group_by_columns
[string]
Columns to group results by.
model_type_override
enum
Override for the model type used in anomaly detection. Allowed enum values: `freshness,percentage,any`
name [_required_]
string
Name of the query for use in formulas.
schema_version
string
Schema version for the data quality query.
scope
string
Optional scoping expression to further filter metrics. Uses metrics filter syntax. This is useful when an entity has been configured to emit metrics with additional tags.
overall_state
enum
The different states your monitor can be in. Allowed enum values: `Alert,Ignored,No Data,OK,Skipped,Unknown,Warn`
priority
int64
Integer from 1 (high) to 5 (low) indicating alert severity.
query [_required_]
string
The monitor query.
restricted_roles
[string]
A list of unique role identifiers to define which roles are allowed to edit the monitor. The unique identifiers for all roles can be pulled from the [Roles API](https://docs.datadoghq.com/api/latest/roles/#list-roles) and are located in the `data.id` field. Editing a monitor includes any updates to the monitor configuration, monitor deletion, and muting of the monitor for any amount of time. You can use the [Restriction Policies API](https://docs.datadoghq.com/api/latest/restriction-policies/) to manage write authorization for individual monitors by teams and users, in addition to roles.
state
object
Wrapper object with the different monitor states.
groups
object
Dictionary where the keys are groups (comma separated lists of tags) and the values are the list of groups your monitor is broken down on.
<any-key>
object
Monitor state for a single group.
last_nodata_ts
int64
Latest timestamp the monitor was in NO_DATA state.
last_notified_ts
int64
Latest timestamp of the notification sent for this monitor group.
last_resolved_ts
int64
Latest timestamp the monitor group was resolved.
last_triggered_ts
int64
Latest timestamp the monitor group triggered.
name
string
The name of the monitor.
status
enum
The different states your monitor can be in. Allowed enum values: `Alert,Ignored,No Data,OK,Skipped,Unknown,Warn`
tags
[string]
Tags associated to your monitor.
type [_required_]
enum
The type of the monitor. For more information about `type`, see the [monitor options](https://docs.datadoghq.com/monitors/guide/monitor_api_options/) docs. Allowed enum values: `composite,event alert,log alert,metric alert,process alert,query alert,rum alert,service check,synthetics alert,trace-analytics alert,slo alert,event-v2 alert,audit alert,ci-pipelines alert,ci-tests alert,error-tracking alert,database-monitoring alert,network-performance alert,cost alert,data-quality alert`
```
{
  "assets": [
    {
      "category": "runbook",
      "name": "Monitor Runbook",
      "resource_key": "12345",
      "resource_type": "string",
      "url": "/notebooks/12345"
    }
  ],
  "created": "2019-09-19T10:00:00.000Z",
  "creator": {
    "email": "string",
    "handle": "string",
    "name": "string"
  },
  "deleted": "2019-09-19T10:00:00.000Z",
  "draft_status": "string",
  "id": "integer",
  "matching_downtimes": [
    {
      "end": 1412792983,
      "id": 1625,
      "scope": [
        "env:staging"
      ],
      "start": 1412792983
    }
  ],
  "message": "string",
  "modified": "2019-09-19T10:00:00.000Z",
  "multi": false,
  "name": "My monitor",
  "options": {
    "aggregation": {
      "group_by": "host",
      "metric": "metrics.name",
      "type": "count"
    },
    "device_ids": [],
    "enable_logs_sample": false,
    "enable_samples": false,
    "escalation_message": "string",
    "evaluation_delay": "integer",
    "group_retention_duration": "string",
    "groupby_simple_monitor": false,
    "include_tags": false,
    "locked": false,
    "min_failure_duration": "integer",
    "min_location_failed": "integer",
    "new_group_delay": "integer",
    "new_host_delay": "integer",
    "no_data_timeframe": "integer",
    "notification_preset_name": "string",
    "notify_audit": false,
    "notify_by": [],
    "notify_no_data": false,
    "on_missing_data": "string",
    "renotify_interval": "integer",
    "renotify_occurrences": "integer",
    "renotify_statuses": [],
    "require_full_window": false,
    "scheduling_options": {
      "custom_schedule": {
        "recurrences": [
          {
            "rrule": "FREQ=WEEKLY;BYDAY=MO,TU,WE,TH,FR",
            "start": "2023-08-31T16:30:00",
            "timezone": "Europe/Paris"
          }
        ]
      },
      "evaluation_window": {
        "day_starts": "04:00",
        "hour_starts": 0,
        "month_starts": 1,
        "timezone": "Europe/Paris"
      }
    },
    "silenced": {
      "<any-key>": "integer"
    },
    "synthetics_check_id": "string",
    "threshold_windows": {
      "recovery_window": "string",
      "trigger_window": "string"
    },
    "thresholds": {
      "critical": "number",
      "critical_recovery": "number",
      "ok": "number",
      "unknown": "number",
      "warning": "number",
      "warning_recovery": "number"
    },
    "timeout_h": "integer",
    "variables": [
      {
        "compute": {
          "aggregation": "avg",
          "interval": 60000,
          "metric": "@duration"
        },
        "data_source": "rum",
        "group_by": [
          {
            "facet": "status",
            "limit": 10,
            "sort": {
              "aggregation": "avg",
              "metric": "string",
              "order": "string"
            }
          }
        ],
        "indexes": [
          "days-3",
          "days-7"
        ],
        "name": "query_errors",
        "search": {
          "query": "service:query"
        }
      }
    ]
  },
  "overall_state": "string",
  "priority": "integer",
  "query": "avg(last_5m):sum:system.net.bytes_rcvd{host:host0} > 100",
  "restricted_roles": [],
  "state": {
    "groups": {
      "<any-key>": {
        "last_nodata_ts": "integer",
        "last_notified_ts": "integer",
        "last_resolved_ts": "integer",
        "last_triggered_ts": "integer",
        "name": "string",
        "status": "string"
      }
    }
  },
  "tags": [],
  "type": "query alert"
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


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
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


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
Monitor Not Found error
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


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
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/monitors/?code-lang=curl)
  * [Ruby [legacy]](https://docs.datadoghq.com/api/latest/monitors/?code-lang=ruby-legacy)
  * [Python [legacy]](https://docs.datadoghq.com/api/latest/monitors/?code-lang=python-legacy)


#####  Unmute a monitor
Copy
```
                  # Path parameters  
export monitor_id="CHANGE_ME"  
# Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/monitor/${monitor_id}/unmute" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Unmute a monitor
```
require 'dogapi'

api_key = '<DATADOG_API_KEY>'
app_key = '<DATADOG_APPLICATION_KEY>'

dog = Dogapi::Client.new(api_key, app_key)

# Unmute an alert
dog.unmute_monitor(62_628)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby-legacy) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Unmute a monitor
```
from datadog import initialize, api

options = {
    'api_key': '<DATADOG_API_KEY>',
    'app_key': '<DATADOG_APPLICATION_KEY>'
}

initialize(**options)

# Unmute all alerts
api.Monitor.unmute(2088)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python-legacy) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python "example.py"


```

* * *
## [Get all monitors](https://docs.datadoghq.com/api/latest/monitors/#get-all-monitors)
  * [v1 (latest)](https://docs.datadoghq.com/api/latest/monitors/#get-all-monitors-v1)


GET https://api.ap1.datadoghq.com/api/v1/monitorhttps://api.ap2.datadoghq.com/api/v1/monitorhttps://api.datadoghq.eu/api/v1/monitorhttps://api.ddog-gov.com/api/v1/monitorhttps://api.datadoghq.com/api/v1/monitorhttps://api.us3.datadoghq.com/api/v1/monitorhttps://api.us5.datadoghq.com/api/v1/monitor
### Overview
Get all monitors from your organization. This endpoint requires the `monitors_read` permission.
OAuth apps require the `monitors_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#monitors) to access this endpoint.
### Arguments
#### Query Strings
Name
Type
Description
group_states
string
When specified, shows additional information about the group states. Choose one or more from `all`, `alert`, `warn`, and `no data`.
name
string
A string to filter monitors by name.
tags
string
A comma separated list indicating what tags, if any, should be used to filter the list of monitors by scope. For example, `host:host0`.
monitor_tags
string
A comma separated list indicating what service and/or custom tags, if any, should be used to filter the list of monitors. Tags created in the Datadog UI automatically have the service key prepended. For example, `service:my-app`.
with_downtimes
boolean
If this argument is set to true, then the returned data includes all current active downtimes for each monitor.
id_offset
integer
Use this parameter for paginating through large sets of monitors. Start with a value of zero, make a request, set the value to the last ID of result set, and then repeat until the response is empty.
page
integer
The page to start paginating from. If this argument is not specified, the request returns all monitors without pagination.
page_size
integer
The number of monitors to return per page. If the page argument is not specified, the default behavior returns all monitors without a `page_size` limit. However, if page is specified and `page_size` is not, the argument defaults to 100.
### Response
  * [200](https://docs.datadoghq.com/api/latest/monitors/#ListMonitors-200-v1)
  * [400](https://docs.datadoghq.com/api/latest/monitors/#ListMonitors-400-v1)
  * [403](https://docs.datadoghq.com/api/latest/monitors/#ListMonitors-403-v1)
  * [429](https://docs.datadoghq.com/api/latest/monitors/#ListMonitors-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


An array of monitor objects.
Field
Type
Description
assets
[object]
The list of monitor assets tied to a monitor, which represents key links for users to take action on monitor alerts (for example, runbooks).
category [_required_]
enum
Indicates the type of asset this entity represents on a monitor. Allowed enum values: `runbook`
name [_required_]
string
Name for the monitor asset
resource_key
string
Represents the identifier of the internal Datadog resource that this asset represents. IDs in this field should be passed in as strings.
resource_type
enum
Type of internal Datadog resource associated with a monitor asset. Allowed enum values: `notebook`
url [_required_]
string
URL link for the asset. For links with an internal resource type set, this should be the relative path to where the Datadog domain is appended internally. For external links, this should be the full URL path.
created
date-time
Timestamp of the monitor creation.
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
deleted
date-time
Whether or not the monitor is deleted. (Always `null`)
draft_status
enum
Indicates whether the monitor is in a draft or published state.
`draft`: The monitor appears as Draft and does not send notifications. `published`: The monitor is active and evaluates conditions and notify as configured.
This field is in preview. The draft value is only available to customers with the feature enabled. Allowed enum values: `draft,published`
default: `published`
id
int64
ID of this monitor.
matching_downtimes
[object]
A list of active v1 downtimes that match this monitor.
end
int64
POSIX timestamp to end the downtime.
id [_required_]
int64
The downtime ID.
scope
[string]
The scope(s) to which the downtime applies. Must be in `key:value` format. For example, `host:app2`. Provide multiple scopes as a comma-separated list like `env:dev,env:prod`. The resulting downtime applies to sources that matches ALL provided scopes (`env:dev` **AND** `env:prod`).
start
int64
POSIX timestamp to start the downtime.
message
string
A message to include with notifications for this monitor.
modified
date-time
Last timestamp when the monitor was edited.
multi
boolean
Whether or not the monitor is broken down on different groups.
name
string
The monitor name.
options
object
List of options associated with your monitor.
aggregation
object
Type of aggregation performed in the monitor query.
group_by
string
Group to break down the monitor on.
metric
string
Metric name used in the monitor.
type
string
Metric type used in the monitor.
device_ids
[string]
**DEPRECATED** : IDs of the device the Synthetics monitor is running on.
enable_logs_sample
boolean
Whether or not to send a log sample when the log monitor triggers.
enable_samples
boolean
Whether or not to send a list of samples when the monitor triggers. This is only used by CI Test and Pipeline monitors.
escalation_message
string
We recommend using the [is_renotify](https://docs.datadoghq.com/monitors/notify/?tab=is_alert#renotify), block in the original message instead. A message to include with a re-notification. Supports the `@username` notification we allow elsewhere. Not applicable if `renotify_interval` is `None`.
evaluation_delay
int64
Time (in seconds) to delay evaluation, as a non-negative integer. For example, if the value is set to `300` (5min), the timeframe is set to `last_5m` and the time is 7:00, the monitor evaluates data from 6:50 to 6:55. This is useful for AWS CloudWatch and other backfilled metrics to ensure the monitor always has data during evaluation.
group_retention_duration
string
The time span after which groups with missing data are dropped from the monitor state. The minimum value is one hour, and the maximum value is 72 hours. Example values are: "60m", "1h", and "2d". This option is only available for APM Trace Analytics, Audit Trail, CI, Error Tracking, Event, Logs, and RUM monitors.
groupby_simple_monitor
boolean
**DEPRECATED** : Whether the log alert monitor triggers a single alert or multiple alerts when any group breaches a threshold. Use `notify_by` instead.
include_tags
boolean
A Boolean indicating whether notifications from this monitor automatically inserts its triggering tags into the title.
**Examples**
  * If `True`, `[Triggered on {host:h1}] Monitor Title`
  * If `False`, `[Triggered] Monitor Title`


default: `true`
locked
boolean
**DEPRECATED** : Whether or not the monitor is locked (only editable by creator and admins). Use `restricted_roles` instead.
min_failure_duration
int64
How long the test should be in failure before alerting (integer, number of seconds, max 7200).
min_location_failed
int64
The minimum number of locations in failure at the same time during at least one moment in the `min_failure_duration` period (`min_location_failed` and `min_failure_duration` are part of the advanced alerting rules - integer, >= 1).
default: `1`
new_group_delay
int64
Time (in seconds) to skip evaluations for new groups.
For example, this option can be used to skip evaluations for new hosts while they initialize.
Must be a non negative integer.
new_host_delay
int64
**DEPRECATED** : Time (in seconds) to allow a host to boot and applications to fully start before starting the evaluation of monitor results. Should be a non negative integer.
Use new_group_delay instead.
default: `300`
no_data_timeframe
int64
The number of minutes before a monitor notifies after data stops reporting. Datadog recommends at least 2x the monitor timeframe for query alerts or 2 minutes for service checks. If omitted, 2x the evaluation timeframe is used for query alerts, and 24 hours is used for service checks.
notification_preset_name
enum
Toggles the display of additional content sent in the monitor notification. Allowed enum values: `show_all,hide_query,hide_handles,hide_all`
default: `show_all`
notify_audit
boolean
A Boolean indicating whether tagged users is notified on changes to this monitor.
notify_by
[string]
Controls what granularity a monitor alerts on. Only available for monitors with groupings. For instance, a monitor grouped by `cluster`, `namespace`, and `pod` can be configured to only notify on each new `cluster` violating the alert conditions by setting `notify_by` to `["cluster"]`. Tags mentioned in `notify_by` must be a subset of the grouping tags in the query. For example, a query grouped by `cluster` and `namespace` cannot notify on `region`. Setting `notify_by` to `["*"]` configures the monitor to notify as a simple-alert.
notify_no_data
boolean
A Boolean indicating whether this monitor notifies when data stops reporting. Defaults to `false`.
on_missing_data
enum
Controls how groups or monitors are treated if an evaluation does not return any data points. The default option results in different behavior depending on the monitor query type. For monitors using Count queries, an empty monitor evaluation is treated as 0 and is compared to the threshold conditions. For monitors using any query type other than Count, for example Gauge, Measure, or Rate, the monitor shows the last known status. This option is only available for APM Trace Analytics, Audit Trail, CI, Error Tracking, Event, Logs, and RUM monitors. Allowed enum values: `default,show_no_data,show_and_notify_no_data,resolve`
renotify_interval
int64
The number of minutes after the last notification before a monitor re-notifies on the current status. It only re-notifies if it’s not resolved.
renotify_occurrences
int64
The number of times re-notification messages should be sent on the current status at the provided re-notification interval.
renotify_statuses
[string]
The types of monitor statuses for which re-notification messages are sent. Default: **null** if `renotify_interval` is **null**. If `renotify_interval` is set, defaults to renotify on `Alert` and `No Data`.
require_full_window
boolean
A Boolean indicating whether this monitor needs a full window of data before it’s evaluated. We highly recommend you set this to `false` for sparse metrics, otherwise some evaluations are skipped. Default is false. This setting only applies to metric monitors.
scheduling_options
object
Configuration options for scheduling.
custom_schedule
object
Configuration options for the custom schedule. **This feature is in private beta.**
recurrences
[object]
Array of custom schedule recurrences.
rrule
string
Defines the recurrence rule (RRULE) for a given schedule.
start
string
Defines the start date and time of the recurring schedule.
timezone
string
Defines the timezone the schedule runs on.
evaluation_window
object
Configuration options for the evaluation window. If `hour_starts` is set, no other fields may be set. Otherwise, `day_starts` and `month_starts` must be set together.
day_starts
string
The time of the day at which a one day cumulative evaluation window starts.
hour_starts
int32
The minute of the hour at which a one hour cumulative evaluation window starts.
month_starts
int32
The day of the month at which a one month cumulative evaluation window starts.
timezone
string
The timezone of the time of the day of the cumulative evaluation window start.
silenced
object
**DEPRECATED** : Information about the downtime applied to the monitor. Only shows v1 downtimes.
<any-key>
int64
UTC epoch timestamp in seconds when the downtime for the group expires.
synthetics_check_id
string
**DEPRECATED** : ID of the corresponding Synthetic check.
threshold_windows
object
Alerting time window options.
recovery_window
string
Describes how long an anomalous metric must be normal before the alert recovers.
trigger_window
string
Describes how long a metric must be anomalous before an alert triggers.
thresholds
object
List of the different monitor threshold available.
critical
double
The monitor `CRITICAL` threshold.
critical_recovery
double
The monitor `CRITICAL` recovery threshold.
ok
double
The monitor `OK` threshold.
unknown
double
The monitor UNKNOWN threshold.
warning
double
The monitor `WARNING` threshold.
warning_recovery
double
The monitor `WARNING` recovery threshold.
timeout_h
int64
The number of hours of the monitor not reporting data before it automatically resolves from a triggered state. The minimum allowed value is 0 hours. The maximum allowed value is 24 hours.
variables
[ <oneOf>]
List of requests that can be used in the monitor query. **This feature is currently in beta.**
Option 1
object
A formula and functions events query.
compute [_required_]
object
Compute options.
aggregation [_required_]
enum
Aggregation methods for event platform queries. Allowed enum values: `count,cardinality,median,pc75,pc90,pc95,pc98,pc99,sum,min,max,avg`
interval
int64
A time interval in milliseconds.
metric
string
Measurable attribute to compute.
data_source [_required_]
enum
Data source for event platform-based queries. Allowed enum values: `rum,ci_pipelines,ci_tests,audit,events,logs,spans,database_queries,network`
group_by
[object]
Group by options.
facet [_required_]
string
Event facet.
limit
int64
Number of groups to return.
sort
object
Options for sorting group by results.
aggregation [_required_]
enum
Aggregation methods for event platform queries. Allowed enum values: `count,cardinality,median,pc75,pc90,pc95,pc98,pc99,sum,min,max,avg`
metric
string
Metric used for sorting group by results.
order
enum
Direction of sort. Allowed enum values: `asc,desc`
default: `desc`
indexes
[string]
An array of index names to query in the stream. Omit or use `[]` to query all indexes at once.
name [_required_]
string
Name of the query for use in formulas.
search
object
Search options.
query [_required_]
string
Events search string.
Option 2
object
A formula and functions cost query.
aggregator
enum
Aggregation methods for metric queries. Allowed enum values: `avg,sum,max,min,last,area,l2norm,percentile,stddev`
data_source [_required_]
enum
Data source for cost queries. Allowed enum values: `metrics,cloud_cost,datadog_usage`
name [_required_]
string
Name of the query for use in formulas.
query [_required_]
string
The monitor query.
Option 3
object
A formula and functions data quality query.
data_source [_required_]
enum
Data source for data quality queries. Allowed enum values: `data_quality_metrics`
filter [_required_]
string
Filter expression used to match on data entities. Uses Aastra query syntax.
group_by
[string]
Optional grouping fields for aggregation.
measure [_required_]
string
The data quality measure to query. Common values include: `bytes`, `cardinality`, `custom`, `freshness`, `max`, `mean`, `min`, `nullness`, `percent_negative`, `percent_zero`, `row_count`, `stddev`, `sum`, `uniqueness`. Additional values may be supported.
monitor_options
object
Monitor configuration options for data quality queries.
crontab_override
string
Crontab expression to override the default schedule.
custom_sql
string
Custom SQL query for the monitor.
custom_where
string
Custom WHERE clause for the query.
group_by_columns
[string]
Columns to group results by.
model_type_override
enum
Override for the model type used in anomaly detection. Allowed enum values: `freshness,percentage,any`
name [_required_]
string
Name of the query for use in formulas.
schema_version
string
Schema version for the data quality query.
scope
string
Optional scoping expression to further filter metrics. Uses metrics filter syntax. This is useful when an entity has been configured to emit metrics with additional tags.
overall_state
enum
The different states your monitor can be in. Allowed enum values: `Alert,Ignored,No Data,OK,Skipped,Unknown,Warn`
priority
int64
Integer from 1 (high) to 5 (low) indicating alert severity.
query
string
The monitor query.
restricted_roles
[string]
A list of unique role identifiers to define which roles are allowed to edit the monitor. The unique identifiers for all roles can be pulled from the [Roles API](https://docs.datadoghq.com/api/latest/roles/#list-roles) and are located in the `data.id` field. Editing a monitor includes any updates to the monitor configuration, monitor deletion, and muting of the monitor for any amount of time. You can use the [Restriction Policies API](https://docs.datadoghq.com/api/latest/restriction-policies/) to manage write authorization for individual monitors by teams and users, in addition to roles.
state
object
Wrapper object with the different monitor states.
groups
object
Dictionary where the keys are groups (comma separated lists of tags) and the values are the list of groups your monitor is broken down on.
<any-key>
object
Monitor state for a single group.
last_nodata_ts
int64
Latest timestamp the monitor was in NO_DATA state.
last_notified_ts
int64
Latest timestamp of the notification sent for this monitor group.
last_resolved_ts
int64
Latest timestamp the monitor group was resolved.
last_triggered_ts
int64
Latest timestamp the monitor group triggered.
name
string
The name of the monitor.
status
enum
The different states your monitor can be in. Allowed enum values: `Alert,Ignored,No Data,OK,Skipped,Unknown,Warn`
tags
[string]
Tags associated to your monitor.
type
enum
The type of the monitor. For more information about `type`, see the [monitor options](https://docs.datadoghq.com/monitors/guide/monitor_api_options/) docs. Allowed enum values: `composite,event alert,log alert,metric alert,process alert,query alert,rum alert,service check,synthetics alert,trace-analytics alert,slo alert,event-v2 alert,audit alert,ci-pipelines alert,ci-tests alert,error-tracking alert,database-monitoring alert,network-performance alert,cost alert,data-quality alert`
```
{
  "assets": [
    {
      "category": "runbook",
      "name": "Monitor Runbook",
      "resource_key": "12345",
      "resource_type": "string",
      "url": "/notebooks/12345"
    }
  ],
  "created": "2019-09-19T10:00:00.000Z",
  "creator": {
    "email": "string",
    "handle": "string",
    "name": "string"
  },
  "deleted": "2019-09-19T10:00:00.000Z",
  "draft_status": "string",
  "id": "integer",
  "matching_downtimes": [
    {
      "end": 1412792983,
      "id": 1625,
      "scope": [
        "env:staging"
      ],
      "start": 1412792983
    }
  ],
  "message": "string",
  "modified": "2019-09-19T10:00:00.000Z",
  "multi": false,
  "name": "My monitor",
  "options": {
    "aggregation": {
      "group_by": "host",
      "metric": "metrics.name",
      "type": "count"
    },
    "device_ids": [],
    "enable_logs_sample": false,
    "enable_samples": false,
    "escalation_message": "string",
    "evaluation_delay": "integer",
    "group_retention_duration": "string",
    "groupby_simple_monitor": false,
    "include_tags": false,
    "locked": false,
    "min_failure_duration": "integer",
    "min_location_failed": "integer",
    "new_group_delay": "integer",
    "new_host_delay": "integer",
    "no_data_timeframe": "integer",
    "notification_preset_name": "string",
    "notify_audit": false,
    "notify_by": [],
    "notify_no_data": false,
    "on_missing_data": "string",
    "renotify_interval": "integer",
    "renotify_occurrences": "integer",
    "renotify_statuses": [],
    "require_full_window": false,
    "scheduling_options": {
      "custom_schedule": {
        "recurrences": [
          {
            "rrule": "FREQ=WEEKLY;BYDAY=MO,TU,WE,TH,FR",
            "start": "2023-08-31T16:30:00",
            "timezone": "Europe/Paris"
          }
        ]
      },
      "evaluation_window": {
        "day_starts": "04:00",
        "hour_starts": 0,
        "month_starts": 1,
        "timezone": "Europe/Paris"
      }
    },
    "silenced": {
      "<any-key>": "integer"
    },
    "synthetics_check_id": "string",
    "threshold_windows": {
      "recovery_window": "string",
      "trigger_window": "string"
    },
    "thresholds": {
      "critical": "number",
      "critical_recovery": "number",
      "ok": "number",
      "unknown": "number",
      "warning": "number",
      "warning_recovery": "number"
    },
    "timeout_h": "integer",
    "variables": [
      {
        "compute": {
          "aggregation": "avg",
          "interval": 60000,
          "metric": "@duration"
        },
        "data_source": "rum",
        "group_by": [
          {
            "facet": "status",
            "limit": 10,
            "sort": {
              "aggregation": "avg",
              "metric": "string",
              "order": "string"
            }
          }
        ],
        "indexes": [
          "days-3",
          "days-7"
        ],
        "name": "query_errors",
        "search": {
          "query": "service:query"
        }
      }
    ]
  },
  "overall_state": "string",
  "priority": "integer",
  "query": "avg(last_5m):sum:system.net.bytes_rcvd{host:host0} > 100",
  "restricted_roles": [],
  "state": {
    "groups": {
      "<any-key>": {
        "last_nodata_ts": "integer",
        "last_notified_ts": "integer",
        "last_resolved_ts": "integer",
        "last_triggered_ts": "integer",
        "name": "string",
        "status": "string"
      }
    }
  },
  "tags": [],
  "type": "query alert"
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


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
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


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
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/monitors/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/monitors/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/monitors/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/monitors/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/monitors/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/monitors/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/monitors/?code-lang=typescript)
  * [Ruby [legacy]](https://docs.datadoghq.com/api/latest/monitors/?code-lang=ruby-legacy)
  * [Python [legacy]](https://docs.datadoghq.com/api/latest/monitors/?code-lang=python-legacy)


#####  Get all monitors
Copy
```
                  # Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/monitor" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get all monitors
```
"""
Get all monitors returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.monitors_api import MonitorsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MonitorsApi(api_client)
    response = api_instance.list_monitors()

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get all monitors
```
# Get all monitors returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::MonitorsAPI.new
p api_instance.list_monitors()

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get all monitors
```
require 'dogapi'

api_key = '<DATADOG_API_KEY>'
app_key = '<DATADOG_APPLICATION_KEY>'

dog = Dogapi::Client.new(api_key, app_key)

# Get all monitor details
dog.get_all_monitors

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby-legacy) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get all monitors
```
// Get all monitors returns "OK" response

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
	api := datadogV1.NewMonitorsApi(apiClient)
	resp, r, err := api.ListMonitors(ctx, *datadogV1.NewListMonitorsOptionalParameters())

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `MonitorsApi.ListMonitors`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `MonitorsApi.ListMonitors`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get all monitors
```
// Get all monitors returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.MonitorsApi;
import com.datadog.api.client.v1.model.Monitor;
import java.util.List;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    MonitorsApi apiInstance = new MonitorsApi(defaultClient);

    try {
      List<Monitor> result = apiInstance.listMonitors();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MonitorsApi#listMonitors");
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

#####  Get all monitors
```
from datadog import initialize, api

options = {
    'api_key': '<DATADOG_API_KEY>',
    'app_key': '<DATADOG_APPLICATION_KEY>'
}

initialize(**options)

# Get all monitor details
print(api.Monitor.get_all())

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python-legacy) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python "example.py"


```

#####  Get all monitors
```
// Get all monitors returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_monitors::ListMonitorsOptionalParams;
use datadog_api_client::datadogV1::api_monitors::MonitorsAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = MonitorsAPI::with_config(configuration);
    let resp = api
        .list_monitors(ListMonitorsOptionalParams::default())
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

#####  Get all monitors
```
/**
 * Get all monitors returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.MonitorsApi(configuration);

apiInstance
  .listMonitors()
  .then((data: v1.Monitor[]) => {
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
## [Monitors group search](https://docs.datadoghq.com/api/latest/monitors/#monitors-group-search)
  * [v1 (latest)](https://docs.datadoghq.com/api/latest/monitors/#monitors-group-search-v1)


GET https://api.ap1.datadoghq.com/api/v1/monitor/groups/searchhttps://api.ap2.datadoghq.com/api/v1/monitor/groups/searchhttps://api.datadoghq.eu/api/v1/monitor/groups/searchhttps://api.ddog-gov.com/api/v1/monitor/groups/searchhttps://api.datadoghq.com/api/v1/monitor/groups/searchhttps://api.us3.datadoghq.com/api/v1/monitor/groups/searchhttps://api.us5.datadoghq.com/api/v1/monitor/groups/search
### Overview
Search and filter your monitor groups details. This endpoint requires the `monitors_read` permission.
OAuth apps require the `monitors_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#monitors) to access this endpoint.
### Arguments
#### Query Strings
Name
Type
Description
query
string
After entering a search query on the [Triggered Monitors page](https://app.datadoghq.com/monitors/triggered), use the query parameter value in the URL of the page as a value for this parameter. For more information, see the [Manage Monitors documentation](https://docs.datadoghq.com/monitors/manage/#triggered-monitors).
The query can contain any number of space-separated monitor attributes, for instance: `query="type:metric group_status:alert"`.
page
integer
Page to start paginating from.
per_page
integer
Number of monitors to return per page.
sort
string
String for sort order, composed of field and sort order separate by a comma, for example `name,asc`. Supported sort directions: `asc`, `desc`. Supported fields:
  * `name`
  * `status`
  * `tags`


### Response
  * [200](https://docs.datadoghq.com/api/latest/monitors/#SearchMonitorGroups-200-v1)
  * [400](https://docs.datadoghq.com/api/latest/monitors/#SearchMonitorGroups-400-v1)
  * [403](https://docs.datadoghq.com/api/latest/monitors/#SearchMonitorGroups-403-v1)
  * [429](https://docs.datadoghq.com/api/latest/monitors/#SearchMonitorGroups-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


The response of a monitor group search.
Field
Type
Description
counts
object
The counts of monitor groups per different criteria.
status
[object]
Search facets.
count
int64
The number of found monitors with the listed value.
name
The facet value.
type
[object]
Search facets.
count
int64
The number of found monitors with the listed value.
name
The facet value.
groups
[object]
The list of found monitor groups.
group
string
The name of the group.
group_tags
[string]
The list of tags of the monitor group.
last_nodata_ts
int64
Latest timestamp the monitor group was in NO_DATA state.
last_triggered_ts
int64
Latest timestamp the monitor group triggered.
monitor_id
int64
The ID of the monitor.
monitor_name
string
The name of the monitor.
status
enum
The different states your monitor can be in. Allowed enum values: `Alert,Ignored,No Data,OK,Skipped,Unknown,Warn`
metadata
object
Metadata about the response.
page
int64
The page to start paginating from.
page_count
int64
The number of pages.
per_page
int64
The number of monitors to return per page.
total_count
int64
The total number of monitors.
```
{
  "counts": {
    "status": [
      {
        "count": 2,
        "name": "OK"
      }
    ],
    "type": [
      {
        "count": 2,
        "name": "metric"
      }
    ]
  },
  "groups": [
    {
      "group": "*",
      "group_tags": [
        "*"
      ],
      "last_nodata_ts": 0,
      "last_triggered_ts": 1525702966,
      "monitor_id": 2738266,
      "monitor_name": "[demo] Cassandra disk usage is high on {{host.name}}",
      "status": "OK"
    },
    {
      "group": "*",
      "group_tags": [
        "*"
      ],
      "last_nodata_ts": 0,
      "last_triggered_ts": 1525703008,
      "monitor_id": 1576648,
      "monitor_name": "[demo] Disk usage is high on {{host.name}}",
      "status": "OK"
    }
  ],
  "metadata": {
    "page": 0,
    "page_count": 2,
    "per_page": 30,
    "total_count": 2
  }
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


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
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


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
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/monitors/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/monitors/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/monitors/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/monitors/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/monitors/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/monitors/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/monitors/?code-lang=typescript)
  * [Ruby [legacy]](https://docs.datadoghq.com/api/latest/monitors/?code-lang=ruby-legacy)
  * [Python [legacy]](https://docs.datadoghq.com/api/latest/monitors/?code-lang=python-legacy)


#####  Monitors group search
Copy
```
                  # Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/monitor/groups/search" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Monitors group search
```
"""
Monitors group search returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.monitors_api import MonitorsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MonitorsApi(api_client)
    response = api_instance.search_monitor_groups()

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Monitors group search
```
# Monitors group search returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::MonitorsAPI.new
p api_instance.search_monitor_groups()

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Monitors group search
```
require 'dogapi'

api_key = '<DATADOG_API_KEY>'
app_key = '<DATADOG_APPLICATION_KEY>'

dog = Dogapi::Client.new(api_key, app_key)

# Search monitor groups
dog.search_monitor_groups

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby-legacy) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Monitors group search
```
// Monitors group search returns "OK" response

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
	api := datadogV1.NewMonitorsApi(apiClient)
	resp, r, err := api.SearchMonitorGroups(ctx, *datadogV1.NewSearchMonitorGroupsOptionalParameters())

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `MonitorsApi.SearchMonitorGroups`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `MonitorsApi.SearchMonitorGroups`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Monitors group search
```
// Monitors group search returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.MonitorsApi;
import com.datadog.api.client.v1.model.MonitorGroupSearchResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    MonitorsApi apiInstance = new MonitorsApi(defaultClient);

    try {
      MonitorGroupSearchResponse result = apiInstance.searchMonitorGroups();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MonitorsApi#searchMonitorGroups");
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

#####  Monitors group search
```
from datadog import initialize, api

options = {
	'api_key': '<DATADOG_API_KEY>',
	'app_key': '<DATADOG_APPLICATION_KEY>'
}

initialize(**options)

# Search monitor groups
api.Monitor.search_groups()

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python-legacy) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python "example.py"


```

#####  Monitors group search
```
// Monitors group search returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_monitors::MonitorsAPI;
use datadog_api_client::datadogV1::api_monitors::SearchMonitorGroupsOptionalParams;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = MonitorsAPI::with_config(configuration);
    let resp = api
        .search_monitor_groups(SearchMonitorGroupsOptionalParams::default())
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

#####  Monitors group search
```
/**
 * Monitors group search returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.MonitorsApi(configuration);

apiInstance
  .searchMonitorGroups()
  .then((data: v1.MonitorGroupSearchResponse) => {
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
## [Mute a monitor](https://docs.datadoghq.com/api/latest/monitors/#mute-a-monitor)
  * [v1 (latest)](https://docs.datadoghq.com/api/latest/monitors/#mute-a-monitor-v1)


POST https://api.ap1.datadoghq.com/api/v1/monitor/{monitor_id}/mutehttps://api.ap2.datadoghq.com/api/v1/monitor/{monitor_id}/mutehttps://api.datadoghq.eu/api/v1/monitor/{monitor_id}/mutehttps://api.ddog-gov.com/api/v1/monitor/{monitor_id}/mutehttps://api.datadoghq.com/api/v1/monitor/{monitor_id}/mutehttps://api.us3.datadoghq.com/api/v1/monitor/{monitor_id}/mutehttps://api.us5.datadoghq.com/api/v1/monitor/{monitor_id}/mute
### Overview
Mute the specified monitor. This endpoint requires the `monitors_write` permission.
OAuth apps require the `monitors_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#monitors) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
monitor_id [_required_]
integer
The id of the monitor
#### Query Strings
Name
Type
Description
scope
string
The scope to apply the mute to. For example, if your alert is grouped by `{host}`, you might mute `host:app1`.
end
integer
A POSIX timestamp for when the mute should end.
### Response
  * [200](https://docs.datadoghq.com/api/latest/monitors/#MuteMonitor-200-v1)
  * [400](https://docs.datadoghq.com/api/latest/monitors/#MuteMonitor-400-v1)
  * [401](https://docs.datadoghq.com/api/latest/monitors/#MuteMonitor-401-v1)
  * [404](https://docs.datadoghq.com/api/latest/monitors/#MuteMonitor-404-v1)
  * [429](https://docs.datadoghq.com/api/latest/monitors/#MuteMonitor-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


Object describing a monitor.
Field
Type
Description
assets
[object]
The list of monitor assets tied to a monitor, which represents key links for users to take action on monitor alerts (for example, runbooks).
category [_required_]
enum
Indicates the type of asset this entity represents on a monitor. Allowed enum values: `runbook`
name [_required_]
string
Name for the monitor asset
resource_key
string
Represents the identifier of the internal Datadog resource that this asset represents. IDs in this field should be passed in as strings.
resource_type
enum
Type of internal Datadog resource associated with a monitor asset. Allowed enum values: `notebook`
url [_required_]
string
URL link for the asset. For links with an internal resource type set, this should be the relative path to where the Datadog domain is appended internally. For external links, this should be the full URL path.
created
date-time
Timestamp of the monitor creation.
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
deleted
date-time
Whether or not the monitor is deleted. (Always `null`)
draft_status
enum
Indicates whether the monitor is in a draft or published state.
`draft`: The monitor appears as Draft and does not send notifications. `published`: The monitor is active and evaluates conditions and notify as configured.
This field is in preview. The draft value is only available to customers with the feature enabled. Allowed enum values: `draft,published`
default: `published`
id
int64
ID of this monitor.
matching_downtimes
[object]
A list of active v1 downtimes that match this monitor.
end
int64
POSIX timestamp to end the downtime.
id [_required_]
int64
The downtime ID.
scope
[string]
The scope(s) to which the downtime applies. Must be in `key:value` format. For example, `host:app2`. Provide multiple scopes as a comma-separated list like `env:dev,env:prod`. The resulting downtime applies to sources that matches ALL provided scopes (`env:dev` **AND** `env:prod`).
start
int64
POSIX timestamp to start the downtime.
message
string
A message to include with notifications for this monitor.
modified
date-time
Last timestamp when the monitor was edited.
multi
boolean
Whether or not the monitor is broken down on different groups.
name
string
The monitor name.
options
object
List of options associated with your monitor.
aggregation
object
Type of aggregation performed in the monitor query.
group_by
string
Group to break down the monitor on.
metric
string
Metric name used in the monitor.
type
string
Metric type used in the monitor.
device_ids
[string]
**DEPRECATED** : IDs of the device the Synthetics monitor is running on.
enable_logs_sample
boolean
Whether or not to send a log sample when the log monitor triggers.
enable_samples
boolean
Whether or not to send a list of samples when the monitor triggers. This is only used by CI Test and Pipeline monitors.
escalation_message
string
We recommend using the [is_renotify](https://docs.datadoghq.com/monitors/notify/?tab=is_alert#renotify), block in the original message instead. A message to include with a re-notification. Supports the `@username` notification we allow elsewhere. Not applicable if `renotify_interval` is `None`.
evaluation_delay
int64
Time (in seconds) to delay evaluation, as a non-negative integer. For example, if the value is set to `300` (5min), the timeframe is set to `last_5m` and the time is 7:00, the monitor evaluates data from 6:50 to 6:55. This is useful for AWS CloudWatch and other backfilled metrics to ensure the monitor always has data during evaluation.
group_retention_duration
string
The time span after which groups with missing data are dropped from the monitor state. The minimum value is one hour, and the maximum value is 72 hours. Example values are: "60m", "1h", and "2d". This option is only available for APM Trace Analytics, Audit Trail, CI, Error Tracking, Event, Logs, and RUM monitors.
groupby_simple_monitor
boolean
**DEPRECATED** : Whether the log alert monitor triggers a single alert or multiple alerts when any group breaches a threshold. Use `notify_by` instead.
include_tags
boolean
A Boolean indicating whether notifications from this monitor automatically inserts its triggering tags into the title.
**Examples**
  * If `True`, `[Triggered on {host:h1}] Monitor Title`
  * If `False`, `[Triggered] Monitor Title`


default: `true`
locked
boolean
**DEPRECATED** : Whether or not the monitor is locked (only editable by creator and admins). Use `restricted_roles` instead.
min_failure_duration
int64
How long the test should be in failure before alerting (integer, number of seconds, max 7200).
min_location_failed
int64
The minimum number of locations in failure at the same time during at least one moment in the `min_failure_duration` period (`min_location_failed` and `min_failure_duration` are part of the advanced alerting rules - integer, >= 1).
default: `1`
new_group_delay
int64
Time (in seconds) to skip evaluations for new groups.
For example, this option can be used to skip evaluations for new hosts while they initialize.
Must be a non negative integer.
new_host_delay
int64
**DEPRECATED** : Time (in seconds) to allow a host to boot and applications to fully start before starting the evaluation of monitor results. Should be a non negative integer.
Use new_group_delay instead.
default: `300`
no_data_timeframe
int64
The number of minutes before a monitor notifies after data stops reporting. Datadog recommends at least 2x the monitor timeframe for query alerts or 2 minutes for service checks. If omitted, 2x the evaluation timeframe is used for query alerts, and 24 hours is used for service checks.
notification_preset_name
enum
Toggles the display of additional content sent in the monitor notification. Allowed enum values: `show_all,hide_query,hide_handles,hide_all`
default: `show_all`
notify_audit
boolean
A Boolean indicating whether tagged users is notified on changes to this monitor.
notify_by
[string]
Controls what granularity a monitor alerts on. Only available for monitors with groupings. For instance, a monitor grouped by `cluster`, `namespace`, and `pod` can be configured to only notify on each new `cluster` violating the alert conditions by setting `notify_by` to `["cluster"]`. Tags mentioned in `notify_by` must be a subset of the grouping tags in the query. For example, a query grouped by `cluster` and `namespace` cannot notify on `region`. Setting `notify_by` to `["*"]` configures the monitor to notify as a simple-alert.
notify_no_data
boolean
A Boolean indicating whether this monitor notifies when data stops reporting. Defaults to `false`.
on_missing_data
enum
Controls how groups or monitors are treated if an evaluation does not return any data points. The default option results in different behavior depending on the monitor query type. For monitors using Count queries, an empty monitor evaluation is treated as 0 and is compared to the threshold conditions. For monitors using any query type other than Count, for example Gauge, Measure, or Rate, the monitor shows the last known status. This option is only available for APM Trace Analytics, Audit Trail, CI, Error Tracking, Event, Logs, and RUM monitors. Allowed enum values: `default,show_no_data,show_and_notify_no_data,resolve`
renotify_interval
int64
The number of minutes after the last notification before a monitor re-notifies on the current status. It only re-notifies if it’s not resolved.
renotify_occurrences
int64
The number of times re-notification messages should be sent on the current status at the provided re-notification interval.
renotify_statuses
[string]
The types of monitor statuses for which re-notification messages are sent. Default: **null** if `renotify_interval` is **null**. If `renotify_interval` is set, defaults to renotify on `Alert` and `No Data`.
require_full_window
boolean
A Boolean indicating whether this monitor needs a full window of data before it’s evaluated. We highly recommend you set this to `false` for sparse metrics, otherwise some evaluations are skipped. Default is false. This setting only applies to metric monitors.
scheduling_options
object
Configuration options for scheduling.
custom_schedule
object
Configuration options for the custom schedule. **This feature is in private beta.**
recurrences
[object]
Array of custom schedule recurrences.
rrule
string
Defines the recurrence rule (RRULE) for a given schedule.
start
string
Defines the start date and time of the recurring schedule.
timezone
string
Defines the timezone the schedule runs on.
evaluation_window
object
Configuration options for the evaluation window. If `hour_starts` is set, no other fields may be set. Otherwise, `day_starts` and `month_starts` must be set together.
day_starts
string
The time of the day at which a one day cumulative evaluation window starts.
hour_starts
int32
The minute of the hour at which a one hour cumulative evaluation window starts.
month_starts
int32
The day of the month at which a one month cumulative evaluation window starts.
timezone
string
The timezone of the time of the day of the cumulative evaluation window start.
silenced
object
**DEPRECATED** : Information about the downtime applied to the monitor. Only shows v1 downtimes.
<any-key>
int64
UTC epoch timestamp in seconds when the downtime for the group expires.
synthetics_check_id
string
**DEPRECATED** : ID of the corresponding Synthetic check.
threshold_windows
object
Alerting time window options.
recovery_window
string
Describes how long an anomalous metric must be normal before the alert recovers.
trigger_window
string
Describes how long a metric must be anomalous before an alert triggers.
thresholds
object
List of the different monitor threshold available.
critical
double
The monitor `CRITICAL` threshold.
critical_recovery
double
The monitor `CRITICAL` recovery threshold.
ok
double
The monitor `OK` threshold.
unknown
double
The monitor UNKNOWN threshold.
warning
double
The monitor `WARNING` threshold.
warning_recovery
double
The monitor `WARNING` recovery threshold.
timeout_h
int64
The number of hours of the monitor not reporting data before it automatically resolves from a triggered state. The minimum allowed value is 0 hours. The maximum allowed value is 24 hours.
variables
[ <oneOf>]
List of requests that can be used in the monitor query. **This feature is currently in beta.**
Option 1
object
A formula and functions events query.
compute [_required_]
object
Compute options.
aggregation [_required_]
enum
Aggregation methods for event platform queries. Allowed enum values: `count,cardinality,median,pc75,pc90,pc95,pc98,pc99,sum,min,max,avg`
interval
int64
A time interval in milliseconds.
metric
string
Measurable attribute to compute.
data_source [_required_]
enum
Data source for event platform-based queries. Allowed enum values: `rum,ci_pipelines,ci_tests,audit,events,logs,spans,database_queries,network`
group_by
[object]
Group by options.
facet [_required_]
string
Event facet.
limit
int64
Number of groups to return.
sort
object
Options for sorting group by results.
aggregation [_required_]
enum
Aggregation methods for event platform queries. Allowed enum values: `count,cardinality,median,pc75,pc90,pc95,pc98,pc99,sum,min,max,avg`
metric
string
Metric used for sorting group by results.
order
enum
Direction of sort. Allowed enum values: `asc,desc`
default: `desc`
indexes
[string]
An array of index names to query in the stream. Omit or use `[]` to query all indexes at once.
name [_required_]
string
Name of the query for use in formulas.
search
object
Search options.
query [_required_]
string
Events search string.
Option 2
object
A formula and functions cost query.
aggregator
enum
Aggregation methods for metric queries. Allowed enum values: `avg,sum,max,min,last,area,l2norm,percentile,stddev`
data_source [_required_]
enum
Data source for cost queries. Allowed enum values: `metrics,cloud_cost,datadog_usage`
name [_required_]
string
Name of the query for use in formulas.
query [_required_]
string
The monitor query.
Option 3
object
A formula and functions data quality query.
data_source [_required_]
enum
Data source for data quality queries. Allowed enum values: `data_quality_metrics`
filter [_required_]
string
Filter expression used to match on data entities. Uses Aastra query syntax.
group_by
[string]
Optional grouping fields for aggregation.
measure [_required_]
string
The data quality measure to query. Common values include: `bytes`, `cardinality`, `custom`, `freshness`, `max`, `mean`, `min`, `nullness`, `percent_negative`, `percent_zero`, `row_count`, `stddev`, `sum`, `uniqueness`. Additional values may be supported.
monitor_options
object
Monitor configuration options for data quality queries.
crontab_override
string
Crontab expression to override the default schedule.
custom_sql
string
Custom SQL query for the monitor.
custom_where
string
Custom WHERE clause for the query.
group_by_columns
[string]
Columns to group results by.
model_type_override
enum
Override for the model type used in anomaly detection. Allowed enum values: `freshness,percentage,any`
name [_required_]
string
Name of the query for use in formulas.
schema_version
string
Schema version for the data quality query.
scope
string
Optional scoping expression to further filter metrics. Uses metrics filter syntax. This is useful when an entity has been configured to emit metrics with additional tags.
overall_state
enum
The different states your monitor can be in. Allowed enum values: `Alert,Ignored,No Data,OK,Skipped,Unknown,Warn`
priority
int64
Integer from 1 (high) to 5 (low) indicating alert severity.
query [_required_]
string
The monitor query.
restricted_roles
[string]
A list of unique role identifiers to define which roles are allowed to edit the monitor. The unique identifiers for all roles can be pulled from the [Roles API](https://docs.datadoghq.com/api/latest/roles/#list-roles) and are located in the `data.id` field. Editing a monitor includes any updates to the monitor configuration, monitor deletion, and muting of the monitor for any amount of time. You can use the [Restriction Policies API](https://docs.datadoghq.com/api/latest/restriction-policies/) to manage write authorization for individual monitors by teams and users, in addition to roles.
state
object
Wrapper object with the different monitor states.
groups
object
Dictionary where the keys are groups (comma separated lists of tags) and the values are the list of groups your monitor is broken down on.
<any-key>
object
Monitor state for a single group.
last_nodata_ts
int64
Latest timestamp the monitor was in NO_DATA state.
last_notified_ts
int64
Latest timestamp of the notification sent for this monitor group.
last_resolved_ts
int64
Latest timestamp the monitor group was resolved.
last_triggered_ts
int64
Latest timestamp the monitor group triggered.
name
string
The name of the monitor.
status
enum
The different states your monitor can be in. Allowed enum values: `Alert,Ignored,No Data,OK,Skipped,Unknown,Warn`
tags
[string]
Tags associated to your monitor.
type [_required_]
enum
The type of the monitor. For more information about `type`, see the [monitor options](https://docs.datadoghq.com/monitors/guide/monitor_api_options/) docs. Allowed enum values: `composite,event alert,log alert,metric alert,process alert,query alert,rum alert,service check,synthetics alert,trace-analytics alert,slo alert,event-v2 alert,audit alert,ci-pipelines alert,ci-tests alert,error-tracking alert,database-monitoring alert,network-performance alert,cost alert,data-quality alert`
```
{
  "assets": [
    {
      "category": "runbook",
      "name": "Monitor Runbook",
      "resource_key": "12345",
      "resource_type": "string",
      "url": "/notebooks/12345"
    }
  ],
  "created": "2019-09-19T10:00:00.000Z",
  "creator": {
    "email": "string",
    "handle": "string",
    "name": "string"
  },
  "deleted": "2019-09-19T10:00:00.000Z",
  "draft_status": "string",
  "id": "integer",
  "matching_downtimes": [
    {
      "end": 1412792983,
      "id": 1625,
      "scope": [
        "env:staging"
      ],
      "start": 1412792983
    }
  ],
  "message": "string",
  "modified": "2019-09-19T10:00:00.000Z",
  "multi": false,
  "name": "My monitor",
  "options": {
    "aggregation": {
      "group_by": "host",
      "metric": "metrics.name",
      "type": "count"
    },
    "device_ids": [],
    "enable_logs_sample": false,
    "enable_samples": false,
    "escalation_message": "string",
    "evaluation_delay": "integer",
    "group_retention_duration": "string",
    "groupby_simple_monitor": false,
    "include_tags": false,
    "locked": false,
    "min_failure_duration": "integer",
    "min_location_failed": "integer",
    "new_group_delay": "integer",
    "new_host_delay": "integer",
    "no_data_timeframe": "integer",
    "notification_preset_name": "string",
    "notify_audit": false,
    "notify_by": [],
    "notify_no_data": false,
    "on_missing_data": "string",
    "renotify_interval": "integer",
    "renotify_occurrences": "integer",
    "renotify_statuses": [],
    "require_full_window": false,
    "scheduling_options": {
      "custom_schedule": {
        "recurrences": [
          {
            "rrule": "FREQ=WEEKLY;BYDAY=MO,TU,WE,TH,FR",
            "start": "2023-08-31T16:30:00",
            "timezone": "Europe/Paris"
          }
        ]
      },
      "evaluation_window": {
        "day_starts": "04:00",
        "hour_starts": 0,
        "month_starts": 1,
        "timezone": "Europe/Paris"
      }
    },
    "silenced": {
      "<any-key>": "integer"
    },
    "synthetics_check_id": "string",
    "threshold_windows": {
      "recovery_window": "string",
      "trigger_window": "string"
    },
    "thresholds": {
      "critical": "number",
      "critical_recovery": "number",
      "ok": "number",
      "unknown": "number",
      "warning": "number",
      "warning_recovery": "number"
    },
    "timeout_h": "integer",
    "variables": [
      {
        "compute": {
          "aggregation": "avg",
          "interval": 60000,
          "metric": "@duration"
        },
        "data_source": "rum",
        "group_by": [
          {
            "facet": "status",
            "limit": 10,
            "sort": {
              "aggregation": "avg",
              "metric": "string",
              "order": "string"
            }
          }
        ],
        "indexes": [
          "days-3",
          "days-7"
        ],
        "name": "query_errors",
        "search": {
          "query": "service:query"
        }
      }
    ]
  },
  "overall_state": "string",
  "priority": "integer",
  "query": "avg(last_5m):sum:system.net.bytes_rcvd{host:host0} > 100",
  "restricted_roles": [],
  "state": {
    "groups": {
      "<any-key>": {
        "last_nodata_ts": "integer",
        "last_notified_ts": "integer",
        "last_resolved_ts": "integer",
        "last_triggered_ts": "integer",
        "name": "string",
        "status": "string"
      }
    }
  },
  "tags": [],
  "type": "query alert"
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


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
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


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
Monitor Not Found error
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


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
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/monitors/?code-lang=curl)
  * [Ruby [legacy]](https://docs.datadoghq.com/api/latest/monitors/?code-lang=ruby-legacy)
  * [Python [legacy]](https://docs.datadoghq.com/api/latest/monitors/?code-lang=python-legacy)


#####  Mute a monitor
Copy
```
                  # Path parameters  
export monitor_id="CHANGE_ME"  
# Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/monitor/${monitor_id}/mute" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Mute a monitor
```
require 'dogapi'

api_key = '<DATADOG_API_KEY>'
app_key = '<DATADOG_APPLICATION_KEY>'

dog = Dogapi::Client.new(api_key, app_key)

# Mute a monitor
dog.mute_monitor(62_628)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby-legacy) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Mute a monitor
```

from datadog import initialize, api

options = {
    'api_key': '<DATADOG_API_KEY>',
    'app_key': '<DATADOG_APPLICATION_KEY>'
}

initialize(**options)

# Mute a monitor
api.Monitor.mute(2088)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python-legacy) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python "example.py"


```

* * *
## [Edit a monitor](https://docs.datadoghq.com/api/latest/monitors/#edit-a-monitor)
  * [v1 (latest)](https://docs.datadoghq.com/api/latest/monitors/#edit-a-monitor-v1)


PUT https://api.ap1.datadoghq.com/api/v1/monitor/{monitor_id}https://api.ap2.datadoghq.com/api/v1/monitor/{monitor_id}https://api.datadoghq.eu/api/v1/monitor/{monitor_id}https://api.ddog-gov.com/api/v1/monitor/{monitor_id}https://api.datadoghq.com/api/v1/monitor/{monitor_id}https://api.us3.datadoghq.com/api/v1/monitor/{monitor_id}https://api.us5.datadoghq.com/api/v1/monitor/{monitor_id}
### Overview
Edit the specified monitor. This endpoint requires the `monitors_write` permission.
OAuth apps require the `monitors_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#monitors) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
monitor_id [_required_]
integer
The ID of the monitor.
### Request
#### Body Data (required)
Edit a monitor request body.
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


Field
Type
Description
assets
[object]
The list of monitor assets tied to a monitor, which represents key links for users to take action on monitor alerts (for example, runbooks).
category [_required_]
enum
Indicates the type of asset this entity represents on a monitor. Allowed enum values: `runbook`
name [_required_]
string
Name for the monitor asset
resource_key
string
Represents the identifier of the internal Datadog resource that this asset represents. IDs in this field should be passed in as strings.
resource_type
enum
Type of internal Datadog resource associated with a monitor asset. Allowed enum values: `notebook`
url [_required_]
string
URL link for the asset. For links with an internal resource type set, this should be the relative path to where the Datadog domain is appended internally. For external links, this should be the full URL path.
created
date-time
Timestamp of the monitor creation.
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
deleted
date-time
Whether or not the monitor is deleted. (Always `null`)
draft_status
enum
Indicates whether the monitor is in a draft or published state.
`draft`: The monitor appears as Draft and does not send notifications. `published`: The monitor is active and evaluates conditions and notify as configured.
This field is in preview. The draft value is only available to customers with the feature enabled. Allowed enum values: `draft,published`
default: `published`
id
int64
ID of this monitor.
message
string
A message to include with notifications for this monitor.
modified
date-time
Last timestamp when the monitor was edited.
multi
boolean
Whether or not the monitor is broken down on different groups.
name
string
The monitor name.
options
object
List of options associated with your monitor.
aggregation
object
Type of aggregation performed in the monitor query.
group_by
string
Group to break down the monitor on.
metric
string
Metric name used in the monitor.
type
string
Metric type used in the monitor.
device_ids
[string]
**DEPRECATED** : IDs of the device the Synthetics monitor is running on.
enable_logs_sample
boolean
Whether or not to send a log sample when the log monitor triggers.
enable_samples
boolean
Whether or not to send a list of samples when the monitor triggers. This is only used by CI Test and Pipeline monitors.
escalation_message
string
We recommend using the [is_renotify](https://docs.datadoghq.com/monitors/notify/?tab=is_alert#renotify), block in the original message instead. A message to include with a re-notification. Supports the `@username` notification we allow elsewhere. Not applicable if `renotify_interval` is `None`.
evaluation_delay
int64
Time (in seconds) to delay evaluation, as a non-negative integer. For example, if the value is set to `300` (5min), the timeframe is set to `last_5m` and the time is 7:00, the monitor evaluates data from 6:50 to 6:55. This is useful for AWS CloudWatch and other backfilled metrics to ensure the monitor always has data during evaluation.
group_retention_duration
string
The time span after which groups with missing data are dropped from the monitor state. The minimum value is one hour, and the maximum value is 72 hours. Example values are: "60m", "1h", and "2d". This option is only available for APM Trace Analytics, Audit Trail, CI, Error Tracking, Event, Logs, and RUM monitors.
groupby_simple_monitor
boolean
**DEPRECATED** : Whether the log alert monitor triggers a single alert or multiple alerts when any group breaches a threshold. Use `notify_by` instead.
include_tags
boolean
A Boolean indicating whether notifications from this monitor automatically inserts its triggering tags into the title.
**Examples**
  * If `True`, `[Triggered on {host:h1}] Monitor Title`
  * If `False`, `[Triggered] Monitor Title`


default: `true`
locked
boolean
**DEPRECATED** : Whether or not the monitor is locked (only editable by creator and admins). Use `restricted_roles` instead.
min_failure_duration
int64
How long the test should be in failure before alerting (integer, number of seconds, max 7200).
min_location_failed
int64
The minimum number of locations in failure at the same time during at least one moment in the `min_failure_duration` period (`min_location_failed` and `min_failure_duration` are part of the advanced alerting rules - integer, >= 1).
default: `1`
new_group_delay
int64
Time (in seconds) to skip evaluations for new groups.
For example, this option can be used to skip evaluations for new hosts while they initialize.
Must be a non negative integer.
new_host_delay
int64
**DEPRECATED** : Time (in seconds) to allow a host to boot and applications to fully start before starting the evaluation of monitor results. Should be a non negative integer.
Use new_group_delay instead.
default: `300`
no_data_timeframe
int64
The number of minutes before a monitor notifies after data stops reporting. Datadog recommends at least 2x the monitor timeframe for query alerts or 2 minutes for service checks. If omitted, 2x the evaluation timeframe is used for query alerts, and 24 hours is used for service checks.
notification_preset_name
enum
Toggles the display of additional content sent in the monitor notification. Allowed enum values: `show_all,hide_query,hide_handles,hide_all`
default: `show_all`
notify_audit
boolean
A Boolean indicating whether tagged users is notified on changes to this monitor.
notify_by
[string]
Controls what granularity a monitor alerts on. Only available for monitors with groupings. For instance, a monitor grouped by `cluster`, `namespace`, and `pod` can be configured to only notify on each new `cluster` violating the alert conditions by setting `notify_by` to `["cluster"]`. Tags mentioned in `notify_by` must be a subset of the grouping tags in the query. For example, a query grouped by `cluster` and `namespace` cannot notify on `region`. Setting `notify_by` to `["*"]` configures the monitor to notify as a simple-alert.
notify_no_data
boolean
A Boolean indicating whether this monitor notifies when data stops reporting. Defaults to `false`.
on_missing_data
enum
Controls how groups or monitors are treated if an evaluation does not return any data points. The default option results in different behavior depending on the monitor query type. For monitors using Count queries, an empty monitor evaluation is treated as 0 and is compared to the threshold conditions. For monitors using any query type other than Count, for example Gauge, Measure, or Rate, the monitor shows the last known status. This option is only available for APM Trace Analytics, Audit Trail, CI, Error Tracking, Event, Logs, and RUM monitors. Allowed enum values: `default,show_no_data,show_and_notify_no_data,resolve`
renotify_interval
int64
The number of minutes after the last notification before a monitor re-notifies on the current status. It only re-notifies if it’s not resolved.
renotify_occurrences
int64
The number of times re-notification messages should be sent on the current status at the provided re-notification interval.
renotify_statuses
[string]
The types of monitor statuses for which re-notification messages are sent. Default: **null** if `renotify_interval` is **null**. If `renotify_interval` is set, defaults to renotify on `Alert` and `No Data`.
require_full_window
boolean
A Boolean indicating whether this monitor needs a full window of data before it’s evaluated. We highly recommend you set this to `false` for sparse metrics, otherwise some evaluations are skipped. Default is false. This setting only applies to metric monitors.
scheduling_options
object
Configuration options for scheduling.
custom_schedule
object
Configuration options for the custom schedule. **This feature is in private beta.**
recurrences
[object]
Array of custom schedule recurrences.
rrule
string
Defines the recurrence rule (RRULE) for a given schedule.
start
string
Defines the start date and time of the recurring schedule.
timezone
string
Defines the timezone the schedule runs on.
evaluation_window
object
Configuration options for the evaluation window. If `hour_starts` is set, no other fields may be set. Otherwise, `day_starts` and `month_starts` must be set together.
day_starts
string
The time of the day at which a one day cumulative evaluation window starts.
hour_starts
int32
The minute of the hour at which a one hour cumulative evaluation window starts.
month_starts
int32
The day of the month at which a one month cumulative evaluation window starts.
timezone
string
The timezone of the time of the day of the cumulative evaluation window start.
silenced
object
**DEPRECATED** : Information about the downtime applied to the monitor. Only shows v1 downtimes.
<any-key>
int64
UTC epoch timestamp in seconds when the downtime for the group expires.
synthetics_check_id
string
**DEPRECATED** : ID of the corresponding Synthetic check.
threshold_windows
object
Alerting time window options.
recovery_window
string
Describes how long an anomalous metric must be normal before the alert recovers.
trigger_window
string
Describes how long a metric must be anomalous before an alert triggers.
thresholds
object
List of the different monitor threshold available.
critical
double
The monitor `CRITICAL` threshold.
critical_recovery
double
The monitor `CRITICAL` recovery threshold.
ok
double
The monitor `OK` threshold.
unknown
double
The monitor UNKNOWN threshold.
warning
double
The monitor `WARNING` threshold.
warning_recovery
double
The monitor `WARNING` recovery threshold.
timeout_h
int64
The number of hours of the monitor not reporting data before it automatically resolves from a triggered state. The minimum allowed value is 0 hours. The maximum allowed value is 24 hours.
variables
[ <oneOf>]
List of requests that can be used in the monitor query. **This feature is currently in beta.**
Option 1
object
A formula and functions events query.
compute [_required_]
object
Compute options.
aggregation [_required_]
enum
Aggregation methods for event platform queries. Allowed enum values: `count,cardinality,median,pc75,pc90,pc95,pc98,pc99,sum,min,max,avg`
interval
int64
A time interval in milliseconds.
metric
string
Measurable attribute to compute.
data_source [_required_]
enum
Data source for event platform-based queries. Allowed enum values: `rum,ci_pipelines,ci_tests,audit,events,logs,spans,database_queries,network`
group_by
[object]
Group by options.
facet [_required_]
string
Event facet.
limit
int64
Number of groups to return.
sort
object
Options for sorting group by results.
aggregation [_required_]
enum
Aggregation methods for event platform queries. Allowed enum values: `count,cardinality,median,pc75,pc90,pc95,pc98,pc99,sum,min,max,avg`
metric
string
Metric used for sorting group by results.
order
enum
Direction of sort. Allowed enum values: `asc,desc`
default: `desc`
indexes
[string]
An array of index names to query in the stream. Omit or use `[]` to query all indexes at once.
name [_required_]
string
Name of the query for use in formulas.
search
object
Search options.
query [_required_]
string
Events search string.
Option 2
object
A formula and functions cost query.
aggregator
enum
Aggregation methods for metric queries. Allowed enum values: `avg,sum,max,min,last,area,l2norm,percentile,stddev`
data_source [_required_]
enum
Data source for cost queries. Allowed enum values: `metrics,cloud_cost,datadog_usage`
name [_required_]
string
Name of the query for use in formulas.
query [_required_]
string
The monitor query.
Option 3
object
A formula and functions data quality query.
data_source [_required_]
enum
Data source for data quality queries. Allowed enum values: `data_quality_metrics`
filter [_required_]
string
Filter expression used to match on data entities. Uses Aastra query syntax.
group_by
[string]
Optional grouping fields for aggregation.
measure [_required_]
string
The data quality measure to query. Common values include: `bytes`, `cardinality`, `custom`, `freshness`, `max`, `mean`, `min`, `nullness`, `percent_negative`, `percent_zero`, `row_count`, `stddev`, `sum`, `uniqueness`. Additional values may be supported.
monitor_options
object
Monitor configuration options for data quality queries.
crontab_override
string
Crontab expression to override the default schedule.
custom_sql
string
Custom SQL query for the monitor.
custom_where
string
Custom WHERE clause for the query.
group_by_columns
[string]
Columns to group results by.
model_type_override
enum
Override for the model type used in anomaly detection. Allowed enum values: `freshness,percentage,any`
name [_required_]
string
Name of the query for use in formulas.
schema_version
string
Schema version for the data quality query.
scope
string
Optional scoping expression to further filter metrics. Uses metrics filter syntax. This is useful when an entity has been configured to emit metrics with additional tags.
overall_state
enum
The different states your monitor can be in. Allowed enum values: `Alert,Ignored,No Data,OK,Skipped,Unknown,Warn`
priority
int64
Integer from 1 (high) to 5 (low) indicating alert severity.
query
string
The monitor query.
restricted_roles
[string]
A list of unique role identifiers to define which roles are allowed to edit the monitor. The unique identifiers for all roles can be pulled from the [Roles API](https://docs.datadoghq.com/api/latest/roles/#list-roles) and are located in the `data.id` field. Editing a monitor includes any updates to the monitor configuration, monitor deletion, and muting of the monitor for any amount of time. You can use the [Restriction Policies API](https://docs.datadoghq.com/api/latest/restriction-policies/) to manage write authorization for individual monitors by teams and users, in addition to roles.
state
object
Wrapper object with the different monitor states.
groups
object
Dictionary where the keys are groups (comma separated lists of tags) and the values are the list of groups your monitor is broken down on.
<any-key>
object
Monitor state for a single group.
last_nodata_ts
int64
Latest timestamp the monitor was in NO_DATA state.
last_notified_ts
int64
Latest timestamp of the notification sent for this monitor group.
last_resolved_ts
int64
Latest timestamp the monitor group was resolved.
last_triggered_ts
int64
Latest timestamp the monitor group triggered.
name
string
The name of the monitor.
status
enum
The different states your monitor can be in. Allowed enum values: `Alert,Ignored,No Data,OK,Skipped,Unknown,Warn`
tags
[string]
Tags associated to your monitor.
type
enum
The type of the monitor. For more information about `type`, see the [monitor options](https://docs.datadoghq.com/monitors/guide/monitor_api_options/) docs. Allowed enum values: `composite,event alert,log alert,metric alert,process alert,query alert,rum alert,service check,synthetics alert,trace-analytics alert,slo alert,event-v2 alert,audit alert,ci-pipelines alert,ci-tests alert,error-tracking alert,database-monitoring alert,network-performance alert,cost alert,data-quality alert`
```
{
  "name": "My monitor-updated",
  "priority": null,
  "options": {
    "evaluation_delay": null,
    "new_group_delay": 600,
    "new_host_delay": null,
    "renotify_interval": null,
    "thresholds": {
      "critical": 2,
      "warning": null
    },
    "timeout_h": null
  }
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/monitors/#UpdateMonitor-200-v1)
  * [400](https://docs.datadoghq.com/api/latest/monitors/#UpdateMonitor-400-v1)
  * [401](https://docs.datadoghq.com/api/latest/monitors/#UpdateMonitor-401-v1)
  * [403](https://docs.datadoghq.com/api/latest/monitors/#UpdateMonitor-403-v1)
  * [404](https://docs.datadoghq.com/api/latest/monitors/#UpdateMonitor-404-v1)
  * [429](https://docs.datadoghq.com/api/latest/monitors/#UpdateMonitor-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


Object describing a monitor.
Field
Type
Description
assets
[object]
The list of monitor assets tied to a monitor, which represents key links for users to take action on monitor alerts (for example, runbooks).
category [_required_]
enum
Indicates the type of asset this entity represents on a monitor. Allowed enum values: `runbook`
name [_required_]
string
Name for the monitor asset
resource_key
string
Represents the identifier of the internal Datadog resource that this asset represents. IDs in this field should be passed in as strings.
resource_type
enum
Type of internal Datadog resource associated with a monitor asset. Allowed enum values: `notebook`
url [_required_]
string
URL link for the asset. For links with an internal resource type set, this should be the relative path to where the Datadog domain is appended internally. For external links, this should be the full URL path.
created
date-time
Timestamp of the monitor creation.
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
deleted
date-time
Whether or not the monitor is deleted. (Always `null`)
draft_status
enum
Indicates whether the monitor is in a draft or published state.
`draft`: The monitor appears as Draft and does not send notifications. `published`: The monitor is active and evaluates conditions and notify as configured.
This field is in preview. The draft value is only available to customers with the feature enabled. Allowed enum values: `draft,published`
default: `published`
id
int64
ID of this monitor.
matching_downtimes
[object]
A list of active v1 downtimes that match this monitor.
end
int64
POSIX timestamp to end the downtime.
id [_required_]
int64
The downtime ID.
scope
[string]
The scope(s) to which the downtime applies. Must be in `key:value` format. For example, `host:app2`. Provide multiple scopes as a comma-separated list like `env:dev,env:prod`. The resulting downtime applies to sources that matches ALL provided scopes (`env:dev` **AND** `env:prod`).
start
int64
POSIX timestamp to start the downtime.
message
string
A message to include with notifications for this monitor.
modified
date-time
Last timestamp when the monitor was edited.
multi
boolean
Whether or not the monitor is broken down on different groups.
name
string
The monitor name.
options
object
List of options associated with your monitor.
aggregation
object
Type of aggregation performed in the monitor query.
group_by
string
Group to break down the monitor on.
metric
string
Metric name used in the monitor.
type
string
Metric type used in the monitor.
device_ids
[string]
**DEPRECATED** : IDs of the device the Synthetics monitor is running on.
enable_logs_sample
boolean
Whether or not to send a log sample when the log monitor triggers.
enable_samples
boolean
Whether or not to send a list of samples when the monitor triggers. This is only used by CI Test and Pipeline monitors.
escalation_message
string
We recommend using the [is_renotify](https://docs.datadoghq.com/monitors/notify/?tab=is_alert#renotify), block in the original message instead. A message to include with a re-notification. Supports the `@username` notification we allow elsewhere. Not applicable if `renotify_interval` is `None`.
evaluation_delay
int64
Time (in seconds) to delay evaluation, as a non-negative integer. For example, if the value is set to `300` (5min), the timeframe is set to `last_5m` and the time is 7:00, the monitor evaluates data from 6:50 to 6:55. This is useful for AWS CloudWatch and other backfilled metrics to ensure the monitor always has data during evaluation.
group_retention_duration
string
The time span after which groups with missing data are dropped from the monitor state. The minimum value is one hour, and the maximum value is 72 hours. Example values are: "60m", "1h", and "2d". This option is only available for APM Trace Analytics, Audit Trail, CI, Error Tracking, Event, Logs, and RUM monitors.
groupby_simple_monitor
boolean
**DEPRECATED** : Whether the log alert monitor triggers a single alert or multiple alerts when any group breaches a threshold. Use `notify_by` instead.
include_tags
boolean
A Boolean indicating whether notifications from this monitor automatically inserts its triggering tags into the title.
**Examples**
  * If `True`, `[Triggered on {host:h1}] Monitor Title`
  * If `False`, `[Triggered] Monitor Title`


default: `true`
locked
boolean
**DEPRECATED** : Whether or not the monitor is locked (only editable by creator and admins). Use `restricted_roles` instead.
min_failure_duration
int64
How long the test should be in failure before alerting (integer, number of seconds, max 7200).
min_location_failed
int64
The minimum number of locations in failure at the same time during at least one moment in the `min_failure_duration` period (`min_location_failed` and `min_failure_duration` are part of the advanced alerting rules - integer, >= 1).
default: `1`
new_group_delay
int64
Time (in seconds) to skip evaluations for new groups.
For example, this option can be used to skip evaluations for new hosts while they initialize.
Must be a non negative integer.
new_host_delay
int64
**DEPRECATED** : Time (in seconds) to allow a host to boot and applications to fully start before starting the evaluation of monitor results. Should be a non negative integer.
Use new_group_delay instead.
default: `300`
no_data_timeframe
int64
The number of minutes before a monitor notifies after data stops reporting. Datadog recommends at least 2x the monitor timeframe for query alerts or 2 minutes for service checks. If omitted, 2x the evaluation timeframe is used for query alerts, and 24 hours is used for service checks.
notification_preset_name
enum
Toggles the display of additional content sent in the monitor notification. Allowed enum values: `show_all,hide_query,hide_handles,hide_all`
default: `show_all`
notify_audit
boolean
A Boolean indicating whether tagged users is notified on changes to this monitor.
notify_by
[string]
Controls what granularity a monitor alerts on. Only available for monitors with groupings. For instance, a monitor grouped by `cluster`, `namespace`, and `pod` can be configured to only notify on each new `cluster` violating the alert conditions by setting `notify_by` to `["cluster"]`. Tags mentioned in `notify_by` must be a subset of the grouping tags in the query. For example, a query grouped by `cluster` and `namespace` cannot notify on `region`. Setting `notify_by` to `["*"]` configures the monitor to notify as a simple-alert.
notify_no_data
boolean
A Boolean indicating whether this monitor notifies when data stops reporting. Defaults to `false`.
on_missing_data
enum
Controls how groups or monitors are treated if an evaluation does not return any data points. The default option results in different behavior depending on the monitor query type. For monitors using Count queries, an empty monitor evaluation is treated as 0 and is compared to the threshold conditions. For monitors using any query type other than Count, for example Gauge, Measure, or Rate, the monitor shows the last known status. This option is only available for APM Trace Analytics, Audit Trail, CI, Error Tracking, Event, Logs, and RUM monitors. Allowed enum values: `default,show_no_data,show_and_notify_no_data,resolve`
renotify_interval
int64
The number of minutes after the last notification before a monitor re-notifies on the current status. It only re-notifies if it’s not resolved.
renotify_occurrences
int64
The number of times re-notification messages should be sent on the current status at the provided re-notification interval.
renotify_statuses
[string]
The types of monitor statuses for which re-notification messages are sent. Default: **null** if `renotify_interval` is **null**. If `renotify_interval` is set, defaults to renotify on `Alert` and `No Data`.
require_full_window
boolean
A Boolean indicating whether this monitor needs a full window of data before it’s evaluated. We highly recommend you set this to `false` for sparse metrics, otherwise some evaluations are skipped. Default is false. This setting only applies to metric monitors.
scheduling_options
object
Configuration options for scheduling.
custom_schedule
object
Configuration options for the custom schedule. **This feature is in private beta.**
recurrences
[object]
Array of custom schedule recurrences.
rrule
string
Defines the recurrence rule (RRULE) for a given schedule.
start
string
Defines the start date and time of the recurring schedule.
timezone
string
Defines the timezone the schedule runs on.
evaluation_window
object
Configuration options for the evaluation window. If `hour_starts` is set, no other fields may be set. Otherwise, `day_starts` and `month_starts` must be set together.
day_starts
string
The time of the day at which a one day cumulative evaluation window starts.
hour_starts
int32
The minute of the hour at which a one hour cumulative evaluation window starts.
month_starts
int32
The day of the month at which a one month cumulative evaluation window starts.
timezone
string
The timezone of the time of the day of the cumulative evaluation window start.
silenced
object
**DEPRECATED** : Information about the downtime applied to the monitor. Only shows v1 downtimes.
<any-key>
int64
UTC epoch timestamp in seconds when the downtime for the group expires.
synthetics_check_id
string
**DEPRECATED** : ID of the corresponding Synthetic check.
threshold_windows
object
Alerting time window options.
recovery_window
string
Describes how long an anomalous metric must be normal before the alert recovers.
trigger_window
string
Describes how long a metric must be anomalous before an alert triggers.
thresholds
object
List of the different monitor threshold available.
critical
double
The monitor `CRITICAL` threshold.
critical_recovery
double
The monitor `CRITICAL` recovery threshold.
ok
double
The monitor `OK` threshold.
unknown
double
The monitor UNKNOWN threshold.
warning
double
The monitor `WARNING` threshold.
warning_recovery
double
The monitor `WARNING` recovery threshold.
timeout_h
int64
The number of hours of the monitor not reporting data before it automatically resolves from a triggered state. The minimum allowed value is 0 hours. The maximum allowed value is 24 hours.
variables
[ <oneOf>]
List of requests that can be used in the monitor query. **This feature is currently in beta.**
Option 1
object
A formula and functions events query.
compute [_required_]
object
Compute options.
aggregation [_required_]
enum
Aggregation methods for event platform queries. Allowed enum values: `count,cardinality,median,pc75,pc90,pc95,pc98,pc99,sum,min,max,avg`
interval
int64
A time interval in milliseconds.
metric
string
Measurable attribute to compute.
data_source [_required_]
enum
Data source for event platform-based queries. Allowed enum values: `rum,ci_pipelines,ci_tests,audit,events,logs,spans,database_queries,network`
group_by
[object]
Group by options.
facet [_required_]
string
Event facet.
limit
int64
Number of groups to return.
sort
object
Options for sorting group by results.
aggregation [_required_]
enum
Aggregation methods for event platform queries. Allowed enum values: `count,cardinality,median,pc75,pc90,pc95,pc98,pc99,sum,min,max,avg`
metric
string
Metric used for sorting group by results.
order
enum
Direction of sort. Allowed enum values: `asc,desc`
default: `desc`
indexes
[string]
An array of index names to query in the stream. Omit or use `[]` to query all indexes at once.
name [_required_]
string
Name of the query for use in formulas.
search
object
Search options.
query [_required_]
string
Events search string.
Option 2
object
A formula and functions cost query.
aggregator
enum
Aggregation methods for metric queries. Allowed enum values: `avg,sum,max,min,last,area,l2norm,percentile,stddev`
data_source [_required_]
enum
Data source for cost queries. Allowed enum values: `metrics,cloud_cost,datadog_usage`
name [_required_]
string
Name of the query for use in formulas.
query [_required_]
string
The monitor query.
Option 3
object
A formula and functions data quality query.
data_source [_required_]
enum
Data source for data quality queries. Allowed enum values: `data_quality_metrics`
filter [_required_]
string
Filter expression used to match on data entities. Uses Aastra query syntax.
group_by
[string]
Optional grouping fields for aggregation.
measure [_required_]
string
The data quality measure to query. Common values include: `bytes`, `cardinality`, `custom`, `freshness`, `max`, `mean`, `min`, `nullness`, `percent_negative`, `percent_zero`, `row_count`, `stddev`, `sum`, `uniqueness`. Additional values may be supported.
monitor_options
object
Monitor configuration options for data quality queries.
crontab_override
string
Crontab expression to override the default schedule.
custom_sql
string
Custom SQL query for the monitor.
custom_where
string
Custom WHERE clause for the query.
group_by_columns
[string]
Columns to group results by.
model_type_override
enum
Override for the model type used in anomaly detection. Allowed enum values: `freshness,percentage,any`
name [_required_]
string
Name of the query for use in formulas.
schema_version
string
Schema version for the data quality query.
scope
string
Optional scoping expression to further filter metrics. Uses metrics filter syntax. This is useful when an entity has been configured to emit metrics with additional tags.
overall_state
enum
The different states your monitor can be in. Allowed enum values: `Alert,Ignored,No Data,OK,Skipped,Unknown,Warn`
priority
int64
Integer from 1 (high) to 5 (low) indicating alert severity.
query [_required_]
string
The monitor query.
restricted_roles
[string]
A list of unique role identifiers to define which roles are allowed to edit the monitor. The unique identifiers for all roles can be pulled from the [Roles API](https://docs.datadoghq.com/api/latest/roles/#list-roles) and are located in the `data.id` field. Editing a monitor includes any updates to the monitor configuration, monitor deletion, and muting of the monitor for any amount of time. You can use the [Restriction Policies API](https://docs.datadoghq.com/api/latest/restriction-policies/) to manage write authorization for individual monitors by teams and users, in addition to roles.
state
object
Wrapper object with the different monitor states.
groups
object
Dictionary where the keys are groups (comma separated lists of tags) and the values are the list of groups your monitor is broken down on.
<any-key>
object
Monitor state for a single group.
last_nodata_ts
int64
Latest timestamp the monitor was in NO_DATA state.
last_notified_ts
int64
Latest timestamp of the notification sent for this monitor group.
last_resolved_ts
int64
Latest timestamp the monitor group was resolved.
last_triggered_ts
int64
Latest timestamp the monitor group triggered.
name
string
The name of the monitor.
status
enum
The different states your monitor can be in. Allowed enum values: `Alert,Ignored,No Data,OK,Skipped,Unknown,Warn`
tags
[string]
Tags associated to your monitor.
type [_required_]
enum
The type of the monitor. For more information about `type`, see the [monitor options](https://docs.datadoghq.com/monitors/guide/monitor_api_options/) docs. Allowed enum values: `composite,event alert,log alert,metric alert,process alert,query alert,rum alert,service check,synthetics alert,trace-analytics alert,slo alert,event-v2 alert,audit alert,ci-pipelines alert,ci-tests alert,error-tracking alert,database-monitoring alert,network-performance alert,cost alert,data-quality alert`
```
{
  "assets": [
    {
      "category": "runbook",
      "name": "Monitor Runbook",
      "resource_key": "12345",
      "resource_type": "string",
      "url": "/notebooks/12345"
    }
  ],
  "created": "2019-09-19T10:00:00.000Z",
  "creator": {
    "email": "string",
    "handle": "string",
    "name": "string"
  },
  "deleted": "2019-09-19T10:00:00.000Z",
  "draft_status": "string",
  "id": "integer",
  "matching_downtimes": [
    {
      "end": 1412792983,
      "id": 1625,
      "scope": [
        "env:staging"
      ],
      "start": 1412792983
    }
  ],
  "message": "string",
  "modified": "2019-09-19T10:00:00.000Z",
  "multi": false,
  "name": "My monitor",
  "options": {
    "aggregation": {
      "group_by": "host",
      "metric": "metrics.name",
      "type": "count"
    },
    "device_ids": [],
    "enable_logs_sample": false,
    "enable_samples": false,
    "escalation_message": "string",
    "evaluation_delay": "integer",
    "group_retention_duration": "string",
    "groupby_simple_monitor": false,
    "include_tags": false,
    "locked": false,
    "min_failure_duration": "integer",
    "min_location_failed": "integer",
    "new_group_delay": "integer",
    "new_host_delay": "integer",
    "no_data_timeframe": "integer",
    "notification_preset_name": "string",
    "notify_audit": false,
    "notify_by": [],
    "notify_no_data": false,
    "on_missing_data": "string",
    "renotify_interval": "integer",
    "renotify_occurrences": "integer",
    "renotify_statuses": [],
    "require_full_window": false,
    "scheduling_options": {
      "custom_schedule": {
        "recurrences": [
          {
            "rrule": "FREQ=WEEKLY;BYDAY=MO,TU,WE,TH,FR",
            "start": "2023-08-31T16:30:00",
            "timezone": "Europe/Paris"
          }
        ]
      },
      "evaluation_window": {
        "day_starts": "04:00",
        "hour_starts": 0,
        "month_starts": 1,
        "timezone": "Europe/Paris"
      }
    },
    "silenced": {
      "<any-key>": "integer"
    },
    "synthetics_check_id": "string",
    "threshold_windows": {
      "recovery_window": "string",
      "trigger_window": "string"
    },
    "thresholds": {
      "critical": "number",
      "critical_recovery": "number",
      "ok": "number",
      "unknown": "number",
      "warning": "number",
      "warning_recovery": "number"
    },
    "timeout_h": "integer",
    "variables": [
      {
        "compute": {
          "aggregation": "avg",
          "interval": 60000,
          "metric": "@duration"
        },
        "data_source": "rum",
        "group_by": [
          {
            "facet": "status",
            "limit": 10,
            "sort": {
              "aggregation": "avg",
              "metric": "string",
              "order": "string"
            }
          }
        ],
        "indexes": [
          "days-3",
          "days-7"
        ],
        "name": "query_errors",
        "search": {
          "query": "service:query"
        }
      }
    ]
  },
  "overall_state": "string",
  "priority": "integer",
  "query": "avg(last_5m):sum:system.net.bytes_rcvd{host:host0} > 100",
  "restricted_roles": [],
  "state": {
    "groups": {
      "<any-key>": {
        "last_nodata_ts": "integer",
        "last_notified_ts": "integer",
        "last_resolved_ts": "integer",
        "last_triggered_ts": "integer",
        "name": "string",
        "status": "string"
      }
    }
  },
  "tags": [],
  "type": "query alert"
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


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
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


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
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


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
Monitor Not Found error
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


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
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/monitors/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/monitors/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/monitors/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/monitors/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/monitors/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/monitors/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/monitors/?code-lang=typescript)


#####  Edit a monitor returns "OK" response
Copy
```
                          # Path parameters  
export monitor_id="6.66486743e+08"  
# Curl command  
curl -X PUT "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/monitor/${monitor_id}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "name": "My monitor-updated",
  "priority": null,
  "options": {
    "evaluation_delay": null,
    "new_group_delay": 600,
    "new_host_delay": null,
    "renotify_interval": null,
    "thresholds": {
      "critical": 2,
      "warning": null
    },
    "timeout_h": null
  }
}
EOF  

                        
```

#####  Edit a monitor returns "OK" response
```
// Edit a monitor returns "OK" response

package main

import (
	"context"
	"encoding/json"
	"fmt"
	"os"
	"strconv"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV1"
)

func main() {
	// there is a valid "monitor" in the system
	MonitorID, _ := strconv.ParseInt(os.Getenv("MONITOR_ID"), 10, 64)

	body := datadogV1.MonitorUpdateRequest{
		Name:     datadog.PtrString("My monitor-updated"),
		Priority: *datadog.NewNullableInt64(nil),
		Options: &datadogV1.MonitorOptions{
			EvaluationDelay:  *datadog.NewNullableInt64(nil),
			NewGroupDelay:    *datadog.NewNullableInt64(datadog.PtrInt64(600)),
			NewHostDelay:     *datadog.NewNullableInt64(nil),
			RenotifyInterval: *datadog.NewNullableInt64(nil),
			Thresholds: &datadogV1.MonitorThresholds{
				Critical: datadog.PtrFloat64(2),
				Warning:  *datadog.NewNullableFloat64(nil),
			},
			TimeoutH: *datadog.NewNullableInt64(nil),
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV1.NewMonitorsApi(apiClient)
	resp, r, err := api.UpdateMonitor(ctx, MonitorID, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `MonitorsApi.UpdateMonitor`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `MonitorsApi.UpdateMonitor`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Edit a monitor returns "OK" response
```
// Edit a monitor returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.MonitorsApi;
import com.datadog.api.client.v1.model.Monitor;
import com.datadog.api.client.v1.model.MonitorOptions;
import com.datadog.api.client.v1.model.MonitorThresholds;
import com.datadog.api.client.v1.model.MonitorUpdateRequest;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    MonitorsApi apiInstance = new MonitorsApi(defaultClient);

    // there is a valid "monitor" in the system
    Long MONITOR_ID = Long.parseLong(System.getenv("MONITOR_ID"));
    String MONITOR_NAME = System.getenv("MONITOR_NAME");

    MonitorUpdateRequest body =
        new MonitorUpdateRequest()
            .name("My monitor-updated")
            .priority(null)
            .options(
                new MonitorOptions()
                    .evaluationDelay(null)
                    .newGroupDelay(600L)
                    .newHostDelay(null)
                    .renotifyInterval(null)
                    .thresholds(new MonitorThresholds().critical(2.0).warning(null))
                    .timeoutH(null));

    try {
      Monitor result = apiInstance.updateMonitor(MONITOR_ID, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MonitorsApi#updateMonitor");
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

#####  Edit a monitor returns "OK" response
```
"""
Edit a monitor returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.monitors_api import MonitorsApi
from datadog_api_client.v1.model.monitor_options import MonitorOptions
from datadog_api_client.v1.model.monitor_thresholds import MonitorThresholds
from datadog_api_client.v1.model.monitor_update_request import MonitorUpdateRequest

# there is a valid "monitor" in the system
MONITOR_ID = environ["MONITOR_ID"]
MONITOR_NAME = environ["MONITOR_NAME"]

body = MonitorUpdateRequest(
    name="My monitor-updated",
    priority=None,
    options=MonitorOptions(
        evaluation_delay=None,
        new_group_delay=600,
        new_host_delay=None,
        renotify_interval=None,
        thresholds=MonitorThresholds(
            critical=2.0,
            warning=None,
        ),
        timeout_h=None,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MonitorsApi(api_client)
    response = api_instance.update_monitor(monitor_id=int(MONITOR_ID), body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Edit a monitor returns "OK" response
```
# Edit a monitor returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::MonitorsAPI.new

# there is a valid "monitor" in the system
MONITOR_ID = ENV["MONITOR_ID"]
MONITOR_NAME = ENV["MONITOR_NAME"]

body = DatadogAPIClient::V1::MonitorUpdateRequest.new({
  name: "My monitor-updated",
  priority: nil,
  options: DatadogAPIClient::V1::MonitorOptions.new({
    evaluation_delay: nil,
    new_group_delay: 600,
    new_host_delay: nil,
    renotify_interval: nil,
    thresholds: DatadogAPIClient::V1::MonitorThresholds.new({
      critical: 2,
      warning: nil,
    }),
    timeout_h: nil,
  }),
})
p api_instance.update_monitor(MONITOR_ID.to_i, body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Edit a monitor returns "OK" response
```
// Edit a monitor returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_monitors::MonitorsAPI;
use datadog_api_client::datadogV1::model::MonitorOptions;
use datadog_api_client::datadogV1::model::MonitorThresholds;
use datadog_api_client::datadogV1::model::MonitorUpdateRequest;

#[tokio::main]
async fn main() {
    // there is a valid "monitor" in the system
    let monitor_id: i64 = std::env::var("MONITOR_ID").unwrap().parse().unwrap();
    let body = MonitorUpdateRequest::new()
        .name("My monitor-updated".to_string())
        .options(
            MonitorOptions::new()
                .evaluation_delay(None)
                .new_group_delay(Some(600))
                .new_host_delay(None)
                .renotify_interval(None)
                .thresholds(MonitorThresholds::new().critical(2.0 as f64).warning(None))
                .timeout_h(None),
        )
        .priority(None);
    let configuration = datadog::Configuration::new();
    let api = MonitorsAPI::with_config(configuration);
    let resp = api.update_monitor(monitor_id.clone(), body).await;
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

#####  Edit a monitor returns "OK" response
```
/**
 * Edit a monitor returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.MonitorsApi(configuration);

// there is a valid "monitor" in the system
const MONITOR_ID = parseInt(process.env.MONITOR_ID as string);

const params: v1.MonitorsApiUpdateMonitorRequest = {
  body: {
    name: "My monitor-updated",
    priority: undefined,
    options: {
      evaluationDelay: undefined,
      newGroupDelay: 600,
      newHostDelay: undefined,
      renotifyInterval: undefined,
      thresholds: {
        critical: 2,
        warning: undefined,
      },
      timeoutH: undefined,
    },
  },
  monitorId: MONITOR_ID,
};

apiInstance
  .updateMonitor(params)
  .then((data: v1.Monitor) => {
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
## [Unmute all monitors](https://docs.datadoghq.com/api/latest/monitors/#unmute-all-monitors)
  * [v1 (deprecated)](https://docs.datadoghq.com/api/latest/monitors/#unmute-all-monitors-v1)


POST https://api.ap1.datadoghq.com/v1/monitor/unmute_allhttps://api.ap2.datadoghq.com/v1/monitor/unmute_allhttps://api.datadoghq.eu/v1/monitor/unmute_allhttps://api.ddog-gov.com/v1/monitor/unmute_allhttps://api.datadoghq.com/v1/monitor/unmute_allhttps://api.us3.datadoghq.com/v1/monitor/unmute_allhttps://api.us5.datadoghq.com/v1/monitor/unmute_all
### Overview
Disables muting all monitors. Throws an error if mute all was not enabled previously.
### Response
  * [200](https://docs.datadoghq.com/api/latest/monitors/#UnmuteAllMonitors-200-v1)
  * [400](https://docs.datadoghq.com/api/latest/monitors/#UnmuteAllMonitors-400-v1)
  * [401](https://docs.datadoghq.com/api/latest/monitors/#UnmuteAllMonitors-401-v1)
  * [429](https://docs.datadoghq.com/api/latest/monitors/#UnmuteAllMonitors-429-v1)


OK
Bad Request
Authentication error
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


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
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/monitors/?code-lang=curl)


#####  Unmute all monitors
Copy
```
                  # Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/v1/monitor/unmute_all" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

* * *
## [Get a monitor's details](https://docs.datadoghq.com/api/latest/monitors/#get-a-monitors-details)
  * [v1 (latest)](https://docs.datadoghq.com/api/latest/monitors/#get-a-monitors-details-v1)


GET https://api.ap1.datadoghq.com/api/v1/monitor/{monitor_id}https://api.ap2.datadoghq.com/api/v1/monitor/{monitor_id}https://api.datadoghq.eu/api/v1/monitor/{monitor_id}https://api.ddog-gov.com/api/v1/monitor/{monitor_id}https://api.datadoghq.com/api/v1/monitor/{monitor_id}https://api.us3.datadoghq.com/api/v1/monitor/{monitor_id}https://api.us5.datadoghq.com/api/v1/monitor/{monitor_id}
### Overview
Get details about the specified monitor from your organization. This endpoint requires the `monitors_read` permission.
OAuth apps require the `monitors_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#monitors) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
monitor_id [_required_]
integer
The ID of the monitor
#### Query Strings
Name
Type
Description
group_states
string
When specified, shows additional information about the group states. Choose one or more from `all`, `alert`, `warn`, and `no data`.
with_downtimes
boolean
If this argument is set to true, then the returned data includes all current active downtimes for the monitor.
with_assets
boolean
If this argument is set to `true`, the returned data includes all assets tied to this monitor.
### Response
  * [200](https://docs.datadoghq.com/api/latest/monitors/#GetMonitor-200-v1)
  * [400](https://docs.datadoghq.com/api/latest/monitors/#GetMonitor-400-v1)
  * [403](https://docs.datadoghq.com/api/latest/monitors/#GetMonitor-403-v1)
  * [404](https://docs.datadoghq.com/api/latest/monitors/#GetMonitor-404-v1)
  * [429](https://docs.datadoghq.com/api/latest/monitors/#GetMonitor-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


Object describing a monitor.
Field
Type
Description
assets
[object]
The list of monitor assets tied to a monitor, which represents key links for users to take action on monitor alerts (for example, runbooks).
category [_required_]
enum
Indicates the type of asset this entity represents on a monitor. Allowed enum values: `runbook`
name [_required_]
string
Name for the monitor asset
resource_key
string
Represents the identifier of the internal Datadog resource that this asset represents. IDs in this field should be passed in as strings.
resource_type
enum
Type of internal Datadog resource associated with a monitor asset. Allowed enum values: `notebook`
url [_required_]
string
URL link for the asset. For links with an internal resource type set, this should be the relative path to where the Datadog domain is appended internally. For external links, this should be the full URL path.
created
date-time
Timestamp of the monitor creation.
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
deleted
date-time
Whether or not the monitor is deleted. (Always `null`)
draft_status
enum
Indicates whether the monitor is in a draft or published state.
`draft`: The monitor appears as Draft and does not send notifications. `published`: The monitor is active and evaluates conditions and notify as configured.
This field is in preview. The draft value is only available to customers with the feature enabled. Allowed enum values: `draft,published`
default: `published`
id
int64
ID of this monitor.
matching_downtimes
[object]
A list of active v1 downtimes that match this monitor.
end
int64
POSIX timestamp to end the downtime.
id [_required_]
int64
The downtime ID.
scope
[string]
The scope(s) to which the downtime applies. Must be in `key:value` format. For example, `host:app2`. Provide multiple scopes as a comma-separated list like `env:dev,env:prod`. The resulting downtime applies to sources that matches ALL provided scopes (`env:dev` **AND** `env:prod`).
start
int64
POSIX timestamp to start the downtime.
message
string
A message to include with notifications for this monitor.
modified
date-time
Last timestamp when the monitor was edited.
multi
boolean
Whether or not the monitor is broken down on different groups.
name
string
The monitor name.
options
object
List of options associated with your monitor.
aggregation
object
Type of aggregation performed in the monitor query.
group_by
string
Group to break down the monitor on.
metric
string
Metric name used in the monitor.
type
string
Metric type used in the monitor.
device_ids
[string]
**DEPRECATED** : IDs of the device the Synthetics monitor is running on.
enable_logs_sample
boolean
Whether or not to send a log sample when the log monitor triggers.
enable_samples
boolean
Whether or not to send a list of samples when the monitor triggers. This is only used by CI Test and Pipeline monitors.
escalation_message
string
We recommend using the [is_renotify](https://docs.datadoghq.com/monitors/notify/?tab=is_alert#renotify), block in the original message instead. A message to include with a re-notification. Supports the `@username` notification we allow elsewhere. Not applicable if `renotify_interval` is `None`.
evaluation_delay
int64
Time (in seconds) to delay evaluation, as a non-negative integer. For example, if the value is set to `300` (5min), the timeframe is set to `last_5m` and the time is 7:00, the monitor evaluates data from 6:50 to 6:55. This is useful for AWS CloudWatch and other backfilled metrics to ensure the monitor always has data during evaluation.
group_retention_duration
string
The time span after which groups with missing data are dropped from the monitor state. The minimum value is one hour, and the maximum value is 72 hours. Example values are: "60m", "1h", and "2d". This option is only available for APM Trace Analytics, Audit Trail, CI, Error Tracking, Event, Logs, and RUM monitors.
groupby_simple_monitor
boolean
**DEPRECATED** : Whether the log alert monitor triggers a single alert or multiple alerts when any group breaches a threshold. Use `notify_by` instead.
include_tags
boolean
A Boolean indicating whether notifications from this monitor automatically inserts its triggering tags into the title.
**Examples**
  * If `True`, `[Triggered on {host:h1}] Monitor Title`
  * If `False`, `[Triggered] Monitor Title`


default: `true`
locked
boolean
**DEPRECATED** : Whether or not the monitor is locked (only editable by creator and admins). Use `restricted_roles` instead.
min_failure_duration
int64
How long the test should be in failure before alerting (integer, number of seconds, max 7200).
min_location_failed
int64
The minimum number of locations in failure at the same time during at least one moment in the `min_failure_duration` period (`min_location_failed` and `min_failure_duration` are part of the advanced alerting rules - integer, >= 1).
default: `1`
new_group_delay
int64
Time (in seconds) to skip evaluations for new groups.
For example, this option can be used to skip evaluations for new hosts while they initialize.
Must be a non negative integer.
new_host_delay
int64
**DEPRECATED** : Time (in seconds) to allow a host to boot and applications to fully start before starting the evaluation of monitor results. Should be a non negative integer.
Use new_group_delay instead.
default: `300`
no_data_timeframe
int64
The number of minutes before a monitor notifies after data stops reporting. Datadog recommends at least 2x the monitor timeframe for query alerts or 2 minutes for service checks. If omitted, 2x the evaluation timeframe is used for query alerts, and 24 hours is used for service checks.
notification_preset_name
enum
Toggles the display of additional content sent in the monitor notification. Allowed enum values: `show_all,hide_query,hide_handles,hide_all`
default: `show_all`
notify_audit
boolean
A Boolean indicating whether tagged users is notified on changes to this monitor.
notify_by
[string]
Controls what granularity a monitor alerts on. Only available for monitors with groupings. For instance, a monitor grouped by `cluster`, `namespace`, and `pod` can be configured to only notify on each new `cluster` violating the alert conditions by setting `notify_by` to `["cluster"]`. Tags mentioned in `notify_by` must be a subset of the grouping tags in the query. For example, a query grouped by `cluster` and `namespace` cannot notify on `region`. Setting `notify_by` to `["*"]` configures the monitor to notify as a simple-alert.
notify_no_data
boolean
A Boolean indicating whether this monitor notifies when data stops reporting. Defaults to `false`.
on_missing_data
enum
Controls how groups or monitors are treated if an evaluation does not return any data points. The default option results in different behavior depending on the monitor query type. For monitors using Count queries, an empty monitor evaluation is treated as 0 and is compared to the threshold conditions. For monitors using any query type other than Count, for example Gauge, Measure, or Rate, the monitor shows the last known status. This option is only available for APM Trace Analytics, Audit Trail, CI, Error Tracking, Event, Logs, and RUM monitors. Allowed enum values: `default,show_no_data,show_and_notify_no_data,resolve`
renotify_interval
int64
The number of minutes after the last notification before a monitor re-notifies on the current status. It only re-notifies if it’s not resolved.
renotify_occurrences
int64
The number of times re-notification messages should be sent on the current status at the provided re-notification interval.
renotify_statuses
[string]
The types of monitor statuses for which re-notification messages are sent. Default: **null** if `renotify_interval` is **null**. If `renotify_interval` is set, defaults to renotify on `Alert` and `No Data`.
require_full_window
boolean
A Boolean indicating whether this monitor needs a full window of data before it’s evaluated. We highly recommend you set this to `false` for sparse metrics, otherwise some evaluations are skipped. Default is false. This setting only applies to metric monitors.
scheduling_options
object
Configuration options for scheduling.
custom_schedule
object
Configuration options for the custom schedule. **This feature is in private beta.**
recurrences
[object]
Array of custom schedule recurrences.
rrule
string
Defines the recurrence rule (RRULE) for a given schedule.
start
string
Defines the start date and time of the recurring schedule.
timezone
string
Defines the timezone the schedule runs on.
evaluation_window
object
Configuration options for the evaluation window. If `hour_starts` is set, no other fields may be set. Otherwise, `day_starts` and `month_starts` must be set together.
day_starts
string
The time of the day at which a one day cumulative evaluation window starts.
hour_starts
int32
The minute of the hour at which a one hour cumulative evaluation window starts.
month_starts
int32
The day of the month at which a one month cumulative evaluation window starts.
timezone
string
The timezone of the time of the day of the cumulative evaluation window start.
silenced
object
**DEPRECATED** : Information about the downtime applied to the monitor. Only shows v1 downtimes.
<any-key>
int64
UTC epoch timestamp in seconds when the downtime for the group expires.
synthetics_check_id
string
**DEPRECATED** : ID of the corresponding Synthetic check.
threshold_windows
object
Alerting time window options.
recovery_window
string
Describes how long an anomalous metric must be normal before the alert recovers.
trigger_window
string
Describes how long a metric must be anomalous before an alert triggers.
thresholds
object
List of the different monitor threshold available.
critical
double
The monitor `CRITICAL` threshold.
critical_recovery
double
The monitor `CRITICAL` recovery threshold.
ok
double
The monitor `OK` threshold.
unknown
double
The monitor UNKNOWN threshold.
warning
double
The monitor `WARNING` threshold.
warning_recovery
double
The monitor `WARNING` recovery threshold.
timeout_h
int64
The number of hours of the monitor not reporting data before it automatically resolves from a triggered state. The minimum allowed value is 0 hours. The maximum allowed value is 24 hours.
variables
[ <oneOf>]
List of requests that can be used in the monitor query. **This feature is currently in beta.**
Option 1
object
A formula and functions events query.
compute [_required_]
object
Compute options.
aggregation [_required_]
enum
Aggregation methods for event platform queries. Allowed enum values: `count,cardinality,median,pc75,pc90,pc95,pc98,pc99,sum,min,max,avg`
interval
int64
A time interval in milliseconds.
metric
string
Measurable attribute to compute.
data_source [_required_]
enum
Data source for event platform-based queries. Allowed enum values: `rum,ci_pipelines,ci_tests,audit,events,logs,spans,database_queries,network`
group_by
[object]
Group by options.
facet [_required_]
string
Event facet.
limit
int64
Number of groups to return.
sort
object
Options for sorting group by results.
aggregation [_required_]
enum
Aggregation methods for event platform queries. Allowed enum values: `count,cardinality,median,pc75,pc90,pc95,pc98,pc99,sum,min,max,avg`
metric
string
Metric used for sorting group by results.
order
enum
Direction of sort. Allowed enum values: `asc,desc`
default: `desc`
indexes
[string]
An array of index names to query in the stream. Omit or use `[]` to query all indexes at once.
name [_required_]
string
Name of the query for use in formulas.
search
object
Search options.
query [_required_]
string
Events search string.
Option 2
object
A formula and functions cost query.
aggregator
enum
Aggregation methods for metric queries. Allowed enum values: `avg,sum,max,min,last,area,l2norm,percentile,stddev`
data_source [_required_]
enum
Data source for cost queries. Allowed enum values: `metrics,cloud_cost,datadog_usage`
name [_required_]
string
Name of the query for use in formulas.
query [_required_]
string
The monitor query.
Option 3
object
A formula and functions data quality query.
data_source [_required_]
enum
Data source for data quality queries. Allowed enum values: `data_quality_metrics`
filter [_required_]
string
Filter expression used to match on data entities. Uses Aastra query syntax.
group_by
[string]
Optional grouping fields for aggregation.
measure [_required_]
string
The data quality measure to query. Common values include: `bytes`, `cardinality`, `custom`, `freshness`, `max`, `mean`, `min`, `nullness`, `percent_negative`, `percent_zero`, `row_count`, `stddev`, `sum`, `uniqueness`. Additional values may be supported.
monitor_options
object
Monitor configuration options for data quality queries.
crontab_override
string
Crontab expression to override the default schedule.
custom_sql
string
Custom SQL query for the monitor.
custom_where
string
Custom WHERE clause for the query.
group_by_columns
[string]
Columns to group results by.
model_type_override
enum
Override for the model type used in anomaly detection. Allowed enum values: `freshness,percentage,any`
name [_required_]
string
Name of the query for use in formulas.
schema_version
string
Schema version for the data quality query.
scope
string
Optional scoping expression to further filter metrics. Uses metrics filter syntax. This is useful when an entity has been configured to emit metrics with additional tags.
overall_state
enum
The different states your monitor can be in. Allowed enum values: `Alert,Ignored,No Data,OK,Skipped,Unknown,Warn`
priority
int64
Integer from 1 (high) to 5 (low) indicating alert severity.
query [_required_]
string
The monitor query.
restricted_roles
[string]
A list of unique role identifiers to define which roles are allowed to edit the monitor. The unique identifiers for all roles can be pulled from the [Roles API](https://docs.datadoghq.com/api/latest/roles/#list-roles) and are located in the `data.id` field. Editing a monitor includes any updates to the monitor configuration, monitor deletion, and muting of the monitor for any amount of time. You can use the [Restriction Policies API](https://docs.datadoghq.com/api/latest/restriction-policies/) to manage write authorization for individual monitors by teams and users, in addition to roles.
state
object
Wrapper object with the different monitor states.
groups
object
Dictionary where the keys are groups (comma separated lists of tags) and the values are the list of groups your monitor is broken down on.
<any-key>
object
Monitor state for a single group.
last_nodata_ts
int64
Latest timestamp the monitor was in NO_DATA state.
last_notified_ts
int64
Latest timestamp of the notification sent for this monitor group.
last_resolved_ts
int64
Latest timestamp the monitor group was resolved.
last_triggered_ts
int64
Latest timestamp the monitor group triggered.
name
string
The name of the monitor.
status
enum
The different states your monitor can be in. Allowed enum values: `Alert,Ignored,No Data,OK,Skipped,Unknown,Warn`
tags
[string]
Tags associated to your monitor.
type [_required_]
enum
The type of the monitor. For more information about `type`, see the [monitor options](https://docs.datadoghq.com/monitors/guide/monitor_api_options/) docs. Allowed enum values: `composite,event alert,log alert,metric alert,process alert,query alert,rum alert,service check,synthetics alert,trace-analytics alert,slo alert,event-v2 alert,audit alert,ci-pipelines alert,ci-tests alert,error-tracking alert,database-monitoring alert,network-performance alert,cost alert,data-quality alert`
```
{
  "assets": [
    {
      "category": "runbook",
      "name": "Monitor Runbook",
      "resource_key": "12345",
      "resource_type": "string",
      "url": "/notebooks/12345"
    }
  ],
  "created": "2019-09-19T10:00:00.000Z",
  "creator": {
    "email": "string",
    "handle": "string",
    "name": "string"
  },
  "deleted": "2019-09-19T10:00:00.000Z",
  "draft_status": "string",
  "id": "integer",
  "matching_downtimes": [
    {
      "end": 1412792983,
      "id": 1625,
      "scope": [
        "env:staging"
      ],
      "start": 1412792983
    }
  ],
  "message": "string",
  "modified": "2019-09-19T10:00:00.000Z",
  "multi": false,
  "name": "My monitor",
  "options": {
    "aggregation": {
      "group_by": "host",
      "metric": "metrics.name",
      "type": "count"
    },
    "device_ids": [],
    "enable_logs_sample": false,
    "enable_samples": false,
    "escalation_message": "string",
    "evaluation_delay": "integer",
    "group_retention_duration": "string",
    "groupby_simple_monitor": false,
    "include_tags": false,
    "locked": false,
    "min_failure_duration": "integer",
    "min_location_failed": "integer",
    "new_group_delay": "integer",
    "new_host_delay": "integer",
    "no_data_timeframe": "integer",
    "notification_preset_name": "string",
    "notify_audit": false,
    "notify_by": [],
    "notify_no_data": false,
    "on_missing_data": "string",
    "renotify_interval": "integer",
    "renotify_occurrences": "integer",
    "renotify_statuses": [],
    "require_full_window": false,
    "scheduling_options": {
      "custom_schedule": {
        "recurrences": [
          {
            "rrule": "FREQ=WEEKLY;BYDAY=MO,TU,WE,TH,FR",
            "start": "2023-08-31T16:30:00",
            "timezone": "Europe/Paris"
          }
        ]
      },
      "evaluation_window": {
        "day_starts": "04:00",
        "hour_starts": 0,
        "month_starts": 1,
        "timezone": "Europe/Paris"
      }
    },
    "silenced": {
      "<any-key>": "integer"
    },
    "synthetics_check_id": "string",
    "threshold_windows": {
      "recovery_window": "string",
      "trigger_window": "string"
    },
    "thresholds": {
      "critical": "number",
      "critical_recovery": "number",
      "ok": "number",
      "unknown": "number",
      "warning": "number",
      "warning_recovery": "number"
    },
    "timeout_h": "integer",
    "variables": [
      {
        "compute": {
          "aggregation": "avg",
          "interval": 60000,
          "metric": "@duration"
        },
        "data_source": "rum",
        "group_by": [
          {
            "facet": "status",
            "limit": 10,
            "sort": {
              "aggregation": "avg",
              "metric": "string",
              "order": "string"
            }
          }
        ],
        "indexes": [
          "days-3",
          "days-7"
        ],
        "name": "query_errors",
        "search": {
          "query": "service:query"
        }
      }
    ]
  },
  "overall_state": "string",
  "priority": "integer",
  "query": "avg(last_5m):sum:system.net.bytes_rcvd{host:host0} > 100",
  "restricted_roles": [],
  "state": {
    "groups": {
      "<any-key>": {
        "last_nodata_ts": "integer",
        "last_notified_ts": "integer",
        "last_resolved_ts": "integer",
        "last_triggered_ts": "integer",
        "name": "string",
        "status": "string"
      }
    }
  },
  "tags": [],
  "type": "query alert"
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


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
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


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
Monitor Not Found error
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


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
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/monitors/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/monitors/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/monitors/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/monitors/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/monitors/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/monitors/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/monitors/?code-lang=typescript)
  * [Ruby [legacy]](https://docs.datadoghq.com/api/latest/monitors/?code-lang=ruby-legacy)
  * [Python [legacy]](https://docs.datadoghq.com/api/latest/monitors/?code-lang=python-legacy)


#####  Get a monitor's details
Copy
```
                  # Path parameters  
export monitor_id="6.66486743e+08"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/monitor/${monitor_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get a monitor's details
```
"""
Get a monitor's details returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.monitors_api import MonitorsApi

# there is a valid "monitor" in the system
MONITOR_ID = environ["MONITOR_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MonitorsApi(api_client)
    response = api_instance.get_monitor(
        monitor_id=int(MONITOR_ID),
        with_downtimes=True,
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get a monitor's details
```
# Get a monitor's details returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::MonitorsAPI.new

# there is a valid "monitor" in the system
MONITOR_ID = ENV["MONITOR_ID"]
opts = {
  with_downtimes: true,
}
p api_instance.get_monitor(MONITOR_ID.to_i, opts)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get a monitor's details
```
require 'dogapi'

api_key = '<DATADOG_API_KEY>'
app_key = '<DATADOG_APPLICATION_KEY>'

dog = Dogapi::Client.new(api_key, app_key)

# Get a monitors's details
dog.get_monitor(91_879, group_states: 'all')

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby-legacy) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get a monitor's details
```
// Get a monitor's details returns "OK" response

package main

import (
	"context"
	"encoding/json"
	"fmt"
	"os"
	"strconv"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV1"
)

func main() {
	// there is a valid "monitor" in the system
	MonitorID, _ := strconv.ParseInt(os.Getenv("MONITOR_ID"), 10, 64)

	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV1.NewMonitorsApi(apiClient)
	resp, r, err := api.GetMonitor(ctx, MonitorID, *datadogV1.NewGetMonitorOptionalParameters().WithWithDowntimes(true))

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `MonitorsApi.GetMonitor`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `MonitorsApi.GetMonitor`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get a monitor's details
```
// Get a monitor's details returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.MonitorsApi;
import com.datadog.api.client.v1.api.MonitorsApi.GetMonitorOptionalParameters;
import com.datadog.api.client.v1.model.Monitor;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    MonitorsApi apiInstance = new MonitorsApi(defaultClient);

    // there is a valid "monitor" in the system
    Long MONITOR_ID = Long.parseLong(System.getenv("MONITOR_ID"));

    try {
      Monitor result =
          apiInstance.getMonitor(
              MONITOR_ID, new GetMonitorOptionalParameters().withDowntimes(true));
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MonitorsApi#getMonitor");
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

#####  Get a monitor's details
```
from datadog import initialize, api

options = {
    'api_key': '<DATADOG_API_KEY>',
    'app_key': '<DATADOG_APPLICATION_KEY>'
}

initialize(**options)

# Get a monitor's details
api.Monitor.get(2081, group_states='all')

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python-legacy) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python "example.py"


```

#####  Get a monitor's details
```
// Get a monitor's details returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_monitors::GetMonitorOptionalParams;
use datadog_api_client::datadogV1::api_monitors::MonitorsAPI;

#[tokio::main]
async fn main() {
    // there is a valid "monitor" in the system
    let monitor_id: i64 = std::env::var("MONITOR_ID").unwrap().parse().unwrap();
    let configuration = datadog::Configuration::new();
    let api = MonitorsAPI::with_config(configuration);
    let resp = api
        .get_monitor(
            monitor_id.clone(),
            GetMonitorOptionalParams::default().with_downtimes(true),
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

#####  Get a monitor's details
```
/**
 * Get a monitor's details returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.MonitorsApi(configuration);

// there is a valid "monitor" in the system
const MONITOR_ID = parseInt(process.env.MONITOR_ID as string);

const params: v1.MonitorsApiGetMonitorRequest = {
  monitorId: MONITOR_ID,
  withDowntimes: true,
};

apiInstance
  .getMonitor(params)
  .then((data: v1.Monitor) => {
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
## [Mute all monitors](https://docs.datadoghq.com/api/latest/monitors/#mute-all-monitors)
  * [v1 (deprecated)](https://docs.datadoghq.com/api/latest/monitors/#mute-all-monitors-v1)


POST https://api.ap1.datadoghq.com/v1/monitor/mute_allhttps://api.ap2.datadoghq.com/v1/monitor/mute_allhttps://api.datadoghq.eu/v1/monitor/mute_allhttps://api.ddog-gov.com/v1/monitor/mute_allhttps://api.datadoghq.com/v1/monitor/mute_allhttps://api.us3.datadoghq.com/v1/monitor/mute_allhttps://api.us5.datadoghq.com/v1/monitor/mute_all
### Overview
Muting prevents all monitors from notifying through email and posts to the [event stream](https://docs.datadoghq.com/events). State changes are only visible by checking the alert page.
### Response
  * [200](https://docs.datadoghq.com/api/latest/monitors/#MuteAllMonitors-200-v1)
  * [400](https://docs.datadoghq.com/api/latest/monitors/#MuteAllMonitors-400-v1)
  * [401](https://docs.datadoghq.com/api/latest/monitors/#MuteAllMonitors-401-v1)
  * [429](https://docs.datadoghq.com/api/latest/monitors/#MuteAllMonitors-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


Object describing a monitor.
Field
Type
Description
assets
[object]
The list of monitor assets tied to a monitor, which represents key links for users to take action on monitor alerts (for example, runbooks).
category [_required_]
enum
Indicates the type of asset this entity represents on a monitor. Allowed enum values: `runbook`
name [_required_]
string
Name for the monitor asset
resource_key
string
Represents the identifier of the internal Datadog resource that this asset represents. IDs in this field should be passed in as strings.
resource_type
enum
Type of internal Datadog resource associated with a monitor asset. Allowed enum values: `notebook`
url [_required_]
string
URL link for the asset. For links with an internal resource type set, this should be the relative path to where the Datadog domain is appended internally. For external links, this should be the full URL path.
created
date-time
Timestamp of the monitor creation.
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
deleted
date-time
Whether or not the monitor is deleted. (Always `null`)
draft_status
enum
Indicates whether the monitor is in a draft or published state.
`draft`: The monitor appears as Draft and does not send notifications. `published`: The monitor is active and evaluates conditions and notify as configured.
This field is in preview. The draft value is only available to customers with the feature enabled. Allowed enum values: `draft,published`
default: `published`
id
int64
ID of this monitor.
matching_downtimes
[object]
A list of active v1 downtimes that match this monitor.
end
int64
POSIX timestamp to end the downtime.
id [_required_]
int64
The downtime ID.
scope
[string]
The scope(s) to which the downtime applies. Must be in `key:value` format. For example, `host:app2`. Provide multiple scopes as a comma-separated list like `env:dev,env:prod`. The resulting downtime applies to sources that matches ALL provided scopes (`env:dev` **AND** `env:prod`).
start
int64
POSIX timestamp to start the downtime.
message
string
A message to include with notifications for this monitor.
modified
date-time
Last timestamp when the monitor was edited.
multi
boolean
Whether or not the monitor is broken down on different groups.
name
string
The monitor name.
options
object
List of options associated with your monitor.
aggregation
object
Type of aggregation performed in the monitor query.
group_by
string
Group to break down the monitor on.
metric
string
Metric name used in the monitor.
type
string
Metric type used in the monitor.
device_ids
[string]
**DEPRECATED** : IDs of the device the Synthetics monitor is running on.
enable_logs_sample
boolean
Whether or not to send a log sample when the log monitor triggers.
enable_samples
boolean
Whether or not to send a list of samples when the monitor triggers. This is only used by CI Test and Pipeline monitors.
escalation_message
string
We recommend using the [is_renotify](https://docs.datadoghq.com/monitors/notify/?tab=is_alert#renotify), block in the original message instead. A message to include with a re-notification. Supports the `@username` notification we allow elsewhere. Not applicable if `renotify_interval` is `None`.
evaluation_delay
int64
Time (in seconds) to delay evaluation, as a non-negative integer. For example, if the value is set to `300` (5min), the timeframe is set to `last_5m` and the time is 7:00, the monitor evaluates data from 6:50 to 6:55. This is useful for AWS CloudWatch and other backfilled metrics to ensure the monitor always has data during evaluation.
group_retention_duration
string
The time span after which groups with missing data are dropped from the monitor state. The minimum value is one hour, and the maximum value is 72 hours. Example values are: "60m", "1h", and "2d". This option is only available for APM Trace Analytics, Audit Trail, CI, Error Tracking, Event, Logs, and RUM monitors.
groupby_simple_monitor
boolean
**DEPRECATED** : Whether the log alert monitor triggers a single alert or multiple alerts when any group breaches a threshold. Use `notify_by` instead.
include_tags
boolean
A Boolean indicating whether notifications from this monitor automatically inserts its triggering tags into the title.
**Examples**
  * If `True`, `[Triggered on {host:h1}] Monitor Title`
  * If `False`, `[Triggered] Monitor Title`


default: `true`
locked
boolean
**DEPRECATED** : Whether or not the monitor is locked (only editable by creator and admins). Use `restricted_roles` instead.
min_failure_duration
int64
How long the test should be in failure before alerting (integer, number of seconds, max 7200).
min_location_failed
int64
The minimum number of locations in failure at the same time during at least one moment in the `min_failure_duration` period (`min_location_failed` and `min_failure_duration` are part of the advanced alerting rules - integer, >= 1).
default: `1`
new_group_delay
int64
Time (in seconds) to skip evaluations for new groups.
For example, this option can be used to skip evaluations for new hosts while they initialize.
Must be a non negative integer.
new_host_delay
int64
**DEPRECATED** : Time (in seconds) to allow a host to boot and applications to fully start before starting the evaluation of monitor results. Should be a non negative integer.
Use new_group_delay instead.
default: `300`
no_data_timeframe
int64
The number of minutes before a monitor notifies after data stops reporting. Datadog recommends at least 2x the monitor timeframe for query alerts or 2 minutes for service checks. If omitted, 2x the evaluation timeframe is used for query alerts, and 24 hours is used for service checks.
notification_preset_name
enum
Toggles the display of additional content sent in the monitor notification. Allowed enum values: `show_all,hide_query,hide_handles,hide_all`
default: `show_all`
notify_audit
boolean
A Boolean indicating whether tagged users is notified on changes to this monitor.
notify_by
[string]
Controls what granularity a monitor alerts on. Only available for monitors with groupings. For instance, a monitor grouped by `cluster`, `namespace`, and `pod` can be configured to only notify on each new `cluster` violating the alert conditions by setting `notify_by` to `["cluster"]`. Tags mentioned in `notify_by` must be a subset of the grouping tags in the query. For example, a query grouped by `cluster` and `namespace` cannot notify on `region`. Setting `notify_by` to `["*"]` configures the monitor to notify as a simple-alert.
notify_no_data
boolean
A Boolean indicating whether this monitor notifies when data stops reporting. Defaults to `false`.
on_missing_data
enum
Controls how groups or monitors are treated if an evaluation does not return any data points. The default option results in different behavior depending on the monitor query type. For monitors using Count queries, an empty monitor evaluation is treated as 0 and is compared to the threshold conditions. For monitors using any query type other than Count, for example Gauge, Measure, or Rate, the monitor shows the last known status. This option is only available for APM Trace Analytics, Audit Trail, CI, Error Tracking, Event, Logs, and RUM monitors. Allowed enum values: `default,show_no_data,show_and_notify_no_data,resolve`
renotify_interval
int64
The number of minutes after the last notification before a monitor re-notifies on the current status. It only re-notifies if it’s not resolved.
renotify_occurrences
int64
The number of times re-notification messages should be sent on the current status at the provided re-notification interval.
renotify_statuses
[string]
The types of monitor statuses for which re-notification messages are sent. Default: **null** if `renotify_interval` is **null**. If `renotify_interval` is set, defaults to renotify on `Alert` and `No Data`.
require_full_window
boolean
A Boolean indicating whether this monitor needs a full window of data before it’s evaluated. We highly recommend you set this to `false` for sparse metrics, otherwise some evaluations are skipped. Default is false. This setting only applies to metric monitors.
scheduling_options
object
Configuration options for scheduling.
custom_schedule
object
Configuration options for the custom schedule. **This feature is in private beta.**
recurrences
[object]
Array of custom schedule recurrences.
rrule
string
Defines the recurrence rule (RRULE) for a given schedule.
start
string
Defines the start date and time of the recurring schedule.
timezone
string
Defines the timezone the schedule runs on.
evaluation_window
object
Configuration options for the evaluation window. If `hour_starts` is set, no other fields may be set. Otherwise, `day_starts` and `month_starts` must be set together.
day_starts
string
The time of the day at which a one day cumulative evaluation window starts.
hour_starts
int32
The minute of the hour at which a one hour cumulative evaluation window starts.
month_starts
int32
The day of the month at which a one month cumulative evaluation window starts.
timezone
string
The timezone of the time of the day of the cumulative evaluation window start.
silenced
object
**DEPRECATED** : Information about the downtime applied to the monitor. Only shows v1 downtimes.
<any-key>
int64
UTC epoch timestamp in seconds when the downtime for the group expires.
synthetics_check_id
string
**DEPRECATED** : ID of the corresponding Synthetic check.
threshold_windows
object
Alerting time window options.
recovery_window
string
Describes how long an anomalous metric must be normal before the alert recovers.
trigger_window
string
Describes how long a metric must be anomalous before an alert triggers.
thresholds
object
List of the different monitor threshold available.
critical
double
The monitor `CRITICAL` threshold.
critical_recovery
double
The monitor `CRITICAL` recovery threshold.
ok
double
The monitor `OK` threshold.
unknown
double
The monitor UNKNOWN threshold.
warning
double
The monitor `WARNING` threshold.
warning_recovery
double
The monitor `WARNING` recovery threshold.
timeout_h
int64
The number of hours of the monitor not reporting data before it automatically resolves from a triggered state. The minimum allowed value is 0 hours. The maximum allowed value is 24 hours.
variables
[ <oneOf>]
List of requests that can be used in the monitor query. **This feature is currently in beta.**
Option 1
object
A formula and functions events query.
compute [_required_]
object
Compute options.
aggregation [_required_]
enum
Aggregation methods for event platform queries. Allowed enum values: `count,cardinality,median,pc75,pc90,pc95,pc98,pc99,sum,min,max,avg`
interval
int64
A time interval in milliseconds.
metric
string
Measurable attribute to compute.
data_source [_required_]
enum
Data source for event platform-based queries. Allowed enum values: `rum,ci_pipelines,ci_tests,audit,events,logs,spans,database_queries,network`
group_by
[object]
Group by options.
facet [_required_]
string
Event facet.
limit
int64
Number of groups to return.
sort
object
Options for sorting group by results.
aggregation [_required_]
enum
Aggregation methods for event platform queries. Allowed enum values: `count,cardinality,median,pc75,pc90,pc95,pc98,pc99,sum,min,max,avg`
metric
string
Metric used for sorting group by results.
order
enum
Direction of sort. Allowed enum values: `asc,desc`
default: `desc`
indexes
[string]
An array of index names to query in the stream. Omit or use `[]` to query all indexes at once.
name [_required_]
string
Name of the query for use in formulas.
search
object
Search options.
query [_required_]
string
Events search string.
Option 2
object
A formula and functions cost query.
aggregator
enum
Aggregation methods for metric queries. Allowed enum values: `avg,sum,max,min,last,area,l2norm,percentile,stddev`
data_source [_required_]
enum
Data source for cost queries. Allowed enum values: `metrics,cloud_cost,datadog_usage`
name [_required_]
string
Name of the query for use in formulas.
query [_required_]
string
The monitor query.
Option 3
object
A formula and functions data quality query.
data_source [_required_]
enum
Data source for data quality queries. Allowed enum values: `data_quality_metrics`
filter [_required_]
string
Filter expression used to match on data entities. Uses Aastra query syntax.
group_by
[string]
Optional grouping fields for aggregation.
measure [_required_]
string
The data quality measure to query. Common values include: `bytes`, `cardinality`, `custom`, `freshness`, `max`, `mean`, `min`, `nullness`, `percent_negative`, `percent_zero`, `row_count`, `stddev`, `sum`, `uniqueness`. Additional values may be supported.
monitor_options
object
Monitor configuration options for data quality queries.
crontab_override
string
Crontab expression to override the default schedule.
custom_sql
string
Custom SQL query for the monitor.
custom_where
string
Custom WHERE clause for the query.
group_by_columns
[string]
Columns to group results by.
model_type_override
enum
Override for the model type used in anomaly detection. Allowed enum values: `freshness,percentage,any`
name [_required_]
string
Name of the query for use in formulas.
schema_version
string
Schema version for the data quality query.
scope
string
Optional scoping expression to further filter metrics. Uses metrics filter syntax. This is useful when an entity has been configured to emit metrics with additional tags.
overall_state
enum
The different states your monitor can be in. Allowed enum values: `Alert,Ignored,No Data,OK,Skipped,Unknown,Warn`
priority
int64
Integer from 1 (high) to 5 (low) indicating alert severity.
query [_required_]
string
The monitor query.
restricted_roles
[string]
A list of unique role identifiers to define which roles are allowed to edit the monitor. The unique identifiers for all roles can be pulled from the [Roles API](https://docs.datadoghq.com/api/latest/roles/#list-roles) and are located in the `data.id` field. Editing a monitor includes any updates to the monitor configuration, monitor deletion, and muting of the monitor for any amount of time. You can use the [Restriction Policies API](https://docs.datadoghq.com/api/latest/restriction-policies/) to manage write authorization for individual monitors by teams and users, in addition to roles.
state
object
Wrapper object with the different monitor states.
groups
object
Dictionary where the keys are groups (comma separated lists of tags) and the values are the list of groups your monitor is broken down on.
<any-key>
object
Monitor state for a single group.
last_nodata_ts
int64
Latest timestamp the monitor was in NO_DATA state.
last_notified_ts
int64
Latest timestamp of the notification sent for this monitor group.
last_resolved_ts
int64
Latest timestamp the monitor group was resolved.
last_triggered_ts
int64
Latest timestamp the monitor group triggered.
name
string
The name of the monitor.
status
enum
The different states your monitor can be in. Allowed enum values: `Alert,Ignored,No Data,OK,Skipped,Unknown,Warn`
tags
[string]
Tags associated to your monitor.
type [_required_]
enum
The type of the monitor. For more information about `type`, see the [monitor options](https://docs.datadoghq.com/monitors/guide/monitor_api_options/) docs. Allowed enum values: `composite,event alert,log alert,metric alert,process alert,query alert,rum alert,service check,synthetics alert,trace-analytics alert,slo alert,event-v2 alert,audit alert,ci-pipelines alert,ci-tests alert,error-tracking alert,database-monitoring alert,network-performance alert,cost alert,data-quality alert`
```
{
  "assets": [
    {
      "category": "runbook",
      "name": "Monitor Runbook",
      "resource_key": "12345",
      "resource_type": "string",
      "url": "/notebooks/12345"
    }
  ],
  "created": "2019-09-19T10:00:00.000Z",
  "creator": {
    "email": "string",
    "handle": "string",
    "name": "string"
  },
  "deleted": "2019-09-19T10:00:00.000Z",
  "draft_status": "string",
  "id": "integer",
  "matching_downtimes": [
    {
      "end": 1412792983,
      "id": 1625,
      "scope": [
        "env:staging"
      ],
      "start": 1412792983
    }
  ],
  "message": "string",
  "modified": "2019-09-19T10:00:00.000Z",
  "multi": false,
  "name": "My monitor",
  "options": {
    "aggregation": {
      "group_by": "host",
      "metric": "metrics.name",
      "type": "count"
    },
    "device_ids": [],
    "enable_logs_sample": false,
    "enable_samples": false,
    "escalation_message": "string",
    "evaluation_delay": "integer",
    "group_retention_duration": "string",
    "groupby_simple_monitor": false,
    "include_tags": false,
    "locked": false,
    "min_failure_duration": "integer",
    "min_location_failed": "integer",
    "new_group_delay": "integer",
    "new_host_delay": "integer",
    "no_data_timeframe": "integer",
    "notification_preset_name": "string",
    "notify_audit": false,
    "notify_by": [],
    "notify_no_data": false,
    "on_missing_data": "string",
    "renotify_interval": "integer",
    "renotify_occurrences": "integer",
    "renotify_statuses": [],
    "require_full_window": false,
    "scheduling_options": {
      "custom_schedule": {
        "recurrences": [
          {
            "rrule": "FREQ=WEEKLY;BYDAY=MO,TU,WE,TH,FR",
            "start": "2023-08-31T16:30:00",
            "timezone": "Europe/Paris"
          }
        ]
      },
      "evaluation_window": {
        "day_starts": "04:00",
        "hour_starts": 0,
        "month_starts": 1,
        "timezone": "Europe/Paris"
      }
    },
    "silenced": {
      "<any-key>": "integer"
    },
    "synthetics_check_id": "string",
    "threshold_windows": {
      "recovery_window": "string",
      "trigger_window": "string"
    },
    "thresholds": {
      "critical": "number",
      "critical_recovery": "number",
      "ok": "number",
      "unknown": "number",
      "warning": "number",
      "warning_recovery": "number"
    },
    "timeout_h": "integer",
    "variables": [
      {
        "compute": {
          "aggregation": "avg",
          "interval": 60000,
          "metric": "@duration"
        },
        "data_source": "rum",
        "group_by": [
          {
            "facet": "status",
            "limit": 10,
            "sort": {
              "aggregation": "avg",
              "metric": "string",
              "order": "string"
            }
          }
        ],
        "indexes": [
          "days-3",
          "days-7"
        ],
        "name": "query_errors",
        "search": {
          "query": "service:query"
        }
      }
    ]
  },
  "overall_state": "string",
  "priority": "integer",
  "query": "avg(last_5m):sum:system.net.bytes_rcvd{host:host0} > 100",
  "restricted_roles": [],
  "state": {
    "groups": {
      "<any-key>": {
        "last_nodata_ts": "integer",
        "last_notified_ts": "integer",
        "last_resolved_ts": "integer",
        "last_triggered_ts": "integer",
        "name": "string",
        "status": "string"
      }
    }
  },
  "tags": [],
  "type": "query alert"
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


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
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


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
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/monitors/?code-lang=curl)


#####  Mute all monitors
Copy
```
                  # Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/v1/monitor/mute_all" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

* * *
## [Delete a monitor](https://docs.datadoghq.com/api/latest/monitors/#delete-a-monitor)
  * [v1 (latest)](https://docs.datadoghq.com/api/latest/monitors/#delete-a-monitor-v1)


DELETE https://api.ap1.datadoghq.com/api/v1/monitor/{monitor_id}https://api.ap2.datadoghq.com/api/v1/monitor/{monitor_id}https://api.datadoghq.eu/api/v1/monitor/{monitor_id}https://api.ddog-gov.com/api/v1/monitor/{monitor_id}https://api.datadoghq.com/api/v1/monitor/{monitor_id}https://api.us3.datadoghq.com/api/v1/monitor/{monitor_id}https://api.us5.datadoghq.com/api/v1/monitor/{monitor_id}
### Overview
Delete the specified monitor This endpoint requires the `monitors_write` permission.
OAuth apps require the `monitors_write` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#monitors) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
monitor_id [_required_]
integer
The ID of the monitor.
#### Query Strings
Name
Type
Description
force
string
Delete the monitor even if it’s referenced by other resources (for example SLO, composite monitor).
### Response
  * [200](https://docs.datadoghq.com/api/latest/monitors/#DeleteMonitor-200-v1)
  * [400](https://docs.datadoghq.com/api/latest/monitors/#DeleteMonitor-400-v1)
  * [401](https://docs.datadoghq.com/api/latest/monitors/#DeleteMonitor-401-v1)
  * [403](https://docs.datadoghq.com/api/latest/monitors/#DeleteMonitor-403-v1)
  * [404](https://docs.datadoghq.com/api/latest/monitors/#DeleteMonitor-404-v1)
  * [429](https://docs.datadoghq.com/api/latest/monitors/#DeleteMonitor-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


Response from the delete monitor call.
Expand All
Field
Type
Description
deleted_monitor_id
int64
ID of the deleted monitor.
```
{
  "deleted_monitor_id": 666486743
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


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
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


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
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


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
Item not found error
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


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
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/monitors/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/monitors/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/monitors/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/monitors/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/monitors/?code-lang=typescript)
  * [Go](https://docs.datadoghq.com/api/latest/monitors/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/monitors/?code-lang=java)
  * [Ruby [legacy]](https://docs.datadoghq.com/api/latest/monitors/?code-lang=ruby-legacy)
  * [Python [legacy]](https://docs.datadoghq.com/api/latest/monitors/?code-lang=python-legacy)


#####  Delete a monitor
Copy
```
                  # Path parameters  
export monitor_id="6.66486743e+08"  
# Curl command  
curl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/monitor/${monitor_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Delete a monitor
```
"""
Delete a monitor returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.monitors_api import MonitorsApi

# there is a valid "monitor" in the system
MONITOR_ID = environ["MONITOR_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MonitorsApi(api_client)
    response = api_instance.delete_monitor(
        monitor_id=int(MONITOR_ID),
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Delete a monitor
```
# Delete a monitor returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::MonitorsAPI.new

# there is a valid "monitor" in the system
MONITOR_ID = ENV["MONITOR_ID"]
p api_instance.delete_monitor(MONITOR_ID.to_i)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Delete a monitor
```
require 'dogapi'

api_key = '<DATADOG_API_KEY>'
app_key = '<DATADOG_APPLICATION_KEY>'

dog = Dogapi::Client.new(api_key, app_key)

# Delete a monitor
dog.delete_monitor(62_625)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby-legacy) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Delete a monitor
```
// Delete a monitor returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_monitors::DeleteMonitorOptionalParams;
use datadog_api_client::datadogV1::api_monitors::MonitorsAPI;

#[tokio::main]
async fn main() {
    // there is a valid "monitor" in the system
    let monitor_id: i64 = std::env::var("MONITOR_ID").unwrap().parse().unwrap();
    let configuration = datadog::Configuration::new();
    let api = MonitorsAPI::with_config(configuration);
    let resp = api
        .delete_monitor(monitor_id.clone(), DeleteMonitorOptionalParams::default())
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

#####  Delete a monitor
```
/**
 * Delete a monitor returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.MonitorsApi(configuration);

// there is a valid "monitor" in the system
const MONITOR_ID = parseInt(process.env.MONITOR_ID as string);

const params: v1.MonitorsApiDeleteMonitorRequest = {
  monitorId: MONITOR_ID,
};

apiInstance
  .deleteMonitor(params)
  .then((data: v1.DeletedMonitor) => {
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

#####  Delete a monitor
```
// Delete a monitor returns "OK" response

package main

import (
	"context"
	"encoding/json"
	"fmt"
	"os"
	"strconv"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV1"
)

func main() {
	// there is a valid "monitor" in the system
	MonitorID, _ := strconv.ParseInt(os.Getenv("MONITOR_ID"), 10, 64)

	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV1.NewMonitorsApi(apiClient)
	resp, r, err := api.DeleteMonitor(ctx, MonitorID, *datadogV1.NewDeleteMonitorOptionalParameters())

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `MonitorsApi.DeleteMonitor`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `MonitorsApi.DeleteMonitor`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Delete a monitor
```
// Delete a monitor returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.MonitorsApi;
import com.datadog.api.client.v1.model.DeletedMonitor;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    MonitorsApi apiInstance = new MonitorsApi(defaultClient);

    // there is a valid "monitor" in the system
    Long MONITOR_ID = Long.parseLong(System.getenv("MONITOR_ID"));

    try {
      DeletedMonitor result = apiInstance.deleteMonitor(MONITOR_ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MonitorsApi#deleteMonitor");
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

#####  Delete a monitor
```
from datadog import initialize, api

options = {
    'api_key': '<DATADOG_API_KEY>',
    'app_key': '<DATADOG_APPLICATION_KEY>'
}

initialize(**options)

# Delete a monitor
api.Monitor.delete(2081)

# Force delete a monitor to override warnings
api.Monitor.delete(2081, force=True)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python-legacy) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python "example.py"


```

* * *
## [Check if a monitor can be deleted](https://docs.datadoghq.com/api/latest/monitors/#check-if-a-monitor-can-be-deleted)
  * [v1 (latest)](https://docs.datadoghq.com/api/latest/monitors/#check-if-a-monitor-can-be-deleted-v1)


GET https://api.ap1.datadoghq.com/api/v1/monitor/can_deletehttps://api.ap2.datadoghq.com/api/v1/monitor/can_deletehttps://api.datadoghq.eu/api/v1/monitor/can_deletehttps://api.ddog-gov.com/api/v1/monitor/can_deletehttps://api.datadoghq.com/api/v1/monitor/can_deletehttps://api.us3.datadoghq.com/api/v1/monitor/can_deletehttps://api.us5.datadoghq.com/api/v1/monitor/can_delete
### Overview
Check if the given monitors can be deleted. This endpoint requires the `monitors_read` permission.
OAuth apps require the `monitors_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#monitors) to access this endpoint.
### Arguments
#### Query Strings
Name
Type
Description
monitor_ids [_required_]
array
The IDs of the monitor to check.
### Response
  * [200](https://docs.datadoghq.com/api/latest/monitors/#CheckCanDeleteMonitor-200-v1)
  * [400](https://docs.datadoghq.com/api/latest/monitors/#CheckCanDeleteMonitor-400-v1)
  * [403](https://docs.datadoghq.com/api/latest/monitors/#CheckCanDeleteMonitor-403-v1)
  * [409](https://docs.datadoghq.com/api/latest/monitors/#CheckCanDeleteMonitor-409-v1)
  * [429](https://docs.datadoghq.com/api/latest/monitors/#CheckCanDeleteMonitor-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


Response of monitor IDs that can or can’t be safely deleted.
Field
Type
Description
data [_required_]
object
Wrapper object with the list of monitor IDs.
ok
[integer]
An array of Monitor IDs that can be safely deleted.
errors
object
A mapping of Monitor ID to strings denoting where it's used.
<any-key>
[string]
Strings denoting where a monitor is used.
```
{
  "data": {
    "ok": []
  },
  "errors": {
    "<any-key>": []
  }
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


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
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


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
Deletion conflict error
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


Response of monitor IDs that can or can’t be safely deleted.
Field
Type
Description
data [_required_]
object
Wrapper object with the list of monitor IDs.
ok
[integer]
An array of Monitor IDs that can be safely deleted.
errors
object
A mapping of Monitor ID to strings denoting where it's used.
<any-key>
[string]
Strings denoting where a monitor is used.
```
{
  "data": {
    "ok": []
  },
  "errors": {
    "<any-key>": []
  }
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/monitors/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/monitors/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/monitors/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/monitors/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/monitors/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/monitors/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/monitors/?code-lang=typescript)
  * [Ruby [legacy]](https://docs.datadoghq.com/api/latest/monitors/?code-lang=ruby-legacy)
  * [Python [legacy]](https://docs.datadoghq.com/api/latest/monitors/?code-lang=python-legacy)


#####  Check if a monitor can be deleted
Copy
```
                  # Required query arguments  
export monitor_ids="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/monitor/can_delete?monitor_ids=${monitor_ids}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Check if a monitor can be deleted
```
"""
Check if a monitor can be deleted returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.monitors_api import MonitorsApi

# there is a valid "monitor" in the system
MONITOR_ID = environ["MONITOR_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MonitorsApi(api_client)
    response = api_instance.check_can_delete_monitor(
        monitor_ids=[
            int(MONITOR_ID),
        ],
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Check if a monitor can be deleted
```
# Check if a monitor can be deleted returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::MonitorsAPI.new

# there is a valid "monitor" in the system
MONITOR_ID = ENV["MONITOR_ID"]
p api_instance.check_can_delete_monitor([
  MONITOR_ID.to_i,
])

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Check if a monitor can be deleted
```
require 'rubygems'
require 'dogapi'

api_key = '<DATADOG_API_KEY>'
app_key = '<DATADOG_APPLICATION_KEY>'

dog = Dogapi::Client.new(api_key, app_key)

# Check if you can delete the given monitors.
dog.can_delete_monitors([56838, 771060, 1000376])

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby-legacy) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Check if a monitor can be deleted
```
// Check if a monitor can be deleted returns "OK" response

package main

import (
	"context"
	"encoding/json"
	"fmt"
	"os"
	"strconv"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV1"
)

func main() {
	// there is a valid "monitor" in the system
	MonitorID, _ := strconv.ParseInt(os.Getenv("MONITOR_ID"), 10, 64)

	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV1.NewMonitorsApi(apiClient)
	resp, r, err := api.CheckCanDeleteMonitor(ctx, []int64{
		MonitorID,
	})

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `MonitorsApi.CheckCanDeleteMonitor`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `MonitorsApi.CheckCanDeleteMonitor`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Check if a monitor can be deleted
```
// Check if a monitor can be deleted returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.MonitorsApi;
import com.datadog.api.client.v1.model.CheckCanDeleteMonitorResponse;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    MonitorsApi apiInstance = new MonitorsApi(defaultClient);

    // there is a valid "monitor" in the system
    Long MONITOR_ID = Long.parseLong(System.getenv("MONITOR_ID"));

    try {
      CheckCanDeleteMonitorResponse result =
          apiInstance.checkCanDeleteMonitor(Collections.singletonList(MONITOR_ID));
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MonitorsApi#checkCanDeleteMonitor");
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

#####  Check if a monitor can be deleted
```
from datadog import initialize, api

options = {
    'api_key': '<DATADOG_API_KEY>',
    'app_key': '<DATADOG_APPLICATION_KEY>'
}

initialize(**options)

# Check if you can delete the given monitors.
api.Monitor.can_delete(monitor_ids=[56838, 771060, 1000376])

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python-legacy) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python "example.py"


```

#####  Check if a monitor can be deleted
```
// Check if a monitor can be deleted returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_monitors::MonitorsAPI;

#[tokio::main]
async fn main() {
    // there is a valid "monitor" in the system
    let monitor_id: i64 = std::env::var("MONITOR_ID").unwrap().parse().unwrap();
    let configuration = datadog::Configuration::new();
    let api = MonitorsAPI::with_config(configuration);
    let resp = api.check_can_delete_monitor(vec![monitor_id.clone()]).await;
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

#####  Check if a monitor can be deleted
```
/**
 * Check if a monitor can be deleted returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.MonitorsApi(configuration);

// there is a valid "monitor" in the system
const MONITOR_ID = parseInt(process.env.MONITOR_ID as string);

const params: v1.MonitorsApiCheckCanDeleteMonitorRequest = {
  monitorIds: [MONITOR_ID],
};

apiInstance
  .checkCanDeleteMonitor(params)
  .then((data: v1.CheckCanDeleteMonitorResponse) => {
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
## [Validate a monitor](https://docs.datadoghq.com/api/latest/monitors/#validate-a-monitor)
  * [v1 (latest)](https://docs.datadoghq.com/api/latest/monitors/#validate-a-monitor-v1)


POST https://api.ap1.datadoghq.com/api/v1/monitor/validatehttps://api.ap2.datadoghq.com/api/v1/monitor/validatehttps://api.datadoghq.eu/api/v1/monitor/validatehttps://api.ddog-gov.com/api/v1/monitor/validatehttps://api.datadoghq.com/api/v1/monitor/validatehttps://api.us3.datadoghq.com/api/v1/monitor/validatehttps://api.us5.datadoghq.com/api/v1/monitor/validate
### Overview
Validate the monitor provided in the request.
**Note** : Log monitors require an unscoped App Key.
This endpoint requires the `monitors_read` permission.
OAuth apps require the `monitors_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#monitors) to access this endpoint.
### Request
#### Body Data (required)
Monitor request object
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


Field
Type
Description
assets
[object]
The list of monitor assets tied to a monitor, which represents key links for users to take action on monitor alerts (for example, runbooks).
category [_required_]
enum
Indicates the type of asset this entity represents on a monitor. Allowed enum values: `runbook`
name [_required_]
string
Name for the monitor asset
resource_key
string
Represents the identifier of the internal Datadog resource that this asset represents. IDs in this field should be passed in as strings.
resource_type
enum
Type of internal Datadog resource associated with a monitor asset. Allowed enum values: `notebook`
url [_required_]
string
URL link for the asset. For links with an internal resource type set, this should be the relative path to where the Datadog domain is appended internally. For external links, this should be the full URL path.
created
date-time
Timestamp of the monitor creation.
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
deleted
date-time
Whether or not the monitor is deleted. (Always `null`)
draft_status
enum
Indicates whether the monitor is in a draft or published state.
`draft`: The monitor appears as Draft and does not send notifications. `published`: The monitor is active and evaluates conditions and notify as configured.
This field is in preview. The draft value is only available to customers with the feature enabled. Allowed enum values: `draft,published`
default: `published`
id
int64
ID of this monitor.
matching_downtimes
[object]
A list of active v1 downtimes that match this monitor.
end
int64
POSIX timestamp to end the downtime.
id [_required_]
int64
The downtime ID.
scope
[string]
The scope(s) to which the downtime applies. Must be in `key:value` format. For example, `host:app2`. Provide multiple scopes as a comma-separated list like `env:dev,env:prod`. The resulting downtime applies to sources that matches ALL provided scopes (`env:dev` **AND** `env:prod`).
start
int64
POSIX timestamp to start the downtime.
message
string
A message to include with notifications for this monitor.
modified
date-time
Last timestamp when the monitor was edited.
multi
boolean
Whether or not the monitor is broken down on different groups.
name
string
The monitor name.
options
object
List of options associated with your monitor.
aggregation
object
Type of aggregation performed in the monitor query.
group_by
string
Group to break down the monitor on.
metric
string
Metric name used in the monitor.
type
string
Metric type used in the monitor.
device_ids
[string]
**DEPRECATED** : IDs of the device the Synthetics monitor is running on.
enable_logs_sample
boolean
Whether or not to send a log sample when the log monitor triggers.
enable_samples
boolean
Whether or not to send a list of samples when the monitor triggers. This is only used by CI Test and Pipeline monitors.
escalation_message
string
We recommend using the [is_renotify](https://docs.datadoghq.com/monitors/notify/?tab=is_alert#renotify), block in the original message instead. A message to include with a re-notification. Supports the `@username` notification we allow elsewhere. Not applicable if `renotify_interval` is `None`.
evaluation_delay
int64
Time (in seconds) to delay evaluation, as a non-negative integer. For example, if the value is set to `300` (5min), the timeframe is set to `last_5m` and the time is 7:00, the monitor evaluates data from 6:50 to 6:55. This is useful for AWS CloudWatch and other backfilled metrics to ensure the monitor always has data during evaluation.
group_retention_duration
string
The time span after which groups with missing data are dropped from the monitor state. The minimum value is one hour, and the maximum value is 72 hours. Example values are: "60m", "1h", and "2d". This option is only available for APM Trace Analytics, Audit Trail, CI, Error Tracking, Event, Logs, and RUM monitors.
groupby_simple_monitor
boolean
**DEPRECATED** : Whether the log alert monitor triggers a single alert or multiple alerts when any group breaches a threshold. Use `notify_by` instead.
include_tags
boolean
A Boolean indicating whether notifications from this monitor automatically inserts its triggering tags into the title.
**Examples**
  * If `True`, `[Triggered on {host:h1}] Monitor Title`
  * If `False`, `[Triggered] Monitor Title`


default: `true`
locked
boolean
**DEPRECATED** : Whether or not the monitor is locked (only editable by creator and admins). Use `restricted_roles` instead.
min_failure_duration
int64
How long the test should be in failure before alerting (integer, number of seconds, max 7200).
min_location_failed
int64
The minimum number of locations in failure at the same time during at least one moment in the `min_failure_duration` period (`min_location_failed` and `min_failure_duration` are part of the advanced alerting rules - integer, >= 1).
default: `1`
new_group_delay
int64
Time (in seconds) to skip evaluations for new groups.
For example, this option can be used to skip evaluations for new hosts while they initialize.
Must be a non negative integer.
new_host_delay
int64
**DEPRECATED** : Time (in seconds) to allow a host to boot and applications to fully start before starting the evaluation of monitor results. Should be a non negative integer.
Use new_group_delay instead.
default: `300`
no_data_timeframe
int64
The number of minutes before a monitor notifies after data stops reporting. Datadog recommends at least 2x the monitor timeframe for query alerts or 2 minutes for service checks. If omitted, 2x the evaluation timeframe is used for query alerts, and 24 hours is used for service checks.
notification_preset_name
enum
Toggles the display of additional content sent in the monitor notification. Allowed enum values: `show_all,hide_query,hide_handles,hide_all`
default: `show_all`
notify_audit
boolean
A Boolean indicating whether tagged users is notified on changes to this monitor.
notify_by
[string]
Controls what granularity a monitor alerts on. Only available for monitors with groupings. For instance, a monitor grouped by `cluster`, `namespace`, and `pod` can be configured to only notify on each new `cluster` violating the alert conditions by setting `notify_by` to `["cluster"]`. Tags mentioned in `notify_by` must be a subset of the grouping tags in the query. For example, a query grouped by `cluster` and `namespace` cannot notify on `region`. Setting `notify_by` to `["*"]` configures the monitor to notify as a simple-alert.
notify_no_data
boolean
A Boolean indicating whether this monitor notifies when data stops reporting. Defaults to `false`.
on_missing_data
enum
Controls how groups or monitors are treated if an evaluation does not return any data points. The default option results in different behavior depending on the monitor query type. For monitors using Count queries, an empty monitor evaluation is treated as 0 and is compared to the threshold conditions. For monitors using any query type other than Count, for example Gauge, Measure, or Rate, the monitor shows the last known status. This option is only available for APM Trace Analytics, Audit Trail, CI, Error Tracking, Event, Logs, and RUM monitors. Allowed enum values: `default,show_no_data,show_and_notify_no_data,resolve`
renotify_interval
int64
The number of minutes after the last notification before a monitor re-notifies on the current status. It only re-notifies if it’s not resolved.
renotify_occurrences
int64
The number of times re-notification messages should be sent on the current status at the provided re-notification interval.
renotify_statuses
[string]
The types of monitor statuses for which re-notification messages are sent. Default: **null** if `renotify_interval` is **null**. If `renotify_interval` is set, defaults to renotify on `Alert` and `No Data`.
require_full_window
boolean
A Boolean indicating whether this monitor needs a full window of data before it’s evaluated. We highly recommend you set this to `false` for sparse metrics, otherwise some evaluations are skipped. Default is false. This setting only applies to metric monitors.
scheduling_options
object
Configuration options for scheduling.
custom_schedule
object
Configuration options for the custom schedule. **This feature is in private beta.**
recurrences
[object]
Array of custom schedule recurrences.
rrule
string
Defines the recurrence rule (RRULE) for a given schedule.
start
string
Defines the start date and time of the recurring schedule.
timezone
string
Defines the timezone the schedule runs on.
evaluation_window
object
Configuration options for the evaluation window. If `hour_starts` is set, no other fields may be set. Otherwise, `day_starts` and `month_starts` must be set together.
day_starts
string
The time of the day at which a one day cumulative evaluation window starts.
hour_starts
int32
The minute of the hour at which a one hour cumulative evaluation window starts.
month_starts
int32
The day of the month at which a one month cumulative evaluation window starts.
timezone
string
The timezone of the time of the day of the cumulative evaluation window start.
silenced
object
**DEPRECATED** : Information about the downtime applied to the monitor. Only shows v1 downtimes.
<any-key>
int64
UTC epoch timestamp in seconds when the downtime for the group expires.
synthetics_check_id
string
**DEPRECATED** : ID of the corresponding Synthetic check.
threshold_windows
object
Alerting time window options.
recovery_window
string
Describes how long an anomalous metric must be normal before the alert recovers.
trigger_window
string
Describes how long a metric must be anomalous before an alert triggers.
thresholds
object
List of the different monitor threshold available.
critical
double
The monitor `CRITICAL` threshold.
critical_recovery
double
The monitor `CRITICAL` recovery threshold.
ok
double
The monitor `OK` threshold.
unknown
double
The monitor UNKNOWN threshold.
warning
double
The monitor `WARNING` threshold.
warning_recovery
double
The monitor `WARNING` recovery threshold.
timeout_h
int64
The number of hours of the monitor not reporting data before it automatically resolves from a triggered state. The minimum allowed value is 0 hours. The maximum allowed value is 24 hours.
variables
[ <oneOf>]
List of requests that can be used in the monitor query. **This feature is currently in beta.**
Option 1
object
A formula and functions events query.
compute [_required_]
object
Compute options.
aggregation [_required_]
enum
Aggregation methods for event platform queries. Allowed enum values: `count,cardinality,median,pc75,pc90,pc95,pc98,pc99,sum,min,max,avg`
interval
int64
A time interval in milliseconds.
metric
string
Measurable attribute to compute.
data_source [_required_]
enum
Data source for event platform-based queries. Allowed enum values: `rum,ci_pipelines,ci_tests,audit,events,logs,spans,database_queries,network`
group_by
[object]
Group by options.
facet [_required_]
string
Event facet.
limit
int64
Number of groups to return.
sort
object
Options for sorting group by results.
aggregation [_required_]
enum
Aggregation methods for event platform queries. Allowed enum values: `count,cardinality,median,pc75,pc90,pc95,pc98,pc99,sum,min,max,avg`
metric
string
Metric used for sorting group by results.
order
enum
Direction of sort. Allowed enum values: `asc,desc`
default: `desc`
indexes
[string]
An array of index names to query in the stream. Omit or use `[]` to query all indexes at once.
name [_required_]
string
Name of the query for use in formulas.
search
object
Search options.
query [_required_]
string
Events search string.
Option 2
object
A formula and functions cost query.
aggregator
enum
Aggregation methods for metric queries. Allowed enum values: `avg,sum,max,min,last,area,l2norm,percentile,stddev`
data_source [_required_]
enum
Data source for cost queries. Allowed enum values: `metrics,cloud_cost,datadog_usage`
name [_required_]
string
Name of the query for use in formulas.
query [_required_]
string
The monitor query.
Option 3
object
A formula and functions data quality query.
data_source [_required_]
enum
Data source for data quality queries. Allowed enum values: `data_quality_metrics`
filter [_required_]
string
Filter expression used to match on data entities. Uses Aastra query syntax.
group_by
[string]
Optional grouping fields for aggregation.
measure [_required_]
string
The data quality measure to query. Common values include: `bytes`, `cardinality`, `custom`, `freshness`, `max`, `mean`, `min`, `nullness`, `percent_negative`, `percent_zero`, `row_count`, `stddev`, `sum`, `uniqueness`. Additional values may be supported.
monitor_options
object
Monitor configuration options for data quality queries.
crontab_override
string
Crontab expression to override the default schedule.
custom_sql
string
Custom SQL query for the monitor.
custom_where
string
Custom WHERE clause for the query.
group_by_columns
[string]
Columns to group results by.
model_type_override
enum
Override for the model type used in anomaly detection. Allowed enum values: `freshness,percentage,any`
name [_required_]
string
Name of the query for use in formulas.
schema_version
string
Schema version for the data quality query.
scope
string
Optional scoping expression to further filter metrics. Uses metrics filter syntax. This is useful when an entity has been configured to emit metrics with additional tags.
overall_state
enum
The different states your monitor can be in. Allowed enum values: `Alert,Ignored,No Data,OK,Skipped,Unknown,Warn`
priority
int64
Integer from 1 (high) to 5 (low) indicating alert severity.
query [_required_]
string
The monitor query.
restricted_roles
[string]
A list of unique role identifiers to define which roles are allowed to edit the monitor. The unique identifiers for all roles can be pulled from the [Roles API](https://docs.datadoghq.com/api/latest/roles/#list-roles) and are located in the `data.id` field. Editing a monitor includes any updates to the monitor configuration, monitor deletion, and muting of the monitor for any amount of time. You can use the [Restriction Policies API](https://docs.datadoghq.com/api/latest/restriction-policies/) to manage write authorization for individual monitors by teams and users, in addition to roles.
state
object
Wrapper object with the different monitor states.
groups
object
Dictionary where the keys are groups (comma separated lists of tags) and the values are the list of groups your monitor is broken down on.
<any-key>
object
Monitor state for a single group.
last_nodata_ts
int64
Latest timestamp the monitor was in NO_DATA state.
last_notified_ts
int64
Latest timestamp of the notification sent for this monitor group.
last_resolved_ts
int64
Latest timestamp the monitor group was resolved.
last_triggered_ts
int64
Latest timestamp the monitor group triggered.
name
string
The name of the monitor.
status
enum
The different states your monitor can be in. Allowed enum values: `Alert,Ignored,No Data,OK,Skipped,Unknown,Warn`
tags
[string]
Tags associated to your monitor.
type [_required_]
enum
The type of the monitor. For more information about `type`, see the [monitor options](https://docs.datadoghq.com/monitors/guide/monitor_api_options/) docs. Allowed enum values: `composite,event alert,log alert,metric alert,process alert,query alert,rum alert,service check,synthetics alert,trace-analytics alert,slo alert,event-v2 alert,audit alert,ci-pipelines alert,ci-tests alert,error-tracking alert,database-monitoring alert,network-performance alert,cost alert,data-quality alert`
#####  Validate a monitor returns "OK" response
```
{
  "name": "Example-Monitor",
  "type": "log alert",
  "query": "logs(\"service:foo AND type:error\").index(\"main\").rollup(\"count\").by(\"source\").last(\"5m\") > 2",
  "message": "some message Notify: @hipchat-channel",
  "tags": [
    "test:examplemonitor",
    "env:ci"
  ],
  "priority": 3,
  "options": {
    "enable_logs_sample": true,
    "escalation_message": "the situation has escalated",
    "evaluation_delay": 700,
    "include_tags": true,
    "locked": false,
    "new_host_delay": 600,
    "no_data_timeframe": null,
    "notify_audit": false,
    "notify_no_data": false,
    "on_missing_data": "show_and_notify_no_data",
    "notification_preset_name": "hide_handles",
    "renotify_interval": 60,
    "require_full_window": true,
    "timeout_h": 24,
    "thresholds": {
      "critical": 2,
      "warning": 1
    }
  }
}
```

Copy
#####  Validate a multi-alert monitor returns "OK" response
```
{
  "name": "Example-Monitor",
  "type": "log alert",
  "query": "logs(\"service:foo AND type:error\").index(\"main\").rollup(\"count\").by(\"source,status\").last(\"5m\") > 2",
  "message": "some message Notify: @hipchat-channel",
  "tags": [
    "test:examplemonitor",
    "env:ci"
  ],
  "priority": 3,
  "options": {
    "enable_logs_sample": true,
    "escalation_message": "the situation has escalated",
    "evaluation_delay": 700,
    "group_retention_duration": "2d",
    "include_tags": true,
    "locked": false,
    "new_host_delay": 600,
    "no_data_timeframe": null,
    "notify_audit": false,
    "notify_by": [
      "status"
    ],
    "notify_no_data": false,
    "on_missing_data": "show_and_notify_no_data",
    "renotify_interval": 60,
    "require_full_window": true,
    "timeout_h": 24,
    "thresholds": {
      "critical": 2,
      "warning": 1
    }
  }
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/monitors/#ValidateMonitor-200-v1)
  * [400](https://docs.datadoghq.com/api/latest/monitors/#ValidateMonitor-400-v1)
  * [403](https://docs.datadoghq.com/api/latest/monitors/#ValidateMonitor-403-v1)
  * [429](https://docs.datadoghq.com/api/latest/monitors/#ValidateMonitor-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


Expand All
Field
Type
Description
No response body
```
{}
```

Copy
Invalid JSON
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


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
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


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
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/monitors/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/monitors/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/monitors/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/monitors/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/monitors/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/monitors/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/monitors/?code-lang=typescript)
  * [Python [legacy]](https://docs.datadoghq.com/api/latest/monitors/?code-lang=python-legacy)
  * [Ruby [legacy]](https://docs.datadoghq.com/api/latest/monitors/?code-lang=ruby-legacy)


#####  Validate a monitor returns "OK" response
Copy
```
                          # Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/monitor/validate" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "name": "Example-Monitor",
  "type": "log alert",
  "query": "logs(\"service:foo AND type:error\").index(\"main\").rollup(\"count\").by(\"source\").last(\"5m\") > 2",
  "message": "some message Notify: @hipchat-channel",
  "tags": [
    "test:examplemonitor",
    "env:ci"
  ],
  "priority": 3,
  "options": {
    "enable_logs_sample": true,
    "escalation_message": "the situation has escalated",
    "evaluation_delay": 700,
    "include_tags": true,
    "locked": false,
    "new_host_delay": 600,
    "no_data_timeframe": null,
    "notify_audit": false,
    "notify_no_data": false,
    "on_missing_data": "show_and_notify_no_data",
    "notification_preset_name": "hide_handles",
    "renotify_interval": 60,
    "require_full_window": true,
    "timeout_h": 24,
    "thresholds": {
      "critical": 2,
      "warning": 1
    }
  }
}
EOF  

                        
```

#####  Validate a multi-alert monitor returns "OK" response
Copy
```
                          # Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/monitor/validate" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "name": "Example-Monitor",
  "type": "log alert",
  "query": "logs(\"service:foo AND type:error\").index(\"main\").rollup(\"count\").by(\"source,status\").last(\"5m\") > 2",
  "message": "some message Notify: @hipchat-channel",
  "tags": [
    "test:examplemonitor",
    "env:ci"
  ],
  "priority": 3,
  "options": {
    "enable_logs_sample": true,
    "escalation_message": "the situation has escalated",
    "evaluation_delay": 700,
    "group_retention_duration": "2d",
    "include_tags": true,
    "locked": false,
    "new_host_delay": 600,
    "no_data_timeframe": null,
    "notify_audit": false,
    "notify_by": [
      "status"
    ],
    "notify_no_data": false,
    "on_missing_data": "show_and_notify_no_data",
    "renotify_interval": 60,
    "require_full_window": true,
    "timeout_h": 24,
    "thresholds": {
      "critical": 2,
      "warning": 1
    }
  }
}
EOF  

                        
```

#####  Validate a monitor returns "OK" response 
```
// Validate a monitor returns "OK" response

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
	body := datadogV1.Monitor{
		Name:    datadog.PtrString("Example-Monitor"),
		Type:    datadogV1.MONITORTYPE_LOG_ALERT,
		Query:   `logs("service:foo AND type:error").index("main").rollup("count").by("source").last("5m") > 2`,
		Message: datadog.PtrString("some message Notify: @hipchat-channel"),
		Tags: []string{
			"test:examplemonitor",
			"env:ci",
		},
		Priority: *datadog.NewNullableInt64(datadog.PtrInt64(3)),
		Options: &datadogV1.MonitorOptions{
			EnableLogsSample:       datadog.PtrBool(true),
			EscalationMessage:      datadog.PtrString("the situation has escalated"),
			EvaluationDelay:        *datadog.NewNullableInt64(datadog.PtrInt64(700)),
			IncludeTags:            datadog.PtrBool(true),
			Locked:                 datadog.PtrBool(false),
			NewHostDelay:           *datadog.NewNullableInt64(datadog.PtrInt64(600)),
			NoDataTimeframe:        *datadog.NewNullableInt64(nil),
			NotifyAudit:            datadog.PtrBool(false),
			NotifyNoData:           datadog.PtrBool(false),
			OnMissingData:          datadogV1.ONMISSINGDATAOPTION_SHOW_AND_NOTIFY_NO_DATA.Ptr(),
			NotificationPresetName: datadogV1.MONITOROPTIONSNOTIFICATIONPRESETS_HIDE_HANDLES.Ptr(),
			RenotifyInterval:       *datadog.NewNullableInt64(datadog.PtrInt64(60)),
			RequireFullWindow:      datadog.PtrBool(true),
			TimeoutH:               *datadog.NewNullableInt64(datadog.PtrInt64(24)),
			Thresholds: &datadogV1.MonitorThresholds{
				Critical: datadog.PtrFloat64(2),
				Warning:  *datadog.NewNullableFloat64(datadog.PtrFloat64(1)),
			},
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV1.NewMonitorsApi(apiClient)
	resp, r, err := api.ValidateMonitor(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `MonitorsApi.ValidateMonitor`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `MonitorsApi.ValidateMonitor`:\n%s\n", responseContent)
}

```

Copy
#####  Validate a multi-alert monitor returns "OK" response 
```
// Validate a multi-alert monitor returns "OK" response

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
	body := datadogV1.Monitor{
		Name:    datadog.PtrString("Example-Monitor"),
		Type:    datadogV1.MONITORTYPE_LOG_ALERT,
		Query:   `logs("service:foo AND type:error").index("main").rollup("count").by("source,status").last("5m") > 2`,
		Message: datadog.PtrString("some message Notify: @hipchat-channel"),
		Tags: []string{
			"test:examplemonitor",
			"env:ci",
		},
		Priority: *datadog.NewNullableInt64(datadog.PtrInt64(3)),
		Options: &datadogV1.MonitorOptions{
			EnableLogsSample:       datadog.PtrBool(true),
			EscalationMessage:      datadog.PtrString("the situation has escalated"),
			EvaluationDelay:        *datadog.NewNullableInt64(datadog.PtrInt64(700)),
			GroupRetentionDuration: datadog.PtrString("2d"),
			IncludeTags:            datadog.PtrBool(true),
			Locked:                 datadog.PtrBool(false),
			NewHostDelay:           *datadog.NewNullableInt64(datadog.PtrInt64(600)),
			NoDataTimeframe:        *datadog.NewNullableInt64(nil),
			NotifyAudit:            datadog.PtrBool(false),
			NotifyBy: []string{
				"status",
			},
			NotifyNoData:      datadog.PtrBool(false),
			OnMissingData:     datadogV1.ONMISSINGDATAOPTION_SHOW_AND_NOTIFY_NO_DATA.Ptr(),
			RenotifyInterval:  *datadog.NewNullableInt64(datadog.PtrInt64(60)),
			RequireFullWindow: datadog.PtrBool(true),
			TimeoutH:          *datadog.NewNullableInt64(datadog.PtrInt64(24)),
			Thresholds: &datadogV1.MonitorThresholds{
				Critical: datadog.PtrFloat64(2),
				Warning:  *datadog.NewNullableFloat64(datadog.PtrFloat64(1)),
			},
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV1.NewMonitorsApi(apiClient)
	resp, r, err := api.ValidateMonitor(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `MonitorsApi.ValidateMonitor`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `MonitorsApi.ValidateMonitor`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Validate a monitor returns "OK" response 
```
// Validate a monitor returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.MonitorsApi;
import com.datadog.api.client.v1.model.Monitor;
import com.datadog.api.client.v1.model.MonitorOptions;
import com.datadog.api.client.v1.model.MonitorOptionsNotificationPresets;
import com.datadog.api.client.v1.model.MonitorThresholds;
import com.datadog.api.client.v1.model.MonitorType;
import com.datadog.api.client.v1.model.OnMissingDataOption;
import java.util.Arrays;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    MonitorsApi apiInstance = new MonitorsApi(defaultClient);

    Monitor body =
        new Monitor()
            .name("Example-Monitor")
            .type(MonitorType.LOG_ALERT)
            .query(
                """
logs("service:foo AND type:error").index("main").rollup("count").by("source").last("5m") > 2
""")
            .message("some message Notify: @hipchat-channel")
            .tags(Arrays.asList("test:examplemonitor", "env:ci"))
            .priority(3L)
            .options(
                new MonitorOptions()
                    .enableLogsSample(true)
                    .escalationMessage("the situation has escalated")
                    .evaluationDelay(700L)
                    .includeTags(true)
                    .locked(false)
                    .newHostDelay(600L)
                    .noDataTimeframe(null)
                    .notifyAudit(false)
                    .notifyNoData(false)
                    .onMissingData(OnMissingDataOption.SHOW_AND_NOTIFY_NO_DATA)
                    .notificationPresetName(MonitorOptionsNotificationPresets.HIDE_HANDLES)
                    .renotifyInterval(60L)
                    .requireFullWindow(true)
                    .timeoutH(24L)
                    .thresholds(new MonitorThresholds().critical(2.0).warning(1.0)));

    try {
      apiInstance.validateMonitor(body);
    } catch (ApiException e) {
      System.err.println("Exception when calling MonitorsApi#validateMonitor");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}

```

Copy
#####  Validate a multi-alert monitor returns "OK" response 
```
// Validate a multi-alert monitor returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.MonitorsApi;
import com.datadog.api.client.v1.model.Monitor;
import com.datadog.api.client.v1.model.MonitorOptions;
import com.datadog.api.client.v1.model.MonitorThresholds;
import com.datadog.api.client.v1.model.MonitorType;
import com.datadog.api.client.v1.model.OnMissingDataOption;
import java.util.Arrays;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    MonitorsApi apiInstance = new MonitorsApi(defaultClient);

    Monitor body =
        new Monitor()
            .name("Example-Monitor")
            .type(MonitorType.LOG_ALERT)
            .query(
                """
logs("service:foo AND type:error").index("main").rollup("count").by("source,status").last("5m") > 2
""")
            .message("some message Notify: @hipchat-channel")
            .tags(Arrays.asList("test:examplemonitor", "env:ci"))
            .priority(3L)
            .options(
                new MonitorOptions()
                    .enableLogsSample(true)
                    .escalationMessage("the situation has escalated")
                    .evaluationDelay(700L)
                    .groupRetentionDuration("2d")
                    .includeTags(true)
                    .locked(false)
                    .newHostDelay(600L)
                    .noDataTimeframe(null)
                    .notifyAudit(false)
                    .notifyBy(Collections.singletonList("status"))
                    .notifyNoData(false)
                    .onMissingData(OnMissingDataOption.SHOW_AND_NOTIFY_NO_DATA)
                    .renotifyInterval(60L)
                    .requireFullWindow(true)
                    .timeoutH(24L)
                    .thresholds(new MonitorThresholds().critical(2.0).warning(1.0)));

    try {
      apiInstance.validateMonitor(body);
    } catch (ApiException e) {
      System.err.println("Exception when calling MonitorsApi#validateMonitor");
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

#####  Validate a monitor returns "OK" response
```
from datadog import initialize, api

options = {
    "api_key": "<DATADOG_API_KEY>",
    "app_key": "<DATADOG_APPLICATION_KEY>"
}

initialize(**options)

monitor_type = "query alert"
query = "avg(last_1h):sum:system.net.bytes_rcvd{host:host0} > 200"
monitor_options = {"thresholds": {"critical": 90.0}}

# Validate a monitor's definition
api.Monitor.validate(
    type=monitor_type,
    query=query,
    options=monitor_options,
)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python-legacy) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python "example.py"


```

#####  Validate a monitor returns "OK" response 
```
"""
Validate a monitor returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.monitors_api import MonitorsApi
from datadog_api_client.v1.model.monitor import Monitor
from datadog_api_client.v1.model.monitor_options import MonitorOptions
from datadog_api_client.v1.model.monitor_options_notification_presets import MonitorOptionsNotificationPresets
from datadog_api_client.v1.model.monitor_thresholds import MonitorThresholds
from datadog_api_client.v1.model.monitor_type import MonitorType
from datadog_api_client.v1.model.on_missing_data_option import OnMissingDataOption

body = Monitor(
    name="Example-Monitor",
    type=MonitorType.LOG_ALERT,
    query='logs("service:foo AND type:error").index("main").rollup("count").by("source").last("5m") > 2',
    message="some message Notify: @hipchat-channel",
    tags=[
        "test:examplemonitor",
        "env:ci",
    ],
    priority=3,
    options=MonitorOptions(
        enable_logs_sample=True,
        escalation_message="the situation has escalated",
        evaluation_delay=700,
        include_tags=True,
        locked=False,
        new_host_delay=600,
        no_data_timeframe=None,
        notify_audit=False,
        notify_no_data=False,
        on_missing_data=OnMissingDataOption.SHOW_AND_NOTIFY_NO_DATA,
        notification_preset_name=MonitorOptionsNotificationPresets.HIDE_HANDLES,
        renotify_interval=60,
        require_full_window=True,
        timeout_h=24,
        thresholds=MonitorThresholds(
            critical=2.0,
            warning=1.0,
        ),
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MonitorsApi(api_client)
    response = api_instance.validate_monitor(body=body)

    print(response)

```

Copy
#####  Validate a multi-alert monitor returns "OK" response 
```
"""
Validate a multi-alert monitor returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.monitors_api import MonitorsApi
from datadog_api_client.v1.model.monitor import Monitor
from datadog_api_client.v1.model.monitor_options import MonitorOptions
from datadog_api_client.v1.model.monitor_thresholds import MonitorThresholds
from datadog_api_client.v1.model.monitor_type import MonitorType
from datadog_api_client.v1.model.on_missing_data_option import OnMissingDataOption

body = Monitor(
    name="Example-Monitor",
    type=MonitorType.LOG_ALERT,
    query='logs("service:foo AND type:error").index("main").rollup("count").by("source,status").last("5m") > 2',
    message="some message Notify: @hipchat-channel",
    tags=[
        "test:examplemonitor",
        "env:ci",
    ],
    priority=3,
    options=MonitorOptions(
        enable_logs_sample=True,
        escalation_message="the situation has escalated",
        evaluation_delay=700,
        group_retention_duration="2d",
        include_tags=True,
        locked=False,
        new_host_delay=600,
        no_data_timeframe=None,
        notify_audit=False,
        notify_by=[
            "status",
        ],
        notify_no_data=False,
        on_missing_data=OnMissingDataOption.SHOW_AND_NOTIFY_NO_DATA,
        renotify_interval=60,
        require_full_window=True,
        timeout_h=24,
        thresholds=MonitorThresholds(
            critical=2.0,
            warning=1.0,
        ),
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MonitorsApi(api_client)
    response = api_instance.validate_monitor(body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Validate a monitor returns "OK" response
```
require 'dogapi'

api_key = '<DATADOG_API_KEY>'
app_key = '<DATADOG_APPLICATION_KEY>'

dog = Dogapi::Client.new(api_key, app_key)

type = 'query alert'
query = 'THIS IS A BAD QUERY'
parameters = {
  name: 'Bytes received on host0',
  message: 'We may need to add web hosts if this is consistently high.',
  tags: ['app:webserver', 'frontend'],
  options: {
    notify_no_data: true,
    no_data_timeframe: 20,
    thresholds: { critical: 90.0 }
  }
}

# Validate a monitor definition
dog.validate_monitor(type, query, parameters)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby-legacy) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Validate a monitor returns "OK" response 
```
# Validate a monitor returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::MonitorsAPI.new

body = DatadogAPIClient::V1::Monitor.new({
  name: "Example-Monitor",
  type: DatadogAPIClient::V1::MonitorType::LOG_ALERT,
  query: 'logs("service:foo AND type:error").index("main").rollup("count").by("source").last("5m") > 2',
  message: "some message Notify: @hipchat-channel",
  tags: [
    "test:examplemonitor",
    "env:ci",
  ],
  priority: 3,
  options: DatadogAPIClient::V1::MonitorOptions.new({
    enable_logs_sample: true,
    escalation_message: "the situation has escalated",
    evaluation_delay: 700,
    include_tags: true,
    locked: false,
    new_host_delay: 600,
    no_data_timeframe: nil,
    notify_audit: false,
    notify_no_data: false,
    on_missing_data: DatadogAPIClient::V1::OnMissingDataOption::SHOW_AND_NOTIFY_NO_DATA,
    notification_preset_name: DatadogAPIClient::V1::MonitorOptionsNotificationPresets::HIDE_HANDLES,
    renotify_interval: 60,
    require_full_window: true,
    timeout_h: 24,
    thresholds: DatadogAPIClient::V1::MonitorThresholds.new({
      critical: 2,
      warning: 1,
    }),
  }),
})
p api_instance.validate_monitor(body)

```

Copy
#####  Validate a multi-alert monitor returns "OK" response 
```
# Validate a multi-alert monitor returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::MonitorsAPI.new

body = DatadogAPIClient::V1::Monitor.new({
  name: "Example-Monitor",
  type: DatadogAPIClient::V1::MonitorType::LOG_ALERT,
  query: 'logs("service:foo AND type:error").index("main").rollup("count").by("source,status").last("5m") > 2',
  message: "some message Notify: @hipchat-channel",
  tags: [
    "test:examplemonitor",
    "env:ci",
  ],
  priority: 3,
  options: DatadogAPIClient::V1::MonitorOptions.new({
    enable_logs_sample: true,
    escalation_message: "the situation has escalated",
    evaluation_delay: 700,
    group_retention_duration: "2d",
    include_tags: true,
    locked: false,
    new_host_delay: 600,
    no_data_timeframe: nil,
    notify_audit: false,
    notify_by: [
      "status",
    ],
    notify_no_data: false,
    on_missing_data: DatadogAPIClient::V1::OnMissingDataOption::SHOW_AND_NOTIFY_NO_DATA,
    renotify_interval: 60,
    require_full_window: true,
    timeout_h: 24,
    thresholds: DatadogAPIClient::V1::MonitorThresholds.new({
      critical: 2,
      warning: 1,
    }),
  }),
})
p api_instance.validate_monitor(body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Validate a monitor returns "OK" response 
```
// Validate a monitor returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_monitors::MonitorsAPI;
use datadog_api_client::datadogV1::model::Monitor;
use datadog_api_client::datadogV1::model::MonitorOptions;
use datadog_api_client::datadogV1::model::MonitorOptionsNotificationPresets;
use datadog_api_client::datadogV1::model::MonitorThresholds;
use datadog_api_client::datadogV1::model::MonitorType;
use datadog_api_client::datadogV1::model::OnMissingDataOption;

#[tokio::main]
async fn main() {
    let body =
        Monitor::new(
            r#"logs("service:foo AND type:error").index("main").rollup("count").by("source").last("5m") > 2"#.to_string(),
            MonitorType::LOG_ALERT,
        )
            .message("some message Notify: @hipchat-channel".to_string())
            .name("Example-Monitor".to_string())
            .options(
                MonitorOptions::new()
                    .enable_logs_sample(true)
                    .escalation_message("the situation has escalated".to_string())
                    .evaluation_delay(Some(700))
                    .include_tags(true)
                    .locked(false)
                    .new_host_delay(Some(600))
                    .no_data_timeframe(None)
                    .notification_preset_name(MonitorOptionsNotificationPresets::HIDE_HANDLES)
                    .notify_audit(false)
                    .notify_no_data(false)
                    .on_missing_data(OnMissingDataOption::SHOW_AND_NOTIFY_NO_DATA)
                    .renotify_interval(Some(60))
                    .require_full_window(true)
                    .thresholds(MonitorThresholds::new().critical(2.0 as f64).warning(Some(1.0 as f64)))
                    .timeout_h(Some(24)),
            )
            .priority(Some(3))
            .tags(vec!["test:examplemonitor".to_string(), "env:ci".to_string()]);
    let configuration = datadog::Configuration::new();
    let api = MonitorsAPI::with_config(configuration);
    let resp = api.validate_monitor(body).await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}

```

Copy
#####  Validate a multi-alert monitor returns "OK" response 
```
// Validate a multi-alert monitor returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_monitors::MonitorsAPI;
use datadog_api_client::datadogV1::model::Monitor;
use datadog_api_client::datadogV1::model::MonitorOptions;
use datadog_api_client::datadogV1::model::MonitorThresholds;
use datadog_api_client::datadogV1::model::MonitorType;
use datadog_api_client::datadogV1::model::OnMissingDataOption;

#[tokio::main]
async fn main() {
    let body =
        Monitor::new(
            r#"logs("service:foo AND type:error").index("main").rollup("count").by("source,status").last("5m") > 2"#.to_string(),
            MonitorType::LOG_ALERT,
        )
            .message("some message Notify: @hipchat-channel".to_string())
            .name("Example-Monitor".to_string())
            .options(
                MonitorOptions::new()
                    .enable_logs_sample(true)
                    .escalation_message("the situation has escalated".to_string())
                    .evaluation_delay(Some(700))
                    .group_retention_duration("2d".to_string())
                    .include_tags(true)
                    .locked(false)
                    .new_host_delay(Some(600))
                    .no_data_timeframe(None)
                    .notify_audit(false)
                    .notify_by(vec!["status".to_string()])
                    .notify_no_data(false)
                    .on_missing_data(OnMissingDataOption::SHOW_AND_NOTIFY_NO_DATA)
                    .renotify_interval(Some(60))
                    .require_full_window(true)
                    .thresholds(MonitorThresholds::new().critical(2.0 as f64).warning(Some(1.0 as f64)))
                    .timeout_h(Some(24)),
            )
            .priority(Some(3))
            .tags(vec!["test:examplemonitor".to_string(), "env:ci".to_string()]);
    let configuration = datadog::Configuration::new();
    let api = MonitorsAPI::with_config(configuration);
    let resp = api.validate_monitor(body).await;
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

#####  Validate a monitor returns "OK" response 
```
/**
 * Validate a monitor returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.MonitorsApi(configuration);

const params: v1.MonitorsApiValidateMonitorRequest = {
  body: {
    name: "Example-Monitor",
    type: "log alert",
    query: `logs("service:foo AND type:error").index("main").rollup("count").by("source").last("5m") > 2`,
    message: "some message Notify: @hipchat-channel",
    tags: ["test:examplemonitor", "env:ci"],
    priority: 3,
    options: {
      enableLogsSample: true,
      escalationMessage: "the situation has escalated",
      evaluationDelay: 700,
      includeTags: true,
      locked: false,
      newHostDelay: 600,
      noDataTimeframe: undefined,
      notifyAudit: false,
      notifyNoData: false,
      onMissingData: "show_and_notify_no_data",
      notificationPresetName: "hide_handles",
      renotifyInterval: 60,
      requireFullWindow: true,
      timeoutH: 24,
      thresholds: {
        critical: 2,
        warning: 1,
      },
    },
  },
};

apiInstance
  .validateMonitor(params)
  .then((data: any) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));

```

Copy
#####  Validate a multi-alert monitor returns "OK" response 
```
/**
 * Validate a multi-alert monitor returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.MonitorsApi(configuration);

const params: v1.MonitorsApiValidateMonitorRequest = {
  body: {
    name: "Example-Monitor",
    type: "log alert",
    query: `logs("service:foo AND type:error").index("main").rollup("count").by("source,status").last("5m") > 2`,
    message: "some message Notify: @hipchat-channel",
    tags: ["test:examplemonitor", "env:ci"],
    priority: 3,
    options: {
      enableLogsSample: true,
      escalationMessage: "the situation has escalated",
      evaluationDelay: 700,
      groupRetentionDuration: "2d",
      includeTags: true,
      locked: false,
      newHostDelay: 600,
      noDataTimeframe: undefined,
      notifyAudit: false,
      notifyBy: ["status"],
      notifyNoData: false,
      onMissingData: "show_and_notify_no_data",
      renotifyInterval: 60,
      requireFullWindow: true,
      timeoutH: 24,
      thresholds: {
        critical: 2,
        warning: 1,
      },
    },
  },
};

apiInstance
  .validateMonitor(params)
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
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"


```

* * *
## [Validate an existing monitor](https://docs.datadoghq.com/api/latest/monitors/#validate-an-existing-monitor)
  * [v1 (latest)](https://docs.datadoghq.com/api/latest/monitors/#validate-an-existing-monitor-v1)


POST https://api.ap1.datadoghq.com/api/v1/monitor/{monitor_id}/validatehttps://api.ap2.datadoghq.com/api/v1/monitor/{monitor_id}/validatehttps://api.datadoghq.eu/api/v1/monitor/{monitor_id}/validatehttps://api.ddog-gov.com/api/v1/monitor/{monitor_id}/validatehttps://api.datadoghq.com/api/v1/monitor/{monitor_id}/validatehttps://api.us3.datadoghq.com/api/v1/monitor/{monitor_id}/validatehttps://api.us5.datadoghq.com/api/v1/monitor/{monitor_id}/validate
### Overview
Validate the monitor provided in the request. This endpoint requires the `monitors_read` permission.
OAuth apps require the `monitors_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#monitors) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
monitor_id [_required_]
integer
The ID of the monitor
### Request
#### Body Data (required)
Monitor request object
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


Field
Type
Description
assets
[object]
The list of monitor assets tied to a monitor, which represents key links for users to take action on monitor alerts (for example, runbooks).
category [_required_]
enum
Indicates the type of asset this entity represents on a monitor. Allowed enum values: `runbook`
name [_required_]
string
Name for the monitor asset
resource_key
string
Represents the identifier of the internal Datadog resource that this asset represents. IDs in this field should be passed in as strings.
resource_type
enum
Type of internal Datadog resource associated with a monitor asset. Allowed enum values: `notebook`
url [_required_]
string
URL link for the asset. For links with an internal resource type set, this should be the relative path to where the Datadog domain is appended internally. For external links, this should be the full URL path.
created
date-time
Timestamp of the monitor creation.
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
deleted
date-time
Whether or not the monitor is deleted. (Always `null`)
draft_status
enum
Indicates whether the monitor is in a draft or published state.
`draft`: The monitor appears as Draft and does not send notifications. `published`: The monitor is active and evaluates conditions and notify as configured.
This field is in preview. The draft value is only available to customers with the feature enabled. Allowed enum values: `draft,published`
default: `published`
id
int64
ID of this monitor.
matching_downtimes
[object]
A list of active v1 downtimes that match this monitor.
end
int64
POSIX timestamp to end the downtime.
id [_required_]
int64
The downtime ID.
scope
[string]
The scope(s) to which the downtime applies. Must be in `key:value` format. For example, `host:app2`. Provide multiple scopes as a comma-separated list like `env:dev,env:prod`. The resulting downtime applies to sources that matches ALL provided scopes (`env:dev` **AND** `env:prod`).
start
int64
POSIX timestamp to start the downtime.
message
string
A message to include with notifications for this monitor.
modified
date-time
Last timestamp when the monitor was edited.
multi
boolean
Whether or not the monitor is broken down on different groups.
name
string
The monitor name.
options
object
List of options associated with your monitor.
aggregation
object
Type of aggregation performed in the monitor query.
group_by
string
Group to break down the monitor on.
metric
string
Metric name used in the monitor.
type
string
Metric type used in the monitor.
device_ids
[string]
**DEPRECATED** : IDs of the device the Synthetics monitor is running on.
enable_logs_sample
boolean
Whether or not to send a log sample when the log monitor triggers.
enable_samples
boolean
Whether or not to send a list of samples when the monitor triggers. This is only used by CI Test and Pipeline monitors.
escalation_message
string
We recommend using the [is_renotify](https://docs.datadoghq.com/monitors/notify/?tab=is_alert#renotify), block in the original message instead. A message to include with a re-notification. Supports the `@username` notification we allow elsewhere. Not applicable if `renotify_interval` is `None`.
evaluation_delay
int64
Time (in seconds) to delay evaluation, as a non-negative integer. For example, if the value is set to `300` (5min), the timeframe is set to `last_5m` and the time is 7:00, the monitor evaluates data from 6:50 to 6:55. This is useful for AWS CloudWatch and other backfilled metrics to ensure the monitor always has data during evaluation.
group_retention_duration
string
The time span after which groups with missing data are dropped from the monitor state. The minimum value is one hour, and the maximum value is 72 hours. Example values are: "60m", "1h", and "2d". This option is only available for APM Trace Analytics, Audit Trail, CI, Error Tracking, Event, Logs, and RUM monitors.
groupby_simple_monitor
boolean
**DEPRECATED** : Whether the log alert monitor triggers a single alert or multiple alerts when any group breaches a threshold. Use `notify_by` instead.
include_tags
boolean
A Boolean indicating whether notifications from this monitor automatically inserts its triggering tags into the title.
**Examples**
  * If `True`, `[Triggered on {host:h1}] Monitor Title`
  * If `False`, `[Triggered] Monitor Title`


default: `true`
locked
boolean
**DEPRECATED** : Whether or not the monitor is locked (only editable by creator and admins). Use `restricted_roles` instead.
min_failure_duration
int64
How long the test should be in failure before alerting (integer, number of seconds, max 7200).
min_location_failed
int64
The minimum number of locations in failure at the same time during at least one moment in the `min_failure_duration` period (`min_location_failed` and `min_failure_duration` are part of the advanced alerting rules - integer, >= 1).
default: `1`
new_group_delay
int64
Time (in seconds) to skip evaluations for new groups.
For example, this option can be used to skip evaluations for new hosts while they initialize.
Must be a non negative integer.
new_host_delay
int64
**DEPRECATED** : Time (in seconds) to allow a host to boot and applications to fully start before starting the evaluation of monitor results. Should be a non negative integer.
Use new_group_delay instead.
default: `300`
no_data_timeframe
int64
The number of minutes before a monitor notifies after data stops reporting. Datadog recommends at least 2x the monitor timeframe for query alerts or 2 minutes for service checks. If omitted, 2x the evaluation timeframe is used for query alerts, and 24 hours is used for service checks.
notification_preset_name
enum
Toggles the display of additional content sent in the monitor notification. Allowed enum values: `show_all,hide_query,hide_handles,hide_all`
default: `show_all`
notify_audit
boolean
A Boolean indicating whether tagged users is notified on changes to this monitor.
notify_by
[string]
Controls what granularity a monitor alerts on. Only available for monitors with groupings. For instance, a monitor grouped by `cluster`, `namespace`, and `pod` can be configured to only notify on each new `cluster` violating the alert conditions by setting `notify_by` to `["cluster"]`. Tags mentioned in `notify_by` must be a subset of the grouping tags in the query. For example, a query grouped by `cluster` and `namespace` cannot notify on `region`. Setting `notify_by` to `["*"]` configures the monitor to notify as a simple-alert.
notify_no_data
boolean
A Boolean indicating whether this monitor notifies when data stops reporting. Defaults to `false`.
on_missing_data
enum
Controls how groups or monitors are treated if an evaluation does not return any data points. The default option results in different behavior depending on the monitor query type. For monitors using Count queries, an empty monitor evaluation is treated as 0 and is compared to the threshold conditions. For monitors using any query type other than Count, for example Gauge, Measure, or Rate, the monitor shows the last known status. This option is only available for APM Trace Analytics, Audit Trail, CI, Error Tracking, Event, Logs, and RUM monitors. Allowed enum values: `default,show_no_data,show_and_notify_no_data,resolve`
renotify_interval
int64
The number of minutes after the last notification before a monitor re-notifies on the current status. It only re-notifies if it’s not resolved.
renotify_occurrences
int64
The number of times re-notification messages should be sent on the current status at the provided re-notification interval.
renotify_statuses
[string]
The types of monitor statuses for which re-notification messages are sent. Default: **null** if `renotify_interval` is **null**. If `renotify_interval` is set, defaults to renotify on `Alert` and `No Data`.
require_full_window
boolean
A Boolean indicating whether this monitor needs a full window of data before it’s evaluated. We highly recommend you set this to `false` for sparse metrics, otherwise some evaluations are skipped. Default is false. This setting only applies to metric monitors.
scheduling_options
object
Configuration options for scheduling.
custom_schedule
object
Configuration options for the custom schedule. **This feature is in private beta.**
recurrences
[object]
Array of custom schedule recurrences.
rrule
string
Defines the recurrence rule (RRULE) for a given schedule.
start
string
Defines the start date and time of the recurring schedule.
timezone
string
Defines the timezone the schedule runs on.
evaluation_window
object
Configuration options for the evaluation window. If `hour_starts` is set, no other fields may be set. Otherwise, `day_starts` and `month_starts` must be set together.
day_starts
string
The time of the day at which a one day cumulative evaluation window starts.
hour_starts
int32
The minute of the hour at which a one hour cumulative evaluation window starts.
month_starts
int32
The day of the month at which a one month cumulative evaluation window starts.
timezone
string
The timezone of the time of the day of the cumulative evaluation window start.
silenced
object
**DEPRECATED** : Information about the downtime applied to the monitor. Only shows v1 downtimes.
<any-key>
int64
UTC epoch timestamp in seconds when the downtime for the group expires.
synthetics_check_id
string
**DEPRECATED** : ID of the corresponding Synthetic check.
threshold_windows
object
Alerting time window options.
recovery_window
string
Describes how long an anomalous metric must be normal before the alert recovers.
trigger_window
string
Describes how long a metric must be anomalous before an alert triggers.
thresholds
object
List of the different monitor threshold available.
critical
double
The monitor `CRITICAL` threshold.
critical_recovery
double
The monitor `CRITICAL` recovery threshold.
ok
double
The monitor `OK` threshold.
unknown
double
The monitor UNKNOWN threshold.
warning
double
The monitor `WARNING` threshold.
warning_recovery
double
The monitor `WARNING` recovery threshold.
timeout_h
int64
The number of hours of the monitor not reporting data before it automatically resolves from a triggered state. The minimum allowed value is 0 hours. The maximum allowed value is 24 hours.
variables
[ <oneOf>]
List of requests that can be used in the monitor query. **This feature is currently in beta.**
Option 1
object
A formula and functions events query.
compute [_required_]
object
Compute options.
aggregation [_required_]
enum
Aggregation methods for event platform queries. Allowed enum values: `count,cardinality,median,pc75,pc90,pc95,pc98,pc99,sum,min,max,avg`
interval
int64
A time interval in milliseconds.
metric
string
Measurable attribute to compute.
data_source [_required_]
enum
Data source for event platform-based queries. Allowed enum values: `rum,ci_pipelines,ci_tests,audit,events,logs,spans,database_queries,network`
group_by
[object]
Group by options.
facet [_required_]
string
Event facet.
limit
int64
Number of groups to return.
sort
object
Options for sorting group by results.
aggregation [_required_]
enum
Aggregation methods for event platform queries. Allowed enum values: `count,cardinality,median,pc75,pc90,pc95,pc98,pc99,sum,min,max,avg`
metric
string
Metric used for sorting group by results.
order
enum
Direction of sort. Allowed enum values: `asc,desc`
default: `desc`
indexes
[string]
An array of index names to query in the stream. Omit or use `[]` to query all indexes at once.
name [_required_]
string
Name of the query for use in formulas.
search
object
Search options.
query [_required_]
string
Events search string.
Option 2
object
A formula and functions cost query.
aggregator
enum
Aggregation methods for metric queries. Allowed enum values: `avg,sum,max,min,last,area,l2norm,percentile,stddev`
data_source [_required_]
enum
Data source for cost queries. Allowed enum values: `metrics,cloud_cost,datadog_usage`
name [_required_]
string
Name of the query for use in formulas.
query [_required_]
string
The monitor query.
Option 3
object
A formula and functions data quality query.
data_source [_required_]
enum
Data source for data quality queries. Allowed enum values: `data_quality_metrics`
filter [_required_]
string
Filter expression used to match on data entities. Uses Aastra query syntax.
group_by
[string]
Optional grouping fields for aggregation.
measure [_required_]
string
The data quality measure to query. Common values include: `bytes`, `cardinality`, `custom`, `freshness`, `max`, `mean`, `min`, `nullness`, `percent_negative`, `percent_zero`, `row_count`, `stddev`, `sum`, `uniqueness`. Additional values may be supported.
monitor_options
object
Monitor configuration options for data quality queries.
crontab_override
string
Crontab expression to override the default schedule.
custom_sql
string
Custom SQL query for the monitor.
custom_where
string
Custom WHERE clause for the query.
group_by_columns
[string]
Columns to group results by.
model_type_override
enum
Override for the model type used in anomaly detection. Allowed enum values: `freshness,percentage,any`
name [_required_]
string
Name of the query for use in formulas.
schema_version
string
Schema version for the data quality query.
scope
string
Optional scoping expression to further filter metrics. Uses metrics filter syntax. This is useful when an entity has been configured to emit metrics with additional tags.
overall_state
enum
The different states your monitor can be in. Allowed enum values: `Alert,Ignored,No Data,OK,Skipped,Unknown,Warn`
priority
int64
Integer from 1 (high) to 5 (low) indicating alert severity.
query [_required_]
string
The monitor query.
restricted_roles
[string]
A list of unique role identifiers to define which roles are allowed to edit the monitor. The unique identifiers for all roles can be pulled from the [Roles API](https://docs.datadoghq.com/api/latest/roles/#list-roles) and are located in the `data.id` field. Editing a monitor includes any updates to the monitor configuration, monitor deletion, and muting of the monitor for any amount of time. You can use the [Restriction Policies API](https://docs.datadoghq.com/api/latest/restriction-policies/) to manage write authorization for individual monitors by teams and users, in addition to roles.
state
object
Wrapper object with the different monitor states.
groups
object
Dictionary where the keys are groups (comma separated lists of tags) and the values are the list of groups your monitor is broken down on.
<any-key>
object
Monitor state for a single group.
last_nodata_ts
int64
Latest timestamp the monitor was in NO_DATA state.
last_notified_ts
int64
Latest timestamp of the notification sent for this monitor group.
last_resolved_ts
int64
Latest timestamp the monitor group was resolved.
last_triggered_ts
int64
Latest timestamp the monitor group triggered.
name
string
The name of the monitor.
status
enum
The different states your monitor can be in. Allowed enum values: `Alert,Ignored,No Data,OK,Skipped,Unknown,Warn`
tags
[string]
Tags associated to your monitor.
type [_required_]
enum
The type of the monitor. For more information about `type`, see the [monitor options](https://docs.datadoghq.com/monitors/guide/monitor_api_options/) docs. Allowed enum values: `composite,event alert,log alert,metric alert,process alert,query alert,rum alert,service check,synthetics alert,trace-analytics alert,slo alert,event-v2 alert,audit alert,ci-pipelines alert,ci-tests alert,error-tracking alert,database-monitoring alert,network-performance alert,cost alert,data-quality alert`
```
{
  "name": "Example-Monitor",
  "type": "log alert",
  "query": "logs(\"service:foo AND type:error\").index(\"main\").rollup(\"count\").by(\"source\").last(\"5m\") > 2",
  "message": "some message Notify: @hipchat-channel",
  "tags": [
    "test:examplemonitor",
    "env:ci"
  ],
  "priority": 3,
  "options": {
    "enable_logs_sample": true,
    "escalation_message": "the situation has escalated",
    "evaluation_delay": 700,
    "include_tags": true,
    "locked": false,
    "new_host_delay": 600,
    "no_data_timeframe": null,
    "notify_audit": false,
    "notify_no_data": false,
    "on_missing_data": "show_and_notify_no_data",
    "notification_preset_name": "hide_handles",
    "renotify_interval": 60,
    "require_full_window": true,
    "timeout_h": 24,
    "thresholds": {
      "critical": 2,
      "warning": 1
    }
  }
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/monitors/#ValidateExistingMonitor-200-v1)
  * [400](https://docs.datadoghq.com/api/latest/monitors/#ValidateExistingMonitor-400-v1)
  * [403](https://docs.datadoghq.com/api/latest/monitors/#ValidateExistingMonitor-403-v1)
  * [429](https://docs.datadoghq.com/api/latest/monitors/#ValidateExistingMonitor-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


Expand All
Field
Type
Description
No response body
```
{}
```

Copy
Invalid JSON
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


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
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


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
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/monitors/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/monitors/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/monitors/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/monitors/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/monitors/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/monitors/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/monitors/?code-lang=typescript)


#####  Validate an existing monitor returns "OK" response
Copy
```
                          # Path parameters  
export monitor_id="6.66486743e+08"  
# Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/monitor/${monitor_id}/validate" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "name": "Example-Monitor",
  "type": "log alert",
  "query": "logs(\"service:foo AND type:error\").index(\"main\").rollup(\"count\").by(\"source\").last(\"5m\") > 2",
  "message": "some message Notify: @hipchat-channel",
  "tags": [
    "test:examplemonitor",
    "env:ci"
  ],
  "priority": 3,
  "options": {
    "enable_logs_sample": true,
    "escalation_message": "the situation has escalated",
    "evaluation_delay": 700,
    "include_tags": true,
    "locked": false,
    "new_host_delay": 600,
    "no_data_timeframe": null,
    "notify_audit": false,
    "notify_no_data": false,
    "on_missing_data": "show_and_notify_no_data",
    "notification_preset_name": "hide_handles",
    "renotify_interval": 60,
    "require_full_window": true,
    "timeout_h": 24,
    "thresholds": {
      "critical": 2,
      "warning": 1
    }
  }
}
EOF  

                        
```

#####  Validate an existing monitor returns "OK" response
```
// Validate an existing monitor returns "OK" response

package main

import (
	"context"
	"encoding/json"
	"fmt"
	"os"
	"strconv"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV1"
)

func main() {
	// there is a valid "monitor" in the system
	MonitorID, _ := strconv.ParseInt(os.Getenv("MONITOR_ID"), 10, 64)

	body := datadogV1.Monitor{
		Name:    datadog.PtrString("Example-Monitor"),
		Type:    datadogV1.MONITORTYPE_LOG_ALERT,
		Query:   `logs("service:foo AND type:error").index("main").rollup("count").by("source").last("5m") > 2`,
		Message: datadog.PtrString("some message Notify: @hipchat-channel"),
		Tags: []string{
			"test:examplemonitor",
			"env:ci",
		},
		Priority: *datadog.NewNullableInt64(datadog.PtrInt64(3)),
		Options: &datadogV1.MonitorOptions{
			EnableLogsSample:       datadog.PtrBool(true),
			EscalationMessage:      datadog.PtrString("the situation has escalated"),
			EvaluationDelay:        *datadog.NewNullableInt64(datadog.PtrInt64(700)),
			IncludeTags:            datadog.PtrBool(true),
			Locked:                 datadog.PtrBool(false),
			NewHostDelay:           *datadog.NewNullableInt64(datadog.PtrInt64(600)),
			NoDataTimeframe:        *datadog.NewNullableInt64(nil),
			NotifyAudit:            datadog.PtrBool(false),
			NotifyNoData:           datadog.PtrBool(false),
			OnMissingData:          datadogV1.ONMISSINGDATAOPTION_SHOW_AND_NOTIFY_NO_DATA.Ptr(),
			NotificationPresetName: datadogV1.MONITOROPTIONSNOTIFICATIONPRESETS_HIDE_HANDLES.Ptr(),
			RenotifyInterval:       *datadog.NewNullableInt64(datadog.PtrInt64(60)),
			RequireFullWindow:      datadog.PtrBool(true),
			TimeoutH:               *datadog.NewNullableInt64(datadog.PtrInt64(24)),
			Thresholds: &datadogV1.MonitorThresholds{
				Critical: datadog.PtrFloat64(2),
				Warning:  *datadog.NewNullableFloat64(datadog.PtrFloat64(1)),
			},
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV1.NewMonitorsApi(apiClient)
	resp, r, err := api.ValidateExistingMonitor(ctx, MonitorID, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `MonitorsApi.ValidateExistingMonitor`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `MonitorsApi.ValidateExistingMonitor`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Validate an existing monitor returns "OK" response
```
// Validate an existing monitor returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.MonitorsApi;
import com.datadog.api.client.v1.model.Monitor;
import com.datadog.api.client.v1.model.MonitorOptions;
import com.datadog.api.client.v1.model.MonitorOptionsNotificationPresets;
import com.datadog.api.client.v1.model.MonitorThresholds;
import com.datadog.api.client.v1.model.MonitorType;
import com.datadog.api.client.v1.model.OnMissingDataOption;
import java.util.Arrays;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    MonitorsApi apiInstance = new MonitorsApi(defaultClient);

    // there is a valid "monitor" in the system
    Long MONITOR_ID = Long.parseLong(System.getenv("MONITOR_ID"));

    Monitor body =
        new Monitor()
            .name("Example-Monitor")
            .type(MonitorType.LOG_ALERT)
            .query(
                """
logs("service:foo AND type:error").index("main").rollup("count").by("source").last("5m") > 2
""")
            .message("some message Notify: @hipchat-channel")
            .tags(Arrays.asList("test:examplemonitor", "env:ci"))
            .priority(3L)
            .options(
                new MonitorOptions()
                    .enableLogsSample(true)
                    .escalationMessage("the situation has escalated")
                    .evaluationDelay(700L)
                    .includeTags(true)
                    .locked(false)
                    .newHostDelay(600L)
                    .noDataTimeframe(null)
                    .notifyAudit(false)
                    .notifyNoData(false)
                    .onMissingData(OnMissingDataOption.SHOW_AND_NOTIFY_NO_DATA)
                    .notificationPresetName(MonitorOptionsNotificationPresets.HIDE_HANDLES)
                    .renotifyInterval(60L)
                    .requireFullWindow(true)
                    .timeoutH(24L)
                    .thresholds(new MonitorThresholds().critical(2.0).warning(1.0)));

    try {
      apiInstance.validateExistingMonitor(MONITOR_ID, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling MonitorsApi#validateExistingMonitor");
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

#####  Validate an existing monitor returns "OK" response
```
"""
Validate an existing monitor returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.monitors_api import MonitorsApi
from datadog_api_client.v1.model.monitor import Monitor
from datadog_api_client.v1.model.monitor_options import MonitorOptions
from datadog_api_client.v1.model.monitor_options_notification_presets import MonitorOptionsNotificationPresets
from datadog_api_client.v1.model.monitor_thresholds import MonitorThresholds
from datadog_api_client.v1.model.monitor_type import MonitorType
from datadog_api_client.v1.model.on_missing_data_option import OnMissingDataOption

# there is a valid "monitor" in the system
MONITOR_ID = environ["MONITOR_ID"]

body = Monitor(
    name="Example-Monitor",
    type=MonitorType.LOG_ALERT,
    query='logs("service:foo AND type:error").index("main").rollup("count").by("source").last("5m") > 2',
    message="some message Notify: @hipchat-channel",
    tags=[
        "test:examplemonitor",
        "env:ci",
    ],
    priority=3,
    options=MonitorOptions(
        enable_logs_sample=True,
        escalation_message="the situation has escalated",
        evaluation_delay=700,
        include_tags=True,
        locked=False,
        new_host_delay=600,
        no_data_timeframe=None,
        notify_audit=False,
        notify_no_data=False,
        on_missing_data=OnMissingDataOption.SHOW_AND_NOTIFY_NO_DATA,
        notification_preset_name=MonitorOptionsNotificationPresets.HIDE_HANDLES,
        renotify_interval=60,
        require_full_window=True,
        timeout_h=24,
        thresholds=MonitorThresholds(
            critical=2.0,
            warning=1.0,
        ),
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MonitorsApi(api_client)
    response = api_instance.validate_existing_monitor(monitor_id=int(MONITOR_ID), body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Validate an existing monitor returns "OK" response
```
# Validate an existing monitor returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::MonitorsAPI.new

# there is a valid "monitor" in the system
MONITOR_ID = ENV["MONITOR_ID"]

body = DatadogAPIClient::V1::Monitor.new({
  name: "Example-Monitor",
  type: DatadogAPIClient::V1::MonitorType::LOG_ALERT,
  query: 'logs("service:foo AND type:error").index("main").rollup("count").by("source").last("5m") > 2',
  message: "some message Notify: @hipchat-channel",
  tags: [
    "test:examplemonitor",
    "env:ci",
  ],
  priority: 3,
  options: DatadogAPIClient::V1::MonitorOptions.new({
    enable_logs_sample: true,
    escalation_message: "the situation has escalated",
    evaluation_delay: 700,
    include_tags: true,
    locked: false,
    new_host_delay: 600,
    no_data_timeframe: nil,
    notify_audit: false,
    notify_no_data: false,
    on_missing_data: DatadogAPIClient::V1::OnMissingDataOption::SHOW_AND_NOTIFY_NO_DATA,
    notification_preset_name: DatadogAPIClient::V1::MonitorOptionsNotificationPresets::HIDE_HANDLES,
    renotify_interval: 60,
    require_full_window: true,
    timeout_h: 24,
    thresholds: DatadogAPIClient::V1::MonitorThresholds.new({
      critical: 2,
      warning: 1,
    }),
  }),
})
p api_instance.validate_existing_monitor(MONITOR_ID.to_i, body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Validate an existing monitor returns "OK" response
```
// Validate an existing monitor returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_monitors::MonitorsAPI;
use datadog_api_client::datadogV1::model::Monitor;
use datadog_api_client::datadogV1::model::MonitorOptions;
use datadog_api_client::datadogV1::model::MonitorOptionsNotificationPresets;
use datadog_api_client::datadogV1::model::MonitorThresholds;
use datadog_api_client::datadogV1::model::MonitorType;
use datadog_api_client::datadogV1::model::OnMissingDataOption;

#[tokio::main]
async fn main() {
    // there is a valid "monitor" in the system
    let monitor_id: i64 = std::env::var("MONITOR_ID").unwrap().parse().unwrap();
    let body =
        Monitor::new(
            r#"logs("service:foo AND type:error").index("main").rollup("count").by("source").last("5m") > 2"#.to_string(),
            MonitorType::LOG_ALERT,
        )
            .message("some message Notify: @hipchat-channel".to_string())
            .name("Example-Monitor".to_string())
            .options(
                MonitorOptions::new()
                    .enable_logs_sample(true)
                    .escalation_message("the situation has escalated".to_string())
                    .evaluation_delay(Some(700))
                    .include_tags(true)
                    .locked(false)
                    .new_host_delay(Some(600))
                    .no_data_timeframe(None)
                    .notification_preset_name(MonitorOptionsNotificationPresets::HIDE_HANDLES)
                    .notify_audit(false)
                    .notify_no_data(false)
                    .on_missing_data(OnMissingDataOption::SHOW_AND_NOTIFY_NO_DATA)
                    .renotify_interval(Some(60))
                    .require_full_window(true)
                    .thresholds(MonitorThresholds::new().critical(2.0 as f64).warning(Some(1.0 as f64)))
                    .timeout_h(Some(24)),
            )
            .priority(Some(3))
            .tags(vec!["test:examplemonitor".to_string(), "env:ci".to_string()]);
    let configuration = datadog::Configuration::new();
    let api = MonitorsAPI::with_config(configuration);
    let resp = api
        .validate_existing_monitor(monitor_id.clone(), body)
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

#####  Validate an existing monitor returns "OK" response
```
/**
 * Validate an existing monitor returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.MonitorsApi(configuration);

// there is a valid "monitor" in the system
const MONITOR_ID = parseInt(process.env.MONITOR_ID as string);

const params: v1.MonitorsApiValidateExistingMonitorRequest = {
  body: {
    name: "Example-Monitor",
    type: "log alert",
    query: `logs("service:foo AND type:error").index("main").rollup("count").by("source").last("5m") > 2`,
    message: "some message Notify: @hipchat-channel",
    tags: ["test:examplemonitor", "env:ci"],
    priority: 3,
    options: {
      enableLogsSample: true,
      escalationMessage: "the situation has escalated",
      evaluationDelay: 700,
      includeTags: true,
      locked: false,
      newHostDelay: 600,
      noDataTimeframe: undefined,
      notifyAudit: false,
      notifyNoData: false,
      onMissingData: "show_and_notify_no_data",
      notificationPresetName: "hide_handles",
      renotifyInterval: 60,
      requireFullWindow: true,
      timeoutH: 24,
      thresholds: {
        critical: 2,
        warning: 1,
      },
    },
  },
  monitorId: MONITOR_ID,
};

apiInstance
  .validateExistingMonitor(params)
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
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"


```

* * *
## [Get a monitor configuration policy](https://docs.datadoghq.com/api/latest/monitors/#get-a-monitor-configuration-policy)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/monitors/#get-a-monitor-configuration-policy-v2)


GET https://api.ap1.datadoghq.com/api/v2/monitor/policy/{policy_id}https://api.ap2.datadoghq.com/api/v2/monitor/policy/{policy_id}https://api.datadoghq.eu/api/v2/monitor/policy/{policy_id}https://api.ddog-gov.com/api/v2/monitor/policy/{policy_id}https://api.datadoghq.com/api/v2/monitor/policy/{policy_id}https://api.us3.datadoghq.com/api/v2/monitor/policy/{policy_id}https://api.us5.datadoghq.com/api/v2/monitor/policy/{policy_id}
### Overview
Get a monitor configuration policy by `policy_id`. This endpoint requires the `monitors_read` permission.
OAuth apps require the `monitors_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#monitors) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
policy_id [_required_]
string
ID of the monitor configuration policy.
### Response
  * [200](https://docs.datadoghq.com/api/latest/monitors/#GetMonitorConfigPolicy-200-v2)
  * [403](https://docs.datadoghq.com/api/latest/monitors/#GetMonitorConfigPolicy-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/monitors/#GetMonitorConfigPolicy-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/monitors/#GetMonitorConfigPolicy-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


Response for retrieving a monitor configuration policy.
Field
Type
Description
data
object
A monitor configuration policy data.
attributes
object
Policy and policy type for a monitor configuration policy.
policy
<oneOf>
Configuration for the policy.
Option 1
object
Tag attributes of a monitor configuration policy.
tag_key
string
The key of the tag.
tag_key_required
boolean
If a tag key is required for monitor creation.
valid_tag_values
[string]
Valid values for the tag.
policy_type
enum
The monitor configuration policy type. Allowed enum values: `tag`
default: `tag`
id
string
ID of this monitor configuration policy.
type
enum
Monitor configuration policy resource type. Allowed enum values: `monitor-config-policy`
default: `monitor-config-policy`
```
{
  "data": {
    "attributes": {
      "policy": {
        "tag_key": "datacenter",
        "tag_key_required": true,
        "valid_tag_values": [
          "prod",
          "staging"
        ]
      },
      "policy_type": "tag"
    },
    "id": "00000000-0000-1234-0000-000000000000",
    "type": "monitor-config-policy"
  }
}
```

Copy
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


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
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


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
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/monitors/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/monitors/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/monitors/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/monitors/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/monitors/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/monitors/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/monitors/?code-lang=typescript)


#####  Get a monitor configuration policy
Copy
```
                  # Path parameters  
export policy_id="00000000-0000-1234-0000-000000000000"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/monitor/policy/${policy_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get a monitor configuration policy
```
"""
Get a monitor configuration policy returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.monitors_api import MonitorsApi

# there is a valid "monitor_configuration_policy" in the system
MONITOR_CONFIGURATION_POLICY_DATA_ID = environ["MONITOR_CONFIGURATION_POLICY_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MonitorsApi(api_client)
    response = api_instance.get_monitor_config_policy(
        policy_id=MONITOR_CONFIGURATION_POLICY_DATA_ID,
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get a monitor configuration policy
```
# Get a monitor configuration policy returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::MonitorsAPI.new

# there is a valid "monitor_configuration_policy" in the system
MONITOR_CONFIGURATION_POLICY_DATA_ID = ENV["MONITOR_CONFIGURATION_POLICY_DATA_ID"]
p api_instance.get_monitor_config_policy(MONITOR_CONFIGURATION_POLICY_DATA_ID)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get a monitor configuration policy
```
// Get a monitor configuration policy returns "OK" response

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
	// there is a valid "monitor_configuration_policy" in the system
	MonitorConfigurationPolicyDataID := os.Getenv("MONITOR_CONFIGURATION_POLICY_DATA_ID")

	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewMonitorsApi(apiClient)
	resp, r, err := api.GetMonitorConfigPolicy(ctx, MonitorConfigurationPolicyDataID)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `MonitorsApi.GetMonitorConfigPolicy`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `MonitorsApi.GetMonitorConfigPolicy`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get a monitor configuration policy
```
// Get a monitor configuration policy returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.MonitorsApi;
import com.datadog.api.client.v2.model.MonitorConfigPolicyResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    MonitorsApi apiInstance = new MonitorsApi(defaultClient);

    // there is a valid "monitor_configuration_policy" in the system
    String MONITOR_CONFIGURATION_POLICY_DATA_ID =
        System.getenv("MONITOR_CONFIGURATION_POLICY_DATA_ID");

    try {
      MonitorConfigPolicyResponse result =
          apiInstance.getMonitorConfigPolicy(MONITOR_CONFIGURATION_POLICY_DATA_ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MonitorsApi#getMonitorConfigPolicy");
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

#####  Get a monitor configuration policy
```
// Get a monitor configuration policy returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_monitors::MonitorsAPI;

#[tokio::main]
async fn main() {
    // there is a valid "monitor_configuration_policy" in the system
    let monitor_configuration_policy_data_id =
        std::env::var("MONITOR_CONFIGURATION_POLICY_DATA_ID").unwrap();
    let configuration = datadog::Configuration::new();
    let api = MonitorsAPI::with_config(configuration);
    let resp = api
        .get_monitor_config_policy(monitor_configuration_policy_data_id.clone())
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

#####  Get a monitor configuration policy
```
/**
 * Get a monitor configuration policy returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.MonitorsApi(configuration);

// there is a valid "monitor_configuration_policy" in the system
const MONITOR_CONFIGURATION_POLICY_DATA_ID = process.env
  .MONITOR_CONFIGURATION_POLICY_DATA_ID as string;

const params: v2.MonitorsApiGetMonitorConfigPolicyRequest = {
  policyId: MONITOR_CONFIGURATION_POLICY_DATA_ID,
};

apiInstance
  .getMonitorConfigPolicy(params)
  .then((data: v2.MonitorConfigPolicyResponse) => {
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
## [Get all monitor configuration policies](https://docs.datadoghq.com/api/latest/monitors/#get-all-monitor-configuration-policies)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/monitors/#get-all-monitor-configuration-policies-v2)


GET https://api.ap1.datadoghq.com/api/v2/monitor/policyhttps://api.ap2.datadoghq.com/api/v2/monitor/policyhttps://api.datadoghq.eu/api/v2/monitor/policyhttps://api.ddog-gov.com/api/v2/monitor/policyhttps://api.datadoghq.com/api/v2/monitor/policyhttps://api.us3.datadoghq.com/api/v2/monitor/policyhttps://api.us5.datadoghq.com/api/v2/monitor/policy
### Overview
Get all monitor configuration policies. This endpoint requires the `monitors_read` permission.
OAuth apps require the `monitors_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#monitors) to access this endpoint.
### Response
  * [200](https://docs.datadoghq.com/api/latest/monitors/#ListMonitorConfigPolicies-200-v2)
  * [403](https://docs.datadoghq.com/api/latest/monitors/#ListMonitorConfigPolicies-403-v2)
  * [429](https://docs.datadoghq.com/api/latest/monitors/#ListMonitorConfigPolicies-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


Response for retrieving all monitor configuration policies.
Field
Type
Description
data
[object]
An array of monitor configuration policies.
attributes
object
Policy and policy type for a monitor configuration policy.
policy
<oneOf>
Configuration for the policy.
Option 1
object
Tag attributes of a monitor configuration policy.
tag_key
string
The key of the tag.
tag_key_required
boolean
If a tag key is required for monitor creation.
valid_tag_values
[string]
Valid values for the tag.
policy_type
enum
The monitor configuration policy type. Allowed enum values: `tag`
default: `tag`
id
string
ID of this monitor configuration policy.
type
enum
Monitor configuration policy resource type. Allowed enum values: `monitor-config-policy`
default: `monitor-config-policy`
```
{
  "data": [
    {
      "attributes": {
        "policy": {
          "tag_key": "datacenter",
          "tag_key_required": true,
          "valid_tag_values": [
            "prod",
            "staging"
          ]
        },
        "policy_type": "tag"
      },
      "id": "00000000-0000-1234-0000-000000000000",
      "type": "monitor-config-policy"
    }
  ]
}
```

Copy
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


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
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/monitors/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/monitors/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/monitors/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/monitors/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/monitors/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/monitors/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/monitors/?code-lang=typescript)


#####  Get all monitor configuration policies
Copy
```
                  # Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/monitor/policy" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get all monitor configuration policies
```
"""
Get all monitor configuration policies returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.monitors_api import MonitorsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MonitorsApi(api_client)
    response = api_instance.list_monitor_config_policies()

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get all monitor configuration policies
```
# Get all monitor configuration policies returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::MonitorsAPI.new
p api_instance.list_monitor_config_policies()

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get all monitor configuration policies
```
// Get all monitor configuration policies returns "OK" response

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
	api := datadogV2.NewMonitorsApi(apiClient)
	resp, r, err := api.ListMonitorConfigPolicies(ctx)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `MonitorsApi.ListMonitorConfigPolicies`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `MonitorsApi.ListMonitorConfigPolicies`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get all monitor configuration policies
```
// Get all monitor configuration policies returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.MonitorsApi;
import com.datadog.api.client.v2.model.MonitorConfigPolicyListResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    MonitorsApi apiInstance = new MonitorsApi(defaultClient);

    try {
      MonitorConfigPolicyListResponse result = apiInstance.listMonitorConfigPolicies();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MonitorsApi#listMonitorConfigPolicies");
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

#####  Get all monitor configuration policies
```
// Get all monitor configuration policies returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_monitors::MonitorsAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = MonitorsAPI::with_config(configuration);
    let resp = api.list_monitor_config_policies().await;
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

#####  Get all monitor configuration policies
```
/**
 * Get all monitor configuration policies returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.MonitorsApi(configuration);

apiInstance
  .listMonitorConfigPolicies()
  .then((data: v2.MonitorConfigPolicyListResponse) => {
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
## [Create a monitor configuration policy](https://docs.datadoghq.com/api/latest/monitors/#create-a-monitor-configuration-policy)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/monitors/#create-a-monitor-configuration-policy-v2)


POST https://api.ap1.datadoghq.com/api/v2/monitor/policyhttps://api.ap2.datadoghq.com/api/v2/monitor/policyhttps://api.datadoghq.eu/api/v2/monitor/policyhttps://api.ddog-gov.com/api/v2/monitor/policyhttps://api.datadoghq.com/api/v2/monitor/policyhttps://api.us3.datadoghq.com/api/v2/monitor/policyhttps://api.us5.datadoghq.com/api/v2/monitor/policy
### Overview
Create a monitor configuration policy. This endpoint requires the `monitor_config_policy_write` permission.
### Request
#### Body Data (required)
Create a monitor configuration policy request body.
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


Field
Type
Description
data [_required_]
object
A monitor configuration policy data.
attributes [_required_]
object
Policy and policy type for a monitor configuration policy.
policy [_required_]
<oneOf>
Configuration for the policy.
Option 1
object
Tag attributes of a monitor configuration policy.
tag_key [_required_]
string
The key of the tag.
tag_key_required [_required_]
boolean
If a tag key is required for monitor creation.
valid_tag_values [_required_]
[string]
Valid values for the tag.
policy_type [_required_]
enum
The monitor configuration policy type. Allowed enum values: `tag`
default: `tag`
type [_required_]
enum
Monitor configuration policy resource type. Allowed enum values: `monitor-config-policy`
default: `monitor-config-policy`
```
{
  "data": {
    "attributes": {
      "policy_type": "tag",
      "policy": {
        "tag_key": "examplemonitor",
        "tag_key_required": false,
        "valid_tag_values": [
          "prod",
          "staging"
        ]
      }
    },
    "type": "monitor-config-policy"
  }
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/monitors/#CreateMonitorConfigPolicy-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/monitors/#CreateMonitorConfigPolicy-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/monitors/#CreateMonitorConfigPolicy-403-v2)
  * [429](https://docs.datadoghq.com/api/latest/monitors/#CreateMonitorConfigPolicy-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


Response for retrieving a monitor configuration policy.
Field
Type
Description
data
object
A monitor configuration policy data.
attributes
object
Policy and policy type for a monitor configuration policy.
policy
<oneOf>
Configuration for the policy.
Option 1
object
Tag attributes of a monitor configuration policy.
tag_key
string
The key of the tag.
tag_key_required
boolean
If a tag key is required for monitor creation.
valid_tag_values
[string]
Valid values for the tag.
policy_type
enum
The monitor configuration policy type. Allowed enum values: `tag`
default: `tag`
id
string
ID of this monitor configuration policy.
type
enum
Monitor configuration policy resource type. Allowed enum values: `monitor-config-policy`
default: `monitor-config-policy`
```
{
  "data": {
    "attributes": {
      "policy": {
        "tag_key": "datacenter",
        "tag_key_required": true,
        "valid_tag_values": [
          "prod",
          "staging"
        ]
      },
      "policy_type": "tag"
    },
    "id": "00000000-0000-1234-0000-000000000000",
    "type": "monitor-config-policy"
  }
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


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
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


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
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/monitors/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/monitors/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/monitors/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/monitors/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/monitors/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/monitors/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/monitors/?code-lang=typescript)


#####  Create a monitor configuration policy returns "OK" response
Copy
```
                          # Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/monitor/policy" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "policy_type": "tag",
      "policy": {
        "tag_key": "examplemonitor",
        "tag_key_required": false,
        "valid_tag_values": [
          "prod",
          "staging"
        ]
      }
    },
    "type": "monitor-config-policy"
  }
}
EOF  

                        
```

#####  Create a monitor configuration policy returns "OK" response
```
// Create a monitor configuration policy returns "OK" response

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
	body := datadogV2.MonitorConfigPolicyCreateRequest{
		Data: datadogV2.MonitorConfigPolicyCreateData{
			Attributes: datadogV2.MonitorConfigPolicyAttributeCreateRequest{
				PolicyType: datadogV2.MONITORCONFIGPOLICYTYPE_TAG,
				Policy: datadogV2.MonitorConfigPolicyPolicyCreateRequest{
					MonitorConfigPolicyTagPolicyCreateRequest: &datadogV2.MonitorConfigPolicyTagPolicyCreateRequest{
						TagKey:         "examplemonitor",
						TagKeyRequired: false,
						ValidTagValues: []string{
							"prod",
							"staging",
						},
					}},
			},
			Type: datadogV2.MONITORCONFIGPOLICYRESOURCETYPE_MONITOR_CONFIG_POLICY,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewMonitorsApi(apiClient)
	resp, r, err := api.CreateMonitorConfigPolicy(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `MonitorsApi.CreateMonitorConfigPolicy`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `MonitorsApi.CreateMonitorConfigPolicy`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Create a monitor configuration policy returns "OK" response
```
// Create a monitor configuration policy returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.MonitorsApi;
import com.datadog.api.client.v2.model.MonitorConfigPolicyAttributeCreateRequest;
import com.datadog.api.client.v2.model.MonitorConfigPolicyCreateData;
import com.datadog.api.client.v2.model.MonitorConfigPolicyCreateRequest;
import com.datadog.api.client.v2.model.MonitorConfigPolicyPolicyCreateRequest;
import com.datadog.api.client.v2.model.MonitorConfigPolicyResourceType;
import com.datadog.api.client.v2.model.MonitorConfigPolicyResponse;
import com.datadog.api.client.v2.model.MonitorConfigPolicyTagPolicyCreateRequest;
import com.datadog.api.client.v2.model.MonitorConfigPolicyType;
import java.util.Arrays;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    MonitorsApi apiInstance = new MonitorsApi(defaultClient);

    MonitorConfigPolicyCreateRequest body =
        new MonitorConfigPolicyCreateRequest()
            .data(
                new MonitorConfigPolicyCreateData()
                    .attributes(
                        new MonitorConfigPolicyAttributeCreateRequest()
                            .policyType(MonitorConfigPolicyType.TAG)
                            .policy(
                                new MonitorConfigPolicyPolicyCreateRequest(
                                    new MonitorConfigPolicyTagPolicyCreateRequest()
                                        .tagKey("examplemonitor")
                                        .tagKeyRequired(false)
                                        .validTagValues(Arrays.asList("prod", "staging")))))
                    .type(MonitorConfigPolicyResourceType.MONITOR_CONFIG_POLICY));

    try {
      MonitorConfigPolicyResponse result = apiInstance.createMonitorConfigPolicy(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MonitorsApi#createMonitorConfigPolicy");
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

#####  Create a monitor configuration policy returns "OK" response
```
"""
Create a monitor configuration policy returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.monitors_api import MonitorsApi
from datadog_api_client.v2.model.monitor_config_policy_attribute_create_request import (
    MonitorConfigPolicyAttributeCreateRequest,
)
from datadog_api_client.v2.model.monitor_config_policy_create_data import MonitorConfigPolicyCreateData
from datadog_api_client.v2.model.monitor_config_policy_create_request import MonitorConfigPolicyCreateRequest
from datadog_api_client.v2.model.monitor_config_policy_resource_type import MonitorConfigPolicyResourceType
from datadog_api_client.v2.model.monitor_config_policy_tag_policy_create_request import (
    MonitorConfigPolicyTagPolicyCreateRequest,
)
from datadog_api_client.v2.model.monitor_config_policy_type import MonitorConfigPolicyType

body = MonitorConfigPolicyCreateRequest(
    data=MonitorConfigPolicyCreateData(
        attributes=MonitorConfigPolicyAttributeCreateRequest(
            policy_type=MonitorConfigPolicyType.TAG,
            policy=MonitorConfigPolicyTagPolicyCreateRequest(
                tag_key="examplemonitor",
                tag_key_required=False,
                valid_tag_values=[
                    "prod",
                    "staging",
                ],
            ),
        ),
        type=MonitorConfigPolicyResourceType.MONITOR_CONFIG_POLICY,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MonitorsApi(api_client)
    response = api_instance.create_monitor_config_policy(body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Create a monitor configuration policy returns "OK" response
```
# Create a monitor configuration policy returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::MonitorsAPI.new

body = DatadogAPIClient::V2::MonitorConfigPolicyCreateRequest.new({
  data: DatadogAPIClient::V2::MonitorConfigPolicyCreateData.new({
    attributes: DatadogAPIClient::V2::MonitorConfigPolicyAttributeCreateRequest.new({
      policy_type: DatadogAPIClient::V2::MonitorConfigPolicyType::TAG,
      policy: DatadogAPIClient::V2::MonitorConfigPolicyTagPolicyCreateRequest.new({
        tag_key: "examplemonitor",
        tag_key_required: false,
        valid_tag_values: [
          "prod",
          "staging",
        ],
      }),
    }),
    type: DatadogAPIClient::V2::MonitorConfigPolicyResourceType::MONITOR_CONFIG_POLICY,
  }),
})
p api_instance.create_monitor_config_policy(body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Create a monitor configuration policy returns "OK" response
```
// Create a monitor configuration policy returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_monitors::MonitorsAPI;
use datadog_api_client::datadogV2::model::MonitorConfigPolicyAttributeCreateRequest;
use datadog_api_client::datadogV2::model::MonitorConfigPolicyCreateData;
use datadog_api_client::datadogV2::model::MonitorConfigPolicyCreateRequest;
use datadog_api_client::datadogV2::model::MonitorConfigPolicyPolicyCreateRequest;
use datadog_api_client::datadogV2::model::MonitorConfigPolicyResourceType;
use datadog_api_client::datadogV2::model::MonitorConfigPolicyTagPolicyCreateRequest;
use datadog_api_client::datadogV2::model::MonitorConfigPolicyType;

#[tokio::main]
async fn main() {
    let body = MonitorConfigPolicyCreateRequest::new(MonitorConfigPolicyCreateData::new(
        MonitorConfigPolicyAttributeCreateRequest::new(
            MonitorConfigPolicyPolicyCreateRequest::MonitorConfigPolicyTagPolicyCreateRequest(
                Box::new(MonitorConfigPolicyTagPolicyCreateRequest::new(
                    "examplemonitor".to_string(),
                    false,
                    vec!["prod".to_string(), "staging".to_string()],
                )),
            ),
            MonitorConfigPolicyType::TAG,
        ),
        MonitorConfigPolicyResourceType::MONITOR_CONFIG_POLICY,
    ));
    let configuration = datadog::Configuration::new();
    let api = MonitorsAPI::with_config(configuration);
    let resp = api.create_monitor_config_policy(body).await;
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

#####  Create a monitor configuration policy returns "OK" response
```
/**
 * Create a monitor configuration policy returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.MonitorsApi(configuration);

const params: v2.MonitorsApiCreateMonitorConfigPolicyRequest = {
  body: {
    data: {
      attributes: {
        policyType: "tag",
        policy: {
          tagKey: "examplemonitor",
          tagKeyRequired: false,
          validTagValues: ["prod", "staging"],
        },
      },
      type: "monitor-config-policy",
    },
  },
};

apiInstance
  .createMonitorConfigPolicy(params)
  .then((data: v2.MonitorConfigPolicyResponse) => {
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
## [Edit a monitor configuration policy](https://docs.datadoghq.com/api/latest/monitors/#edit-a-monitor-configuration-policy)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/monitors/#edit-a-monitor-configuration-policy-v2)


PATCH https://api.ap1.datadoghq.com/api/v2/monitor/policy/{policy_id}https://api.ap2.datadoghq.com/api/v2/monitor/policy/{policy_id}https://api.datadoghq.eu/api/v2/monitor/policy/{policy_id}https://api.ddog-gov.com/api/v2/monitor/policy/{policy_id}https://api.datadoghq.com/api/v2/monitor/policy/{policy_id}https://api.us3.datadoghq.com/api/v2/monitor/policy/{policy_id}https://api.us5.datadoghq.com/api/v2/monitor/policy/{policy_id}
### Overview
Edit a monitor configuration policy. This endpoint requires the `monitor_config_policy_write` permission.
### Arguments
#### Path Parameters
Name
Type
Description
policy_id [_required_]
string
ID of the monitor configuration policy.
### Request
#### Body Data (required)
Description of the update.
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


Field
Type
Description
data [_required_]
object
A monitor configuration policy data.
attributes [_required_]
object
Policy and policy type for a monitor configuration policy.
policy [_required_]
<oneOf>
Configuration for the policy.
Option 1
object
Tag attributes of a monitor configuration policy.
tag_key
string
The key of the tag.
tag_key_required
boolean
If a tag key is required for monitor creation.
valid_tag_values
[string]
Valid values for the tag.
policy_type [_required_]
enum
The monitor configuration policy type. Allowed enum values: `tag`
default: `tag`
id [_required_]
string
ID of this monitor configuration policy.
type [_required_]
enum
Monitor configuration policy resource type. Allowed enum values: `monitor-config-policy`
default: `monitor-config-policy`
```
{
  "data": {
    "attributes": {
      "policy": {
        "tag_key": "examplemonitor",
        "tag_key_required": false,
        "valid_tag_values": [
          "prod",
          "staging"
        ]
      },
      "policy_type": "tag"
    },
    "id": "00000000-0000-1234-0000-000000000000",
    "type": "monitor-config-policy"
  }
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/monitors/#UpdateMonitorConfigPolicy-200-v2)
  * [403](https://docs.datadoghq.com/api/latest/monitors/#UpdateMonitorConfigPolicy-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/monitors/#UpdateMonitorConfigPolicy-404-v2)
  * [422](https://docs.datadoghq.com/api/latest/monitors/#UpdateMonitorConfigPolicy-422-v2)
  * [429](https://docs.datadoghq.com/api/latest/monitors/#UpdateMonitorConfigPolicy-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


Response for retrieving a monitor configuration policy.
Field
Type
Description
data
object
A monitor configuration policy data.
attributes
object
Policy and policy type for a monitor configuration policy.
policy
<oneOf>
Configuration for the policy.
Option 1
object
Tag attributes of a monitor configuration policy.
tag_key
string
The key of the tag.
tag_key_required
boolean
If a tag key is required for monitor creation.
valid_tag_values
[string]
Valid values for the tag.
policy_type
enum
The monitor configuration policy type. Allowed enum values: `tag`
default: `tag`
id
string
ID of this monitor configuration policy.
type
enum
Monitor configuration policy resource type. Allowed enum values: `monitor-config-policy`
default: `monitor-config-policy`
```
{
  "data": {
    "attributes": {
      "policy": {
        "tag_key": "datacenter",
        "tag_key_required": true,
        "valid_tag_values": [
          "prod",
          "staging"
        ]
      },
      "policy_type": "tag"
    },
    "id": "00000000-0000-1234-0000-000000000000",
    "type": "monitor-config-policy"
  }
}
```

Copy
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


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
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


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
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


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
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/monitors/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/monitors/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/monitors/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/monitors/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/monitors/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/monitors/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/monitors/?code-lang=typescript)


#####  Edit a monitor configuration policy returns "OK" response
Copy
```
                          # Path parameters  
export policy_id="00000000-0000-1234-0000-000000000000"  
# Curl command  
curl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/monitor/policy/${policy_id}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "policy": {
        "tag_key": "examplemonitor",
        "tag_key_required": false,
        "valid_tag_values": [
          "prod",
          "staging"
        ]
      },
      "policy_type": "tag"
    },
    "id": "00000000-0000-1234-0000-000000000000",
    "type": "monitor-config-policy"
  }
}
EOF  

                        
```

#####  Edit a monitor configuration policy returns "OK" response
```
// Edit a monitor configuration policy returns "OK" response

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
	// there is a valid "monitor_configuration_policy" in the system
	MonitorConfigurationPolicyDataID := os.Getenv("MONITOR_CONFIGURATION_POLICY_DATA_ID")

	body := datadogV2.MonitorConfigPolicyEditRequest{
		Data: datadogV2.MonitorConfigPolicyEditData{
			Attributes: datadogV2.MonitorConfigPolicyAttributeEditRequest{
				Policy: datadogV2.MonitorConfigPolicyPolicy{
					MonitorConfigPolicyTagPolicy: &datadogV2.MonitorConfigPolicyTagPolicy{
						TagKey:         datadog.PtrString("examplemonitor"),
						TagKeyRequired: datadog.PtrBool(false),
						ValidTagValues: []string{
							"prod",
							"staging",
						},
					}},
				PolicyType: datadogV2.MONITORCONFIGPOLICYTYPE_TAG,
			},
			Id:   MonitorConfigurationPolicyDataID,
			Type: datadogV2.MONITORCONFIGPOLICYRESOURCETYPE_MONITOR_CONFIG_POLICY,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewMonitorsApi(apiClient)
	resp, r, err := api.UpdateMonitorConfigPolicy(ctx, MonitorConfigurationPolicyDataID, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `MonitorsApi.UpdateMonitorConfigPolicy`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `MonitorsApi.UpdateMonitorConfigPolicy`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Edit a monitor configuration policy returns "OK" response
```
// Edit a monitor configuration policy returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.MonitorsApi;
import com.datadog.api.client.v2.model.MonitorConfigPolicyAttributeEditRequest;
import com.datadog.api.client.v2.model.MonitorConfigPolicyEditData;
import com.datadog.api.client.v2.model.MonitorConfigPolicyEditRequest;
import com.datadog.api.client.v2.model.MonitorConfigPolicyPolicy;
import com.datadog.api.client.v2.model.MonitorConfigPolicyResourceType;
import com.datadog.api.client.v2.model.MonitorConfigPolicyResponse;
import com.datadog.api.client.v2.model.MonitorConfigPolicyTagPolicy;
import com.datadog.api.client.v2.model.MonitorConfigPolicyType;
import java.util.Arrays;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    MonitorsApi apiInstance = new MonitorsApi(defaultClient);

    // there is a valid "monitor_configuration_policy" in the system
    String MONITOR_CONFIGURATION_POLICY_DATA_ID =
        System.getenv("MONITOR_CONFIGURATION_POLICY_DATA_ID");

    MonitorConfigPolicyEditRequest body =
        new MonitorConfigPolicyEditRequest()
            .data(
                new MonitorConfigPolicyEditData()
                    .attributes(
                        new MonitorConfigPolicyAttributeEditRequest()
                            .policy(
                                new MonitorConfigPolicyPolicy(
                                    new MonitorConfigPolicyTagPolicy()
                                        .tagKey("examplemonitor")
                                        .tagKeyRequired(false)
                                        .validTagValues(Arrays.asList("prod", "staging"))))
                            .policyType(MonitorConfigPolicyType.TAG))
                    .id(MONITOR_CONFIGURATION_POLICY_DATA_ID)
                    .type(MonitorConfigPolicyResourceType.MONITOR_CONFIG_POLICY));

    try {
      MonitorConfigPolicyResponse result =
          apiInstance.updateMonitorConfigPolicy(MONITOR_CONFIGURATION_POLICY_DATA_ID, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MonitorsApi#updateMonitorConfigPolicy");
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

#####  Edit a monitor configuration policy returns "OK" response
```
"""
Edit a monitor configuration policy returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.monitors_api import MonitorsApi
from datadog_api_client.v2.model.monitor_config_policy_attribute_edit_request import (
    MonitorConfigPolicyAttributeEditRequest,
)
from datadog_api_client.v2.model.monitor_config_policy_edit_data import MonitorConfigPolicyEditData
from datadog_api_client.v2.model.monitor_config_policy_edit_request import MonitorConfigPolicyEditRequest
from datadog_api_client.v2.model.monitor_config_policy_resource_type import MonitorConfigPolicyResourceType
from datadog_api_client.v2.model.monitor_config_policy_tag_policy import MonitorConfigPolicyTagPolicy
from datadog_api_client.v2.model.monitor_config_policy_type import MonitorConfigPolicyType

# there is a valid "monitor_configuration_policy" in the system
MONITOR_CONFIGURATION_POLICY_DATA_ID = environ["MONITOR_CONFIGURATION_POLICY_DATA_ID"]

body = MonitorConfigPolicyEditRequest(
    data=MonitorConfigPolicyEditData(
        attributes=MonitorConfigPolicyAttributeEditRequest(
            policy=MonitorConfigPolicyTagPolicy(
                tag_key="examplemonitor",
                tag_key_required=False,
                valid_tag_values=[
                    "prod",
                    "staging",
                ],
            ),
            policy_type=MonitorConfigPolicyType.TAG,
        ),
        id=MONITOR_CONFIGURATION_POLICY_DATA_ID,
        type=MonitorConfigPolicyResourceType.MONITOR_CONFIG_POLICY,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MonitorsApi(api_client)
    response = api_instance.update_monitor_config_policy(policy_id=MONITOR_CONFIGURATION_POLICY_DATA_ID, body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Edit a monitor configuration policy returns "OK" response
```
# Edit a monitor configuration policy returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::MonitorsAPI.new

# there is a valid "monitor_configuration_policy" in the system
MONITOR_CONFIGURATION_POLICY_DATA_ID = ENV["MONITOR_CONFIGURATION_POLICY_DATA_ID"]

body = DatadogAPIClient::V2::MonitorConfigPolicyEditRequest.new({
  data: DatadogAPIClient::V2::MonitorConfigPolicyEditData.new({
    attributes: DatadogAPIClient::V2::MonitorConfigPolicyAttributeEditRequest.new({
      policy: DatadogAPIClient::V2::MonitorConfigPolicyTagPolicy.new({
        tag_key: "examplemonitor",
        tag_key_required: false,
        valid_tag_values: [
          "prod",
          "staging",
        ],
      }),
      policy_type: DatadogAPIClient::V2::MonitorConfigPolicyType::TAG,
    }),
    id: MONITOR_CONFIGURATION_POLICY_DATA_ID,
    type: DatadogAPIClient::V2::MonitorConfigPolicyResourceType::MONITOR_CONFIG_POLICY,
  }),
})
p api_instance.update_monitor_config_policy(MONITOR_CONFIGURATION_POLICY_DATA_ID, body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Edit a monitor configuration policy returns "OK" response
```
// Edit a monitor configuration policy returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_monitors::MonitorsAPI;
use datadog_api_client::datadogV2::model::MonitorConfigPolicyAttributeEditRequest;
use datadog_api_client::datadogV2::model::MonitorConfigPolicyEditData;
use datadog_api_client::datadogV2::model::MonitorConfigPolicyEditRequest;
use datadog_api_client::datadogV2::model::MonitorConfigPolicyPolicy;
use datadog_api_client::datadogV2::model::MonitorConfigPolicyResourceType;
use datadog_api_client::datadogV2::model::MonitorConfigPolicyTagPolicy;
use datadog_api_client::datadogV2::model::MonitorConfigPolicyType;

#[tokio::main]
async fn main() {
    // there is a valid "monitor_configuration_policy" in the system
    let monitor_configuration_policy_data_id =
        std::env::var("MONITOR_CONFIGURATION_POLICY_DATA_ID").unwrap();
    let body = MonitorConfigPolicyEditRequest::new(MonitorConfigPolicyEditData::new(
        MonitorConfigPolicyAttributeEditRequest::new(
            MonitorConfigPolicyPolicy::MonitorConfigPolicyTagPolicy(Box::new(
                MonitorConfigPolicyTagPolicy::new()
                    .tag_key("examplemonitor".to_string())
                    .tag_key_required(false)
                    .valid_tag_values(vec!["prod".to_string(), "staging".to_string()]),
            )),
            MonitorConfigPolicyType::TAG,
        ),
        monitor_configuration_policy_data_id.clone(),
        MonitorConfigPolicyResourceType::MONITOR_CONFIG_POLICY,
    ));
    let configuration = datadog::Configuration::new();
    let api = MonitorsAPI::with_config(configuration);
    let resp = api
        .update_monitor_config_policy(monitor_configuration_policy_data_id.clone(), body)
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

#####  Edit a monitor configuration policy returns "OK" response
```
/**
 * Edit a monitor configuration policy returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.MonitorsApi(configuration);

// there is a valid "monitor_configuration_policy" in the system
const MONITOR_CONFIGURATION_POLICY_DATA_ID = process.env
  .MONITOR_CONFIGURATION_POLICY_DATA_ID as string;

const params: v2.MonitorsApiUpdateMonitorConfigPolicyRequest = {
  body: {
    data: {
      attributes: {
        policy: {
          tagKey: "examplemonitor",
          tagKeyRequired: false,
          validTagValues: ["prod", "staging"],
        },
        policyType: "tag",
      },
      id: MONITOR_CONFIGURATION_POLICY_DATA_ID,
      type: "monitor-config-policy",
    },
  },
  policyId: MONITOR_CONFIGURATION_POLICY_DATA_ID,
};

apiInstance
  .updateMonitorConfigPolicy(params)
  .then((data: v2.MonitorConfigPolicyResponse) => {
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
## [Delete a monitor configuration policy](https://docs.datadoghq.com/api/latest/monitors/#delete-a-monitor-configuration-policy)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/monitors/#delete-a-monitor-configuration-policy-v2)


DELETE https://api.ap1.datadoghq.com/api/v2/monitor/policy/{policy_id}https://api.ap2.datadoghq.com/api/v2/monitor/policy/{policy_id}https://api.datadoghq.eu/api/v2/monitor/policy/{policy_id}https://api.ddog-gov.com/api/v2/monitor/policy/{policy_id}https://api.datadoghq.com/api/v2/monitor/policy/{policy_id}https://api.us3.datadoghq.com/api/v2/monitor/policy/{policy_id}https://api.us5.datadoghq.com/api/v2/monitor/policy/{policy_id}
### Overview
Delete a monitor configuration policy. This endpoint requires the `monitor_config_policy_write` permission.
### Arguments
#### Path Parameters
Name
Type
Description
policy_id [_required_]
string
ID of the monitor configuration policy.
### Response
  * [204](https://docs.datadoghq.com/api/latest/monitors/#DeleteMonitorConfigPolicy-204-v2)
  * [400](https://docs.datadoghq.com/api/latest/monitors/#DeleteMonitorConfigPolicy-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/monitors/#DeleteMonitorConfigPolicy-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/monitors/#DeleteMonitorConfigPolicy-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/monitors/#DeleteMonitorConfigPolicy-429-v2)


OK
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


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
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


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
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


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
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/monitors/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/monitors/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/monitors/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/monitors/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/monitors/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/monitors/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/monitors/?code-lang=typescript)


#####  Delete a monitor configuration policy
Copy
```
                  # Path parameters  
export policy_id="00000000-0000-1234-0000-000000000000"  
# Curl command  
curl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/monitor/policy/${policy_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Delete a monitor configuration policy
```
"""
Delete a monitor configuration policy returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.monitors_api import MonitorsApi

# there is a valid "monitor_configuration_policy" in the system
MONITOR_CONFIGURATION_POLICY_DATA_ID = environ["MONITOR_CONFIGURATION_POLICY_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MonitorsApi(api_client)
    api_instance.delete_monitor_config_policy(
        policy_id=MONITOR_CONFIGURATION_POLICY_DATA_ID,
    )

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Delete a monitor configuration policy
```
# Delete a monitor configuration policy returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::MonitorsAPI.new

# there is a valid "monitor_configuration_policy" in the system
MONITOR_CONFIGURATION_POLICY_DATA_ID = ENV["MONITOR_CONFIGURATION_POLICY_DATA_ID"]
api_instance.delete_monitor_config_policy(MONITOR_CONFIGURATION_POLICY_DATA_ID)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Delete a monitor configuration policy
```
// Delete a monitor configuration policy returns "OK" response

package main

import (
	"context"
	"fmt"
	"os"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
	// there is a valid "monitor_configuration_policy" in the system
	MonitorConfigurationPolicyDataID := os.Getenv("MONITOR_CONFIGURATION_POLICY_DATA_ID")

	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewMonitorsApi(apiClient)
	r, err := api.DeleteMonitorConfigPolicy(ctx, MonitorConfigurationPolicyDataID)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `MonitorsApi.DeleteMonitorConfigPolicy`: %v\n", err)
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

#####  Delete a monitor configuration policy
```
// Delete a monitor configuration policy returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.MonitorsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    MonitorsApi apiInstance = new MonitorsApi(defaultClient);

    // there is a valid "monitor_configuration_policy" in the system
    String MONITOR_CONFIGURATION_POLICY_DATA_ID =
        System.getenv("MONITOR_CONFIGURATION_POLICY_DATA_ID");

    try {
      apiInstance.deleteMonitorConfigPolicy(MONITOR_CONFIGURATION_POLICY_DATA_ID);
    } catch (ApiException e) {
      System.err.println("Exception when calling MonitorsApi#deleteMonitorConfigPolicy");
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

#####  Delete a monitor configuration policy
```
// Delete a monitor configuration policy returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_monitors::MonitorsAPI;

#[tokio::main]
async fn main() {
    // there is a valid "monitor_configuration_policy" in the system
    let monitor_configuration_policy_data_id =
        std::env::var("MONITOR_CONFIGURATION_POLICY_DATA_ID").unwrap();
    let configuration = datadog::Configuration::new();
    let api = MonitorsAPI::with_config(configuration);
    let resp = api
        .delete_monitor_config_policy(monitor_configuration_policy_data_id.clone())
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

#####  Delete a monitor configuration policy
```
/**
 * Delete a monitor configuration policy returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.MonitorsApi(configuration);

// there is a valid "monitor_configuration_policy" in the system
const MONITOR_CONFIGURATION_POLICY_DATA_ID = process.env
  .MONITOR_CONFIGURATION_POLICY_DATA_ID as string;

const params: v2.MonitorsApiDeleteMonitorConfigPolicyRequest = {
  policyId: MONITOR_CONFIGURATION_POLICY_DATA_ID,
};

apiInstance
  .deleteMonitorConfigPolicy(params)
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
## [Get a monitor notification rule](https://docs.datadoghq.com/api/latest/monitors/#get-a-monitor-notification-rule)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/monitors/#get-a-monitor-notification-rule-v2)


GET https://api.ap1.datadoghq.com/api/v2/monitor/notification_rule/{rule_id}https://api.ap2.datadoghq.com/api/v2/monitor/notification_rule/{rule_id}https://api.datadoghq.eu/api/v2/monitor/notification_rule/{rule_id}https://api.ddog-gov.com/api/v2/monitor/notification_rule/{rule_id}https://api.datadoghq.com/api/v2/monitor/notification_rule/{rule_id}https://api.us3.datadoghq.com/api/v2/monitor/notification_rule/{rule_id}https://api.us5.datadoghq.com/api/v2/monitor/notification_rule/{rule_id}
### Overview
Returns a monitor notification rule by `rule_id`. This endpoint requires the `monitors_read` permission.
OAuth apps require the `monitors_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#monitors) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
rule_id [_required_]
string
ID of the monitor notification rule to fetch.
#### Query Strings
Name
Type
Description
include
string
Comma-separated list of resource paths for related resources to include in the response. Supported resource path is `created_by`.
### Response
  * [200](https://docs.datadoghq.com/api/latest/monitors/#GetMonitorNotificationRule-200-v2)
  * [403](https://docs.datadoghq.com/api/latest/monitors/#GetMonitorNotificationRule-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/monitors/#GetMonitorNotificationRule-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/monitors/#GetMonitorNotificationRule-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


A monitor notification rule.
Field
Type
Description
data
object
Monitor notification rule data.
attributes
object
Attributes of the monitor notification rule.
conditional_recipients
object
Use conditional recipients to define different recipients for different situations. Cannot be used with `recipients`.
conditions [_required_]
[object]
Conditions of the notification rule.
recipients [_required_]
[string]
A list of recipients to notify. Uses the same format as the monitor `message` field. Must not start with an '@'.
scope [_required_]
string
The scope to which the monitor applied.
fallback_recipients
[string]
If none of the `conditions` applied, `fallback_recipients` will get notified.
created
date-time
Creation time of the monitor notification rule.
filter
<oneOf>
Filter used to associate the notification rule with monitors.
Option 1
object
Filter monitor notifications by tags. A monitor notification must match all tags.
tags [_required_]
[string]
A list of tags (key:value pairs), which can be used to filter monitor notifications on monitor and group tags.
Option 2
object
Filter monitor notifications. A monitor notification must match the scope.
scope [_required_]
string
A scope composed of one or several key:value pairs, which can be used to filter monitor notifications on monitor and group tags.
modified
date-time
Time the monitor notification rule was last modified.
name
string
The name of the monitor notification rule.
recipients
[string]
A list of recipients to notify. Uses the same format as the monitor `message` field. Must not start with an '@'. Cannot be used with `conditional_recipients`.
id
string
The ID of the monitor notification rule.
relationships
object
All relationships associated with monitor notification rule.
created_by
object
The user who created the monitor notification rule.
data
object
Data for the user who created the monitor notification rule.
id
string
User ID of the monitor notification rule creator.
type
enum
Users resource type. Allowed enum values: `users`
default: `users`
type
enum
Monitor notification rule resource type. Allowed enum values: `monitor-notification-rule`
default: `monitor-notification-rule`
included
[ <oneOf>]
Array of objects related to the monitor notification rule that the user requested.
Option 1
object
User object returned by the API.
attributes
object
Attributes of user object returned by the API.
created_at
date-time
Creation time of the user.
disabled
boolean
Whether the user is disabled.
email
string
Email of the user.
handle
string
Handle of the user.
icon
string
URL of the user's icon.
last_login_time
date-time
The last time the user logged in.
mfa_enabled
boolean
If user has MFA enabled.
modified_at
date-time
Time that the user was last modified.
name
string
Name of the user.
service_account
boolean
Whether the user is a service account.
status
string
Status of the user.
title
string
Title of the user.
verified
boolean
Whether the user is verified.
id
string
ID of the user.
relationships
object
Relationships of the user object returned by the API.
org
object
Relationship to an organization.
data [_required_]
object
Relationship to organization object.
id [_required_]
string
ID of the organization.
type [_required_]
enum
Organizations resource type. Allowed enum values: `orgs`
default: `orgs`
other_orgs
object
Relationship to organizations.
data [_required_]
[object]
Relationships to organization objects.
id [_required_]
string
ID of the organization.
type [_required_]
enum
Organizations resource type. Allowed enum values: `orgs`
default: `orgs`
other_users
object
Relationship to users.
data [_required_]
[object]
Relationships to user objects.
id [_required_]
string
A unique identifier that represents the user.
type [_required_]
enum
Users resource type. Allowed enum values: `users`
default: `users`
roles
object
Relationship to roles.
data
[object]
An array containing type and the unique identifier of a role.
id
string
The unique identifier of the role.
type
enum
Roles type. Allowed enum values: `roles`
default: `roles`
type
enum
Users resource type. Allowed enum values: `users`
default: `users`
```
{
  "data": {
    "attributes": {
      "conditional_recipients": {
        "conditions": [
          {
            "recipients": [
              "slack-test-channel",
              "jira-test"
            ],
            "scope": "transition_type:alert"
          }
        ],
        "fallback_recipients": [
          "slack-test-channel",
          "jira-test"
        ]
      },
      "created": "2020-01-02T03:04:00.000Z",
      "filter": {
        "tags": [
          "team:product",
          "host:abc"
        ]
      },
      "modified": "2020-01-02T03:04:00.000Z",
      "name": "A notification rule name",
      "recipients": [
        "slack-test-channel",
        "jira-test"
      ]
    },
    "id": "00000000-0000-1234-0000-000000000000",
    "relationships": {
      "created_by": {
        "data": {
          "id": "00000000-0000-1234-0000-000000000000",
          "type": "users"
        }
      }
    },
    "type": "monitor-notification-rule"
  },
  "included": [
    {
      "attributes": {
        "created_at": "2019-09-19T10:00:00.000Z",
        "disabled": false,
        "email": "string",
        "handle": "string",
        "icon": "string",
        "last_login_time": "2019-09-19T10:00:00.000Z",
        "mfa_enabled": false,
        "modified_at": "2019-09-19T10:00:00.000Z",
        "name": "string",
        "service_account": false,
        "status": "string",
        "title": "string",
        "verified": false
      },
      "id": "string",
      "relationships": {
        "org": {
          "data": {
            "id": "00000000-0000-beef-0000-000000000000",
            "type": "orgs"
          }
        },
        "other_orgs": {
          "data": [
            {
              "id": "00000000-0000-beef-0000-000000000000",
              "type": "orgs"
            }
          ]
        },
        "other_users": {
          "data": [
            {
              "id": "00000000-0000-0000-2345-000000000000",
              "type": "users"
            }
          ]
        },
        "roles": {
          "data": [
            {
              "id": "3653d3c6-0c75-11ea-ad28-fb5701eabc7d",
              "type": "roles"
            }
          ]
        }
      },
      "type": "users"
    }
  ]
}
```

Copy
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


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
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


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
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/monitors/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/monitors/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/monitors/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/monitors/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/monitors/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/monitors/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/monitors/?code-lang=typescript)


#####  Get a monitor notification rule
Copy
```
                  # Path parameters  
export rule_id="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/monitor/notification_rule/${rule_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get a monitor notification rule
```
"""
Get a monitor notification rule returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.monitors_api import MonitorsApi

# there is a valid "monitor_notification_rule" in the system
MONITOR_NOTIFICATION_RULE_DATA_ID = environ["MONITOR_NOTIFICATION_RULE_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MonitorsApi(api_client)
    response = api_instance.get_monitor_notification_rule(
        rule_id=MONITOR_NOTIFICATION_RULE_DATA_ID,
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get a monitor notification rule
```
# Get a monitor notification rule returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::MonitorsAPI.new

# there is a valid "monitor_notification_rule" in the system
MONITOR_NOTIFICATION_RULE_DATA_ID = ENV["MONITOR_NOTIFICATION_RULE_DATA_ID"]
p api_instance.get_monitor_notification_rule(MONITOR_NOTIFICATION_RULE_DATA_ID)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get a monitor notification rule
```
// Get a monitor notification rule returns "OK" response

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
	// there is a valid "monitor_notification_rule" in the system
	MonitorNotificationRuleDataID := os.Getenv("MONITOR_NOTIFICATION_RULE_DATA_ID")

	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewMonitorsApi(apiClient)
	resp, r, err := api.GetMonitorNotificationRule(ctx, MonitorNotificationRuleDataID, *datadogV2.NewGetMonitorNotificationRuleOptionalParameters())

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `MonitorsApi.GetMonitorNotificationRule`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `MonitorsApi.GetMonitorNotificationRule`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get a monitor notification rule
```
// Get a monitor notification rule returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.MonitorsApi;
import com.datadog.api.client.v2.model.MonitorNotificationRuleResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    MonitorsApi apiInstance = new MonitorsApi(defaultClient);

    // there is a valid "monitor_notification_rule" in the system
    String MONITOR_NOTIFICATION_RULE_DATA_ID = System.getenv("MONITOR_NOTIFICATION_RULE_DATA_ID");

    try {
      MonitorNotificationRuleResponse result =
          apiInstance.getMonitorNotificationRule(MONITOR_NOTIFICATION_RULE_DATA_ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MonitorsApi#getMonitorNotificationRule");
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

#####  Get a monitor notification rule
```
// Get a monitor notification rule returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_monitors::GetMonitorNotificationRuleOptionalParams;
use datadog_api_client::datadogV2::api_monitors::MonitorsAPI;

#[tokio::main]
async fn main() {
    // there is a valid "monitor_notification_rule" in the system
    let monitor_notification_rule_data_id =
        std::env::var("MONITOR_NOTIFICATION_RULE_DATA_ID").unwrap();
    let configuration = datadog::Configuration::new();
    let api = MonitorsAPI::with_config(configuration);
    let resp = api
        .get_monitor_notification_rule(
            monitor_notification_rule_data_id.clone(),
            GetMonitorNotificationRuleOptionalParams::default(),
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

#####  Get a monitor notification rule
```
/**
 * Get a monitor notification rule returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.MonitorsApi(configuration);

// there is a valid "monitor_notification_rule" in the system
const MONITOR_NOTIFICATION_RULE_DATA_ID = process.env
  .MONITOR_NOTIFICATION_RULE_DATA_ID as string;

const params: v2.MonitorsApiGetMonitorNotificationRuleRequest = {
  ruleId: MONITOR_NOTIFICATION_RULE_DATA_ID,
};

apiInstance
  .getMonitorNotificationRule(params)
  .then((data: v2.MonitorNotificationRuleResponse) => {
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
## [Get all monitor notification rules](https://docs.datadoghq.com/api/latest/monitors/#get-all-monitor-notification-rules)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/monitors/#get-all-monitor-notification-rules-v2)


GET https://api.ap1.datadoghq.com/api/v2/monitor/notification_rulehttps://api.ap2.datadoghq.com/api/v2/monitor/notification_rulehttps://api.datadoghq.eu/api/v2/monitor/notification_rulehttps://api.ddog-gov.com/api/v2/monitor/notification_rulehttps://api.datadoghq.com/api/v2/monitor/notification_rulehttps://api.us3.datadoghq.com/api/v2/monitor/notification_rulehttps://api.us5.datadoghq.com/api/v2/monitor/notification_rule
### Overview
Returns a list of all monitor notification rules. This endpoint requires the `monitors_read` permission.
OAuth apps require the `monitors_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#monitors) to access this endpoint.
### Arguments
#### Query Strings
Name
Type
Description
page
integer
The page to start paginating from. If `page` is not specified, the argument defaults to the first page.
per_page
integer
The number of rules to return per page. If `per_page` is not specified, the argument defaults to 100.
sort
string
String for sort order, composed of field and sort order separated by a colon, for example `name:asc`. Supported sort directions: `asc`, `desc`. Supported fields: `name`, `created_at`.
filters
string
JSON-encoded filter object. Supported keys:
  * `text`: Free-text query matched against rule name, tags, and recipients.
  * `tags`: Array of strings. Return rules that have any of these tags.
  * `recipients`: Array of strings. Return rules that have any of these recipients.


include
string
Comma-separated list of resource paths for related resources to include in the response. Supported resource path is `created_by`.
### Response
  * [200](https://docs.datadoghq.com/api/latest/monitors/#GetMonitorNotificationRules-200-v2)
  * [403](https://docs.datadoghq.com/api/latest/monitors/#GetMonitorNotificationRules-403-v2)
  * [429](https://docs.datadoghq.com/api/latest/monitors/#GetMonitorNotificationRules-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


Response for retrieving all monitor notification rules.
Field
Type
Description
data
[object]
A list of monitor notification rules.
attributes
object
Attributes of the monitor notification rule.
conditional_recipients
object
Use conditional recipients to define different recipients for different situations. Cannot be used with `recipients`.
conditions [_required_]
[object]
Conditions of the notification rule.
recipients [_required_]
[string]
A list of recipients to notify. Uses the same format as the monitor `message` field. Must not start with an '@'.
scope [_required_]
string
The scope to which the monitor applied.
fallback_recipients
[string]
If none of the `conditions` applied, `fallback_recipients` will get notified.
created
date-time
Creation time of the monitor notification rule.
filter
<oneOf>
Filter used to associate the notification rule with monitors.
Option 1
object
Filter monitor notifications by tags. A monitor notification must match all tags.
tags [_required_]
[string]
A list of tags (key:value pairs), which can be used to filter monitor notifications on monitor and group tags.
Option 2
object
Filter monitor notifications. A monitor notification must match the scope.
scope [_required_]
string
A scope composed of one or several key:value pairs, which can be used to filter monitor notifications on monitor and group tags.
modified
date-time
Time the monitor notification rule was last modified.
name
string
The name of the monitor notification rule.
recipients
[string]
A list of recipients to notify. Uses the same format as the monitor `message` field. Must not start with an '@'. Cannot be used with `conditional_recipients`.
id
string
The ID of the monitor notification rule.
relationships
object
All relationships associated with monitor notification rule.
created_by
object
The user who created the monitor notification rule.
data
object
Data for the user who created the monitor notification rule.
id
string
User ID of the monitor notification rule creator.
type
enum
Users resource type. Allowed enum values: `users`
default: `users`
type
enum
Monitor notification rule resource type. Allowed enum values: `monitor-notification-rule`
default: `monitor-notification-rule`
included
[ <oneOf>]
Array of objects related to the monitor notification rules.
Option 1
object
User object returned by the API.
attributes
object
Attributes of user object returned by the API.
created_at
date-time
Creation time of the user.
disabled
boolean
Whether the user is disabled.
email
string
Email of the user.
handle
string
Handle of the user.
icon
string
URL of the user's icon.
last_login_time
date-time
The last time the user logged in.
mfa_enabled
boolean
If user has MFA enabled.
modified_at
date-time
Time that the user was last modified.
name
string
Name of the user.
service_account
boolean
Whether the user is a service account.
status
string
Status of the user.
title
string
Title of the user.
verified
boolean
Whether the user is verified.
id
string
ID of the user.
relationships
object
Relationships of the user object returned by the API.
org
object
Relationship to an organization.
data [_required_]
object
Relationship to organization object.
id [_required_]
string
ID of the organization.
type [_required_]
enum
Organizations resource type. Allowed enum values: `orgs`
default: `orgs`
other_orgs
object
Relationship to organizations.
data [_required_]
[object]
Relationships to organization objects.
id [_required_]
string
ID of the organization.
type [_required_]
enum
Organizations resource type. Allowed enum values: `orgs`
default: `orgs`
other_users
object
Relationship to users.
data [_required_]
[object]
Relationships to user objects.
id [_required_]
string
A unique identifier that represents the user.
type [_required_]
enum
Users resource type. Allowed enum values: `users`
default: `users`
roles
object
Relationship to roles.
data
[object]
An array containing type and the unique identifier of a role.
id
string
The unique identifier of the role.
type
enum
Roles type. Allowed enum values: `roles`
default: `roles`
type
enum
Users resource type. Allowed enum values: `users`
default: `users`
```
{
  "data": [
    {
      "attributes": {
        "conditional_recipients": {
          "conditions": [
            {
              "recipients": [
                "slack-test-channel",
                "jira-test"
              ],
              "scope": "transition_type:alert"
            }
          ],
          "fallback_recipients": [
            "slack-test-channel",
            "jira-test"
          ]
        },
        "created": "2020-01-02T03:04:00.000Z",
        "filter": {
          "tags": [
            "team:product",
            "host:abc"
          ]
        },
        "modified": "2020-01-02T03:04:00.000Z",
        "name": "A notification rule name",
        "recipients": [
          "slack-test-channel",
          "jira-test"
        ]
      },
      "id": "00000000-0000-1234-0000-000000000000",
      "relationships": {
        "created_by": {
          "data": {
            "id": "00000000-0000-1234-0000-000000000000",
            "type": "users"
          }
        }
      },
      "type": "monitor-notification-rule"
    }
  ],
  "included": [
    {
      "attributes": {
        "created_at": "2019-09-19T10:00:00.000Z",
        "disabled": false,
        "email": "string",
        "handle": "string",
        "icon": "string",
        "last_login_time": "2019-09-19T10:00:00.000Z",
        "mfa_enabled": false,
        "modified_at": "2019-09-19T10:00:00.000Z",
        "name": "string",
        "service_account": false,
        "status": "string",
        "title": "string",
        "verified": false
      },
      "id": "string",
      "relationships": {
        "org": {
          "data": {
            "id": "00000000-0000-beef-0000-000000000000",
            "type": "orgs"
          }
        },
        "other_orgs": {
          "data": [
            {
              "id": "00000000-0000-beef-0000-000000000000",
              "type": "orgs"
            }
          ]
        },
        "other_users": {
          "data": [
            {
              "id": "00000000-0000-0000-2345-000000000000",
              "type": "users"
            }
          ]
        },
        "roles": {
          "data": [
            {
              "id": "3653d3c6-0c75-11ea-ad28-fb5701eabc7d",
              "type": "roles"
            }
          ]
        }
      },
      "type": "users"
    }
  ]
}
```

Copy
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


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
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/monitors/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/monitors/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/monitors/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/monitors/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/monitors/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/monitors/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/monitors/?code-lang=typescript)


#####  Get all monitor notification rules
Copy
```
                  # Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/monitor/notification_rule" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get all monitor notification rules
```
"""
Get all monitor notification rules returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.monitors_api import MonitorsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MonitorsApi(api_client)
    response = api_instance.get_monitor_notification_rules()

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get all monitor notification rules
```
# Get all monitor notification rules returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::MonitorsAPI.new
p api_instance.get_monitor_notification_rules()

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get all monitor notification rules
```
// Get all monitor notification rules returns "OK" response

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
	api := datadogV2.NewMonitorsApi(apiClient)
	resp, r, err := api.GetMonitorNotificationRules(ctx, *datadogV2.NewGetMonitorNotificationRulesOptionalParameters())

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `MonitorsApi.GetMonitorNotificationRules`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `MonitorsApi.GetMonitorNotificationRules`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get all monitor notification rules
```
// Get all monitor notification rules returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.MonitorsApi;
import com.datadog.api.client.v2.model.MonitorNotificationRuleListResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    MonitorsApi apiInstance = new MonitorsApi(defaultClient);

    try {
      MonitorNotificationRuleListResponse result = apiInstance.getMonitorNotificationRules();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MonitorsApi#getMonitorNotificationRules");
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

#####  Get all monitor notification rules
```
// Get all monitor notification rules returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_monitors::GetMonitorNotificationRulesOptionalParams;
use datadog_api_client::datadogV2::api_monitors::MonitorsAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = MonitorsAPI::with_config(configuration);
    let resp = api
        .get_monitor_notification_rules(GetMonitorNotificationRulesOptionalParams::default())
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

#####  Get all monitor notification rules
```
/**
 * Get all monitor notification rules returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.MonitorsApi(configuration);

apiInstance
  .getMonitorNotificationRules()
  .then((data: v2.MonitorNotificationRuleListResponse) => {
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
## [Create a monitor notification rule](https://docs.datadoghq.com/api/latest/monitors/#create-a-monitor-notification-rule)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/monitors/#create-a-monitor-notification-rule-v2)


POST https://api.ap1.datadoghq.com/api/v2/monitor/notification_rulehttps://api.ap2.datadoghq.com/api/v2/monitor/notification_rulehttps://api.datadoghq.eu/api/v2/monitor/notification_rulehttps://api.ddog-gov.com/api/v2/monitor/notification_rulehttps://api.datadoghq.com/api/v2/monitor/notification_rulehttps://api.us3.datadoghq.com/api/v2/monitor/notification_rulehttps://api.us5.datadoghq.com/api/v2/monitor/notification_rule
### Overview
Creates a monitor notification rule. This endpoint requires the `monitor_config_policy_write` permission.
### Request
#### Body Data (required)
Request body to create a monitor notification rule.
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


Field
Type
Description
data [_required_]
object
Object to create a monitor notification rule.
attributes [_required_]
object
Attributes of the monitor notification rule.
conditional_recipients
object
Use conditional recipients to define different recipients for different situations. Cannot be used with `recipients`.
conditions [_required_]
[object]
Conditions of the notification rule.
recipients [_required_]
[string]
A list of recipients to notify. Uses the same format as the monitor `message` field. Must not start with an '@'.
scope [_required_]
string
The scope to which the monitor applied.
fallback_recipients
[string]
If none of the `conditions` applied, `fallback_recipients` will get notified.
filter
<oneOf>
Filter used to associate the notification rule with monitors.
Option 1
object
Filter monitor notifications by tags. A monitor notification must match all tags.
tags [_required_]
[string]
A list of tags (key:value pairs), which can be used to filter monitor notifications on monitor and group tags.
Option 2
object
Filter monitor notifications. A monitor notification must match the scope.
scope [_required_]
string
A scope composed of one or several key:value pairs, which can be used to filter monitor notifications on monitor and group tags.
name [_required_]
string
The name of the monitor notification rule.
recipients
[string]
A list of recipients to notify. Uses the same format as the monitor `message` field. Must not start with an '@'. Cannot be used with `conditional_recipients`.
type
enum
Monitor notification rule resource type. Allowed enum values: `monitor-notification-rule`
default: `monitor-notification-rule`
#####  Create a monitor notification rule returns "OK" response
```
{
  "data": {
    "attributes": {
      "filter": {
        "tags": [
          "test:example-monitor"
        ]
      },
      "name": "test rule",
      "recipients": [
        "slack-test-channel",
        "jira-test"
      ]
    },
    "type": "monitor-notification-rule"
  }
}
```

Copy
#####  Create a monitor notification rule with conditional recipients returns "OK" response
```
{
  "data": {
    "attributes": {
      "filter": {
        "tags": [
          "test:example-monitor"
        ]
      },
      "name": "test rule",
      "conditional_recipients": {
        "conditions": [
          {
            "scope": "transition_type:is_alert",
            "recipients": [
              "slack-test-channel",
              "jira-test"
            ]
          }
        ]
      }
    },
    "type": "monitor-notification-rule"
  }
}
```

Copy
#####  Create a monitor notification rule with scope returns "OK" response
```
{
  "data": {
    "attributes": {
      "filter": {
        "scope": "test:example-monitor"
      },
      "name": "test rule",
      "recipients": [
        "slack-test-channel",
        "jira-test"
      ]
    },
    "type": "monitor-notification-rule"
  }
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/monitors/#CreateMonitorNotificationRule-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/monitors/#CreateMonitorNotificationRule-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/monitors/#CreateMonitorNotificationRule-403-v2)
  * [429](https://docs.datadoghq.com/api/latest/monitors/#CreateMonitorNotificationRule-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


A monitor notification rule.
Field
Type
Description
data
object
Monitor notification rule data.
attributes
object
Attributes of the monitor notification rule.
conditional_recipients
object
Use conditional recipients to define different recipients for different situations. Cannot be used with `recipients`.
conditions [_required_]
[object]
Conditions of the notification rule.
recipients [_required_]
[string]
A list of recipients to notify. Uses the same format as the monitor `message` field. Must not start with an '@'.
scope [_required_]
string
The scope to which the monitor applied.
fallback_recipients
[string]
If none of the `conditions` applied, `fallback_recipients` will get notified.
created
date-time
Creation time of the monitor notification rule.
filter
<oneOf>
Filter used to associate the notification rule with monitors.
Option 1
object
Filter monitor notifications by tags. A monitor notification must match all tags.
tags [_required_]
[string]
A list of tags (key:value pairs), which can be used to filter monitor notifications on monitor and group tags.
Option 2
object
Filter monitor notifications. A monitor notification must match the scope.
scope [_required_]
string
A scope composed of one or several key:value pairs, which can be used to filter monitor notifications on monitor and group tags.
modified
date-time
Time the monitor notification rule was last modified.
name
string
The name of the monitor notification rule.
recipients
[string]
A list of recipients to notify. Uses the same format as the monitor `message` field. Must not start with an '@'. Cannot be used with `conditional_recipients`.
id
string
The ID of the monitor notification rule.
relationships
object
All relationships associated with monitor notification rule.
created_by
object
The user who created the monitor notification rule.
data
object
Data for the user who created the monitor notification rule.
id
string
User ID of the monitor notification rule creator.
type
enum
Users resource type. Allowed enum values: `users`
default: `users`
type
enum
Monitor notification rule resource type. Allowed enum values: `monitor-notification-rule`
default: `monitor-notification-rule`
included
[ <oneOf>]
Array of objects related to the monitor notification rule that the user requested.
Option 1
object
User object returned by the API.
attributes
object
Attributes of user object returned by the API.
created_at
date-time
Creation time of the user.
disabled
boolean
Whether the user is disabled.
email
string
Email of the user.
handle
string
Handle of the user.
icon
string
URL of the user's icon.
last_login_time
date-time
The last time the user logged in.
mfa_enabled
boolean
If user has MFA enabled.
modified_at
date-time
Time that the user was last modified.
name
string
Name of the user.
service_account
boolean
Whether the user is a service account.
status
string
Status of the user.
title
string
Title of the user.
verified
boolean
Whether the user is verified.
id
string
ID of the user.
relationships
object
Relationships of the user object returned by the API.
org
object
Relationship to an organization.
data [_required_]
object
Relationship to organization object.
id [_required_]
string
ID of the organization.
type [_required_]
enum
Organizations resource type. Allowed enum values: `orgs`
default: `orgs`
other_orgs
object
Relationship to organizations.
data [_required_]
[object]
Relationships to organization objects.
id [_required_]
string
ID of the organization.
type [_required_]
enum
Organizations resource type. Allowed enum values: `orgs`
default: `orgs`
other_users
object
Relationship to users.
data [_required_]
[object]
Relationships to user objects.
id [_required_]
string
A unique identifier that represents the user.
type [_required_]
enum
Users resource type. Allowed enum values: `users`
default: `users`
roles
object
Relationship to roles.
data
[object]
An array containing type and the unique identifier of a role.
id
string
The unique identifier of the role.
type
enum
Roles type. Allowed enum values: `roles`
default: `roles`
type
enum
Users resource type. Allowed enum values: `users`
default: `users`
```
{
  "data": {
    "attributes": {
      "conditional_recipients": {
        "conditions": [
          {
            "recipients": [
              "slack-test-channel",
              "jira-test"
            ],
            "scope": "transition_type:alert"
          }
        ],
        "fallback_recipients": [
          "slack-test-channel",
          "jira-test"
        ]
      },
      "created": "2020-01-02T03:04:00.000Z",
      "filter": {
        "tags": [
          "team:product",
          "host:abc"
        ]
      },
      "modified": "2020-01-02T03:04:00.000Z",
      "name": "A notification rule name",
      "recipients": [
        "slack-test-channel",
        "jira-test"
      ]
    },
    "id": "00000000-0000-1234-0000-000000000000",
    "relationships": {
      "created_by": {
        "data": {
          "id": "00000000-0000-1234-0000-000000000000",
          "type": "users"
        }
      }
    },
    "type": "monitor-notification-rule"
  },
  "included": [
    {
      "attributes": {
        "created_at": "2019-09-19T10:00:00.000Z",
        "disabled": false,
        "email": "string",
        "handle": "string",
        "icon": "string",
        "last_login_time": "2019-09-19T10:00:00.000Z",
        "mfa_enabled": false,
        "modified_at": "2019-09-19T10:00:00.000Z",
        "name": "string",
        "service_account": false,
        "status": "string",
        "title": "string",
        "verified": false
      },
      "id": "string",
      "relationships": {
        "org": {
          "data": {
            "id": "00000000-0000-beef-0000-000000000000",
            "type": "orgs"
          }
        },
        "other_orgs": {
          "data": [
            {
              "id": "00000000-0000-beef-0000-000000000000",
              "type": "orgs"
            }
          ]
        },
        "other_users": {
          "data": [
            {
              "id": "00000000-0000-0000-2345-000000000000",
              "type": "users"
            }
          ]
        },
        "roles": {
          "data": [
            {
              "id": "3653d3c6-0c75-11ea-ad28-fb5701eabc7d",
              "type": "roles"
            }
          ]
        }
      },
      "type": "users"
    }
  ]
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


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
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


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
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/monitors/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/monitors/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/monitors/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/monitors/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/monitors/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/monitors/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/monitors/?code-lang=typescript)


#####  Create a monitor notification rule returns "OK" response
Copy
```
                          # Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/monitor/notification_rule" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "filter": {
        "tags": [
          "test:example-monitor"
        ]
      },
      "name": "test rule",
      "recipients": [
        "slack-test-channel",
        "jira-test"
      ]
    },
    "type": "monitor-notification-rule"
  }
}
EOF  

                        
```

#####  Create a monitor notification rule with conditional recipients returns "OK" response
Copy
```
                          # Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/monitor/notification_rule" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "filter": {
        "tags": [
          "test:example-monitor"
        ]
      },
      "name": "test rule",
      "conditional_recipients": {
        "conditions": [
          {
            "scope": "transition_type:is_alert",
            "recipients": [
              "slack-test-channel",
              "jira-test"
            ]
          }
        ]
      }
    },
    "type": "monitor-notification-rule"
  }
}
EOF  

                        
```

#####  Create a monitor notification rule with scope returns "OK" response
Copy
```
                          # Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/monitor/notification_rule" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "filter": {
        "scope": "test:example-monitor"
      },
      "name": "test rule",
      "recipients": [
        "slack-test-channel",
        "jira-test"
      ]
    },
    "type": "monitor-notification-rule"
  }
}
EOF  

                        
```

#####  Create a monitor notification rule returns "OK" response 
```
// Create a monitor notification rule returns "OK" response

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
	body := datadogV2.MonitorNotificationRuleCreateRequest{
		Data: datadogV2.MonitorNotificationRuleCreateRequestData{
			Attributes: datadogV2.MonitorNotificationRuleAttributes{
				Filter: &datadogV2.MonitorNotificationRuleFilter{
					MonitorNotificationRuleFilterTags: &datadogV2.MonitorNotificationRuleFilterTags{
						Tags: []string{
							"test:example-monitor",
						},
					}},
				Name: "test rule",
				Recipients: []string{
					"slack-test-channel",
					"jira-test",
				},
			},
			Type: datadogV2.MONITORNOTIFICATIONRULERESOURCETYPE_MONITOR_NOTIFICATION_RULE.Ptr(),
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewMonitorsApi(apiClient)
	resp, r, err := api.CreateMonitorNotificationRule(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `MonitorsApi.CreateMonitorNotificationRule`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `MonitorsApi.CreateMonitorNotificationRule`:\n%s\n", responseContent)
}

```

Copy
#####  Create a monitor notification rule with conditional recipients returns "OK" response 
```
// Create a monitor notification rule with conditional recipients returns "OK" response

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
	body := datadogV2.MonitorNotificationRuleCreateRequest{
		Data: datadogV2.MonitorNotificationRuleCreateRequestData{
			Attributes: datadogV2.MonitorNotificationRuleAttributes{
				Filter: &datadogV2.MonitorNotificationRuleFilter{
					MonitorNotificationRuleFilterTags: &datadogV2.MonitorNotificationRuleFilterTags{
						Tags: []string{
							"test:example-monitor",
						},
					}},
				Name: "test rule",
				ConditionalRecipients: &datadogV2.MonitorNotificationRuleConditionalRecipients{
					Conditions: []datadogV2.MonitorNotificationRuleCondition{
						{
							Scope: "transition_type:is_alert",
							Recipients: []string{
								"slack-test-channel",
								"jira-test",
							},
						},
					},
				},
			},
			Type: datadogV2.MONITORNOTIFICATIONRULERESOURCETYPE_MONITOR_NOTIFICATION_RULE.Ptr(),
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewMonitorsApi(apiClient)
	resp, r, err := api.CreateMonitorNotificationRule(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `MonitorsApi.CreateMonitorNotificationRule`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `MonitorsApi.CreateMonitorNotificationRule`:\n%s\n", responseContent)
}

```

Copy
#####  Create a monitor notification rule with scope returns "OK" response 
```
// Create a monitor notification rule with scope returns "OK" response

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
	body := datadogV2.MonitorNotificationRuleCreateRequest{
		Data: datadogV2.MonitorNotificationRuleCreateRequestData{
			Attributes: datadogV2.MonitorNotificationRuleAttributes{
				Filter: &datadogV2.MonitorNotificationRuleFilter{
					MonitorNotificationRuleFilterScope: &datadogV2.MonitorNotificationRuleFilterScope{
						Scope: "test:example-monitor",
					}},
				Name: "test rule",
				Recipients: []string{
					"slack-test-channel",
					"jira-test",
				},
			},
			Type: datadogV2.MONITORNOTIFICATIONRULERESOURCETYPE_MONITOR_NOTIFICATION_RULE.Ptr(),
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewMonitorsApi(apiClient)
	resp, r, err := api.CreateMonitorNotificationRule(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `MonitorsApi.CreateMonitorNotificationRule`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `MonitorsApi.CreateMonitorNotificationRule`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Create a monitor notification rule returns "OK" response 
```
// Create a monitor notification rule returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.MonitorsApi;
import com.datadog.api.client.v2.model.MonitorNotificationRuleAttributes;
import com.datadog.api.client.v2.model.MonitorNotificationRuleCreateRequest;
import com.datadog.api.client.v2.model.MonitorNotificationRuleCreateRequestData;
import com.datadog.api.client.v2.model.MonitorNotificationRuleFilter;
import com.datadog.api.client.v2.model.MonitorNotificationRuleFilterTags;
import com.datadog.api.client.v2.model.MonitorNotificationRuleResourceType;
import com.datadog.api.client.v2.model.MonitorNotificationRuleResponse;
import java.util.Arrays;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    MonitorsApi apiInstance = new MonitorsApi(defaultClient);

    MonitorNotificationRuleCreateRequest body =
        new MonitorNotificationRuleCreateRequest()
            .data(
                new MonitorNotificationRuleCreateRequestData()
                    .attributes(
                        new MonitorNotificationRuleAttributes()
                            .filter(
                                new MonitorNotificationRuleFilter(
                                    new MonitorNotificationRuleFilterTags()
                                        .tags(Collections.singletonList("test:example-monitor"))))
                            .name("test rule")
                            .recipients(Arrays.asList("slack-test-channel", "jira-test")))
                    .type(MonitorNotificationRuleResourceType.MONITOR_NOTIFICATION_RULE));

    try {
      MonitorNotificationRuleResponse result = apiInstance.createMonitorNotificationRule(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MonitorsApi#createMonitorNotificationRule");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}

```

Copy
#####  Create a monitor notification rule with conditional recipients returns "OK" response 
```
// Create a monitor notification rule with conditional recipients returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.MonitorsApi;
import com.datadog.api.client.v2.model.MonitorNotificationRuleAttributes;
import com.datadog.api.client.v2.model.MonitorNotificationRuleCondition;
import com.datadog.api.client.v2.model.MonitorNotificationRuleConditionalRecipients;
import com.datadog.api.client.v2.model.MonitorNotificationRuleCreateRequest;
import com.datadog.api.client.v2.model.MonitorNotificationRuleCreateRequestData;
import com.datadog.api.client.v2.model.MonitorNotificationRuleFilter;
import com.datadog.api.client.v2.model.MonitorNotificationRuleFilterTags;
import com.datadog.api.client.v2.model.MonitorNotificationRuleResourceType;
import com.datadog.api.client.v2.model.MonitorNotificationRuleResponse;
import java.util.Arrays;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    MonitorsApi apiInstance = new MonitorsApi(defaultClient);

    MonitorNotificationRuleCreateRequest body =
        new MonitorNotificationRuleCreateRequest()
            .data(
                new MonitorNotificationRuleCreateRequestData()
                    .attributes(
                        new MonitorNotificationRuleAttributes()
                            .filter(
                                new MonitorNotificationRuleFilter(
                                    new MonitorNotificationRuleFilterTags()
                                        .tags(Collections.singletonList("test:example-monitor"))))
                            .name("test rule")
                            .conditionalRecipients(
                                new MonitorNotificationRuleConditionalRecipients()
                                    .conditions(
                                        Collections.singletonList(
                                            new MonitorNotificationRuleCondition()
                                                .scope("transition_type:is_alert")
                                                .recipients(
                                                    Arrays.asList(
                                                        "slack-test-channel", "jira-test"))))))
                    .type(MonitorNotificationRuleResourceType.MONITOR_NOTIFICATION_RULE));

    try {
      MonitorNotificationRuleResponse result = apiInstance.createMonitorNotificationRule(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MonitorsApi#createMonitorNotificationRule");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}

```

Copy
#####  Create a monitor notification rule with scope returns "OK" response 
```
// Create a monitor notification rule with scope returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.MonitorsApi;
import com.datadog.api.client.v2.model.MonitorNotificationRuleAttributes;
import com.datadog.api.client.v2.model.MonitorNotificationRuleCreateRequest;
import com.datadog.api.client.v2.model.MonitorNotificationRuleCreateRequestData;
import com.datadog.api.client.v2.model.MonitorNotificationRuleFilter;
import com.datadog.api.client.v2.model.MonitorNotificationRuleFilterScope;
import com.datadog.api.client.v2.model.MonitorNotificationRuleResourceType;
import com.datadog.api.client.v2.model.MonitorNotificationRuleResponse;
import java.util.Arrays;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    MonitorsApi apiInstance = new MonitorsApi(defaultClient);

    MonitorNotificationRuleCreateRequest body =
        new MonitorNotificationRuleCreateRequest()
            .data(
                new MonitorNotificationRuleCreateRequestData()
                    .attributes(
                        new MonitorNotificationRuleAttributes()
                            .filter(
                                new MonitorNotificationRuleFilter(
                                    new MonitorNotificationRuleFilterScope()
                                        .scope("test:example-monitor")))
                            .name("test rule")
                            .recipients(Arrays.asList("slack-test-channel", "jira-test")))
                    .type(MonitorNotificationRuleResourceType.MONITOR_NOTIFICATION_RULE));

    try {
      MonitorNotificationRuleResponse result = apiInstance.createMonitorNotificationRule(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MonitorsApi#createMonitorNotificationRule");
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

#####  Create a monitor notification rule returns "OK" response 
```
"""
Create a monitor notification rule returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.monitors_api import MonitorsApi
from datadog_api_client.v2.model.monitor_notification_rule_attributes import MonitorNotificationRuleAttributes
from datadog_api_client.v2.model.monitor_notification_rule_create_request import MonitorNotificationRuleCreateRequest
from datadog_api_client.v2.model.monitor_notification_rule_create_request_data import (
    MonitorNotificationRuleCreateRequestData,
)
from datadog_api_client.v2.model.monitor_notification_rule_filter_tags import MonitorNotificationRuleFilterTags
from datadog_api_client.v2.model.monitor_notification_rule_resource_type import MonitorNotificationRuleResourceType

body = MonitorNotificationRuleCreateRequest(
    data=MonitorNotificationRuleCreateRequestData(
        attributes=MonitorNotificationRuleAttributes(
            filter=MonitorNotificationRuleFilterTags(
                tags=[
                    "test:example-monitor",
                ],
            ),
            name="test rule",
            recipients=[
                "slack-test-channel",
                "jira-test",
            ],
        ),
        type=MonitorNotificationRuleResourceType.MONITOR_NOTIFICATION_RULE,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MonitorsApi(api_client)
    response = api_instance.create_monitor_notification_rule(body=body)

    print(response)

```

Copy
#####  Create a monitor notification rule with conditional recipients returns "OK" response 
```
"""
Create a monitor notification rule with conditional recipients returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.monitors_api import MonitorsApi
from datadog_api_client.v2.model.monitor_notification_rule_attributes import MonitorNotificationRuleAttributes
from datadog_api_client.v2.model.monitor_notification_rule_condition import MonitorNotificationRuleCondition
from datadog_api_client.v2.model.monitor_notification_rule_conditional_recipients import (
    MonitorNotificationRuleConditionalRecipients,
)
from datadog_api_client.v2.model.monitor_notification_rule_create_request import MonitorNotificationRuleCreateRequest
from datadog_api_client.v2.model.monitor_notification_rule_create_request_data import (
    MonitorNotificationRuleCreateRequestData,
)
from datadog_api_client.v2.model.monitor_notification_rule_filter_tags import MonitorNotificationRuleFilterTags
from datadog_api_client.v2.model.monitor_notification_rule_resource_type import MonitorNotificationRuleResourceType

body = MonitorNotificationRuleCreateRequest(
    data=MonitorNotificationRuleCreateRequestData(
        attributes=MonitorNotificationRuleAttributes(
            filter=MonitorNotificationRuleFilterTags(
                tags=[
                    "test:example-monitor",
                ],
            ),
            name="test rule",
            conditional_recipients=MonitorNotificationRuleConditionalRecipients(
                conditions=[
                    MonitorNotificationRuleCondition(
                        scope="transition_type:is_alert",
                        recipients=[
                            "slack-test-channel",
                            "jira-test",
                        ],
                    ),
                ],
            ),
        ),
        type=MonitorNotificationRuleResourceType.MONITOR_NOTIFICATION_RULE,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MonitorsApi(api_client)
    response = api_instance.create_monitor_notification_rule(body=body)

    print(response)

```

Copy
#####  Create a monitor notification rule with scope returns "OK" response 
```
"""
Create a monitor notification rule with scope returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.monitors_api import MonitorsApi
from datadog_api_client.v2.model.monitor_notification_rule_attributes import MonitorNotificationRuleAttributes
from datadog_api_client.v2.model.monitor_notification_rule_create_request import MonitorNotificationRuleCreateRequest
from datadog_api_client.v2.model.monitor_notification_rule_create_request_data import (
    MonitorNotificationRuleCreateRequestData,
)
from datadog_api_client.v2.model.monitor_notification_rule_filter_scope import MonitorNotificationRuleFilterScope
from datadog_api_client.v2.model.monitor_notification_rule_resource_type import MonitorNotificationRuleResourceType

body = MonitorNotificationRuleCreateRequest(
    data=MonitorNotificationRuleCreateRequestData(
        attributes=MonitorNotificationRuleAttributes(
            filter=MonitorNotificationRuleFilterScope(
                scope="test:example-monitor",
            ),
            name="test rule",
            recipients=[
                "slack-test-channel",
                "jira-test",
            ],
        ),
        type=MonitorNotificationRuleResourceType.MONITOR_NOTIFICATION_RULE,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MonitorsApi(api_client)
    response = api_instance.create_monitor_notification_rule(body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Create a monitor notification rule returns "OK" response 
```
# Create a monitor notification rule returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::MonitorsAPI.new

body = DatadogAPIClient::V2::MonitorNotificationRuleCreateRequest.new({
  data: DatadogAPIClient::V2::MonitorNotificationRuleCreateRequestData.new({
    attributes: DatadogAPIClient::V2::MonitorNotificationRuleAttributes.new({
      filter: DatadogAPIClient::V2::MonitorNotificationRuleFilterTags.new({
        tags: [
          "test:example-monitor",
        ],
      }),
      name: "test rule",
      recipients: [
        "slack-test-channel",
        "jira-test",
      ],
    }),
    type: DatadogAPIClient::V2::MonitorNotificationRuleResourceType::MONITOR_NOTIFICATION_RULE,
  }),
})
p api_instance.create_monitor_notification_rule(body)

```

Copy
#####  Create a monitor notification rule with conditional recipients returns "OK" response 
```
# Create a monitor notification rule with conditional recipients returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::MonitorsAPI.new

body = DatadogAPIClient::V2::MonitorNotificationRuleCreateRequest.new({
  data: DatadogAPIClient::V2::MonitorNotificationRuleCreateRequestData.new({
    attributes: DatadogAPIClient::V2::MonitorNotificationRuleAttributes.new({
      filter: DatadogAPIClient::V2::MonitorNotificationRuleFilterTags.new({
        tags: [
          "test:example-monitor",
        ],
      }),
      name: "test rule",
      conditional_recipients: DatadogAPIClient::V2::MonitorNotificationRuleConditionalRecipients.new({
        conditions: [
          DatadogAPIClient::V2::MonitorNotificationRuleCondition.new({
            scope: "transition_type:is_alert",
            recipients: [
              "slack-test-channel",
              "jira-test",
            ],
          }),
        ],
      }),
    }),
    type: DatadogAPIClient::V2::MonitorNotificationRuleResourceType::MONITOR_NOTIFICATION_RULE,
  }),
})
p api_instance.create_monitor_notification_rule(body)

```

Copy
#####  Create a monitor notification rule with scope returns "OK" response 
```
# Create a monitor notification rule with scope returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::MonitorsAPI.new

body = DatadogAPIClient::V2::MonitorNotificationRuleCreateRequest.new({
  data: DatadogAPIClient::V2::MonitorNotificationRuleCreateRequestData.new({
    attributes: DatadogAPIClient::V2::MonitorNotificationRuleAttributes.new({
      filter: DatadogAPIClient::V2::MonitorNotificationRuleFilterScope.new({
        scope: "test:example-monitor",
      }),
      name: "test rule",
      recipients: [
        "slack-test-channel",
        "jira-test",
      ],
    }),
    type: DatadogAPIClient::V2::MonitorNotificationRuleResourceType::MONITOR_NOTIFICATION_RULE,
  }),
})
p api_instance.create_monitor_notification_rule(body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Create a monitor notification rule returns "OK" response 
```
// Create a monitor notification rule returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_monitors::MonitorsAPI;
use datadog_api_client::datadogV2::model::MonitorNotificationRuleAttributes;
use datadog_api_client::datadogV2::model::MonitorNotificationRuleCreateRequest;
use datadog_api_client::datadogV2::model::MonitorNotificationRuleCreateRequestData;
use datadog_api_client::datadogV2::model::MonitorNotificationRuleFilter;
use datadog_api_client::datadogV2::model::MonitorNotificationRuleFilterTags;
use datadog_api_client::datadogV2::model::MonitorNotificationRuleResourceType;

#[tokio::main]
async fn main() {
    let body = MonitorNotificationRuleCreateRequest::new(
        MonitorNotificationRuleCreateRequestData::new(
            MonitorNotificationRuleAttributes::new("test rule".to_string())
                .filter(
                    MonitorNotificationRuleFilter::MonitorNotificationRuleFilterTags(Box::new(
                        MonitorNotificationRuleFilterTags::new(vec![
                            "test:example-monitor".to_string()
                        ]),
                    )),
                )
                .recipients(vec![
                    "slack-test-channel".to_string(),
                    "jira-test".to_string(),
                ]),
        )
        .type_(MonitorNotificationRuleResourceType::MONITOR_NOTIFICATION_RULE),
    );
    let configuration = datadog::Configuration::new();
    let api = MonitorsAPI::with_config(configuration);
    let resp = api.create_monitor_notification_rule(body).await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}

```

Copy
#####  Create a monitor notification rule with conditional recipients returns "OK" response 
```
// Create a monitor notification rule with conditional recipients returns "OK"
// response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_monitors::MonitorsAPI;
use datadog_api_client::datadogV2::model::MonitorNotificationRuleAttributes;
use datadog_api_client::datadogV2::model::MonitorNotificationRuleCondition;
use datadog_api_client::datadogV2::model::MonitorNotificationRuleConditionalRecipients;
use datadog_api_client::datadogV2::model::MonitorNotificationRuleCreateRequest;
use datadog_api_client::datadogV2::model::MonitorNotificationRuleCreateRequestData;
use datadog_api_client::datadogV2::model::MonitorNotificationRuleFilter;
use datadog_api_client::datadogV2::model::MonitorNotificationRuleFilterTags;
use datadog_api_client::datadogV2::model::MonitorNotificationRuleResourceType;

#[tokio::main]
async fn main() {
    let body = MonitorNotificationRuleCreateRequest::new(
        MonitorNotificationRuleCreateRequestData::new(
            MonitorNotificationRuleAttributes::new("test rule".to_string())
                .conditional_recipients(MonitorNotificationRuleConditionalRecipients::new(vec![
                    MonitorNotificationRuleCondition::new(
                        vec!["slack-test-channel".to_string(), "jira-test".to_string()],
                        "transition_type:is_alert".to_string(),
                    ),
                ]))
                .filter(
                    MonitorNotificationRuleFilter::MonitorNotificationRuleFilterTags(Box::new(
                        MonitorNotificationRuleFilterTags::new(vec![
                            "test:example-monitor".to_string()
                        ]),
                    )),
                ),
        )
        .type_(MonitorNotificationRuleResourceType::MONITOR_NOTIFICATION_RULE),
    );
    let configuration = datadog::Configuration::new();
    let api = MonitorsAPI::with_config(configuration);
    let resp = api.create_monitor_notification_rule(body).await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}

```

Copy
#####  Create a monitor notification rule with scope returns "OK" response 
```
// Create a monitor notification rule with scope returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_monitors::MonitorsAPI;
use datadog_api_client::datadogV2::model::MonitorNotificationRuleAttributes;
use datadog_api_client::datadogV2::model::MonitorNotificationRuleCreateRequest;
use datadog_api_client::datadogV2::model::MonitorNotificationRuleCreateRequestData;
use datadog_api_client::datadogV2::model::MonitorNotificationRuleFilter;
use datadog_api_client::datadogV2::model::MonitorNotificationRuleFilterScope;
use datadog_api_client::datadogV2::model::MonitorNotificationRuleResourceType;

#[tokio::main]
async fn main() {
    let body = MonitorNotificationRuleCreateRequest::new(
        MonitorNotificationRuleCreateRequestData::new(
            MonitorNotificationRuleAttributes::new("test rule".to_string())
                .filter(
                    MonitorNotificationRuleFilter::MonitorNotificationRuleFilterScope(Box::new(
                        MonitorNotificationRuleFilterScope::new("test:example-monitor".to_string()),
                    )),
                )
                .recipients(vec![
                    "slack-test-channel".to_string(),
                    "jira-test".to_string(),
                ]),
        )
        .type_(MonitorNotificationRuleResourceType::MONITOR_NOTIFICATION_RULE),
    );
    let configuration = datadog::Configuration::new();
    let api = MonitorsAPI::with_config(configuration);
    let resp = api.create_monitor_notification_rule(body).await;
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

#####  Create a monitor notification rule returns "OK" response 
```
/**
 * Create a monitor notification rule returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.MonitorsApi(configuration);

const params: v2.MonitorsApiCreateMonitorNotificationRuleRequest = {
  body: {
    data: {
      attributes: {
        filter: {
          tags: ["test:example-monitor"],
        },
        name: "test rule",
        recipients: ["slack-test-channel", "jira-test"],
      },
      type: "monitor-notification-rule",
    },
  },
};

apiInstance
  .createMonitorNotificationRule(params)
  .then((data: v2.MonitorNotificationRuleResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));

```

Copy
#####  Create a monitor notification rule with conditional recipients returns "OK" response 
```
/**
 * Create a monitor notification rule with conditional recipients returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.MonitorsApi(configuration);

const params: v2.MonitorsApiCreateMonitorNotificationRuleRequest = {
  body: {
    data: {
      attributes: {
        filter: {
          tags: ["test:example-monitor"],
        },
        name: "test rule",
        conditionalRecipients: {
          conditions: [
            {
              scope: "transition_type:is_alert",
              recipients: ["slack-test-channel", "jira-test"],
            },
          ],
        },
      },
      type: "monitor-notification-rule",
    },
  },
};

apiInstance
  .createMonitorNotificationRule(params)
  .then((data: v2.MonitorNotificationRuleResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));

```

Copy
#####  Create a monitor notification rule with scope returns "OK" response 
```
/**
 * Create a monitor notification rule with scope returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.MonitorsApi(configuration);

const params: v2.MonitorsApiCreateMonitorNotificationRuleRequest = {
  body: {
    data: {
      attributes: {
        filter: {
          scope: "test:example-monitor",
        },
        name: "test rule",
        recipients: ["slack-test-channel", "jira-test"],
      },
      type: "monitor-notification-rule",
    },
  },
};

apiInstance
  .createMonitorNotificationRule(params)
  .then((data: v2.MonitorNotificationRuleResponse) => {
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
## [Update a monitor notification rule](https://docs.datadoghq.com/api/latest/monitors/#update-a-monitor-notification-rule)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/monitors/#update-a-monitor-notification-rule-v2)


PATCH https://api.ap1.datadoghq.com/api/v2/monitor/notification_rule/{rule_id}https://api.ap2.datadoghq.com/api/v2/monitor/notification_rule/{rule_id}https://api.datadoghq.eu/api/v2/monitor/notification_rule/{rule_id}https://api.ddog-gov.com/api/v2/monitor/notification_rule/{rule_id}https://api.datadoghq.com/api/v2/monitor/notification_rule/{rule_id}https://api.us3.datadoghq.com/api/v2/monitor/notification_rule/{rule_id}https://api.us5.datadoghq.com/api/v2/monitor/notification_rule/{rule_id}
### Overview
Updates a monitor notification rule by `rule_id`. This endpoint requires the `monitor_config_policy_write` permission.
### Arguments
#### Path Parameters
Name
Type
Description
rule_id [_required_]
string
ID of the monitor notification rule to update.
### Request
#### Body Data (required)
Request body to update the monitor notification rule.
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


Field
Type
Description
data [_required_]
object
Object to update a monitor notification rule.
attributes [_required_]
object
Attributes of the monitor notification rule.
conditional_recipients
object
Use conditional recipients to define different recipients for different situations. Cannot be used with `recipients`.
conditions [_required_]
[object]
Conditions of the notification rule.
recipients [_required_]
[string]
A list of recipients to notify. Uses the same format as the monitor `message` field. Must not start with an '@'.
scope [_required_]
string
The scope to which the monitor applied.
fallback_recipients
[string]
If none of the `conditions` applied, `fallback_recipients` will get notified.
filter
<oneOf>
Filter used to associate the notification rule with monitors.
Option 1
object
Filter monitor notifications by tags. A monitor notification must match all tags.
tags [_required_]
[string]
A list of tags (key:value pairs), which can be used to filter monitor notifications on monitor and group tags.
Option 2
object
Filter monitor notifications. A monitor notification must match the scope.
scope [_required_]
string
A scope composed of one or several key:value pairs, which can be used to filter monitor notifications on monitor and group tags.
name [_required_]
string
The name of the monitor notification rule.
recipients
[string]
A list of recipients to notify. Uses the same format as the monitor `message` field. Must not start with an '@'. Cannot be used with `conditional_recipients`.
id [_required_]
string
The ID of the monitor notification rule.
type
enum
Monitor notification rule resource type. Allowed enum values: `monitor-notification-rule`
default: `monitor-notification-rule`
#####  Update a monitor notification rule returns "OK" response
```
{
  "data": {
    "attributes": {
      "filter": {
        "tags": [
          "test:example-monitor",
          "host:abc"
        ]
      },
      "name": "updated rule",
      "recipients": [
        "slack-test-channel"
      ]
    },
    "id": "00000000-0000-1234-0000-000000000000",
    "type": "monitor-notification-rule"
  }
}
```

Copy
#####  Update a monitor notification rule with conditional_recipients returns "OK" response
```
{
  "data": {
    "attributes": {
      "filter": {
        "tags": [
          "test:example-monitor",
          "host:abc"
        ]
      },
      "name": "updated rule",
      "conditional_recipients": {
        "conditions": [
          {
            "scope": "transition_type:is_alert",
            "recipients": [
              "slack-test-channel",
              "jira-test"
            ]
          }
        ]
      }
    },
    "id": "00000000-0000-1234-0000-000000000000",
    "type": "monitor-notification-rule"
  }
}
```

Copy
#####  Update a monitor notification rule with scope returns "OK" response
```
{
  "data": {
    "attributes": {
      "filter": {
        "scope": "test:example-monitor"
      },
      "name": "updated rule",
      "recipients": [
        "slack-test-channel"
      ]
    },
    "id": "00000000-0000-1234-0000-000000000000",
    "type": "monitor-notification-rule"
  }
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/monitors/#UpdateMonitorNotificationRule-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/monitors/#UpdateMonitorNotificationRule-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/monitors/#UpdateMonitorNotificationRule-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/monitors/#UpdateMonitorNotificationRule-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/monitors/#UpdateMonitorNotificationRule-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


A monitor notification rule.
Field
Type
Description
data
object
Monitor notification rule data.
attributes
object
Attributes of the monitor notification rule.
conditional_recipients
object
Use conditional recipients to define different recipients for different situations. Cannot be used with `recipients`.
conditions [_required_]
[object]
Conditions of the notification rule.
recipients [_required_]
[string]
A list of recipients to notify. Uses the same format as the monitor `message` field. Must not start with an '@'.
scope [_required_]
string
The scope to which the monitor applied.
fallback_recipients
[string]
If none of the `conditions` applied, `fallback_recipients` will get notified.
created
date-time
Creation time of the monitor notification rule.
filter
<oneOf>
Filter used to associate the notification rule with monitors.
Option 1
object
Filter monitor notifications by tags. A monitor notification must match all tags.
tags [_required_]
[string]
A list of tags (key:value pairs), which can be used to filter monitor notifications on monitor and group tags.
Option 2
object
Filter monitor notifications. A monitor notification must match the scope.
scope [_required_]
string
A scope composed of one or several key:value pairs, which can be used to filter monitor notifications on monitor and group tags.
modified
date-time
Time the monitor notification rule was last modified.
name
string
The name of the monitor notification rule.
recipients
[string]
A list of recipients to notify. Uses the same format as the monitor `message` field. Must not start with an '@'. Cannot be used with `conditional_recipients`.
id
string
The ID of the monitor notification rule.
relationships
object
All relationships associated with monitor notification rule.
created_by
object
The user who created the monitor notification rule.
data
object
Data for the user who created the monitor notification rule.
id
string
User ID of the monitor notification rule creator.
type
enum
Users resource type. Allowed enum values: `users`
default: `users`
type
enum
Monitor notification rule resource type. Allowed enum values: `monitor-notification-rule`
default: `monitor-notification-rule`
included
[ <oneOf>]
Array of objects related to the monitor notification rule that the user requested.
Option 1
object
User object returned by the API.
attributes
object
Attributes of user object returned by the API.
created_at
date-time
Creation time of the user.
disabled
boolean
Whether the user is disabled.
email
string
Email of the user.
handle
string
Handle of the user.
icon
string
URL of the user's icon.
last_login_time
date-time
The last time the user logged in.
mfa_enabled
boolean
If user has MFA enabled.
modified_at
date-time
Time that the user was last modified.
name
string
Name of the user.
service_account
boolean
Whether the user is a service account.
status
string
Status of the user.
title
string
Title of the user.
verified
boolean
Whether the user is verified.
id
string
ID of the user.
relationships
object
Relationships of the user object returned by the API.
org
object
Relationship to an organization.
data [_required_]
object
Relationship to organization object.
id [_required_]
string
ID of the organization.
type [_required_]
enum
Organizations resource type. Allowed enum values: `orgs`
default: `orgs`
other_orgs
object
Relationship to organizations.
data [_required_]
[object]
Relationships to organization objects.
id [_required_]
string
ID of the organization.
type [_required_]
enum
Organizations resource type. Allowed enum values: `orgs`
default: `orgs`
other_users
object
Relationship to users.
data [_required_]
[object]
Relationships to user objects.
id [_required_]
string
A unique identifier that represents the user.
type [_required_]
enum
Users resource type. Allowed enum values: `users`
default: `users`
roles
object
Relationship to roles.
data
[object]
An array containing type and the unique identifier of a role.
id
string
The unique identifier of the role.
type
enum
Roles type. Allowed enum values: `roles`
default: `roles`
type
enum
Users resource type. Allowed enum values: `users`
default: `users`
```
{
  "data": {
    "attributes": {
      "conditional_recipients": {
        "conditions": [
          {
            "recipients": [
              "slack-test-channel",
              "jira-test"
            ],
            "scope": "transition_type:alert"
          }
        ],
        "fallback_recipients": [
          "slack-test-channel",
          "jira-test"
        ]
      },
      "created": "2020-01-02T03:04:00.000Z",
      "filter": {
        "tags": [
          "team:product",
          "host:abc"
        ]
      },
      "modified": "2020-01-02T03:04:00.000Z",
      "name": "A notification rule name",
      "recipients": [
        "slack-test-channel",
        "jira-test"
      ]
    },
    "id": "00000000-0000-1234-0000-000000000000",
    "relationships": {
      "created_by": {
        "data": {
          "id": "00000000-0000-1234-0000-000000000000",
          "type": "users"
        }
      }
    },
    "type": "monitor-notification-rule"
  },
  "included": [
    {
      "attributes": {
        "created_at": "2019-09-19T10:00:00.000Z",
        "disabled": false,
        "email": "string",
        "handle": "string",
        "icon": "string",
        "last_login_time": "2019-09-19T10:00:00.000Z",
        "mfa_enabled": false,
        "modified_at": "2019-09-19T10:00:00.000Z",
        "name": "string",
        "service_account": false,
        "status": "string",
        "title": "string",
        "verified": false
      },
      "id": "string",
      "relationships": {
        "org": {
          "data": {
            "id": "00000000-0000-beef-0000-000000000000",
            "type": "orgs"
          }
        },
        "other_orgs": {
          "data": [
            {
              "id": "00000000-0000-beef-0000-000000000000",
              "type": "orgs"
            }
          ]
        },
        "other_users": {
          "data": [
            {
              "id": "00000000-0000-0000-2345-000000000000",
              "type": "users"
            }
          ]
        },
        "roles": {
          "data": [
            {
              "id": "3653d3c6-0c75-11ea-ad28-fb5701eabc7d",
              "type": "roles"
            }
          ]
        }
      },
      "type": "users"
    }
  ]
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


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
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


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
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


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
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/monitors/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/monitors/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/monitors/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/monitors/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/monitors/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/monitors/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/monitors/?code-lang=typescript)


#####  Update a monitor notification rule returns "OK" response
Copy
```
                          # Path parameters  
export rule_id="CHANGE_ME"  
# Curl command  
curl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/monitor/notification_rule/${rule_id}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "filter": {
        "tags": [
          "test:example-monitor",
          "host:abc"
        ]
      },
      "name": "updated rule",
      "recipients": [
        "slack-test-channel"
      ]
    },
    "id": "00000000-0000-1234-0000-000000000000",
    "type": "monitor-notification-rule"
  }
}
EOF  

                        
```

#####  Update a monitor notification rule with conditional_recipients returns "OK" response
Copy
```
                          # Path parameters  
export rule_id="CHANGE_ME"  
# Curl command  
curl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/monitor/notification_rule/${rule_id}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "filter": {
        "tags": [
          "test:example-monitor",
          "host:abc"
        ]
      },
      "name": "updated rule",
      "conditional_recipients": {
        "conditions": [
          {
            "scope": "transition_type:is_alert",
            "recipients": [
              "slack-test-channel",
              "jira-test"
            ]
          }
        ]
      }
    },
    "id": "00000000-0000-1234-0000-000000000000",
    "type": "monitor-notification-rule"
  }
}
EOF  

                        
```

#####  Update a monitor notification rule with scope returns "OK" response
Copy
```
                          # Path parameters  
export rule_id="CHANGE_ME"  
# Curl command  
curl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/monitor/notification_rule/${rule_id}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "filter": {
        "scope": "test:example-monitor"
      },
      "name": "updated rule",
      "recipients": [
        "slack-test-channel"
      ]
    },
    "id": "00000000-0000-1234-0000-000000000000",
    "type": "monitor-notification-rule"
  }
}
EOF  

                        
```

#####  Update a monitor notification rule returns "OK" response 
```
// Update a monitor notification rule returns "OK" response

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
	// there is a valid "monitor_notification_rule" in the system
	MonitorNotificationRuleDataID := os.Getenv("MONITOR_NOTIFICATION_RULE_DATA_ID")

	body := datadogV2.MonitorNotificationRuleUpdateRequest{
		Data: datadogV2.MonitorNotificationRuleUpdateRequestData{
			Attributes: datadogV2.MonitorNotificationRuleAttributes{
				Filter: &datadogV2.MonitorNotificationRuleFilter{
					MonitorNotificationRuleFilterTags: &datadogV2.MonitorNotificationRuleFilterTags{
						Tags: []string{
							"test:example-monitor",
							"host:abc",
						},
					}},
				Name: "updated rule",
				Recipients: []string{
					"slack-test-channel",
				},
			},
			Id:   MonitorNotificationRuleDataID,
			Type: datadogV2.MONITORNOTIFICATIONRULERESOURCETYPE_MONITOR_NOTIFICATION_RULE.Ptr(),
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewMonitorsApi(apiClient)
	resp, r, err := api.UpdateMonitorNotificationRule(ctx, MonitorNotificationRuleDataID, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `MonitorsApi.UpdateMonitorNotificationRule`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `MonitorsApi.UpdateMonitorNotificationRule`:\n%s\n", responseContent)
}

```

Copy
#####  Update a monitor notification rule with conditional_recipients returns "OK" response 
```
// Update a monitor notification rule with conditional_recipients returns "OK" response

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
	// there is a valid "monitor_notification_rule" in the system
	MonitorNotificationRuleDataID := os.Getenv("MONITOR_NOTIFICATION_RULE_DATA_ID")

	body := datadogV2.MonitorNotificationRuleUpdateRequest{
		Data: datadogV2.MonitorNotificationRuleUpdateRequestData{
			Attributes: datadogV2.MonitorNotificationRuleAttributes{
				Filter: &datadogV2.MonitorNotificationRuleFilter{
					MonitorNotificationRuleFilterTags: &datadogV2.MonitorNotificationRuleFilterTags{
						Tags: []string{
							"test:example-monitor",
							"host:abc",
						},
					}},
				Name: "updated rule",
				ConditionalRecipients: &datadogV2.MonitorNotificationRuleConditionalRecipients{
					Conditions: []datadogV2.MonitorNotificationRuleCondition{
						{
							Scope: "transition_type:is_alert",
							Recipients: []string{
								"slack-test-channel",
								"jira-test",
							},
						},
					},
				},
			},
			Id:   MonitorNotificationRuleDataID,
			Type: datadogV2.MONITORNOTIFICATIONRULERESOURCETYPE_MONITOR_NOTIFICATION_RULE.Ptr(),
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewMonitorsApi(apiClient)
	resp, r, err := api.UpdateMonitorNotificationRule(ctx, MonitorNotificationRuleDataID, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `MonitorsApi.UpdateMonitorNotificationRule`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `MonitorsApi.UpdateMonitorNotificationRule`:\n%s\n", responseContent)
}

```

Copy
#####  Update a monitor notification rule with scope returns "OK" response 
```
// Update a monitor notification rule with scope returns "OK" response

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
	// there is a valid "monitor_notification_rule" in the system
	MonitorNotificationRuleDataID := os.Getenv("MONITOR_NOTIFICATION_RULE_DATA_ID")

	body := datadogV2.MonitorNotificationRuleUpdateRequest{
		Data: datadogV2.MonitorNotificationRuleUpdateRequestData{
			Attributes: datadogV2.MonitorNotificationRuleAttributes{
				Filter: &datadogV2.MonitorNotificationRuleFilter{
					MonitorNotificationRuleFilterScope: &datadogV2.MonitorNotificationRuleFilterScope{
						Scope: "test:example-monitor",
					}},
				Name: "updated rule",
				Recipients: []string{
					"slack-test-channel",
				},
			},
			Id:   MonitorNotificationRuleDataID,
			Type: datadogV2.MONITORNOTIFICATIONRULERESOURCETYPE_MONITOR_NOTIFICATION_RULE.Ptr(),
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewMonitorsApi(apiClient)
	resp, r, err := api.UpdateMonitorNotificationRule(ctx, MonitorNotificationRuleDataID, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `MonitorsApi.UpdateMonitorNotificationRule`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `MonitorsApi.UpdateMonitorNotificationRule`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Update a monitor notification rule returns "OK" response 
```
// Update a monitor notification rule returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.MonitorsApi;
import com.datadog.api.client.v2.model.MonitorNotificationRuleAttributes;
import com.datadog.api.client.v2.model.MonitorNotificationRuleFilter;
import com.datadog.api.client.v2.model.MonitorNotificationRuleFilterTags;
import com.datadog.api.client.v2.model.MonitorNotificationRuleResourceType;
import com.datadog.api.client.v2.model.MonitorNotificationRuleResponse;
import com.datadog.api.client.v2.model.MonitorNotificationRuleUpdateRequest;
import com.datadog.api.client.v2.model.MonitorNotificationRuleUpdateRequestData;
import java.util.Arrays;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    MonitorsApi apiInstance = new MonitorsApi(defaultClient);

    // there is a valid "monitor_notification_rule" in the system
    String MONITOR_NOTIFICATION_RULE_DATA_ID = System.getenv("MONITOR_NOTIFICATION_RULE_DATA_ID");

    MonitorNotificationRuleUpdateRequest body =
        new MonitorNotificationRuleUpdateRequest()
            .data(
                new MonitorNotificationRuleUpdateRequestData()
                    .attributes(
                        new MonitorNotificationRuleAttributes()
                            .filter(
                                new MonitorNotificationRuleFilter(
                                    new MonitorNotificationRuleFilterTags()
                                        .tags(Arrays.asList("test:example-monitor", "host:abc"))))
                            .name("updated rule")
                            .recipients(Collections.singletonList("slack-test-channel")))
                    .id(MONITOR_NOTIFICATION_RULE_DATA_ID)
                    .type(MonitorNotificationRuleResourceType.MONITOR_NOTIFICATION_RULE));

    try {
      MonitorNotificationRuleResponse result =
          apiInstance.updateMonitorNotificationRule(MONITOR_NOTIFICATION_RULE_DATA_ID, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MonitorsApi#updateMonitorNotificationRule");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}

```

Copy
#####  Update a monitor notification rule with conditional_recipients returns "OK" response 
```
// Update a monitor notification rule with conditional_recipients returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.MonitorsApi;
import com.datadog.api.client.v2.model.MonitorNotificationRuleAttributes;
import com.datadog.api.client.v2.model.MonitorNotificationRuleCondition;
import com.datadog.api.client.v2.model.MonitorNotificationRuleConditionalRecipients;
import com.datadog.api.client.v2.model.MonitorNotificationRuleFilter;
import com.datadog.api.client.v2.model.MonitorNotificationRuleFilterTags;
import com.datadog.api.client.v2.model.MonitorNotificationRuleResourceType;
import com.datadog.api.client.v2.model.MonitorNotificationRuleResponse;
import com.datadog.api.client.v2.model.MonitorNotificationRuleUpdateRequest;
import com.datadog.api.client.v2.model.MonitorNotificationRuleUpdateRequestData;
import java.util.Arrays;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    MonitorsApi apiInstance = new MonitorsApi(defaultClient);

    // there is a valid "monitor_notification_rule" in the system
    String MONITOR_NOTIFICATION_RULE_DATA_ID = System.getenv("MONITOR_NOTIFICATION_RULE_DATA_ID");

    MonitorNotificationRuleUpdateRequest body =
        new MonitorNotificationRuleUpdateRequest()
            .data(
                new MonitorNotificationRuleUpdateRequestData()
                    .attributes(
                        new MonitorNotificationRuleAttributes()
                            .filter(
                                new MonitorNotificationRuleFilter(
                                    new MonitorNotificationRuleFilterTags()
                                        .tags(Arrays.asList("test:example-monitor", "host:abc"))))
                            .name("updated rule")
                            .conditionalRecipients(
                                new MonitorNotificationRuleConditionalRecipients()
                                    .conditions(
                                        Collections.singletonList(
                                            new MonitorNotificationRuleCondition()
                                                .scope("transition_type:is_alert")
                                                .recipients(
                                                    Arrays.asList(
                                                        "slack-test-channel", "jira-test"))))))
                    .id(MONITOR_NOTIFICATION_RULE_DATA_ID)
                    .type(MonitorNotificationRuleResourceType.MONITOR_NOTIFICATION_RULE));

    try {
      MonitorNotificationRuleResponse result =
          apiInstance.updateMonitorNotificationRule(MONITOR_NOTIFICATION_RULE_DATA_ID, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MonitorsApi#updateMonitorNotificationRule");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}

```

Copy
#####  Update a monitor notification rule with scope returns "OK" response 
```
// Update a monitor notification rule with scope returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.MonitorsApi;
import com.datadog.api.client.v2.model.MonitorNotificationRuleAttributes;
import com.datadog.api.client.v2.model.MonitorNotificationRuleFilter;
import com.datadog.api.client.v2.model.MonitorNotificationRuleFilterScope;
import com.datadog.api.client.v2.model.MonitorNotificationRuleResourceType;
import com.datadog.api.client.v2.model.MonitorNotificationRuleResponse;
import com.datadog.api.client.v2.model.MonitorNotificationRuleUpdateRequest;
import com.datadog.api.client.v2.model.MonitorNotificationRuleUpdateRequestData;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    MonitorsApi apiInstance = new MonitorsApi(defaultClient);

    // there is a valid "monitor_notification_rule" in the system
    String MONITOR_NOTIFICATION_RULE_DATA_ID = System.getenv("MONITOR_NOTIFICATION_RULE_DATA_ID");

    MonitorNotificationRuleUpdateRequest body =
        new MonitorNotificationRuleUpdateRequest()
            .data(
                new MonitorNotificationRuleUpdateRequestData()
                    .attributes(
                        new MonitorNotificationRuleAttributes()
                            .filter(
                                new MonitorNotificationRuleFilter(
                                    new MonitorNotificationRuleFilterScope()
                                        .scope("test:example-monitor")))
                            .name("updated rule")
                            .recipients(Collections.singletonList("slack-test-channel")))
                    .id(MONITOR_NOTIFICATION_RULE_DATA_ID)
                    .type(MonitorNotificationRuleResourceType.MONITOR_NOTIFICATION_RULE));

    try {
      MonitorNotificationRuleResponse result =
          apiInstance.updateMonitorNotificationRule(MONITOR_NOTIFICATION_RULE_DATA_ID, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MonitorsApi#updateMonitorNotificationRule");
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

#####  Update a monitor notification rule returns "OK" response 
```
"""
Update a monitor notification rule returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.monitors_api import MonitorsApi
from datadog_api_client.v2.model.monitor_notification_rule_attributes import MonitorNotificationRuleAttributes
from datadog_api_client.v2.model.monitor_notification_rule_filter_tags import MonitorNotificationRuleFilterTags
from datadog_api_client.v2.model.monitor_notification_rule_resource_type import MonitorNotificationRuleResourceType
from datadog_api_client.v2.model.monitor_notification_rule_update_request import MonitorNotificationRuleUpdateRequest
from datadog_api_client.v2.model.monitor_notification_rule_update_request_data import (
    MonitorNotificationRuleUpdateRequestData,
)

# there is a valid "monitor_notification_rule" in the system
MONITOR_NOTIFICATION_RULE_DATA_ID = environ["MONITOR_NOTIFICATION_RULE_DATA_ID"]

body = MonitorNotificationRuleUpdateRequest(
    data=MonitorNotificationRuleUpdateRequestData(
        attributes=MonitorNotificationRuleAttributes(
            filter=MonitorNotificationRuleFilterTags(
                tags=[
                    "test:example-monitor",
                    "host:abc",
                ],
            ),
            name="updated rule",
            recipients=[
                "slack-test-channel",
            ],
        ),
        id=MONITOR_NOTIFICATION_RULE_DATA_ID,
        type=MonitorNotificationRuleResourceType.MONITOR_NOTIFICATION_RULE,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MonitorsApi(api_client)
    response = api_instance.update_monitor_notification_rule(rule_id=MONITOR_NOTIFICATION_RULE_DATA_ID, body=body)

    print(response)

```

Copy
#####  Update a monitor notification rule with conditional_recipients returns "OK" response 
```
"""
Update a monitor notification rule with conditional_recipients returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.monitors_api import MonitorsApi
from datadog_api_client.v2.model.monitor_notification_rule_attributes import MonitorNotificationRuleAttributes
from datadog_api_client.v2.model.monitor_notification_rule_condition import MonitorNotificationRuleCondition
from datadog_api_client.v2.model.monitor_notification_rule_conditional_recipients import (
    MonitorNotificationRuleConditionalRecipients,
)
from datadog_api_client.v2.model.monitor_notification_rule_filter_tags import MonitorNotificationRuleFilterTags
from datadog_api_client.v2.model.monitor_notification_rule_resource_type import MonitorNotificationRuleResourceType
from datadog_api_client.v2.model.monitor_notification_rule_update_request import MonitorNotificationRuleUpdateRequest
from datadog_api_client.v2.model.monitor_notification_rule_update_request_data import (
    MonitorNotificationRuleUpdateRequestData,
)

# there is a valid "monitor_notification_rule" in the system
MONITOR_NOTIFICATION_RULE_DATA_ID = environ["MONITOR_NOTIFICATION_RULE_DATA_ID"]

body = MonitorNotificationRuleUpdateRequest(
    data=MonitorNotificationRuleUpdateRequestData(
        attributes=MonitorNotificationRuleAttributes(
            filter=MonitorNotificationRuleFilterTags(
                tags=[
                    "test:example-monitor",
                    "host:abc",
                ],
            ),
            name="updated rule",
            conditional_recipients=MonitorNotificationRuleConditionalRecipients(
                conditions=[
                    MonitorNotificationRuleCondition(
                        scope="transition_type:is_alert",
                        recipients=[
                            "slack-test-channel",
                            "jira-test",
                        ],
                    ),
                ],
            ),
        ),
        id=MONITOR_NOTIFICATION_RULE_DATA_ID,
        type=MonitorNotificationRuleResourceType.MONITOR_NOTIFICATION_RULE,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MonitorsApi(api_client)
    response = api_instance.update_monitor_notification_rule(rule_id=MONITOR_NOTIFICATION_RULE_DATA_ID, body=body)

    print(response)

```

Copy
#####  Update a monitor notification rule with scope returns "OK" response 
```
"""
Update a monitor notification rule with scope returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.monitors_api import MonitorsApi
from datadog_api_client.v2.model.monitor_notification_rule_attributes import MonitorNotificationRuleAttributes
from datadog_api_client.v2.model.monitor_notification_rule_filter_scope import MonitorNotificationRuleFilterScope
from datadog_api_client.v2.model.monitor_notification_rule_resource_type import MonitorNotificationRuleResourceType
from datadog_api_client.v2.model.monitor_notification_rule_update_request import MonitorNotificationRuleUpdateRequest
from datadog_api_client.v2.model.monitor_notification_rule_update_request_data import (
    MonitorNotificationRuleUpdateRequestData,
)

# there is a valid "monitor_notification_rule" in the system
MONITOR_NOTIFICATION_RULE_DATA_ID = environ["MONITOR_NOTIFICATION_RULE_DATA_ID"]

body = MonitorNotificationRuleUpdateRequest(
    data=MonitorNotificationRuleUpdateRequestData(
        attributes=MonitorNotificationRuleAttributes(
            filter=MonitorNotificationRuleFilterScope(
                scope="test:example-monitor",
            ),
            name="updated rule",
            recipients=[
                "slack-test-channel",
            ],
        ),
        id=MONITOR_NOTIFICATION_RULE_DATA_ID,
        type=MonitorNotificationRuleResourceType.MONITOR_NOTIFICATION_RULE,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MonitorsApi(api_client)
    response = api_instance.update_monitor_notification_rule(rule_id=MONITOR_NOTIFICATION_RULE_DATA_ID, body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Update a monitor notification rule returns "OK" response 
```
# Update a monitor notification rule returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::MonitorsAPI.new

# there is a valid "monitor_notification_rule" in the system
MONITOR_NOTIFICATION_RULE_DATA_ID = ENV["MONITOR_NOTIFICATION_RULE_DATA_ID"]

body = DatadogAPIClient::V2::MonitorNotificationRuleUpdateRequest.new({
  data: DatadogAPIClient::V2::MonitorNotificationRuleUpdateRequestData.new({
    attributes: DatadogAPIClient::V2::MonitorNotificationRuleAttributes.new({
      filter: DatadogAPIClient::V2::MonitorNotificationRuleFilterTags.new({
        tags: [
          "test:example-monitor",
          "host:abc",
        ],
      }),
      name: "updated rule",
      recipients: [
        "slack-test-channel",
      ],
    }),
    id: MONITOR_NOTIFICATION_RULE_DATA_ID,
    type: DatadogAPIClient::V2::MonitorNotificationRuleResourceType::MONITOR_NOTIFICATION_RULE,
  }),
})
p api_instance.update_monitor_notification_rule(MONITOR_NOTIFICATION_RULE_DATA_ID, body)

```

Copy
#####  Update a monitor notification rule with conditional_recipients returns "OK" response 
```
# Update a monitor notification rule with conditional_recipients returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::MonitorsAPI.new

# there is a valid "monitor_notification_rule" in the system
MONITOR_NOTIFICATION_RULE_DATA_ID = ENV["MONITOR_NOTIFICATION_RULE_DATA_ID"]

body = DatadogAPIClient::V2::MonitorNotificationRuleUpdateRequest.new({
  data: DatadogAPIClient::V2::MonitorNotificationRuleUpdateRequestData.new({
    attributes: DatadogAPIClient::V2::MonitorNotificationRuleAttributes.new({
      filter: DatadogAPIClient::V2::MonitorNotificationRuleFilterTags.new({
        tags: [
          "test:example-monitor",
          "host:abc",
        ],
      }),
      name: "updated rule",
      conditional_recipients: DatadogAPIClient::V2::MonitorNotificationRuleConditionalRecipients.new({
        conditions: [
          DatadogAPIClient::V2::MonitorNotificationRuleCondition.new({
            scope: "transition_type:is_alert",
            recipients: [
              "slack-test-channel",
              "jira-test",
            ],
          }),
        ],
      }),
    }),
    id: MONITOR_NOTIFICATION_RULE_DATA_ID,
    type: DatadogAPIClient::V2::MonitorNotificationRuleResourceType::MONITOR_NOTIFICATION_RULE,
  }),
})
p api_instance.update_monitor_notification_rule(MONITOR_NOTIFICATION_RULE_DATA_ID, body)

```

Copy
#####  Update a monitor notification rule with scope returns "OK" response 
```
# Update a monitor notification rule with scope returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::MonitorsAPI.new

# there is a valid "monitor_notification_rule" in the system
MONITOR_NOTIFICATION_RULE_DATA_ID = ENV["MONITOR_NOTIFICATION_RULE_DATA_ID"]

body = DatadogAPIClient::V2::MonitorNotificationRuleUpdateRequest.new({
  data: DatadogAPIClient::V2::MonitorNotificationRuleUpdateRequestData.new({
    attributes: DatadogAPIClient::V2::MonitorNotificationRuleAttributes.new({
      filter: DatadogAPIClient::V2::MonitorNotificationRuleFilterScope.new({
        scope: "test:example-monitor",
      }),
      name: "updated rule",
      recipients: [
        "slack-test-channel",
      ],
    }),
    id: MONITOR_NOTIFICATION_RULE_DATA_ID,
    type: DatadogAPIClient::V2::MonitorNotificationRuleResourceType::MONITOR_NOTIFICATION_RULE,
  }),
})
p api_instance.update_monitor_notification_rule(MONITOR_NOTIFICATION_RULE_DATA_ID, body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Update a monitor notification rule returns "OK" response 
```
// Update a monitor notification rule returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_monitors::MonitorsAPI;
use datadog_api_client::datadogV2::model::MonitorNotificationRuleAttributes;
use datadog_api_client::datadogV2::model::MonitorNotificationRuleFilter;
use datadog_api_client::datadogV2::model::MonitorNotificationRuleFilterTags;
use datadog_api_client::datadogV2::model::MonitorNotificationRuleResourceType;
use datadog_api_client::datadogV2::model::MonitorNotificationRuleUpdateRequest;
use datadog_api_client::datadogV2::model::MonitorNotificationRuleUpdateRequestData;

#[tokio::main]
async fn main() {
    // there is a valid "monitor_notification_rule" in the system
    let monitor_notification_rule_data_id =
        std::env::var("MONITOR_NOTIFICATION_RULE_DATA_ID").unwrap();
    let body = MonitorNotificationRuleUpdateRequest::new(
        MonitorNotificationRuleUpdateRequestData::new(
            MonitorNotificationRuleAttributes::new("updated rule".to_string())
                .filter(
                    MonitorNotificationRuleFilter::MonitorNotificationRuleFilterTags(Box::new(
                        MonitorNotificationRuleFilterTags::new(vec![
                            "test:example-monitor".to_string(),
                            "host:abc".to_string(),
                        ]),
                    )),
                )
                .recipients(vec!["slack-test-channel".to_string()]),
            monitor_notification_rule_data_id.clone(),
        )
        .type_(MonitorNotificationRuleResourceType::MONITOR_NOTIFICATION_RULE),
    );
    let configuration = datadog::Configuration::new();
    let api = MonitorsAPI::with_config(configuration);
    let resp = api
        .update_monitor_notification_rule(monitor_notification_rule_data_id.clone(), body)
        .await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}

```

Copy
#####  Update a monitor notification rule with conditional_recipients returns "OK" response 
```
// Update a monitor notification rule with conditional_recipients returns "OK"
// response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_monitors::MonitorsAPI;
use datadog_api_client::datadogV2::model::MonitorNotificationRuleAttributes;
use datadog_api_client::datadogV2::model::MonitorNotificationRuleCondition;
use datadog_api_client::datadogV2::model::MonitorNotificationRuleConditionalRecipients;
use datadog_api_client::datadogV2::model::MonitorNotificationRuleFilter;
use datadog_api_client::datadogV2::model::MonitorNotificationRuleFilterTags;
use datadog_api_client::datadogV2::model::MonitorNotificationRuleResourceType;
use datadog_api_client::datadogV2::model::MonitorNotificationRuleUpdateRequest;
use datadog_api_client::datadogV2::model::MonitorNotificationRuleUpdateRequestData;

#[tokio::main]
async fn main() {
    // there is a valid "monitor_notification_rule" in the system
    let monitor_notification_rule_data_id =
        std::env::var("MONITOR_NOTIFICATION_RULE_DATA_ID").unwrap();
    let body = MonitorNotificationRuleUpdateRequest::new(
        MonitorNotificationRuleUpdateRequestData::new(
            MonitorNotificationRuleAttributes::new("updated rule".to_string())
                .conditional_recipients(MonitorNotificationRuleConditionalRecipients::new(vec![
                    MonitorNotificationRuleCondition::new(
                        vec!["slack-test-channel".to_string(), "jira-test".to_string()],
                        "transition_type:is_alert".to_string(),
                    ),
                ]))
                .filter(
                    MonitorNotificationRuleFilter::MonitorNotificationRuleFilterTags(Box::new(
                        MonitorNotificationRuleFilterTags::new(vec![
                            "test:example-monitor".to_string(),
                            "host:abc".to_string(),
                        ]),
                    )),
                ),
            monitor_notification_rule_data_id.clone(),
        )
        .type_(MonitorNotificationRuleResourceType::MONITOR_NOTIFICATION_RULE),
    );
    let configuration = datadog::Configuration::new();
    let api = MonitorsAPI::with_config(configuration);
    let resp = api
        .update_monitor_notification_rule(monitor_notification_rule_data_id.clone(), body)
        .await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}

```

Copy
#####  Update a monitor notification rule with scope returns "OK" response 
```
// Update a monitor notification rule with scope returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_monitors::MonitorsAPI;
use datadog_api_client::datadogV2::model::MonitorNotificationRuleAttributes;
use datadog_api_client::datadogV2::model::MonitorNotificationRuleFilter;
use datadog_api_client::datadogV2::model::MonitorNotificationRuleFilterScope;
use datadog_api_client::datadogV2::model::MonitorNotificationRuleResourceType;
use datadog_api_client::datadogV2::model::MonitorNotificationRuleUpdateRequest;
use datadog_api_client::datadogV2::model::MonitorNotificationRuleUpdateRequestData;

#[tokio::main]
async fn main() {
    // there is a valid "monitor_notification_rule" in the system
    let monitor_notification_rule_data_id =
        std::env::var("MONITOR_NOTIFICATION_RULE_DATA_ID").unwrap();
    let body = MonitorNotificationRuleUpdateRequest::new(
        MonitorNotificationRuleUpdateRequestData::new(
            MonitorNotificationRuleAttributes::new("updated rule".to_string())
                .filter(
                    MonitorNotificationRuleFilter::MonitorNotificationRuleFilterScope(Box::new(
                        MonitorNotificationRuleFilterScope::new("test:example-monitor".to_string()),
                    )),
                )
                .recipients(vec!["slack-test-channel".to_string()]),
            monitor_notification_rule_data_id.clone(),
        )
        .type_(MonitorNotificationRuleResourceType::MONITOR_NOTIFICATION_RULE),
    );
    let configuration = datadog::Configuration::new();
    let api = MonitorsAPI::with_config(configuration);
    let resp = api
        .update_monitor_notification_rule(monitor_notification_rule_data_id.clone(), body)
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

#####  Update a monitor notification rule returns "OK" response 
```
/**
 * Update a monitor notification rule returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.MonitorsApi(configuration);

// there is a valid "monitor_notification_rule" in the system
const MONITOR_NOTIFICATION_RULE_DATA_ID = process.env
  .MONITOR_NOTIFICATION_RULE_DATA_ID as string;

const params: v2.MonitorsApiUpdateMonitorNotificationRuleRequest = {
  body: {
    data: {
      attributes: {
        filter: {
          tags: ["test:example-monitor", "host:abc"],
        },
        name: "updated rule",
        recipients: ["slack-test-channel"],
      },
      id: MONITOR_NOTIFICATION_RULE_DATA_ID,
      type: "monitor-notification-rule",
    },
  },
  ruleId: MONITOR_NOTIFICATION_RULE_DATA_ID,
};

apiInstance
  .updateMonitorNotificationRule(params)
  .then((data: v2.MonitorNotificationRuleResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));

```

Copy
#####  Update a monitor notification rule with conditional_recipients returns "OK" response 
```
/**
 * Update a monitor notification rule with conditional_recipients returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.MonitorsApi(configuration);

// there is a valid "monitor_notification_rule" in the system
const MONITOR_NOTIFICATION_RULE_DATA_ID = process.env
  .MONITOR_NOTIFICATION_RULE_DATA_ID as string;

const params: v2.MonitorsApiUpdateMonitorNotificationRuleRequest = {
  body: {
    data: {
      attributes: {
        filter: {
          tags: ["test:example-monitor", "host:abc"],
        },
        name: "updated rule",
        conditionalRecipients: {
          conditions: [
            {
              scope: "transition_type:is_alert",
              recipients: ["slack-test-channel", "jira-test"],
            },
          ],
        },
      },
      id: MONITOR_NOTIFICATION_RULE_DATA_ID,
      type: "monitor-notification-rule",
    },
  },
  ruleId: MONITOR_NOTIFICATION_RULE_DATA_ID,
};

apiInstance
  .updateMonitorNotificationRule(params)
  .then((data: v2.MonitorNotificationRuleResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));

```

Copy
#####  Update a monitor notification rule with scope returns "OK" response 
```
/**
 * Update a monitor notification rule with scope returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.MonitorsApi(configuration);

// there is a valid "monitor_notification_rule" in the system
const MONITOR_NOTIFICATION_RULE_DATA_ID = process.env
  .MONITOR_NOTIFICATION_RULE_DATA_ID as string;

const params: v2.MonitorsApiUpdateMonitorNotificationRuleRequest = {
  body: {
    data: {
      attributes: {
        filter: {
          scope: "test:example-monitor",
        },
        name: "updated rule",
        recipients: ["slack-test-channel"],
      },
      id: MONITOR_NOTIFICATION_RULE_DATA_ID,
      type: "monitor-notification-rule",
    },
  },
  ruleId: MONITOR_NOTIFICATION_RULE_DATA_ID,
};

apiInstance
  .updateMonitorNotificationRule(params)
  .then((data: v2.MonitorNotificationRuleResponse) => {
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
## [Delete a monitor notification rule](https://docs.datadoghq.com/api/latest/monitors/#delete-a-monitor-notification-rule)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/monitors/#delete-a-monitor-notification-rule-v2)


DELETE https://api.ap1.datadoghq.com/api/v2/monitor/notification_rule/{rule_id}https://api.ap2.datadoghq.com/api/v2/monitor/notification_rule/{rule_id}https://api.datadoghq.eu/api/v2/monitor/notification_rule/{rule_id}https://api.ddog-gov.com/api/v2/monitor/notification_rule/{rule_id}https://api.datadoghq.com/api/v2/monitor/notification_rule/{rule_id}https://api.us3.datadoghq.com/api/v2/monitor/notification_rule/{rule_id}https://api.us5.datadoghq.com/api/v2/monitor/notification_rule/{rule_id}
### Overview
Deletes a monitor notification rule by `rule_id`. This endpoint requires the `monitor_config_policy_write` permission.
### Arguments
#### Path Parameters
Name
Type
Description
rule_id [_required_]
string
ID of the monitor notification rule to delete.
### Response
  * [204](https://docs.datadoghq.com/api/latest/monitors/#DeleteMonitorNotificationRule-204-v2)
  * [403](https://docs.datadoghq.com/api/latest/monitors/#DeleteMonitorNotificationRule-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/monitors/#DeleteMonitorNotificationRule-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/monitors/#DeleteMonitorNotificationRule-429-v2)


OK
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


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
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


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
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/monitors/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/monitors/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/monitors/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/monitors/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/monitors/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/monitors/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/monitors/?code-lang=typescript)


#####  Delete a monitor notification rule
Copy
```
                  # Path parameters  
export rule_id="CHANGE_ME"  
# Curl command  
curl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/monitor/notification_rule/${rule_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Delete a monitor notification rule
```
"""
Delete a monitor notification rule returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.monitors_api import MonitorsApi

# there is a valid "monitor_notification_rule" in the system
MONITOR_NOTIFICATION_RULE_DATA_ID = environ["MONITOR_NOTIFICATION_RULE_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MonitorsApi(api_client)
    api_instance.delete_monitor_notification_rule(
        rule_id=MONITOR_NOTIFICATION_RULE_DATA_ID,
    )

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Delete a monitor notification rule
```
# Delete a monitor notification rule returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::MonitorsAPI.new

# there is a valid "monitor_notification_rule" in the system
MONITOR_NOTIFICATION_RULE_DATA_ID = ENV["MONITOR_NOTIFICATION_RULE_DATA_ID"]
api_instance.delete_monitor_notification_rule(MONITOR_NOTIFICATION_RULE_DATA_ID)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Delete a monitor notification rule
```
// Delete a monitor notification rule returns "OK" response

package main

import (
	"context"
	"fmt"
	"os"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
	// there is a valid "monitor_notification_rule" in the system
	MonitorNotificationRuleDataID := os.Getenv("MONITOR_NOTIFICATION_RULE_DATA_ID")

	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewMonitorsApi(apiClient)
	r, err := api.DeleteMonitorNotificationRule(ctx, MonitorNotificationRuleDataID)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `MonitorsApi.DeleteMonitorNotificationRule`: %v\n", err)
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

#####  Delete a monitor notification rule
```
// Delete a monitor notification rule returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.MonitorsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    MonitorsApi apiInstance = new MonitorsApi(defaultClient);

    // there is a valid "monitor_notification_rule" in the system
    String MONITOR_NOTIFICATION_RULE_DATA_ID = System.getenv("MONITOR_NOTIFICATION_RULE_DATA_ID");

    try {
      apiInstance.deleteMonitorNotificationRule(MONITOR_NOTIFICATION_RULE_DATA_ID);
    } catch (ApiException e) {
      System.err.println("Exception when calling MonitorsApi#deleteMonitorNotificationRule");
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

#####  Delete a monitor notification rule
```
// Delete a monitor notification rule returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_monitors::MonitorsAPI;

#[tokio::main]
async fn main() {
    // there is a valid "monitor_notification_rule" in the system
    let monitor_notification_rule_data_id =
        std::env::var("MONITOR_NOTIFICATION_RULE_DATA_ID").unwrap();
    let configuration = datadog::Configuration::new();
    let api = MonitorsAPI::with_config(configuration);
    let resp = api
        .delete_monitor_notification_rule(monitor_notification_rule_data_id.clone())
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

#####  Delete a monitor notification rule
```
/**
 * Delete a monitor notification rule returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.MonitorsApi(configuration);

// there is a valid "monitor_notification_rule" in the system
const MONITOR_NOTIFICATION_RULE_DATA_ID = process.env
  .MONITOR_NOTIFICATION_RULE_DATA_ID as string;

const params: v2.MonitorsApiDeleteMonitorNotificationRuleRequest = {
  ruleId: MONITOR_NOTIFICATION_RULE_DATA_ID,
};

apiInstance
  .deleteMonitorNotificationRule(params)
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
## [Get a monitor user template](https://docs.datadoghq.com/api/latest/monitors/#get-a-monitor-user-template)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/monitors/#get-a-monitor-user-template-v2)


**Note** : This endpoint is in Preview. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
GET https://api.ap1.datadoghq.com/api/v2/monitor/template/{template_id}https://api.ap2.datadoghq.com/api/v2/monitor/template/{template_id}https://api.datadoghq.eu/api/v2/monitor/template/{template_id}https://api.ddog-gov.com/api/v2/monitor/template/{template_id}https://api.datadoghq.com/api/v2/monitor/template/{template_id}https://api.us3.datadoghq.com/api/v2/monitor/template/{template_id}https://api.us5.datadoghq.com/api/v2/monitor/template/{template_id}
### Overview
Retrieve a monitor user template by its ID. This endpoint requires the `monitors_read` permission.
OAuth apps require the `monitors_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#monitors) to access this endpoint.
### Arguments
#### Path Parameters
Name
Type
Description
template_id [_required_]
string
ID of the monitor user template.
#### Query Strings
Name
Type
Description
with_all_versions
boolean
Whether to include all versions of the template in the response in the versions field.
### Response
  * [200](https://docs.datadoghq.com/api/latest/monitors/#GetMonitorUserTemplate-200-v2)
  * [404](https://docs.datadoghq.com/api/latest/monitors/#GetMonitorUserTemplate-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/monitors/#GetMonitorUserTemplate-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


Response for retrieving a monitor user template.
Field
Type
Description
data
object
Monitor user template data.
attributes
object
A monitor user template object.
created
date-time
The created timestamp of the template.
description
string
A brief description of the monitor user template.
modified
date-time
The last modified timestamp. When the template version was created.
monitor_definition
object
A valid monitor definition in the same format as the [V1 Monitor API](https://docs.datadoghq.com/api/latest/monitors/#create-a-monitor).
tags
[string]
The definition of `MonitorUserTemplateTags` object.
template_variables
[object]
The definition of `MonitorUserTemplateTemplateVariables` object.
available_values
[string]
Available values for the variable.
defaults
[string]
Default values of the template variable.
name [_required_]
string
The name of the template variable.
tag_key
string
The tag key associated with the variable. This works the same as dashboard template variables.
title
string
The title of the monitor user template.
version
int64
The version of the monitor user template.
versions
[object]
All versions of the monitor user template.
created
date-time
The created timestamp of the template.
description
string
A brief description of the monitor user template.
id
string
The unique identifier. The initial version will match the template ID.
monitor_definition
object
A valid monitor definition in the same format as the [V1 Monitor API](https://docs.datadoghq.com/api/latest/monitors/#create-a-monitor).
tags
[string]
The definition of `MonitorUserTemplateTags` object.
template_variables
[object]
The definition of `MonitorUserTemplateTemplateVariables` object.
available_values
[string]
Available values for the variable.
defaults
[string]
Default values of the template variable.
name [_required_]
string
The name of the template variable.
tag_key
string
The tag key associated with the variable. This works the same as dashboard template variables.
title
string
The title of the monitor user template.
version
int64
The version of the monitor user template.
id
string
The unique identifier.
type
enum
Monitor user template resource type. Allowed enum values: `monitor-user-template`
default: `monitor-user-template`
```
{
  "data": {
    "attributes": {
      "created": "2024-01-02T03:04:23.274966+00:00",
      "description": "This is a template for monitoring user activity.",
      "modified": "2024-02-02T03:04:23.274966+00:00",
      "monitor_definition": {
        "message": "You may need to add web hosts if this is consistently high.",
        "name": "Bytes received on host0",
        "query": "avg(last_5m):sum:system.net.bytes_rcvd{host:host0} > 100",
        "type": "query alert"
      },
      "tags": [
        "product:Our Custom App",
        "integration:Azure"
      ],
      "template_variables": [
        {
          "available_values": [
            "value1",
            "value2"
          ],
          "defaults": [
            "defaultValue"
          ],
          "name": "regionName",
          "tag_key": "datacenter"
        }
      ],
      "title": "Postgres CPU Monitor",
      "version": 0,
      "versions": [
        {
          "created": "2024-01-02T03:04:23.274966+00:00",
          "description": "This is a template for monitoring user activity.",
          "id": "00000000-0000-1234-0000-000000000000",
          "monitor_definition": {
            "message": "You may need to add web hosts if this is consistently high.",
            "name": "Bytes received on host0",
            "query": "avg(last_5m):sum:system.net.bytes_rcvd{host:host0} > 100",
            "type": "query alert"
          },
          "tags": [
            "product:Our Custom App",
            "integration:Azure"
          ],
          "template_variables": [
            {
              "available_values": [
                "value1",
                "value2"
              ],
              "defaults": [
                "defaultValue"
              ],
              "name": "regionName",
              "tag_key": "datacenter"
            }
          ],
          "title": "Postgres CPU Monitor",
          "version": 0
        }
      ]
    },
    "id": "00000000-0000-1234-0000-000000000000",
    "type": "monitor-user-template"
  }
}
```

Copy
Not Found
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


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
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/monitors/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/monitors/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/monitors/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/monitors/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/monitors/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/monitors/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/monitors/?code-lang=typescript)


#####  Get a monitor user template
Copy
```
                  # Path parameters  
export template_id="00000000-0000-1234-0000-000000000000"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/monitor/template/${template_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get a monitor user template
```
"""
Get a monitor user template returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.monitors_api import MonitorsApi

# there is a valid "monitor_user_template" in the system
MONITOR_USER_TEMPLATE_DATA_ID = environ["MONITOR_USER_TEMPLATE_DATA_ID"]

configuration = Configuration()
configuration.unstable_operations["get_monitor_user_template"] = True
with ApiClient(configuration) as api_client:
    api_instance = MonitorsApi(api_client)
    response = api_instance.get_monitor_user_template(
        template_id=MONITOR_USER_TEMPLATE_DATA_ID,
    )

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get a monitor user template
```
# Get a monitor user template returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.get_monitor_user_template".to_sym] = true
end
api_instance = DatadogAPIClient::V2::MonitorsAPI.new

# there is a valid "monitor_user_template" in the system
MONITOR_USER_TEMPLATE_DATA_ID = ENV["MONITOR_USER_TEMPLATE_DATA_ID"]
p api_instance.get_monitor_user_template(MONITOR_USER_TEMPLATE_DATA_ID)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get a monitor user template
```
// Get a monitor user template returns "OK" response

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
	// there is a valid "monitor_user_template" in the system
	MonitorUserTemplateDataID := os.Getenv("MONITOR_USER_TEMPLATE_DATA_ID")

	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	configuration.SetUnstableOperationEnabled("v2.GetMonitorUserTemplate", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewMonitorsApi(apiClient)
	resp, r, err := api.GetMonitorUserTemplate(ctx, MonitorUserTemplateDataID, *datadogV2.NewGetMonitorUserTemplateOptionalParameters())

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `MonitorsApi.GetMonitorUserTemplate`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `MonitorsApi.GetMonitorUserTemplate`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get a monitor user template
```
// Get a monitor user template returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.MonitorsApi;
import com.datadog.api.client.v2.model.MonitorUserTemplateResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.getMonitorUserTemplate", true);
    MonitorsApi apiInstance = new MonitorsApi(defaultClient);

    // there is a valid "monitor_user_template" in the system
    String MONITOR_USER_TEMPLATE_DATA_ID = System.getenv("MONITOR_USER_TEMPLATE_DATA_ID");

    try {
      MonitorUserTemplateResponse result =
          apiInstance.getMonitorUserTemplate(MONITOR_USER_TEMPLATE_DATA_ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MonitorsApi#getMonitorUserTemplate");
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

#####  Get a monitor user template
```
// Get a monitor user template returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_monitors::GetMonitorUserTemplateOptionalParams;
use datadog_api_client::datadogV2::api_monitors::MonitorsAPI;

#[tokio::main]
async fn main() {
    // there is a valid "monitor_user_template" in the system
    let monitor_user_template_data_id = std::env::var("MONITOR_USER_TEMPLATE_DATA_ID").unwrap();
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.GetMonitorUserTemplate", true);
    let api = MonitorsAPI::with_config(configuration);
    let resp = api
        .get_monitor_user_template(
            monitor_user_template_data_id.clone(),
            GetMonitorUserTemplateOptionalParams::default(),
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

#####  Get a monitor user template
```
/**
 * Get a monitor user template returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.getMonitorUserTemplate"] = true;
const apiInstance = new v2.MonitorsApi(configuration);

// there is a valid "monitor_user_template" in the system
const MONITOR_USER_TEMPLATE_DATA_ID = process.env
  .MONITOR_USER_TEMPLATE_DATA_ID as string;

const params: v2.MonitorsApiGetMonitorUserTemplateRequest = {
  templateId: MONITOR_USER_TEMPLATE_DATA_ID,
};

apiInstance
  .getMonitorUserTemplate(params)
  .then((data: v2.MonitorUserTemplateResponse) => {
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
## [Get all monitor user templates](https://docs.datadoghq.com/api/latest/monitors/#get-all-monitor-user-templates)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/monitors/#get-all-monitor-user-templates-v2)


**Note** : This endpoint is in Preview. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
GET https://api.ap1.datadoghq.com/api/v2/monitor/templatehttps://api.ap2.datadoghq.com/api/v2/monitor/templatehttps://api.datadoghq.eu/api/v2/monitor/templatehttps://api.ddog-gov.com/api/v2/monitor/templatehttps://api.datadoghq.com/api/v2/monitor/templatehttps://api.us3.datadoghq.com/api/v2/monitor/templatehttps://api.us5.datadoghq.com/api/v2/monitor/template
### Overview
Retrieve all monitor user templates. This endpoint requires the `monitors_read` permission.
OAuth apps require the `monitors_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#monitors) to access this endpoint.
### Response
  * [200](https://docs.datadoghq.com/api/latest/monitors/#ListMonitorUserTemplates-200-v2)
  * [429](https://docs.datadoghq.com/api/latest/monitors/#ListMonitorUserTemplates-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


Response for retrieving all monitor user templates.
Field
Type
Description
data
[object]
An array of monitor user templates.
attributes
object
Attributes for a monitor user template.
created
date-time
The created timestamp of the template.
description
string
A brief description of the monitor user template.
modified
date-time
The last modified timestamp. When the template version was created.
monitor_definition
object
A valid monitor definition in the same format as the [V1 Monitor API](https://docs.datadoghq.com/api/latest/monitors/#create-a-monitor).
tags
[string]
The definition of `MonitorUserTemplateTags` object.
template_variables
[object]
The definition of `MonitorUserTemplateTemplateVariables` object.
available_values
[string]
Available values for the variable.
defaults
[string]
Default values of the template variable.
name [_required_]
string
The name of the template variable.
tag_key
string
The tag key associated with the variable. This works the same as dashboard template variables.
title
string
The title of the monitor user template.
version
int64
The version of the monitor user template.
id
string
The unique identifier.
type
enum
Monitor user template resource type. Allowed enum values: `monitor-user-template`
default: `monitor-user-template`
```
{
  "data": [
    {
      "attributes": {
        "created": "2024-01-02T03:04:23.274966+00:00",
        "description": "This is a template for monitoring user activity.",
        "modified": "2024-02-02T03:04:23.274966+00:00",
        "monitor_definition": {
          "message": "You may need to add web hosts if this is consistently high.",
          "name": "Bytes received on host0",
          "query": "avg(last_5m):sum:system.net.bytes_rcvd{host:host0} > 100",
          "type": "query alert"
        },
        "tags": [
          "product:Our Custom App",
          "integration:Azure"
        ],
        "template_variables": [
          {
            "available_values": [
              "value1",
              "value2"
            ],
            "defaults": [
              "defaultValue"
            ],
            "name": "regionName",
            "tag_key": "datacenter"
          }
        ],
        "title": "Postgres CPU Monitor",
        "version": 0
      },
      "id": "00000000-0000-1234-0000-000000000000",
      "type": "monitor-user-template"
    }
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/monitors/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/monitors/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/monitors/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/monitors/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/monitors/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/monitors/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/monitors/?code-lang=typescript)


#####  Get all monitor user templates
Copy
```
                  # Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/monitor/template" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get all monitor user templates
```
"""
Get all monitor user templates returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.monitors_api import MonitorsApi

configuration = Configuration()
configuration.unstable_operations["list_monitor_user_templates"] = True
with ApiClient(configuration) as api_client:
    api_instance = MonitorsApi(api_client)
    response = api_instance.list_monitor_user_templates()

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"


```

#####  Get all monitor user templates
```
# Get all monitor user templates returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.list_monitor_user_templates".to_sym] = true
end
api_instance = DatadogAPIClient::V2::MonitorsAPI.new
p api_instance.list_monitor_user_templates()

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"


```

#####  Get all monitor user templates
```
// Get all monitor user templates returns "OK" response

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
	configuration.SetUnstableOperationEnabled("v2.ListMonitorUserTemplates", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewMonitorsApi(apiClient)
	resp, r, err := api.ListMonitorUserTemplates(ctx)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `MonitorsApi.ListMonitorUserTemplates`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `MonitorsApi.ListMonitorUserTemplates`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"


```

#####  Get all monitor user templates
```
// Get all monitor user templates returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.MonitorsApi;
import com.datadog.api.client.v2.model.MonitorUserTemplateListResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.listMonitorUserTemplates", true);
    MonitorsApi apiInstance = new MonitorsApi(defaultClient);

    try {
      MonitorUserTemplateListResponse result = apiInstance.listMonitorUserTemplates();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MonitorsApi#listMonitorUserTemplates");
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

#####  Get all monitor user templates
```
// Get all monitor user templates returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_monitors::MonitorsAPI;

#[tokio::main]
async fn main() {
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.ListMonitorUserTemplates", true);
    let api = MonitorsAPI::with_config(configuration);
    let resp = api.list_monitor_user_templates().await;
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

#####  Get all monitor user templates
```
/**
 * Get all monitor user templates returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.listMonitorUserTemplates"] = true;
const apiInstance = new v2.MonitorsApi(configuration);

apiInstance
  .listMonitorUserTemplates()
  .then((data: v2.MonitorUserTemplateListResponse) => {
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
## [Create a monitor user template](https://docs.datadoghq.com/api/latest/monitors/#create-a-monitor-user-template)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/monitors/#create-a-monitor-user-template-v2)


**Note** : This endpoint is in Preview. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
POST https://api.ap1.datadoghq.com/api/v2/monitor/templatehttps://api.ap2.datadoghq.com/api/v2/monitor/templatehttps://api.datadoghq.eu/api/v2/monitor/templatehttps://api.ddog-gov.com/api/v2/monitor/templatehttps://api.datadoghq.com/api/v2/monitor/templatehttps://api.us3.datadoghq.com/api/v2/monitor/templatehttps://api.us5.datadoghq.com/api/v2/monitor/template
### Overview
Create a new monitor user template. This endpoint requires the `monitor_config_policy_write` permission.
### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


Field
Type
Description
data [_required_]
object
Monitor user template data.
attributes [_required_]
object
Attributes for a monitor user template.
description
string
A brief description of the monitor user template.
monitor_definition [_required_]
object
A valid monitor definition in the same format as the [V1 Monitor API](https://docs.datadoghq.com/api/latest/monitors/#create-a-monitor).
tags [_required_]
[string]
The definition of `MonitorUserTemplateTags` object.
template_variables
[object]
The definition of `MonitorUserTemplateTemplateVariables` object.
available_values
[string]
Available values for the variable.
defaults
[string]
Default values of the template variable.
name [_required_]
string
The name of the template variable.
tag_key
string
The tag key associated with the variable. This works the same as dashboard template variables.
title [_required_]
string
The title of the monitor user template.
type [_required_]
enum
Monitor user template resource type. Allowed enum values: `monitor-user-template`
default: `monitor-user-template`
```
{
  "data": {
    "attributes": {
      "description": "A description.",
      "monitor_definition": {
        "message": "A msg.",
        "name": "A name example-monitor",
        "query": "avg(last_5m):sum:system.net.bytes_rcvd{host:host0} > 100",
        "type": "query alert"
      },
      "tags": [
        "integration:Azure"
      ],
      "template_variables": [
        {
          "available_values": [
            "value1",
            "value2"
          ],
          "defaults": [
            "defaultValue"
          ],
          "name": "regionName",
          "tag_key": "datacenter"
        }
      ],
      "title": "Postgres DB example-monitor"
    },
    "type": "monitor-user-template"
  }
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/monitors/#CreateMonitorUserTemplate-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/monitors/#CreateMonitorUserTemplate-400-v2)
  * [429](https://docs.datadoghq.com/api/latest/monitors/#CreateMonitorUserTemplate-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


Response for creating a monitor user template.
Field
Type
Description
data
object
Monitor user template list response data.
attributes
object
Attributes for a monitor user template.
created
date-time
The created timestamp of the template.
description
string
A brief description of the monitor user template.
modified
date-time
The last modified timestamp. When the template version was created.
monitor_definition
object
A valid monitor definition in the same format as the [V1 Monitor API](https://docs.datadoghq.com/api/latest/monitors/#create-a-monitor).
tags
[string]
The definition of `MonitorUserTemplateTags` object.
template_variables
[object]
The definition of `MonitorUserTemplateTemplateVariables` object.
available_values
[string]
Available values for the variable.
defaults
[string]
Default values of the template variable.
name [_required_]
string
The name of the template variable.
tag_key
string
The tag key associated with the variable. This works the same as dashboard template variables.
title
string
The title of the monitor user template.
version
int64
The version of the monitor user template.
id
string
The unique identifier.
type
enum
Monitor user template resource type. Allowed enum values: `monitor-user-template`
default: `monitor-user-template`
```
{
  "data": {
    "attributes": {
      "created": "2024-01-02T03:04:23.274966+00:00",
      "description": "This is a template for monitoring user activity.",
      "modified": "2024-02-02T03:04:23.274966+00:00",
      "monitor_definition": {
        "message": "You may need to add web hosts if this is consistently high.",
        "name": "Bytes received on host0",
        "query": "avg(last_5m):sum:system.net.bytes_rcvd{host:host0} > 100",
        "type": "query alert"
      },
      "tags": [
        "product:Our Custom App",
        "integration:Azure"
      ],
      "template_variables": [
        {
          "available_values": [
            "value1",
            "value2"
          ],
          "defaults": [
            "defaultValue"
          ],
          "name": "regionName",
          "tag_key": "datacenter"
        }
      ],
      "title": "Postgres CPU Monitor",
      "version": 0
    },
    "id": "00000000-0000-1234-0000-000000000000",
    "type": "monitor-user-template"
  }
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


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
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/monitors/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/monitors/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/monitors/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/monitors/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/monitors/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/monitors/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/monitors/?code-lang=typescript)


#####  Create a monitor user template returns "OK" response
Copy
```
                          # Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/monitor/template" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "description": "A description.",
      "monitor_definition": {
        "message": "A msg.",
        "name": "A name example-monitor",
        "query": "avg(last_5m):sum:system.net.bytes_rcvd{host:host0} > 100",
        "type": "query alert"
      },
      "tags": [
        "integration:Azure"
      ],
      "template_variables": [
        {
          "available_values": [
            "value1",
            "value2"
          ],
          "defaults": [
            "defaultValue"
          ],
          "name": "regionName",
          "tag_key": "datacenter"
        }
      ],
      "title": "Postgres DB example-monitor"
    },
    "type": "monitor-user-template"
  }
}
EOF  

                        
```

#####  Create a monitor user template returns "OK" response
```
// Create a monitor user template returns "OK" response

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
	body := datadogV2.MonitorUserTemplateCreateRequest{
		Data: datadogV2.MonitorUserTemplateCreateData{
			Attributes: datadogV2.MonitorUserTemplateRequestAttributes{
				Description: *datadog.NewNullableString(datadog.PtrString("A description.")),
				MonitorDefinition: map[string]interface{}{
					"message": "A msg.",
					"name":    "A name example-monitor",
					"query":   "avg(last_5m):sum:system.net.bytes_rcvd{host:host0} > 100",
					"type":    "query alert",
				},
				Tags: []string{
					"integration:Azure",
				},
				TemplateVariables: []datadogV2.MonitorUserTemplateTemplateVariablesItems{
					{
						AvailableValues: []string{
							"value1",
							"value2",
						},
						Defaults: []string{
							"defaultValue",
						},
						Name:   "regionName",
						TagKey: datadog.PtrString("datacenter"),
					},
				},
				Title: "Postgres DB example-monitor",
			},
			Type: datadogV2.MONITORUSERTEMPLATERESOURCETYPE_MONITOR_USER_TEMPLATE,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	configuration.SetUnstableOperationEnabled("v2.CreateMonitorUserTemplate", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewMonitorsApi(apiClient)
	resp, r, err := api.CreateMonitorUserTemplate(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `MonitorsApi.CreateMonitorUserTemplate`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `MonitorsApi.CreateMonitorUserTemplate`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Create a monitor user template returns "OK" response
```
// Create a monitor user template returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.MonitorsApi;
import com.datadog.api.client.v2.model.MonitorUserTemplateCreateData;
import com.datadog.api.client.v2.model.MonitorUserTemplateCreateRequest;
import com.datadog.api.client.v2.model.MonitorUserTemplateCreateResponse;
import com.datadog.api.client.v2.model.MonitorUserTemplateRequestAttributes;
import com.datadog.api.client.v2.model.MonitorUserTemplateResourceType;
import com.datadog.api.client.v2.model.MonitorUserTemplateTemplateVariablesItems;
import java.util.Arrays;
import java.util.Collections;
import java.util.Map;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.createMonitorUserTemplate", true);
    MonitorsApi apiInstance = new MonitorsApi(defaultClient);

    MonitorUserTemplateCreateRequest body =
        new MonitorUserTemplateCreateRequest()
            .data(
                new MonitorUserTemplateCreateData()
                    .attributes(
                        new MonitorUserTemplateRequestAttributes()
                            .description("A description.")
                            .monitorDefinition(
                                Map.ofEntries(
                                    Map.entry("message", "A msg."),
                                    Map.entry("name", "A name example-monitor"),
                                    Map.entry(
                                        "query",
                                        "avg(last_5m):sum:system.net.bytes_rcvd{host:host0} > 100"),
                                    Map.entry("type", "query alert")))
                            .tags(Collections.singletonList("integration:Azure"))
                            .templateVariables(
                                Collections.singletonList(
                                    new MonitorUserTemplateTemplateVariablesItems()
                                        .availableValues(Arrays.asList("value1", "value2"))
                                        .defaults(Collections.singletonList("defaultValue"))
                                        .name("regionName")
                                        .tagKey("datacenter")))
                            .title("Postgres DB example-monitor"))
                    .type(MonitorUserTemplateResourceType.MONITOR_USER_TEMPLATE));

    try {
      MonitorUserTemplateCreateResponse result = apiInstance.createMonitorUserTemplate(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MonitorsApi#createMonitorUserTemplate");
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

#####  Create a monitor user template returns "OK" response
```
"""
Create a monitor user template returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.monitors_api import MonitorsApi
from datadog_api_client.v2.model.monitor_user_template_create_data import MonitorUserTemplateCreateData
from datadog_api_client.v2.model.monitor_user_template_create_request import MonitorUserTemplateCreateRequest
from datadog_api_client.v2.model.monitor_user_template_request_attributes import MonitorUserTemplateRequestAttributes
from datadog_api_client.v2.model.monitor_user_template_resource_type import MonitorUserTemplateResourceType
from datadog_api_client.v2.model.monitor_user_template_template_variables_items import (
    MonitorUserTemplateTemplateVariablesItems,
)

body = MonitorUserTemplateCreateRequest(
    data=MonitorUserTemplateCreateData(
        attributes=MonitorUserTemplateRequestAttributes(
            description="A description.",
            monitor_definition=dict(
                [
                    ("message", "A msg."),
                    ("name", "A name example-monitor"),
                    ("query", "avg(last_5m):sum:system.net.bytes_rcvd{host:host0} > 100"),
                    ("type", "query alert"),
                ]
            ),
            tags=[
                "integration:Azure",
            ],
            template_variables=[
                MonitorUserTemplateTemplateVariablesItems(
                    available_values=[
                        "value1",
                        "value2",
                    ],
                    defaults=[
                        "defaultValue",
                    ],
                    name="regionName",
                    tag_key="datacenter",
                ),
            ],
            title="Postgres DB example-monitor",
        ),
        type=MonitorUserTemplateResourceType.MONITOR_USER_TEMPLATE,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_monitor_user_template"] = True
with ApiClient(configuration) as api_client:
    api_instance = MonitorsApi(api_client)
    response = api_instance.create_monitor_user_template(body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Create a monitor user template returns "OK" response
```
# Create a monitor user template returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.create_monitor_user_template".to_sym] = true
end
api_instance = DatadogAPIClient::V2::MonitorsAPI.new

body = DatadogAPIClient::V2::MonitorUserTemplateCreateRequest.new({
  data: DatadogAPIClient::V2::MonitorUserTemplateCreateData.new({
    attributes: DatadogAPIClient::V2::MonitorUserTemplateRequestAttributes.new({
      description: "A description.",
      monitor_definition: {
        "message": "A msg.", "name": "A name example-monitor", "query": "avg(last_5m):sum:system.net.bytes_rcvd{host:host0} > 100", "type": "query alert",
      },
      tags: [
        "integration:Azure",
      ],
      template_variables: [
        DatadogAPIClient::V2::MonitorUserTemplateTemplateVariablesItems.new({
          available_values: [
            "value1",
            "value2",
          ],
          defaults: [
            "defaultValue",
          ],
          name: "regionName",
          tag_key: "datacenter",
        }),
      ],
      title: "Postgres DB example-monitor",
    }),
    type: DatadogAPIClient::V2::MonitorUserTemplateResourceType::MONITOR_USER_TEMPLATE,
  }),
})
p api_instance.create_monitor_user_template(body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Create a monitor user template returns "OK" response
```
// Create a monitor user template returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_monitors::MonitorsAPI;
use datadog_api_client::datadogV2::model::MonitorUserTemplateCreateData;
use datadog_api_client::datadogV2::model::MonitorUserTemplateCreateRequest;
use datadog_api_client::datadogV2::model::MonitorUserTemplateRequestAttributes;
use datadog_api_client::datadogV2::model::MonitorUserTemplateResourceType;
use datadog_api_client::datadogV2::model::MonitorUserTemplateTemplateVariablesItems;
use serde_json::Value;
use std::collections::BTreeMap;

#[tokio::main]
async fn main() {
    let body = MonitorUserTemplateCreateRequest::new(MonitorUserTemplateCreateData::new(
        MonitorUserTemplateRequestAttributes::new(
            BTreeMap::from([
                ("message".to_string(), Value::from("A msg.")),
                ("name".to_string(), Value::from("A name example-monitor")),
                (
                    "query".to_string(),
                    Value::from("avg(last_5m):sum:system.net.bytes_rcvd{host:host0} > 100"),
                ),
                ("type".to_string(), Value::from("query alert")),
            ]),
            vec!["integration:Azure".to_string()],
            "Postgres DB example-monitor".to_string(),
        )
        .description(Some("A description.".to_string()))
        .template_variables(vec![MonitorUserTemplateTemplateVariablesItems::new(
            "regionName".to_string(),
        )
        .available_values(vec!["value1".to_string(), "value2".to_string()])
        .defaults(vec!["defaultValue".to_string()])
        .tag_key("datacenter".to_string())]),
        MonitorUserTemplateResourceType::MONITOR_USER_TEMPLATE,
    ));
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.CreateMonitorUserTemplate", true);
    let api = MonitorsAPI::with_config(configuration);
    let resp = api.create_monitor_user_template(body).await;
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

#####  Create a monitor user template returns "OK" response
```
/**
 * Create a monitor user template returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.createMonitorUserTemplate"] = true;
const apiInstance = new v2.MonitorsApi(configuration);

const params: v2.MonitorsApiCreateMonitorUserTemplateRequest = {
  body: {
    data: {
      attributes: {
        description: "A description.",
        monitorDefinition: {
          message: "A msg.",
          name: "A name example-monitor",
          query: "avg(last_5m):sum:system.net.bytes_rcvd{host:host0} > 100",
          type: "query alert",
        },
        tags: ["integration:Azure"],
        templateVariables: [
          {
            availableValues: ["value1", "value2"],
            defaults: ["defaultValue"],
            name: "regionName",
            tagKey: "datacenter",
          },
        ],
        title: "Postgres DB example-monitor",
      },
      type: "monitor-user-template",
    },
  },
};

apiInstance
  .createMonitorUserTemplate(params)
  .then((data: v2.MonitorUserTemplateCreateResponse) => {
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
## [Update a monitor user template to a new version](https://docs.datadoghq.com/api/latest/monitors/#update-a-monitor-user-template-to-a-new-version)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/monitors/#update-a-monitor-user-template-to-a-new-version-v2)


**Note** : This endpoint is in Preview. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
PUT https://api.ap1.datadoghq.com/api/v2/monitor/template/{template_id}https://api.ap2.datadoghq.com/api/v2/monitor/template/{template_id}https://api.datadoghq.eu/api/v2/monitor/template/{template_id}https://api.ddog-gov.com/api/v2/monitor/template/{template_id}https://api.datadoghq.com/api/v2/monitor/template/{template_id}https://api.us3.datadoghq.com/api/v2/monitor/template/{template_id}https://api.us5.datadoghq.com/api/v2/monitor/template/{template_id}
### Overview
Creates a new version of an existing monitor user template. This endpoint requires the `monitor_config_policy_write` permission.
### Arguments
#### Path Parameters
Name
Type
Description
template_id [_required_]
string
ID of the monitor user template.
### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


Field
Type
Description
data [_required_]
object
Monitor user template data.
attributes [_required_]
object
Attributes for a monitor user template.
description
string
A brief description of the monitor user template.
monitor_definition [_required_]
object
A valid monitor definition in the same format as the [V1 Monitor API](https://docs.datadoghq.com/api/latest/monitors/#create-a-monitor).
tags [_required_]
[string]
The definition of `MonitorUserTemplateTags` object.
template_variables
[object]
The definition of `MonitorUserTemplateTemplateVariables` object.
available_values
[string]
Available values for the variable.
defaults
[string]
Default values of the template variable.
name [_required_]
string
The name of the template variable.
tag_key
string
The tag key associated with the variable. This works the same as dashboard template variables.
title [_required_]
string
The title of the monitor user template.
id [_required_]
string
The unique identifier.
type [_required_]
enum
Monitor user template resource type. Allowed enum values: `monitor-user-template`
default: `monitor-user-template`
```
{
  "data": {
    "attributes": {
      "description": "A description.",
      "monitor_definition": {
        "message": "A msg.",
        "name": "A name example-monitor",
        "query": "avg(last_5m):sum:system.net.bytes_rcvd{host:host0} > 100",
        "type": "query alert"
      },
      "tags": [
        "integration:Azure"
      ],
      "template_variables": [
        {
          "available_values": [
            "value1",
            "value2"
          ],
          "defaults": [
            "defaultValue"
          ],
          "name": "regionName",
          "tag_key": "datacenter"
        }
      ],
      "title": "Postgres DB example-monitor"
    },
    "id": "00000000-0000-1234-0000-000000000000",
    "type": "monitor-user-template"
  }
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/monitors/#UpdateMonitorUserTemplate-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/monitors/#UpdateMonitorUserTemplate-400-v2)
  * [404](https://docs.datadoghq.com/api/latest/monitors/#UpdateMonitorUserTemplate-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/monitors/#UpdateMonitorUserTemplate-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


Response for retrieving a monitor user template.
Field
Type
Description
data
object
Monitor user template data.
attributes
object
A monitor user template object.
created
date-time
The created timestamp of the template.
description
string
A brief description of the monitor user template.
modified
date-time
The last modified timestamp. When the template version was created.
monitor_definition
object
A valid monitor definition in the same format as the [V1 Monitor API](https://docs.datadoghq.com/api/latest/monitors/#create-a-monitor).
tags
[string]
The definition of `MonitorUserTemplateTags` object.
template_variables
[object]
The definition of `MonitorUserTemplateTemplateVariables` object.
available_values
[string]
Available values for the variable.
defaults
[string]
Default values of the template variable.
name [_required_]
string
The name of the template variable.
tag_key
string
The tag key associated with the variable. This works the same as dashboard template variables.
title
string
The title of the monitor user template.
version
int64
The version of the monitor user template.
versions
[object]
All versions of the monitor user template.
created
date-time
The created timestamp of the template.
description
string
A brief description of the monitor user template.
id
string
The unique identifier. The initial version will match the template ID.
monitor_definition
object
A valid monitor definition in the same format as the [V1 Monitor API](https://docs.datadoghq.com/api/latest/monitors/#create-a-monitor).
tags
[string]
The definition of `MonitorUserTemplateTags` object.
template_variables
[object]
The definition of `MonitorUserTemplateTemplateVariables` object.
available_values
[string]
Available values for the variable.
defaults
[string]
Default values of the template variable.
name [_required_]
string
The name of the template variable.
tag_key
string
The tag key associated with the variable. This works the same as dashboard template variables.
title
string
The title of the monitor user template.
version
int64
The version of the monitor user template.
id
string
The unique identifier.
type
enum
Monitor user template resource type. Allowed enum values: `monitor-user-template`
default: `monitor-user-template`
```
{
  "data": {
    "attributes": {
      "created": "2024-01-02T03:04:23.274966+00:00",
      "description": "This is a template for monitoring user activity.",
      "modified": "2024-02-02T03:04:23.274966+00:00",
      "monitor_definition": {
        "message": "You may need to add web hosts if this is consistently high.",
        "name": "Bytes received on host0",
        "query": "avg(last_5m):sum:system.net.bytes_rcvd{host:host0} > 100",
        "type": "query alert"
      },
      "tags": [
        "product:Our Custom App",
        "integration:Azure"
      ],
      "template_variables": [
        {
          "available_values": [
            "value1",
            "value2"
          ],
          "defaults": [
            "defaultValue"
          ],
          "name": "regionName",
          "tag_key": "datacenter"
        }
      ],
      "title": "Postgres CPU Monitor",
      "version": 0,
      "versions": [
        {
          "created": "2024-01-02T03:04:23.274966+00:00",
          "description": "This is a template for monitoring user activity.",
          "id": "00000000-0000-1234-0000-000000000000",
          "monitor_definition": {
            "message": "You may need to add web hosts if this is consistently high.",
            "name": "Bytes received on host0",
            "query": "avg(last_5m):sum:system.net.bytes_rcvd{host:host0} > 100",
            "type": "query alert"
          },
          "tags": [
            "product:Our Custom App",
            "integration:Azure"
          ],
          "template_variables": [
            {
              "available_values": [
                "value1",
                "value2"
              ],
              "defaults": [
                "defaultValue"
              ],
              "name": "regionName",
              "tag_key": "datacenter"
            }
          ],
          "title": "Postgres CPU Monitor",
          "version": 0
        }
      ]
    },
    "id": "00000000-0000-1234-0000-000000000000",
    "type": "monitor-user-template"
  }
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


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
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


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
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/monitors/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/monitors/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/monitors/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/monitors/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/monitors/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/monitors/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/monitors/?code-lang=typescript)


#####  Update a monitor user template to a new version returns "OK" response
Copy
```
                          # Path parameters  
export template_id="CHANGE_ME"  
# Curl command  
curl -X PUT "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/monitor/template/${template_id}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "description": "A description.",
      "monitor_definition": {
        "message": "A msg.",
        "name": "A name example-monitor",
        "query": "avg(last_5m):sum:system.net.bytes_rcvd{host:host0} > 100",
        "type": "query alert"
      },
      "tags": [
        "integration:Azure"
      ],
      "template_variables": [
        {
          "available_values": [
            "value1",
            "value2"
          ],
          "defaults": [
            "defaultValue"
          ],
          "name": "regionName",
          "tag_key": "datacenter"
        }
      ],
      "title": "Postgres DB example-monitor"
    },
    "id": "00000000-0000-1234-0000-000000000000",
    "type": "monitor-user-template"
  }
}
EOF  

                        
```

#####  Update a monitor user template to a new version returns "OK" response
```
// Update a monitor user template to a new version returns "OK" response

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
	// there is a valid "monitor_user_template" in the system
	MonitorUserTemplateDataID := os.Getenv("MONITOR_USER_TEMPLATE_DATA_ID")

	body := datadogV2.MonitorUserTemplateUpdateRequest{
		Data: datadogV2.MonitorUserTemplateUpdateData{
			Attributes: datadogV2.MonitorUserTemplateRequestAttributes{
				Description: *datadog.NewNullableString(datadog.PtrString("A description.")),
				MonitorDefinition: map[string]interface{}{
					"message": "A msg.",
					"name":    "A name example-monitor",
					"query":   "avg(last_5m):sum:system.net.bytes_rcvd{host:host0} > 100",
					"type":    "query alert",
				},
				Tags: []string{
					"integration:Azure",
				},
				TemplateVariables: []datadogV2.MonitorUserTemplateTemplateVariablesItems{
					{
						AvailableValues: []string{
							"value1",
							"value2",
						},
						Defaults: []string{
							"defaultValue",
						},
						Name:   "regionName",
						TagKey: datadog.PtrString("datacenter"),
					},
				},
				Title: "Postgres DB example-monitor",
			},
			Id:   MonitorUserTemplateDataID,
			Type: datadogV2.MONITORUSERTEMPLATERESOURCETYPE_MONITOR_USER_TEMPLATE,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	configuration.SetUnstableOperationEnabled("v2.UpdateMonitorUserTemplate", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewMonitorsApi(apiClient)
	resp, r, err := api.UpdateMonitorUserTemplate(ctx, MonitorUserTemplateDataID, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `MonitorsApi.UpdateMonitorUserTemplate`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `MonitorsApi.UpdateMonitorUserTemplate`:\n%s\n", responseContent)
}

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Update a monitor user template to a new version returns "OK" response
```
// Update a monitor user template to a new version returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.MonitorsApi;
import com.datadog.api.client.v2.model.MonitorUserTemplateRequestAttributes;
import com.datadog.api.client.v2.model.MonitorUserTemplateResourceType;
import com.datadog.api.client.v2.model.MonitorUserTemplateResponse;
import com.datadog.api.client.v2.model.MonitorUserTemplateTemplateVariablesItems;
import com.datadog.api.client.v2.model.MonitorUserTemplateUpdateData;
import com.datadog.api.client.v2.model.MonitorUserTemplateUpdateRequest;
import java.util.Arrays;
import java.util.Collections;
import java.util.Map;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.updateMonitorUserTemplate", true);
    MonitorsApi apiInstance = new MonitorsApi(defaultClient);

    // there is a valid "monitor_user_template" in the system
    String MONITOR_USER_TEMPLATE_DATA_ID = System.getenv("MONITOR_USER_TEMPLATE_DATA_ID");

    MonitorUserTemplateUpdateRequest body =
        new MonitorUserTemplateUpdateRequest()
            .data(
                new MonitorUserTemplateUpdateData()
                    .attributes(
                        new MonitorUserTemplateRequestAttributes()
                            .description("A description.")
                            .monitorDefinition(
                                Map.ofEntries(
                                    Map.entry("message", "A msg."),
                                    Map.entry("name", "A name example-monitor"),
                                    Map.entry(
                                        "query",
                                        "avg(last_5m):sum:system.net.bytes_rcvd{host:host0} > 100"),
                                    Map.entry("type", "query alert")))
                            .tags(Collections.singletonList("integration:Azure"))
                            .templateVariables(
                                Collections.singletonList(
                                    new MonitorUserTemplateTemplateVariablesItems()
                                        .availableValues(Arrays.asList("value1", "value2"))
                                        .defaults(Collections.singletonList("defaultValue"))
                                        .name("regionName")
                                        .tagKey("datacenter")))
                            .title("Postgres DB example-monitor"))
                    .id(MONITOR_USER_TEMPLATE_DATA_ID)
                    .type(MonitorUserTemplateResourceType.MONITOR_USER_TEMPLATE));

    try {
      MonitorUserTemplateResponse result =
          apiInstance.updateMonitorUserTemplate(MONITOR_USER_TEMPLATE_DATA_ID, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MonitorsApi#updateMonitorUserTemplate");
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

#####  Update a monitor user template to a new version returns "OK" response
```
"""
Update a monitor user template to a new version returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.monitors_api import MonitorsApi
from datadog_api_client.v2.model.monitor_user_template_request_attributes import MonitorUserTemplateRequestAttributes
from datadog_api_client.v2.model.monitor_user_template_resource_type import MonitorUserTemplateResourceType
from datadog_api_client.v2.model.monitor_user_template_template_variables_items import (
    MonitorUserTemplateTemplateVariablesItems,
)
from datadog_api_client.v2.model.monitor_user_template_update_data import MonitorUserTemplateUpdateData
from datadog_api_client.v2.model.monitor_user_template_update_request import MonitorUserTemplateUpdateRequest

# there is a valid "monitor_user_template" in the system
MONITOR_USER_TEMPLATE_DATA_ID = environ["MONITOR_USER_TEMPLATE_DATA_ID"]

body = MonitorUserTemplateUpdateRequest(
    data=MonitorUserTemplateUpdateData(
        attributes=MonitorUserTemplateRequestAttributes(
            description="A description.",
            monitor_definition=dict(
                [
                    ("message", "A msg."),
                    ("name", "A name example-monitor"),
                    ("query", "avg(last_5m):sum:system.net.bytes_rcvd{host:host0} > 100"),
                    ("type", "query alert"),
                ]
            ),
            tags=[
                "integration:Azure",
            ],
            template_variables=[
                MonitorUserTemplateTemplateVariablesItems(
                    available_values=[
                        "value1",
                        "value2",
                    ],
                    defaults=[
                        "defaultValue",
                    ],
                    name="regionName",
                    tag_key="datacenter",
                ),
            ],
            title="Postgres DB example-monitor",
        ),
        id=MONITOR_USER_TEMPLATE_DATA_ID,
        type=MonitorUserTemplateResourceType.MONITOR_USER_TEMPLATE,
    ),
)

configuration = Configuration()
configuration.unstable_operations["update_monitor_user_template"] = True
with ApiClient(configuration) as api_client:
    api_instance = MonitorsApi(api_client)
    response = api_instance.update_monitor_user_template(template_id=MONITOR_USER_TEMPLATE_DATA_ID, body=body)

    print(response)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Update a monitor user template to a new version returns "OK" response
```
# Update a monitor user template to a new version returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.update_monitor_user_template".to_sym] = true
end
api_instance = DatadogAPIClient::V2::MonitorsAPI.new

# there is a valid "monitor_user_template" in the system
MONITOR_USER_TEMPLATE_DATA_ID = ENV["MONITOR_USER_TEMPLATE_DATA_ID"]

body = DatadogAPIClient::V2::MonitorUserTemplateUpdateRequest.new({
  data: DatadogAPIClient::V2::MonitorUserTemplateUpdateData.new({
    attributes: DatadogAPIClient::V2::MonitorUserTemplateRequestAttributes.new({
      description: "A description.",
      monitor_definition: {
        "message": "A msg.", "name": "A name example-monitor", "query": "avg(last_5m):sum:system.net.bytes_rcvd{host:host0} > 100", "type": "query alert",
      },
      tags: [
        "integration:Azure",
      ],
      template_variables: [
        DatadogAPIClient::V2::MonitorUserTemplateTemplateVariablesItems.new({
          available_values: [
            "value1",
            "value2",
          ],
          defaults: [
            "defaultValue",
          ],
          name: "regionName",
          tag_key: "datacenter",
        }),
      ],
      title: "Postgres DB example-monitor",
    }),
    id: MONITOR_USER_TEMPLATE_DATA_ID,
    type: DatadogAPIClient::V2::MonitorUserTemplateResourceType::MONITOR_USER_TEMPLATE,
  }),
})
p api_instance.update_monitor_user_template(MONITOR_USER_TEMPLATE_DATA_ID, body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Update a monitor user template to a new version returns "OK" response
```
// Update a monitor user template to a new version returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_monitors::MonitorsAPI;
use datadog_api_client::datadogV2::model::MonitorUserTemplateRequestAttributes;
use datadog_api_client::datadogV2::model::MonitorUserTemplateResourceType;
use datadog_api_client::datadogV2::model::MonitorUserTemplateTemplateVariablesItems;
use datadog_api_client::datadogV2::model::MonitorUserTemplateUpdateData;
use datadog_api_client::datadogV2::model::MonitorUserTemplateUpdateRequest;
use serde_json::Value;
use std::collections::BTreeMap;

#[tokio::main]
async fn main() {
    // there is a valid "monitor_user_template" in the system
    let monitor_user_template_data_id = std::env::var("MONITOR_USER_TEMPLATE_DATA_ID").unwrap();
    let body = MonitorUserTemplateUpdateRequest::new(MonitorUserTemplateUpdateData::new(
        MonitorUserTemplateRequestAttributes::new(
            BTreeMap::from([
                ("message".to_string(), Value::from("A msg.")),
                ("name".to_string(), Value::from("A name example-monitor")),
                (
                    "query".to_string(),
                    Value::from("avg(last_5m):sum:system.net.bytes_rcvd{host:host0} > 100"),
                ),
                ("type".to_string(), Value::from("query alert")),
            ]),
            vec!["integration:Azure".to_string()],
            "Postgres DB example-monitor".to_string(),
        )
        .description(Some("A description.".to_string()))
        .template_variables(vec![MonitorUserTemplateTemplateVariablesItems::new(
            "regionName".to_string(),
        )
        .available_values(vec!["value1".to_string(), "value2".to_string()])
        .defaults(vec!["defaultValue".to_string()])
        .tag_key("datacenter".to_string())]),
        monitor_user_template_data_id.clone(),
        MonitorUserTemplateResourceType::MONITOR_USER_TEMPLATE,
    ));
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.UpdateMonitorUserTemplate", true);
    let api = MonitorsAPI::with_config(configuration);
    let resp = api
        .update_monitor_user_template(monitor_user_template_data_id.clone(), body)
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

#####  Update a monitor user template to a new version returns "OK" response
```
/**
 * Update a monitor user template to a new version returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.updateMonitorUserTemplate"] = true;
const apiInstance = new v2.MonitorsApi(configuration);

// there is a valid "monitor_user_template" in the system
const MONITOR_USER_TEMPLATE_DATA_ID = process.env
  .MONITOR_USER_TEMPLATE_DATA_ID as string;

const params: v2.MonitorsApiUpdateMonitorUserTemplateRequest = {
  body: {
    data: {
      attributes: {
        description: "A description.",
        monitorDefinition: {
          message: "A msg.",
          name: "A name example-monitor",
          query: "avg(last_5m):sum:system.net.bytes_rcvd{host:host0} > 100",
          type: "query alert",
        },
        tags: ["integration:Azure"],
        templateVariables: [
          {
            availableValues: ["value1", "value2"],
            defaults: ["defaultValue"],
            name: "regionName",
            tagKey: "datacenter",
          },
        ],
        title: "Postgres DB example-monitor",
      },
      id: MONITOR_USER_TEMPLATE_DATA_ID,
      type: "monitor-user-template",
    },
  },
  templateId: MONITOR_USER_TEMPLATE_DATA_ID,
};

apiInstance
  .updateMonitorUserTemplate(params)
  .then((data: v2.MonitorUserTemplateResponse) => {
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
## [Delete a monitor user template](https://docs.datadoghq.com/api/latest/monitors/#delete-a-monitor-user-template)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/monitors/#delete-a-monitor-user-template-v2)


**Note** : This endpoint is in Preview. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
DELETE https://api.ap1.datadoghq.com/api/v2/monitor/template/{template_id}https://api.ap2.datadoghq.com/api/v2/monitor/template/{template_id}https://api.datadoghq.eu/api/v2/monitor/template/{template_id}https://api.ddog-gov.com/api/v2/monitor/template/{template_id}https://api.datadoghq.com/api/v2/monitor/template/{template_id}https://api.us3.datadoghq.com/api/v2/monitor/template/{template_id}https://api.us5.datadoghq.com/api/v2/monitor/template/{template_id}
### Overview
Delete an existing monitor user template by its ID. This endpoint requires the `monitor_config_policy_write` permission.
### Arguments
#### Path Parameters
Name
Type
Description
template_id [_required_]
string
ID of the monitor user template.
### Response
  * [204](https://docs.datadoghq.com/api/latest/monitors/#DeleteMonitorUserTemplate-204-v2)
  * [404](https://docs.datadoghq.com/api/latest/monitors/#DeleteMonitorUserTemplate-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/monitors/#DeleteMonitorUserTemplate-429-v2)


OK
Not Found
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


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
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/monitors/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/monitors/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/monitors/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/monitors/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/monitors/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/monitors/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/monitors/?code-lang=typescript)


#####  Delete a monitor user template
Copy
```
                  # Path parameters  
export template_id="CHANGE_ME"  
# Curl command  
curl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/monitor/template/${template_id}" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Delete a monitor user template
```
"""
Delete a monitor user template returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.monitors_api import MonitorsApi

configuration = Configuration()
configuration.unstable_operations["delete_monitor_user_template"] = True
with ApiClient(configuration) as api_client:
    api_instance = MonitorsApi(api_client)
    api_instance.delete_monitor_user_template(
        template_id="template_id",
    )

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Delete a monitor user template
```
# Delete a monitor user template returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.delete_monitor_user_template".to_sym] = true
end
api_instance = DatadogAPIClient::V2::MonitorsAPI.new
api_instance.delete_monitor_user_template("template_id")

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Delete a monitor user template
```
// Delete a monitor user template returns "OK" response

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
	configuration.SetUnstableOperationEnabled("v2.DeleteMonitorUserTemplate", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewMonitorsApi(apiClient)
	r, err := api.DeleteMonitorUserTemplate(ctx, "template_id")

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `MonitorsApi.DeleteMonitorUserTemplate`: %v\n", err)
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

#####  Delete a monitor user template
```
// Delete a monitor user template returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.MonitorsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.deleteMonitorUserTemplate", true);
    MonitorsApi apiInstance = new MonitorsApi(defaultClient);

    try {
      apiInstance.deleteMonitorUserTemplate("template_id");
    } catch (ApiException e) {
      System.err.println("Exception when calling MonitorsApi#deleteMonitorUserTemplate");
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

#####  Delete a monitor user template
```
// Delete a monitor user template returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_monitors::MonitorsAPI;

#[tokio::main]
async fn main() {
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.DeleteMonitorUserTemplate", true);
    let api = MonitorsAPI::with_config(configuration);
    let resp = api
        .delete_monitor_user_template("template_id".to_string())
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

#####  Delete a monitor user template
```
/**
 * Delete a monitor user template returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.deleteMonitorUserTemplate"] = true;
const apiInstance = new v2.MonitorsApi(configuration);

const params: v2.MonitorsApiDeleteMonitorUserTemplateRequest = {
  templateId: "template_id",
};

apiInstance
  .deleteMonitorUserTemplate(params)
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
## [Validate a monitor user template](https://docs.datadoghq.com/api/latest/monitors/#validate-a-monitor-user-template)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/monitors/#validate-a-monitor-user-template-v2)


**Note** : This endpoint is in Preview. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
POST https://api.ap1.datadoghq.com/api/v2/monitor/template/validatehttps://api.ap2.datadoghq.com/api/v2/monitor/template/validatehttps://api.datadoghq.eu/api/v2/monitor/template/validatehttps://api.ddog-gov.com/api/v2/monitor/template/validatehttps://api.datadoghq.com/api/v2/monitor/template/validatehttps://api.us3.datadoghq.com/api/v2/monitor/template/validatehttps://api.us5.datadoghq.com/api/v2/monitor/template/validate
### Overview
Validate the structure and content of a monitor user template. This endpoint requires the `monitor_config_policy_write` permission.
### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


Field
Type
Description
data [_required_]
object
Monitor user template data.
attributes [_required_]
object
Attributes for a monitor user template.
description
string
A brief description of the monitor user template.
monitor_definition [_required_]
object
A valid monitor definition in the same format as the [V1 Monitor API](https://docs.datadoghq.com/api/latest/monitors/#create-a-monitor).
tags [_required_]
[string]
The definition of `MonitorUserTemplateTags` object.
template_variables
[object]
The definition of `MonitorUserTemplateTemplateVariables` object.
available_values
[string]
Available values for the variable.
defaults
[string]
Default values of the template variable.
name [_required_]
string
The name of the template variable.
tag_key
string
The tag key associated with the variable. This works the same as dashboard template variables.
title [_required_]
string
The title of the monitor user template.
type [_required_]
enum
Monitor user template resource type. Allowed enum values: `monitor-user-template`
default: `monitor-user-template`
```
{
  "data": {
    "attributes": {
      "description": "A description.",
      "monitor_definition": {
        "message": "A msg.",
        "name": "A name example-monitor",
        "query": "avg(last_5m):sum:system.net.bytes_rcvd{host:host0} > 100",
        "type": "query alert"
      },
      "tags": [
        "integration:Azure"
      ],
      "template_variables": [
        {
          "available_values": [
            "value1",
            "value2"
          ],
          "defaults": [
            "defaultValue"
          ],
          "name": "regionName",
          "tag_key": "datacenter"
        }
      ],
      "title": "Postgres DB example-monitor"
    },
    "type": "monitor-user-template"
  }
}
```

Copy
### Response
  * [204](https://docs.datadoghq.com/api/latest/monitors/#ValidateMonitorUserTemplate-204-v2)
  * [400](https://docs.datadoghq.com/api/latest/monitors/#ValidateMonitorUserTemplate-400-v2)
  * [429](https://docs.datadoghq.com/api/latest/monitors/#ValidateMonitorUserTemplate-429-v2)


OK
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


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
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/monitors/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/monitors/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/monitors/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/monitors/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/monitors/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/monitors/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/monitors/?code-lang=typescript)


#####  Validate a monitor user template returns "OK" response
Copy
```
                          # Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/monitor/template/validate" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "description": "A description.",
      "monitor_definition": {
        "message": "A msg.",
        "name": "A name example-monitor",
        "query": "avg(last_5m):sum:system.net.bytes_rcvd{host:host0} > 100",
        "type": "query alert"
      },
      "tags": [
        "integration:Azure"
      ],
      "template_variables": [
        {
          "available_values": [
            "value1",
            "value2"
          ],
          "defaults": [
            "defaultValue"
          ],
          "name": "regionName",
          "tag_key": "datacenter"
        }
      ],
      "title": "Postgres DB example-monitor"
    },
    "type": "monitor-user-template"
  }
}
EOF  

                        
```

#####  Validate a monitor user template returns "OK" response
```
// Validate a monitor user template returns "OK" response

package main

import (
	"context"
	"fmt"
	"os"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
	body := datadogV2.MonitorUserTemplateCreateRequest{
		Data: datadogV2.MonitorUserTemplateCreateData{
			Attributes: datadogV2.MonitorUserTemplateRequestAttributes{
				Description: *datadog.NewNullableString(datadog.PtrString("A description.")),
				MonitorDefinition: map[string]interface{}{
					"message": "A msg.",
					"name":    "A name example-monitor",
					"query":   "avg(last_5m):sum:system.net.bytes_rcvd{host:host0} > 100",
					"type":    "query alert",
				},
				Tags: []string{
					"integration:Azure",
				},
				TemplateVariables: []datadogV2.MonitorUserTemplateTemplateVariablesItems{
					{
						AvailableValues: []string{
							"value1",
							"value2",
						},
						Defaults: []string{
							"defaultValue",
						},
						Name:   "regionName",
						TagKey: datadog.PtrString("datacenter"),
					},
				},
				Title: "Postgres DB example-monitor",
			},
			Type: datadogV2.MONITORUSERTEMPLATERESOURCETYPE_MONITOR_USER_TEMPLATE,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	configuration.SetUnstableOperationEnabled("v2.ValidateMonitorUserTemplate", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewMonitorsApi(apiClient)
	r, err := api.ValidateMonitorUserTemplate(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `MonitorsApi.ValidateMonitorUserTemplate`: %v\n", err)
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

#####  Validate a monitor user template returns "OK" response
```
// Validate a monitor user template returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.MonitorsApi;
import com.datadog.api.client.v2.model.MonitorUserTemplateCreateData;
import com.datadog.api.client.v2.model.MonitorUserTemplateCreateRequest;
import com.datadog.api.client.v2.model.MonitorUserTemplateRequestAttributes;
import com.datadog.api.client.v2.model.MonitorUserTemplateResourceType;
import com.datadog.api.client.v2.model.MonitorUserTemplateTemplateVariablesItems;
import java.util.Arrays;
import java.util.Collections;
import java.util.Map;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.validateMonitorUserTemplate", true);
    MonitorsApi apiInstance = new MonitorsApi(defaultClient);

    MonitorUserTemplateCreateRequest body =
        new MonitorUserTemplateCreateRequest()
            .data(
                new MonitorUserTemplateCreateData()
                    .attributes(
                        new MonitorUserTemplateRequestAttributes()
                            .description("A description.")
                            .monitorDefinition(
                                Map.ofEntries(
                                    Map.entry("message", "A msg."),
                                    Map.entry("name", "A name example-monitor"),
                                    Map.entry(
                                        "query",
                                        "avg(last_5m):sum:system.net.bytes_rcvd{host:host0} > 100"),
                                    Map.entry("type", "query alert")))
                            .tags(Collections.singletonList("integration:Azure"))
                            .templateVariables(
                                Collections.singletonList(
                                    new MonitorUserTemplateTemplateVariablesItems()
                                        .availableValues(Arrays.asList("value1", "value2"))
                                        .defaults(Collections.singletonList("defaultValue"))
                                        .name("regionName")
                                        .tagKey("datacenter")))
                            .title("Postgres DB example-monitor"))
                    .type(MonitorUserTemplateResourceType.MONITOR_USER_TEMPLATE));

    try {
      apiInstance.validateMonitorUserTemplate(body);
    } catch (ApiException e) {
      System.err.println("Exception when calling MonitorsApi#validateMonitorUserTemplate");
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

#####  Validate a monitor user template returns "OK" response
```
"""
Validate a monitor user template returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.monitors_api import MonitorsApi
from datadog_api_client.v2.model.monitor_user_template_create_data import MonitorUserTemplateCreateData
from datadog_api_client.v2.model.monitor_user_template_create_request import MonitorUserTemplateCreateRequest
from datadog_api_client.v2.model.monitor_user_template_request_attributes import MonitorUserTemplateRequestAttributes
from datadog_api_client.v2.model.monitor_user_template_resource_type import MonitorUserTemplateResourceType
from datadog_api_client.v2.model.monitor_user_template_template_variables_items import (
    MonitorUserTemplateTemplateVariablesItems,
)

body = MonitorUserTemplateCreateRequest(
    data=MonitorUserTemplateCreateData(
        attributes=MonitorUserTemplateRequestAttributes(
            description="A description.",
            monitor_definition=dict(
                [
                    ("message", "A msg."),
                    ("name", "A name example-monitor"),
                    ("query", "avg(last_5m):sum:system.net.bytes_rcvd{host:host0} > 100"),
                    ("type", "query alert"),
                ]
            ),
            tags=[
                "integration:Azure",
            ],
            template_variables=[
                MonitorUserTemplateTemplateVariablesItems(
                    available_values=[
                        "value1",
                        "value2",
                    ],
                    defaults=[
                        "defaultValue",
                    ],
                    name="regionName",
                    tag_key="datacenter",
                ),
            ],
            title="Postgres DB example-monitor",
        ),
        type=MonitorUserTemplateResourceType.MONITOR_USER_TEMPLATE,
    ),
)

configuration = Configuration()
configuration.unstable_operations["validate_monitor_user_template"] = True
with ApiClient(configuration) as api_client:
    api_instance = MonitorsApi(api_client)
    api_instance.validate_monitor_user_template(body=body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Validate a monitor user template returns "OK" response
```
# Validate a monitor user template returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.validate_monitor_user_template".to_sym] = true
end
api_instance = DatadogAPIClient::V2::MonitorsAPI.new

body = DatadogAPIClient::V2::MonitorUserTemplateCreateRequest.new({
  data: DatadogAPIClient::V2::MonitorUserTemplateCreateData.new({
    attributes: DatadogAPIClient::V2::MonitorUserTemplateRequestAttributes.new({
      description: "A description.",
      monitor_definition: {
        "message": "A msg.", "name": "A name example-monitor", "query": "avg(last_5m):sum:system.net.bytes_rcvd{host:host0} > 100", "type": "query alert",
      },
      tags: [
        "integration:Azure",
      ],
      template_variables: [
        DatadogAPIClient::V2::MonitorUserTemplateTemplateVariablesItems.new({
          available_values: [
            "value1",
            "value2",
          ],
          defaults: [
            "defaultValue",
          ],
          name: "regionName",
          tag_key: "datacenter",
        }),
      ],
      title: "Postgres DB example-monitor",
    }),
    type: DatadogAPIClient::V2::MonitorUserTemplateResourceType::MONITOR_USER_TEMPLATE,
  }),
})
api_instance.validate_monitor_user_template(body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Validate a monitor user template returns "OK" response
```
// Validate a monitor user template returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_monitors::MonitorsAPI;
use datadog_api_client::datadogV2::model::MonitorUserTemplateCreateData;
use datadog_api_client::datadogV2::model::MonitorUserTemplateCreateRequest;
use datadog_api_client::datadogV2::model::MonitorUserTemplateRequestAttributes;
use datadog_api_client::datadogV2::model::MonitorUserTemplateResourceType;
use datadog_api_client::datadogV2::model::MonitorUserTemplateTemplateVariablesItems;
use serde_json::Value;
use std::collections::BTreeMap;

#[tokio::main]
async fn main() {
    let body = MonitorUserTemplateCreateRequest::new(MonitorUserTemplateCreateData::new(
        MonitorUserTemplateRequestAttributes::new(
            BTreeMap::from([
                ("message".to_string(), Value::from("A msg.")),
                ("name".to_string(), Value::from("A name example-monitor")),
                (
                    "query".to_string(),
                    Value::from("avg(last_5m):sum:system.net.bytes_rcvd{host:host0} > 100"),
                ),
                ("type".to_string(), Value::from("query alert")),
            ]),
            vec!["integration:Azure".to_string()],
            "Postgres DB example-monitor".to_string(),
        )
        .description(Some("A description.".to_string()))
        .template_variables(vec![MonitorUserTemplateTemplateVariablesItems::new(
            "regionName".to_string(),
        )
        .available_values(vec!["value1".to_string(), "value2".to_string()])
        .defaults(vec!["defaultValue".to_string()])
        .tag_key("datacenter".to_string())]),
        MonitorUserTemplateResourceType::MONITOR_USER_TEMPLATE,
    ));
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.ValidateMonitorUserTemplate", true);
    let api = MonitorsAPI::with_config(configuration);
    let resp = api.validate_monitor_user_template(body).await;
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

#####  Validate a monitor user template returns "OK" response
```
/**
 * Validate a monitor user template returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.validateMonitorUserTemplate"] = true;
const apiInstance = new v2.MonitorsApi(configuration);

const params: v2.MonitorsApiValidateMonitorUserTemplateRequest = {
  body: {
    data: {
      attributes: {
        description: "A description.",
        monitorDefinition: {
          message: "A msg.",
          name: "A name example-monitor",
          query: "avg(last_5m):sum:system.net.bytes_rcvd{host:host0} > 100",
          type: "query alert",
        },
        tags: ["integration:Azure"],
        templateVariables: [
          {
            availableValues: ["value1", "value2"],
            defaults: ["defaultValue"],
            name: "regionName",
            tagKey: "datacenter",
          },
        ],
        title: "Postgres DB example-monitor",
      },
      type: "monitor-user-template",
    },
  },
};

apiInstance
  .validateMonitorUserTemplate(params)
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
## [Validate an existing monitor user template](https://docs.datadoghq.com/api/latest/monitors/#validate-an-existing-monitor-user-template)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/monitors/#validate-an-existing-monitor-user-template-v2)


**Note** : This endpoint is in Preview. If you have any feedback, contact [Datadog support](https://docs.datadoghq.com/help/).
POST https://api.ap1.datadoghq.com/api/v2/monitor/template/{template_id}/validatehttps://api.ap2.datadoghq.com/api/v2/monitor/template/{template_id}/validatehttps://api.datadoghq.eu/api/v2/monitor/template/{template_id}/validatehttps://api.ddog-gov.com/api/v2/monitor/template/{template_id}/validatehttps://api.datadoghq.com/api/v2/monitor/template/{template_id}/validatehttps://api.us3.datadoghq.com/api/v2/monitor/template/{template_id}/validatehttps://api.us5.datadoghq.com/api/v2/monitor/template/{template_id}/validate
### Overview
Validate the structure and content of an existing monitor user template being updated to a new version. This endpoint requires the `monitor_config_policy_write` permission.
### Arguments
#### Path Parameters
Name
Type
Description
template_id [_required_]
string
ID of the monitor user template.
### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


Field
Type
Description
data [_required_]
object
Monitor user template data.
attributes [_required_]
object
Attributes for a monitor user template.
description
string
A brief description of the monitor user template.
monitor_definition [_required_]
object
A valid monitor definition in the same format as the [V1 Monitor API](https://docs.datadoghq.com/api/latest/monitors/#create-a-monitor).
tags [_required_]
[string]
The definition of `MonitorUserTemplateTags` object.
template_variables
[object]
The definition of `MonitorUserTemplateTemplateVariables` object.
available_values
[string]
Available values for the variable.
defaults
[string]
Default values of the template variable.
name [_required_]
string
The name of the template variable.
tag_key
string
The tag key associated with the variable. This works the same as dashboard template variables.
title [_required_]
string
The title of the monitor user template.
id [_required_]
string
The unique identifier.
type [_required_]
enum
Monitor user template resource type. Allowed enum values: `monitor-user-template`
default: `monitor-user-template`
```
{
  "data": {
    "attributes": {
      "description": "A description.",
      "monitor_definition": {
        "message": "A msg.",
        "name": "A name example-monitor",
        "query": "avg(last_5m):sum:system.net.bytes_rcvd{host:host0} > 100",
        "type": "query alert"
      },
      "tags": [
        "integration:Azure"
      ],
      "template_variables": [
        {
          "available_values": [
            "value1",
            "value2"
          ],
          "defaults": [
            "defaultValue"
          ],
          "name": "regionName",
          "tag_key": "datacenter"
        }
      ],
      "title": "Postgres DB example-monitor"
    },
    "id": "00000000-0000-1234-0000-000000000000",
    "type": "monitor-user-template"
  }
}
```

Copy
### Response
  * [204](https://docs.datadoghq.com/api/latest/monitors/#ValidateExistingMonitorUserTemplate-204-v2)
  * [400](https://docs.datadoghq.com/api/latest/monitors/#ValidateExistingMonitorUserTemplate-400-v2)
  * [404](https://docs.datadoghq.com/api/latest/monitors/#ValidateExistingMonitorUserTemplate-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/monitors/#ValidateExistingMonitorUserTemplate-429-v2)


OK
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


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
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


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
  * [Model](https://docs.datadoghq.com/api/latest/monitors/)
  * [Example](https://docs.datadoghq.com/api/latest/monitors/)


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
  * [Curl](https://docs.datadoghq.com/api/latest/monitors/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/monitors/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/monitors/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/monitors/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/monitors/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/monitors/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/monitors/?code-lang=typescript)


#####  Validate an existing monitor user template returns "OK" response
Copy
```
                          # Path parameters  
export template_id="00000000-0000-1234-0000-000000000000"  
# Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/monitor/template/${template_id}/validate" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "description": "A description.",
      "monitor_definition": {
        "message": "A msg.",
        "name": "A name example-monitor",
        "query": "avg(last_5m):sum:system.net.bytes_rcvd{host:host0} > 100",
        "type": "query alert"
      },
      "tags": [
        "integration:Azure"
      ],
      "template_variables": [
        {
          "available_values": [
            "value1",
            "value2"
          ],
          "defaults": [
            "defaultValue"
          ],
          "name": "regionName",
          "tag_key": "datacenter"
        }
      ],
      "title": "Postgres DB example-monitor"
    },
    "id": "00000000-0000-1234-0000-000000000000",
    "type": "monitor-user-template"
  }
}
EOF  

                        
```

#####  Validate an existing monitor user template returns "OK" response
```
// Validate an existing monitor user template returns "OK" response

package main

import (
	"context"
	"fmt"
	"os"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
	// there is a valid "monitor_user_template" in the system
	MonitorUserTemplateDataID := os.Getenv("MONITOR_USER_TEMPLATE_DATA_ID")

	body := datadogV2.MonitorUserTemplateUpdateRequest{
		Data: datadogV2.MonitorUserTemplateUpdateData{
			Attributes: datadogV2.MonitorUserTemplateRequestAttributes{
				Description: *datadog.NewNullableString(datadog.PtrString("A description.")),
				MonitorDefinition: map[string]interface{}{
					"message": "A msg.",
					"name":    "A name example-monitor",
					"query":   "avg(last_5m):sum:system.net.bytes_rcvd{host:host0} > 100",
					"type":    "query alert",
				},
				Tags: []string{
					"integration:Azure",
				},
				TemplateVariables: []datadogV2.MonitorUserTemplateTemplateVariablesItems{
					{
						AvailableValues: []string{
							"value1",
							"value2",
						},
						Defaults: []string{
							"defaultValue",
						},
						Name:   "regionName",
						TagKey: datadog.PtrString("datacenter"),
					},
				},
				Title: "Postgres DB example-monitor",
			},
			Id:   MonitorUserTemplateDataID,
			Type: datadogV2.MONITORUSERTEMPLATERESOURCETYPE_MONITOR_USER_TEMPLATE,
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	configuration.SetUnstableOperationEnabled("v2.ValidateExistingMonitorUserTemplate", true)
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewMonitorsApi(apiClient)
	r, err := api.ValidateExistingMonitorUserTemplate(ctx, MonitorUserTemplateDataID, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `MonitorsApi.ValidateExistingMonitorUserTemplate`: %v\n", err)
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

#####  Validate an existing monitor user template returns "OK" response
```
// Validate an existing monitor user template returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.MonitorsApi;
import com.datadog.api.client.v2.model.MonitorUserTemplateRequestAttributes;
import com.datadog.api.client.v2.model.MonitorUserTemplateResourceType;
import com.datadog.api.client.v2.model.MonitorUserTemplateTemplateVariablesItems;
import com.datadog.api.client.v2.model.MonitorUserTemplateUpdateData;
import com.datadog.api.client.v2.model.MonitorUserTemplateUpdateRequest;
import java.util.Arrays;
import java.util.Collections;
import java.util.Map;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    defaultClient.setUnstableOperationEnabled("v2.validateExistingMonitorUserTemplate", true);
    MonitorsApi apiInstance = new MonitorsApi(defaultClient);

    // there is a valid "monitor_user_template" in the system
    String MONITOR_USER_TEMPLATE_DATA_ID = System.getenv("MONITOR_USER_TEMPLATE_DATA_ID");

    MonitorUserTemplateUpdateRequest body =
        new MonitorUserTemplateUpdateRequest()
            .data(
                new MonitorUserTemplateUpdateData()
                    .attributes(
                        new MonitorUserTemplateRequestAttributes()
                            .description("A description.")
                            .monitorDefinition(
                                Map.ofEntries(
                                    Map.entry("message", "A msg."),
                                    Map.entry("name", "A name example-monitor"),
                                    Map.entry(
                                        "query",
                                        "avg(last_5m):sum:system.net.bytes_rcvd{host:host0} > 100"),
                                    Map.entry("type", "query alert")))
                            .tags(Collections.singletonList("integration:Azure"))
                            .templateVariables(
                                Collections.singletonList(
                                    new MonitorUserTemplateTemplateVariablesItems()
                                        .availableValues(Arrays.asList("value1", "value2"))
                                        .defaults(Collections.singletonList("defaultValue"))
                                        .name("regionName")
                                        .tagKey("datacenter")))
                            .title("Postgres DB example-monitor"))
                    .id(MONITOR_USER_TEMPLATE_DATA_ID)
                    .type(MonitorUserTemplateResourceType.MONITOR_USER_TEMPLATE));

    try {
      apiInstance.validateExistingMonitorUserTemplate(MONITOR_USER_TEMPLATE_DATA_ID, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling MonitorsApi#validateExistingMonitorUserTemplate");
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

#####  Validate an existing monitor user template returns "OK" response
```
"""
Validate an existing monitor user template returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.monitors_api import MonitorsApi
from datadog_api_client.v2.model.monitor_user_template_request_attributes import MonitorUserTemplateRequestAttributes
from datadog_api_client.v2.model.monitor_user_template_resource_type import MonitorUserTemplateResourceType
from datadog_api_client.v2.model.monitor_user_template_template_variables_items import (
    MonitorUserTemplateTemplateVariablesItems,
)
from datadog_api_client.v2.model.monitor_user_template_update_data import MonitorUserTemplateUpdateData
from datadog_api_client.v2.model.monitor_user_template_update_request import MonitorUserTemplateUpdateRequest

# there is a valid "monitor_user_template" in the system
MONITOR_USER_TEMPLATE_DATA_ID = environ["MONITOR_USER_TEMPLATE_DATA_ID"]

body = MonitorUserTemplateUpdateRequest(
    data=MonitorUserTemplateUpdateData(
        attributes=MonitorUserTemplateRequestAttributes(
            description="A description.",
            monitor_definition=dict(
                [
                    ("message", "A msg."),
                    ("name", "A name example-monitor"),
                    ("query", "avg(last_5m):sum:system.net.bytes_rcvd{host:host0} > 100"),
                    ("type", "query alert"),
                ]
            ),
            tags=[
                "integration:Azure",
            ],
            template_variables=[
                MonitorUserTemplateTemplateVariablesItems(
                    available_values=[
                        "value1",
                        "value2",
                    ],
                    defaults=[
                        "defaultValue",
                    ],
                    name="regionName",
                    tag_key="datacenter",
                ),
            ],
            title="Postgres DB example-monitor",
        ),
        id=MONITOR_USER_TEMPLATE_DATA_ID,
        type=MonitorUserTemplateResourceType.MONITOR_USER_TEMPLATE,
    ),
)

configuration = Configuration()
configuration.unstable_operations["validate_existing_monitor_user_template"] = True
with ApiClient(configuration) as api_client:
    api_instance = MonitorsApi(api_client)
    api_instance.validate_existing_monitor_user_template(template_id=MONITOR_USER_TEMPLATE_DATA_ID, body=body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Validate an existing monitor user template returns "OK" response
```
# Validate an existing monitor user template returns "OK" response

require "datadog_api_client"
DatadogAPIClient.configure do |config|
  config.unstable_operations["v2.validate_existing_monitor_user_template".to_sym] = true
end
api_instance = DatadogAPIClient::V2::MonitorsAPI.new

# there is a valid "monitor_user_template" in the system
MONITOR_USER_TEMPLATE_DATA_ID = ENV["MONITOR_USER_TEMPLATE_DATA_ID"]

body = DatadogAPIClient::V2::MonitorUserTemplateUpdateRequest.new({
  data: DatadogAPIClient::V2::MonitorUserTemplateUpdateData.new({
    attributes: DatadogAPIClient::V2::MonitorUserTemplateRequestAttributes.new({
      description: "A description.",
      monitor_definition: {
        "message": "A msg.", "name": "A name example-monitor", "query": "avg(last_5m):sum:system.net.bytes_rcvd{host:host0} > 100", "type": "query alert",
      },
      tags: [
        "integration:Azure",
      ],
      template_variables: [
        DatadogAPIClient::V2::MonitorUserTemplateTemplateVariablesItems.new({
          available_values: [
            "value1",
            "value2",
          ],
          defaults: [
            "defaultValue",
          ],
          name: "regionName",
          tag_key: "datacenter",
        }),
      ],
      title: "Postgres DB example-monitor",
    }),
    id: MONITOR_USER_TEMPLATE_DATA_ID,
    type: DatadogAPIClient::V2::MonitorUserTemplateResourceType::MONITOR_USER_TEMPLATE,
  }),
})
api_instance.validate_existing_monitor_user_template(MONITOR_USER_TEMPLATE_DATA_ID, body)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Validate an existing monitor user template returns "OK" response
```
// Validate an existing monitor user template returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_monitors::MonitorsAPI;
use datadog_api_client::datadogV2::model::MonitorUserTemplateRequestAttributes;
use datadog_api_client::datadogV2::model::MonitorUserTemplateResourceType;
use datadog_api_client::datadogV2::model::MonitorUserTemplateTemplateVariablesItems;
use datadog_api_client::datadogV2::model::MonitorUserTemplateUpdateData;
use datadog_api_client::datadogV2::model::MonitorUserTemplateUpdateRequest;
use serde_json::Value;
use std::collections::BTreeMap;

#[tokio::main]
async fn main() {
    // there is a valid "monitor_user_template" in the system
    let monitor_user_template_data_id = std::env::var("MONITOR_USER_TEMPLATE_DATA_ID").unwrap();
    let body = MonitorUserTemplateUpdateRequest::new(MonitorUserTemplateUpdateData::new(
        MonitorUserTemplateRequestAttributes::new(
            BTreeMap::from([
                ("message".to_string(), Value::from("A msg.")),
                ("name".to_string(), Value::from("A name example-monitor")),
                (
                    "query".to_string(),
                    Value::from("avg(last_5m):sum:system.net.bytes_rcvd{host:host0} > 100"),
                ),
                ("type".to_string(), Value::from("query alert")),
            ]),
            vec!["integration:Azure".to_string()],
            "Postgres DB example-monitor".to_string(),
        )
        .description(Some("A description.".to_string()))
        .template_variables(vec![MonitorUserTemplateTemplateVariablesItems::new(
            "regionName".to_string(),
        )
        .available_values(vec!["value1".to_string(), "value2".to_string()])
        .defaults(vec!["defaultValue".to_string()])
        .tag_key("datacenter".to_string())]),
        monitor_user_template_data_id.clone(),
        MonitorUserTemplateResourceType::MONITOR_USER_TEMPLATE,
    ));
    let mut configuration = datadog::Configuration::new();
    configuration.set_unstable_operation_enabled("v2.ValidateExistingMonitorUserTemplate", true);
    let api = MonitorsAPI::with_config(configuration);
    let resp = api
        .validate_existing_monitor_user_template(monitor_user_template_data_id.clone(), body)
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

#####  Validate an existing monitor user template returns "OK" response
```
/**
 * Validate an existing monitor user template returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
configuration.unstableOperations["v2.validateExistingMonitorUserTemplate"] =
  true;
const apiInstance = new v2.MonitorsApi(configuration);

// there is a valid "monitor_user_template" in the system
const MONITOR_USER_TEMPLATE_DATA_ID = process.env
  .MONITOR_USER_TEMPLATE_DATA_ID as string;

const params: v2.MonitorsApiValidateExistingMonitorUserTemplateRequest = {
  body: {
    data: {
      attributes: {
        description: "A description.",
        monitorDefinition: {
          message: "A msg.",
          name: "A name example-monitor",
          query: "avg(last_5m):sum:system.net.bytes_rcvd{host:host0} > 100",
          type: "query alert",
        },
        tags: ["integration:Azure"],
        templateVariables: [
          {
            availableValues: ["value1", "value2"],
            defaults: ["defaultValue"],
            name: "regionName",
            tagKey: "datacenter",
          },
        ],
        title: "Postgres DB example-monitor",
      },
      id: MONITOR_USER_TEMPLATE_DATA_ID,
      type: "monitor-user-template",
    },
  },
  templateId: MONITOR_USER_TEMPLATE_DATA_ID,
};

apiInstance
  .validateExistingMonitorUserTemplate(params)
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
![](https://id.rlcdn.com/464526.gif)![](https://t.co/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=3739093d-2e4b-4de6-96e8-bfee9390624a&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=c06e3c58-9146-4399-bf9e-49f62e42ca81&pt=Monitors&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fmonitors%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=3739093d-2e4b-4de6-96e8-bfee9390624a&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=c06e3c58-9146-4399-bf9e-49f62e42ca81&pt=Monitors&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fmonitors%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)
![](https://bat.bing.com/action/0?ti=4061438&Ver=2&mid=48f2d69f-8b1b-4119-b1c0-1295a47fb142&bo=2&sid=e9375cd0f0bd11f08bcff787fa0fba6f&vid=e9375d80f0bd11f0b5075ff6ae9d9677&vids=0&msclkid=N&pi=918639831&lg=en-US&sw=1080&sh=600&sc=24&tl=Monitors&p=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fmonitors%2F&r=&lt=33873&evt=pageLoad&sv=2&asc=G&cdb=AQAS&rn=509539)
