# Source: https://docs.voyageai.com/docs/introduction

## GET STARTED 

- [[[Introduction]]](/docs/introduction)
- [[[API Key and Python Client]]](/docs/api-key-and-installation)
- [[[Quickstart Tutorial]]](/docs/quickstart-tutorial)

## CAPABILITIES 

- [[[Text Embeddings]]](/docs/embeddings)
- [[[Contextualized Chunk Embeddings]]](/docs/contextualized-chunk-embeddings)
- [[[Multimodal Embeddings]]](/docs/multimodal-embeddings)
- [[[Rerankers]]](/docs/reranker)

## GUIDES 

- [[[Tokenization]]](/docs/tokenization)
- [[[Flexible Dimensions and Quantization]]](/docs/flexible-dimensions-and-quantization)
- [[[Batch Inference]]](/docs/batch-inference)
- [[[Error Codes]]](/docs/error-codes)
- [[[Rate Limits]]](/docs/rate-limits)
- [[[Pricing]]](/docs/pricing)
- [[[Organizations and Projects]]](/docs/organizations-and-projects)
- [[[Service Level Objectives]]](/docs/service-level-objectives)

## DEPLOYMENT ON VPC 

- [[AWS Marketplace Model Package]]
  - [[[MongoDB Voyage AI Models in AWS]]](/docs/aws-marketplace-mongodb-voyage)
  - [[[Voyage AI Models in AWS]]](/docs/aws-marketplace-voyage)
- [[Azure Marketplace Managed Application]]
  - [[[MongoDB Voyage AI Models in Azure]]](/docs/azure-marketplace-mongodb-voyage)
  - [[[Voyage AI Models in Azure]]](/docs/azure-marketplace-voyage)

## ACCESS VIA DATA PLATFORMS 

- [[[Snowflake]]](/docs/snowflake)

## Community 

- [[[Integrations]]](/docs/integrations-and-other-libraries)
- [[[Community SDKs]]](/docs/community-sdks)

## HELP 

- [[[FAQ]]](/docs/faq)
- [[[Contact Email]]](/docs/contact-email)
- [[[Discord]]](/docs/discord)

Powered by [](https://readme.com?ref_src=hub&project=voyage-ai)

# Introduction

Voyage AI provides cutting-edge embedding and rerankers.

Embedding models are neural net models (e.g., transformers) that convert unstructured and complex data, such as documents, images, audios, videos, or tabular data, into dense numerical vectors (i.e. embeddings) that capture their semantic meanings. These vectors serve as representations/indices for datapoints and are essential building blocks for semantic search and retrieval-augmented generation (RAG), which is the predominant approach for domain-specific or company-specific chatbots and other AI applications.

Rerankers are neural nets that output relevance scores between a query and multiple documents. It is common practice to use the relevance scores to rerank the documents initially retrieved with embedding-based methods (or with lexical search algorithms such as [BM25](https://en.wikipedia.org/wiki/Okapi_BM25) and [TF-IDF](https://en.wikipedia.org/wiki/Tf–idf)). Selecting the highest-scored documents refines the retrieval results into a more relevant subset.

Voyage AI provides API endpoints for embedding and reranking models that take in your data (e.g., documents, queries, or query-document pairs) and return their embeddings or relevance scores. Embedding models and rerankers, as modular components, seamlessly integrate with other parts of a RAG stack, including vector stores and generative Large Language Models (LLMs).

Voyage AI's embedding models and rerankers are **state-of-the-art** in retrieval accuracy. Please read our announcing [blog post](https://blog.voyageai.com/2023/10/29/voyage-embeddings/) for details. Please also check out a high-level [introduction](https://www.mongodb.com/resources/basics/artificial-intelligence/retrieval-augmented-generation) of embedding models, semantic search, and RAG, and our step-by-step [quickstart tutorial](/docs/quickstart-tutorial) on implementing a minimalist RAG chatbot using Voyage model endpoints.

Updated 24 days ago

------------------------------------------------------------------------

[](/docs/api-key-and-installation)

API Key and Python Client

[]