# Source: https://docs.snowflake.com/en/release-notes/2025/other/2025-08-04-hybrid-tables-time-travel-billing.md

# Aug 04, 2025: Hybrid table storage for Time Travel data

Consumption for hybrid table storage now takes into account the data that is retained by
[Time Travel](../../../user-guide/data-time-travel.md).
Data retained by Time Travel is included in the following storage metrics:

* STORAGE_BYTES column in the [STORAGE_USAGE view](../../../sql-reference/account-usage/storage_usage.md)
* AVERAGE_DATABASE_BYTES column in:

  * The Account Usage [DATABASE_STORAGE_USAGE_HISTORY view](../../../sql-reference/account-usage/database_storage_usage_history.md)
  * The Organization Usage [DATABASE_STORAGE_USAGE_HISTORY view](../../../sql-reference/organization-usage/database_storage_usage_history.md)
  * The Information Schema [DATABASE_STORAGE_USAGE_HISTORY](../../../sql-reference/functions/database_storage_usage_history.md) function

Time Travel data is stored in object storage, not the row store, and is charged at the standard table rate,
not the higher hybrid table rate.
