# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-guardrail-metrics/uncertainty.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.galileo.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Uncertainty

> Understand Galileo's Uncertainty Metric

***Definition:*** Measures how much the model is deciding randomly between multiple ways of continuing the output. *Uncertainty* is measured at both the token level and the response level. Higher uncertainty means the model is less certain.

***Availability:***

Uncertainty can be calculated only with the LLM intergrations that provide log probabilities. Those are:

* OpenAI:
  * Any Evaluate runs created from the Galileo Playground or with `pq.run(...)`, using the chosen model.
  * Any Evaluate workflow runs using `davinci-001`.
  * Any Observe worfklows using `davinci-001`.
* Azure OpenAI:
  * Any Evaluate runs created from the Galileo Playground or with `pq.run(...)`, using the chosen model.
  * Any Evaluate workflow runs `text-davinci-003` or `text-curie-001`, if they're available in your Azure deployment.
  * Any Observe worfklows using `text-davinci-003` or `text-curie-001`, if they're available in your Azure deployment.

***Calculation:*** *Uncertainty* at the token level tells us how confident the model is of the next token given the preceding tokens. *Uncertainty* at the response level is simply the maximum token-level *Uncertainty,* over all the tokens in the model's response. It is calculated using OpenAI's Davinci models or Chat Completion models (available via OpenAI or Azure).

<Info>
  To calculate the *Uncertainty* metric, we require having`text-curie-001` or
  `text-davinci-003`models available in your Azure environment. This is required
  in order to fetch log probabilities. For Galileo's Guardrail metrics that rely
  on GPT calls (*Factuality* and *Groundedness*), we require using `0613` or
  above versions of `gpt-35-turbo` ([Azure docs](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/models)).
</Info>

***What to do when uncertainty is low?***

Our research has found high uncertainty scores correlate with hallucinations, made up facts, and citations. Looking at highly uncertain responses can flag areas where your model is struggling.
