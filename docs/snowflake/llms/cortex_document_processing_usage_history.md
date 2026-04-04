# Source: https://docs.snowflake.com/en/sql-reference/account-usage/cortex_document_processing_usage_history.md

Schema:
:   [ACCOUNT_USAGE](../account-usage.md)

# CORTEX_DOCUMENT_PROCESSING_USAGE_HISTORY view

This Account Usage view displays Document AI processing function activity, including [<model_build_name>!PREDICT](../classes/document-intelligence/methods/predict.md),
[PARSE_DOCUMENT (SNOWFLAKE.CORTEX)](../functions/parse_document-snowflake-cortex.md), and [AI_EXTRACT](../functions/ai_extract.md) calls. It shows pages processed and credits
used, aggregated hourly by function and model. The view includes metadata such as the following:

* Warehouse ID
* Execution timestamps
* Function names
* Model names

## Columns

| Column Name | Data Type | Description |
| --- | --- | --- |
| QUERY_ID | VARCHAR | A unique identifier for the SQL query |
| CREDITS_USED | NUMBER(38,9) | The number of credits billed for Cortex Document processing functions for the specified query |
| START_TIME | TIMESTAMP_LTZ | Start of the hourly time range in which the query usage took place. |
| END_TIME | TIMESTAMP_LTZ | End of the hourly time range in which the query usage took place. |
| FUNCTION_NAME | TEXT | The name of the Cortex Document processing function |
| MODEL_NAME | TEXT | The name of the model |
| OPERATION_NAME | TEXT | The name of the operation  Valid values:   *`inference`* `train` |
| PAGE_COUNT | NUMBER | The number of pages processed |
| DOCUMENT_COUNT | NUMBER | The number of documents processed |
| FEATURE_COUNT | NUMBER | The number of data values defined for document processing operations that involve entry extraction |

## Usage notes

* The view provides up-to-date credit usage for an account within the last 365 days (1 year).
* Credit rate usage is based on the number of messages processed, as outlined in the [Snowflake Service Consumption Table](https://www.snowflake.com/legal-files/CreditConsumptionTable.pdf).
