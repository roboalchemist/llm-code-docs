# patito.DataFrame.set_model

DataFrame.set_model(*model*)

Associate a given patito `Model` with the dataframe.

The model schema is used by methods that depend on a model being associated with
the given dataframe such as DataFrame.validate()
and DataFrame.get().

`DataFrame(...).set_model(Model)` is equivalent with `Model.DataFrame(...)`.

Parameters:

**model** (*Model*) – Sub-class of `patito.Model` declaring the schema of the
dataframe.

Returns:

Returns the same dataframe, but with an attached model
that is required for certain model-specific dataframe methods to work.

Return type:

DataFrame[Model]

Examples

```
>>> from typing_extensions import Literal
>>> import patito as pt
>>> import polars as pl
>>> class SchoolClass(pt.Model):
...     year: int = pt.Field(dtype=pl.UInt16)
...     letter: Literal["A", "B"] = pt.Field(dtype=pl.Categorical)
...
>>> classes = pt.DataFrame(
...     {"year": [1, 1, 2, 2], "letter": list("ABAB")}
... ).set_model(SchoolClass)
>>> classes
shape: (4, 2)
┌──────┬────────┐
│ year ┆ letter │
│ ---  ┆ ---    │
│ i64  ┆ str    │
╞══════╪════════╡
│ 1    ┆ A      │
│ 1    ┆ B      │
│ 2    ┆ A      │
│ 2    ┆ B      │
└──────┴────────┘
>>> casted_classes = classes.cast()
>>> casted_classes
shape: (4, 2)
┌──────┬────────┐
│ year ┆ letter │
│ ---  ┆ ---    │
│ u16  ┆ cat    │
╞══════╪════════╡
│ 1    ┆ A      │
│ 1    ┆ B      │
│ 2    ┆ A      │
│ 2    ┆ B      │
└──────┴────────┘
>>> casted_classes.validate()

```