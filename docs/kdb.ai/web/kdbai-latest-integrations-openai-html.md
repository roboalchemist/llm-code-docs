# Source: https://code.kx.com/kdbai/latest/integrations/openai.html

Title: KDB.AI OpenAI Retrieval PLugin - KDB.AI Documentation

URL Source: https://code.kx.com/kdbai/latest/integrations/openai.html

Markdown Content:
_This section explains how to integrate KDB.AI with the OpenAI Retrieval Plugin._

_Audience: these instructions are targeted at Application Builders and assume knowledge of setting up and running hosted applications._

The OpenAI Retrieval Plugin is a tool that enhances the capabilities of ChatGPT by allowing developers to create custom document retrieval functionality. With this plugin, you can find relevant information in real-time during ChatGPT conversations without the need for fine-tuning.

This integration guide helps you create custom GPTs on OpenAI using the **Actions** feature. **Actions** helps GPTs integrate external data, interact with the real-world, and connect to databases, all through APIs.

To create a custom GPT that can use your OpenAI Retrieval Plugin for semantic search and retrieval of your documents, and even store new information back to the database, you first need to have deployed an [OpenAI Retrieval Plugin](https://github.com/openai/chatgpt-retrieval-plugin/blob/main/README.md#deployment).

Getting started
---------------

Before you integrate KDB.AI with the OpenAI Retrieval Plugin, ensure you have the following:

*   Installed [Python 3](https://www.python.org/downloads), [Pip](https://pip.pypa.io/en/stable/installation/), and [Git](https://git-scm.com/downloads)
*   An active KDB.AI [Server](https://kx.com/kdb-ai-server-download) license
*   A valid [API key](https://platform.openai.com/docs/quickstart/account-setup) for OpenAI (you might need to upgrade to a paid plan)
*   Advanced understanding of how to create and deploy APIs
*   Know how to work with [vector databases](https://kdb.ai/learning-hub/articles/vector-database-101/) and [embedding models](https://kdb.ai/learning-hub/articles/vector-embeddings/)
*   Understand how to setup the necessary configurations for interacting with either KDB.AI [Server](https://code.kx.com/kdbai/latest/gettingStarted/kdb-ai-server-setup.html)

Setup
-----

To complete the KDB.AI integration with the OpenAI Retrieval Plugin, follow the steps below:

### 1. Set up environment and dependencies

To install the KDB.AI ChatGPT Retrieval Plugin server app, you need to:

*   Clone the repository (note that the default is the KDB.AI branch)
*   Go to the cloned repository directory and install `poetry` for dependency management.

To do so, run the following commands:

```
git clone https://github.com/KxSystems/chatgpt-retrieval-plugin -b KDB.AI
cd chatgpt-retrieval-plugin
pip install poetry
poetry install
```

 Next, set the following environment variables to run the KDB.AI ChatGPT Retrieval Plugin server app: 

```
export BEARER_TOKEN='<BEARER TOKEN>'  # You can create your own bearer token on https://jwt.io/
export DATASTORE=kdbai
export KDBAI_ENDPOINT='<KDB.AI ENDPOINT>'
export KDBAI_API_KEY='<KDB.AI API KEY>'
export OPENAI_API_KEY='<OPENAI API KEY>'  # You can get an API key on https://platform.openai.com
```

 To start the local server run the following command: 

```
poetry run start
```

At this point, your app works locally. To connect it with a custom GPT, you have to host it on any cloud platform that supports Docker containers, such as [Fly.io](https://fly.io/), [Heroku](https://www.heroku.com/), [Render](https://render.com/), or [Azure Container Apps](https://azure.microsoft.com/en-gb/products/container-apps/).

### 2. Prepare and add data to the API

Once you deploy the API, you need to load, prepare, embed, and chunk data to remove any part that you don't want to store in the database.

```
import os
from pprint import pprint
import random

from datasets import load_dataset
import openai
import requests
from tqdm.auto import tqdm

BEARER_TOKEN = os.environ.get("BEARER_TOKEN")

data = load_dataset("adversarial_qa", 'adversarialQA', ignore_verifications=True)['train'].to_pandas()
data = data.drop_duplicates(subset=["context"])
print(f"Number of unique contexts: {len(data)}") # at this point, your {len(data)} should be 2648
data.head()
```

For instance, you can change the format to a dictionary and divide it into batches (refer to our [Ingest data](https://code.kx.com/kdbai/latest/use/ingestion.html) page for details).

```
# extract text data from the dataset. This will follow the default schema.
documents = [
    {
        'id': r['id'],
        'text': r['context'],
        'metadata': {
        'title': r['title']
        }
        } for r in data.to_dict(orient='records')
]
pprint(documents[0])
```

 When you're happy with the results, call the `/upsert` API endpoint to send your data to the OpenAI embedding model and store the embeddings into a KDB.AI table. 

```
# initialise an HTTP session with the KDB.AI ChatGPT Retrieval Plugin app
s = requests.Session()

batchSize = 100

# upsert documents from the dataset in batches
for i in tqdm(range(0, len(documents), batchSize)):
    i_end = min(len(documents), i+batchSize)
    res = s.post(
        "https://your-app-url.com/upsert", # for local servers the URL will be http://localhost:8000/upsert
        headers = {
            "Authorization": f"Bearer {BEARER_TOKEN}"
        },
        json = {
            "documents": documents[i:i_end]
        }
    )
```

Once you upserted the data, start querying the datastore by passing queries to the `/query` endpoint and evaluate the responses.

```
# extract questions and reformat into queries
queries = data['question'].tolist()
queries = [{'query': queries[i]} for i in range(len(queries))]

# choose 5 queries at random 
i = random.randint(0, len(queries)-5)
searchQueries = queries[i:i+5]

print(searchQueries)

# query the vector database
results = requests.post(
    "https://your-app-url.com/query", # for local servers the URL will be http://localhost:8000/query
    headers = {
        "Authorization": f"Bearer {BEARER_TOKEN}"
    },
    json = {
        'queries': searchQueries
    }
)

# get list of queries and answers
import json
response_dict = json.loads(results.content)

for result in response_dict['results']:
    print(result['query'])
    for answer in result['results']:
        print(answer['text'])
```

### 3. Integrate into ChatGPT

Use **Actions** within GPTs to connect it with your newly created API. First, make sure you're a ChatGPT Plus subscriber.

Go to Directory files (yaml., ai-plugin json) and update the files with the API URL:

1.   Go to this [Create GPT page](https://chat.openai.com/gpts/editor).
2.   Follow the steps to create and set up your GPT. 
3.   In the **Configure** tab, manually fill in name, description, and instructions, or use the smart creator tool.
4.   In the **Actions** section, click on **Create new action**. 
5.   Choose an authentication method: **None**, **API key** (Basic or Bearer), or **OAuth**.
6.   Import the OpenAPI schema. You have two ways of doing this, either:

    *   straight from the OpenAPI schema located in your app at `https://your-app-url.com/.well-known/openapi.yaml`, or
    *   copy and paste the contents of this file into the **schema** input area if you only want to expose the `/query` endpoint to the GPT. Make a note to edit the URL under the **Servers** section of the OpenAPI schema you paste in. 

Optionally, you can add a **fetch** endpoint to the OpenAPI schema by editing the `/server/main.py`. This fetches more content from a document by ID if some section is cut off in the retrieved result. It might also be useful to pass in a string with the text from the retrieved result and an option to return a fixed length of context before and after the retrieved result.

To allow the GPT to save information back to your KDB.AI vector database, you have to connect it to the Retrieval Plugin's `/upsert` endpoint by copying the contents of this file into the schema area. Now the GPT can store the newly-generated or learned information from the conversation.

If you need help with the integration, feel free to reach out to the KDB.AI [Slack community](http://kx.com/slack) or email [support@kdb.ai](mailto:support@kdb.ai).

Summary
-------

Now that you have successfully configured your integration, you should have:

*   The embeddings generated from the data successfully loaded into your KDB.AI vector database.
*   Access to these embeddings from KDB.AI Server for more applications within ChatGPT.

Next steps
----------

*   Head to the OpenAI [GitHub repository](https://github.com/openai/chatgpt-retrieval-plugin).
*   Check out our [KDB.AI for Q&A with ChatGPT Retrieval Plugin](https://github.com/KxSystems/chatgpt-retrieval-plugin/blob/KDB.AI/examples/providers/kdbai/ChatGPT_QA_Demo.ipynb) notebook.
*   Watch a [YouTube video demonstrating the integration of a custom GPT with KDB.AI](https://www.youtube.com/watch?v=8IsVeTYh-MY).
