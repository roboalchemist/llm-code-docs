# Source: https://docs.snowflake.com/en/sql-reference/account-usage/cortex_ai_functions_usage_history.md

Schema:
:   [ACCOUNT_USAGE](../account-usage.md)

# CORTEX_AI_FUNCTIONS_USAGE_HISTORY view

This Account Usage view can be used to query the usage history of [Cortex AI Functions](../../user-guide/snowflake-cortex/aisql.md).

The view includes the number of tokens and credits consumed each time a Cortex Function is called, aggregated in one
hour windows. The view also includes relevant metadata, such as the warehouse ID, start and end times of the function
execution, and the name of the function and the model, if specified. Each row represents the usage for a single function
call.

## Columns

| Column Name | Data Type | Description |
| --- | --- | --- |
| START_TIME | TIMESTAMP_LTZ | Start of the usage aggregation window. The window resolution is 1 hour. For example, if a query began at 05:30 and completed at 08:30, four records appear in the usage view, one each for the 5:00, 6:00, 7:00, and 8:00 aggregation windows. |
| END_TIME | TIMESTAMP_LTZ | End of the usage aggregation window. |
| FUNCTION_NAME | VARCHAR | Name of the Cortex AI Function called. Usage history contains a row for each function called in a query. |
| MODEL_NAME | VARCHAR | Model name. Empty for Cortex AI Functions where a model is not specified as an argument. Usage history contains a row for each model used in a query. |
| QUERY_ID | VARCHAR | The ID of the query in which the function was called. |
| WAREHOUSE_ID | NUMBER | System-generated identifier for the warehouse used by the query calling the Cortex AI Function. |
| ROLE_NAMES | ARRAY | Roles associated with the query. The primary role is the first element of the array. |
| QUERY_TAG | VARCHAR | The tag, if any, associated with the query in which the function was called. |
| USER_ID | VARCHAR | System-generated identifier for the user that executed the query calling the Cortex AI Function. |
| METRICS | ARRAY | A breakdown of usage metrics for the specified function and model for the combination of QUERY_ID, MODEL_NAME, and WAREHOUSE_ID. See Metrics column below for more details. |
| CREDITS | NUMBER | Number of credits billed for Cortex AI Function usage based on metrics for the specified function and model for the combination of QUERY_ID, MODEL_NAME, and WAREHOUSE_ID. Does not include warehouse usage credits. |
| IS_COMPLETED | BOOLEAN | Whether the query was completed in this aggregation window. |

## Metrics column

The metrics column contains a breakdown of usage metrics for the specified function and model for the combination of
QUERY_ID, MODEL_NAME, and WAREHOUSE_ID. Each element contains a `key` object (with `metric` type and `unit`
fields) and a `value`. The structure varies by metering method, as follows:

* **Token-based metering** (most AI Functions): Bills by token count, either as separate input and output token counts or as total token count, depending on the function.

  Example: `` [{"key":{"metric":"input","unit":"tokens"},"value":17},{"key":{"metric":"output","unit":"tokens"},"value":65}]`<br>`[{"key":{"metric":"total","unit":"tokens"},"value":527}] ``
* **Page-based metering** (AI_PARSE_DOCUMENT): Bills by page.

  Example: `[{"key":{"metric":"total","unit":"pages"},"value":3}]`

## Usage notes

* This view includes only usage that occurred on or after January 5, 2026.
* User ID attribution, Query tag, and Roles fields are available for data acquired after February 16, 2026.
* The view provides up-to-date credit usage for an account within the last 365 days (1 year).
* The view tracks both function calls that have completed and calls that are still in progress.
* Running queries are updated every 30 minutes (best effort) with a SLA of one hour.
* The credit rate usage is determined based on the function called, model used and the tokens processed as outlined in the
  [Snowflake Service Consumption Table](https://www.snowflake.com/legal-files/CreditConsumptionTable.pdf).
