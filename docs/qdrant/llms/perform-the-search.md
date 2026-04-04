# Perform the search
results = qdrant_client.query_points(
    collection_name=collection_name,
    query=to_vector(my_ratings),
    using="ratings",
    limit=20
).points

```

Now we can find the movies liked by the other similar users, but we haven’t seen yet.
Let’s combine the results from found users, filter out seen movies, and sort by the score.

```python