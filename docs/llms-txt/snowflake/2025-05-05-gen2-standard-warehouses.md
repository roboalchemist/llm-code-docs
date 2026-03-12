# Source: https://docs.snowflake.com/en/release-notes/2025/other/2025-05-05-gen2-standard-warehouses.md

# May 05, 2025: Generation 2 standard warehouses (*General availability*)

With this release, you can take advantage of the Generation 2 Standard Warehouse (Gen2) feature.

This feature is an updated version (the “next generation”) of the
current standard virtual warehouse in Snowflake, focused on improving performance for
analytics and data engineering workloads. Gen2 is built on top of faster underlying hardware
and intelligent software optimizations, such as enhancements to delete, update, and merge operations,
and table scan operations. With Gen2, you can expect the majority of queries finish faster, and you can
do more work at the same time. The exact details depend on your configuration and workload.
Conduct tests to verify how much this feature improves your costs, performance, or both.

To create and manage generation 2 standard warehouses, you can use the SQL commands
[CREATE WAREHOUSE](../../../sql-reference/sql/create-warehouse.md) and
[ALTER WAREHOUSE](../../../sql-reference/sql/alter-warehouse.md).

For more information, see [Snowflake generation 2 standard warehouses](../../../user-guide/warehouses-gen2.md).
For the regions and cloud service providers where this feature is currently available,
see [region availability for generation 2 standard warehouses](../../../user-guide/warehouses-gen2.md).
