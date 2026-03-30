# Source: https://docs.snowflake.com/en/sql-reference/functions/embed_text_1024-snowflake-cortex.md

Categories:
:   [String & binary functions](../functions-string.md) (AI Functions)

# EMBED_TEXT_1024 (SNOWFLAKE.CORTEX)

> **Note:**
>
> [AI_EMBED](ai_embed.md) is the latest version of this function.
> Use AI_EMBED for the latest functionality.
> You can continue to use EMBED_TEXT_1024 (SNOWFLAKE.CORTEX).

Creates a vector embedding of 1024 dimensions from text.

## Syntax

```sqlsyntax
SNOWFLAKE.CORTEX.EMBED_TEXT_1024( <model>, <text> )
```

## Arguments

`model`
:   A string specifying the vector embedding model to be used to generate the embedding. This must be one of the following values.

    > * `snowflake-arctic-embed-l-v2.0`
    > * `snowflake-arctic-embed-l-v2.0-8k`
    > * `nv-embed-qa-4`
    > * `multilingual-e5-large`
    > * `voyage-multilingual-2`

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

## Example

In this example, a vector embedding is generated for the phrase `hello world` using the `snowflake-arctic-embed-l-v2.0` model:

```sqlexample
SELECT SNOWFLAKE.CORTEX.EMBED_TEXT_1024('snowflake-arctic-embed-l-v2.0', 'hello world');
```

In this example, a vector embedding is generated for the Spanish phrase `hola mundo` using the `snowflake-arctic-embed-l-v2.0` model:

```sqlexample
SELECT SNOWFLAKE.CORTEX.EMBED_TEXT_1024('snowflake-arctic-embed-l-v2.0', 'hola mundo');
```

## Legal notices

Refer to [Snowflake AI and ML](../../guides-overview-ai-features.md).

## Limitations

Snowflake Cortex functions do not support dynamic tables.
