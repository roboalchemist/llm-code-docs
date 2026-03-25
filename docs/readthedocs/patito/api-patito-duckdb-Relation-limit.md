# patito.duckdb.Relation.limit

Relation.limit(*n*, ***, *offset=0*)

Remove all but the first n rows.

Parameters:

- 

**n** (`int`) – The number of rows to keep.

- 

**offset** (`int`) – Disregard the first `offset` rows before starting to count which
rows to keep.

Return type:

`TypeVar`(`RelationType`, bound= Relation)

Returns:

New relation with only n rows.

Example

```
>>> import patito as pt
>>> relation = (
...     pt.duckdb.Relation("select 1 as column")
...     + pt.duckdb.Relation("select 2 as column")
...     + pt.duckdb.Relation("select 3 as column")
...     + pt.duckdb.Relation("select 4 as column")
... )
>>> relation.limit(2).to_df()
shape: (2, 1)
┌────────┐
│ column │
│ ---    │
│ i64    │
╞════════╡
│ 1      │
│ 2      │
└────────┘
>>> relation.limit(2, offset=2).to_df()
shape: (2, 1)
┌────────┐
│ column │
│ ---    │
│ i64    │
╞════════╡
│ 3      │
│ 4      │
└────────┘

```