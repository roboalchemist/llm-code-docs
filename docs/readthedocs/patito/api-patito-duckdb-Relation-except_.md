# patito.duckdb.Relation.except_

Relation.except_(*other*)

Remove all rows that can be found in the other other relation.

Parameters:

**other** (`Union`[`DataFrame`, `DataFrame`, `DataFrame`, `Path`, `str`, `DuckDBPyRelation`, `Relation`]) – Another relation or something that can be casted to a relation.

Return type:

`TypeVar`(`RelationType`, bound= Relation)

Returns:

New relation without the rows that can be found in the other relation.

Example

```
>>> import patito as pt
>>> relation_123 = pt.duckdb.Relation(
...     "select 1 union select 2 union select 3"
... )
>>> relation_123.order(by="1").to_df()
shape: (3, 1)
┌─────┐
│ 1   │
│ --- │
│ i64 │
╞═════╡
│ 1   │
│ 2   │
│ 3   │
└─────┘
>>> relation_2 = pt.duckdb.Relation("select 2")
>>> relation_2.to_df()
shape: (1, 1)
┌─────┐
│ 2   │
│ --- │
│ i64 │
╞═════╡
│ 2   │
└─────┘
>>> relation_123.except_(relation_2).order(by="1").to_df()
shape: (2, 1)
┌─────┐
│ 1   │
│ --- │
│ i64 │
╞═════╡
│ 1   │
│ 3   │
└─────┘

```