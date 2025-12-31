# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-guardrail-metrics/prompt-perplexity.md

# Prompt Perplexity

> Understanding Galileo's Prompt Perplexity Metrics

***Definition:*** Measures the Prompt *Perplexity*, using the log probability's provided by most models of the prompt.

***Availability:***

Perplexity can be calculated only with the LLM intergrations that provide log probabilities. Those are:

* OpenAI:
  * Any Evaluate runs created from the Galileo Playground or with `pq.run(...)`, using the chosen model.
  * Any Evaluate workflow runs using `davinci-001`.
  * Any Observe worfklows using `davinci-001`.
* Azure OpenAI:
  * Any Evaluate runs created from the Galileo Playground or with `pq.run(...)`, using the chosen model.
  * Any Evaluate workflow runs `text-davinci-003` or `text-curie-001`, if they're available in your Azure deployment.
  * Any Observe worfklows using `text-davinci-003` or `text-curie-001`, if they're available in your Azure deployment.

***Calculation:*** *Prompt Perplexity* is calculated using OpenAI's Davinci models. It is calculated as the exponential of the negative average of the log probability's over the entire prompt. Thus it ranges from 0-infinity with lower values indicating the model on average was more certain of the next token in a sequence.

***What to do when Prompt Perplexity is low?***

Lower perplexity indicates your model is better tuned towards your data, as it can better predict the next token. Furthermore, the paper [Demystifying Prompts in Language Models via Perplexity Estimation](https://arxiv.org/abs/2212.04037) has shown that lower perplexity values in the input (aka. prompt) also lead to better outcomes in the generations (aka. results).
