# Source: https://docs.snowflake.com/en/developer-guide/logging-tracing/unhandled-exception-messages.md

# Capturing messages from unhandled exceptions

By default, when you’ve [set up an event table](event-table-setting-up.md), Snowflake automatically logs
unhandled exceptions in procedure and UDF handlers in the event table. Capturing these messages does not require that you add handler
code specific to logging or tracing. You can disable this feature so that unhandled exceptions aren’t automatically logged.

> **Important:**
>
> Error messages can contain sensitive information. Consider disabling this feature if you don’t want potentially sensitive
> information captured in an event table. To learn more, see Protecting sensitive data.

## Configuring logging and tracing to capture unhandled exceptions

Set log or trace level so that Snowflake captures entries for unhandled exceptions. You can have entries captured as log entries, trace
event entries, or both.

* To capture messages as log entries, [set the log level](telemetry-levels.md) to `ERROR` or
  more verbose.
* To capture messages as trace event entries, [set the trace level](telemetry-levels.md) to
  `ALWAYS` or `ON_EVENT`.

## Data captured for unhandled exceptions

You can capture message data as a log entry, a trace event, or both. The captured data will differ between log and trace event entries.

### Data captured in a log entry

By default, Snowflake records the following in the event table for unhandled exceptions in procedure and UDF handlers:

| Column | Data |
| --- | --- |
| [RECORD column](event-table-columns.md) | A `severity_text` attribute whose value is the highest-severity error level for the current language runtime. For example, for a handler written in Python, the value is `FATAL`. |
| [RECORD_ATTRIBUTES column](event-table-columns.md) | The following attributes are recorded for an unhandled exception.   *`exception.message` – The error message.* `exception.type` – The name of the exception’s class. *`exception.stacktrace` – The exception’s stack trace formatted by a language runtime.* `exception.escaped` – `true` if this entry is from an unhandled exception. |
| [VALUE column](event-table-columns.md) | The string `exception`. |

#### Example

Code in the following example queries an event table for log data recorded for an unhandled exception from a UDF handler.

For more about querying an event table for log data, see [Viewing log messages](logging-accessing-messages.md).

```sqlexample
SET event_table_name = 'my_db.public.my_event_table';

SELECT
  RECORD['severity_text'] AS severity,
  RECORD_ATTRIBUTES['exception.message'] AS error_message,
  RECORD_ATTRIBUTES['exception.type'] AS exception_type,
  RECORD_ATTRIBUTES['exception.stacktrace'] AS stacktrace
FROM
  my_event_table
WHERE
  RECORD_TYPE = 'LOG';
```

The following is possible output from the query.

```output
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
| SEVERITY | ERROR_MESSAGE                                        | EXCEPTION_TYPE | STACKTRACE                                                                                                                                          |
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
| "FATAL"  | "could not convert string to float: '$1,000,000.00'" | "ValueError"   | "Traceback (most recent call last):\n  File \"_udf_code.py\", line 6, in compute\nValueError: could not convert string to float: '$1,000,000.00'\n" |
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
```

### Data captured in a trace event entry

By default, Snowflake records the following in the event table for unhandled exceptions in procedure and UDF handlers:

| Column | Data |
| --- | --- |
| [RECORD column](event-table-columns.md) | A `name` attribute whose value is `exception` and a `status` attribute whose value is `STATUS_CODE_ERROR`. |
| [RECORD_ATTRIBUTES column](event-table-columns.md) | The following attributes are recorded for an unhandled exception.   *`exception.message` – The error message.* `exception.type` – The name of the exception’s class. *`exception.stacktrace` – The exception’s stack trace formatted by a language runtime.* `exception.escaped` – `true` if this entry is from an unhandled exception. |

#### Examples

Code in the following examples query an event table for trace event data recorded for an unhandled exception from a UDF handler.

For more about querying an event table for trace event data, see [Viewing trace data](tracing-accessing-events.md).

##### Span example

```sqlexample
SET event_table_name = 'my_db.public.my_event_table';

SELECT
  RECORD['status']['code'] AS span_status
FROM
  my_event_table
WHERE
  record_type = 'SPAN';
```

The following is possible output from the query.

```output
-----------------------
| SPAN_STATUS         |
-----------------------
| "STATUS_CODE_ERROR" |
-----------------------
```

##### Span event example

```sqlexample
SET event_table_name = 'my_db.public.my_event_table';

SELECT
  RECORD['name'] AS event_name,
  RECORD_ATTRIBUTES['exception.message'] AS error_message,
  RECORD_ATTRIBUTES['exception.type'] AS exception_type,
  RECORD_ATTRIBUTES['exception.stacktrace'] AS stacktrace
FROM
  my_event_table
WHERE
  RECORD_TYPE = 'SPAN_EVENT';
```

The following is possible output from the query.

```output
-----------------------------------------------------------------------------------------------------------------------------------------
| EVENT_NAME  | ERROR_MESSAGE                                        | EXCEPTION_TYPE | STACKTRACE                                      |
-----------------------------------------------------------------------------------------------------------------------------------------
| "exception" | "could not convert string to float: '$1,000,000.00'" | "ValueError"   | "  File \"_udf_code.py\", line 6, in compute\n" |
-----------------------------------------------------------------------------------------------------------------------------------------
```

## Protecting sensitive data

Given that log and trace messages from unhandled exceptions can include sensitive data, consider doing the following to protect that data:

* Take steps to protect sensitive data, such as by doing the following:

  * Improve your exception handling code to minimize the risk of unhandled exceptions.
  * Apply [row access policies](../../user-guide/security-row-intro.md) to your event table to restrict access to rows that contain
    personally identifiable information (PII).
  * [Create a view](../../sql-reference/sql/create-view.md) on top of the event table and
    [apply masking policies](../../sql-reference/sql/create-masking-policy.md) to it to mask or delete personally identifiable
    information (PII).
* Turn off unhandled exception logging by setting the [ENABLE_UNHANDLED_EXCEPTIONS_REPORTING](../../sql-reference/parameters.md) parameter to `false`.
