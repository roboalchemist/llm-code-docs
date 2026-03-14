# Source: https://docs.snowflake.com/en/sql-reference/functions/count_tokens-snowflake-cortex.md

Categories:
:   [String & binary functions](../functions-string.md) (AI Functions)

# COUNT_TOKENS (SNOWFLAKE.CORTEX)

> **Note:**
>
> [AI_COUNT_TOKENS](ai_count_tokens.md) is the latest version of this function.
> Use AI_COUNT_TOKENS for the latest functionality.
> You can continue to use COUNT_TOKENS (SNOWFLAKE.CORTEX).

Returns the number of tokens in a prompt for the large language model or the task-specific function specified in the argument. This
function does not support fine-tuned models.

## Syntax

```sqlsyntax
SNOWFLAKE.CORTEX.COUNT_TOKENS( <model_name> , <input_text> )
```

## Arguments

**Required:**

`model_name`
:   Name of the model you want to base the token count on. Specify one of the following values:

    * `deepseek-r1`
    * `e5-base-v2`
    * `e5-large-v2`
    * `llama3-70b`
    * `llama3-8b`
    * `llama3.1-405b`
    * `llama3.1-70b`
    * `llama3.1-8b`
    * `llama3.3-70b`
    * `llama4-maverick`
    * `llama4-scout`
    * `mistral-7b`
    * `mistral-large`
    * `mistral-large2`
    * `mixtral-8x7b`
    * `nv-embed-qa-4`
    * `snowflake-arctic-embed-l-v2.0`
    * `snowflake-arctic-embed-m-v1.5`
    * `snowflake-arctic-embed-m`
    * `snowflake-arctic`
    * `snowflake-llama-3.1-405b`
    * `snowflake-llama-3.3-70b`
    * `voyage-multilingual-2`

`input_text`
:   Input text to count the tokens in.

## Returns

Returns an [INT , INTEGER , BIGINT , SMALLINT , TINYINT , BYTEINT](../data-types-numeric.md) type that is the number of tokens in the input text based on the model or function specified.

## Usage notes

* If a function name is specified, the token count is based on the model used by the function.
* Use lowercase letters in function names.

> **Note:**
>
> COUNT_TOKENS does not account for the managed system prompt that is automatically added to the beginning of the input
> text when using a Cortex [Cortex AI functions](../../user-guide/snowflake-cortex/aisql.md). As a result, the value
> returned by COUNT_TOKENS is lower than the actual number of tokens processed by these functions.

## Examples

The following example returns the token count for the specified prompt using the `llama3.1-70b` model:

```sqlexample
SELECT SNOWFLAKE.CORTEX.COUNT_TOKENS( 'llama3.1-70b', 'what is a large language model?' );
```

```output
+---+
| 6 |
+---+
```

## Legal notices

Refer to [Snowflake AI and ML](../../guides-overview-ai-features.md).
