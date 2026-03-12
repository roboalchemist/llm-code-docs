# Source: https://code.kx.com/kdbai/latest/integrations/hugging-face.html

Title: KDB.AI Hugging Face - KDB.AI Documentation

URL Source: https://code.kx.com/kdbai/latest/integrations/hugging-face.html

Markdown Content:
_This section explains how to integrate KDB.AI with Hugging Face._

Hugging Face is a platform where you can access models, datasets, and applications for Machine Learning (ML) workloads. Hugging Face allows you to create, train, deploy ML models or fine-tune pre-trained models. Notable tools include the Transformers model library, pipelines for performing ML tasks, and collaborative resources.

The KDB.AI Hugging Face integration guide helps you execute a wide variety of tasks with your KDB.AI vector database, including detect objects, summarize documents, answer questions, generate text, translate content, and convert text to speech.

Why use Hugging Face for embeddings?
When building production applications that utilize embeddings, using open-source embedding models has the following advantages:

*   **Control**: reduces dependence on third-party embedding providers.
*   **Local embedding**: you can create embeddings locally, which is useful for embedding your dataset.
*   **Scalability**: KDB.AI's vector database can handle large-scale data and search operations efficiently. 
*   **Flexibility**: you can experiment with different embedding models and configurations to optimize performance for your specific use cases. 

A common approach is to use a Python framework like sentence-transformers, developed by Hugging Face, which offers state-of-the-art sentence, text, and image embeddings. Here's a typical workflow:

