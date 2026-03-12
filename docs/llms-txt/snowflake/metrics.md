# Source: https://docs.snowflake.com/en/developer-guide/snowflake-cli/command-reference/spcs-commands/service-commands/metrics.md

# Source: https://docs.snowflake.com/en/developer-guide/logging-tracing/metrics.md

# Collecting metrics data

You can better understand stored procedure and UDF resource consumption by using CPU and memory metrics that Snowflake generates.
With this information, you can troubleshoot errors and performance issues. The metrics data is stored in your account event table.

After you’ve collected data in the event table, you can access the data for analysis via SQL or in Snowsight. For more information,
see [Viewing metrics data](metrics-viewing-data.md).

> **Note:**
>
> Before you can collect metrics data, you must [enable telemetry data collection](logging-tracing-enabling.md).
> You don’t need to add code to emit metrics data. Snowflake generates the data and collects it in an event table.

## Level for metrics data

You can specify whether to collect metrics data in the event table by setting the metric level. Be sure to set the level so that data
will be collected.

For more information, see [Setting levels for logging, metrics, and tracing](telemetry-levels.md).

When you’ve collected data, you can [view metric data](tracing-accessing-events.md)
by using a graphical tool or by querying the event table with SQL.

## Supported languages

You can collect metrics from code written in the following languages, including when handler code is written with
[Snowpark APIs](../snowpark/index.md).

| Language / Type | Java | Python | JavaScript | Scala | Snowflake Scripting |
| --- | --- | --- | --- | --- | --- |
| Stored procedure handler | ✔ | ✔ |  |  |  |
| Streamlit app | ✔ | ✔ |  |  |  |
| UDF handler (scalar function) | ✔ | ✔ |  |  |  |
| UDTF handler (table function) | ✔ | ✔ |  |  |  |

### Metrics data from handler code

Snowflake automatically captures metrics data when your code is executed. You don’t need to make any changes to your handler code.

For more information, see [Emitting metrics data from handler code](metrics-handler.md)

## Viewing metrics data

You can view collected metrics data either through Snowsight or by querying the event table where data is stored. For more
information, see [Viewing metrics data](metrics-viewing-data.md).
