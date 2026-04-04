# Source: https://docs.snowflake.com/en/sql-reference/account-usage/cortex_fine_tuning_usage_history.md

Schema:
:   [ACCOUNT_USAGE](../account-usage.md)

# CORTEX_FINE_TUNING_USAGE_HISTORY view

This Account Usage view can be used to query the training usage history of [Cortex Fine-tuning](../../user-guide/snowflake-cortex/cortex-finetuning.md).
This view includes the number of tokens processed and the training credits consumed by Cortex Fine-tuning jobs, aggregated by the job’s base model and the hour in which the job completed. This view only contains credits consumed for
fine-tuning training but not costs for using the fine-tuned model in inference, costs for storage, or costs associated with data replication. For
inference usage, see [CORTEX_FUNCTIONS_USAGE_HISTORY view](cortex_functions_usage_history.md). For more information, see
[Cost considerations](../../user-guide/snowflake-cortex/cortex-finetuning.md).

## Columns

| Column Name | Data Type | Description |
| --- | --- | --- |
| START_TIME | TIMESTAMP_LTZ | Start of the specified time range in which the Cortex Fine-tuning job terminated. |
| END_TIME | TIMESTAMP_LTZ | End of the specified time range in which the Cortex Fine-tuning job terminated. |
| MODEL_NAME | VARCHAR | Name of the base model. |
| TOKEN_CREDITS | NUMBER | Number of credits billed for Cortex Fine-tuning usage based on tokens processed by training jobs that terminated during the specified time range. |
| TOKENS | NUMBER | Number of tokens billed for Cortex Fine-tuning jobs terminated during the specified time range. |

## Usage notes

* The view provides up-to-date credit usage for an account within the last 365 days (1 year).
* In some cases where a model is used but is not billed, the model column may be empty.
