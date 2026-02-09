# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-guardrail-metrics/chunk-utilization/chunk-utilization-luna.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.galileo.ai/llms.txt
> Use this file to discover all available pages before exploring further.

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

<img src="https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/chunk-utilization-explanation-luna.png?fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=14a3805062917a39bac7c4daf093cd55" alt="" data-og-width="1218" width="1218" data-og-height="912" height="912" data-path="images/chunk-utilization-explanation-luna.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/chunk-utilization-explanation-luna.png?w=280&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=4a5d788f65470a8b156d059f03a38144 280w, https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/chunk-utilization-explanation-luna.png?w=560&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=f865020d8c4c3f09b0628540f64ea46c 560w, https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/chunk-utilization-explanation-luna.png?w=840&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=d64230886dfd29686496794226e993e1 840w, https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/chunk-utilization-explanation-luna.png?w=1100&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=63f4b5687c283f1ee420e93c44fbf2c7 1100w, https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/chunk-utilization-explanation-luna.png?w=1650&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=6bb5fab455033116ddeb255cd9941fb3 1650w, https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/chunk-utilization-explanation-luna.png?w=2500&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=d0c8fa5b4ed2b433192395810610ec6d 2500w" />
