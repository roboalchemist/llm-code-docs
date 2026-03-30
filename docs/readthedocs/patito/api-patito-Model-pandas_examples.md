# patito.Model.pandas_examples

*classmethod *Model.pandas_examples(*data*, *columns=None*)

Generate dataframe with dummy data for all unspecified columns.

Offers the same API as the pandas.DataFrame constructor.
Non-iterable values, besides strings, are repeated until they become as long as
the iterable arguments.

Parameters:

- 

**data** (`Union`[`dict`, `Iterable`]) – Data to populate the dummy dataframe with. If
not a dict, column names must also be provided.

- 

**columns** (`Optional`[`Iterable`[`str`]]) – Ignored if data is a dict. If
data is an iterable, it will be used as the column names in the
resulting dataframe. Defaults to None.

Return type:

`DataFrame`

Returns:

A pandas DataFrame filled with dummy example data.

Raises:

- 

**ImportError** – If pandas has not been installed. You should install
    patito[pandas] in order to integrate patito with pandas.

- 

**TypeError** – If column names have not been specified in the input data.

Example

```
>>> from typing import Literal
>>> import patito as pt

```