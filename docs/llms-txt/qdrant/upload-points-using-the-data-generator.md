# Upload points using the data generator
qdrant_client.upload_points(
    collection_name=collection_name,
    points=data_generator()
)

```

### [Anchor](https://qdrant.tech/documentation/advanced-tutorials/collaborative-filtering/\#define-query) Define query

In order to get recommendations, we need to find users with similar tastes to ours.
Let’s describe our preferences by providing ratings for some of our favorite movies.

`1` indicates that we like the movie, `-1` indicates that we dislike it.

```python
my_ratings = {
    603: 1,     # Matrix
    13475: 1,   # Star Trek
    11: 1,      # Star Wars
    1091: -1,   # The Thing
    862: 1,     # Toy Story
    597: -1,    # Titanic
    680: -1,    # Pulp Fiction
    13: 1,      # Forrest Gump
    120: 1,     # Lord of the Rings
    87: -1,     # Indiana Jones
    562: -1     # Die Hard
}

```

Click to see the code for `to_vector`

```python