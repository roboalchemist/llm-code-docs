# [Anchor](https://qdrant.tech/documentation/examples/graphrag-qdrant-neo4j/\#introduction-to-graphrag) Introduction to GraphRAG

Unlike RAG, which typically relies on document retrieval, GraphRAG builds knowledge graphs (KGs) to capture entities and their relationships. For datasets or use cases that demand human-level intelligence from an AI system, GraphRAG offers a promising solution:

- It can follow chains of relationships to answer complex queries, making it suitable for better reasoning beyond simple document retrieval.
- The graph structure allows a deeper understanding of the context, leading to more accurate and relevant responses.

The workflow of GraphRAG is as follows:

1. The LLM analyzes the dataset to identify entities (people, places, organizations) and their relationships, creating a comprehensive knowledge graph where entities are nodes and their connections form edges.
2. A bottom-up clustering algorithm organizes the KG into hierarchical semantic groups. This creates meaningful segments of related information, enabling understanding at different levels of abstraction.
3. GraphRAG uses both the KG and semantic clusters to select a relevant context for the LLM when answering queries.

![image2](https://qdrant.tech/documentation/examples/graphrag-qdrant-neo4j/image2.png)

[Fig](https://arxiv.org/pdf/2404.16130) 1: A Complete Picture of GraphRAG Ingestion and Retrieval

### [Anchor](https://qdrant.tech/documentation/examples/graphrag-qdrant-neo4j/\#challenges-of-graphrag) Challenges of GraphRAG

Despite its advantages, the LLM-centric GraphRAG approach faces several challenges:

- **KG Construction with LLMs:** Since the LLM is responsible for constructing the knowledge graph, there are risks such as inconsistencies, propagation of biases or errors, and lack of control over the ontology used. However, we used a LLM to extract the ontology in our implementation.
- **Querying KG with LLMs:** Once the graph is constructed, an LLM translates the human query into Cypher (Neo4j’s declarative query language). However, crafting complex queries in Cypher may result in inaccurate outcomes.
- **Scalability & Cost Consideration:** To be practical, applications must be both scalable and cost-effective. Relying on LLMs increases costs and decreases scalability, as they are used every time data is added, queried, or generated.

To address these challenges, a more controlled and structured knowledge representation system may be required for GraphRAG to function optimally at scale.