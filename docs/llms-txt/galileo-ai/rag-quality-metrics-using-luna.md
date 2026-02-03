# Source: https://docs.galileo.ai/galileo-ai-research/rag-quality-metrics-using-luna.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.galileo.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Rag Quality Metrics Using Luna

> This page provides a brief overview of the research behind Galileo's RAG Quality Metrics.

## Metrics

### Chunk-level metrics: Chunk Relevance, Chunk Attribution and Chunk Utilization

These metrics evaluate individual chunks retrieved by a RAG system, in light of the question and the response written by the system.

* [Chunk Relevance](/galileo/gen-ai-studio-products/galileo-guardrail-metrics/chunk-relevance). For each chunk retrieved in a RAG pipeline, Chunk Relevance measures the fraction of the text in that chunk that is levant to the query.

* [Chunk Utilization](/galileo/gen-ai-studio-products/galileo-guardrail-metrics/context-adherence/context-adherence-luna). For each chunk retrieved in a RAG pipeline, Chunk Utilization measures the fraction of the text in that chunk that had an impact on the model's response.

* [Chunk Attribution](/galileo/gen-ai-studio-products/galileo-guardrail-metrics/context-adherence/context-adherence-luna). For each chunk retrieved in a RAG pipeline, Chunk Attribution measures whether or not that chunk had an effect on the model's response.

### Response-level metrics: Context Adherence and Completeness

These metrics capture different facets of RAG response quality. Both involve assessing the relationship between the response, the retrieved context, and the query that the RAG system is responding to.

* [Context Adherence](/galileo/gen-ai-studio-products/galileo-guardrail-metrics/context-adherence/context-adherence-luna). Measures whether your model's response was purely based on the context provided.

* [Completeness](/galileo/gen-ai-studio-products/galileo-guardrail-metrics/completeness/completeness-luna). Measures how thoroughly your model's response covered the relevant information available in the context provided.

## Luna Model

For a comprehensive look at the in-house model we built to predict RAG Quality metrics check out our research paper [Luna: An Evaluation Foundation Model to Catch Language Model Hallucinations with High Accuracy and Low Cost](https://arxiv.org/abs/2406.00975)

Luna is a DeBERTa-large encoder that has been fine-tuned to predict RAG Quality metrics from input RAG context chunk(s), a user query, and an LLM response. Luna model predicts three sets of token-level probabilities:

* Adherence probability on every token in the response.

* Relevance probability on every token of the context.

* Utilization probability on every token of the context.

RAG quality metrics are derived from the output token probabilities as illustrated in the Figure below.

<Frame>
  <img src="https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/rag-luna-1.png?fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=958e543d626b89eaba57b252469e8e67" data-og-width="825" width="825" data-og-height="732" height="732" data-path="images/rag-luna-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/rag-luna-1.png?w=280&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=825ee1f9d4920a5f709878a4c8988df6 280w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/rag-luna-1.png?w=560&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=894ee51316c8e70caeccb7e56fcb6955 560w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/rag-luna-1.png?w=840&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=18e342410b7f5e3d4ad020830e33e81b 840w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/rag-luna-1.png?w=1100&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=b3624f9a7ccae3d19233bf56b61cf606 1100w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/rag-luna-1.png?w=1650&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=97082198a42e4dbd7bf14144c35ce32c 1650w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/rag-luna-1.png?w=2500&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=c66ac9cc76a45d774bdaed0466061889 2500w" />
</Frame>

The example in the Figure above returns

* High Chunk Relevance because the retrieved chunk is, for the most part, relevant to the input query.

* Attributed because the response uses the information in the chunk.

* Low Chunk Utilization because the response only utilizes a fraction of the information provided in the chunk.

* Low Completeness because the response utilizes \~55% of the relevant information in the retrieved chunk.

* Low Adherence because the response partially contradicts the information provided in the chunk, claiming that it is not possible to determine the numbed of football clubs in England, while the context chunk indicates otherwise.

## Luna Performance

Luna has been trained and evaluated on a broad range of domains and RAG task-types. Here is how it performs on these evaluation metrics:

* For Adherence (Adh) we measure **AUROC: Area Under Receiver Operator Characteristic curve**. Measures how well the model detects non-adherent responses (hallucinations), balancing the weight of False Negative and False Positive predictions. Range \[0-1], higher is better.

* For Relevance (Rel) and Utilization(Util) we measure **RMSE: Root Mean Squared Error**. Measures model's Chunk Relevance and Chunk Utilization proximity to ground truth. Range \[0-1], lower is better.

<Frame>
  <img src="https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/rag-luna-2.png?fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=6e14272cdee8d9fad99545cb44da1fe4" data-og-width="1044" width="1044" data-og-height="270" height="270" data-path="images/rag-luna-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/rag-luna-2.png?w=280&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=284e4e69769fbf740d613512b55fde16 280w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/rag-luna-2.png?w=560&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=48b5d25016524b42b93a165736bd2286 560w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/rag-luna-2.png?w=840&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=2a68db5f476ae9453a573bdc3ba4302a 840w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/rag-luna-2.png?w=1100&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=2313401678ba2486ccacb891e427d85b 1100w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/rag-luna-2.png?w=1650&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=a2c93cc7bc8348888c0b8069611ec68a 1650w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/rag-luna-2.png?w=2500&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=f69880d07b96dfacfea6dd6eb6e30e7a 2500w" />
</Frame>
