# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-guardrail-metrics/context-adherence/context-adherence-plus.md

# Context Adherence Plus

> Understand Galileo's Context Adherence Plus Metric

***Definition:*** Measures whether your model's response was purely based on the context provided.

***Calculation:*** Context Adherence Plus is computed by sending additional requests to OpenAI's GPT3.5 (by default) and GPT4, using a carefully engineered chain-of-thought prompt that asks the model to judge whether or not the response was grounded in the context. The metric requests multiple distinct responses to this prompt, each of which produces an explanation along with a final judgment: yes or no. The *Context Adherence Plus* score is the fraction of "yes" responses, divided by the total number of responses.

We also surface one of the generated explanations. The surfaced explanation is always chosen to align with the majority judgment among the responses. In other words, if the score is greater than 0.5, the explanation will provide an argument that the response is grounded; if the score is less than 0.5, the explanation will provide an argument that it is not grounded.

#### *What to Do When Context Adherence Is Low?*

When a response is highly adherent to the context (i.e., it has a value of 1 or close to 1), it strictly includes information from the provided context. However, when a response is not adherent (i.e., it has a value of 0 or close to 0), it likely contains facts not present in the given context.

Several factors can contribute to low context adherence:

1. **Insufficient Context**: If the source document lacks key information needed to answer the user's question, the response may be incomplete or off-topic. To address this, users should consider using various context enrichment strategies to ensure that the source documents retrieved contain the necessary information to answer the user's questions effectively.

2. **Lack of Internal Reasoning and Creativity**: While Retrieval-Augmented Generation (RAG) focuses on factual grounding, it doesn't directly enhance the internal reasoning processes of the LLM. This limitation can cause the model to struggle with logic or common-sense reasoning, potentially resulting in nonsensical outputs even if the facts are accurate.

3. **Lack of Contextual Awareness**: Although RAG provides factual grounding for the language model, it might not fully understand the nuances of the prompt or user intent. This can lead to the model incorporating irrelevant information or missing key points, thus affecting the overall quality of the response.

To improve context adherence, we recommend:

1. Ensuring your context DB has all the necessary info to answer the question

2. Adjusting the prompt to tell the model to stick to the information it's given in the context.

***Deep dive:*** to read more about the research behind this metric, see [RAG Quality Metrics using ChainPoll](/galileo/gen-ai-studio-products/galileo-ai-research/rag-quality-metrics-using-chainpoll).

<Info>*Note:* This metric is computed by prompting an LLM multiple times, and thus requires additional LLM calls to compute.</Info>
