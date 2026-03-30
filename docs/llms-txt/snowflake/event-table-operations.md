# Source: https://docs.snowflake.com/en/developer-guide/logging-tracing/event-table-operations.md

# Working with event tables

You can perform a subset of table operations on an event table you create, which is specifically designed for capturing events. The
sections in this topic describe the operations an event table supports.

> **Note:**
>
> You can perform only a subset of the operations listed here on the default event table, as noted in this topic.

## Operations supported on an event table

An event table is designed specifically for capturing events. You cannot perform some of the operations on an event table that you can
perform on a regular table.

With an event table, you can perform the following operations (note exceptions for the default event table):

| Operation | Default event table support | User-created event table support |
| --- | --- | --- |
| [SHOW EVENT TABLES](../../sql-reference/sql/show-event-tables.md) | ✔ | ✔ |
| [DESCRIBE EVENT TABLE](../../sql-reference/sql/desc-event-table.md) | ✔ | ✔ |
| [SELECT](../../sql-reference/sql/select.md) | ✔ | ✔ |
| [DROP TABLE](../../sql-reference/sql/drop-table.md) |  | ✔ |
| [UNDROP TABLE](../../sql-reference/sql/undrop-table.md) |  | ✔ |
| [CREATE TABLE](../../sql-reference/sql/create-table.md) |  | ✔ |
| [TRUNCATE TABLE](../../sql-reference/sql/truncate-table.md) | ✔ | ✔ |
| [DELETE](../../sql-reference/sql/delete.md) | ✔ | ✔ |
| [ALTER TABLE (event tables)](../../sql-reference/sql/alter-table-event-table.md) | ✔ (rename is not supported) | ✔ (rename is not supported) |

## Deleting rows from an event table

If you need to delete rows from an event table, you can use the following commands:

* Use [TRUNCATE TABLE](../../sql-reference/sql/truncate-table.md) to remove all rows from the event table.
* Use [DELETE](../../sql-reference/sql/delete.md) to remove selected rows from the event table.

  You can use this if you need to implement more complex log retention policies (e.g. if you need to retain logs for some functions for a
  longer period of time than other functions).

## Parameters for event tables

You can use the following parameters to specify how the event table should be used by handler code.

EVENT_TABLE
:   Specifies the name of the event table for logging messages from stored procedures and UDFs in this account. For reference information,
    see [EVENT_TABLE](../../sql-reference/parameters.md).

LOG_LEVEL
:   Specifies the severity level of messages that should be ingested and made available in the active event table. Messages at the specified
    level (and at more severe levels) are ingested. For more information, see [LOG_LEVEL](../../sql-reference/parameters.md) and
    [Setting levels for logging, metrics, and tracing](telemetry-levels.md).

METRIC_LEVEL
:   Specifies whether metrics data should be ingested and made available in the active event table. For more information, see
    [METRIC_LEVEL](../../sql-reference/parameters.md) and [Setting levels for logging, metrics, and tracing](telemetry-levels.md).

TRACE_LEVEL
:   Specifies the verbosity of trace events that should be ingested and made available in the active event table. Events at the specified
    level are ingested. For more information, see [TRACE_LEVEL](../../sql-reference/parameters.md) and
    [Setting levels for logging, metrics, and tracing](telemetry-levels.md).

## Access control privileges for event tables

You can use privileges in the global and event table scope to manage access to operations on an event table.

For more information, see [Event table privileges](../../user-guide/security-access-control-privileges.md) and log level privileges in [Global privileges (account privileges)](../../user-guide/security-access-control-privileges.md).

## Managing access to event table data

When it’s impractical for you to make event table data available to a range of users and roles, you can create views
for access by users with specific roles.

When you want to manage access to the data in this table, you can create views on the event table, then grant access for each view to
separate roles. Through the view, a role might have access to specified subset of the data in the event table.

For more information about creating views, see [CREATE VIEW](../../sql-reference/sql/create-view.md).

## Using streams to track changes to event tables

You can create a stream on an event table, such as to capture changes to the table.

For more information about streams, see [Introduction to streams](../../user-guide/streams-intro.md) and [CREATE STREAM](../../sql-reference/sql/create-stream.md).

Code in the following example creates a stream to capture inserts on the event table `my_event_table`.

```sqlexample
CREATE STREAM append_only_comparison ON EVENT TABLE my_event_table APPEND_ONLY=TRUE;
```
