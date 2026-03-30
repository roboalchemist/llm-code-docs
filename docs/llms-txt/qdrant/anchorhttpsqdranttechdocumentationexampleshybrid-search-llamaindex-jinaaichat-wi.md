# [Anchor](https://qdrant.tech/documentation/examples/hybrid-search-llamaindex-jinaai/\#chat-with-product-pdf-manuals-using-hybrid-search) Chat With Product PDF Manuals Using Hybrid Search

| Time: 120 min | Level: Advanced | Output: [GitHub](https://github.com/infoslack/qdrant-example/blob/main/HC-demo/HC-DO-LlamaIndex-Jina-v2.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://githubtocolab.com/infoslack/qdrant-example/blob/main/HC-demo/HC-DO-LlamaIndex-Jina-v2.ipynb) |
| --- | --- | --- | --- |

With the proliferation of digital manuals and the increasing demand for quick and accurate customer support, having a chatbot capable of efficiently parsing through complex PDF documents and delivering precise information can be a game-changer for any business.

In this tutorial, we’ll walk you through the process of building a RAG-based chatbot, designed specifically to assist users with understanding the operation of various household appliances.
We’ll cover the essential steps required to build your system, including data ingestion, natural language understanding, and response generation for customer support use cases.

## [Anchor](https://qdrant.tech/documentation/examples/hybrid-search-llamaindex-jinaai/\#components) Components

- **Embeddings:** Jina Embeddings, served via the [Jina Embeddings API](https://jina.ai/embeddings/#apiform)
- **Database:** [Qdrant Hybrid Cloud](https://qdrant.tech/documentation/hybrid-cloud/), deployed in a managed Kubernetes cluster on [DigitalOcean\\
(DOKS)](https://www.digitalocean.com/products/kubernetes)
- **LLM:** [Mixtral-8x7B-Instruct-v0.1](https://huggingface.co/mistralai/Mixtral-8x7B-Instruct-v0.1) language model on HuggingFace
- **Framework:** [LlamaIndex](https://www.llamaindex.ai/) for extended RAG functionality and [Hybrid Search support](https://docs.llamaindex.ai/en/stable/examples/vector_stores/qdrant_hybrid/).
- **Parser:** [LlamaParse](https://github.com/run-llama/llama_parse) as a way to parse complex documents with embedded objects such as tables and figures.

![Architecture diagram](https://qdrant.tech/documentation/examples/hybrid-search-llamaindex-jinaai/architecture-diagram.png)

### [Anchor](https://qdrant.tech/documentation/examples/hybrid-search-llamaindex-jinaai/\#procedure) Procedure

Retrieval Augmented Generation (RAG) combines search with language generation. An external information retrieval system is used to identify documents likely to provide information relevant to the user’s query. These documents, along with the user’s request, are then passed on to a text-generating language model, producing a natural response.

This method enables a language model to respond to questions and access information from a much larger set of documents than it could see otherwise. The language model only looks at a few relevant sections of the documents when generating responses, which also helps to reduce inexplicable errors.

## [Anchor](https://qdrant.tech/documentation/examples/hybrid-search-llamaindex-jinaai/\#heading)

[Service Managed Kubernetes](https://www.ovhcloud.com/en-in/public-cloud/kubernetes/), powered by OVH Public Cloud Instances, a leading European cloud provider. With OVHcloud Load Balancers and disks built in. OVHcloud Managed Kubernetes provides high availability, compliance, and CNCF conformance, allowing you to focus on your containerized software layers with total reversibility.

## [Anchor](https://qdrant.tech/documentation/examples/hybrid-search-llamaindex-jinaai/\#prerequisites) Prerequisites

### [Anchor](https://qdrant.tech/documentation/examples/hybrid-search-llamaindex-jinaai/\#deploying-qdrant-hybrid-cloud-on-digitalocean) Deploying Qdrant Hybrid Cloud on DigitalOcean

[DigitalOcean Kubernetes (DOKS)](https://www.digitalocean.com/products/kubernetes) is a managed Kubernetes service that lets you deploy Kubernetes clusters without the complexities of handling the control plane and containerized infrastructure. Clusters are compatible with standard Kubernetes toolchains and integrate natively with DigitalOcean Load Balancers and volumes.

1. To start using managed Kubernetes on DigitalOcean, follow the [platform-specific documentation](https://qdrant.tech/documentation/hybrid-cloud/platform-deployment-options/#digital-ocean).
2. Once your Kubernetes clusters are up, [you can begin deploying Qdrant Hybrid Cloud](https://qdrant.tech/documentation/hybrid-cloud/).
3. Once it’s deployed, you should have a running Qdrant cluster with an API key.

### [Anchor](https://qdrant.tech/documentation/examples/hybrid-search-llamaindex-jinaai/\#development-environment) Development environment

Then, install all dependencies:

```python
!pip install -U  \
    llama-index  \
    llama-parse \
    python-dotenv \
    llama-index-embeddings-jinaai  \
    llama-index-llms-huggingface  \
    llama-index-vector-stores-qdrant  \
    "huggingface_hub[inference]"  \
    datasets

```

Set up secret key values on `.env` file:

```bash
JINAAI_API_KEY
HF_INFERENCE_API_KEY
LLAMA_CLOUD_API_KEY
QDRANT_HOST
QDRANT_API_KEY

```

Load all environment variables:

```python
import os
from dotenv import load_dotenv
load_dotenv('./.env')

```

## [Anchor](https://qdrant.tech/documentation/examples/hybrid-search-llamaindex-jinaai/\#implementation) Implementation

### [Anchor](https://qdrant.tech/documentation/examples/hybrid-search-llamaindex-jinaai/\#connect-jina-embeddings-and-mixtral-llm) Connect Jina Embeddings and Mixtral LLM

LlamaIndex provides built-in support for the [Jina Embeddings API](https://jina.ai/embeddings/#apiform). To use it, you need to initialize the `JinaEmbedding` object with your API Key and model name.

For the LLM, you need wrap it in a subclass of `llama_index.llms.CustomLLM` to make it compatible with LlamaIndex.

```python