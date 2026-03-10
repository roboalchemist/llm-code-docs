# Convert ratings to sparse vectors
user_sparse_vectors = defaultdict(lambda: {"values": [], "indices": []})
for row in ratings_agg_df.itertuples():
    user_sparse_vectors[row.userId]["values"].append(row.rating)
    user_sparse_vectors[row.userId]["indices"].append(int(row.movieId))

```

![collaborative-filtering](https://qdrant.tech/blog/collaborative-filtering/collaborative-filtering.png)

### [Anchor](https://qdrant.tech/documentation/advanced-tutorials/collaborative-filtering/\#upload-the-data) Upload the data

Here, you will initialize the Qdrant client and create a new collection to store the data.
Convert the user ratings to sparse vectors and include the `movieId` in the payload.

```python