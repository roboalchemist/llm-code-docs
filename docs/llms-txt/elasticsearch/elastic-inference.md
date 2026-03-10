# Source: https://www.elastic.co/docs/explore-analyze/elastic-inference

﻿---
title: Elastic Inference
description: Inference is a process of using a machine learning trained model to make predictions or operations - such as text embedding, or reranking - on your data...
url: https://www.elastic.co/docs/explore-analyze/elastic-inference
products:
  - Elastic Cloud Enterprise
  - Elastic Cloud Hosted
  - Elastic Cloud Serverless
  - Elastic Cloud on Kubernetes
  - Elastic Stack
  - Elasticsearch
  - Machine Learning
applies_to:
  - Elastic Cloud Serverless: Generally available
  - Elastic Stack: Generally available
---

# Elastic Inference
## Overview

Inference is a process of using a machine learning trained model to make predictions or operations - such as text embedding, or reranking - on your data.
You can use inference during ingest time (for example, to create embeddings from textual data you ingest) or search time (to perform [semantic search](https://www.elastic.co/docs/solutions/search/semantic-search) based on the embeddings created previously).
There are several ways to perform inference in the Elastic Stack, depending on the underlying inference infrastructure and the interface you use:
- **Inference infrastructure:**
  - [Elastic Inference Service](https://www.elastic.co/docs/explore-analyze/elastic-inference/eis): a managed service that runs inference outside your cluster resources.
- [Trained models deployed in your cluster](https://www.elastic.co/docs/explore-analyze/machine-learning/nlp/ml-nlp-overview): models run on your own machine learning nodes
- **Access methods:**
  - [The `semantic_text` workflow](https://www.elastic.co/docs/solutions/search/semantic-search/semantic-search-semantic-text): a simplified method that uses the inference API behind the scenes to enable semantic search.
- [The inference API](https://www.elastic.co/docs/explore-analyze/elastic-inference/inference-api): a general-purpose API that enables you to run inference using EIS, your own models, or third-party services.