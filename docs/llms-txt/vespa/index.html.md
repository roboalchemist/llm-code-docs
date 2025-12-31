# Source: https://docs.vespa.ai/index.html.md

# Source: https://docs.vespa.ai/en/performance/index.html.md

# Source: https://docs.vespa.ai/en/learn/tutorials/index.html.md

# Source: https://docs.vespa.ai/index.html.md

# Source: https://docs.vespa.ai/en/performance/index.html.md

# Source: https://docs.vespa.ai/en/learn/tutorials/index.html.md

# Source: https://docs.vespa.ai/index.html.md

# Source: https://docs.vespa.ai/en/performance/index.html.md

# Source: https://docs.vespa.ai/en/learn/tutorials/index.html.md

# Tutorials and use cases

 

### Text search

- [Tutorial: Text Search](text-search). A text search tutorial and introduction to text ranking with Vespa using traditional information retrieval techniques like BM25. 
- [Tutorial: Improving Text Search with Machine Learning](text-search-ml). This tutorial builds on the text search tutorial but introduces Learning to Rank to improve relevance. 

### Vector Search

Learn how to use Vespa Vector Search in the [practical nearest neighbor search guide](../../querying/nearest-neighbor-search-guide). It uses Vespa's support for [nearest neighbor search](../../querying/nearest-neighbor-search), there is also support for fast [approximate nearest neighbor search](../../querying/approximate-nn-hnsw) in Vespa. The guide covers combining vector search with filters and how to perform hybrid search, combining retrieval over inverted index structures with vector search.

### Hybrid Search

[Tutorial: Hybrid Text Search](hybrid-search). A search tutorial and introduction to hybrid text ranking with Vespa, combining BM25 with text embedding models.

### RAG (Retrieval-Augmented Generation)

- [Tutorial: The RAG Blueprint](rag-blueprint). A tutorial that provides a blueprint for building high-quality RAG applications with Vespa. Includes evaluation and learning-to-rank (LTR). 
- [Retrieval-augmented generation (RAG) in Vespa](../../rag/rag). 

### Combining search and recommendation: The News tutorial

Follow this series to learn how to build a complete application supporting both content recommendation/personalization, navigation, and search.

- [News 1: Getting Started](news-1-deploy-an-application)
- [News 2: Application Packages, Feeding, Query](news-2-basic-feeding-and-query)
- [News 3: Sorting, Grouping and Ranking](news-3-searching)
- [News 4: Embeddings](news-4-embeddings)
- [News 5: Partial Updates, ANNs, Filtering](news-5-recommendation)
- [News 6: Custom Searchers, Document Processors](news-6-recommendation-with-searchers)
- [News 7: Parent-Child, Tensor Ranking](news-7-recommendation-with-parent-child)

### ML Model Serving

Learn how to use Vespa for ML model serving in [Stateless Model Evaluation](../../ranking/stateless-model-evaluation.html). Vespa supports running inference with models from many popular ML frameworks, which can be used for ranking, query classification, question answering, multi-modal retrieval, and more.

- [Ranking with ONNX models](../../ranking/onnx). Export models from popular deep learning frameworks such as [PyTorch](https://pytorch.org/docs/stable/onnx.html) to [ONNX](https://onnx.ai/) format for serving in Vespa. Vespa integrates with [ONNX-Runtime](https://blog.vespa.ai/stateful-model-serving-how-we-accelerate-inference-using-onnx-runtime/) for [accelerated inference](https://blog.vespa.ai/stateless-model-evaluation/). Many ML frameworks support exporting models to ONNX, including [sklearn](http://onnx.ai/sklearn-onnx/). 
- [Ranking with LightGBM models](../../ranking/lightgbm)
- [Ranking with XGBoost models](../../ranking/xgboost)
- [Ranking with TensorFlow models](../../ranking/tensorflow)

### Embedding Model Inference

Vespa supports integrating [embedding](../../rag/embedding.html) models, which avoids transferring large amounts of embedding vector data over the network and allows for efficient serving of embedding models.

- [Huggingface Embedder](../../rag/embedding.html#huggingface-embedder) Use single-vector embedding models from Hugging face
- [ColBERT Embedder](../../rag/embedding.html#colbert-embedder) Use multi-vector embedding models 
- [Splade Embedder](../../rag/embedding.html#splade-embedder) Use sparse learned single vector embedding models

### E-Commerce

The [e-commerce shopping sample application](e-commerce) demonstrates Vespa grouping, true in-place partial updates, custom ranking, and more.

### Building a custom HTTP API

The [HTTP API tutorial](http-api.html) shows how to build a custom HTTP API in an application.

### More examples and sample applications

There are many examples and starting applications on[GitHub](https://github.com/vespa-engine/sample-apps/)and [Pyvespa examples](https://vespa-engine.github.io/pyvespa/index.html).

 Copyright © 2025 - [Cookie Preferences](#)

### On this page:

- [Text search](#)
- [Vector Search](#)
- [Hybrid Search](#)
- [RAG (Retrieval-Augmented Generation)](#)
- [Combining search and recommendation: The News tutorial](#)
- [ML Model Serving](#)
- [Embedding Model Inference](#)
- [E-Commerce](#)
- [Building a custom HTTP API](#)
- [More examples and sample applications](#)

