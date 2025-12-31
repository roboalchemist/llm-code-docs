# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-guardrail-metrics/ground-truth-adherence.md

# Ground Truth Adherence

> Measure ground truth adherence in generative AI models with Galileo's Guardrail Metrics, ensuring accurate and aligned outputs with dataset benchmarks.

***Definition:*** Measures whether the model's response is semantically equivalent to your Ground Truth.

If the response has a *High Ground Truth Adherence* (i.e. it has a value of 1 or close to 1), the model's response was semantically equivalent to the Groud Truth. If a response has a *Low Ground Truth Adherence* (i.e. it has a value of 0 or close to 0), the model's response is likely semantically different from the Ground Truth.

<Info>
  *Note:* This metric requires a Ground Truth to be set. Check out [this page](/galileo/gen-ai-studio-products/galileo-evaluate/how-to/logging-and-comparing-against-your-expected-answers) to learn how to add a Ground Truth to your runs.
</Info>

***Calculation:*** *Ground Truth Adherence* is computed by sending additional requests to OpenAI's GPT4o, using a carefully engineered chain-of-thought prompt that asks the model to judge whether or not the Ground Truth and Response are equivalent. The metric requests multiple distinct responses to this prompt, each of which produces an explanation along with a final judgment: yes or no. The Ground Truth Adherence score is the fraction of "yes" responses, divided by the total number of responses.

We also surface one of the generated explanations. The surfaced explanation is always chosen to align with the majority judgment among the responses.

<Info>*Note:* This metric is computed by prompting an LLM multiple times, and thus requires additional LLM calls to compute.</Info>
