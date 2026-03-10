# Search for nearest neighbors of the negated mean vector
response = client.search_groups(
    settings.QDRANT_COLLECTION,
    query_vector=negated_vector.tolist(),
    group_by=settings.GROUP_BY_FIELD,
    limit=search_query.limit,
)

```

#### [Anchor](https://qdrant.tech/articles/food-discovery-demo/\#positive-and-negative-feedback) Positive and negative feedback

Since the [Recommendation API](https://qdrant.tech/documentation/concepts/search/#recommendation-api) requires at least one positive example, we can use it only when
the user has liked at least one dish. We could theoretically use the same trick as above and negate the disliked dishes, but it would be a bit weird, as Qdrant has
that feature already built-in, and we can call it just once to do the job. It’s always better to perform the search server-side. Thus, in this case [we just call\\
the Qdrant server with a list of positive and negative examples](https://github.com/qdrant/demo-food-discovery/blob/6b49e11cfbd6412637d527cdd62fe9b9f74ac699/backend/discovery.py#L166),
so it can find some points which are close to the positive examples and far from the negative ones.

```python
response = client.recommend_groups(
    settings.QDRANT_COLLECTION,
    positive=search_query.positive,
    negative=search_query.negative,
    group_by=settings.GROUP_BY_FIELD,
    limit=search_query.limit,
)

```

From the user perspective nothing changes comparing to the previous case.

### [Anchor](https://qdrant.tech/articles/food-discovery-demo/\#location-based-search) Location-based search

Last but not least, location plays an important role in the food discovery process. You are definitely looking for something you can find nearby, not on the other
side of the globe. Therefore, your current location can be toggled as a filtering condition. You can enable it by clicking on “Find near me” icon
in the top right. This way you can find the best pizza in your neighborhood, not in the whole world. Qdrant [geo radius filter](https://qdrant.tech/documentation/concepts/filtering/#geo-radius) is a perfect choice for this. It lets you
filter the results by distance from a given point.

```python
from qdrant_client import models