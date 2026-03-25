# patito.duckdb.Relation.union

Relation.union(*other*)

Produce a new relation that contains the rows of both relations.

The `+` operator can also be used to union two relations.

The two relations must have the same column names, but not necessarily in the
same order as reordering of columns is automatically performed, unlike regular
SQL.

Duplicates are not dropped.

Parameters:

**other** (`Union`[`DataFrame`, `DataFrame`, `DataFrame`, `Path`, `str`, `DuckDBPyRelation`, `Relation`]) – A `patito.duckdb.Relation` object or something that can be
*casted* to `patito.duckdb.Relation`.
See Relation.

Return type:

`TypeVar`(`RelationType`, bound= Relation)

Returns:

New relation containing the rows of both `self` and `other`.

Raises:

**TypeError** – If the two relations do not contain the same columns.

Examples

```
>>> import patito as pt
>>> relation_1 = pt.duckdb.Relation("select 1 as a")
>>> relation_2 = pt.duckdb.Relation("select 2 as a")
>>> relation_1.union(relation_2).to_df()
shape: (2, 1)
┌─────┐
│ a   │
│ --- │
│ i64 │
╞═════╡
│ 1   │
│ 2   │
└─────┘

```