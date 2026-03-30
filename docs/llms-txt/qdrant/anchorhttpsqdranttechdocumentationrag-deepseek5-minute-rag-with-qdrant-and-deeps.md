# [Anchor](https://qdrant.tech/documentation/rag-deepseek/\#5-minute-rag-with-qdrant-and-deepseek) 5 Minute RAG with Qdrant and DeepSeek

| Time: 5 min | Level: Beginner | Output: [GitHub](https://github.com/qdrant/examples/blob/master/rag-with-qdrant-deepseek/deepseek-qdrant.ipynb) |  |
| --- | --- | --- | --- |

This tutorial demonstrates how to build a **Retrieval-Augmented Generation (RAG)** pipeline using Qdrant as a vector storage solution and DeepSeek for semantic query enrichment. RAG pipelines enhance Large Language Model (LLM) responses by providing contextually relevant data.

## [Anchor](https://qdrant.tech/documentation/rag-deepseek/\#overview) Overview

In this tutorial, we will:

1. Take sample text and turn it into vectors with FastEmbed.
2. Send the vectors to a Qdrant collection.
3. Connect Qdrant and DeepSeek into a minimal RAG pipeline.
4. Ask DeepSeek different questions and test answer accuracy.
5. Enrich DeepSeek prompts with content retrieved from Qdrant.
6. Evaluate answer accuracy before and after.

#### [Anchor](https://qdrant.tech/documentation/rag-deepseek/\#architecture) Architecture:

![deepseek-rag-architecture](https://qdrant.tech/documentation/examples/rag-deepseek/architecture.png)

* * *

## [Anchor](https://qdrant.tech/documentation/rag-deepseek/\#prerequisites) Prerequisites

Ensure you have the following:

- Python environment (3.9+)
- Access to [Qdrant Cloud](https://qdrant.tech/)
- A DeepSeek API key from [DeepSeek Platform](https://platform.deepseek.com/api_keys)

## [Anchor](https://qdrant.tech/documentation/rag-deepseek/\#setup-qdrant) Setup Qdrant

```python
pip install "qdrant-client[fastembed]>=1.14.1"

```

[Qdrant](https://qdrant.tech/) will act as a knowledge base providing the context information for the prompts we’ll be sending to the LLM.

You can get a free-forever Qdrant cloud instance at [http://cloud.qdrant.io](http://cloud.qdrant.io/). Learn about setting up your instance from the [Quickstart](https://qdrant.tech/documentation/quickstart-cloud/).

```python
QDRANT_URL = "https://xyz-example.eu-central.aws.cloud.qdrant.io:6333"
QDRANT_API_KEY = "<your-api-key>"

```

### [Anchor](https://qdrant.tech/documentation/rag-deepseek/\#instantiating-qdrant-client) Instantiating Qdrant Client

```python
from qdrant_client import QdrantClient, models

client = QdrantClient(url=QDRANT_URL, api_key=QDRANT_API_KEY)

```

### [Anchor](https://qdrant.tech/documentation/rag-deepseek/\#building-the-knowledge-base) Building the knowledge base

Qdrant will use vector embeddings of our facts to enrich the original prompt with some context. Thus, we need to store the vector embeddings and the facts used to generate them.

We’ll be using the [bge-base-en-v1.5](https://huggingface.co/BAAI/bge-small-en-v1.5) model via [FastEmbed](https://github.com/qdrant/fastembed/) \- A lightweight, fast, Python library for embeddings generation.

The Qdrant client provides a handy integration with FastEmbed that makes building a knowledge base very straighforward.

First, we need to create a collection, so Qdrant would know what vectors it will be dealing with, and then, we just pass our raw documents
wrapped into `models.Document` to compute and upload the embeddings.

pythonpython

```python
collection_name = "knowledge_base"
model_name = "BAAI/bge-small-en-v1.5"
client.create_collection(
    collection_name=collection_name,
    vectors_config=models.VectorParams(size=384, distance=models.Distance.COSINE)
)

```

```python
documents = [\
    "Qdrant is a vector database & vector similarity search engine. It deploys as an API service providing search for the nearest high-dimensional vectors. With Qdrant, embeddings or neural network encoders can be turned into full-fledged applications for matching, searching, recommending, and much more!",\
    "Docker helps developers build, share, and run applications anywhere — without tedious environment configuration or management.",\
    "PyTorch is a machine learning framework based on the Torch library, used for applications such as computer vision and natural language processing.",\
    "MySQL is an open-source relational database management system (RDBMS). A relational database organizes data into one or more data tables in which data may be related to each other; these relations help structure the data. SQL is a language that programmers use to create, modify and extract data from the relational database, as well as control user access to the database.",\
    "NGINX is a free, open-source, high-performance HTTP server and reverse proxy, as well as an IMAP/POP3 proxy server. NGINX is known for its high performance, stability, rich feature set, simple configuration, and low resource consumption.",\
    "FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints.",\
    "SentenceTransformers is a Python framework for state-of-the-art sentence, text and image embeddings. You can use this framework to compute sentence / text embeddings for more than 100 languages. These embeddings can then be compared e.g. with cosine-similarity to find sentences with a similar meaning. This can be useful for semantic textual similar, semantic search, or paraphrase mining.",\
    "The cron command-line utility is a job scheduler on Unix-like operating systems. Users who set up and maintain software environments use cron to schedule jobs (commands or shell scripts), also known as cron jobs, to run periodically at fixed times, dates, or intervals.",\
]
client.upsert(
    collection_name=collection_name,
    points=[\
        models.PointStruct(\
            id=idx,\
            vector=models.Document(text=document, model=model_name),\
            payload={"document": document},\
        )\
        for idx, document in enumerate(documents)\
    ],
)

```

## [Anchor](https://qdrant.tech/documentation/rag-deepseek/\#setup-deepseek) Setup DeepSeek

RAG changes the way we interact with Large Language Models. We’re converting a knowledge-oriented task, in which the model may create a counterfactual answer, into a language-oriented task. The latter expects the model to extract meaningful information and generate an answer. LLMs, when implemented correctly, are supposed to be carrying out language-oriented tasks.

The task starts with the original prompt sent by the user. The same prompt is then vectorized and used as a search query for the most relevant facts. Those facts are combined with the original prompt to build a longer prompt containing more information.

But let’s start simply by asking our question directly.

```python
prompt = """
What tools should I need to use to build a web service using vector embeddings for search?
"""

```

Using the Deepseek API requires providing the API key. You can obtain it from the [DeepSeek platform](https://platform.deepseek.com/api_keys).

Now we can finally call the completion API.

```python
import requests
import json