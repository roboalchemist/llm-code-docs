# Source: https://docs-v3.activeloop.ai/v3.4.1/tutorials/vector-store/vector-search-using-the-deep-lake-managed-database.md

# Vector Search Using the Deep Lake Tensor Database

## How to Run Vector Search in the Deep Lake Tensor Database

{% hint style="danger" %}
The REST API is currently in Alpha, and the syntax may change without announcement.
{% endhint %}

Deep Lake offers a [Managed Tensor Database](https://docs-v3.activeloop.ai/v3.4.1/enterprise-features/managed-database) for querying datasets, including vector search. The database is serverless, which simplifies self-hosting and substantially lowers costs. This tutorial demonstrates how to execute embedding search on a Deep Lake dataset using the REST API for the Tensor Database.

### Creating the Dataset

A Deep Lake dataset containing embeddings can be created using a variety of APIs, [including Deep Lake's LangChain integration](https://docs-v3.activeloop.ai/v3.4.1/tutorials/vector-store/deep-lake-vector-store-in-langchain).&#x20;

{% hint style="danger" %}
**Most importantly**, when a dataset is stored in the Deep Lake Managed Tensor Database, the dataset `dataset_path` and `runtime` must be specified accordingly:
{% endhint %}

```python
dataset_path = "hub://<org_id>/<dataset_name>"
runtime = {"db_engine": True}

# from langchain.vectorstores import DeepLake
# db = DeepLake.from_documents(texts, embeddings, dataset_path=dataset_path, runtime = runtime)
```

**In this tutorial, the dataset has already been created** [**can be found here**](https://app.activeloop.ai/activeloop/twitter-algorithm)**.**

### Performing Vector Search

Let's query our dataset stored in the Managed Tensor Database using the [REST API](https://docs-v3.activeloop.ai/v3.4.1/enterprise-features/managed-database/rest-api). The steps are:

1. Define the authentication tokens and search terms
2. Embed the search search term using OpenAI
3. Reformat the embedding to an `embedding_search` string that can be passed to the REST API request.
4. Create the query string using [Deep Lake TQL](https://docs-v3.activeloop.ai/v3.4.1/enterprise-features/compute-engine/querying-datasets/query-syntax). The `dataset_path` and `embedding_search` are a part of the query string. &#x20;
5. Submit the request and print the response data data

{% tabs %}
{% tab title="Python" %}

```python
import requests
import openai
import os

# Tokens should be set in environmental variables.
ACTIVELOOP_TOKEN = os.environ['ACTIVELOOP_TOKEN']
DATASET_PATH = 'hub://activeloop/twitter-algorithm'
ENDPOINT_URL = 'https://app.activeloop.ai/api/query/v1'
SEARCH_TERM = 'What do the trust and safety models do?'
# os.environ['OPENAI_API_KEY'] OPEN AI TOKEN should also exist in env variables

# The headers contains the user token
headers = {
    "Authorization": f"Bearer {ACTIVELOOP_TOKEN}",
}

# Embed the search term
embedding = openai.Embedding.create(input=SEARCH_TERM, model="text-embedding-ada-002")["data"][0]["embedding"]

# Format the embedding array or list as a string, so it can be passed in the REST API request.
embedding_string = ",".join([str(item) for item in embedding])

# Create the query using TQL
query = f"select * from (select text, cosine_similarity(embedding, ARRAY[{embedding_string}]) as score from \"{dataset_path}\") order by score desc limit 5"
          
# Submit the request                              
response = requests.post(ENDPOINT_URL, json={"query": query}, headers=headers)

data = response.json()

print(data)
```

{% endtab %}

{% tab title="Node.js" %}

```javascript
const axios = require('axios');

OPENAI_API_KEY = process.env.OPENAI_API_KEY;
ACTIVELOOP_TOKEN = process.env.ACTIVELOOP_TOKEN;

const QUERY = 'What do the trust and safety models do?';
const DATASET_PATH = 'hub://activeloop/twitter-algorithm';
const ENDPOINT_URL = 'https://app.activeloop.ai/api/query/v1';

// Function to get the embeddings of a text from Open AI API
async function getEmbedding(text) {
  const response = await axios.post('https://api.openai.com/v1/embeddings', {
    input: text,
    model: "text-embedding-ada-002"
  }, {
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${OPENAI_API_KEY}`
    }
  });

  return response.data;
}

// Function to search the dataset using the given query on Activeloop
async function searchDataset(query) {
  const response = await axios.post(${ENDPOINT_URL}, {
    query: query,
  }, {
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${ACTIVELOOP_TOKEN}`
    }
  });

  return response.data;
}

// Main function to search for similar texts in the dataset based on the query_term
async function searchSimilarTexts(query, dataset_path) {
  // Get the embedding of the query_term
  const embedding = await getEmbedding(query);
  const embedding_search = embedding.data[0].embedding.join(',');

  // Construct the search query
  const TQL = `SELECT * FROM (
                    SELECT text, l2_norm(embedding - ARRAY[${embedding_search}]) AS score 
                    from "${dataset_path}"
                  ) ORDER BY score DESC LIMIT 5`;

  // Search the dataset using the constructed query
  const response = await searchDataset(TQL);

  // Log the search results
  console.log(response);
}

searchSimilarTexts(QUERY, DATASET_PATH)
```

{% endtab %}
{% endtabs %}

Congrats! You performed a vector search using the Deep Lake Managed Database! 🎉
