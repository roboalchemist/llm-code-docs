# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-guardrail-metrics/action-completion.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.galileo.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Action Completion

> Understand Galileo's Action Completion Metric

***Definition:*** Determines whether the assistant successfully accomplished all user's goals.

More precisely, accomplishing a user's goal requires the assistant to provide a complete answer in the case of a question, or providing a confirmation that a successful action has been taken in the case of a request. The answer or resolution must in addition be coherent, factually accurate, comprehensively address every aspect of the user's ask, not contradict tools outputs and summarize every relevant part returned by tools.

If the response does not have an *Action Completion* score of 100%, then at least one judge considered that the model did not accomplish every user goal.

***Calculation:*** *Action Completion* is computed by sending additional requests to an LLM (e.g. OpenAI's GPT4o), using a carefully engineered chain-of-thought prompt that asks the model to follow the above precise definition. The metric requests multiple distinct responses to this prompt, each of which produces an explanation along with a final judgment: yes or no. The final Action Completion score is the fraction of "yes" responses, divided by the total number of responses.

We also surface one of the generated explanations. The surfaced explanation is always chosen to align with the majority judgment among the responses.

<Info>*Note:* This metric is computed by prompting an LLM multiple times, and thus requires additional LLM calls to compute.</Info>

***Usefulness:*** This metric is most useful in Agentic Workflows, where an Agent decides the course of action to take and could select Tools. This metric helps you detect whether the right course of action was eventually taken by the Agent, and whether it fully accomplished all user's goals.
