# patito.duckdb.Database.to_relation

Database.to_relation(*derived_from*)

Create a new relation object based on data source.

The given data will be represented as a relation associated with the database.
`Database(x).to_relation(y)` is equivalent to
`Relation(y, database=Database(x))`.

Parameters:

**derived_from** (*RelationSource*) – One of either a polars or pandas
`DataFrame`, a `pathlib.Path` to a parquet or CSV file, a SQL query
string, or an existing relation.

Return type:

`Relation`

Example

```
>>> import patito as pt
>>> db = pt.duckdb.Database()
>>> db.to_relation("select 1 as a, 2 as b").to_df()
shape: (1, 2)
┌─────┬─────┐
│ a   ┆ b   │
│ --- ┆ --- │
│ i64 ┆ i64 │
╞═════╪═════╡
│ 1   ┆ 2   │
└─────┴─────┘
>>> db.to_relation(pt.DataFrame({"c": [3, 4], "d": ["5", "6"]})).to_df()
shape: (2, 2)
┌─────┬─────┐
│ c   ┆ d   │
│ --- ┆ --- │
│ i64 ┆ str │
╞═════╪═════╡
│ 3   ┆ 5   │
│ 4   ┆ 6   │
└─────┴─────┘

```