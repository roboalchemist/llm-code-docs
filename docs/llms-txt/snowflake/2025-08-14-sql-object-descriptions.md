# Source: https://docs.snowflake.com/en/release-notes/2025/other/2025-08-14-sql-object-descriptions.md

# Aug 14, 2025: Using SQL for Cortex Powered Object Descriptions (*Preview*)

You can now call a stored procedure, AI_GENERATE_TABLE_DESC, to programmatically generate Cortex Powered Object Descriptions. The Cortex
Powered Object Descriptions feature uses the [Snowflake Cortex COMPLETE function](../../../sql-reference/functions/complete-snowflake-cortex.md)
to automatically generate descriptions for tables, views, and columns.

The AI_GENERATE_TABLE_DESC stored procedure is in preview. Using Snowsight to generate object descriptions is generally available.

For more information, see [Using SQL to automatically generate object descriptions](../../../user-guide/sql-cortex-descriptions.md).
