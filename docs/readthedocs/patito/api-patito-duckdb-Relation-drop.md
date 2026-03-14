# patito.duckdb.Relation.drop

Relation.drop(**columns*)

Remove specified column(s) from relation.

Parameters:

**columns** (*str*) – Any number of string column names to be dropped.

Return type:

`Relation`

Examples

```
>>> import patito as pt
>>> relation = pt.duckdb.Relation("select 1 as a, 2 as b, 3 as c")
>>> relation.columns
['a', 'b', 'c']
>>> relation.drop("c").columns
['a', 'b']
>>> relation.drop("b", "c").columns
['a']

```