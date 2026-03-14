# Source: https://docs.snowflake.com/en/sql-reference/telemetry/events_view.md

# EVENTS_VIEW view

This view displays rows for telemetry data collected in the [default event table](../../developer-guide/logging-tracing/event-table-setting-up.md),
SNOWFLAKE.TELEMETRY.EVENTS.

You can manage access to this view with row access policies. To manage row access policies you create with this view, use the following stored
procedures:

* [ADD_ROW_ACCESS_POLICY_ON_EVENTS_VIEW](../stored-procedures/snowflake_telemetry_add_row_access_policy_on_events_view.md)
* [DROP_ROW_ACCESS_POLICY_ON_EVENTS_VIEW](../stored-procedures/snowflake_telemetry_drop_row_access_policy_on_events_view.md)

## Columns

Columns in this view correspond to columns in an event table you create. For more information, see
[Event table columns](../../developer-guide/logging-tracing/event-table-columns.md).

| Column Name | Data Type | Description |
| --- | --- | --- |
| TIMESTAMP | TIMESTAMP_NTZ | Timestamp when the event record was added. See [TIMESTAMP column](../../developer-guide/logging-tracing/event-table-columns.md). |
| START_TIMESTAMP | TIMESTAMP_NTZ | Event period starting timestamp for metrics and spans. See [START_TIMESTAMP column](../../developer-guide/logging-tracing/event-table-columns.md). |
| OBSERVED_TIMESTAMP | TIMESTAMP_NTZ | A log’s UTC timestamp. Used when capturing logs that do not have an accompanying timestamp. See [OBSERVED_TIMESTAMP column](../../developer-guide/logging-tracing/event-table-columns.md). |
| TRACE | OBJECT | Tracing context. See [TRACE column](../../developer-guide/logging-tracing/event-table-columns.md). |
| RESOURCE | OBJECT | For future use. See [RESOURCE column](../../developer-guide/logging-tracing/event-table-columns.md). |
| RESOURCE_ATTRIBUTES | OBJECT | Attributes that identify the source of an event. See [RESOURCE_ATTRIBUTES column](../../developer-guide/logging-tracing/event-table-columns.md). |
| SCOPE | OBJECT | Scope for signals. See [SCOPE column](../../developer-guide/logging-tracing/event-table-columns.md). |
| SCOPE_ATTRIBUTES | OBJECT | For future use. See [SCOPE_ATTRIBUTES column](../../developer-guide/logging-tracing/event-table-columns.md). |
| RECORD_TYPE | VARCHAR | Type of the value in the RECORD field. See [RECORD_TYPE column](../../developer-guide/logging-tracing/event-table-columns.md). |
| RECORD | OBJECT | Fixed fields for each signal type. See [RECORD column](../../developer-guide/logging-tracing/event-table-columns.md). |
| RECORD_ATTRIBUTES | OBJECT | Variable attributes for each signal type. See [RECORD_ATTRIBUTES column](../../developer-guide/logging-tracing/event-table-columns.md). |
| VALUE | VARIANT | Primary event value. See [VALUE column](../../developer-guide/logging-tracing/event-table-columns.md). |
| EXEMPLARS | ARRAY | Exemplars for metrics. See [EXEMPLARS column](../../developer-guide/logging-tracing/event-table-columns.md). |
