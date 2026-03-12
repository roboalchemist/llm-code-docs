# Source: https://docs.snowflake.com/en/sql-reference/functions/ai_sentiment.md

Categories:
:   [String & binary functions](../functions-string.md) (AI Functions)

# AI_SENTIMENT

> **Note:**
>
> AI_SENTIMENT is the updated version of [ENTITY_SENTIMENT (SNOWFLAKE.CORTEX)](entity_sentiment-snowflake-cortex.md).
> For the latest functionality, use AI_SENTIMENT.

Returns overall and category [sentiment](../../user-guide/snowflake-cortex/ai-sentiment.md) in the given input text.

## Syntax

```sqlsyntax
AI_SENTIMENT( <text> [ , <categories> ] )
```

## Arguments

**Required:**

`text`
:   A string containing the text in which sentiment is detected.

**Optional:**

`categories`
:   An array containing up to ten categories (also called entities or aspects) for which sentiment should be extracted. Each category is a
    string. For example, if extracting sentiment from a restaurant review, you might specify
    `['cost', 'quality', 'service', 'wait time']` as the categories. Each category may be a maximum of 30 characters long.

    If you do not provide this argument, AI_SENTIMENT returns only the overall sentiment.

## Returns

An OBJECT value containing a `categories` field. `categories` is an array of category records. Each category includes these fields:

* `name`: The name of the category. The category names match the categories specified in the `categories` argument.
* `sentiment`: The sentiment of the category. Each sentiment result is one of the following strings.

  * `unknown`: The category was not mentioned in the text.
  * `positive`: The category was mentioned positively in the text.
  * `negative`: The category was mentioned negatively in the text.
  * `neutral`: The category was mentioned in the text, but neither positively nor negatively.
  * `mixed`: The category was mentioned both positively and negatively in the text.

The `overall` category record is always included and contains the overall sentiment of the text.

Example:

```output
{
  "categories": [
    {
      "name": "overall",
      "sentiment": "mixed"
    },
    {
      "name": "Brand",
      "sentiment": "unknown"
    },
    {
      "name": "Cost",
      "sentiment": "negative"
    },
    {
      "name": "Professionalism",
      "sentiment": "unknown"
    }
  ]
}
```

## Access control requirements

Users must use a role that has been granted the [SNOWFLAKE.CORTEX_USER database role](../snowflake-db-roles.md).
See [Cortex LLM privileges](../../user-guide/snowflake-cortex/aisql.md) for more information on this role.

## Usage notes

AI_SENTIMENT can analyze sentiment in English, French, German, Hindi, Italian, Spanish, and Portuguese. You can specify
categories in the language of the text or in English.

## Examples

The following example uses AI_SENTIMENT to get the overall sentiment of a food service review.

```sqlexample
SELECT AI_SENTIMENT('A tourist\'s delight, in low urban light,
    Recommended gem, a pizza night sight. Swift arrival, a pleasure so right,
    Yet, pockets felt lighter, a slight pricey bite. 💰🍕🚀');
```

Return value:

```output
{
  "categories": [
    {
      "name": "overall",
      "sentiment": "positive"
    }
  ]
}
```

In this example, a table named `reviews` contains a column named `review_content` containing the text of movie reviews
submitted by users. The query returns the sentiment of several facets of up to ten reviews.

```sqlexample
SELECT
  AI_SENTIMENT(
    review_content,
    ['concept', 'performance', 'script', 'cinematography', 'soundtrack']
  ),
  review_content
  FROM reviews LIMIT 10;
```

## Regional availability

AI_SENTIMENT is available in the following regions:

| Function  (Model) | AWS US West 2  (Oregon) | AWS US East 1  (N. Virginia) | AWS Europe Central 1  (Frankfurt) | AWS Europe West 1  (Ireland) | AWS AP Southeast 2  (Sydney) | AWS AP Northeast 1  (Tokyo) | Azure East US 2  (Virginia) | Azure West Europe  (Netherlands) | AWS  (Cross-Region) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| AI_SENTIMENT | ✔ | ✔ | ✔ |  |  | ✔ | ✔ | ✔ | ✔ |

## Legal notices

Refer to [Snowflake AI and ML](../../guides-overview-ai-features.md).

## Limitations

Snowflake Cortex functions do not support dynamic tables.
