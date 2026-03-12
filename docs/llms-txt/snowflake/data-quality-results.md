# Source: https://docs.snowflake.com/en/user-guide/data-quality-results.md

# View results of a data metric function

You can access the results of a scheduled data metric function (DMF) in the following ways:

* Query the dedicated event table.
* Query the [DATA_QUALITY_MONITORING_RESULTS](../sql-reference/local/data_quality_monitoring_results.md) view, which is a
  flattened version of the event table.
* Call the [DATA_QUALITY_MONITORING_RESULTS](../sql-reference/functions/data_quality_monitoring_results.md) table function.

Each method of viewing results has its own access control requirements. For example, an application role that grants access to the table
function might not let you query the event table. For a description of these access control requirements, see
[Viewing data quality results](data-quality-access-control.md).

> **Note:**
>
> This topic describes how you can use SQL to view the results of a DMF. To interact with a user interface to see the results of a data quality check, see [Monitoring data quality checks in Snowsight](data-quality-ui-monitor.md). A DMF is a building block of a data quality check.

## Query the dedicated event table

This option gives you access to the raw data, and you have more freedom to post-process the data using derived objects, such as creating
views, table functions, or stored procedures based on how you want to analyze the results. Additionally, if you create these
derived objects, you can selectively grant access on these objects to different roles. For example, a data engineer can access the stored
procedures to maintain the approach to obtain the results, and a data analyst can access the view to analyze the results.

The event table is named `SNOWFLAKE.LOCAL.DATA_QUALITY_MONITORING_RESULTS_RAW`.

For information about the event table columns, see [Event table columns](../developer-guide/logging-tracing/event-table-columns.md).

For a representative example to query the event table, see the
[logging and tracing tutorial](../developer-guide/logging-tracing/tutorials/logging-tracing-getting-started.md).

## Query the DATA_QUALITY_MONITORING_RESULTS view

This option enables you to query the [DATA_QUALITY_MONITORING_RESULTS](../sql-reference/local/data_quality_monitoring_results.md) view,
which flattens the raw data in the event table to enable easier access to the DMF results. Additionally, this option is best when data
post-processing is not needed and when you don’t want to grant access to the raw data.

The view exists in the LOCAL schema in the shared SNOWFLAKE database: `SNOWFLAKE.LOCAL.DATA_QUALITY_MONITORING_RESULTS`.

For information, see the [DATA_QUALITY_MONITORING_RESULTS](../sql-reference/local/data_quality_monitoring_results.md) view.

> **Note:**
>
> The SNOWFLAKE.GOVERNANCE_VIEWER database role does not have access to query the DATA_QUALITY_MONITORING_RESULTS view.

## Call the DATA_QUALITY_MONITORING_RESULTS table function

This option enables you to call the [DATA_QUALITY_MONITORING_RESULTS](../sql-reference/functions/data_quality_monitoring_results.md) table function to view the DMF
results. The function returns the same columns as the DATA_QUALITY_MONITORING_RESULTS view. However, you can only specify a single table
when calling the function. This option is best when you want to limit data metric function results to a single table and not provide
access to the measurements of other tables or the event table.
