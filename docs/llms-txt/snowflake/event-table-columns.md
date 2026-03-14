# Source: https://docs.snowflake.com/en/developer-guide/logging-tracing/event-table-columns.md

# Event table columns

An [event table](event-table-setting-up.md) is a special kind of database table with a predefined set of
columns. The table’s structure is designed to support the data model for [OpenTelemetry](https://opentelemetry.io/), a framework for handling telemetry data.

For more information about working with event tables, see [Working with event tables](event-table-operations.md).

## Event table columns

Event tables have the following columns:

| Column | Data Type | Description |
| --- | --- | --- |
| TIMESTAMP | TIMESTAMP_NTZ | The UTC timestamp when an event was created. For events representing a span of time, this is the end of the time span. |
| START_TIMESTAMP | TIMESTAMP_NTZ | For events representing a span of time, such as trace events, the start of the time span as a UTC timestamp. |
| OBSERVED_TIMESTAMP | TIMESTAMP_NTZ | A UTC time used for logs. Currently the same value as for TIMESTAMP. |
| TRACE | OBJECT | Tracing context for all signal types. Contains string values `trace_id` and `span_id`. |
| RESOURCE | OBJECT | Reserved for future use. |
| RESOURCE_ATTRIBUTES | OBJECT | Attributes that identify the source of an event such as database, schema, user, warehouse, [Openflow](../../user-guide/data-integration/openflow/monitor.md), etc. |
| SCOPE | OBJECT | Scopes for events. For example, class names for logs. |
| SCOPE_ATTRIBUTES | OBJECT | Reserved for future use. |
| RECORD_TYPE | STRING | The event type. One of the following:   *`LOG` for a log message.* `SPAN` for user-defined function invocations performed sequentially on the same thread. For more information, see   RECORD_TYPE column. *`SPAN_EVENT` for a single trace event. A single query can emit more than one `SPAN_EVENT`.* `EVENT` for an event associated with an operation such as Iceberg automated refresh. |
| RECORD | OBJECT | Fixed values for each record type, as described in RECORD column. |
| RECORD_ATTRIBUTES | OBJECT | Variable attributes for each record type, as described in RECORD_ATTRIBUTES column. |
| VALUE | VARIANT | Primary event value. |
| EXEMPLARS | ARRAY | Reserved for future use. |

## Data captured by event type

### Data for logs

| Attribute | Description |
| --- | --- |
| OBSERVED_TIMESTAMP | Currently the same value as for TIMESTAMP. |
| RECORD | The severity level recorded by the log event. |
| RECORD_ATTRIBUTES | The location in code from which the log event was emitted. The values vary by language, but can include the code file path, function name, line number, and so on. |
| RECORD_TYPE | The event type: `LOG` for a log message |
| RESOURCE_ATTRIBUTES | Attributes that identify the source of the event, such as database, schema, user, warehouse, and so on. |
| SCOPE | Scope within which the event occurred, such as the name of the class where the log event was created. |
| TIMESTAMP | The timestamp when the event was created. |
| VALUE | The log message. |

### Data for metrics

| Attribute | Description |
| --- | --- |
| RECORD | For a metric event, an object that includes the metric’s name and unit. |
| RECORD_TYPE | The event type: `METRIC` for a metric data point. |
| RESOURCE_ATTRIBUTES | Attributes that identify the source of the event, such as database, schema, user, or warehouse. |
| START_TIMESTAMP | When the RECORD column `metric_type` value is `sum`, this is the time when the metric was collected. Not used when the `metric_type` value is `gauge`. |
| TIMESTAMP | The timestamp when the event was created. |
| VALUE | The numeric value of the metric. |

### Data for trace events

| Attribute | Description |
| --- | --- |
| RECORD | For a span, an object that includes the span’s name and kind; for a span event, the object includes the span’s name. |
| RECORD_ATTRIBUTES | Attribute data associated with a span or span event. |
| RECORD_TYPE | The event type: `SPAN` for a span, `SPAN_EVENT` for a span event. |
| RESOURCE_ATTRIBUTES | Attributes that identify the source of the event, such as database, schema, user, warehouse, and so on. |
| START_TIMESTAMP | For a span, the time when the span began. Not used for a span event. |
| TIMESTAMP | The timestamp when the event was created. |
| TRACE | Identifiers `trace_id` and `span_id` for a span and the span events within it. |

### Data for Iceberg automated refresh events

Snowflake logs an event to your event table when it processes a snapshot for [Iceberg automated refresh](../../user-guide/tables-iceberg-auto-refresh.md).
The following table describes the columns for Iceberg automated refresh events:

| Attribute | Description |
| --- | --- |
| TIMESTAMP | The timestamp when the event was created. |
| RESOURCE_ATTRIBUTES | Attributes that identify the Iceberg Auto Refresh event, such as database, schema, table, and catalog names. |
| RECORD_TYPE | The event type `EVENT`. |
| RECORD | Detailed information about the status of the operation associated with the event, including name and severity. |
| RECORD_ATTRIBUTES | Attributes associated with the event. |
| VALUE | Additional information specific to the event. |

## EXEMPLARS column

Reserved for future use.

## OBSERVED_TIMESTAMP column

A log’s UTC timestamp. Not used for trace events.

## RECORD column

Provides core information about the event, include the log level for a log event, or the name for trace event (span or span event record).

Attributes, if any, for the record are recorded in the RECORD_ATTRIBUTES column.

Values contained by this column will vary depending on the value of the RECORD_TYPE column
(`LOG`, `SPAN` or `SPAN_EVENT`), as described in the following sections.

### For `LOG` RECORD_TYPE

When the RECORD_TYPE column value is `LOG`, the RECORD column value contains the severity of the log message. The column value may
contain the following keys:

| Key | Type | Description |
| --- | --- | --- |
| `severity_text` | STRING | The text for the log severity. One of the following:   *`TRACE`* `DEBUG` *`INFO`* `WARN` *`ERROR`* `FATAL`   When the log entry is for an [unhandled exception](unhandled-exception-messages.md), this value is the highest-severity error level for the current language runtime. For example, for code written in Python, the value is `FATAL`. |

#### Example

```json
{
  "severity_text": "INFO"
}
```

### For `METRIC` RECORD_TYPE

Metrics are CPU and memory data generated by Snowflake. You can use this data to analyze resource consumption.

The execution handler language and its environment significantly affect the meaning of the metrics data. See
[Emitting metrics data from handler code](metrics-handler.md) for more information.

| Key | Type | Description |
| --- | --- | --- |
| `metric.name` | string | The name of the metric recorded by the row. One of the following:   *`process.memory.usage`: Amount of memory, in bytes, consumed during execution.* `process.cpu.utilization`: CPU use. Measured differently based on the handler language.   For more information, see [Emitting metrics data from handler code](metrics-handler.md). |
| `metric.unit` | string | The units of the metric; for example, `bytes`. |
| `metric_type` | string | The OpenTelemetry Metric Point type of the metric data; for example, `sum` or `gauge`. |
| `value_type` | string | The data type of the value in the VALUE column; for example, `DOUBLE` or `INT`. |

### Example

```json
{
  "metric": {
    "name": "process.memory.usage",
    "unit": "bytes"
  },
  "metric_type": "sum",
  "value_type": "INT"
}
```

### For `SPAN` RECORD_TYPE

Spans represent individual executions of functions and procedures. For stored procedures there will be a single span. For user-defined
functions there may be multiple spans for a single function call, depending on how Snowflake decides to schedule execution.

All spans for a given query have the same value for the `trace_id` key of the `TRACE` column.

The duration of a span is the difference between the values in the `start_timestamp` and `timestamp` columns, indicating the
time of the beginning and end of the span execution, respectively.

The ID of the span and the query trace are represented in the value in the TRACE column.

Snowflake will create one span for each execution with the keys shown below:

| Key | Type | Description |
| --- | --- | --- |
| `dropped_attributes_count` | int | The number of attributes ignored after the recorded maximum has been reached. |
| `name` | string | When the executable’s handler is written in Python, this identifies the handler for the function or procedure that emitted the data. This varies by executable type, as follows:   *Procedure: handler function name* User-defined function (UDF): handler function name *User-defined table function (UDTF): handler class name* Client code: name of the client-side API that began the span.   When the traced code is written in SQL, such as a SQL statement executed within a procedure, this is the name of the executed statement, such as `SELECT` or `INSERT`.  When the executable’s handler is written in a language other than Python or SQL, this is a fixed value such as `snow.auto_instrumented`. |
| `kind` | string | `SPAN_KIND_SERVER` when the traced code is written in SQL. Otherwise, this is the fixed value `SPAN_KIND_INTERNAL`. |
| `parent_span_id` | Hex string | Identifies the span of the procedure or UDF from which the current trace passed. When this value is present, it means that the current procedure or UDF call was made by another procedure in a call chain relationship. That “parent” procedure’s `span_id` value is the same as this `parent_span_id`. |
| `snow.process.memory.usage.max` | string | Optional. When present, specifies the maximum amount of memory, in bytes, used during this span’s execution. |
| `status` | string | `STATUS_CODE_ERROR` when the span corresponds to an [unhandled exception](unhandled-exception-messages.md). Otherwise, `STATUS_CODE_UNSET`. |

In the case of user-defined functions, Snowflake may add attributes for spans to indicate the number of rows processed and emitted by the function.

### For `SPAN_EVENT` RECORD_TYPE

Span events are event records attached to a particular span execution, described above. You can create events to fit the needs of your
application. The number of span events is limited to 128.

The value of the TRACE column will identify the span in which the event was created.

Span events have a single key, `name`, and can have arbitrary attributes added in the RECORD_ATTRIBUTES column.

| Key | Type | Description |
| --- | --- | --- |
| `name` | string | The name of the span event. |

### For `EVENT` RECORD_TYPE for Iceberg automated refresh events

| Key | Type | Description |
| --- | --- | --- |
| `name` | VARCHAR | The name of the event; for example, `iceberg_auto_refresh_snapshot_lifecycle` |
| `severity_text` | VARCHAR | The text for the event severity. One of the following values:   *`DEBUG`* `WARN` *`ERROR`   The severity text when the `snapshot_state` is `"errored"` is one of the following values:* `WARN` if Snowflake encountered an error that can be resolved without human intervention. * `ERROR` if Snowflake encountered an error that requires human intervention to resolve.   The `snapshot_state` is a key-value pair in an object in the VALUE column. For more information, see For EVENT VALUE for Iceberg automated refresh events. |

### For `EVENT` RECORD_TYPE for Snowflake Native Apps lifecycle events

| Key | Type | Description |
| --- | --- | --- |
| `name` | VARCHAR | The name of the event; for example, `application.state_change` |
| `severity_number` | NUMBER | The severity number of the event. |
| `severity_text` | VARCHAR | The text for the event severity. One of the following values:   *`INFO`* `WARN` * `ERROR` |

## RECORD_ATTRIBUTES column

Describes the event with metadata set by Snowflake or by code. The value will vary depending on the type of record the row
contains, as described in the following sections.

### For `LOG` RECORD_TYPE

The location in code from which the log event was emitted, including the code file path, function name, line number, and so on.

In addition to the attributes listed below, you can add your own attributes to include in the RECORD_ATTRIBUTES value.

| Attribute | Type | Description |
| --- | --- | --- |
| `code.filepath` | int | The file containing code that generated the message. |
| `code.function` | string | The name of the function that generated the message. |
| `code.lineno` | int | The line number in code that generated the message. |
| `code.namespace` | int | The namespace of code that generated the messages. |
| `exception.message` | string | The error message from an [unhandled exception](unhandled-exception-messages.md). |
| `exception.type` | string | The name of the class for an [unhandled exception](unhandled-exception-messages.md). |
| `exception.stacktrace` | string | An [unhandled exception](unhandled-exception-messages.md)’s stack trace formatted by a language runtime. |
| `exception.escaped` | boolean | `true` if this entry is from an [unhandled exception](unhandled-exception-messages.md). |
| `thread.id` | int | The thread on which the log event was created. |
| `thread.name` | string | The thread on which the log event was created. |

### Example

In the following example, all attributes have been added by Snowflake except `employee.id`, which was added by a custom attribute.

```json
{
  "code.filepath": "main.scala",
  "code.function": "$anonfun$new$10",
  "code.lineno": 149,
  "code.namespace": "main.main$",
  "thread.id": 1,
  "thread.name": "main"
  "employee.id": "52307953446424"
}
```

### For `SPAN` RECORD_TYPE

Attributes, if any, assigned to the span when it is recorded. Attribute names and values are set by code or by Snowflake.

The following table lists attributes that might be set by Snowflake.

| Attribute | Type | Description |
| --- | --- | --- |
| `db.query.executable.names` | string | The names of the executables executed under the query traced in this span. |
| `db.query.table.names` | string | The names of tables read or modified in the query traced in this span. |
| `db.query.view.names` | string | The names of views accessed in the query traced in this span. |
| `db.query.text` | string | The text of the SQL query traced in this span. Included only if SQL trace query text is enabled for tracing. For more information, see [SQL statement tracing](tracing.md). |
| `snow.input.rows` | int | The number of input rows processed by the span of the function. |
| `snow.output.rows` | int | The number of output rows successfully processed by the span of the function. |

#### Example

Code in the following example includes attributes set by Snowflake.

```json
{
  "snow.input.rows": 12
  "snow.output.rows": 12
}
```

#### Example

Code in the following example includes attributes set by handler code.

```json
{
  "MyFunctionVersion": "1.1.0"
}
```

### For `SPAN_EVENT` RECORD_TYPE

Attributes, if any, assigned to the span event when it is recorded. Attribute names and values may be set by Snowflake or by user code.

#### Example

Code in the following example includes attributes set by handler code.

```json
{
  "mykey1": "value1",
  "mykey2": "value2"
}
```

### For `EVENT` RECORD_TYPE for Iceberg automated refresh events

Attributes assigned to the EVENT event when it is recorded for [Iceberg automated refresh](../../user-guide/tables-iceberg-auto-refresh.md).
Attribute names and values are set by Snowflake.

| Attribute | Type | Description | Example |
| --- | --- | --- | --- |
| `snow.snapshot.id` | INTEGER | The ID of the Iceberg snapshot being processed during Iceberg automated refresh. NULL if the automated refresh process fails. | `12345` |

## RECORD_TYPE column

Specifies the kind of record described by the event table row. This column’s value identifies which of the various types of records for which
the event table may contain data.

The RECORD column contains this
record’s data. The RECORD_ATTRIBUTES column contains this record’s metadata, if any.

The following table lists possible values for this column.

| Column Value | Description |
| --- | --- |
| `LOG` | The row represents a log entry generated by handler code. |
| `SPAN` | The row represents a span.  For a stored procedure there will be a single span. For a user-defined function, which may be parallelized, there will be a span for each thread on which the function executes. The number of threads will vary depending on multiple factors, including the size of the Snowflake warehouse in which the function executes.  A span may contain multiple span events. For more information, see [Span data recorded](tracing-how-events-work.md). |
| `SPAN_EVENT` | The row represents a span event. The may be multiple span event records attached to a particular span. Your handler code may create events to fit your needs. The number of span events is limited to 128. |
| `METRIC` | The row represents an observation of a metric. Multiple observations of multiple metrics can be associated with a particular span. |
| `EVENT` | The row represents an event associated with a particular operation, such as Iceberg automated refresh. |

## RESOURCE column

Reserved for future use.

## RESOURCE_ATTRIBUTES column

Describes the source of an event in terms of Snowflake objects.

Attributes making up this column’s value are set by Snowflake and cannot be changed.

### Resource attributes for event source

> **Note:**
>
> When the event source is Iceberg automated refresh, only the following attribute types are set:
>
> * snow.catalog.integration.name
> * snow.catalog.table.name
> * snow.database.name
> * snow.schema.name
> * snow.table.name

| Attribute Name | Attribute Type | Description | Example |
| --- | --- | --- | --- |
| `snow.catalog.integration.name` | string | The name of the catalog integration associated with the executable for Iceberg automated refresh. | `MY_CATALOG_INTEGRATION_NAME` |
| `snow.catalog.table.name` | string | The name of the Iceberg table in the catalog. | `MY_CATALOG_TABLE_NAME` |
| `snow.database.id` | int | The internal/system-generated identifier of the database containing the executable. | `12345` |
| `snow.database.name` | string | The name of the database containing the executable. | `MY_DATABASE` |
| `snow.executable.id` | int | The internal/system-generated identifier of the executable (procedure, function, SnowService, etc.) generating the event. | `12345` |
| `snow.executable.name` | string | The name of the executable generating the event. For example, this might be the name of the procedure, function, or Streamlit app. | `MY_UDF` |
| `snow.executable.runtime.version` | string | The executable language’s runtime version. This will be a value specific to the language, as described below:   *Java: `11` or `17`* JavaScript: No value *Python: From `3.10` to `3.12`* Scala: `2.12` * SQL: No value | `procedure` |
| `snow.executable.type` | string | One of the following:   *`procedure` for stored procedure* `function` for a user-defined function *`query` for an event in which SQL was executed, such as when a SQL statement is executed within a stored procedure.* `sql` for an event from a single query, such as a Snowflake Scripting block. *`spcs` for a Snowpark Container Services service.* `streamlit` for a Streamlit app | `procedure` |
| `snow.owner.id` | int | The internal/system-generated identifier of the role with OWNERSHIP privilege for the executable. | `1234` |
| `snow.owner.name` | string | The name of the role with OWNERSHIP privilege for the executable. | `UDF_OWNER_RL` |
| `snow.schema.id` | int | The internal/system-generated identifier of the schema containing the executable. | `12345` |
| `snow.schema.name` | string | The name of the schema containing the executable. | `MY_SCHEMA` |
| `snow.table.name` | string | The name of the table associated with the executable. | `MY_TABLE_NAME` |
| `telemetry.sdk.language` | string | The language of the resource/SDK. Snowflake uses java, scala, python, javascript and sql. | `java` |

### Resource attributes for execution environment

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `db.user` | string | For a function or procedure, the name of the user executing the function or procedure. For a Streamlit app, the name of the user who was viewing the app for a given event. | `MY_USER_NAME` |
| `snow.query.id` | string | The ID of the query. | `01a6aeb7-0604-c466-0000-097127d13812` |
| `snow.release.version` | string | The Snowflake release running when event was generated | `7.9.0` |
| `snow.session.id` | int | The ID of the session running the executable. | `10` |
| `snow.session.role.primary.id` | int | The internal/system-generated identifier of the primary role in the session. | `10` |
| `snow.session.role.primary.name` | string | The name of the primary role in the session. | `MY_ROLE` |
| `snow.user.id` | int | The internal/system-generated identifier of the user running the query. | `1234` |
| `snow.warehouse.id` | int | The internal/system-generated identifier of the warehouse running the query generating the event. | `12345` |
| `snow.warehouse.name` | string | The name of the warehouse running the query generating the event. | `MY_WAREHOUSE` |

### Resource attributes for apps

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `snow.application.consumer.name` | string | For a Snowflake Native App, the name of the consumer’s account. | `CONSUMER_NAME` |
| `snow.application.consumer.organization` | string | For a Snowflake Native App, the name of the consumer’s organization. | `CONSUMER_ORG_NAME` |
| `snow.application.id` | string | For a Snowflake Native App, the internal/system-generated identifier of the app. | `ABCZN3J3` |
| `snow.application.name` | string | For a Snowflake Native App, the name of the app. | `MY_INSTALLED_APP_NAME` |
| `snow.application.package.name` | string | For a Snowflake Native App, the name of the application package. | `MY_INSTALLED_PACKAGE_NAME` |
| `snow.listing.global_name` | string | For a Snowflake Native App, the internal/system-generated identifier of the listing. | `GZYZN3J3` |
| `snow.listing.name` | string | For a Snowflake Native App, the name of the listing. | `MY_LISTING_NAME` |

### Resource attributes for Snowflake version

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `service.version` | string | The version of the executable, where relevant. The combination of `snow.version` and `snow.patch` joined by a dot where they exist. Standard OpenTelemetry attribute. | `2.3.1` |
| `snow.patch` | string | The patch level of the executable running. | `1` |
| `snow.version` | string | The version of the executable running. | `2.3` |

### Example

```json
{
  "db.user": "MYUSERNAME",
  "snow.database.id": 13,
  "snow.database.name": "MY_DB",
  "snow.executable.id": 197,
  "snow.executable.name": "FUNCTION_NAME(I NUMBER):ARG_NAME(38,0)",
  "snow.executable.type": "FUNCTION",
  "snow.owner.id": 2,
  "snow.owner.name": "MY_ROLE",
  "snow.query.id": "01ab0f07-0000-15c8-0000-0129000592c2",
  "snow.schema.id": 16,
  "snow.schema.name": "PUBLIC",
  "snow.session.id": 1275605667850,
  "snow.session.role.primary.id": 2,
  "snow.session.role.primary.name": "MY_ROLE",
  "snow.user.id": 25,
  "snow.warehouse.id": 5,
  "snow.warehouse.name": "MYWH",
  "telemetry.sdk.language": "python"
}
```

## SCOPE column

For log events, the namespace of the code that emitted the event, such as the name of the class creating a log entry. This is not used
for trace events.

The following table lists attributes that may be included in this column.

### Scope value

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `name` | String | Namespace of code emitting the event. | `com.sample.MyClass` |

### Example

```json
{
  "name": "com.sample.MyClass"
}
```

## SCOPE_ATTRIBUTES column

Reserved for future use.

## START_TIMESTAMP column

The time a span started as a UTC timestamp.

| RECORD_TYPE Column Value | START_TIMESTAMP Value Description |
| --- | --- |
| `LOG` | Not used. |
| `SPAN` | The time the span started. |
| `SPAN_EVENT` | Not used. |
| `METRIC` | When the RECORD column `metric_type` value is `sum`, this is the time when the metric was collected. Not used when the `metric_type` value is `gauge`. |

## TIMESTAMP column

The time an event was emitted. The value’s meaning will vary depending on the type of record the row represents, as listed in the following
table:

| RECORD_TYPE Column Value | TIMESTAMP Value Description |
| --- | --- |
| `LOG` | The wall-clock time that the event was emitted. |
| `SPAN` | The time at which execution concluded. |
| `SPAN_EVENT` | The wall-clock time that the event was emitted. |

## TRACE column

Unique identifiers representing execution for functions and procedures.

| RECORD_TYPE Column Value | TRACE Value Description |
| --- | --- |
| `LOG` | Not used. |
| `SPAN` | `trace_id` and `span_id` |
| `SPAN_EVENT` | `trace_id` and `span_id` |

### Trace value

The following table lists attributes that may be included in this column.

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `span_id` | Hex string | A unique identifier to the threading model. Procedures, which are single-threaded, will have a single `span_id` value. Functions, which may be executed by Snowflake on multiple threads (such as for multiple rows), may have multiple `span_id` values.  When the current span is from a procedure that called another procedure or UDF in the trace, this `span_id` value is the same as the RECORD column `parent_span_id` value of the span for the procedure or UDF it called. | `b4c28078330873a2` |
| `trace_id` | Hex string | A unique identifier for calls made from a query. When a stored procedure is not being called in a chain of calls, each call has its own `trace_id` value. Within a query, calls to all functions made from the query share the same `trace_id` value.  When a procedure is called by another procedure or UDF in a call chain, it has the same `trace_id` value as other procedures and UDFs in the chain.  This value is unique for each query and will be the same for all spans within a query. You can use it for grouping events within a single query execution. | `6992e9febf0b97f45b34a62e54936adb` |

### Example

Code in the following example shows the attributes that would be present for a span or span event.

```json
{
  "span_id": "b4c28078330873a2",
  "trace_id": "6992e9febf0b97f45b34a62e54936adb"
}
```

## VALUE column

* For log events, this is usually the log message. When the event logged is for an
  [unhandled exception](unhandled-exception-messages.md), the value in this column will be simply
  `exception`.
* For metrics, this is the numeric value of the metric.

Note that the VALUE column’s type is VARIANT (not STRING) so that it can have non-string values for some languages, such as JavaScript.

### For `EVENT` VALUE for Iceberg automated refresh events

| Key | Type | Description | Example |
| --- | --- | --- | --- |
| `metadata_file_location` | VARCHAR | The location of the Iceberg metadata file, which can be NULL if the automated refresh process failed. | `"s3://my_bucket/iceberg_snapshots/metadata/...metadata.json"` |
| `snapshot_state` | VARCHAR | The state of the automated refresh process, which can be one of the following values:   *`started`: Snowflake has started to process a snapshot.* `completed`: Snowflake completed processing a snapshot * `errored`: Snowflake failed to process a snapshot. | `"errored"` |
| `error_message` | VARCHAR | If the value in `snapshot_state` is `errored`, this column includes an error message. | “Iceberg Auto Refresh encountered a fatal error. Please disable Auto Refresh and manually refresh the table before re-enabling Auto Refresh. FailedMetadataFile: s3://my_bucket/…, FailedSnapshotId: null.n” |

### For `EVENT` VALUE for Snowflake Native Apps application lifecycle events

| Key | Type | Description |
| --- | --- | --- |
| `upgrade_state` | VARCHAR | The current state of the background installation or upgrade. |
| `upgrade_attempt` | VARCHAR | Indicates whether an upgrade was attempted for the app. |
| `target_upgrade_version` | VARCHAR | The version of the app that is running or pending upgrade. |
| `target_upgrade_patch` | VARCHAR | The version patch level of the app that is running or pending upgrade. |
| `upgrade_failure_reason` | VARCHAR | The reason the upgrade failed, if applicable. |
| `health_status` | VARCHAR | The health status of the app. Possible values:   *`OK`* `PAUSE` * `FAILED` |
| `action` | VARCHAR | The action applied to privileges during installation or upgrade. Possible values:   *`GRANTED`* `REVOKED` |
| `privileges` | VARCHAR | A list of privileges that were granted or revoked during installation or upgrade. |

### Example

```json
{
  "metadata_file_location": "<path>",
  "snapshot_state": "errored",
  "error_message": "<error_message>"
}
```
