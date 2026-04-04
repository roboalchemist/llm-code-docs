# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-guardrail-metrics/chunk-attribution/chunk-attribution-luna.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.galileo.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Chunk Attribution Luna

> Understand Galileo's Chunk Attribution Luna Metric

***Definition:*** For each chunk retrieved in a RAG pipeline, Chunk Attribution measures whether or not that chunk had an effect on the model's response.

Chunk Attribution is a binary metric: each chunk is either Attributed or Not Attributed.

Chunk Attribution is closely related to Chunk Utilization: Attribution measures whether or not a chunk affected the response, and Utilization measures how much of the chunk text was involved in the effect. Only chunks that were Attributed can have Utilization scores greater than zero.

***Calculation:*** Chunk Attribution Luna is computed using a fine-tuned in-house Galileo evaluation model. The model is a transformer-based encoder that is trained to identify the relevant and utilized information in the provided a query, context, and response. The same model is used to compute Chunk Adherence, Chunk Completeness, Chunk Attribution and Utilization, and a single inference call is used to compute all the Luna metrics at once. The model is trained on carefully curated RAG datasets and optimized to closely align with the RAG Plus metrics.

For each token in the provided context, the model outputs a *utilization probability*, i.e the probability that this token affected the response. If the *utilization probability* of any token in the chunk exceeds a pre-defined threshold, that chunk is labeled as Attributed.

<Info>
  We recommend starting with "Luna" and seeing if this covers your needs. If you see the need for higher accuracy, you can switch over to [Chunk Attribution
  Plus](/galileo/gen-ai-studio-products/galileo-guardrail-metrics/context-adherence/context-adherence-plus).
</Info>
