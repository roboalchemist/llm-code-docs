# patito.duckdb.Database.execute

Database.execute(*query*, **parameters*)

Execute SQL query in DuckDB database.

Parameters:

- 

**query** (`str`) – A SQL statement to execute. Does not have to be terminated with
a semicolon (`;`).

- 

**parameters** (`Collection`[`Union`[`str`, `int`, `float`, `bool`]]) – One or more sets of parameters to insert into prepared
statements. The values are replaced in place of the question marks
(`?`) in the prepared query.

Return type:

`None`

Example

```
>>> import patito as pt
>>> db = pt.duckdb.Database()
>>> db.execute("create table my_table (x bigint);")
>>> db.execute("insert into my_table values (1), (2), (3)")
>>> db.table("my_table").to_df()
shape: (3, 1)
┌─────┐
│ x   │
│ --- │
│ i64 │
╞═════╡
│ 1   │
│ 2   │
│ 3   │
└─────┘

```