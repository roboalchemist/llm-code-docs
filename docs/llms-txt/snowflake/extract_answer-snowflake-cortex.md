# Source: https://docs.snowflake.com/en/sql-reference/functions/extract_answer-snowflake-cortex.md

Categories:
:   [String & binary functions](../functions-string.md) (AI Functions)

# EXTRACT_ANSWER (SNOWFLAKE.CORTEX)

Extracts an answer to a given question from a text document. The document may be a plain-English document or a string
representation of a semi-structured (JSON) data object.

## Syntax

```sqlsyntax
SNOWFLAKE.CORTEX.EXTRACT_ANSWER(
    <source_document>, <question>)
```

## Arguments

`source_document`
:   A string containing the plain-text or JSON document that contains the answer to the question.

`question`
:   A string containing the question to be answered.

## Returns

A string containing an answer to the given question.

## Access control requirements

Users must use a role that has been granted the [SNOWFLAKE.CORTEX_USER database role](../snowflake-db-roles.md).
See [Cortex LLM privileges](../../user-guide/snowflake-cortex/aisql.md) for more information on granting this privilege.

## Example

In this example, `review_content` is a column from the `reviews` table:. To extract an answer from each row
of the table:

```sqlexample
SELECT SNOWFLAKE.CORTEX.EXTRACT_ANSWER(review_content,
    'What dishes does this review mention?')
FROM reviews LIMIT 10;
```

## Legal notices

Refer to [Snowflake AI and ML](../../guides-overview-ai-features.md).

## Limitations

Snowflake Cortex functions do not support dynamic tables.
