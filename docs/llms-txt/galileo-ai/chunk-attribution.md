# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-guardrail-metrics/chunk-attribution.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.galileo.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Chunk Attribution

> Understand Galileo's Chunk Attribution Metric

<Info>This metric is intended for RAG use cases and is only available if you [log your retriever's output](/galileo/gen-ai-studio-products/galileo-evaluate/how-to/evaluate-and-optimize-rag-applications).</Info>

<iframe src="https://cdn.iframe.ly/ScPpa09" width="100%" height="480px" allowfullscreen="" scrolling="no" allow="encrypted-media *;" />

***Definition:*** For each chunk retrieved in a RAG pipeline, Chunk Attribution measures whether or not that chunk had an effect on the model's response.

Chunk Attribution is a binary metric: each chunk is either Attributed or Not Attributed.

Chunk Attribution is closely related to Chunk Utilization: Attribution measures whether or not a chunk affected the response, and Utilization measures how much of the chunk text was involved in the effect. Only chunks that were Attributed can have Utilization scores greater than zero.

***What to do when Chunk Attribution is low?***

Chunk Attribution can help you iterate on your RAG pipeline in several different ways:

* *Tuning the number of retrieved chunks.*
  * If your system is producing satisfactory responses, but many chunks are Not Attributed, then you may be able to reduce the number of chunks retrieved per example without adversely impacting response quality.

  * This will improve the efficiency of the system, resulting in lower cost and latency.

* *"Debugging" anomalous model behavior in individual examples.*
  * If a specific model response is unsatisfactory or unusual, and you want to understand why, Attribution can help you zero in on the chunks that affected the response.

  * This lets you get to the root of the issue more quickly when inspecting individual examples.

### Luna vs Plus

We offer two ways of calculating Completeness: *Luna* and *Plus*.

[*Chunk Attribution Luna*](/galileo/gen-ai-studio-products/galileo-guardrail-metrics/context-adherence/context-adherence-luna) is computed using Galileo in-house small language models. They're free of cost. Completeness Luna is a cost-effective way to scale up you RAG evaluation workflows.

[*Chunk Attribution Plus*](/galileo/gen-ai-studio-products/galileo-guardrail-metrics/context-adherence/context-adherence-plus) is computed by sending an additional request to your LLM. It relies on OpenAI models so it incurs an additional cost. *Chunk Attribution Plus* has shown better results in internal benchmarks.

<Info>
  **Chunk Attribution** and **Chunk Utilization** are closely related and rely on the same models for computation. The "**chunk\_attribution\_utilization\_\{luna/plus}**" scorer will compute both.
</Info>
