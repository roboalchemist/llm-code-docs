# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-evaluate/how-to/choose-your-guardrail-metrics.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.galileo.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Choose your Guardrail Metrics

> Select and understand guardrail metrics in Galileo Evaluate to effectively assess your prompts and models, utilizing both industry-standard and proprietary metrics.

<iframe src="https://cdn.iframe.ly/u1tjpYO" width="500px" height="300px" allowfullscreen="" scrolling="no" allow="encrypted-media *;" />

## Galileo Metrics

Galileo has built a menu of **Guardrail Metrics** for you to choose from. These metrics are tailored to your use case and are designed to help you evaluate your prompts and models.

Galileo's Guardrail Metrics are a combination of industry-standard metrics (e.g. BLEU, ROUGE-1, Perplexity) and an outcome of Galileo's in-house ML Research Team (e.g. Uncertainty, Correctness, Context Adherence).

Here's a list of the metrics supported today

### Output Quality Metrics:

* [**Uncertainty**](/galileo/gen-ai-studio-products/galileo-guardrail-metrics/uncertainty)**:** Measures the model's certainty in its generated responses. Uncertainty works at the response level as well as at the token level. It has shown a strong correlation with hallucinations or made-up facts, names, or citations.

* [**Correctness**](/galileo/gen-ai-studio-products/galileo-guardrail-metrics/correctness) - Measures whether the facts stated in the response are based on real facts. This metric requires additional LLM calls. Combined with Uncertainty, Factuality is a good way of uncovering Hallucinations.

* [**BLEU & ROUGE-1**](/galileo/gen-ai-studio-products/galileo-guardrail-metrics/bleu-and-rouge-1) - These metrics measure n-gram similarities between your Generated Responses and your Target output. These metrics are automatically computed when you add a {target} column in your dataset.

* [**Prompt Perplexity**](/galileo/gen-ai-studio-products/galileo-guardrail-metrics/prompt-perplexity) - Measure the perplexity of a prompt. Previous research has shown that as perplexity decreases, generations tend to increase in quality.

### RAG Quality Metrics:

* [**Context Adherence**](/galileo/gen-ai-studio-products/galileo-guardrail-metrics/context-adherence) - Measures whether your model's response was purely based on the context provided. This metric is intended for RAG users. We have two options for this metric: *Luna* and *Plus*.
  * Context Adherence *Luna* is powered by small language models we've trained. It's free of cost.

  * Context Adherence *Plus* includes an explanation or rationale for the rating. These metrics and the explanations are powered by an LLM (e.g. OpenAI GPT3.5) and thus incur additional costs. *Plus* has shown to have better performance.

* [**Completeness**](/galileo/gen-ai-studio-products/galileo-guardrail-metrics/completeness/completeness) - Measures how thoroughly your model's response covered relevant information from the context provided. This metric is intended for RAG use cases and is only available if you [log your retriever's output](/galileo/gen-ai-studio-products/galileo-evaluate/how-to/evaluate-and-optimize-rag-applications). There are two versions available:
  * Completeness *Luna* is powered by small language models we've trained. It's free of cost.

  * Completeness *Plus* includes an explanation or rationale for the rating. These metrics and the explanations are powered by an LLM (e.g. OpenAI GPT3.5) and thus incur additional costs. *Plus* has shown to have better performance.

* [**Chunk Attribution**](/galileo/gen-ai-studio-products/galileo-guardrail-metrics/chunk-attribution) - Measures which individual chunks retrieved in a RAG workflow influenced your model's response. This metric is intended for RAG use cases and is only available if you [log your retriever's output](/galileo/gen-ai-studio-products/galileo-evaluate/how-to/evaluate-and-optimize-rag-applications). There are two versions available:
  * Chunk Attribution *Luna* is powered by small language models we've trained. It's free of cost.

  * Chunk Attribution *Plus* is powered by an LLM (e.g. OpenAI GPT3.5) and thus incurs additional costs. *Plus* has shown to have better performance.

* [**Chunk Utilization**](/galileo/gen-ai-studio-products/galileo-guardrail-metrics/chunk-utilization) - For each chunk retrieved in a RAG workflow, measures the fraction of the chunk text that influenced your model's response. This metric is intended for RAG use cases and is only available if you [log your retriever's output](/galileo/gen-ai-studio-products/galileo-evaluate/how-to/evaluate-and-optimize-rag-applications). There are two versions available:
  * Chunk Attribution *Luna* is powered by small language models we've trained. It's free of cost.

  * Chunk Attribution *Plus* is powered by an LLM (e.g. OpenAI GPT3.5) and thus incurs additional costs. *Plus* has shown to have better performance.

* [**Context Relevance**](/galileo/gen-ai-studio-products/galileo-guardrail-metrics/context-relevance) - Measures if the context has enough information to answer the user query. This metric is intended for RAG users.

### Safety Metrics:

* [**Private Identifiable Information**](/galileo/gen-ai-studio-products/galileo-guardrail-metrics/private-identifiable-information) **-** This Guardrail Metric surfaces any instances of PII in your model's responses. We surface whether your text contains any credit card numbers, social security numbers, phone numbers, street addresses, and email addresses.

* [**Toxicity**](/galileo/gen-ai-studio-products/galileo-guardrail-metrics/toxicity) - Measures whether the model's responses contained any abusive, toxic, or foul language.

* [**Tone**](/galileo/gen-ai-studio-products/galileo-guardrail-metrics/tone) - Classifies the tone of the response into 9 different emotion categories: neutral, joy, love, fear, surprise, sadness, anger, annoyance, and confusion.

* [**Sexism**](/galileo/gen-ai-studio-products/galileo-guardrail-metrics/sexism) - Measures how 'sexist' a comment might be perceived ranging in the values of 0-1 (1 being more sexist).

* [**Prompt Injection**](https://docs.rungalileo.io/galileo/gen-ai-studio-products/galileo-guardrail-metrics/prompt-injection) - Detects and classifies various categories of prompt injection attacks.

* More coming very soon.

A more thorough description of all Guardrail Metrics can be found [here](/galileo/gen-ai-studio-products/galileo-guardrail-metrics).

<Info>
  When creating runs from code, you'll need to add your Guardrail Metrics as "scorers", check out "[Enabling Scorers in Run](/galileo/gen-ai-studio-products/galileo-evaluate/how-to/enabling-scorers-in-runs)" to learn how to do so.
</Info>

If you want to set up your custom metrics, please see instructions [here](https://docs.rungalileo.io/galileo/galileo-gen-ai-studio/prompt-inspector/registering-and-using-custom-metrics).
