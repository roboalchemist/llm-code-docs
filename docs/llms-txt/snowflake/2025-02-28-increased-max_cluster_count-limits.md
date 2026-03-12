# Source: https://docs.snowflake.com/en/release-notes/2025/other/2025-02-28-increased-max_cluster_count-limits.md

# Feb 28, 2025: Increased max_cluster_count limits for multi-cluster warehouses

You now have more flexibility when specifying upper limits for the MAX_CLUSTER_COUNT property
in [Multi-cluster warehouses](../../../user-guide/warehouses-multicluster.md).

The upper limit for MAX_CLUSTER_COUNT is no longer restricted to 10. Instead, the upper limit
varies depending on the warehouse size.
Currently, you must use a SQL command, not Snowsight, to specify an upper limit higher than 10.

The scaling policies for multi-cluster warehouses now can increase or decrease the capacity
of a warehouse by more than one cluster at a time.

For more information, see [Upper limit on number of clusters for a multi-cluster warehouse](../../../user-guide/warehouses-multicluster.md).
