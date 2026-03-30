# [Anchor](https://qdrant.tech/documentation/agentic-rag-camelai-discord/\#agentic-rag-discord-chatbot-with-qdrant-camel-ai--openai) Agentic RAG Discord ChatBot with Qdrant, CAMEL-AI, & OpenAI

| Time: 45 min | Level: Intermediate | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1Ymqzm6ySoyVOekY7fteQBCFCXYiYyHxw#scrollTo=QQZXwzqmNfaS) |  |
| --- | --- | --- | --- |

Unlike traditional RAG techniques, which passively retrieve context and generate responses, **agentic RAG** involves active decision-making and multi-step reasoning by the chatbot. Instead of just fetching data, the chatbot makes decisions, dynamically interacts with various data sources, and adapts based on context, giving it a much more dynamic and intelligent approach.

In this tutorial, we’ll develop a fully functional chatbot using Qdrant, [CAMEL-AI](https://www.camel-ai.org/), and [OpenAI](https://openai.com/).

Let’s get started!

* * *

## [Anchor](https://qdrant.tech/documentation/agentic-rag-camelai-discord/\#workflow-overview) Workflow Overview

Below is a high-level look at our Agentic RAG workflow:

| Step | Description |
| --- | --- |
| **1\. Environment Setup** | Install required libraries ( `camel-ai`, `qdrant-client`, `discord.py`) and set up the Python environment. |
| **2\. Set Up the OpenAI Embedding Instance** | Create an OpenAI account, generate an API key, and configure the embedding model. |
| **3\. Configure the Qdrant Client** | Sign up for Qdrant Cloud, create a cluster, configure `QdrantStorage`, and set up the API connection. |
| **4\. Scrape and Process Data** | Use `VectorRetriever` to scrape Qdrant documentation, chunk text, and store embeddings in Qdrant. |
| **5\. Set Up the CAMEL-AI ChatAgent** | Instantiate a CAMEL-AI `ChatAgent` with OpenAI models for multi-step reasoning and context-aware responses. |
| **6\. Create and Configure the Discord Bot** | Register a new bot in the Discord Developer Portal, invite it to a server, and enable permissions. |
| **7\. Build the Discord Bot** | Integrate Discord.py with CAMEL-AI and Qdrant to retrieve context and generate intelligent responses. |
| **8\. Test the Bot** | Run the bot in a live Discord server and verify that it provides relevant, context-rich answers. |

## [Anchor](https://qdrant.tech/documentation/agentic-rag-camelai-discord/\#architecture-diagram) Architecture Diagram

Below is the architecture diagram representing the workflow and interactions of the chatbot:

![Architecture Diagram](https://qdrant.tech/documentation/examples/agentic-rag-camelai-discord/diagram_discord_bot.png)

The workflow starts by **scraping, chunking, and upserting** content from URLs using the `vector_retriever.process()` method, which generates embeddings with the **OpenAI embedding instance**. These embeddings, along with their metadata, are then indexed and stored in **Qdrant** via the `QdrantStorage` class.

When a user sends a query through the **Discord bot**, it is processed by `vector_retriever.query()`, which first embeds the query using **OpenAI Embeddings** and then retrieves the most relevant matches from Qdrant via `QdrantStorage`. The retrieved context (e.g., relevant documentation snippets) is then passed to an **OpenAI-powered Qdrant Agent** under **CAMEL-AI**, which generates a final, context-aware response.

The Qdrant Agent processes the retrieved vectors using the `GPT_4O_MINI` language model, producing a response that is contextually relevant to the user’s query. This response is then sent back to the user through the **Discord bot**, completing the flow.

* * *

## [Anchor](https://qdrant.tech/documentation/agentic-rag-camelai-discord/\#step-1-environment-setup)**Step 1: Environment Setup**

Before diving into the implementation, here’s a high-level overview of the stack we’ll use:

| **Component** | **Purpose** |
| --- | --- |
| **Qdrant** | Vector database for storing and querying document embeddings. |
| **OpenAI** | Embedding and language model for generating vector representations and chatbot responses. |
| **CAMEL-AI** | Framework for managing dialogue flow, retrieval, and AI agent interactions. |
| **Discord API** | Platform for deploying and interacting with the chatbot. |

### [Anchor](https://qdrant.tech/documentation/agentic-rag-camelai-discord/\#install-dependencies) Install Dependencies

We’ll install CAMEL-AI, which includes all necessary dependencies:

```python
!pip install camel-ai[all]==0.2.17

```

* * *

## [Anchor](https://qdrant.tech/documentation/agentic-rag-camelai-discord/\#step-2-set-up-the-openai-embedding-instance)**Step 2: Set Up the OpenAI Embedding Instance**

1. **Create an OpenAI Account**: Go to [OpenAI](https://platform.openai.com/signup) and sign up for an account if you don’t already have one.

2. **Generate an API Key**:

   - After logging in, click on your profile icon in the top-right corner and select **API keys**.

   - Click **Create new secret key**.

   - Copy the generated API key and store it securely. You won’t be able to see it again.

Here’s how to set up the OpenAI client in your code:

Create a `.env` file in your project directory and add your API key:

```bash
OPENAI_API_KEY=<your_openai_api_key>

```

Make sure to replace `<your_openai_api_key>` with your actual API key.

Now, start the OpenAI Client

```python
import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai_client = openai.Client(
    api_key=os.getenv("OPENAI_API_KEY")
)

```

To set up the embedding instance, we will use text embedding 3 large:

```python
from camel.embeddings import OpenAIEmbedding
from camel.types import EmbeddingModelType

embedding_instance = OpenAIEmbedding(model_type=EmbeddingModelType.TEXT_EMBEDDING_3_LARGE)

```

## [Anchor](https://qdrant.tech/documentation/agentic-rag-camelai-discord/\#step-3-configure-the-qdrant-client)**Step 3: Configure the Qdrant Client**

For this tutorial, we will be using the **Qdrant Cloud Free Tier**. Here’s how to set it up:

1. **Create an Account**: Sign up for a Qdrant Cloud account at [Qdrant Cloud](https://cloud.qdrant.io/).

2. **Create a Cluster**:

   - Navigate to the **Overview** section.
   - Follow the onboarding instructions under **Create First Cluster** to set up your cluster.
   - When you create the cluster, you will receive an **API Key**. Copy and securely store it, as you will need it later.
3. **Wait for the Cluster to Provision**:

   - Your new cluster will appear under the **Clusters** section.

After obtaining your Qdrant Cloud details, add to your `.env` file:

```bash
QDRANT_CLOUD_URL=<your-qdrant-cloud-url>
QDRANT_CLOUD_API_KEY=<your-api-key>

```

### [Anchor](https://qdrant.tech/documentation/agentic-rag-camelai-discord/\#configure-the-qdrantstorage) Configure the QdrantStorage

The `QdrantStorage` will deal with connecting with the Qdrant Client for all necessary operations to your collection.

```python
from camel.retrievers import VectorRetriever