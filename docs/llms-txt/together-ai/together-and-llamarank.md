# Source: https://docs.together.ai/docs/together-and-llamarank.md

# QuickStart: LlamaRank

> Try out Salesforce's LlamaRank exclusively on Together's Rerank API

The Together AI platform makes it easy to run state-of-the-art models using only a few lines of code. [LlamaRank](https://blog.salesforceairesearch.com/llamarank/) is a proprietary reranker model developed by Salesforce AI Research that has been shown to outperform competitive reranker models like Cohere Rerank v3 and Mistral-7B QLM on accuracy.

Reranker models **improve search relevancy** by reassessing and reordering a set of retrieved documents based on their relevance to a given query. It takes a `query` and a set of text inputs (called `documents`), and returns a relevancy score for each document relative to the given query. In RAG pipelines, the reranking step sits between the initial retrieval step and the final generation phase, enhancing the quality of information fed into language models.

Try out Salesforce's LlamaRank *exclusively* on Together's serverless Rerank API endpoint. Together's Rerank API is **Cohere compatible**, making it easy to integrate into your existing applications.

## Key specs of Together Rerank + LlamaRank

LlamaRank along with Together Rerank has the following key specs:

* Support for JSON and tabular data
* Long 8000 token context per document
* LlamaRank has been shown to outperform other models on accuracy for general docs and code.
* Compatible with Cohere's Rerank API
* Low latency for fast search queries
* Linear relevancy scores, making it easier to interpret

## Quickstart

### 1. Get your Together API key

First, [register for an account](https://api.together.ai/settings/api-keys?utm_source=docs\&utm_medium=quickstart\&utm_campaign=salesforce-llamarank) to get an API key.

Once you've registered, set your account's API key to an environment variable named `TOGETHER_API_KEY`:

```sh Shell theme={null}
export TOGETHER_API_KEY=xxxxx
```

### 2. Install your preferred library

Together provides an official library for Python:

```sh  theme={null}
pip install together --upgrade
```

As well as an official library for TypeScript/JavaScript:

```sh  theme={null}
npm install together-ai
```

You can also call our HTTP API directly using any language you like.

### 3. Run your first reranking query against LlamaRank

In the example below, we use the Rerank API endpoint to index the list of `documents` from most to least relevant to the query `What animals can I find near Peru?`.

```py Python theme={null}
from together import Together

client = Together()

query = "What animals can I find near Peru?"

documents = [
    "The giant panda (Ailuropoda melanoleuca), also known as the panda bear or simply panda, is a bear species endemic to China.",
    "The llama is a domesticated South American camelid, widely used as a meat and pack animal by Andean cultures since the pre-Columbian era.",
    "The wild Bactrian camel (Camelus ferus) is an endangered species of camel endemic to Northwest China and southwestern Mongolia.",
    "The guanaco is a camelid native to South America, closely related to the llama. Guanacos are one of two wild South American camelids; the other species is the vicuña, which lives at higher elevations.",
]

response = client.rerank.create(
    model="Salesforce/Llama-Rank-V1",
    query=query,
    documents=documents,
    top_n=2,
)

for result in response.results:
    print(f"Document Index: {result.index}")
    print(f"Document: {documents[result.index]}")
    print(f"Relevance Score: {result.relevance_score}")
```

In the example above, the documents being passed in are a list of strings, but Together's Rerank API also supports JSON data.

## Cohere Rerank compatibility

The Together Rerank endpoint is compatible with Cohere Rerank, making it easy to test out LlamaRank for your existing applications. Simply switch it out by updating the `URL`, `API key` and `model`.

```py Python theme={null}
import cohere

co = cohere.Client(
    base_url="https://api.together.xyz/v1",
    api_key=TOGETHER_API_KEY,
)
docs = [
    "Carson City is the capital city of the American state of Nevada.",
    "The Commonwealth of the Northern Mariana Islands is a group of islands in the Pacific Ocean. Its capital is Saipan.",
    "Capitalization or capitalisation in English grammar is the use of a capital letter at the start of a word. English usage varies from capitalization in other languages.",
    "Washington, D.C. (also known as simply Washington or D.C., and officially as the District of Columbia) is the capital of the United States. It is a federal district.",
    "Capital punishment (the death penalty) has existed in the United States since beforethe United States was a country. As of 2017, capital punishment is legal in 30 of the 50 states.",
]
response = co.rerank(
    model="Salesforce/Llama-Rank-V1",
    query="What is the capital of the United States?",
    documents=docs,
    top_n=3,
)
```

## Interpreting Results

LlamaRank produces linear and calibrated scores across all (doc, query) pairs, normalized on a scale of 0-1, making it easier to interpret relevancy scores:

* 0.9 — Highly Relevant
* 0.8 \~ 0.7 — Relevant
* 0.6 \~ 0.5 — Somewhat Relevant
* 0.4 \~ 0.3 — Marginally Relevant
* 0.2 \~ 0.1 — Slightly Relevant
* \~ 0.0 — Irrelevant

## Next steps

* Learn more about [reranking and Together's Rerank endpoint](/docs/rerank-overview)
* Get started by [signing up for a free together.ai account](https://api.together.ai/settings/api-keys?utm_source=docs\&utm_medium=quickstart\&utm_campaign=salesforce-llamarank), and get your API key.
* If you'd like to discuss your production reranking use case, [contact our sales team](https://www.together.ai/forms/contact-sales).
* Check out our [playground](https://api.together.ai/playground) to try out other models on the Together Platform for chat, images, languages or code.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.together.ai/llms.txt