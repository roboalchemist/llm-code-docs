# patito.duckdb.Relation.to_pandas

Relation.to_pandas()

Return a pandas DataFrame representation of relation object.

Returns: A `pandas.DataFrame` object containing all the data of the relation.

Return type:

`DataFrame`

Example

```
>>> import patito as pt
>>> pt.duckdb.Relation("select 1 as column union select 2 as column").order(
...     by="1"
... ).to_pandas()
      column
   0       1
   1       2

```