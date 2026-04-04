# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-guardrail-metrics/context-adherence/context-adherence-luna.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.galileo.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Context Adherence Luna

> Understand Galileo's Context Adherence Luna Metric

***Definition:*** Measures whether your model's response was purely based on the context provided.

***Calculation:*** Context Adherence Luna is computed using a fine-tuned in-house Galileo evaluation model. The model is a transformer-based encoder that predicts the probability of *Context Adherence* for an input response and context. The model is trained on carefully curated RAG datasets and optimized to mimic the Context Adherence Plus metric.

The same model is used to compute Chunk Adherence, Chunk Completeness, Chunk Attribution and Utilization, and a single inference call is used to compute all the Luna metrics at once.

#### Explainability

The *Luna* model identifies which parts of the response are not adhering to the context provided. These sections can be highlighted in the response by clicking on the <Icon icon="eye" /> icon next to the *Context Adherence* metric value in *LLM* or *Chat* nodes.

<img src="https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/context-adherence-explanation-luna.png?fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=98df6a04677de72c5b7947d00b648021" alt="" data-og-width="1218" width="1218" data-og-height="724" height="724" data-path="images/context-adherence-explanation-luna.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/context-adherence-explanation-luna.png?w=280&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=1cdfc1fae2c5e994fc54e487cc8741d7 280w, https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/context-adherence-explanation-luna.png?w=560&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=daf7457fb7b7bf4562118d76c2ec75c1 560w, https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/context-adherence-explanation-luna.png?w=840&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=3cf7c9313561ae30e73565a0e6c3800f 840w, https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/context-adherence-explanation-luna.png?w=1100&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=a9529f81c2c824d9c164059775526b44 1100w, https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/context-adherence-explanation-luna.png?w=1650&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=7f65eefedf00d8d63500db6ae6a0efd1 1650w, https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/context-adherence-explanation-luna.png?w=2500&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=d291ce6507f5c1b6a7bcebe2d6197751 2500w" />

#### *What to Do When Context Adherence Is Low?*

When a response is highly adherent to the context (i.e., it has a value of 1 or close to 1), it strictly includes information from the provided context. However, when a response is not adherent (i.e., it has a value of 0 or close to 0), it likely contains facts not present in the given context.

Several factors can contribute to low context adherence:

1. **Insufficient Context**: If the source document lacks key information needed to answer the user's question, the response may be incomplete or off-topic. To address this, users should consider using various context enrichment strategies to ensure that the source documents retrieved contain the necessary information to answer the user's questions effectively.

2. **Lack of Internal Reasoning and Creativity**: While Retrieval-Augmented Generation (RAG) focuses on factual grounding, it doesn't directly enhance the internal reasoning processes of the LLM. This limitation can cause the model to struggle with logic or common-sense reasoning, potentially resulting in nonsensical outputs even if the facts are accurate.

3. **Lack of Contextual Awareness**: Although RAG provides factual grounding for the language model, it might not fully understand the nuances of the prompt or user intent. This can lead to the model incorporating irrelevant information or missing key points, thus affecting the overall quality of the response.

To improve context adherence, we recommend:

1. Ensuring your context DB has all the necessary info to answer the question

2. Adjusting the prompt to tell the model to stick to the information it's given in the context.
