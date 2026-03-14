# patito.duckdb.Relation.types

Relation.types

Return the SQL types of all the columns of the given relation.

Returns:

A dictionary where the keys are the column names and the
values are SQL types as strings.

Return type:

dict[str, str]

Examples

```
>>> import patito as pt
>>> pt.duckdb.Relation("select 1 as a, 'my_value' as b").types
{'a': INTEGER, 'b': VARCHAR}

```