# Source: https://docs.snowflake.com/en/sql-reference/functions/summarize-snowflake-cortex.md

Categories:
:   [String & binary functions](../functions-string.md) (AI Functions)

# SUMMARIZE (SNOWFLAKE.CORTEX)

Summarizes the given English-language input text.

## Syntax

```sqlsyntax
SNOWFLAKE.CORTEX.SUMMARIZE(<text>)
```

## Arguments

`text`
:   A string containing the English text from which a summary should be generated.

## Returns

A string containing a summary of the original text.

## Access control requirements

Users must use a role that has been granted the [SNOWFLAKE.CORTEX_USER database role](../snowflake-db-roles.md).
See [Cortex LLM privileges](../../user-guide/snowflake-cortex/aisql.md) for more information on this privilege.

## Example

In this example, a table named `reviews` contains a column named `review_content` containing the text of reviews
submitted by users. The query returns a summary of each review.

```sqlexample
SELECT SNOWFLAKE.CORTEX.SUMMARIZE(review_content) FROM reviews LIMIT 10;
```

## Legal notices

Refer to [Snowflake AI and ML](../../guides-overview-ai-features.md).

## Limitations

Snowflake Cortex functions do not support dynamic tables.
