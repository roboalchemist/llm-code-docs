# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-guardrail-metrics/chunk-relevance.md

# Chunk Relevance

> Understand Galileo's Chunk Relevance Luna Metric

***Definition:*** For each chunk retrieved in a RAG pipeline, Chunk Relevance detects the sections of the text that contain useful information to address the query.

Chunk Relevance ranges from 0 to 1. A value of 1 means that the entire chunk is useful for answering the query, while a lower value like 0.5 means that the chunk contained some unnecessary text that is not relevant to the query.

**Explainability**

The Luna model identifies which parts of the chunks were relevant to the query. These sections can be highlighted in your retriever nodes by clicking on the <Icon icon="eye" /> icon next to the Chunk Utilization metric value in your *Retriever* nodes.

<img src="https://mintlify.s3.us-west-1.amazonaws.com/galileo/images/chunk-relevance-explanation-luna.png" />

***Calculation:*** Chunk Relevance Luna is computed using a fine-tuned in-house Galileo evaluation model. The model is a transformer-based encoder that is trained to identify the relevant and utilized information in the provided a query, context, and response. The same model is used to compute Chunk Adherence, Chunk Completeness, Chunk Attribution, and Utilization, and a single inference call is used to compute all the Luna metrics at once. The model is trained on carefully curated RAG datasets and optimized to closely align with the RAG Plus metrics.

For each token in the provided context, the model outputs a *relevance probability*, i.e the probability that this token is useful for answering the query.

***What to do when Chunk Relevance is low?***

Low Chunk Relevance scores indicate that your chunks are probably longer than they need to be. In this case, we recommend tuning your retriever to return shorter chunks, which will improve the efficiency of the system (lower cost and latency).
