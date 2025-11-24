# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-guardrail-metrics/chunk-utilization/chunk-utilization-luna.md

# Chunk Utilization Luna

> Understand Galileo's Chunk Utilization Luna Metric

***Definition:*** For each chunk retrieved in a RAG pipeline, Chunk Utilization measures the fraction of the text in that chunk that had an impact on the model's response.

Chunk Utilization ranges from 0 to 1. A value of 1 means that the entire chunk affected the response, while a lower value like 0.5 means that the chunk contained some "extraneous" text which did not affect the response.

Chunk Utilization is closely related to Chunk Attribution: Attribution measures whether or not a chunk affected the response, and Utilization measures how much of the chunk text was involved in the effect. Only chunks that were Attributed can have Utilization scores greater than zero.

***Calculation:*** Chunk Utilization Luna is computed using a fine-tuned in-house Galileo evaluation model. The model is a transformer-based encoder that is trained to identify the relevant and utilized information in the provided a query, context, and response. The same model is used to compute Chunk Adherence, Chunk Completeness, Chunk Attribution and Utilization, and a single inference call is used to compute all the Luna metrics at once. The model is trained on carefully curated RAG datasets and optimized to closely align with the RAG Plus metrics.

For each token in the provided context, the model outputs a *utilization probability*, i.e the probability that this token affected the response. *Chunk Utilization Luna* is then computed as the fraction of tokens with high utilization probability out of all tokens in the chunk.

We recommend starting with "Luna" and seeing if this covers your needs. If you see the need for higher accuracy or would like explanations for the ratings, you can switch over to [Chunk Utilization Plus](/galileo/gen-ai-studio-products/galileo-guardrail-metrics/chunk-utilization/chunk-utilization-plus).

**Explainability**

The Luna model identifies which parts of the chunks were utilized by the model when generating its response. These sections can be highlighted in your retriever nodes by clicking on the <Icon icon="eye" /> icon next to the Chunk Utilization metric value in your *Retriever* nodes.

![](https://mintlify.s3.us-west-1.amazonaws.com/galileo/images/chunk-utilization-explanation-luna.png)
