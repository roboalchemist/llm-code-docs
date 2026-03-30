# Source: https://code.kx.com/kdbai/latest/use/rerank.html

Title: Rerank in KDB.AI - KDB.AI Documentation

URL Source: https://code.kx.com/kdbai/latest/use/rerank.html

Markdown Content:
How to Use Rerankers in KDB.AI: Cohere, Jina AI, and Voyage AI
--------------------------------------------------------------

_This page provides details on how to improve your search results with Cohere, Jina AI, and Voyage AI rerankers in KDB.AI._

KDB.AI allows you to enhance the relevance and personalization of search results through the integration of Cohere, Voyage AI, and Jina AI rerankers. Integrating rerankers in KDB.AI involves a few steps to set up your environment, prepare your data, and configure the reranking process. Here’s a general guide to follow:

Get started
-----------

Before you begin, make sure you have the following:

*   Installed [Python 3](https://www.python.org/downloads) (versions 3.9 to 3.13), [Pip](https://pip.pypa.io/en/stable/installation/), and [Git](https://git-scm.com/downloads)
*   Active KDB.AI [Server](https://kx.com/kdb-ai-server-download/) license
*   Valid API keys for Cohere, Jina AI, or/and Voyage AI.
*   Basic knowledge of working with [vector databases](https://kdb.ai/learning-hub/articles/vector-database-101/) and [embedding models](https://kdb.ai/learning-hub/articles/vector-embeddings/)
*   Necessary configurations for interacting with KDB.AI [Server](https://code.kx.com/kdbai/latest/gettingStarted/kdb-ai-server-setup.html)

Environment variables you need

KDB.AI Cohere/JinaAI/VoyageAI

*   `KDBAI_ENDPOINT` - The endpoint URL for your KDB.AI instance, represented by `--endpoint` (CLI) or `endpoint` (Python).
*   `KDBAI_API_KEY` - The KDB.AI API key, represented by `--api-key` (CLI) or `api_key` (Python).

*   `COHERE_API_KEY`
*   `VOYAGEAI_API_KEY`
*   `JINAAI_API_KEY`

Choose a reranker
-----------------

Use one reranker at a time (or multiple within the same notebook), depending on your use case. Check out the comparison table below to decide which reranker is suitable for you:

| **Criteria** | **Cohere** | **Jina AI** | **Voyage AI** |
| --- | --- | --- | --- |
| **Best For** | Enterprise applications needing high accuracy and efficiency in retrieval | Multimodal data applications requiring robust search and retrieval | Industry-specific data like finance, legal, and code with high-retrieval accuracy |
| **Key Features** | - High-performing embedding models - Advanced retrieval models - Flexible deployment options | - Multimodal embeddings - Neural retrievers - Easy integration with cloud-native stack | - Optimized for domain-specific data - Fine-tuned models - Cost-effective vector search |
| **Deployment Options** | Cloud or on-premises | Cloud-native, supports gRPC, HTTP, WebSockets | SaaS and customer tenant deployment (in-VPC) |
| **Performance** | High accuracy and efficiency | High performance with support for various data types | Superior accuracy with smaller model size and faster inference |
| **Integration** | Seamless integration with enterprise data sources | Smooth Pythonic experience, supports Docker and Kubernetes | Easy integration with existing stacks, supports major clouds and data platforms |
| **Use Cases** | - Generative AI applications - Search and discovery - Advanced retrieval | - Multimodal AI applications - Embedding services - Tokenization | - Legal AI solutions - Code retrieval - Financial data analysis |

Choose the reranking model
--------------------------

Different rerankers provide different models. Each reranker has a default model. `model` determines the [rerank model](https://code.kx.com/kdbai/latest/reference/reranking.html#reranker-models). With `Cohere` you can even [create your own model](https://docs.cohere.com/docs/rerank-starting-the-training).

Cohere Jina AI Voyage AI

```
reranker = CohereReranker(api_key='COHERE_API_KEY', model='rerank-english-v3.0')
```

```
reranker = JinaAIReranker(api_key='JINAAI_API_KEY', model='jina-reranker-v2-base-multilingual')
```

```
reranker = VoyageAIReranker(api_key='VOYAGEAI_API_KEY', model='rerank-2')
```

Reranker set up
---------------

### Install dependencies

Use OpenAI to embed the data and queries, and Langchain to chunk the data.

```
!pip install langchain
!pip install openai
```

### Import dependencies

```
import os
import numpy as np
import pandas as pd
import langchain
import openai
from langchain_text_splitters import RecursiveCharacterTextSplitter
from openai import OpenAI
import kdbai_client as kdbai 

os.environ["OPENAI_API_KEY"] = "OPENAI_API_KEY"
```

### Set up your KDB.AI database

```
session = kdbai.Session(endpoint='http://localhost:8082')

schema = [
    {'name': 'id', 'type': 'int16'},
    {'name': 'content', 'type': 'str'},
    {'name': 'embeddings', 'type': 'float64s'}
]

indexes = [
    {'type': 'flat', 'name': 'flat', 'column': 'embeddings',  'params': {'dims': 1536}},
    {'type': 'hnsw', 'name': 'fast_hnsw', 'column': 'embeddings', 'params': {'dims': 1536,'M': 8, 'efConstruction': 8}},
    {'type': 'hnsw', 'name': 'accurate_hnsw','column': 'embeddings', 'params': {'dims': 1536,'M': 64, 'efConstruction':256}} 
]

database = session.database('rerank')

table = database.create_table('rerank', schema=schema, indexes=indexes)
```

### Prepare your data

`data` refers to any type of data you want to use. Below is an example of how to prepare data before inserting it to your KDB.AI database.

```
client = OpenAI()

def get_data_chunks(data: str) -> list[str]:
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=384,
        chunk_overlap=20,
        length_function=len,
        is_separator_regex=False,
    )
    texts = text_splitter.create_documents([data])
    return texts

def get_embedding(text, model):
    text = text.replace("\n", " ")
    return client.embeddings.create(input=[text], model=model).data[0].embedding

df = pd.DataFrame(columns = ["id", "content", "embeddings"])

data_chunks = get_data_chunks(data)

for num, data_chunk in enumerate(data_chunks):
    text = data_chunk.page_content
    text_embeddings = get_embedding(text, model='text-embedding-3-small')
    df.loc[len(df), :] = (num, text, text_embeddings)

table.insert(df)
```

### Execute search and rerank

```
query1 = 'What are the key things president delivered in the speech?'
query2 = 'What did president say about inflation?'

query1_embeddings = get_embedding(query1, model='text-embedding-3-small')
query2_embeddings = get_embedding(query2, model='text-embedding-3-small')

from kdbai_client.rerankers import CohereReranker

reranker = CohereReranker(api_key='COHERE_API_KEY')

table.search_and_rerank(vectors={"flat": [query1_embeddings, query2_embeddings]}, n=3, reranker=reranker, queries=[query1, query2], text_column='content')
```

Fine tune the reranker
----------------------

### Choose the number of documents to rerank

The `overfetch_factor` value determines how many documents are processed by the reranker. The `overfetch_factor` is multiplied by `n` (nearest neighbors). By default, the `overfetch_factor` is `2`, so if `n` is `3`, the amount of documents processed by the reranker is `6`. You only get `n` results returned. To further fine tune the results, adjust the `overfetch_factor`.

Cohere Jina AI Voyage AI

```
reranker = CohereReranker(api_key='COHERE_API_KEY', overfetch_factor=4)
```

```
reranker = JinaAIReranker(api_key='JINAAI_API_KEY', overfetch_factor=4)
```

```
reranker = VoyageAIReranker(api_key='VOYAGEAI_API_KEY', overfetch_factor=4)
```

If you need help with the integration of Cohere, Jina AI, and Voyage AI rerankers within KDB.AI, feel free to reach out to the KDB.AI [Slack community](http://kx.com/slack) or email [support@kdb.ai](mailto:support@kdb.ai).

Next steps
----------

Now that you're familiar with reranking, try the following:

*   Head to the [Reranking with Cohere](https://docs.cohere.com/v2/docs/reranking-with-cohere) docs.
*   Read our Jina AI-related blog article [The end of high dimensions](https://kx.com/blog/end-high-dimensions-ai-search/) to discover how Matryoshka learning is revolutionizing AI search forever.
