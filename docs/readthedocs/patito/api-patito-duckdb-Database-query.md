# patito.duckdb.Database.query

Database.query(*query*, *alias='query_relation'*)

Execute arbitrary SQL select query and return the relation.

Parameters:

- 

**query** (`str`) – Arbitrary SQL select query.

- 

**alias** (`str`) – The alias to assign to the resulting relation, to be used in further
queries.

Return type:

`Relation`

Returns: A relation representing the data produced by the given query.

Example

```
>>> import patito as pt
>>> db = pt.duckdb.Database()
>>> relation = db.query("select 1 as a, 2 as b, 3 as c")
>>> relation.to_df()
shape: (1, 3)
┌─────┬─────┬─────┐
│ a   ┆ b   ┆ c   │
│ --- ┆ --- ┆ --- │
│ i64 ┆ i64 ┆ i64 │
╞═════╪═════╪═════╡
│ 1   ┆ 2   ┆ 3   │
└─────┴─────┴─────┘

```