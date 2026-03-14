# patito.duckdb.Relation.execute

Relation.execute()

Execute built relation query and return result object.

Return type:

`DuckDBPyRelation`

Returns:

A native `duckdb.DuckDBPyResult` object representing the executed query.

Examples

```
>>> import patito as pt
>>> relation = pt.duckdb.Relation(
...     "select 1 as a, 2 as b union select 3 as a, 4 as b"
... )
>>> result = relation.aggregate("sum(a)", group_by="").execute()
>>> result.description
[('sum(a)', 'NUMBER', None, None, None, None, None)]
>>> result.fetchall()
[(4,)]

```