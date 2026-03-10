# Try to fetch the collection status
try:
    collection_info = client.get_collection(collection_name)
    print(f"Skipping creating collection; '{collection_name}' already exists.")
except Exception as e:
    # If collection does not exist, an error will be thrown, so we create the collection
    if 'Not found: Collection' in str(e):
        print(f"Collection '{collection_name}' not found. Creating it now...")

        client.create_collection(
            collection_name=collection_name,
            vectors_config=models.VectorParams(size=vector_dimension, distance=models.Distance.COSINE)
        )

        print(f"Collection '{collection_name}' created successfully.")
    else:
        print(f"Error while checking collection: {e}")

```

* * *

- **Qdrant Client:** The QdrantClient is used to connect to the Qdrant instance.
- **Creating Collection:** The create\_collection function checks if a collection exists. If not, it creates one with a specified vector dimension and distance metric (cosine similarity in this case).

### [Anchor](https://qdrant.tech/documentation/examples/graphrag-qdrant-neo4j/\#generating-embeddings) Generating Embeddings

Next, we define a function that generates embeddings for text using OpenAI’s API.

```python
def openai_embeddings(text):
    response = client.embeddings.create(
        input=text,
        model="text-embedding-3-small"
    )

    return response.data[0].embedding

```

* * *

This function uses OpenAI’s embedding model to transform input text into vector representations.

### [Anchor](https://qdrant.tech/documentation/examples/graphrag-qdrant-neo4j/\#ingesting-into-qdrant) Ingesting into Qdrant

Let’s ingest the data into the vector database.

```python
def ingest_to_qdrant(collection_name, raw_data, node_id_mapping):
    embeddings = [openai_embeddings(paragraph) for paragraph in raw_data.split("\n")]

    qdrant_client.upsert(
        collection_name=collection_name,
        points=[\
            {\
                "id": str(uuid.uuid4()),\
                "vector": embedding,\
                "payload": {"id": node_id}\
            }\
            for node_id, embedding in zip(node_id_mapping.values(), embeddings)\
        ]
    )

```

* * *

The ingest\_to\_qdrant function generates embeddings for each paragraph in the raw data and stores them in a Qdrant collection. It associates each embedding with a unique ID and its corresponding node ID from the node\_id\_mapping dictionary, ensuring proper linkage for later retrieval.

* * *

## [Anchor](https://qdrant.tech/documentation/examples/graphrag-qdrant-neo4j/\#retrieval--generation-1) Retrieval & Generation

In this section, we will create the retrieval and generation engine for the system.

### [Anchor](https://qdrant.tech/documentation/examples/graphrag-qdrant-neo4j/\#building-a-retriever) Building a Retriever

The retriever integrates vector search and graph data, enabling semantic similarity searches with Qdrant and fetching relevant graph data from Neo4j. This enriches the RAG process and allows for more informed responses.

```python
def retriever_search(neo4j_driver, qdrant_client, collection_name, query):
    retriever = QdrantNeo4jRetriever(
        driver=neo4j_driver,
        client=qdrant_client,
        collection_name=collection_name,
        id_property_external="id",
        id_property_neo4j="id",
    )

    results = retriever.search(query_vector=openai_embeddings(query), top_k=5)

    return results

