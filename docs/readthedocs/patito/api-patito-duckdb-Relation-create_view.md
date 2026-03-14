# patito.duckdb.Relation.create_view

Relation.create_view(*name*, *replace=False*)

Create new database view based on relation.

Returns:

A relation pointing to the newly created view.

Return type:

Relation

Examples

```
>>> import patito as pt
>>> db = pt.duckdb.Database()
>>> df = pt.DataFrame({"column": ["A", "A", "B"]})
>>> relation = db.to_relation(df)
>>> relation.create_view("my_view")
>>> db.query("select * from my_view").to_df()
shape: (3, 1)
┌────────┐
│ column │
│ ---    │
│ str    │
╞════════╡
│ A      │
│ A      │
│ B      │
└────────┘

```