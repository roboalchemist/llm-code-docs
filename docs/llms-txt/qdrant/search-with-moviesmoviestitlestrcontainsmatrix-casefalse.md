# Search with movies[movies.title.str.contains("Matrix", case=False)].

my_ratings = {
    2571: 1,  # Matrix
    329: 1,   # Star Trek
    260: 1,   # Star Wars
    2288: -1, # The Thing
    1: 1,     # Toy Story
    1721: -1, # Titanic
    296: -1,  # Pulp Fiction
    356: 1,   # Forrest Gump
    2116: 1,  # Lord of the Rings
    1291: -1, # Indiana Jones
    1036: -1  # Die Hard
}

inverse_ratings = {k: -v for k, v in my_ratings.items()}

def to_vector(ratings):
    vector = models.SparseVector(
        values=[],
        indices=[]
    )
    for movie_id, rating in ratings.items():
        vector.values.append(rating)
        vector.indices.append(movie_id)
    return vector

```

Query Qdrant to find users with similar tastes based on the provided personal ratings. The search returns a list of similar users along with their ratings, facilitating collaborative filtering.

```python
results = client.query_points(
    "movielens",
    query=to_vector(my_ratings),
    using="ratings",
    with_vectors=True, # We will use those to find new movies
    limit=20
).points

```

Movie scores are computed based on how frequently each movie appears in the ratings of similar users, weighted by their ratings. This step identifies popular movies among users with similar tastes. Calculate how frequently each movie is found in similar users’ ratings

```python
def results_to_scores(results):
    movie_scores = defaultdict(lambda: 0)

    for user in results:
        user_scores = user.vector['ratings']
        for idx, rating in zip(user_scores.indices, user_scores.values):
            if idx in my_ratings:
                continue
            movie_scores[idx] += rating

    return movie_scores

```

The top-rated movies are sorted based on their scores and printed as recommendations for the user. These recommendations are tailored to the user’s preferences and aligned with their tastes. Sort movies by score and print top five:

```python
movie_scores = results_to_scores(results)
top_movies = sorted(movie_scores.items(), key=lambda x: x[1], reverse=True)

for movie_id, score in top_movies[:5]:
    print(movies[movies.movie_id == movie_id].title.values[0], score)

```

Result:

```text
Star Wars: Episode V - The Empire Strikes Back (1980) 20.02387858
Star Wars: Episode VI - Return of the Jedi (1983) 16.443184379999998
Princess Bride, The (1987) 15.840068229999996
Raiders of the Lost Ark (1981) 14.94489462
Sixth Sense, The (1999) 14.570322149999999

```

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/examples/recommendation-system-ovhcloud.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/examples/recommendation-system-ovhcloud.md)
- [Create an issue](https://github.com/qdrant/landing_page/issues/new/choose)

×

[Powered by](https://qdrant.tech/)

<|page-170-lllmstxt|>
## search
- [Documentation](https://qdrant.tech/documentation/)
- [Concepts](https://qdrant.tech/documentation/concepts/)
- Search