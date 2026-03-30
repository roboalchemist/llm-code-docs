# patito.duckdb.Relation.count

Relation.count()

Return the number of rows in the given relation.

Return type:

`int`

Returns:

Number of rows in the relation as an integer.

Examples

```
>>> import patito as pt
>>> relation = pt.duckdb.Relation("select 1 as a")
>>> relation.count()
1
>>> (relation + relation).count()
2

```