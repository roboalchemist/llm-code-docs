# Source: https://docs.snowflake.com/en/sql-reference/account-usage/cortex_functions_query_usage_history.md

Schema:
:   [ACCOUNT_USAGE](../account-usage.md)

# CORTEX_FUNCTIONS_QUERY_USAGE_HISTORY view

> **Important:**
>
> This view is no longer updated. Use the [CORTEX_AISQL_USAGE_HISTORY](cortex_aisql_usage_history.md) view instead.

The CORTEX_FUNCTIONS_QUERY_USAGE_HISTORY view can be used to view the usage history of each [Cortex Functions](../../user-guide/snowflake-cortex/aisql.md) query in a Snowflake account. For more information, see [Cost considerations](../../user-guide/snowflake-cortex/aisql.md).

The information in the view includes the number of tokens and credits consumed for each query.

The view also includes relevant metadata, such as the model name and the ID of the warehouse running the queries.

## Columns

| Column Name | Data Type | Description |
| --- | --- | --- |
| FUNCTION_NAME | VARCHAR | Function name for the model. |
| MODEL_NAME | VARCHAR | Model name used in the query. A query can have more than one model. For queries with multiple models, the usage history includes a row for each model. |
| QUERY_ID | VARCHAR | Query ID |
| TOKENS | NUMBER | Number of tokens used for the (`QUERY_ID`, `MODEL_NAME`, `WAREHOUSE_ID`) combination. |
| TOKEN_CREDITS | NUMBER | Tokens converted to credits for the (`QUERY_ID`, `MODEL_NAME`, `WAREHOUSE_ID`) combination. |
| WAREHOUSE_ID | VARCHAR | ID of the warehouse used to run the query. |

## Usage notes

* The view provides up-to-date credit usage for an account within the last 365 days (1 year).
* Query usage data might take a few hours to appear in the CORTEX_FUNCTIONS_QUERY_USAGE_HISTORY view.
* Credit rate usage is based on the number of messages processed, as outlined in the [Snowflake Service Consumption Table](https://www.snowflake.com/legal-files/CreditConsumptionTable.pdf).
