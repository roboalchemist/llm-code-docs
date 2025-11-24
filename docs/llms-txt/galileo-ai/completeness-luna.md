# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-guardrail-metrics/completeness/completeness-luna.md

# Completeness Luna

> Understand Galileo's Completeness Luna Metric

The metric is mainly intended for RAG workflows.

***Definition:*** Measures how thoroughly your model's response covered the relevant information available in the context provided.

***Calculation:*** Completeness Luna is computed using a fine-tuned in-house Galileo evaluation model. The model is a transformer-based encoder that is trained to identify the relevant and utilized information in the provided a query, context, and response. The same model is used to compute Chunk Adherence, Chunk Completeness, Chunk Attribution, and Utilization, and a single inference call is used to compute all the Luna metrics at once. The model is trained on carefully curated RAG datasets and optimized to closely align with the RAG Plus metrics.

For each token in the provided context, the model outputs a *relevance probability* and *utilization probability. Relevance probability* measures the extent to which the token is useful for answering the provided query. *Utilization probability measures the extent to which* the token affected the response.

Chunk Completeness is derived from relevance and utilization probabilities as the fraction of relevant AND utilized tokens out of all relevant tokens.

<Info>
  We recommend starting with "Luna" and seeing if this covers your needs. If you see the need for higher accuracy or would like explanations for the ratings, you can switch over to [Completeness
  Plus](/galileo/gen-ai-studio-products/galileo-guardrail-metrics/completeness/completeness-plus).
</Info>
