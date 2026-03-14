# patito.duckdb.Relation.distinct

Relation.distinct()

Drop all duplicate rows of the relation.

Return type:

`TypeVar`(`RelationType`, bound= Relation)

Example

```
>>> import patito as pt
>>> df = pt.DataFrame(
...     [[1, 2, 3], [1, 2, 3], [3, 2, 1]],
...     schema=["a", "b", "c"],
...     orient="row",
... )
>>> relation = pt.duckdb.Relation(df)
>>> relation.to_df()
shape: (3, 3)
┌─────┬─────┬─────┐
│ a   ┆ b   ┆ c   │
│ --- ┆ --- ┆ --- │
│ i64 ┆ i64 ┆ i64 │
╞═════╪═════╪═════╡
│ 1   ┆ 2   ┆ 3   │
│ 1   ┆ 2   ┆ 3   │
│ 3   ┆ 2   ┆ 1   │
└─────┴─────┴─────┘
>>> relation.distinct().to_df()
shape: (2, 3)
┌─────┬─────┬─────┐
│ a   ┆ b   ┆ c   │
│ --- ┆ --- ┆ --- │
│ i64 ┆ i64 ┆ i64 │
╞═════╪═════╪═════╡
│ 1   ┆ 2   ┆ 3   │
│ 3   ┆ 2   ┆ 1   │
└─────┴─────┴─────┘

```