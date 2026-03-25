# patito.duckdb.Relation.with_missing_nullable_columns

Relation.with_missing_nullable_columns(*include=None*, *exclude=None*)

Add missing nullable columns filled with correctly typed nulls.

Make sure to invoke Relation.set_model() with
the correct model schema before executing
`Relation.with_missing_nullable_columns()`.

Parameters:

- 

**include** (`Optional`[`Iterable`[`str`]]) – If provided, only fill in null values for missing columns part of
this collection of column names.

- 

**exclude** (`Optional`[`Iterable`[`str`]]) – If provided, do not fill in null values for missing columns
part of this collection of column names.

Returns:

New relation where missing nullable columns have been filled in
with null values.

Return type:

Relation

Example

```
>>> from typing import Optional
>>> import patito as pt
>>> class MyModel(pt.Model):
...     non_nullable_column: int
...     nullable_column: Optional[int]
...     another_nullable_column: Optional[int]
...
>>> relation = pt.duckdb.Relation("select 1 as nullable_column")
>>> relation.to_df()
shape: (1, 1)
┌─────────────────┐
│ nullable_column │
│ ---             │
│ i64             │
╞═════════════════╡
│ 1               │
└─────────────────┘
>>> relation.set_model(MyModel).with_missing_nullable_columns().to_df()
shape: (1, 2)
┌─────────────────┬─────────────────────────┐
│ nullable_column ┆ another_nullable_column │
│ ---             ┆ ---                     │
│ i64             ┆ i64                     │
╞═════════════════╪═════════════════════════╡
│ 1               ┆ null                    │
└─────────────────┴─────────────────────────┘

```