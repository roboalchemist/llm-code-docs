# Resulting query embedding is a tensor of shape (22, 128)
query_embedding = model(**processed_queries)[0]

```

Now let’s design a function for the two-stage retrieval with multivectors produced by VLLMs:

- **Step 1:** Prefetch results using a compressed multivector representation & HNSW index.
- **Step 2:** Re-rank the prefetched results using the original multivector representation.

Let’s query our collections using combined mean pooled representations for the first stage of retrieval.

```python