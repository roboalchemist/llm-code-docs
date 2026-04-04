# Source: https://docs.snowflake.com/en/release-notes/2025/other/2025-04-15-search-optimization-scalar-functions.md

# Apr 15, 2025: Search optimization improves the performance of queries containing scalar functions

The search optimization service can now improve the performance of queries containing scalar functions.
A scalar function returns a single value for each invocation. The search optimization service can improve the
performance of queries that use scalar functions in equality predicates. The scalar function can be a
[system-defined scalar function](../../../sql-reference/functions.md) or a
[user-defined scalar SQL function](../../../developer-guide/udf/sql/udf-sql-introduction.md).

For more information, see [Speeding up queries with scalar functions using search optimization](../../../user-guide/search-optimization/scalar-functions.md).
