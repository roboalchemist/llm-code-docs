# patito.duckdb.Relation.columns

*property *Relation.columns*: List[str]*

Return the columns of the relation as a list of strings.

Examples

```
>>> import patito as pt
>>> pt.duckdb.Relation("select 1 as a, 2 as b").columns
['a', 'b']

```