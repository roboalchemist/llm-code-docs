# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-guardrail-metrics/correctness.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.galileo.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Correctness

> Understand Galileo's Correctness Metric

<iframe src="https://cdn.iframe.ly/r50dDNO" width="100%" height="480px" allowfullscreen="" scrolling="no" allow="encrypted-media *;" />

***Definition:*** Measures whether a given model response is factual or not. *Correctness (f.k.a. Factuality)* is a good way of uncovering *open-domain hallucinations:* factual errors that don't relate to any specific documents or context. A high Correctness score means the response is more likely to be accurate vs a low response indicates a high probability for hallucination.

If the response is *factual* (i.e. it has a value of 1 or close to 1), the information is believed to be correct. If a response is *not factual* (i.e. it has a value of 0 or close to 0), it's likely to contain factual errors.

***Calculation:*** *Correctness* is computed by sending an additional requests to OpenAI's GPT4-o, using a carefully engineered chain-of-thought prompt that asks the model to judge whether or not the response was factually accurate. The metric requests multiple distinct responses to this prompt, each of which produces an explanation along with a final judgment: yes or no. The Correctness score is the fraction of "yes" responses, divided by the total number of responses.

We also surface one of the generated explanations. The surfaced explanation is always chosen to align with the majority judgment among the responses. In other words, if the score is greater than 0.5, the explanation will provide an argument that the response is factual; if the score is less than 0.5, the explanation will provide an argument that it is not factual.

<Info>*Note:* This metric is computed by prompting an LLM multiple times, and thus requires additional LLM calls to compute.</Info>

***What to do when Correctness is low?***

When an response has a low Correctness score, it's likely that the response has non-factual information. We recommend:

1. Flag and examine response that are likely to be non-factual

2. Adjust the prompt to tell the model to stick to the information it's given in the context.

3. Take precaution measures to stop non-factual responses from reaching the end user.

***How to differentiate between Correctness and Context Adherence?***

Correctness measures whether a model response has factually correct information, regardless of whether that piece of information is contained in the context.

Here we are illustrating the difference between Correctness and Context Adherence using a text-to-sql example.

<iframe src="https://cdn.iframe.ly/vSeh0Pd" width="100%" height="480px" allowfullscreen="" scrolling="no" allow="encrypted-media *;" />
