# Aggregate ratings to handle duplicate (userId, title) pairs
ratings_agg_df = merged_df.groupby(['userId', 'movieId']).rating.mean().reset_index()

ratings_agg_df.head()

```

|  | userId | movieId | rating |
| --- | --- | --- | --- |
| 0 | 1 | 1 | 0.429960 |
| 1 | 1 | 1036 | 1.369846 |
| 2 | 1 | 1049 | -0.509926 |
| 3 | 1 | 1066 | 0.429960 |
| 4 | 1 | 110 | 0.429960 |

### [Anchor](https://qdrant.tech/documentation/advanced-tutorials/collaborative-filtering/\#convert-to-sparse) Convert to sparse

If you want to search across numerous reviews from different users, you can represent these reviews in a sparse matrix.

```python