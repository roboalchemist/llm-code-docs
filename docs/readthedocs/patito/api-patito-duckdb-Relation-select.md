# patito.duckdb.Relation.select

Relation.select(**projections*, ***named_projections*)

Return relation based on one or more SQL `SELECT` projections.

Keyword arguments are converted into `{arg} as {keyword}` in the executed SQL
query.

Parameters:

- 

***projections** (`Union`[`str`, `int`, `float`]) – One or more strings representing SQL statements to be
selected. For example `"2"` or `"another_column"`.

- 

****named_projections** (`Union`[`str`, `int`, `float`]) – One ore more keyword arguments where the keyword
specifies the name of the new column and the value is an SQL statement
defining the content of the new column. For example
`new_column="2 * another_column"`.

Return type:

`Relation`

Examples

```
>>> import patito as pt
>>> db = pt.duckdb.Database()
>>> relation = db.to_relation(pt.DataFrame({"original_column": [1, 2, 3]}))
>>> relation.select("*").to_df()
shape: (3, 1)
┌─────────────────┐
│ original_column │
│ ---             │
│ i64             │
╞═════════════════╡
│ 1               │
│ 2               │
│ 3               │
└─────────────────┘
>>> relation.select("*", multiplied_column="2 * original_column").to_df()
shape: (3, 2)
┌─────────────────┬───────────────────┐
│ original_column ┆ multiplied_column │
│ ---             ┆ ---               │
│ i64             ┆ i64               │
╞═════════════════╪═══════════════════╡
│ 1               ┆ 2                 │
│ 2               ┆ 4                 │
│ 3               ┆ 6                 │
└─────────────────┴───────────────────┘

```