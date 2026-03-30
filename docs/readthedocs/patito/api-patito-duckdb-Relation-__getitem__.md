# patito.duckdb.Relation.__getitem__

Relation.__getitem__(*key*)

Return Relation with selected columns.

Uses Relation.select() under-the-hood in order to
perform the selection. Can technically be used to rename columns,
define derived columns, and so on, but prefer the use of Relation.select() for
such use cases.

Parameters:

**key** (`Union`[`str`, `Iterable`[`str`]]) – Columns to select, either a single column represented as a string, or
an iterable of strings.

Return type:

`Relation`

Returns:

New relation only containing the column subset specified.

Example

```
>>> import patito as pt
>>> relation = pt.duckdb.Relation("select 1 as a, 2 as b, 3 as c")
>>> relation.to_df()
shape: (1, 3)
┌─────┬─────┬─────┐
│ a   ┆ b   ┆ c   │
│ --- ┆ --- ┆ --- │
│ i64 ┆ i64 ┆ i64 │
╞═════╪═════╪═════╡
│ 1   ┆ 2   ┆ 3   │
└─────┴─────┴─────┘
>>> relation[["a", "b"]].to_df()
shape: (1, 2)
┌─────┬─────┐
│ a   ┆ b   │
│ --- ┆ --- │
│ i64 ┆ i64 │
╞═════╪═════╡
│ 1   ┆ 2   │
└─────┴─────┘
>>> relation["a"].to_df()
shape: (1, 1)
┌─────┐
│ a   │
│ --- │
│ i64 │
╞═════╡
│ 1   │
└─────┘

```