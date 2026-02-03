# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-guardrail-metrics/completeness.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.galileo.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Completeness

> Understand Galileo's Completeness Metric

<Info>This metric is intended for RAG use cases and is only available if you [log your retriever's output](/galileo/gen-ai-studio-products/galileo-evaluate/how-to/evaluate-and-optimize-rag-applications).</Info>

<iframe src="https://cdn.iframe.ly/8FcEdmh" width="100%" height="480px" allowfullscreen="" scrolling="no" allow="encrypted-media *;" />

***Definition:*** Measures how thoroughly your model's response covered the relevant information available in the context provided.

Completeness and Context Adherence are closely related, and designed to complement one another:

* Context Adherence answers the question, "is the model's response *consistent with* the information in the context?"

* Completeness answers the question, "is the relevant information in the context *fully reflected* in the model's response?"

In other words, if Context Adherence is "precision," then Completeness is "recall."

Consider this simple, stylized example that illustrates the distinction:

* User query: "Who was Galileo Galilei?"

* Context: "Galileo Galilei was an Italian astronomer."

* Model response: "Galileo Galilei was Italian."

This response would receive a perfect *Context Adherence* score: everything the model said is *supported* by the context.

But this is not an ideal response. The context also specified that Galileo was an astronomer, and the user probably wants to know that information as well.

Hence, this response would receive a low *Completeness* score. Tracking Completeness alongside Context Adherence allows you to detect cases like this one, where the model is "too reticent" and fails to mention relevant information.

***What to do when completeness is low?***

To fix low *Completeness* values, we recommend adjusting the prompt to tell the model to include all the relevant information it can find in the provided context.

### Luna vs Plus

We offer two ways of calculating Completeness: *Luna* and *Plus*.

[*Completeness Luna*](/galileo/gen-ai-studio-products/galileo-guardrail-metrics/completeness/completeness-luna) is computed using Galileo in-house small language models. They're free of cost, but lack 'explanations'. Completeness Luna is a cost effective way to scale up you RAG evaluation workflows.

[*Completeness Plus*](/galileo/gen-ai-studio-products/galileo-guardrail-metrics/completeness/completeness-plus) is computed using the [Chainpoll](/galileo/gen-ai-studio-products/galileo-ai-research/chainpoll) technique. It relies on OpenAI models so it incurs an additional cost. Completeness Plus has shown better results in internal benchmarks. Additionally, *Plus* offers explanations for its ratings (i.e. why a response was or was not complete).
