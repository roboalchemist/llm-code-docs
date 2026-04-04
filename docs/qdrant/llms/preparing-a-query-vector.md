# Preparing a query vector

query_text = "Who was Arthur Ashe?"
query_vec, query_tokens = compute_vector(query_text)
query_vec.shape

query_indices = query_vec.nonzero().numpy().flatten()
query_values = query_vec.detach().numpy()[query_indices]

```

In this example, we use the same model for both document and query. This is not a requirement, but it’s a simpler approach.

### [Anchor](https://qdrant.tech/articles/sparse-vectors/\#5-retrieve-and-interpret-results) 5\. Retrieve and interpret results

After setting up the collection and inserting sparse vectors, the next critical step is retrieving and interpreting the results. This process involves executing a search query and then analyzing the returned results.

```python