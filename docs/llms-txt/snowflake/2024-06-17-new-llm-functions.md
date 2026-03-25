# Source: https://docs.snowflake.com/en/release-notes/2024/other/2024-06-17-new-llm-functions.md

# June 17, 2024 — New LLM helper functions - TRY_COMPLETE and COUNT_TOKENS

With this release, we are pleased to announce the availability of two Cortex LLM helper functions, TRY_COMPLETE and COUNT_TOKENS.
These functions are purpose-built and managed functions that help to reduce cases of query failures when the number of input tokens
exceed a model limit.

For more information, see [Snowflake Cortex AI Functions (including LLM functions)](../../../user-guide/snowflake-cortex/aisql.md).

## New SQL function

The following functions are now generally available with this release:

| Function Category | New Function | Description |
| --- | --- | --- |
| [LLM Function](../../../user-guide/snowflake-cortex/aisql.md) | [TRY_COMPLETE (SNOWFLAKE.CORTEX)](../../../sql-reference/functions/try_complete-snowflake-cortex.md) | Tries to run the COMPLETE function but returns NULL instead of an error code if unable to run. |
| [LLM Function](../../../user-guide/snowflake-cortex/aisql.md) | [COUNT_TOKENS (SNOWFLAKE.CORTEX)](../../../sql-reference/functions/count_tokens-snowflake-cortex.md) | Counts the tokens in a given input text based on the model or function specified. |
