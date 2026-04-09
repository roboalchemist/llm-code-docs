# patito.duckdb.Database.empty_relation

Database.empty_relation(*schema*)

Create relation with zero rows, but correct schema that matches the given model.

Parameters:

**schema** (`Type`[`TypeVar`(`ModelType`, bound= Model)]) – A patito model which specifies the column names and types of the
given relation.

Return type:

`Relation`[`TypeVar`(`ModelType`, bound= Model)]

Example

```
>>> import patito as pt
>>> class Schema(pt.Model):
...     string_column: str
...     bool_column: bool
...
>>> db = pt.duckdb.Database()
>>> empty_relation = db.empty_relation(Schema)
>>> empty_relation.to_df()
shape: (0, 2)
┌───────────────┬─────────────┐
│ string_column ┆ bool_column │
│ ---           ┆ ---         │
│ str           ┆ bool        │
╞═══════════════╪═════════════╡
└───────────────┴─────────────┘
>>> non_empty_relation = db.query(
...     "select 'dummy' as string_column, true as bool_column"
... )
>>> non_empty_relation.union(empty_relation).to_df()
shape: (1, 2)
┌───────────────┬─────────────┐
│ string_column ┆ bool_column │
│ ---           ┆ ---         │
│ str           ┆ bool        │
╞═══════════════╪═════════════╡
│ dummy         ┆ true        │
└───────────────┴─────────────┘

```