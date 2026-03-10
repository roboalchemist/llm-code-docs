# using the Matryoshka embeddings with multistep retrieval.
matryoshka_prefetch = models.Prefetch(
    prefetch=[\
        models.Prefetch(\
            prefetch=[\
                # The first prefetch operation retrieves 100 documents\
                # using the Matryoshka embeddings with the lowest\
                # dimensionality of 64.\
                models.Prefetch(\
                    query=[0.456, -0.789, ..., 0.239],\
                    using="matryoshka-64dim",\
                    limit=100,\
                ),\
            ],\
            # Then, the retrieved documents are re-ranked using the\
            # Matryoshka embeddings with the dimensionality of 128.\
            query=[0.456, -0.789, ..., -0.789],\
            using="matryoshka-128dim",\
            limit=50,\
        )\
    ],
    # Finally, the results are re-ranked using the Matryoshka
    # embeddings with the dimensionality of 256.
    query=[0.456, -0.789, ..., 0.123],
    using="matryoshka-256dim",
    limit=25,
)

```

Similarly, we can build the second branch of our search pipeline, which retrieves the documents using the dense and
sparse vectors and performs the fusion of them using the Reciprocal Rank Fusion method:

```python