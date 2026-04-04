# Retrieve the disliked points based on their ids
disliked_points, _ = client.scroll(
    settings.QDRANT_COLLECTION,
    scroll_filter=models.Filter(
        must=[\
            models.HasIdCondition(has_id=search_query.negative),\
        ]
    ),
    with_vectors=True,
)