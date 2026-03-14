# patito.DataFrame.derive

DataFrame.derive()

Populate columns which have `pt.Field(derived_from=...)` definitions.

If a column field on the data frame model has `patito.Field(derived_from=...)`
specified, the given value will be used to define the column. If
`derived_from` is set to a string, the column will be derived from the given
column name. Alternatively, an arbitrary polars expression can be given, the
result of which will be used to populate the column values.

Returns:

A new dataframe where all derivable columns are provided.

Return type:

DataFrame[Model]

Raises:

**TypeError** – If the `derived_from` parameter of `patito.Field` is given
    as something else than a string or polars expression.

Examples

```
>>> import patito as pt
>>> import polars as pl
>>> class Foo(pt.Model):
...     bar: int = pt.Field(derived_from="foo")
...     double_bar: int = pt.Field(derived_from=2 * pl.col("bar"))
...
>>> Foo.DataFrame({"foo": [1, 2]}).derive()
shape: (2, 3)
┌─────┬─────┬────────────┐
│ foo ┆ bar ┆ double_bar │
│ --- ┆ --- ┆ ---        │
│ i64 ┆ i64 ┆ i64        │
╞═════╪═════╪════════════╡
│ 1   ┆ 1   ┆ 2          │
│ 2   ┆ 2   ┆ 4          │
└─────┴─────┴────────────┘

```