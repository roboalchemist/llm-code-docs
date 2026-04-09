# patito.duckdb.Relation.order

Relation.order(*by*)

Change the order of the rows of the relation.

Parameters:

**by** (`Union`[`str`, `Iterable`[`str`]]) – An `ORDER BY` SQL expression such as `"age DESC"` or
`("age DESC", "name ASC")`.

Return type:

`TypeVar`(`RelationType`, bound= Relation)

Returns:

New relation where the rows have been ordered according to `by`.

Example

```
>>> import patito as pt
>>> df = pt.DataFrame(
...     {
...         "name": ["Alice", "Bob", "Charles", "Diana"],
...         "age": [20, 20, 30, 35],
...     }
... )
>>> df
shape: (4, 2)
┌─────────┬─────┐
│ name    ┆ age │
│ ---     ┆ --- │
│ str     ┆ i64 │
╞═════════╪═════╡
│ Alice   ┆ 20  │
│ Bob     ┆ 20  │
│ Charles ┆ 30  │
│ Diana   ┆ 35  │
└─────────┴─────┘
>>> relation = pt.duckdb.Relation(df)
>>> relation.order(by="age desc").to_df()
shape: (4, 2)
┌─────────┬─────┐
│ name    ┆ age │
│ ---     ┆ --- │
│ str     ┆ i64 │
╞═════════╪═════╡
│ Diana   ┆ 35  │
│ Charles ┆ 30  │
│ Alice   ┆ 20  │
│ Bob     ┆ 20  │
└─────────┴─────┘
>>> relation.order(by=["age desc", "name desc"]).to_df()
shape: (4, 2)
┌─────────┬─────┐
│ name    ┆ age │
│ ---     ┆ --- │
│ str     ┆ i64 │
╞═════════╪═════╡
│ Diana   ┆ 35  │
│ Charles ┆ 30  │
│ Bob     ┆ 20  │
│ Alice   ┆ 20  │
└─────────┴─────┘

```