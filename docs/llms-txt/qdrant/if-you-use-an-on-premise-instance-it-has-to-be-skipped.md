# If you use an on-premise instance, it has to be skipped.
qdrant_client = QdrantClient(
    host="xyz-example.eu-central.aws.cloud.qdrant.io",
    prefer_grpc=True,
    api_key=QDRANT_API_KEY,
)

```

Now we’re able to vectorize all the answers. They are going to form our collection, so we can also put them already into Qdrant, along with the
payloads and identifiers. That will make our dataset easily searchable.

```python
answer_response = cohere_client.embed(
    texts=dataset["train"]["long_answer"],
    model="large",
)
vectors = [\
    # Conversion to float is required for Qdrant\
    list(map(float, vector))\
    for vector in answer_response.embeddings\
]
ids = [entry["pubid"] for entry in dataset["train"]]