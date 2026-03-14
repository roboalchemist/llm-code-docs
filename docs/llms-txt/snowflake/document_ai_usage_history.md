# Source: https://docs.snowflake.com/en/sql-reference/account-usage/document_ai_usage_history.md

Schema:
:   [ACCOUNT_USAGE](../account-usage.md)

# DOCUMENT_AI_USAGE_HISTORY view

The DOCUMENT_AI_USAGE_HISTORY view can be used to query the job history for
[Document AI](../../user-guide/snowflake-cortex/document-ai/overview.md).

## Columns

| Column Name | Data Type | Description |
| --- | --- | --- |
| START_TIME | TIMESTAMP_LTZ | Start of the hourly time range in which the query usage took place. |
| END_TIME | TIMESTAMP_LTZ | End of the hourly time range in which the query usage took place. |
| CREDITS_USED | NUMBER(38,9) | Number of credits used for Document AI compute between START_TIME and END_TIME. |
| QUERY_ID | VARCHAR | A unique identifier for the SQL query. |
| OPERATION_NAME | TEXT | Name of the Document AI operation: `Inference` (entity extraction) or `Inference-Table-Extraction` (table extraction). |
| PAGE_COUNT | NUMBER | Number of pages processed. |
| DOCUMENT_COUNT | NUMBER | Number of documents processed. |
| FEATURE_COUNT | NUMBER | Number of data values defined to be extracted. |
