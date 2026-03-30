# Source: https://docs.snowflake.com/en/sql-reference/account-usage/cortex_aisql_usage_history.md

Schema:
:   [ACCOUNT_USAGE](../account-usage.md)

# CORTEX_AISQL_USAGE_HISTORY view

The CORTEX_AISQL_USAGE_HISTORY view can be used to query the usage history of [Cortex AI Functions](../../user-guide/snowflake-cortex/aisql.md).

The information in the view includes the number of credits consumed each time an AI function is called, aggregated in
one-hour increment, based on the time each query completed. The view also includes relevant metadata, such as the user
ID, query ID, function, and model. Each row in the view represents the usage for a specific combination of function, model, query, and
warehouse. For more information on Cortex billing, see [Cost considerations](../../user-guide/snowflake-cortex/aisql.md).

> **Important:**
>
> This view replaces both the [CORTEX_FUNCTIONS_USAGE_HISTORY](cortex_functions_usage_history.md) and
> [CORTEX_FUNCTIONS_QUERY_USAGE_HISTORY](cortex_functions_query_usage_history.md) views.

## Columns

| Column Name | Data Type | Description |
| --- | --- | --- |
| USAGE_TIME | TIMESTAMP_LTZ | The date and the beginning of the hour (in the local time zone) in which this usage record was billed. Usage is not recorded until the query completes, so this timestamp represents the hour in which the query completed. For example, if a query begins at 05:30 and completes at 08:30, the record is aggregated in the 08:00-09:00 hour. |
| MODEL_NAME | TEXT | Name of the model used in the query. A query can use more than one model; in this case, usage history includes a row for each model. |
| FUNCTION_NAME | TEXT | The name of the Cortex AI Function called. A query can use more than one function; in this case, usage history includes a row for each function. |
| TOKEN_CREDITS | NUMBER | Number of credits billed for Cortex AI Function usage based on tokens processed for the specified function and model for the combination of QUERY_ID, MODEL_NAME, and WAREHOUSE_ID. Does not include warehouse usage credits. |
| TOKENS | NUMBER | Number of tokens processed for the specified function and model for the combination of QUERY_ID, MODEL_NAME, and WAREHOUSE_ID. |
| TOKEN_CREDITS_GRANULAR | OBJECT | A SQL object that provides a breakdown of credits billed by token type (input or output) for the specified function and model for the combination of QUERY_ID, MODEL_NAME, and WAREHOUSE_ID. |
| TOKENS_GRANULAR | OBJECT | A SQL object that provides a breakdown of tokens processed by token type (input or output) for the specified function and model for the combination of QUERY_ID, MODEL_NAME, and WAREHOUSE_ID. |
| QUERY_ID | TEXT | The ID of the query in which the function was called. |
| QUERY_TAG | TEXT | The tag, if any, associated with the query in which the function was called. |
| USER_ID | TEXT | The internal ID of the user who invoked the function.  For more information about authenticating, see [Authenticating to the server](../../developer-guide/sql-api/authenticating.md). |
| WAREHOUSE_ID | TEXT | The ID of the virtual warehouse that processed the query in which the function was called. |

## Usage notes

* This view includes only usage that occurred on or after November 17, 2025.
* Billing is reported only after the query completes, and the timestamp is the hour in which the query completed.
* Credit usage is based on the number of tokes processed, as outlined in the [Snowflake Service Consumption Table](https://www.snowflake.com/legal-files/CreditConsumptionTable.pdf).
