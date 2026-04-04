# Source: https://docs.snowflake.com/en/sql-reference/account-usage/cortex_rest_api_usage_history.md

Schema:
:   [ACCOUNT_USAGE](../account-usage.md)

# CORTEX_REST_API_USAGE_HISTORY view

Query the CORTEX_REST_API_USAGE_HISTORY view to see the history of Cortex REST API calls.

The information in the view includes the number of tokens processed and credits consumed for each REST API request. The view also includes
relevant metadata, such as the request ID, model name, user ID, and inference region. For more information on Cortex billing, see
[Cost considerations](../../user-guide/snowflake-cortex/aisql.md).

## Columns

| Column Name | Data Type | Description |
| --- | --- | --- |
| START_TIME | TIMESTAMP_LTZ | The beginning of the time range for the usage history. |
| END_TIME | TIMESTAMP_LTZ | The end of the time range for the usage history. |
| REQUEST_ID | TEXT | The unique identifier for the REST API request. |
| MODEL_NAME | TEXT | Name of the model used in the REST API call. |
| TOKENS | NUMBER | Number of tokens processed for the REST API request. |
| TOKENS_GRANULAR | OBJECT | A SQL object that provides a breakdown of tokens processed by token type (input or output) for the REST API request. |
| USER_ID | TEXT | The internal ID of the user who invoked the REST API.  For more information about authenticating, see [Authenticating to the server](../../developer-guide/sql-api/authenticating.md). |
| INFERENCE_REGION | TEXT | The region in which the inference was performed. |

## Usage notes

* The view provides up-to-date usage information for an account within the last 365 days (1 year).
* Credit usage is based on the number of tokens processed, as outlined in the [Snowflake Service Consumption Table](https://www.snowflake.com/legal-files/CreditConsumptionTable.pdf).