```

* * *

The [QdrantNeo4jRetriever](https://qdrant.tech/documentation/frameworks/neo4j-graphrag/) handles both vector search and graph data fetching, combining Qdrant for vector-based retrieval and Neo4j for graph-based queries.

**Vector Search:**

- **`qdrant_client`** connects to Qdrant for efficient vector similarity search.
- **`collection_name`** specifies where vectors are stored.
- **`id_property_external="id"`** maps the external entity’s ID for retrieval.

**Graph Fetching:**

- **`neo4j_driver`** connects to Neo4j for querying graph data.
- **`id_property_neo4j="id"`** ensures the entity IDs from Qdrant match the graph nodes in Neo4j.

### [Anchor](https://qdrant.tech/documentation/examples/graphrag-qdrant-neo4j/\#querying-neo4j-for-related-graph-data) Querying Neo4j for Related Graph Data

We need to fetch subgraph data from a Neo4j database based on specific entity IDs after the retriever has provided the relevant IDs.

```python
def fetch_related_graph(neo4j_client, entity_ids):
    query = """
    MATCH (e:Entity)-[r1]-(n1)-[r2]-(n2)
    WHERE e.id IN $entity_ids
    RETURN e, r1 as r, n1 as related, r2, n2
    UNION
    MATCH (e:Entity)-[r]-(related)
    WHERE e.id IN $entity_ids
    RETURN e, r, related, null as r2, null as n2
    """
    with neo4j_client.session() as session:
        result = session.run(query, entity_ids=entity_ids)
        subgraph = []
        for record in result:
            subgraph.append({
                "entity": record["e"],
                "relationship": record["r"],
                "related_node": record["related"]
            })
            if record["r2"] and record["n2"]:
                subgraph.append({
                    "entity": record["related"],
                    "relationship": record["r2"],
                    "related_node": record["n2"]
                })
    return subgraph

```

* * *

The function fetch\_related\_graph takes in a Neo4j client and a list of entity\_ids. It runs a Cypher query to find related nodes (entities) and their relationships based on the given entity IDs. The query matches entities (e:Entity) and finds related nodes through any relationship \[r\]. The function returns a list of subgraph data, where each record contains the entity, relationship, and related\_node.

This subgraph is essential for generating context to answer user queries.

### [Anchor](https://qdrant.tech/documentation/examples/graphrag-qdrant-neo4j/\#setting-up-the-graph-context) Setting up the Graph Context

The second part of the implementation involves preparing a graph context. We’ll fetch relevant subgraph data from a Neo4j database and format it for the model. Let’s break it down.

```python
def format_graph_context(subgraph):
    nodes = set()
    edges = []

    for entry in subgraph:
        entity = entry["entity"]
        related = entry["related_node"]
        relationship = entry["relationship"]

        nodes.add(entity["name"])
        nodes.add(related["name"])

        edges.append(f"{entity['name']} {relationship['type']} {related['name']}")

    return {"nodes": list(nodes), "edges": edges}

```

* * *

The function format\_graph\_context processes a subgraph returned by a Neo4j query. It extracts the graph’s entities (nodes) and relationships (edges). The nodes set ensures each entity is added only once. The edges list captures the relationships in a readable format: _Entity1 relationship Entity2_.

### [Anchor](https://qdrant.tech/documentation/examples/graphrag-qdrant-neo4j/\#integrating-with-the-llm) Integrating with the LLM

Now that we have the graph context, we need to generate a prompt for a language model like GPT-4. This is where the core of the Retrieval-Augmented Generation (RAG) happens — we combine the graph data and the user query into a comprehensive prompt for the model.

```python
def graphRAG_run(graph_context, user_query):
    nodes_str = ", ".join(graph_context["nodes"])
    edges_str = "; ".join(graph_context["edges"])
    prompt = f"""
    You are an intelligent assistant with access to the following knowledge graph:

    Nodes: {nodes_str}

    Edges: {edges_str}

    Using this graph, Answer the following question:

    User Query: "{user_query}"
    """

    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[\
                {"role": "system", "content": "Provide the answer for the following question:"},\
                {"role": "user", "content": prompt}\
            ]
        )
        return response.choices[0].message

    except Exception as e:
        return f"Error querying LLM: {str(e)}"

