# Output: Qdrant is a vector database & vector similarity search engine. 0.60551536

```

The description of Qdrant was the best match, even though it didn’t mention large language models
at all. However, it was the only document that belonged to the `qdrant` library, so there was no
other choice. Let’s try to search for something that is not present in the collection.

Let’s define another retrieve, this time for the `llama-index` library:

```python
llama_index_retriever = index.as_retriever(
    filters=MetadataFilters(
        filters=[\
            ExactMatchFilter(\
                key="library",\
                value="llama-index",\
            )\
        ]
    )
)

nodes_with_scores = llama_index_retriever.retrieve("large language models")
for node in nodes_with_scores:
    print(node.text, node.score)