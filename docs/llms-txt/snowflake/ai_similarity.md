# Source: https://docs.snowflake.com/en/sql-reference/functions/ai_similarity.md

Categories:
:   [String & binary functions](../functions-string.md) (AI Functions)

# AI_SIMILARITY

Computes a similarity score based on the vector cosine similarity value of the inputs’ embedding vectors. Currently supports both text and image similarity computation.

## Syntax

Applying AI_SIMILARITY to string or image inputs:

```sqlsyntax
AI_SIMILARITY( <input1>, <input2> )
```

Specifying the config object:

```sqlsyntax
AI_SIMILARITY( <input1>, <input2>, <config_object> )
```

## Arguments

**Required:**

If you’re specifying input strings:

`input1`, `input2`
:   The strings with the text that you’re comparing and using to compute the similarity score.

If you’re specifying input images:

`input1`, `input2`
:   [FILE data type](../../user-guide/unstructured-intro.md) referencing the images to be compared.

> **Note:**
>
> AI_SIMILARITY does not support computing the similarity between text and image inputs.

**Optional:**

`config_object`
:   An [OBJECT](../data-types-semistructured.md) containing key-value pairs used to configure the model.

| Key | Type | Default | Description |
| --- | --- | --- | --- |
| `model` | [STRING](../data-types-text.md) | For STRING input, default to `'snowflake-arctic-embed-l-v2.0'`. For IMAGE input, default to `'voyage-multimodal-3'` | The embedding model used for embedding. Supported values are:   *`'snowflake-arctic-embed-l-v2.0'`* `'nv-embed-qa-4'` *`'multilingual-e5-large'`* `'voyage-multilingual-2'` *`'snowflake-arctic-embed-m-v1.5'`* `'snowflake-arctic-embed-m'` *`'e5-base-v2'`* `'voyage-multimodal-3'` (IMAGE) |

## Returns

Returns a float value of range -1 to 1 that represents the similarity score computed using vector similarity between two embedding vectors for the inputs.

## Access control requirements

Users must use a role that has been granted the [SNOWFLAKE.CORTEX_USER database role](../snowflake-db-roles.md).
See [Cortex LLM privileges](../../user-guide/snowflake-cortex/aisql.md) for more information on this privilege.

## Examples

### AI_SIMILARITY: Text

In this example, the function is computing a similarity score between the two statement inputs `'I like this dish'` and `'This dish is very good'`.

```sqlexample
SELECT AI_SIMILARITY('I like this dish', 'This dish is very good');
```

We can also compute similarity on text columns.

```sqlexample
SELECT
    review
FROM restaurant_reviews
ORDER BY AI_SIMILARITY(review, 'I love the food here!');
```

### AI_SIMILARITY: Images

In this example, the function computes a similarity score between the two images, `cat.jpg` and `2cats.jpg`, stored in a Snowflake stage `@file_stage`.

```sqlexample
SELECT AI_SIMILARITY(TO_FILE('@file_stage', 'cat.jpg'), TO_FILE('@file_stage', '2cats.jpg'));
```

We can also compute similarity among the images using Snowflake Directory Table for the stage containing the images.

```sqlexample
SELECT
    to_file('@file_stage', relative_path)
FROM directory(@file_stage)
WHERE AI_SIMILARITY(f, to_file(@file_stage, 'cat.jpg')) >= 0.5;
```

## Limitations

* Snowflake AI functions don’t work on FILEs created from stage files from the following stage types:

  * Internal stages with encryption mode `TYPE = 'SNOWFLAKE_FULL'`
  * External stages with any customer-side encrypted mode:

    * `TYPE = 'AWS_CSE'`
    * `TYPE = 'AZURE_CSE'`
  * User stage, table stage
  * Stage with double-quoted names

## Billing

`AI_SIMILARITY` is currently billed under the `AI_EMBED` line item in SNOWFLAKE.ACCOUNT_USAGE.CORTEX_FUNCTIONS_USAGE_HISTORY view.
