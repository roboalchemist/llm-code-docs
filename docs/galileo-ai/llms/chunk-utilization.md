# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-guardrail-metrics/chunk-utilization.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.galileo.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Chunk Utilization

> Understand Galileo's Chunk Utilization Metric

<Info>This metric is intended for RAG use cases and is only available if you [log your retriever's output](/galileo/gen-ai-studio-products/galileo-evaluate/how-to/evaluate-and-optimize-rag-applications).</Info>

<iframe src="https://cdn.iframe.ly/6WQtsx4" width="100%" height="480px" allowfullscreen="" scrolling="no" allow="encrypted-media *;" />

***Definition:*** For each chunk retrieved in a RAG pipeline, Chunk Utilization measures the fraction of the text in that chunk that had an impact on the model's response.

Chunk Utilization ranges from 0 to 1. A value of 1 means that the entire chunk affected the response, while a lower value like 0.5 means that the chunk contained some "extraneous" text which did not affect the response.

Chunk Utilization is closely related to Chunk Attribution: Attribution measures whether or not a chunk affected the response, and Utilization measures how much of the chunk text was involved in the effect. Only chunks that were Attributed can have Utilization scores greater than zero.

***What to do when Chunk Utilization is low?***

Low Chunk Utilization scores could mean one of two things: (1) your chunks are probably longer than they need to be, or (2) the LLM generator model is failing at incorporating all the relevant information in the chunks. You can differentiate between the two scenarios by checking the [Chunk Relevance](/galileo/gen-ai-studio-products/galileo-guardrail-metrics/chunk-relevance) score. If Chunk Relevance is also low, then you are likely experiencing scenario (1). If Chunk Relevance is high, you are likely experiencing scenario (2).

In case (1), we recommend tuning your retriever to return shorter chunks, which will improve the efficiency of the system (lower cost and latency). In case (2), we recommend exploring a different LLM that may leverage the relevant information in the chunks more efficiently.

### Luna vs Plus

We offer two ways of calculating Completeness: *Luna* and *Plus*.

[*Chunk Utilization Luna*](/galileo/gen-ai-studio-products/galileo-guardrail-metrics/context-adherence/context-adherence-luna) is computed using Galileo in-house small language models. They're free of cost. Completeness Luna is a cost effective way to scale up you RAG evaluation workflows.

[*Chunk Utilization Plus*](/galileo/gen-ai-studio-products/galileo-guardrail-metrics/chunk-utilization/chunk-utilization-plus) is computed by sending an additional request to your LLM. It relies on OpenAI models so it incurs an additional cost. *Chunk Utilization Plus* has shown better results in internal benchmarks.

<Info>
  **Chunk Attribution** and **Chunk Utilization** are closely related and rely on the same models for computation. The "**chunk\_attribution\_utilization\_\{luna/plus}**" scorer will compute both.
</Info>
