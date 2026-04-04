# using the Reciprocal Rank Fusion.
sparse_dense_rrf_prefetch = models.Prefetch(
    prefetch=[\
        models.Prefetch(\
            prefetch=[\
                # The first prefetch operation retrieves 100 documents\
                # using dense vectors using integer data type. Retrieval\
                # is faster, but quality is lower.\
                models.Prefetch(\
                    query=[7, 63, ..., 92],\
                    using="dense-uint8",\
                    limit=100,\
                )\
            ],\
            # Integer-based embeddings are then re-ranked using the\
            # float-based embeddings. Here we just want to retrieve\
            # 25 documents.\
            query=[-1.234, 0.762, ..., 1.532],\
            using="dense",\
            limit=25,\
        ),\
        # Here we just add another 25 documents using the sparse\
        # vectors only.\
        models.Prefetch(\
            query=models.SparseVector(\
                indices=[125, 9325, 58214],\
                values=[-0.164, 0.229, 0.731],\
            ),\
            using="sparse",\
            limit=25,\
        ),\
    ],
    # RRF is activated below, so there is no need to specify the
    # query vector here, as fusion is done on the scores of the
    # retrieved documents.
    query=models.FusionQuery(
        fusion=models.Fusion.RRF,
    ),
)

```

The second branch could have already been called hybrid, as it combines the results from the dense and sparse vectors
with fusion. However, nothing stops us from building even more complex search pipelines.

Here is how the target call to the Query API would look like in Python:

```python
client.query_points(
    "my-collection",
    prefetch=[\
        matryoshka_prefetch,\
        sparse_dense_rrf_prefetch,\
    ],
    # Finally rerank the results with the late interaction model. It only
    # considers the documents retrieved by all the prefetch operations above.
    # Return 10 final results.
    query=[\
        [1.928, -0.654, ..., 0.213],\
        [-1.197, 0.583, ..., 1.901],\
        ...,\
        [0.112, -1.473, ..., 1.786],\
    ],
    using="late-interaction",
    with_payload=False,
    limit=10,
)

```

The options are endless, the new Query API gives you the flexibility to experiment with different setups. **You**
**rarely need to build such a complex search pipeline**, but it’s good to know that you can do that if needed.

## [Anchor](https://qdrant.tech/articles/hybrid-search/\#lessons-learned-multi-vector-representations) Lessons learned: multi-vector representations

Many of you have already started building hybrid search systems and reached out to us with questions and feedback.
We’ve seen many different approaches, however one recurring idea was to utilize **multi-vector representations with**
**ColBERT-style models as a reranking step**, after retrieving candidates with single-vector dense and/or sparse methods.
This reflects the latest trends in the field, as single-vector methods are still the most efficient, but multivectors
capture the nuances of the text better.

![Reranking with late interaction models](https://qdrant.tech/articles_data/hybrid-search/late-interaction-reranking.png)

Assuming you never use late interaction models for retrieval alone, but only for reranking, this setup comes with a
hidden cost. By default, each configured dense vector of the collection will have a corresponding HNSW graph created.
Even, if it is a multi-vector.

```python
from qdrant_client import QdrantClient, models

client = QdrantClient(...)
client.create_collection(
    collection_name="my-collection",
    vectors_config={
        "dense": models.VectorParams(...),
        "late-interaction": models.VectorParams(
            size=128,
            distance=models.Distance.COSINE,
            multivector_config=models.MultiVectorConfig(
                comparator=models.MultiVectorComparator.MAX_SIM
            ),
        )
    },
    sparse_vectors_config={
        "sparse": models.SparseVectorParams(...)
    },
)

```

Reranking will never use the created graph, as all the candidates are already retrieved. Multi-vector ranking will only
be applied to the candidates retrieved by the previous steps, so no search operation is needed. HNSW becomes redundant
while still the indexing process has to be performed, and in that case, it will be quite heavy. ColBERT-like models
create hundreds of embeddings for each document, so the overhead is significant. **To avoid it, you can disable the HNSW**
**graph creation for this kind of model**:

```python
client.create_collection(
    collection_name="my-collection",
    vectors_config={
        "dense": models.VectorParams(...),
        "late-interaction": models.VectorParams(
            size=128,
            distance=models.Distance.COSINE,
            multivector_config=models.MultiVectorConfig(
                comparator=models.MultiVectorComparator.MAX_SIM
            ),
            hnsw_config=models.HnswConfigDiff(
                m=0,  # Disable HNSW graph creation
            ),
        )
    },
    sparse_vectors_config={
        "sparse": models.SparseVectorParams(...)
    },
)

