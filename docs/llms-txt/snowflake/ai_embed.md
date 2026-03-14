# Source: https://docs.snowflake.com/en/sql-reference/functions/ai_embed.md

Categories:
:   [String & binary functions](../functions-string.md) (AI Functions)

# AI_EMBED

> **Note:**
>
> AI_EMBED is the updated version of [EMBED_TEXT_1024 (SNOWFLAKE.CORTEX)](embed_text_1024-snowflake-cortex.md) and [EMBED_TEXT_768 (SNOWFLAKE.CORTEX)](embed_text-snowflake-cortex.md).
> For the latest functionality, use AI_EMBED.

Creates an embedding vector from text or an image. Embeddings are abstract numerical representations of the features of
a piece of text or an image that can be used to determine the degree of similarity between pieces of text or images,
which can be used for semantic search, clustering, classification, and other tasks.

## Region availability

The following table shows the regions where you can use the AI_EMBED function for text and images:

| Data type | AWS US West 2  (Oregon) | AWS US East 1  (N. Virginia) | AWS Europe Central 1  (Frankfurt) | AWS Europe West 1  (Ireland) | AWS AP Southeast 2  (Sydney) | AWS AP Northeast 1  (Tokyo) | Azure East US 2  (Virginia) | Azure West Europe  (Netherlands) | AWS  (Cross-Region) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Text | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| Image | ✔ | ✔ | ✔ |  |  |  |  | ✔ | ✔ |

## Syntax

```sqlsyntax
AI_EMBED( <model> , <input> )
```

## Arguments

**Required:**

`model`
:   A string specifying the vector embedding model to be used to generate an embedding.

    For text, you can provide the following values:

    * `snowflake-arctic-embed-l-v2.0`
    * `snowflake-arctic-embed-l-v2.0-8k`
    * `nv-embed-qa-4`
    * `multilingual-e5-large`
    * `voyage-multilingual-2`
    * `snowflake-arctic-embed-m-v1.5`
    * `snowflake-arctic-embed-m`
    * `e5-base-v2`

    For images, you can provide only the following value:

    * `voyage-multimodal-3`

    Supported models might have different [costs](../../user-guide/snowflake-cortex/aisql.md).

`input`
:   The string or image (as a [FILE object](to_file.md)) to generate an embedding from. Images must be:

    * In JPEG, WEBP, PNG, or BMP format
    * No more than 10 MB in size
    * No more than 8,000 x 8,000 pixels

## Returns

An embedding vector of type VECTOR derived from the input text or image.

## Access control requirements

You must use a role that has been granted the SNOWFLAKE.CORTEX_USER database role *or* the SNOWFLAKE.CORTEX_EMBED_USER
database role to call this function. See [Cortex LLM privileges](../../user-guide/snowflake-cortex/aisql.md) for more information on granting one of
these privileges.

## Examples

### Text example

In this example, a vector embedding is generated for the phrase `hello world` using the `snowflake-arctic-embed-l-v2.0` model:

```sqlexample
SELECT AI_EMBED('snowflake-arctic-embed-l-v2.0', 'hello world');
```

### Image example

In this example, a vector embedding is generated for a staged image using the `voyage-multimodal-3` model:

```sqlexample
SELECT AI_EMBED('voyage-multimodal-3',
        TO_FILE ('@my_images', 'CITY_WALKING1.PNG'));
```

## Limitations

* Snowflake AI functions don’t work on FILE objects created from files in the following kinds of stages:

  * Internal stages with encryption mode `TYPE = 'SNOWFLAKE_FULL'`
  * External stages with any customer-side encrypted mode, such as `AWS_CSE` or `AZURE_CSE`.
  * User stage
  * Table stage
  * Stage with double-quoted names

## Legal notices

Refer to [Snowflake AI and ML](../../guides-overview-ai-features.md).
