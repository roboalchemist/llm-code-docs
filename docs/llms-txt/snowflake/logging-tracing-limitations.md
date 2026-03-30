# Source: https://docs.snowflake.com/en/developer-guide/logging-tracing/logging-tracing-limitations.md

# Logging and tracing limitations

## General limitations

There is a 1MB limit for log and trace event payloads. If the payload is over the 1MB threshold, the record in the event table will be
incomplete and only contain values for the following columns: TIMESTAMP, RECORD_TYPE, and RESOURCE_ATTRIBUTES. Currently there is no
additional indication that the threshold was exceeded.

## Event tables associated with databases

* When you use [event tables associated with databases](event-table-setting-up.md), the Snowsight trace explorer
  currently won’t show the entire span for traces with spans across multiple event tables. Instead, you can see the partial trace with
  the spans in the currently selected event table from the drop-down.
* Snowflake does not support collecting events for Snowpark Container Services when the event table is associated with a database.
