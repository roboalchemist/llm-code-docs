# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-guardrail-metrics/chunk-utilization/chunk-utilization-plus.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.galileo.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Chunk Utilization Plus

> Leverage Chunk Utilization+ in Galileo Guardrail Metrics to optimize generative AI output segmentation and maximize model efficiency.

# Chunk Utilization Plus

Understand Galileo's Chunk Utilization Plus Metric

The metric is intended for RAG workflows.

***Definition:*** For each chunk retrieved in a RAG pipeline, Chunk Utilization measures the fraction of the text in that chunk that had an impact on the model's response.

Chunk Utilization ranges from 0 to 1. A value of 1 means that the entire chunk affected the response, while a lower value like 0.5 means that the chunk contained some "extraneous" text which did not affect the response.

Chunk Utilization is closely related to Chunk Attribution: Attribution measures whether or not a chunk affected the response, and Utilization measures how much of the chunk text was involved in the effect. Only chunks that were Attributed can have Utilization scores greater than zero.

***Calculation:*** Chunk Utilization is computed by sending an additional request to an OpenAI LLM, using a carefully engineered prompt that asks the model to trace information in the response back to individual chunks and sentences within those chunks.

The same prompt is used for both Chunk Attribution and Chunk Utilization, and a single LLM request is used to compute both metrics at once.

***Deep dive:*** to read more about the research behind this metric, see [RAG Quality Metrics using ChainPoll](/galileo/gen-ai-studio-products/galileo-ai-research/rag-quality-metrics-using-chainpoll).

*Note:* This metric is computed by prompting an LLM, and thus requires additional LLM calls to compute.

[PreviousChunk Utilization Luna](/galileo/gen-ai-studio-products/galileo-guardrail-metrics/context-adherence/context-adherence-luna)[NextUncertainty](/galileo/gen-ai-studio-products/galileo-guardrail-metrics/uncertainty)

Last updated 2 months ago
