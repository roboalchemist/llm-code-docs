# patito.duckdb.Database

Database.__init__(*path=None*, *read_only=False*, ***kwargs*)

Instantiate a new DuckDB database, either persisted to disk or in-memory.

Parameters:

- 

**path** (`Optional`[`Path`]) – Optional path to store all the data to. If `None` the data is
persisted in-memory only.

- 

**read_only** (`bool`) – If the database connection should be a read-only connection.

- 

****kwargs** (`Any`) – Additional keywords forwarded to `duckdb.connect()`.

Examples

```
>>> import patito as pt
>>> db = pt.duckdb.Database()
>>> db.to_relation("select 1 as a, 2 as b").create_table("my_table")
>>> db.query("select * from my_table").to_df()
shape: (1, 2)
┌─────┬─────┐
│ a   ┆ b   │
│ --- ┆ --- │
│ i64 ┆ i64 │
╞═════╪═════╡
│ 1   ┆ 2   │
└─────┴─────┘

```