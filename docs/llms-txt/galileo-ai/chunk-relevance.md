# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-guardrail-metrics/chunk-relevance.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.galileo.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Chunk Relevance

> Understand Galileo's Chunk Relevance Luna Metric

***Definition:*** For each chunk retrieved in a RAG pipeline, Chunk Relevance detects the sections of the text that contain useful information to address the query.

Chunk Relevance ranges from 0 to 1. A value of 1 means that the entire chunk is useful for answering the query, while a lower value like 0.5 means that the chunk contained some unnecessary text that is not relevant to the query.

**Explainability**

The Luna model identifies which parts of the chunks were relevant to the query. These sections can be highlighted in your retriever nodes by clicking on the <Icon icon="eye" /> icon next to the Chunk Utilization metric value in your *Retriever* nodes.

<img src="https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/chunk-relevance-explanation-luna.png?fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=ceb24bd84d09bd1dbecb17a6b7338051" data-og-width="1130" width="1130" data-og-height="842" height="842" data-path="images/chunk-relevance-explanation-luna.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/chunk-relevance-explanation-luna.png?w=280&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=dfb9bd2e810e3f28af2467ce06fb0c4a 280w, https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/chunk-relevance-explanation-luna.png?w=560&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=8e7c7bb7405d579fa61dd043dab647f1 560w, https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/chunk-relevance-explanation-luna.png?w=840&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=7fe7a9c331151d0fb900092fedce36bd 840w, https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/chunk-relevance-explanation-luna.png?w=1100&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=6f2f1d596a9248b5d6e561c32d23557a 1100w, https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/chunk-relevance-explanation-luna.png?w=1650&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=737d0ec9a47c04e3517a47cdc066895e 1650w, https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/chunk-relevance-explanation-luna.png?w=2500&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=0255a30b66d16128ad9e4825b1cb1229 2500w" />

***Calculation:*** Chunk Relevance Luna is computed using a fine-tuned in-house Galileo evaluation model. The model is a transformer-based encoder that is trained to identify the relevant and utilized information in the provided a query, context, and response. The same model is used to compute Chunk Adherence, Chunk Completeness, Chunk Attribution, and Utilization, and a single inference call is used to compute all the Luna metrics at once. The model is trained on carefully curated RAG datasets and optimized to closely align with the RAG Plus metrics.

For each token in the provided context, the model outputs a *relevance probability*, i.e the probability that this token is useful for answering the query.

***What to do when Chunk Relevance is low?***

Low Chunk Relevance scores indicate that your chunks are probably longer than they need to be. In this case, we recommend tuning your retriever to return shorter chunks, which will improve the efficiency of the system (lower cost and latency).
