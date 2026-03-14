# Source: https://docs.snowflake.com/en/release-notes/2026/other/2026-02-20-use-ai-functions-privilege.md

# Feb 20, 2026: USE AI FUNCTIONS account privilege for Cortex AI Functions

Snowflake now provides the USE AI FUNCTIONS account privilege to control access to Cortex AI Functions. This privilege allows administrators to manage which roles can use AI Functions across the account.

By default, the USE AI FUNCTIONS privilege is granted to the PUBLIC role, allowing all users to access Cortex AI Functions. Account administrators can revoke this privilege from PUBLIC and grant it to specific roles for more granular access control.

Users need both the USE AI FUNCTIONS account privilege and the CORTEX_USER database role to use all Snowflake Cortex AI Functions. Note that AI_AGG and AI_SUMMARIZE_AGG functions remain accessible to users with only the CORTEX_USER role.

For more information, see [Snowflake Cortex AI Functions (including LLM functions)](../../../user-guide/snowflake-cortex/aisql.md).
