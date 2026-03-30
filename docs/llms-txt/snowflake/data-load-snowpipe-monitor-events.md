# Source: https://docs.snowflake.com/en/user-guide/data-load-snowpipe-monitor-events.md

# Monitor events for Snowpipe

You can configure Snowflake to record events that provide detailed information about the status of your pipes. These events are captured in the active event table associated with the pipe.

By monitoring these events, you can gain insights into the following areas:

* Pipe status changes: Track the operational state of your Snowpipes.
* File processing progress: Understand the journey of files through the Snowpipe system.
* Periodic, aggregated, ingestion statistics digest: Get summarized statistics on data ingestion.

Additionally, you can configure alerts for the following critical conditions:

* High volume of incoming files
* High ingestion latencies
* Pipe errors
* File errors

The following sections explain how to enable event logging for Snowpipe, configure the log level, and interpret the events recorded in the event table:

* Snowpipe event types: Learn about the different categories of events and their details.
* Set the severity level of events to capture: Configure which events are recorded based on their importance.
* Query the event table for Snowpipe events: Discover how to retrieve and analyze event data.
* Information logged for Snowpipe events: Understand the structure and meaning of the data within the event table columns.

> **Caution:**
>
> Logging events for Snowpipe incurs costs. For more information, see [Costs of telemetry data collection](../developer-guide/logging-tracing/logging-tracing-billing.md).

## Snowpipe event types

Snowpipe events are identified by the `name` attribute within the `RECORD` column of your event table.

### file_lifecycle

`file_lifecycle` events track a file’s journey through the Snowpipe system. The state of a file can be `RECEIVED`, `INGESTED`, or `ERRORED`.

`RECEIVED`: An event is emitted when Snowpipe receives a file request. The pipe might skip this file if it was previously processed; in such cases, the `skipped` attribute indicates this.

```json
{
  "TIMESTAMP": "<some_timestamp>",
  "RESOURCE_ATTRIBUTES": {
    "snow.database.name": "<MY_DB_NAME>",
    "snow.schema.name": "<MY_SCHEMA_NAME>",
    "snow.pipe.name": "<MY_PIPE_NAME>"
  },
  "RECORD_TYPE": "EVENT",
  "RECORD": {
    "name": "file_lifecycle",
    "severity_text": "DEBUG"
  },
  "RECORD_ATTRIBUTES": {
    "snow.file.path": "<a/path/to/a/file>"
  },
  "VALUE": {
    "notification_channel": "<notification_channel>",
    "file_content_key": "<file_content_key>",
    "last_modified_time": "<last_modified_time>",
    "state": "<received_or_skipped>"
  }
}
```

`INGESTED`: An event is emitted after the file is successfully ingested by Snowpipe.

```json
{
  "TIMESTAMP": "<some_timestamp>",
  "RESOURCE_ATTRIBUTES": {
    "snow.database.name": "<MY_DB_NAME>",
    "snow.schema.name": "<MY_SCHEMA_NAME>",
    "snow.pipe.name": "<MY_PIPE_NAME>"
  },
  "RECORD_TYPE": "EVENT",
  "RECORD": {
    "name": "file_lifecycle",
    "severity_text": "DEBUG"
  },
  "RECORD_ATTRIBUTES": {
    "snow.file.path": "<a/path/to/a/file>"
  },
  "VALUE": {
    "notification_channel": "<notification_channel>",
    "file_content_key": "<file_content_key>",
    "state": "ingested"
  }
}
```

`ERRORED`: An event is emitted if the file failed to be ingested by Snowpipe.

```json
{
  "TIMESTAMP": "<some_timestamp>",
  "RESOURCE_ATTRIBUTES": {
    "snow.database.name": "<MY_DB_NAME>",
    "snow.schema.name": "<MY_SCHEMA_NAME>",
    "snow.pipe.name": "<MY_PIPE_NAME>"
  },
  "RECORD_TYPE": "EVENT",
  "RECORD": {
    "name": "file_lifecycle",
    "severity_text": "ERROR"
  },
  "RECORD_ATTRIBUTES": {
    "snow.file.path": "<a/path/to/a/file>"
  },
  "VALUE": {
    "notification_channel": "<notification_channel>",
    "file_content_key": "<file_content_key>",
    "first_error_message": "<first_error_message>",
    "first_error_line_number": "<some_number>",
    "first_error_character_pos": "<some_character_pos>",
    "error_count": "<error_count>",
    "error_limit": "<error_limit>",
    "file_state": "FAILED"
  }
}
```

### notification_received

This event is emitted when Snowflake receives a notification message.

```json
{
  "TIMESTAMP": "<some_timestamp>",
  "RESOURCE_ATTRIBUTES": {
    "notification_channel_name": "<notification_channel_name>"
  },
  "RECORD_TYPE": "EVENT",
  "RECORD": {
    "name": "notification_received",
    "severity_text": "TRACE"
  },
  "VALUE": {
    "file_path": "<a/path/to/a/file>",
    "file_content_key": "<file_content_key>",
    "upstream_event_time": "<upstream_event_time>"
  }
}
```

