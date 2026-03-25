# Source: https://docs.snowflake.com/en/release-notes/2024/other/2024-06-25-to-query-function.md

# June 25, 2024 — New TO_QUERY table function

The [TO_QUERY](../../../sql-reference/functions/to_query.md) table function returns a result set based on SQL text and an optional
set of arguments that are passed to the SQL text if it is parameterized. The function compiles the SQL text as the
definition of a subquery in the FROM clause. When writing an application or a stored procedure, you can call this
function to construct a SQL statement.
