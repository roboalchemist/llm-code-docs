# Source: https://docs.snowflake.com/en/release-notes/2026/other/2026-01-27-ai-count-tokens-function-ga.md

# Jan 27, 2026: Estimate token usage with AI_COUNT_TOKENS (*General availability*)

AI_COUNT_TOKENS, a Cortex AI helper function that helps users estimate token consumption and understand how prompt
context impacts cost, is now generally available. AI_COUNT_TOKENS takes into account the function, the LLM model (if
applicable), and any additional inputs that affect token count, such as categories/labels for classification tasks.

In general, token usage increases as prompts become more descriptive and complex. Minimal prompts with limited context
consume fewer tokens, while deeper context, task descriptions, and examples increase token counts. With AI_COUNT_TOKENS,
users can evaluate how these tradeoffs affect token usage and therefore cost while developing their AI workloads.

This capability is especially useful for establishing best practices around:

* How much context to include in prompts
* When richer prompts meaningfully improve accuracy
* When examples are worth the additional token cost
* How best to standardize prompt design across teams and workloads

The supported functions include:

* [AI_CLASSIFY](../../../sql-reference/functions/ai_classify.md)
* [AI_COMPLETE](../../../sql-reference/functions/ai_complete.md)
* [AI_EMBED](../../../sql-reference/functions/ai_embed.md)
* [AI_SENTIMENT](../../../sql-reference/functions/ai_sentiment.md)
* [AI_SIMILARITY](../../../sql-reference/functions/ai_similarity.md)
* [AI_TRANSLATE](../../../sql-reference/functions/ai_translate.md)

For more information, see [AI_COUNT_TOKENS](../../../sql-reference/functions/ai_count_tokens.md).
