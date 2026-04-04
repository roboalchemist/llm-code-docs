# Create collection
if not client.collection_exists(collection_name):
    client.create_collection(
        collection_name=collection_name,
        vectors_config={
            "dense": models.VectorParams(size=384, distance=models.Distance.COSINE),
            "colbert": models.VectorParams(
                size=128,
                distance=models.Distance.COSINE,
                multivector_config=models.MultiVectorConfig(
                    comparator=models.MultiVectorComparator.MAX_SIM
                ),
                hnsw_config=models.HnswConfigDiff(m=0),  # reranker: no indexing
            ),
        },
    )

```

We disable indexing for the ColBERT multivector since it will only be used for reranking. To learn more about this, check out the [How to Effectively Use Multivector Representations in Qdrant for Reranking](https://qdrant.tech/documentation/advanced-tutorials/using-multivector-representations/) article.

### [Anchor](https://qdrant.tech/documentation/examples/qdrant-dspy-medicalbot/\#batch-uploading-to-qdrant) Batch Uploading to Qdrant

To avoid hitting API limits, we upload the data in batches, each batch containing:

- The passage text
- ColBERT and dense embeddings.
- `year` and `specialty` metadata fields.

```python
BATCH_SIZE = 3
points_batch = []

for i in range(len(ds["passage_text"])):
    point = models.PointStruct(
        id=i,
        vector={"dense": dense_documents[i], "colbert": colbert_documents[i]},
        payload={
            "passage_text": ds["passage_text"][i],
            "year": ds["year"][i],
            "specialty": ds["specialty"][i],
        },
    )
    points_batch.append(point)

    if len(points_batch) == BATCH_SIZE:
        client.upsert(collection_name=collection_name, points=points_batch)
        print(f"Uploaded batch ending at index {i}")
        points_batch = []