# Source: https://docs.snowflake.com/en/sql-reference/account-usage/cortex_search_daily_usage_history.md

Schema:
:   [ACCOUNT_USAGE](../account-usage.md)

# CORTEX_SEARCH_DAILY_USAGE_HISTORY view

This Account Usage view can be used to query the daily usage history of [Cortex Search](../../user-guide/snowflake-cortex/cortex-search/cortex-search-overview.md),
with consumption broken out by category. The information in this view includes the number of credits consumed per day for a Cortex Search Service
for both serving and for embedding text, but not the other costs associated with a Cortex Search Service.
For more information, see [Cost considerations](../../user-guide/snowflake-cortex/cortex-search/cortex-search-overview.md).

## Columns

| Column Name | Data Type | Description |
| --- | --- | --- |
| USAGE_DATE | TIMESTAMP_LTZ | Start of the specified time range in which the Cortex Search serving usage took place. |
| DATABASE_NAME | VARCHAR | Name of the database in which the Cortex Search Service resides. |
| SCHEMA_NAME | VARCHAR | Name of the schema in which the Cortex Search Service resides. |
| SERVICE_NAME | VARCHAR | Name of the Cortex Search Service. |
| SERVICE_ID | NUMBER | ID of the Cortex Search Service. |
| CONSUMPTION_TYPE | VARCHAR | The category of consumption incurred. One of “SERVING”, “EMBED_TEXT_TOKENS”. |
| CREDITS | NUMBER | Number of credits billed for Cortex Search usage on the USAGE_DATE date for the specified CONSUMPTION_TYPE. |
| MODEL_NAME | VARCHAR | For CONSUMPTION_TYPE = “EMBED_TEXT_TOKENS”, the name of the embedding model used to generate vector embeddings (nullable). |
| TOKENS | VARCHAR | For CONSUMPTION_TYPE = “EMBED_TEXT_TOKENS”, the number of input tokens consumed (nullable). |

## Usage notes

* The view provides up-to-date credit usage for an account within the last 365 days (1 year).
* Serving costs are incurred per gigabyte-month of indexed data, metered at one-second resolution. You can get an estimate of
  the indexed data size for a given service using the credit rate defined in the [Snowflake Service Consumption Table](https://www.snowflake.com/legal-files/CreditConsumptionTable.pdf).
* EMBED_TEXT_TOKENS cost is incurred per input token.
