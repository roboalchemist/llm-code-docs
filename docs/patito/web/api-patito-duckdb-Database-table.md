# patito.duckdb.Database.table

Database.table(*name*)

Return relation representing all the data in the given table.

Parameters:

**name** (`str`) – The name of the table.

Return type:

`Relation`

Example

```
>>> import patito as pt
>>> df = pt.DataFrame({"a": [1, 2], "b": [3, 4]})
>>> db = pt.duckdb.Database()
>>> relation = db.to_relation(df)
>>> relation.create_table(name="my_table")
>>> db.table("my_table").to_df()
shape: (2, 2)
┌─────┬─────┐
│ a   ┆ b   │
│ --- ┆ --- │
│ i64 ┆ i64 │
╞═════╪═════╡
│ 1   ┆ 3   │
│ 2   ┆ 4   │
└─────┴─────┘

```