### notification_channel_errored

This event is emitted when an error occurs while Snowflake is reading messages from a notification channel. This typically indicates a user configuration error, such as an authorization issue.

```json
{
  "TIMESTAMP": "<some_timestamp>",
  "RESOURCE_ATTRIBUTES": {
    "notification_channel_name": "<notification_channel_name>"
  },
  "RECORD_TYPE": "EVENT",
  "RECORD": {
    "name": "notification_channel_errored",
    "severity_text": "ERROR"
  },
  "VALUE": {
    "first_error_message": "<error_message>"
  }
}
```

### pipe_lifecycle

This event is emitted when the [status of a pipe](../sql-reference/functions/system_pipe_status.md) changes. The new status can be `RUNNING`, `PAUSED`, `STOPPED`, or `STALLED`.

For RUNNING or PAUSED pipe statuses:

```json
{
  "TIMESTAMP": "<some_timestamp>",
  "RESOURCE_ATTRIBUTES": {
    "snow.database.name": "<MY_DB_NAME>",
    "snow.schema.name": "<MY_SCHEMA_NAME>",
    "snow.pipe.name": "<MY_PIPE_NAME>"
  },
  "RECORD_TYPE": "EVENT",
  "RECORD": {
    "name": "pipe_lifecycle",
    "severity_text": "INFO"
  },
  "VALUE": {
    "state": "<running_or_paused>"
  }
}
```

For STOPPED_\* or STALLED_\* pipe statuses: These statuses indicate that a pipe has unexpectedly stopped processing files.

```json
{
  "TIMESTAMP": "<some_timestamp>",
  "RESOURCE_ATTRIBUTES": {
    "snow.database.name": "<MY_DB_NAME>",
    "snow.schema.name": "<MY_SCHEMA_NAME>",
    "snow.pipe.name": "<MY_PIPE_NAME>"
  },
  "RECORD_TYPE": "EVENT",
  "RECORD": {
    "name": "pipe_lifecycle",
    "severity_text": "<WARN_or_ERROR>"
  },
  "VALUE": {
    "state": "<pipe_status>",
    "error_message": "<error_message>"
  }
}
```

The `severity_text` for `STOPPED_*` or `STALLED_*` states depends on the specific reason:

`WARN` if the pipe stopped because of the following reasons:

* `STOPPED_BY_SNOWFLAKE_ADMIN`
* `STOPPED_CLONED`
* `STOPPED_FEATURE_DISABLED`

`ERROR` if the pipe stopped because of the following reasons:

* `STOPPED_STAGE_ALTERED`
* `STOPPED_STAGE_DROPPED`
* `STOPPED_FILE_FORMAT_DROPPED`
* `STOPPED_NOTIFICATION_INTEGRATION_DROPPED`
* `STOPPED_MISSING_PIPE`
* `STOPPED_MISSING_TABLE`
* `STALLED_COMPILATION_ERROR`
* `STALLED_INITIALIZATION_ERROR`
* `STALLED_EXECUTION_ERROR`
* `STALLED_INTERNAL_ERROR`
* `STALLED_STAGE_PERMISSION_ERROR`

### pipe_throttled

This event is emitted if a Snowpipe is throttled.

```json
{
  "TIMESTAMP": "<some_timestamp>",
  "RESOURCE_ATTRIBUTES": {
    "snow.database.name": "<MY_DB_NAME>",
    "snow.schema.name": "<MY_SCHEMA_NAME>",
    "snow.pipe.name": "<MY_PIPE_NAME>"
  },
  "RECORD_TYPE": "EVENT",
  "RECORD": {
    "name": "pipe_throttled",
    "severity_text": "WARN"
  },
  "VALUE": {
    "throttled_files": "<throttled_file_name_list>"
  }
}
```

## Set the severity level of events to capture

To enable Snowpipe events to be recorded in an event table, you must set the `LOG_LEVEL` parameter at either the pipe level or the account level. The `LOG_LEVEL` determines which events are captured based on their severity:

* `ERROR`: Use for events that signal a change that requires human intervention to resolve.
* `WARN`: Use for events that signal an issue that can be resolved without human intervention.
* `INFO`: Use for user-initiated events that are generally useful and aren’t high- volume events.
* `DEBUG`: Use for high-volume events.
* `TRACE`: The lowest level of logging, that captures very detailed information.

> **Caution:**
>
> If the severity level isn’t set at the account level or pipe level, no events are captured.

**Examples:**

To capture ERROR-level events for all objects in an account, run the following code:

```sqlexample
ALTER ACCOUNT <my_account_name> SET LOG_LEVEL = ERROR;
```

To capture INFO-level events for a specific pipe, run the following code:

```sqlexample
ALTER PIPE <my_pipe_name> SET LOG_LEVEL = INFO;
```

