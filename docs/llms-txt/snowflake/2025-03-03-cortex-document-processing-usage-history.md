# Source: https://docs.snowflake.com/en/release-notes/2025/other/2025-03-03-cortex-document-processing-usage-history.md

# Mar 03, 2025: Snowflake Cortex Document Processing Usage History

Snowflake announces support for viewing the query usage history for document processing functions. You can use the ACCOUNT_USAGE.CORTEX_DOCUMENT_PROCESSING_USAGE_HISTORY view to see the document processing features, such as Document AI or PARSE_DOCUMENT, that were run and the number of credits that they consume. For example:

```sqlexample
SELECT *
  FROM SNOWFLAKE.ACCOUNT_USAGE.CORTEX_DOCUMENT_PROCESSING_USAGE_HISTORY
  WHERE CREDITS_USED > 0.072
```

For more information, see [CORTEX_DOCUMENT_PROCESSING_USAGE_HISTORY view](../../../sql-reference/account-usage/cortex_document_processing_usage_history.md).
