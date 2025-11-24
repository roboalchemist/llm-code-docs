# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-guardrail-metrics/tool-selection-quality.md

# Tool Selection Quality

> Understand Galileo's Tool Selection Quality Metric

***Definition:*** Determines whether the agent selected the correct tool and for each tool the correct arguments.

More precisely, the assistant is not expected to call tools if there are no unanswered user queries, if no tools can help answer any query or if all the information to answer is contained in the history. In cases where the agent shouldn’t call tools but it does, the turn is considered unsuccessful. In cases where the assistant should use tools and it does, then the turn is considered successful if in addition it selected the correct tool and for each tool the correct arguments (i.e., correct argument names and values, and provided all required arguments).

If the response does not have a *Tool Selection Quality* score of 100%, then at least one judge considered that the model chose the wrong Tool(s), or the correct Tool(s) with incorrect parameters.

***Calculation:*** *Tool Selection Quality* is computed by sending additional requests to an LLM (e.g. OpenAI's GPT4o-mini), using a carefully engineered chain-of-thought prompt that asks the model to judge whether or not the tools selected were correct. The metric requests multiple distinct responses to this prompt, each of which produces an explanation along with a final judgment: yes or no. The final Tool Selection Quality score is the fraction of "yes" responses, divided by the total number of responses.

We also surface one of the generated explanations. The surfaced explanation is always chosen to align with the majority judgment among the responses.

<Info>*Note:* This metric is computed by prompting an LLM multiple times, and thus requires additional LLM calls to compute.</Info>

***Usefulness:*** This metric is most useful in Agentic Workflows, where an LLM decides the course of action to take by selecting a Tool. This metric helps you detect whether the right course of action was taken by the Agent.