## Log level for each event type

The following table summarizes the default or recommended `LOG_LEVEL` for each Snowpipe event type:

| Event | Log Level |
| --- | --- |
| file_lifecycle - RECEIVED, INGESTED | DEBUG |
| file_lifecycle - ERRORED | ERROR |
| notification_received | TRACE |
| notification_channel_errored | ERROR |
| pipe_lifecycle - RUNNING, PAUSED | INFO |
| pipe_lifecycle - STOPPED | WARN or ERROR (see the following section) |
| pipe_throttled | WARN |

**pipe_lifecycle - STOPPED log-level details:**

`WARN` if the pipe stopped because of the following reasons:

* `STOPPED_BY_SNOWFLAKE_ADMIN`
* `STOPPED_CLONED`
* `STOPPED_FEATURE_DISABLED`

`ERROR` if the pipe stopped because of the following reasons:

* `STOPPED_STAGE_ALTERED`
* `STOPPED_STAGE_DROPPED`
* `STOPPED_FILE_FORMAT_DROPPED`
* `STOPPED_NOTIFICATION_INTEGRATION_DROPPED`
* `STOPPED_MISSING_PIPE`
* `STOPPED_MISSING_TABLE`
* `STALLED_COMPILATION_ERROR`
* `STALLED_INITIALIZATION_ERROR`
* `STALLED_EXECUTION_ERROR`
* `STALLED_INTERNAL_ERROR`
* `STALLED_STAGE_PERMISSION_ERROR`

## Query the event table for Snowpipe events

Before you query, ensure that you have set up an event table and configured the severity level you want for events to be captured.

The following example query shows how to retrieve Snowpipe events, such as those generated during file ingestion:

```sqlexample
SELECT
    record_type,
    record:"name" AS event_name,
    record:"severity_text" AS log_level,
    resource_attributes:"snow.database.name" AS database_name,
    resource_attributes:"snow.schema.name" AS schema_name,
    resource_attributes:"snow.pipe.name" AS pipe_name,
    record_attributes,
    PARSE_JSON(value):file_content_key AS file_content_key,
    PARSE_JSON(value):state AS state
FROM {my_event_table_name}
ORDER BY state;
```

**Example output (successful file ingestion):**

The following output shows both RECEIVED and INGESTED events for a file, which indicates successful processing:

| SCOPE | RECORD_TYPE | EVENT_NAME | LOG_LEVEL | DATABASE_NAME | SCHEMA_NAME | PIPE_NAME | RECORD_ATTRIBUTES | FILE_CONTENT_KEY | STATE |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [NULL] | EVENT | “file_lifecycle” | “DEBUG” | “TESTDB” | “TESTSH” | “MYPIPE” | { “snow.file.path”: “data_0_0_0.event” } | “ba1f2511fc30423bdbb183fe33f3dd0f” | “INGESTED” |
| [NULL] | EVENT | “file_lifecycle” | “DEBUG” | “TESTDB” | “TESTSH” | “MYPIPE” | { “snow.file.path”: “data_0_0_0.event” } | “ba1f2511fc30423bdbb183fe33f3dd0f” | “RECEIVED” |

## Information logged for Snowpipe events

The following sections describe the key columns and their contents within the event table for Snowpipe events. If a column isn’t explicitly listed in the following sections, its value is NULL for Snowpipe events.

## Event table column values

| Column | Data Type | Description |
| --- | --- | --- |
| timestamp | TIMESTAMP_NTZ | The UTC timestamp when the event was created. |
| resource_attributes | OBJECT | Attributes that identify the Snowpipe event, such as database, schema, and pipe names. |
| record_type | STRING | The type of event recorded. For Snowpipe events, this value is always EVENT. |
| record | OBJECT | Contains detailed information about the status of running the Snowpipe event, including name and severity_text. |
| value | VARIANT | Additional information specific to the Snowpipe event. If the Snowpipe task failed, this includes the error message. |

## Key-value pairs in the resource_attributes column

The `resource_attributes` column contains an OBJECT value with the following key-value pairs:

| Attribute Name | Attribute Type | Description | Example |
| --- | --- | --- | --- |
| snow.database.name | VARCHAR | The name of the database associated with the pipe. | “MY_DATABASE” |
| snow.schema.name | VARCHAR | The name of the schema associated with the pipe. | “MY_SCHEMA_NAME” |
| snow.pipe.name | VARCHAR | The name of the pipe. | “MY_PIPE_NAME” |
| notification_channel_name | VARCHAR | The name of the notification channel that received the message or encountered an error. | “arn:aws:sqs:us-west-2:774383465531:sf-snowpipe-AIDA3” |

## Key-value pairs in the record column

The `record` column contains an OBJECT value with the following key-value pairs:

| Key | Type | Description | Example |
| --- | --- | --- | --- |
| name | VARCHAR | The name of the event. | “pipe_lifecycle” |
| severity_text | VARCHAR | The severity level of the event. | “INFO” |
