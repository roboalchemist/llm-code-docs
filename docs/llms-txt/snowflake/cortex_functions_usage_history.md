# Source: https://docs.snowflake.com/en/sql-reference/account-usage/cortex_functions_usage_history.md

Schema:
:   [ACCOUNT_USAGE](../account-usage.md)

# CORTEX_FUNCTIONS_USAGE_HISTORY view

> **Important:**
>
> This view is no longer updated. Use the [CORTEX_AISQL_USAGE_HISTORY](cortex_aisql_usage_history.md) view instead.

This Account Usage view can be used to query the usage history of [Cortex Functions](../../user-guide/snowflake-cortex/aisql.md) such
as COMPLETE and TRANSLATE. The information in the view includes the number of tokens and credits consumed each time a Cortex Function is
called, aggregated in one hour increments based on function and model. The view also includes relevant metadata, such as the warehouse ID,
start and end times of the function execution, and the name of the function and the model, if specified.

> **Note:**
>
> The view might not include usage information on functions called with recently added models. A new model can take up to 2 weeks to
> be included in this view.

## Columns

| Column Name | Data Type | Description |
| --- | --- | --- |
| START_TIME | TIMESTAMP_LTZ | Start of the specified time range in which the Cortex LLM function usage took place. |
| END_TIME | TIMESTAMP_LTZ | End of the specified time range in which the Cortex LLM function usage took place. |
| FUNCTION_NAME | VARCHAR | Name of the Cortex LLM function. |
| MODEL_NAME | VARCHAR | Model name. Empty for Cortex LLM functions where a model is not specified as an argument. |
| WAREHOUSE_ID | NUMBER | System-generated identifier for the warehouse used by the query calling the Cortex LLM function. |
| TOKENS | NUMBER | Number of tokens billed. |
| TOKEN_CREDITS | NUMBER | Number of credits billed for Cortex LLM functions usage based on tokens processed for the specified function and model (if applicable) during the START_TIME and END_TIME window. |

## Usage notes

* The view provides up-to-date credit usage for an account within the last 365 days (1 year).
* The credit rate usage is determined based on the function called, model used and the tokens processed as outlined in the
  [Snowflake Service Consumption Table](https://www.snowflake.com/legal-files/CreditConsumptionTable.pdf).
* In some cases where a model is used but is not billed, the model column may be empty.
