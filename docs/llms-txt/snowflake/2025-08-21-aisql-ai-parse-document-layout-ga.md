# Source: https://docs.snowflake.com/en/release-notes/2025/other/2025-08-21-aisql-ai-parse-document-layout-ga.md

# Aug 21, 2025: AI Parse Document layout mode (*General availability*)

The Snowflake Cortex AI_PARSE_DOCUMENT document is now generally available with advanced layout extraction capabilities. This fully managed SQL function extracts the layout of the page in Markdown format, preserving text, tables, and structural elements from documents with enterprise-grade accuracy and scale.

> **Note:**
>
> The AI_PARSE_DOCUMENT function is the new version of SNOWFLAKE.CORTEX.PARSE_DOCUMENT.
> The old function is still supported, but Snowflake recommends using the new function.

Key capabilities of AI_PARSE_DOCUMENT include:

* **Complex layout mastery:** Accurately process multi-column research papers, financial reports, and technical
  documentation while preserving reading order and document hierarchy.
* **Precise table extraction:** Maintains table structure, headers, and relationships from financial statements,
  regulatory filings, and data-heavy documents for downstream analysis
* **Advanced Layout Preservation** Handles mixed content including embedded images, pull quotes, and complex
  formatting without losing context or meaning

For more information, see [Parsing documents with AI_PARSE_DOCUMENT](../../../user-guide/snowflake-cortex/parse-document.md).
