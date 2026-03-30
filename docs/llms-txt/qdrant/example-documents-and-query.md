# Example documents and query
documents = [\
    "Artificial intelligence is used in hospitals for cancer diagnosis and treatment.",\
    "Self-driving cars use AI to detect obstacles and make driving decisions.",\
    "AI is transforming customer service through chatbots and automation.",\
    # ...\
]
query_text = "How does AI help in medicine?"

dense_documents = [\
    models.Document(text=doc, model="BAAI/bge-small-en")\
    for doc in documents\
]
dense_query = models.Document(text=query_text, model="BAAI/bge-small-en")

colbert_documents = [\
    models.Document(text=doc, model="colbert-ir/colbertv2.0")\
    for doc in documents\
]
colbert_query = models.Document(text=query_text, model="colbert-ir/colbertv2.0")

```

### [Anchor](https://qdrant.tech/documentation/advanced-tutorials/using-multivector-representations/\#2-create-a-qdrant-collection) 2\. Create a Qdrant collection

Then create a Qdrant collection with both vector types. Note that we leave indexing on for the `dense` vector but turn it off for the `colbert` vector that will be used for reranking.

```python
collection_name = "dense_multivector_demo"
client.create_collection(
    collection_name=collection_name,
    vectors_config={
        "dense": models.VectorParams(
            size=384,
            distance=models.Distance.COSINE
            # Leave HNSW indexing ON for dense
        ),
        "colbert": models.VectorParams(
            size=128,
            distance=models.Distance.COSINE,
            multivector_config=models.MultiVectorConfig(
                comparator=models.MultiVectorComparator.MAX_SIM
            ),
            hnsw_config=models.HnswConfigDiff(m=0)  # Disable HNSW for reranking
        )
    }
)

```

### [Anchor](https://qdrant.tech/documentation/advanced-tutorials/using-multivector-representations/\#3-upload-documents-dense--multivector) 3\. Upload Documents (Dense + Multivector)

Now upload the vectors:

```python
points = [\
    models.PointStruct(\
        id=i,\
        vector={\
            "dense": dense_documents[i],\
            "colbert": colbert_documents[i]\
        },\
        payload={"text": documents[i]}\
    ) for i in range(len(documents))\
]
client.upsert(collection_name="dense_multivector_demo", points=points)

```

### [Anchor](https://qdrant.tech/documentation/advanced-tutorials/using-multivector-representations/\#query-with-retrieval--reranking-in-one-call) Query with Retrieval + Reranking in One Call

Now let’s run a search:

```python
results = client.query_points(
    collection_name="dense_multivector_demo",
    prefetch=models.Prefetch(
        query=dense_query,
        using="dense",
    ),
    query=colbert_query,
    using="colbert",
    limit=3,
    with_payload=True
)

```

- The dense vector retrieves the top candidates quickly.
- The Colbert multivector reranks them using token-level `MaxSim` with fine-grained precision.
- Returns the top 3 results.

## [Anchor](https://qdrant.tech/documentation/advanced-tutorials/using-multivector-representations/\#conclusion) Conclusion

Multivector search is one of the most powerful features of a vector database when used correctly. With this functionality in Qdrant, you can:

- Store token-level embeddings natively.
- Disable indexing to reduce overhead.
- Run fast retrieval and accurate reranking in one API call.
- Efficiently scale late interaction.

Combining FastEmbed and Qdrant leads to a production-ready pipeline for ColBERT-style reranking without wasting resources. You can do this locally or use Qdrant Cloud. Qdrant offers an easy-to-use API to get started with your search engine, so if you’re ready to dive in, sign up for free at [Qdrant Cloud](https://qdrant.tech/cloud/) and start building.

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/advanced-tutorials/using-multivector-representations.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/advanced-tutorials/using-multivector-representations.md)
- [Create an issue](https://github.com/qdrant/landing_page/issues/new/choose)

×

[Powered by](https://qdrant.tech/)

<|page-11-lllmstxt|>
## cloud-api
- [Documentation](https://qdrant.tech/documentation/)
- Qdrant Cloud API