```

You won’t notice any difference in the search performance, but the use of resources will be significantly lower when you
upload the embeddings to the collection.

## [Anchor](https://qdrant.tech/articles/hybrid-search/\#some-anecdotal-observations) Some anecdotal observations

Neither of the algorithms performs best in all cases. In some cases, keyword-based search
will be the winner and vice-versa. The following table shows some interesting examples we could find in the
[WANDS](https://github.com/wayfair/WANDS) dataset during experimentation:

| Query | BM25 Search | Vector Search |
| --- | --- | --- |
| cybersport desk | desk ❌ | gaming desk ✅ |
| plates for icecream | "eat" plates on wood wall décor ❌ | alicyn 8.5 '' melamine dessert plate ✅ |
| kitchen table with a thick board | craft kitchen acacia wood cutting board ❌ | industrial solid wood dining table ✅ |
| wooden bedside table | 30 '' bedside table lamp ❌ | portable bedside end table ✅ |

Also examples where keyword-based search did better:

| Query | BM25 Search | Vector Search |
| --- | --- | --- |
| computer chair | vibrant computer task chair ✅ | office chair ❌ |
| 64.2 inch console table | cervantez 64.2 '' console table ✅ | 69.5 '' console table ❌ |

## [Anchor](https://qdrant.tech/articles/hybrid-search/\#try-the-new-query-api-in-qdrant-110) Try the New Query API in Qdrant 1.10

The new Query API introduced in Qdrant 1.10 is a game-changer for building hybrid search systems. You don’t need any
additional services to combine the results from different search methods, and you can even create more complex pipelines
and serve them directly from Qdrant.

Our webinar on _Building the Ultimate Hybrid Search_ takes you through the process of building a hybrid search system
with Qdrant Query API. If you missed it, you can [watch the recording](https://www.youtube.com/watch?v=LAZOxqzceEU), or
[check the notebooks](https://github.com/qdrant/workshop-ultimate-hybrid-search).

How to Build the Ultimate Hybrid Search with Qdrant - YouTube

[Photo image of Qdrant - Vector Database & Search Engine](https://www.youtube.com/channel/UC6ftm8PwH1RU_LM1jwG0LQA?embeds_referring_euri=https%3A%2F%2Fqdrant.tech%2F)

Qdrant - Vector Database & Search Engine

8.12K subscribers

[How to Build the Ultimate Hybrid Search with Qdrant](https://www.youtube.com/watch?v=LAZOxqzceEU)

Qdrant - Vector Database & Search Engine

Search

Watch later

Share

Copy link

Info

Shopping

Tap to unmute

If playback doesn't begin shortly, try restarting your device.

More videos

## More videos

You're signed out

Videos you watch may be added to the TV's watch history and influence TV recommendations. To avoid this, cancel and sign in to YouTube on your computer.

CancelConfirm

Share

Include playlist

An error occurred while retrieving sharing information. Please try again later.

[Watch on](https://www.youtube.com/watch?v=LAZOxqzceEU&embeds_referring_euri=https%3A%2F%2Fqdrant.tech%2F)

0:00

0:00 / 1:01:18
•Live

•

[Watch on YouTube](https://www.youtube.com/watch?v=LAZOxqzceEU "Watch on YouTube")

If you have any questions or need help with building your hybrid search system, don’t hesitate to reach out to us on
[Discord](https://qdrant.to/discord).

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/articles/hybrid-search.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/articles/hybrid-search.md)
- [Create an issue](https://github.com/qdrant/landing_page/issues/new/choose)

×

[Powered by](https://qdrant.tech/)

<|page-94-lllmstxt|>
## why-rust
- [Articles](https://qdrant.tech/articles/)
- Why Rust?

[Back to Qdrant Articles](https://qdrant.tech/articles/)