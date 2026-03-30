# Create sparse vector from my_ratings
def to_vector(ratings):
    vector = SparseVector(
        values=[],
        indices=[]
    )
    for movie_id, rating in ratings.items():
        vector.values.append(rating)
        vector.indices.append(movie_id)
    return vector

```

### [Anchor](https://qdrant.tech/documentation/advanced-tutorials/collaborative-filtering/\#run-the-query) Run the query

From the uploaded list of movies with ratings, we can perform a search in Qdrant to get the top most similar users to us.

```python