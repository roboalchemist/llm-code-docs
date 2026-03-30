# patito.Model.examples

*classmethod *Model.examples(*data=None*, *columns=None*)

Generate polars dataframe with dummy data for all unspecified columns.

This constructor accepts the same data format as polars.DataFrame.

Parameters:

- 

**data** (`Union`[`dict`, `Iterable`, `None`]) – Data to populate the dummy dataframe with. If given as an iterable of
values, then column names must also be provided. If not provided at all,
a dataframe with a single row populated with dummy data is provided.

- 

**columns** (`Optional`[`Iterable`[`str`]]) – Ignored if `data` is provided as a dictionary. If data is
provided as an `iterable`, then `columns` will be used as the
column names in the resulting dataframe. Defaults to None.

Return type:

`DataFrame`

Returns:

A polars dataframe where all unspecified columns have been filled with dummy
data which should pass model validation.

Raises:

**TypeError** – If one or more of the model fields are not mappable to polars
    column dtype equivalents.

Example

```
>>> from typing import Literal
>>> import patito as pt

```