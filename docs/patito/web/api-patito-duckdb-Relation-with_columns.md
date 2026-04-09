# patito.duckdb.Relation.with_columns

Relation.with_columns(***named_projections*)

Return relations with additional columns.

If the provided columns expressions already exists as a column on the relation,
the given column is overwritten.

Parameters:

**named_projections** (`Union`[`str`, `int`, `float`]) – A set of column expressions, where the keyword is used
as the column name, while the right-hand argument is a valid SQL
expression.

Return type:

`Relation`

Returns:

Relation with the given columns appended, or possibly overwritten.

Examples

```
>>> import patito as pt
>>> db = pt.duckdb.Database()
>>> relation = db.to_relation("select 1 as a, 2 as b")
>>> relation.with_columns(c="a + b").to_df()
shape: (1, 3)
┌─────┬─────┬─────┐
│ a   ┆ b   ┆ c   │
│ --- ┆ --- ┆ --- │
│ i64 ┆ i64 ┆ i64 │
╞═════╪═════╪═════╡
│ 1   ┆ 2   ┆ 3   │
└─────┴─────┴─────┘

```