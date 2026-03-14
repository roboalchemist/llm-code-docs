# Source: https://docs.snowflake.com/en/release-notes/2025/other/2025-12-08-dynamic-tables-dual-warehouses.md

# Dec 08, 2025: Dynamic tables: Support for dual warehouses

Dynamic tables support dual warehouses to optimize performance and cost for different types of refresh operations. You can specify a dedicated
warehouse for [initializations and reinitializations](../../../user-guide/dynamic-tables-refresh.md), which are typically more resource-intensive,
while you use another warehouse for all other refreshes.

For more information, see [Understand warehouse usage for dynamic tables](../../../user-guide/dynamic-tables-warehouses.md).
