# Store documents in Meilisearch
embeddings = OpenAIEmbeddings()
embedders = { 
        "custom": {
            "source": "userProvided",
            "dimensions": 1536
        }
    }
embedder_name = "custom" 
vector_store = Meilisearch.from_documents(documents=documents, embedding=embeddings, embedders=embedders, embedder_name=embedder_name)

print("Started importing documents")
```

Your Meilisearch instance will now contain your documents. Meilisearch runs tasks like document import asynchronously, so you might need to wait a bit for documents to be available. Consult [the asynchronous operations explanation](/learn/async/asynchronous_operations) for more information on how tasks work.

## Performing similarity search

Your database is now populated with the data from the movies dataset. Create a new `search.py` file to make a semantic search query: searching for documents using similarity search.

```python theme={null}