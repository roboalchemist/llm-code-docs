# Get credentials from environment variables
qdrant_key = os.getenv("QDRANT_KEY")
qdrant_url = os.getenv("QDRANT_URL")
neo4j_uri = os.getenv("NEO4J_URI")
neo4j_username = os.getenv("NEO4J_USERNAME")
neo4j_password = os.getenv("NEO4J_PASSWORD")
openai_key = os.getenv("OPENAI_API_KEY")

```

* * *

This ensures that sensitive information (like API keys and database credentials) is securely stored in environment variables.

### [Anchor](https://qdrant.tech/documentation/examples/graphrag-qdrant-neo4j/\#initializing-neo4j-and-qdrant-clients) Initializing Neo4j and Qdrant Clients

Now, we initialize the Neo4j and Qdrant clients using the credentials.

```python