# Insert sparse vector into Qdrant collection
point_id = 1  # Assign a unique ID for the point

```

### [Anchor](https://qdrant.tech/articles/sparse-vectors/\#2-create-a-collection-with-sparse-vector-support) 2\. Create a collection with sparse vector support

```python
client.create_collection(
    collection_name=COLLECTION_NAME,
    vectors_config={},
    sparse_vectors_config={
        "text": models.SparseVectorParams(
            index=models.SparseIndexParams(
                on_disk=False,
            )
        )
    },
)

```

### [Anchor](https://qdrant.tech/articles/sparse-vectors/\#3-insert-sparse-vectors) 3\. Insert sparse vectors

Here, we see the process of inserting a sparse vector into the Qdrant collection. This step is key to building a dataset that can be quickly retrieved in the first stage of the retrieval process, utilizing the efficiency of sparse vectors. Since this is for demonstration purposes, we insert only one point with Sparse Vector and no dense vector.

```python
client.upsert(
    collection_name=COLLECTION_NAME,
    points=[\
        models.PointStruct(\
            id=point_id,\
            payload={},  # Add any additional payload if necessary\
            vector={\
                "text": models.SparseVector(\
                    indices=indices.tolist(), values=values.tolist()\
                )\
            },\
        )\
    ],
)

```

By upserting points with sparse vectors, we prepare our dataset for rapid first-stage retrieval, laying the groundwork for subsequent detailed analysis using dense vectors. Notice that we use “text” to denote the name of the sparse vector.

Those familiar with the Qdrant API will notice that the extra care taken to be consistent with the existing named vectors API – this is to make it easier to use sparse vectors in existing codebases. As always, you’re able to **apply payload filters**, shard keys, and other advanced features you’ve come to expect from Qdrant. To make things easier for you, the indices and values don’t have to be sorted before upsert. Qdrant will sort them when the index is persisted e.g. on disk.

### [Anchor](https://qdrant.tech/articles/sparse-vectors/\#4-query-with-sparse-vectors) 4\. Query with sparse vectors

We use the same process to prepare a query vector as well. This involves computing the vector from a query text and extracting its indices and values. We then use these details to construct a query against our collection.

```python