# patito.duckdb.Relation.insert_into

Relation.insert_into(*table*)

Insert all rows of the relation into a given table.

The relation must contain all the columns present in the target table.
Extra columns are ignored and the column order is automatically matched
with the target table.

Parameters:

**table** (`str`) – Name of table for which to insert values into.

Returns:

The original relation, i.e. `self`.

Return type:

Relation

Examples

```
>>> import patito as pt
>>> db = pt.duckdb.Database()
>>> db.to_relation("select 1 as a").create_table("my_table")
>>> db.table("my_table").to_df()
shape: (1, 1)
┌─────┐
│ a   │
│ --- │
│ i64 │
╞═════╡
│ 1   │
└─────┘
>>> db.to_relation("select 2 as a").insert_into("my_table")
>>> db.table("my_table").to_df()
shape: (2, 1)
┌─────┐
│ a   │
│ --- │
│ i64 │
╞═════╡
│ 1   │
│ 2   │
└─────┘

```