# Generating the embeddings with Cohere client library
embeddings = cohere_client.embed(
    texts=["A test sentence"],
    model="large",
)
vector_size = len(embeddings.embeddings[0])
print(vector_size) # output: 4096

```

Let’s connect to the Qdrant instance first and create a collection with the proper configuration, so we can put some embeddings into it later on.

```python