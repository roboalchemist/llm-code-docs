# Source: https://docs.snowflake.com/en/release-notes/bcr-bundles/un-bundled/bcr-warehouse-events-history-cluster-number.md

# WAREHOUSE_EVENTS_HISTORY view: Change to the CLUSTER_NUMBER column output

The output of the [WAREHOUSE_EVENTS_HISTORY](../../../sql-reference/account-usage/warehouse_events_history.md) view behaves as follows:

Before the change:
:   The default value of the CLUSTER_NUMBER column is `0`.

After the change:
:   The default value of the CLUSTER_NUMBER column is `1`.

Ref: n/a
