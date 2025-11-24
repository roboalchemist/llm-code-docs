# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-guardrail-metrics/context-adherence.md

# Context Adherence

> Understand Galileo's Context Adherence Metric

<iframe src="https://cdn.iframe.ly/SmSQBT2" width="100%" height="480px" allowfullscreen="" scrolling="no" allow="encrypted-media *;" />

***Definition:*** *Context Adherence* is a measurement of *closed-domain* *hallucinations:* cases where your model said things that were not provided in the context.

If a response is *adherent* to the context (i.e. it has a value of 1 or close to 1), it only contains information given in the context. If a response is *not adherent* (i.e. it has a value of 0 or close to 0), it's likely to contain facts not included in the context provided to the model.

### Luna vs Plus

We offer two ways of calculating Context Adherence: *Luna* and *Plus*.

[*Context Adherence Luna*](/galileo/gen-ai-studio-products/galileo-guardrail-metrics/context-adherence/context-adherence-luna) is computed using Galileo in-house small language models (Luna). They're free of cost, but lack 'explanations'. Context Adherence Luna is a cost effective way to scale up you RAG evaluation workflows.

[*Context Adherence Plus*](/galileo/gen-ai-studio-products/galileo-guardrail-metrics/completeness/completeness-plus) is computed using the [Chainpoll](/galileo/gen-ai-studio-products/galileo-ai-research/chainpoll) technique. It relies on OpenAI models so it incurs an additional cost. Context Adherence Plus has shown better results in internal benchmarks. Additionally, *Plus* offers explanations for its ratings (i.e. why something was or was not adherent).
