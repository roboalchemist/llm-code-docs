# Source: https://docs.snowflake.com/en/release-notes/2024/other/2024-11-06-split-text-recursive-character.md

# November 06, 2024 — SPLIT_TEXT_RECURSIVE_CHARACTER Cortex function — *Preview*

Snowflake is pleased to announce the preview of the SPLIT_TEXT_RECURSIVE_CHARACTER function. This function splits a
string into smaller chunks of text, recursively, so that the text can be passed to embedding or search indexing
functions. Since many language models have a limit on the number of tokens they can process, this function is essential
to processing text larger than the token limit.

For more information, see [SPLIT_TEXT_RECURSIVE_CHARACTER (SNOWFLAKE.CORTEX)](../../../sql-reference/functions/split_text_recursive_character-snowflake-cortex.md).
