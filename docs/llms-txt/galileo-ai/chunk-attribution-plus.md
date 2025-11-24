# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-guardrail-metrics/chunk-attribution/chunk-attribution-plus.md

# Chunk Attribution Plus

> Understand Galileo's Chunk Attribution Plus Metric

The metric is intended for RAG workflows.

***Definition:*** For each chunk retrieved in a RAG pipeline, Chunk Attribution measures whether or not that chunk had an effect on the model's response.

Chunk Attribution is a binary metric: each chunk is either Attributed or Not Attributed.

Chunk Attribution is closely related to Chunk Utilization: Attribution measures whether or not a chunk affected the response, and Utilization measures how much of the chunk text was involved in the effect. Only chunks that were Attributed can have Utilization scores greater than zero.

***Calculation:*** Chunk Attribution is computed by sending an additional request to an OpenAI LLM, using a carefully engineered prompt that asks the model to trace information in the response back to individual chunks and sentences within those chunks.

The same prompt is used for both Chunk Attribution and Chunk Utilization, and a single LLM request is used to compute both metrics at once.

***Deep dive:*** to read more about the research behind this metric, see [RAG Quality Metrics using ChainPoll](/galileo/gen-ai-studio-products/galileo-ai-research/rag-quality-metrics-using-chainpoll).

<Info>*Note:* This metric is computed by prompting an LLM, and thus requires additional LLM calls to compute.</Info>
