# [Anchor](https://qdrant.tech/documentation/examples/graphrag-qdrant-neo4j/\#rag--its-challenges) RAG & Its Challenges

[RAG](https://qdrant.tech/rag/) combines retrieval-based and generative AI to enhance LLMs with relevant, up-to-date information from a knowledge base, like a vector database. However, RAG faces several challenges:

1. **Understanding Context:** Models may misinterpret queries, particularly when the context is complex or ambiguous, leading to incorrect or irrelevant answers.
2. **Balancing Similarity vs. Relevance:** RAG systems can struggle to ensure that retrieved information is similar and contextually relevant.
3. **Answer Completeness:** Traditional RAGs might not be able to capture all relevant details for complex queries that require LLMs to find relationships in the context that are not explicitly present.