# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-evaluate/how-to/customize-chainpoll-powered-metrics.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.galileo.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Customize Chainpoll-powered Metrics

> Improve metric accuracy by customizing your Chainpoll-powered metrics

[**ChainPoll**](/galileo/gen-ai-studio-products/galileo-ai-research/chainpoll) is a powerful, flexible technique for LLM-based evaluation built by Galileo's Research team. It is used to power multiple Guardrail Metrics across the Galileo platform:

* Context Adherence Plus

* Chunk Attribution & Utilization

* Completeness Plus

* Correctness

Chainpoll leverages a chain-of-thought prompting technique and prompting an LLM multiple times to calculate metric values. There are two levers one can customize for a Chainpoll metric:

* The model that gets queried

* The number of times we prompt that model

Generally, better models will provide more accurate metric values, and a higher number of judges will increase the accuracy and stability of metric values. We've configured our Chainpoll-powered metrics to balance the trade-off of Cost and Accuracy.

## Changing the model or number of judges of a Chainpoll metric

We allow customizing execution parameters for the [AI-powered metrics](/galileo/gen-ai-studio-products/galileo-guardrail-metrics) from our Guardrail Store. By default, these metrics use gpt-4o-mini for the model and 3 judges (except for chunk attribution & utilization, which uses 1 judge and for which the number of judges cannot be customized). To customize this, when creating your run you can customize these metrics as:

```python  theme={null}
pq.EvaluateRun(..., scorers=[
    pq.CustomizedChainPollScorer(
        scorer_name=pq.CustomizedScorerName.context_adherence_plus,
        model_alias=pq.Models.gpt_4o,
        num_judges=7)
    ])
```

#### Customizable Metrics

The metrics that can be customized are:

1. Chunk Attribution & Chunk Utilization: `pq.CustomizedScorerName.chunk_attribution_utilization_plus`

2. Completeness: `pq.CustomizedScorerName.completeness_plus`

3. Context Adherence: `pq.CustomizedScorerName.context_adherence_plus`

4. Correctness: `pq.CustomizedScorerName.correctness`

#### Models supported

* OpenAI or Azure models that use the Chat Completions API
* Gemini 1.5 Flash and Pro through VertexAI

When entering the model name, use a model alias from [this list](https://promptquality.docs.rungalileo.io/#promptquality.Models).

#### Number of Judges supported

Judges can be set to integers between `0` and `10`.

<Note>Note: Chunk Attribution and Chunk Utilization don't benefit from increasing the number of judges.</Note>
