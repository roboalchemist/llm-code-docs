# [Anchor](https://qdrant.tech/documentation/examples/graphrag-qdrant-neo4j/\#architecture-overview) Architecture Overview

The architecture has two main components: **Ingestion** and **Retrieval & Generation**. Ingestion processes raw data into structured knowledge and vector representations, while Retrieval and Generation enable efficient querying and response generation.

This process is divided into two steps: **Ingestion**, where data is prepared and stored, and **Retrieval and Generation**, where the prepared data is queried and utilized. Let’s start with Ingestion.

## [Anchor](https://qdrant.tech/documentation/examples/graphrag-qdrant-neo4j/\#ingestion) Ingestion

The GraphRAG ingestion pipeline combines a **Graph Database** and a **Vector Database** to improve RAG workflows.

![image1](https://qdrant.tech/documentation/examples/graphrag-qdrant-neo4j/image1.png)

Fig 2: Overview of Ingestion Pipeline

Let’s break it down:

1. **Raw Data:** Serves as the foundation, comprising unstructured or structured content.
2. **Ontology Creation:** An **LLM** processes the raw data into an **ontology**, structuring entities, relationships, and hierarchies. Better approaches exist to extracting more structured information from raw data, like using NER to identify the names of people, organizations, and places. Unlike LLMs, this method creates.
3. **Graph Database:** The ontology is stored in a **Graph database** to capture complex relationships.
4. **Vector Embeddings:** An **Embedding model** converts the raw data into high-dimensional vectors capturing semantic similarities.
5. **Vector Database:** These embeddings are stored in a **Vector database** for similarity-based retrieval.
6. **Database Interlinking:** The **Graph database** (e.g., Neo4j) and **Vector database** (e.g., Qdrant) share unique IDs, enabling cross-referencing between ontology-based and vector-based results.

## [Anchor](https://qdrant.tech/documentation/examples/graphrag-qdrant-neo4j/\#retrieval--generation) Retrieval & Generation

The **Retrieval and Generation** process is designed to handle user queries by leveraging both semantic search and graph-based context extraction.

![image3](https://qdrant.tech/documentation/examples/graphrag-qdrant-neo4j/image3.png)

Fig 3: Overview of Retrieval and Generation Pipeline

The architecture can be broken down into the following steps:

1. **Query Vectorization:** An embedding model converts The user query into a high-dimensional vector.
2. **Semantic Search:** The vector performs a similarity-based search in the **Vector database**, retrieving relevant documents or entries.
3. **ID Extraction:** Extracted IDs from the semantic search results are used to query the **Graph database**.
4. **Graph Context Retrieval:** The **Graph database** provides contextual information, including relationships and entities linked to the extracted IDs.
5. **Response Generation:** The context retrieved from the graph is passed to an LLM to generate a final response.
6. **Results:** The generated response is returned to the user.

This architecture combines the strengths of both databases:

1. **Semantic Search with Vector Database:** The user query is first processed semantically to identify the most relevant data points without needing explicit keyword matches.
2. **Contextual Expansion with Graph Database:** IDs or entities retrieved from the vector database query the graph database for detailed relationships, enriching the retrieved data with structured context.
3. **Enhanced Generation:** The architecture combines semantic relevance (from the vector database) and graph-based context to enable the LLM to generate more informed, accurate, and contextually rich responses.