# patito.DataFrame.drop

DataFrame.drop(*columns=None*, **more_columns*)

Drop one or more columns from the dataframe.

If `name` is not provided then all columns not specified by the associated
patito model, for instance set with
DataFrame.set_model, are dropped.

Parameters:

- 

**columns** (`Union`[`str`, `Collection`[`str`], `None`]) – A single column string name, or list of strings, indicating
which columns to drop. If not specified, all columns *not*
specified by the associated dataframe model will be dropped.

- 

**more_columns** (`str`) – Additional named columns to drop.

Returns:

New dataframe without the specified columns.

Return type:

DataFrame[Model]

Examples

```
>>> import patito as pt
>>> class Model(pt.Model):
...     column_1: int
...
>>> Model.DataFrame({"column_1": [1, 2], "column_2": [3, 4]}).drop()
shape: (2, 1)
┌──────────┐
│ column_1 │
│ ---      │
│ i64      │
╞══════════╡
│ 1        │
│ 2        │
└──────────┘

```