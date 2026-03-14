# patito.duckdb.Database.default

*classmethod *Database.default()

Return the default DuckDB database.

Return type:

`Database`

Returns:

A patito Database object wrapping around the given
connection.

Example

```
>>> import patito as pt
>>> db = pt.duckdb.Database.default()
>>> db.query("select 1 as a, 2 as b").to_df()
shape: (1, 2)
┌─────┬─────┐
│ a   ┆ b   │
│ --- ┆ --- │
│ i64 ┆ i64 │
╞═════╪═════╡
│ 1   ┆ 2   │
└─────┴─────┘

```