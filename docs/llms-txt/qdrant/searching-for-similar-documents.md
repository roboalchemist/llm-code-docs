# Searching for similar documents
result = client.search(
    collection_name=COLLECTION_NAME,
    query_vector=models.NamedSparseVector(
        name="text",
        vector=models.SparseVector(
            indices=query_indices,
            values=query_values,
        ),
    ),
    with_vectors=True,
)

result

```

In the above code, we execute a search against our collection using the prepared sparse vector query. The `client.search` method takes the collection name and the query vector as inputs. The query vector is constructed using the `models.NamedSparseVector`, which includes the indices and values derived from the query text. This is a crucial step in efficiently retrieving relevant documents.

```python
ScoredPoint(
    id=1,
    version=0,
    score=3.4292831420898438,
    payload={},
    vector={
        "text": SparseVector(
            indices=[2001, 2002, 2010, 2018, 2032, ...],
            values=[\
                1.0660614967346191,\
                1.391068458557129,\
                0.8903818726539612,\
                0.2502821087837219,\
                ...,\
            ],
        )
    },
)

```

The result, as shown above, is a `ScoredPoint` object containing the ID of the retrieved document, its version, a similarity score, and the sparse vector. The score is a key element as it quantifies the similarity between the query and the document, based on their respective vectors.

To understand how this scoring works, we use the familiar dot product method:

Similarity(Query,Document)=∑i∈IQueryi×Documenti

This formula calculates the similarity score by multiplying corresponding elements of the query and document vectors and summing these products. This method is particularly effective with sparse vectors, where many elements are zero, leading to a computationally efficient process. The higher the score, the greater the similarity between the query and the document, making it a valuable metric for assessing the relevance of the retrieved documents.

## [Anchor](https://qdrant.tech/articles/sparse-vectors/\#hybrid-search-combining-sparse-and-dense-vectors) Hybrid search: combining sparse and dense vectors

By combining search results from both dense and sparse vectors, you can achieve a hybrid search that is both efficient and accurate.
Results from sparse vectors will guarantee, that all results with the required keywords are returned,
while dense vectors will cover the semantically similar results.

The mixture of dense and sparse results can be presented directly to the user, or used as a first stage of a two-stage retrieval process.

Let’s see how you can make a hybrid search query in Qdrant.

First, you need to create a collection with both dense and sparse vectors:

```python
client.create_collection(
    collection_name=COLLECTION_NAME,
    vectors_config={
        "text-dense": models.VectorParams(
            size=1536,  # OpenAI Embeddings
            distance=models.Distance.COSINE,
        )
    },
    sparse_vectors_config={
        "text-sparse": models.SparseVectorParams(
            index=models.SparseIndexParams(
                on_disk=False,
            )
        )
    },
)

```

Then, assuming you have upserted both dense and sparse vectors, you can query them together:

```python
query_text = "Who was Arthur Ashe?"