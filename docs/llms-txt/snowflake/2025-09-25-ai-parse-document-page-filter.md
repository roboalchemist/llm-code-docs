# Source: https://docs.snowflake.com/en/release-notes/2025/other/2025-09-25-ai-parse-document-page-filter.md

# Sep 25, 2025: Page filtering for AI_PARSE_DOCUMENT

The AI_PARSE_DOCUMENT function now includes page filtering capabilities, allowing you to parse specific pages or ranges within large documents.
You can process only the content you need, improving efficiency and reducing processing costs when working with multi-page documents.

These page filtering capabilities let you:

* Target specific content by specifying exact start and end points within a document.
* Build efficient document classification pipelines by extracting just the first page from multiple documents and using
  AI_CLASSIFY for instant categorization across document collections.
* Optimize batch processing workflows by combining directory scanning with selective page extraction to automatically categorize and process large document repositories based on content from key pages.

For more information, see [Parsing documents with AI_PARSE_DOCUMENT](../../../user-guide/snowflake-cortex/parse-document.md) and [AI_PARSE_DOCUMENT](../../../sql-reference/functions/ai_parse_document.md).
