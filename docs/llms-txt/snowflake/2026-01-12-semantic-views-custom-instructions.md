# Source: https://docs.snowflake.com/en/release-notes/2026/other/2026-01-12-semantic-views-custom-instructions.md

# Jan 12, 2026: Specifying custom instructions in semantic views

When defining a [semantic view](../../../user-guide/views-semantic/overview.md), you can now provide
[instructions for Cortex Analyst](../../../user-guide/snowflake-cortex/cortex-analyst/custom-instructions.md) that explain how to:

* Generate the SQL statement
* Classify questions and prompt for additional information

In the [CREATE SEMANTIC VIEW](../../../sql-reference/sql/create-semantic-view.md) command, you can use the AI_SQL_GENERATION and AI_QUESTION_CATEGORIZATION
clauses to specify instructions for generating the SQL statement and classifying questions.

For more information, see [Providing custom instructions for Cortex Analyst](../../../user-guide/views-semantic/sql.md).
