# Source: https://docs.snowflake.com/en/user-guide/cost-insights.md

# Using cost insights to save

Snowflake provides cost insights that identify opportunities to optimize Snowflake for cost within a particular account. These insights are
calculated and refreshed weekly.

Each insight indicates how many credits or terabytes could be saved by optimizing Snowflake.

To access the Cost Insights tile:

1. Sign in to [Snowsight](ui-snowsight-gs.md).
2. Switch to a role with [access to cost-related features](cost-access-control.md).
3. In the navigation menu, select Admin » Cost management.
4. Select the Account Overview tab.
5. Find the Cost insights tile.

Each of the following insights includes suggestions on how to optimize your spend.

* Insight: Rarely used tables with automatic clustering
* Insight: Rarely used materialized views
* Insight: Rarely used search optimization paths
* Insight: Large tables that are never queried
* Insight: Tables over 100 GB from which data is written but not read
* Insight: Short-lived permanent tables
* Insight: Inefficient usage of multi-cluster warehouses

Insight: Rarely used tables with automatic clustering
:   This insight identifies tables with [automatic clustering](tables-auto-reclustering.md) that are queried fewer than 100
    times per week by this account.

    Enabling automatic clustering for a table can significantly improve the performance of queries against that table. However, as the table
    changes, Snowflake must use serverless compute resources to keep it in a well-clustered state. If the number of queries executed against
    the table is minimal, the cost incurred might not justify the performance improvements.

    **Recommendation:**
    Consider disabling automatic clustering on these tables. Before you turn off automatic clustering, determine whether the table exists
    solely for disaster recovery purposes or for use by other Snowflake accounts through data sharing, which might explain why it isn’t
    accessed frequently.

    For example, to disable automatic clustering for a table named `t1`, execute the following command:

    ```sqlexample
    ALTER TABLE t1 SUSPEND RECLUSTER;
    ```

Insight: Rarely used materialized views
:   This insight identifies [materialized views](views-materialized.md) that are queried fewer than 10 times per week by this
    account.

    Creating a materialized view can significantly improve performance for certain query patterns. However, materialized views incur
    additional storage costs as well as serverless compute costs associated with keeping the materialized view up to date with new data. If
    the number of queries executed against the materialized view is minimal, the cost incurred might not justify the performance improvements.

    **Recommendation:**
    Consider removing or suspending updates to the materialized views. Before you drop a materialized view, determine whether the table exists
    solely for disaster recovery purposes or for use by other Snowflake accounts through data sharing, which might explain why it isn’t
    accessed frequently.

    For example, to delete a materialized view named `mv1`, execute the following command:

    ```sqlexample
    DROP MATERIALIZED VIEW mv1;
    ```

Insight: Rarely used search optimization paths
:   This insight identifies [search optimization](search-optimization-service.md) access paths that are used fewer than
    10 times per week by this account.

    Search optimization uses search access paths to improve the performance of certain types of point lookup and analytical queries. Adding
    search optimization to a table can significantly improve performance for these queries. However, search optimization incurs additional
    storage costs as well as serverless compute costs associated with keeping that storage up to date. If the number of queries that use the
    search access path created by search optimization is minimal, the cost incurred might not justify the performance improvements.

    **Recommendation:**
    Consider removing search optimization from the table. Before you remove search optimization, determine whether the table exists solely
    for disaster recovery purposes or for use by other Snowflake accounts through data sharing, which might explain why it isn’t accessed
    frequently.

    For example, to completely remove search optimization from a table named `t1`, execute the following command:

    ```sqlexample
    ALTER TABLE t1 DROP SEARCH OPTIMIZATION;
    ```

Insight: Large tables that are never queried
:   This insight identifies large tables that have not been queried in the last week by this account.

    **Recommendation:**
    Consider deleting unused tables, which can reduce storage costs without impacting any workloads. Before you drop the tables, determine
    whether the table exists solely for disaster recovery purposes or for use by other Snowflake accounts through data sharing, which might
    explain why it isn’t accessed frequently.

    For example, to delete a table name `t1`, execute the following command:

    ```sqlexample
    DROP TABLE t1;
    ```

Insight: Tables over 100 GB from which data is written but not read
:   This insight identifies tables where data is written but never read by this account.

    **Recommendation:**
    It might be wasteful to store data and ingest new data into Snowflake if the data is never read. Consider dropping these tables to save on
    storage costs or stop writing new data to save on credits consumed by ingestion. Before you drop the tables, determine whether the table
    exists solely for disaster recovery purposes or for use by other Snowflake accounts through data sharing, which might explain why it
    isn’t being read.

    For example, to drop a table name `t1`, execute the following command:

    ```sqlexample
    DROP TABLE t1;
    ```

Insight: Short-lived permanent tables
:   This insight identifies tables over 100 GB that were deleted within 24 hours of their creation.

    **Recommendation:** If data needs to be persisted for only a short time, consider using a
    [temporary table or transient table](tables-temp-transient.md) for future tables. Using a temporary table or transient
    table might help you save on [Fail-safe and Time Travel costs](data-cdp-storage-costs.md).

    For example, to create a new transient table `t1`, execute the following command:

    ```sqlexample
    CREATE TRANSIENT TABLE t1;
    ```

Insight: Inefficient usage of multi-cluster warehouses
:   This insight identifies when you have the minimum and maximum cluster count set to the same value for a multi-cluster warehouse, which
    prevents the warehouse from scaling up or down to respond to demand. If your multi-cluster warehouse can scale down during periods of
    lighter usage, it can save credits.

    **Recommendation:** Consider lowering the minimum cluster count to allow the multi-cluster warehouse to scale down during periods of
    lighter usage.

    For example, to set the minimum cluster count to 1 for a warehouse named `wh1`, execute the following command:

    ```sqlexample
    ALTER WAREHOUSE wh1 SET MIN_CLUSTER_COUNT = 1;
    ```