*   **Embed your dataset locally**: use a library like FastEmbed (built on top of Hugging Face's transformers library, optimized for speed) to embed your dataset, which might consist of AI tools and associated metadata.
*   **Embed queries at inference time**: when a user submits a query, use an external service like Hugging Face's Inference API to embed the query. This eliminates the need to deploy your own model, allowing you to leverage a fully optimized external service.

By following this approach, you can build a system that searches through hundreds of AI tools without the need to deploy any infrastructure (and scale to millions!). Additionally, since you embed the dataset locally, you can use Hugging Face's free plan without requiring a credit card or worrying about hitting rate limits, at least until you are ready for production.

Getting started
---------------

Before you integrate KDB.AI with Hugging Face, you need to have the following:

*   [Python 3](https://www.python.org/downloads) (versions 3.9 to 3.13), [Pip](https://pip.pypa.io/en/stable/installation/), and [Git](https://git-scm.com/downloads) installed
*   An active KDB.AI [Server](https://kx.com/kdb-ai-server-download) license
*   Know how to work with [vector databases](https://kdb.ai/learning-hub/articles/vector-database-101/) and [embedding models](https://kdb.ai/learning-hub/articles/vector-embeddings/)
*   Understand how to setup the necessary configurations for interacting with either KDB.AI [Server](https://code.kx.com/kdbai/latest/gettingStarted/kdb-ai-server-setup.html)

Setup
-----

To complete the KDB.AI integration, you can use the Hugging Face Inference API endpoints to generate high-quality embeddings and store/index them in the vector database.

*   Sign Up/Sign In to [Hugging Face](https://huggingface.co/) and verify your account.
*   Log in and go to **Avatar** ->**Settings**.
*   Select **Access Tokens** -> click **New token**
*   Give the token name and `Write` type.
*   Click **Generate token**.
*   Copy the generated token and use in the script below as `HF_TOKEN`
*   Install dependencies: ```
!pip install kdbai_client fastembed
``` 
*   Import packages: ```
# vector DB
import os
from getpass import getpass
import kdbai_client as kdbai
import time
import numpy as np
import pandas as pd
``` 

1. Connect to KDB.AI
--------------------

To use KDB.AI Server, you need download and run your own container. Follow the instructions in the signup email to get your session up and running, then passing your local endpoint:

```
session = kdbai.Session(endpoint="http://localhost:8082")
```

### Create empty database

Delete existing database `myDatabase`:

```
try:
    session.database("myDatabase").drop()
except kdbai.KDBAIException:
    pass
```

 Create a new database called `myDatabase`: 

```
try:
    session.create_database("myDatabase")
except kdbai.KDBAIException:
    pass
```

### Verify defined tables

Check your connection using the `session.database('myDatabase').tables` function. This returns a list of all the tables you have defined in your vector database:

```
# ensure no table called "ai_tools" exists
try:
   session.database('myDatabase').table("ai_tools").drop()
   time.sleep(5)
except kdbai.KDBAIException:
   pass
```

 If you're just starting out, it should return an empty list: 

```
session.database('myDatabase').tables
```

2. Create table
---------------

To create a table in KDB.AI, use the `create_table` function, which takes two arguments: `name` and `schema`. This schema must meet the following criteria:

*   Must contain a list of columns.
*   All columns must have a `type` specified, except the vectors column.

Define schema - to create a table with two columns, you can use, for example, the following columns:

*   **id** with a list of dummy IDs
*   **vector embeddings** to use for similarity search later on.

Next, you need to define dimensionality, similarity metric, and index type with the `indexes` parameter. You can use:

*   `dims = 384`: In the next section, you generate embeddings that are eight-dimensional to match this. You can chose any value here.
*   `metric = L2`: Stands for L2/Euclidean distance. You can also use IP/Inner Product and CS/Cosine Similarity, depending on the specific context and nature of your data.
*   `type = flat`: We use a Flat index, but you can go for HNSW and IVFPQ, depending on the data and your performance requirements.

```
numDim = 384
schema = [
            {"name": "id", "type": "str"},
            {"name": "name", "type": "str"},
            {"name": "description", "type": "str"},
            {"name": "summary", "type": "str"},
            {"name": "title", "type": "str"},
            {"name": "visitors", "type": "int64"},
            {"name": "description_embedding", "type": "float32s"},
            ]

indexes =       [{"name": "myVectorIndex", 
                  "column": "description_embedding",
                  "type": "flat", 
                  "params": {"dims": numDim, "metric": "L2"},
                  }]
```

 Create table: 

```
table = session.database('myDatabase').create_table('ai_tools', schema, indexes=indexes)
```

3. Add data to table
--------------------

First, generate a vector of five 8-dimensional vectors - they'll be the vector embeddings. Next, add to pandas dataframe with column names/types matching the target table:

```
import requests

gist_url = "https://gist.github.com/mrmps/2f62a2287cb2c1ca63a2762fcaac89bc/raw"
response = requests.get(gist_url)
ai_tools_data = response.json()
df = pd.DataFrame.from_dict(ai_tools_data)
df.drop(columns=["xata"], inplace=True)
df.head()
```

 Use the FastEmbed library to embed every description in the dataset: 

```
from fastembed import TextEmbedding

embedding_model = TextEmbedding()

descriptions = [tool["description"] for tool in ai_tools_data]
embeddings = list(embedding_model.embed(descriptions))
```

 Insert the data into your KDB.AI table: 

```
# Create a DataFrame with the AI tools data
data = pd.DataFrame(ai_tools_data)[["id", "name", "description", "summary", "title", "visitors"]]
data["description_embedding"] = embeddings

# Bulk insert the data into KDB.AI
table.insert(data)
```

4. Search with Hugging Face
---------------------------

Use the Hugging Face Inference API to embed the query so that you can use it to search your index:

```
# Perform a similarity search using Hugging Face embeddings
import requests

# Make sure your URL looks like this to ensure you get instant results, and not a model loading error
embedding_url = "https://api-inference.huggingface.co/pipeline/feature-extraction/BAAI/bge-small-en-v1.5"

def waitForResourceAvailable(response, timeout_seconds):
    timer = 0
    while response.status_code == 204:
        time.sleep(10)
        timer += 10
        if timer > timeout_seconds:
            break
        if response.status_code == 200:
            break

def generate_query_embedding(text: str) -> list[float]:
    response = requests.post(
        embedding_url,
        headers={"Authorization": f"Bearer {HF_TOKEN}"},
        json={"inputs": text}
    )
    waitForResourceAvailable(response, 5)
    if response.status_code != 200:
       raise ValueError(f"Request failed with status code {response.status_code}: {response.text}")
    print(response.status_code)
    return response.json()
# Sometimes you might get a status code 503 (Unavailable server error response code indicates that the server is not ready to handle the request)

query = "AI tool for creating 3D textures"
query_embedding = generate_query_embedding(query)

results = table.search(
    vectors={'myVectorIndex': [query_embedding]}, 
    n=3,
)
```

 Once you are finished with your searches, it is recommended to delete the KDB.AI Table to conserve resources: 

```
table.drop()
```

Example #1: Use KDB.AI and Hugging Face for Transfer Learning
In this [Image Search on Brain MRI Scans](https://github.com/KxSystems/kdbai-samples/blob/main/image_search/image_search.ipynb) example, we take a model that has been pre-trained for a task (ResNet-50 for ImageNet classification) and use it as a starting point to solve a more specific problem. To create our image embeddings, we used a neural network that has been pre-trained on the brain tumor classification problem.

Example #2: Use a LLM model from Hugging Face to execute RAG
This [Retrieval Augmented Generation (RAG) with LangChain](https://github.com/KxSystems/kdbai-samples/blob/main/retrieval_augmented_generation/retrieval_augmented_generation.ipynb) notebook demonstrates how to use an advanced prompt engineering technique called Retrieval Augmented Generation (RAG), with hands-on examples using Langchain, KDB.AI and various LLMs.

Example #3: Use Hugging Face with KDB.AI to create a AI tool search engine
This [notebook](https://colab.research.google.com/drive/18QowsL2PtLkuEXOXQ0Azio9SZX40dfJ9) walks you through the process of embedding a dataset of AI tools using FastEmbed (a lightweight, fast, Python library built for embedding generation,) storing the embeddings in a KDB.AI table, and then using Hugging Face's Inference API to embed queries at inference time. This enables efficient and scalable similarity search capabilities.

If you need help with the integration, feel free to reach out to the KDB.AI [Slack community](http://kx.com/slack) or email [support@kdb.ai](mailto:support@kdb.ai).

Summary
-------

Whether you're building a semantic search engine, a recommendation system, or any application that relies on finding similar items, the KDB.AI integration with Hugging Face provides a powerful and flexible solution.

Now that you have successfully configured the integration you can achieve the following:

*   Enjoy a seamless connection between Hugging Face and KDB.AI.
*   Develop Machine Learning (ML) applications using Hugging Face models by following the pre-built integration notebooks between KDB.AI and Hugging Face: [Image search sample](https://github.com/KxSystems/kdbai-samples/blob/main/image_search/image_search.ipynb), [RAG with LangChain](https://github.com/KxSystems/kdbai-samples/blob/main/retrieval_augmented_generation/retrieval_augmented_generation.ipynb), and [AI tool search engine](https://colab.research.google.com/drive/18QowsL2PtLkuEXOXQ0Azio9SZX40dfJ9). 

Next steps
----------

*   Head to our [GitHub repository](https://github.com/KxSystems/kdbai-samples) for more examples.
*   Use Google Colab to run our notebooks: [Image Search on Brain MRI Scans](https://colab.research.google.com/github/KxSystems/kdbai-samples/blob/main/image_search/image_search.ipynb) and [Retrieval Augmented Generation (RAG) with LangChain](https://colab.research.google.com/github/KxSystems/kdbai-samples/blob/main/retrieval_augmented_generation/retrieval_augmented_generation.ipynb)
