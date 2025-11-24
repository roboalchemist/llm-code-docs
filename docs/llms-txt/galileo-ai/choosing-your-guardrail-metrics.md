# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-observe/how-to/choosing-your-guardrail-metrics.md

# Choosing Your Guardrail Metrics

> Select and understand guardrail metrics in Galileo Observe to effectively evaluate your LLM applications, utilizing both industry-standard and proprietary metrics.

## How to turn metrics on or off

For metrics to be computed on your Observe project, open the `Settings & Alerts` section of your project, and turn on any metric you'd like to be calculated. Metrics are not computed retroactively, they'll only be computed on new traffic that flows through Observe.

## Galileo Metrics

Galileo has built a menu of **Guardrail Metrics** for you to choose from. These metrics are tailored to your use case and are designed to help you evaluate your LLM applications.

Galileo's Guardrail Metrics are a combination of industry-standard metrics and a product of Galileo's in-house [AI Research](/galileo-ai-research) Team (e.g. Uncertainty, Correctness, Context Adherence).

Here's a list of some of the metrics supported today:

* [**Context Adherence**](/galileo/gen-ai-studio-products/galileo-guardrail-metrics/context-adherence) - Measures whether your model's response was grounded on the context provided. This metric is intended for RAG or context-based use cases and is a good measure for hallucinations.

* [**Completeness**](/galileo/gen-ai-studio-products/galileo-guardrail-metrics/completeness) - Evaluates how comprehensively the response addresses the question using all the relevant information from the provided context. If Context Adherence is your RAG 'Precision' metric, Completeness is your RAG 'Recall'.

* [**Chunk Attribution**](/galileo/gen-ai-studio-products/galileo-guardrail-metrics/chunk-attribution) - Measures the number of chunks a model uses when generating an output. By optimizing the number of chunks a model is retrieving, teams can improve output quality and system performance and avoid the excess costs of including unused chunks in prompts to LLMs. This metric requires Galileo to [be hooked into your retriever step](/galileo/gen-ai-studio-products/galileo-observe/how-to/monitoring-your-rag-application).

* [**Chunk Utilization**](/galileo/gen-ai-studio-products/galileo-guardrail-metrics/chunk-utilization) - Measures how much of each chunk was used by a model when generating an output, and helps teams rightsize their chunk size. This metric requires Galileo to [be hooked into your retriever step](/galileo/gen-ai-studio-products/galileo-observe/how-to/monitoring-your-rag-application).

* [**Instruction Adherence**](/galileo/gen-ai-studio-products/galileo-guardrail-metrics/instruction-adherence) - Measures whether your model's response was grounded on the context provided. This metric is intended for RAG or context-based use cases and is a good measure for hallucinations.

* [**Correctness**](/galileo/gen-ai-studio-products/galileo-guardrail-metrics/correctness) - Measures whether the facts stated in the response are based on real facts. This metric requires additional LLM calls. Combined with Uncertainty, Factuality is a good way of uncovering Hallucinations.

* [**Prompt Injections**](/galileo/gen-ai-studio-products/galileo-guardrail-metrics/prompt-injection) - Identifies any adversarial attacks or prompt injections.

* [**Private Identifiable Information**](/galileo/gen-ai-studio-products/galileo-guardrail-metrics/private-identifiable-information) **-** This Guardrail Metric surfaces any instances of PII in your model's responses. We surface whether your text contains any credit card numbers, social security numbers, phone numbers, street addresses and email addresses.

* [**Toxicity**](/galileo/gen-ai-studio-products/galileo-guardrail-metrics/toxicity) - Measures whether the model's responses contained any abusive, toxic or foul language.

* [**Tone**](/galileo/gen-ai-studio-products/galileo-guardrail-metrics/tone) - Classifies the tone of the response into 9 different emotion categories: neutral, joy, love, fear, surprise, sadness, anger, annoyance, and confusion.

* [**Sexism**](/galileo/gen-ai-studio-products/galileo-guardrail-metrics/sexism) - Measures how 'sexist' a comment might be perceived ranging in the values of 0-1 (1 being more sexist).

* [**Uncertainty**](/galileo/gen-ai-studio-products/galileo-guardrail-metrics/uncertainty) - Measures the model's certainty in its generated responses. Uncertainty works at the response level as well as at the token level. It has shown a strong correlation with hallucinations or made-up facts, names, or citations.

* and more.

A more thorough description of all Guardrail Metrics can be found [here](/galileo/gen-ai-studio-products/galileo-guardrail-metrics).

## Custom Metrics

To set up custom metrics for Galileo Observe projects, please see instructions and sample code snippet [here.](https://docs.rungalileo.io/galileo/galileo-gen-ai-studio/observe-getting-started/registering-and-using-custom-metrics)
