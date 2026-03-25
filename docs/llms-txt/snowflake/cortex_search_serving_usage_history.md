# Source: https://docs.snowflake.com/en/sql-reference/account-usage/cortex_search_serving_usage_history.md

Schema:
:   [ACCOUNT_USAGE](../account-usage.md)

# CORTEX_SEARCH_SERVING_USAGE_HISTORY view

This Account Usage view can be used to query the hourly serving usage history of [Cortex Search](../../user-guide/snowflake-cortex/cortex-search/cortex-search-overview.md).
The information in this view includes the number of serving credits consumed per hour for a Cortex Search Service. This view
only contains credits consumed for serving, not the other costs associated with a Cortex Search Service. For more information, see
[Cost considerations](../../user-guide/snowflake-cortex/cortex-search/cortex-search-overview.md).

## Columns

| Column Name | Data Type | Description |
| --- | --- | --- |
| START_TIME | TIMESTAMP_LTZ | Start of the specified time range in which the Cortex Search serving usage took place. |
| END_TIME | TIMESTAMP_LTZ | End of the specified time range in which the Cortex Search usage took place. |
| DATABASE_NAME | VARCHAR | Name of the database in which the Cortex Search Service resides. |
| SCHEMA_NAME | VARCHAR | Name of the schema in which the Cortex Search Service resides. |
| SERVICE_NAME | VARCHAR | Name of the Cortex Search Service. |
| SERVICE_ID | NUMBER | ID of the Cortex Search Service. |
| CREDITS | NUMBER | Number of credits billed for Cortex Search serving usage based on the size of indexed data during the START_TIME and END_TIME window. |

## Usage notes

* The view provides up-to-date credit usage for an account within the last 365 days (1 year).
* Serving credits are incurred per GB-mo of indexed data, metered at the second-level. One may get an estimate of
  the indexed data size for a given service using the credit rate defined in the [Snowflake Service Consumption Table](https://www.snowflake.com/legal-files/CreditConsumptionTable.pdf).
* This view may show small discrepancies in incurred cost from hour-to-hour based on the second-level metering.
