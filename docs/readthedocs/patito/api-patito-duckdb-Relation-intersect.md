# patito.duckdb.Relation.intersect

Relation.intersect(*other*)

Return a new relation containing the rows that are present in both relations.

This is a set operation which will remove duplicate rows as well.

Parameters:

**other** (`Union`[`DataFrame`, `DataFrame`, `DataFrame`, `Path`, `str`, `DuckDBPyRelation`, `Relation`]) – Another relation with the same column names.

Returns:

A new relation with only those rows that are present in
both relations.

Return type:

Relation[Model]

Example

```
>>> import patito as pt
>>> df1 = pt.DataFrame({"a": [1, 1, 2], "b": [1, 1, 2]})
>>> df2 = pt.DataFrame({"a": [1, 1, 3], "b": [1, 1, 3]})
>>> pt.duckdb.Relation(df1).intersect(pt.duckdb.Relation(df2)).to_df()
shape: (1, 2)
┌─────┬─────┐
│ a   ┆ b   │
│ --- ┆ --- │
│ i64 ┆ i64 │
╞═════╪═════╡
│ 1   ┆ 1   │
└─────┴─────┘

```