# Source: https://docs.snowflake.com/en/release-notes/2024/other/2024-05-08-embed-text-model.md

# May 08, 2024 — New model for vector embedding — *Preview*

We’re pleased to announce a change that will make it easier for you to build generative AI workflows using
the [EMBED_TEXT_768 (SNOWFLAKE.CORTEX)](../../../sql-reference/functions/embed_text-snowflake-cortex.md) function, part of the
[Cortex LLM Functions](../../../user-guide/snowflake-cortex/aisql.md).

* The `snowflake-arctic-embed-m` model is now available for text embedding tasks. This model was trained by
  Snowflake. It outperforms the existing `e5-base-v2` model on standard retrieval benchmarks, while keeping the same
  number of parameters. Read more in the [model announcement blog](https://www.snowflake.com/blog/introducing-snowflake-arctic-embed-snowflakes-state-of-the-art-text-embedding-family-of-models/).
