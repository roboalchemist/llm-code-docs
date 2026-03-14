# Source: https://docs.snowflake.com/en/sql-reference/functions/embed_text-snowflake-cortex.md

Categories:
:   [String & binary functions](../functions-string.md) (AI Functions)

# EMBED_TEXT_768 (SNOWFLAKE.CORTEX)

> **Note:**
>
> [AI_EMBED](ai_embed.md) is the latest version of this function.
> Use AI_EMBED for the latest functionality.
> You can continue to use EMBED_TEXT_768 (SNOWFLAKE.CORTEX).

Creates a vector embedding of 768 dimensions from English-language text.

## Syntax

```sqlsyntax
SNOWFLAKE.CORTEX.EMBED_TEXT_768( <model>, <text> )
```

## Arguments

`model`
:   A string specifying the vector embedding model to be used to generate the embedding. This must be one of the following values.

    > * `snowflake-arctic-embed-m-v1.5`
    > * `snowflake-arctic-embed-m`
    > * `e5-base-v2`

    Supported models might have different [costs](../../user-guide/snowflake-cortex/aisql.md).

`text`
:   The text for which an embedding should be calculated.

## Returns

A vector embedding of type VECTOR.

## Access control requirements

You must use a role that has been granted the SNOWFLAKE.CORTEX_USER database role *or* the SNOWFLAKE.CORTEX_EMBED_USER
database role to call this function. See [Cortex LLM privileges](../../user-guide/snowflake-cortex/aisql.md) for more information on granting one of
these privileges.

You must also have the USAGE privilege on the SNOWFLAKE.CORTEX schema to call this function.

## Examples

In this example, a vector embedding is generated for the phrase `hello world` using the `snowflake-arctic-embed-m-v1.5` model:

```sqlexample
SELECT SNOWFLAKE.CORTEX.EMBED_TEXT_768('snowflake-arctic-embed-m-v1.5', 'hello world');
```

## Legal notices

Refer to [Snowflake AI and ML](../../guides-overview-ai-features.md).

## Limitations

Snowflake Cortex functions do not support dynamic tables.
