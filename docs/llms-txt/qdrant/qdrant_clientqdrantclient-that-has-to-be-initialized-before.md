# qdrant_client.QdrantClient that has to be initialized before
response = client.search_groups(
    settings.QDRANT_COLLECTION,
    query_vector=query_vector,
    group_by=settings.GROUP_BY_FIELD,
    limit=search_query.limit,
)

```

### [Anchor](https://qdrant.tech/articles/food-discovery-demo/\#exploring-the-results) Exploring the results

The main feature of the demo is the ability to explore the space of the dishes. You can click on any of them to see more details, but first of all you can like or dislike it,
and the demo will update the search results accordingly.

![Recommendation results](https://qdrant.tech/articles_data/food-discovery-demo/recommendation-results.png)

#### [Anchor](https://qdrant.tech/articles/food-discovery-demo/\#negative-feedback-only) Negative feedback only

Qdrant [Recommendation API](https://qdrant.tech/documentation/concepts/search/#recommendation-api) needs at least one positive example to work. However, in our demo
we want to be able to provide only negative examples. This is because we want to be able to say “I don’t like this dish” without having to like anything first.
To achieve this, we use a trick. We negate the vectors of the disliked dishes and use their mean as a query. This way, the disliked dishes will be pushed away
from the search results. **This works because the cosine distance is based on the angle between two vectors, and the angle between a vector and its negation is 180 degrees.**

![CLIP model](https://qdrant.tech/articles_data/food-discovery-demo/negated-vector.png)

Food Discovery Demo [implements that trick](https://github.com/qdrant/demo-food-discovery/blob/6b49e11cfbd6412637d527cdd62fe9b9f74ac699/backend/discovery.py#L122)
by calling Qdrant twice. Initially, we use the [Scroll API](https://qdrant.tech/documentation/concepts/points/#scroll-points) to find disliked items,
and then calculate a negated mean of all their vectors. That allows using the [Search Groups API](https://qdrant.tech/documentation/concepts/search/#search-groups)
to find the nearest neighbors of the negated mean vector.

```python
import numpy as np