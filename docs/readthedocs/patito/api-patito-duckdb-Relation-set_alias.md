# patito.duckdb.Relation.set_alias

Relation.set_alias(*name*)

Set SQL alias for the given relation to be used in further queries.

Parameters:

**name** (`str`) – The new alias for the given relation.

Returns:

A new relation containing the same query but addressable with the
new alias.

Return type:

Relation

Example

```
>>> import patito as pt
>>> relation_1 = pt.duckdb.Relation("select 1 as a, 2 as b")
>>> relation_2 = pt.duckdb.Relation("select 1 as a, 3 as c")
>>> relation_1.set_alias("x").inner_join(
...     relation_2.set_alias("y"),
...     on="x.a = y.a",
... ).select("x.a", "y.a", "b", "c").to_df()
shape: (1, 4)
┌─────┬─────┬─────┬─────┐
│ a   ┆ a:1 ┆ b   ┆ c   │
│ --- ┆ --- ┆ --- ┆ --- │
│ i64 ┆ i64 ┆ i64 ┆ i64 │
╞═════╪═════╪═════╪═════╡
│ 1   ┆ 1   ┆ 2   ┆ 3   │
└─────┴─────┴─────┴─────┘

```