# patito.duckdb.Relation.to_df

Relation.to_df()

Return a polars DataFrame representation of relation object.

Returns: A `patito.DataFrame` object which inherits from `polars.DataFrame`.

Return type:

`DataFrame`

Example

```
>>> import patito as pt
>>> pt.duckdb.Relation("select 1 as column union select 2 as column").order(
...     by="1"
... ).to_df()
shape: (2, 1)
┌────────┐
│ column │
│ ---    │
│ i64    │
╞════════╡
│ 1      │
│ 2      │
└────────┘

```