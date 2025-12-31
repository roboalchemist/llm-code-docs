# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-guardrail-metrics/instruction-adherence.md

# Instruction Adherence

> Assess instruction adherence in AI outputs using Galileo Guardrail Metrics to ensure prompt-driven models generate precise and actionable results.

***Definition:*** Measures whether a model followed or adhered to the system or prompt instructions when generating a response. *Instruction Adherence* is a good way to uncover hallucinations where the model is ignoring instructions.

If the response has a *High Instruction Adherence* (i.e. it has a value of 1 or close to 1), the model likely followed its instructions when generating its response. If a response has a *Low Instruction Adherence* (i.e. it has a value of 0 or close to 0), the model likely went off-script and ignored parts of its instructions when generating a response.

***Calculation:*** *Instruction Adherence* is computed by sending additional requests to OpenAI's GPT4o, using a carefully engineered chain-of-thought prompt that asks the model to judge whether or not the response was generated in adherence to the instructions. The metric requests multiple distinct responses to this prompt, each of which produces an explanation along with a final judgment: yes or no. The Instruction Adherence score is the fraction of "yes" responses, divided by the total number of responses.

We also surface one of the generated explanations. The surfaced explanation is always chosen to align with the majority judgment among the responses.

<Info>*Note:* This metric is computed by prompting an LLM multiple times, and thus requires additional LLM calls to compute.</Info>

***What to do when Instruction Adherence is low?***

When a response has a low Instruction Adherence score, the model likely ignored its instructions when generating the response. We recommend:

1. Flag and examine response that did not follow instructions

2. Experiment with different prompts to see which version the model is more likely to adhere to

3. Take precaution measures to stop non-factual responses from reaching the end user.

***How to differentiate between Instruction Adherence and Context Adherence?***

Context Adherence measures whether the response is adhering to the *Context* provided (e.g. your retrieved documents), whereas Instruction Adherence measures whether the response is adhering to the instructions in your prompt template.
