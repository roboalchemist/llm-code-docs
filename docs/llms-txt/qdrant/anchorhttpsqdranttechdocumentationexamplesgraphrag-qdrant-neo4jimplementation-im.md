# [Anchor](https://qdrant.tech/documentation/examples/graphrag-qdrant-neo4j/\#implementation) Implementation

We’ll walk through a complete pipeline that ingests data into Neo4j and Qdrant, retrieves relevant data, and generates responses using an LLM based on the retrieved graph context.

The main components of this pipeline include data ingestion (to Neo4j and Qdrant), retrieval, and generation steps.

## [Anchor](https://qdrant.tech/documentation/examples/graphrag-qdrant-neo4j/\#prerequisites) Prerequisites

These are the tutorial prerequisites, which are divided into setup, imports, and initialization of the two DBs.

### [Anchor](https://qdrant.tech/documentation/examples/graphrag-qdrant-neo4j/\#setup) Setup

Let’s start with setting up instances with Qdrant and Neo4j.

### [Anchor](https://qdrant.tech/documentation/examples/graphrag-qdrant-neo4j/\#qdrant-setup) Qdrant Setup

To create a Qdrant instance, you can use their **managed service** (Qdrant Cloud) or set up a self-hosted cluster. For simplicity, we will use Qdrant cloud:

- Go to [Qdrant Cloud](https://qdrant.tech/) and sign up or log in.
- Once logged in, click on **Create New Cluster**.
- Follow the on-screen instructions to create your cluster.
- Once your cluster is created, you’ll be given a **Cluster URL** and **API Key**, which you will use in the client to interact with Qdrant.

### [Anchor](https://qdrant.tech/documentation/examples/graphrag-qdrant-neo4j/\#neo4j-setup) Neo4j Setup

To set up a Neo4j instance, you can use **Neo4j Aura** (cloud service) or host it yourself. We will use Neo4j Aura:

- Go to Neo4j Aura and sign up/log in.
- After setting up, an instance will be created if it is the first time.
- After the database is set up, you’ll receive a **connection URI**, **username**, and **password**.

We can add the following in the .env file for security purposes.

### [Anchor](https://qdrant.tech/documentation/examples/graphrag-qdrant-neo4j/\#imports) Imports

First, we import the required libraries for working with Neo4j, Qdrant, OpenAI, and other utility functions.

```python
from neo4j import GraphDatabase
from qdrant_client import QdrantClient, models
from dotenv import load_dotenv
from pydantic import BaseModel
from openai import OpenAI
from collections import defaultdict
from neo4j_graphrag.retrievers import QdrantNeo4jRetriever
import uuid
import os

```

* * *

- **Neo4j:** Used to store and query the graph database.
- **Qdrant:** A vector database used for semantic similarity search.
- **dotenv:** Loads environment variables for credentials and API keys.
- **Pydantic:** Ensures data is structured properly when interacting with the graph data.
- **OpenAI:** Interfaces with the OpenAI API to generate responses and embeddings.
- **neo4j\_graphrag:** A helper package to retrieve data from both Qdrant and Neo4j.

### [Anchor](https://qdrant.tech/documentation/examples/graphrag-qdrant-neo4j/\#setting-up-environment-variables) Setting Up Environment Variables

Before initializing the clients, we load the necessary credentials from environment variables.

```python