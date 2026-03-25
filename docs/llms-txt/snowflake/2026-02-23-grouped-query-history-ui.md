# Source: https://docs.snowflake.com/en/release-notes/2026/other/2026-02-23-grouped-query-history-ui.md

# Feb 23, 2026: Grouped Query History in Snowsight (*General availability*)

You can use the Grouped Query History view in Snowsight to monitor usage
and performance of critical and frequently run queries. This graphical view is based on information
that is recorded in the [AGGREGATE_QUERY_HISTORY view](../../../sql-reference/account-usage/aggregate_query_history.md).

The Grouped Query History view is particularly useful for monitoring and analyzing
[Unistore workloads](https://www.snowflake.com/en/data-cloud/workloads/unistore/)
that execute a small number of distinct statements repeatedly at high throughput.

For more information, see [Use the Grouped Query History view in Snowsight](../../../user-guide/ui-snowsight-activity.md).
