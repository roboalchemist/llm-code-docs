# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-guardrail-metrics/action-advancement.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.galileo.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Action Advancement

> Understand Galileo's Action Advancement Metric

***Definition:*** Determines whether the assistant successfully accomplished or advanced towards at least one user goal.

More precisely, accomplishing or advancing towards a user's goal requires the assistant to either provide a (at least partial) answer to one of the user's questions, ask for further information or clarification about a user ask, or providing confirmation that a successful action has been taken.
The answer or resolution must in addition be factually accurate, directly addressing a user's ask and align with the tool's outputs.

If the response does not have an *Action Advancement* score of 100%, then at least one judge considered that the model did not make progress on any user goal.

***Calculation:*** *Action Advancement* is computed by sending additional requests to an LLM (e.g. OpenAI's GPT4o-mini), using a carefully engineered chain-of-thought prompt that asks the model to follow the above precise definition. The metric requests multiple distinct responses to this prompt, each of which produces an explanation along with a final judgment: yes or no. The final Action Advancement score is the fraction of "yes" responses, divided by the total number of responses.

We also surface one of the generated explanations. The surfaced explanation is always chosen to align with the majority judgment among the responses.

<Info>*Note:* This metric is computed by prompting an LLM multiple times, and thus requires additional LLM calls to compute.</Info>

***Usefulness:*** This metric is most useful in Agentic Workflows, where an Agent decides the course of action to take and could select Tools. This metric helps you detect whether the right course of action was taken by the Agent, and whether it helped advance towards the user's goal.
