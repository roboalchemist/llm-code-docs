# Initialize Qdrant client
qdrant_client = QdrantClient(
    url=qdrant_url,
    api_key=qdrant_key
)

```

* * *

- **Neo4j:** We set up a connection to the Neo4j graph database.
- **Qdrant:** We initialize the connection to the Qdrant vector store.

This will connect with Neo4j and Qdrant, and we can now start with Ingestion.

## [Anchor](https://qdrant.tech/documentation/examples/graphrag-qdrant-neo4j/\#ingestion-1) Ingestion

We will follow the workflow of the ingestion pipeline presented in the architecture section. Let’s examine it implementation-wise.

### [Anchor](https://qdrant.tech/documentation/examples/graphrag-qdrant-neo4j/\#defining-output-parser) Defining Output Parser

The single and GraphComponents classes structure the LLM’s responses into a usable format.

```python
class single(BaseModel):
    node: str
    target_node: str
    relationship: str

class GraphComponents(BaseModel):
    graph: list[single]

```

* * *

These classes help ensure that data from the OpenAI LLM is parsed correctly into the graph components (nodes and relationships).

### [Anchor](https://qdrant.tech/documentation/examples/graphrag-qdrant-neo4j/\#defining-openai-client-and-llm-parser-function) Defining OpenAI Client and LLM Parser Function

We now initialize the OpenAI client and define a function to send prompts to the LLM and parse its responses.

```python
client = OpenAI()

def openai_llm_parser(prompt):
    completion = client.chat.completions.create(
        model="gpt-4o-2024-08-06",
        response_format={"type": "json_object"},
        messages=[\
            {\
                "role": "system",\
                "content":\
\
                """ You are a precise graph relationship extractor. Extract all\
                    relationships from the text and format them as a JSON object\
                    with this exact structure:\
                    {\
                        "graph": [\
                            {"node": "Person/Entity",\
                             "target_node": "Related Entity",\
                             "relationship": "Type of Relationship"},\
                            ...more relationships...\
                        ]\
                    }\
                    Include ALL relationships mentioned in the text, including\
                    implicit ones. Be thorough and precise. """\
\
            },\
            {\
                "role": "user",\
                "content": prompt\
            }\
        ]
    )

    return GraphComponents.model_validate_json(completion.choices[0].message.content)


```

* * *

This function sends a prompt to the LLM, asking it to extract graph components (nodes and relationships) from the provided text. The response is parsed into structured graph data.

### [Anchor](https://qdrant.tech/documentation/examples/graphrag-qdrant-neo4j/\#extracting-graph-components) Extracting Graph Components

The function extract\_graph\_components processes raw data, extracting the nodes and relationships as graph components.

```python
def extract_graph_components(raw_data):
    prompt = f"Extract nodes and relationships from the following text:\n{raw_data}"

    parsed_response = openai_llm_parser(prompt)  # Assuming this returns a list of dictionaries
    parsed_response = parsed_response.graph  # Assuming the 'graph' structure is a key in the parsed response

    nodes = {}
    relationships = []

    for entry in parsed_response:
        node = entry.node
        target_node = entry.target_node  # Get target node if available
        relationship = entry.relationship  # Get relationship if available

        # Add nodes to the dictionary with a unique ID
        if node not in nodes:
            nodes[node] = str(uuid.uuid4())

        if target_node and target_node not in nodes:
            nodes[target_node] = str(uuid.uuid4())

        # Add relationship to the relationships list with node IDs
        if target_node and relationship:
            relationships.append({
                "source": nodes[node],
                "target": nodes[target_node],
                "type": relationship
            })

    return nodes, relationships

```

* * *

This function takes raw data, uses the LLM to parse it into graph components, and then assigns unique IDs to nodes and relationships.

### [Anchor](https://qdrant.tech/documentation/examples/graphrag-qdrant-neo4j/\#ingesting-data-to-neo4j) Ingesting Data to Neo4j

The function ingest\_to\_neo4j ingests the extracted graph data (nodes and relationships) into Neo4j.

```python
def ingest_to_neo4j(nodes, relationships):
    """
    Ingest nodes and relationships into Neo4j.
    """

    with neo4j_driver.session() as session:
        # Create nodes in Neo4j
        for name, node_id in nodes.items():
            session.run(
                "CREATE (n:Entity {id: $id, name: $name})",
                id=node_id,
                name=name
            )

        # Create relationships in Neo4j
        for relationship in relationships:
            session.run(
                "MATCH (a:Entity {id: $source_id}), (b:Entity {id: $target_id}) "
                "CREATE (a)-[:RELATIONSHIP {type: $type}]->(b)",
                source_id=relationship["source"],
                target_id=relationship["target"],
                type=relationship["type"]
            )

    return nodes

```

* * *

Here, we create nodes and relationships in the Neo4j graph database. Nodes are entities, and relationships link these entities.

This will ingest the data into Neo4j and on a sample dataset it looks something like this:

![image4](https://qdrant.tech/documentation/examples/graphrag-qdrant-neo4j/image4.png)

Fig 4: Visualization of the Knowledge Graph

Let’s explore how to map nodes with their IDs and integrate this information, along with vectors, into Qdrant. First, let’s create a Qdrant collection.

### [Anchor](https://qdrant.tech/documentation/examples/graphrag-qdrant-neo4j/\#creating-qdrant-collection) Creating Qdrant Collection

You can create a collection once you have set up your Qdrant instance. A collection in Qdrant holds vectors for search and retrieval.

```python
def create_collection(client, collection_name, vector_dimension):

```

try:

```python