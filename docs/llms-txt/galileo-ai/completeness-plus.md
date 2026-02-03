# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-guardrail-metrics/completeness/completeness-plus.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.galileo.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Completeness Plus

> Understand Galileo's Completeness Plus Metric

The metric is intended for RAG workflows.

***Definition:*** Measures how thoroughly your model's response covered the relevant information available in the context provided.

***Calculation:*** Completeness is computed by sending additional requests to an OpenAI LLM, using a carefully engineered chain-of-thought prompt that asks the model to determine what fraction of relevant information was covered in the response. The metric requests multiple distinct responses to this prompt, each of which produces an explanation along with a final numeric score between 0 and 1.

The Completeness score is an average over the individual scores.

We also surface one of the generated explanations. The surfaced explanation is chosen from the response whose *individual* score was closest to the *average* score over all the responses. For example, if we make 3 requests and receive the scores \[0.4, 0.5, 0.6], the Completeness score will be 0.5, and the explanation from the second response will be surfaced.

***Usefulness:*** To fix low *Completeness* values, we recommend adjusting the prompt to tell the model to include all the relevant information it can find in the provided context.

***Deep dive:*** to read more about the research behind this metric, see [RAG Quality Metrics using ChainPoll](/galileo/gen-ai-studio-products/galileo-ai-research/rag-quality-metrics-using-chainpoll).

<Info>*Note:* This metric is computed by prompting an LLM multiple times, and thus requires additional LLM calls to compute.</Info>
