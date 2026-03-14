# Source: https://docs.snowflake.com/en/release-notes/2025/other/2025-10-13-cortex-embed-user-db-role.md

# Oct 13, 2025: CORTEX_EMBED_USER database role (*General availability*)

Snowflake has added a CORTEX_EMBED_USER database role in the SNOWFLAKE database to better manage access to Cortex
embedding functions. Embedding functions, which convert text to a vector of numbers that represent the meaning of the
text, include AI_EMBED, EMBED_TEXT_768, and EMBED_TEXT_1024. This new role allows you to grant users access to embedding
functions without granting them access to other Cortex features. The pre-existing CORTEX_USER role continues to provide
access to Cortex features including embedding functions.

For more information about this role, see [SNOWFLAKE.CORTEX_EMBED_USER database role](../../../sql-reference/snowflake-db-roles.md).
