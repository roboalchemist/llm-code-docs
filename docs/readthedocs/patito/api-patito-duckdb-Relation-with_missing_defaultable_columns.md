# patito.duckdb.Relation.with_missing_defaultable_columns

Relation.with_missing_defaultable_columns(*include=None*, *exclude=None*)

Add missing defaultable columns filled with the default values of correct type.

Make sure to invoke Relation.set_model() with
the correct model schema before executing
`Relation.with_missing_default_columns()`.

Parameters:

- 

**include** (`Optional`[`Iterable`[`str`]]) – If provided, only fill in default values for missing columns part
of this collection of column names.

- 

**exclude** (`Optional`[`Iterable`[`str`]]) – If provided, do not fill in default values for missing columns
part of this collection of column names.

Returns:

New relation where missing columns with default values according
to the schema have been filled in.

Return type:

Relation

Example

```
>>> import patito as pt
>>> class MyModel(pt.Model):
...     non_default_column: int
...     another_non_default_column: int
...     default_column: int = 42
...     another_default_column: int = 42
...
>>> relation = pt.duckdb.Relation(
...     "select 1 as non_default_column, 2 as default_column"
... )
>>> relation.to_df()
shape: (1, 2)
┌────────────────────┬────────────────┐
│ non_default_column ┆ default_column │
│ ---                ┆ ---            │
│ i64                ┆ i64            │
╞════════════════════╪════════════════╡
│ 1                  ┆ 2              │
└────────────────────┴────────────────┘
>>> relation.set_model(MyModel).with_missing_defaultable_columns().to_df()
shape: (1, 3)
┌────────────────────┬────────────────┬────────────────────────┐
│ non_default_column ┆ default_column ┆ another_default_column │
│ ---                ┆ ---            ┆ ---                    │
│ i64                ┆ i64            ┆ i64                    │
╞════════════════════╪════════════════╪════════════════════════╡
│ 1                  ┆ 2              ┆ 42                     │
└────────────────────┴────────────────┴────────────────────────┘

```