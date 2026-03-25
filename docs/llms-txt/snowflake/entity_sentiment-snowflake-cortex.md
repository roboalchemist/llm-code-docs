# Source: https://docs.snowflake.com/en/sql-reference/functions/entity_sentiment-snowflake-cortex.md

Categories:
:   [String & binary functions](../functions-string.md) (AI Functions)

# ENTITY_SENTIMENT (SNOWFLAKE.CORTEX)

> **Note:**
>
> [AI_SENTIMENT](ai_sentiment.md) is the latest version of this function.
> Use AI_SENTIMENT for the latest functionality.
> You can continue to use ENTITY_SENTIMENT (SNOWFLAKE.CORTEX).

Returns sentiment scores for English-language text, including overall sentiment and specific sentiment for specified entities.

## Syntax

```sqlsyntax
SNOWFLAKE.CORTEX.ENTITY_SENTIMENT(<text> [, <entities> ])
```

## Arguments

`text`
:   A string containing the text for which sentiment scores should be calculated.

`entities`
:   An array containing up to ten entities or aspects for which sentiment scores should be calculated. Each entity is a
    string. For example, if scoring sentiment from a restaurant review, the `entities` array might be `['cost',
    'quality', 'waiting time']`. Entities may be a maximum of 30 characters long.

    This argument is optional. If you do not provide it, the function will return only the overall sentiment.

## Returns

An OBJECT containing a `categories` field. `categories` is an ARRAY of category records. Each category includes these fields:

* `name`: The name of the category.
* `sentiment`: The sentiment of the category: positive, negative, neutral, mixed, or unknown, as a string.

Additionally, an `overall` category contains the overall sentiment of the text.

## Access control requirements

Users must use a role that has been granted the [SNOWFLAKE.CORTEX_USER database role](../snowflake-db-roles.md).
See [Cortex LLM privileges](../../user-guide/snowflake-cortex/aisql.md) for more information on this privilege.

## Example

In this example, a table named `reviews` contains a column named `review_content` containing the text of movie reviews
submitted by users. The query returns a sentiment for several entities from each review.

```sqlexample
SELECT SNOWFLAKE.CORTEX.ENTITY_SENTIMENT(review_content,
    ['concept', 'performance', 'script', 'cinematography', 'soundtrack']),
        review_content FROM reviews LIMIT 10;
```

## Legal notices

Refer to [Snowflake AI and ML](../../guides-overview-ai-features.md).

## Limitations

Snowflake Cortex functions do not support dynamic tables.
