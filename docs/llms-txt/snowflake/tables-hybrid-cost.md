# Source: https://docs.snowflake.com/en/user-guide/tables-hybrid-cost.md

# Evaluate cost for hybrid tables

When you use hybrid tables, your account is charged based on two modes of consumption:

* **Hybrid table storage**: Cost for storage of hybrid tables depends on the
  amount of data that you are storing. Storage cost is based on a flat monthly rate per gigabyte (GB).
  See Table 3(b) in the [Snowflake Service Consumption Table](https://www.snowflake.com/legal-files/CreditConsumptionTable.pdf), which covers unit pricing for hybrid
  table storage.

  Note that hybrid table storage *for the row-store copy of the data* is more expensive than traditional
  Snowflake storage. The copy of the current data in the column store (object storage) is not billed.

  Historical time travel data is billed at standard storage prices.
* **Virtual warehouse compute**: Queries against hybrid tables are executed
  through virtual warehouses. The consumption rate of a warehouse is the same
  for querying hybrid tables as it is for standard tables.
  See [Virtual warehouse credit usage](cost-understanding-compute.md).

## Monitoring storage consumption for hybrid tables

You can view storage usage for hybrid tables and monitor consumption of hybrid table storage credits by querying the following views and functions:

* [STORAGE_USAGE view](../sql-reference/account-usage/storage_usage.md) (STORAGE_BYTES and HYBRID_TABLE_STORAGE_BYTES columns).
* DATABASE_STORAGE_USAGE_HISTORY (AVERAGE_HYBRID_TABLE_STORAGE_BYTES and AVERAGE_DATABASE_BYTES columns):

  * Account Usage [DATABASE_STORAGE_USAGE_HISTORY view](../sql-reference/account-usage/database_storage_usage_history.md)
  * Organization Usage [DATABASE_STORAGE_USAGE_HISTORY view](../sql-reference/organization-usage/database_storage_usage_history.md)
  * Information Schema [DATABASE_STORAGE_USAGE_HISTORY](../sql-reference/functions/database_storage_usage_history.md) function
* [HYBRID_TABLES view](../sql-reference/account-usage/hybrid_tables.md) (data per specific hybrid table in the BYTES column).
* [AGGREGATE_QUERY_HISTORY view](../sql-reference/account-usage/aggregate_query_history.md): Monitor virtual warehouse compute resources used during specific queries that are
  executed against hybrid tables. See [Monitor workloads](tables-hybrid-monitor-workload.md).

## Hybrid table storage for Time Travel data

Consumption for hybrid table storage takes into account the data that is retained by [Time Travel](data-time-travel.md).
Data retained by Time Travel is included in the following storage metrics:

* STORAGE_BYTES column in the [STORAGE_USAGE view](../sql-reference/account-usage/storage_usage.md)
* AVERAGE_DATABASE_BYTES column in DATABASE_STORAGE_USAGE_HISTORY:

  * Account Usage [DATABASE_STORAGE_USAGE_HISTORY view](../sql-reference/account-usage/database_storage_usage_history.md)
  * Organization Usage [DATABASE_STORAGE_USAGE_HISTORY view](../sql-reference/organization-usage/database_storage_usage_history.md)
  * Information Schema [DATABASE_STORAGE_USAGE_HISTORY](../sql-reference/functions/database_storage_usage_history.md) function

Data retained by Time Travel is stored in object storage, not the row store, and is charged at the standard table rate,
not the higher hybrid table rate.