```

* * *

The function graphRAG\_run takes the graph context (nodes and edges) and the user query, combining them into a structured prompt for the LLM. The nodes and edges are formatted as readable strings to form part of the LLM input. The LLM is then queried with the generated prompt, asking it to refine the user query using the graph context and provide an answer. If the model successfully generates a response, it returns the answer.

### [Anchor](https://qdrant.tech/documentation/examples/graphrag-qdrant-neo4j/\#end-to-end-pipeline) End-to-End Pipeline

Finally, let’s integrate everything into an end-to-end pipeline where we ingest some sample data, run the retrieval process, and query the language model.

```python
if __name__ == "__main__":
    print("Script started")
    print("Loading environment variables...")
    load_dotenv('.env.local')
    print("Environment variables loaded")

    print("Initializing clients...")
    neo4j_driver = GraphDatabase.driver(neo4j_uri, auth=(neo4j_username, neo4j_password))
    qdrant_client = QdrantClient(
        url=qdrant_url,
        api_key=qdrant_key
    )
    print("Clients initialized")

    print("Creating collection...")
    collection_name = "graphRAGstoreds"
    vector_dimension = 1536
    create_collection(qdrant_client, collection_name, vector_dimension)
    print("Collection created/verified")

    print("Extracting graph components...")

    raw_data = """Alice is a data scientist at TechCorp's Seattle office.
    Bob and Carol collaborate on the Alpha project.
    Carol transferred to the New York office last year.
    Dave mentors both Alice and Bob.
    TechCorp's headquarters is in Seattle.
    Carol leads the East Coast team.
    Dave started his career in Seattle.
    The Alpha project is managed from New York.
    Alice previously worked with Carol at DataCo.
    Bob joined the team after Dave's recommendation.
    Eve runs the West Coast operations from Seattle.
    Frank works with Carol on client relations.
    The New York office expanded under Carol's leadership.
    Dave's team spans multiple locations.
    Alice visits Seattle monthly for team meetings.
    Bob's expertise is crucial for the Alpha project.
    Carol implemented new processes in New York.
    Eve and Dave collaborated on previous projects.
    Frank reports to the New York office.
    TechCorp's main AI research is in Seattle.
    The Alpha project revolutionized East Coast operations.
    Dave oversees projects in both offices.
    Bob's contributions are mainly remote.
    Carol's team grew significantly after moving to New York.
    Seattle remains the technology hub for TechCorp."""

    nodes, relationships = extract_graph_components(raw_data)
    print("Nodes:", nodes)
    print("Relationships:", relationships)

    print("Ingesting to Neo4j...")
    node_id_mapping = ingest_to_neo4j(nodes, relationships)
    print("Neo4j ingestion complete")

    print("Ingesting to Qdrant...")
    ingest_to_qdrant(collection_name, raw_data, node_id_mapping)
    print("Qdrant ingestion complete")

    query = "How is Bob connected to New York?"
    print("Starting retriever search...")
    retriever_result = retriever_search(neo4j_driver, qdrant_client, collection_name, query)
    print("Retriever results:", retriever_result)

    print("Extracting entity IDs...")
    entity_ids = [item.content.split("'id': '")[1].split("'")[0] for item in retriever_result.items]
    print("Entity IDs:", entity_ids)

    print("Fetching related graph...")
    subgraph = fetch_related_graph(neo4j_driver, entity_ids)
    print("Subgraph:", subgraph)

    print("Formatting graph context...")
    graph_context = format_graph_context(subgraph)
    print("Graph context:", graph_context)

    print("Running GraphRAG...")
    answer = graphRAG_run(graph_context, query)
    print("Final Answer:", answer)

```

* * *

Here’s what’s happening:

- First, the user query is defined (“How is Bob connected to New York?”).
- The QdrantNeo4jRetriever searches for related entities in the Qdrant vector database based on the user query’s embedding. It retrieves the top 5 results (top\_k=5).
- The entity\_ids are extracted from the retriever result.
- The fetch\_related\_graph function retrieves related entities and their relationships from the Neo4j database.
- The format\_graph\_context function prepares the graph data in a format the LLM can understand.
- Finally, the graphRAG\_run function is called to generate and query the language model, producing an answer based on the retrieved graph context.

With this, we have successfully created GraphRAG, a system capable of capturing complex relationships and delivering improved performance compared to the baseline RAG approach.