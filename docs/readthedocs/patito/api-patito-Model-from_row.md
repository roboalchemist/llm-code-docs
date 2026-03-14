# patito.Model.from_row

*classmethod *Model.from_row(*row*, *validate=True*)

Represent a single data frame row as a Patito model.

Parameters:

- 

**row** (`Union`[`DataFrame`, `DataFrame`]) – A dataframe, either polars and pandas, consisting of a single row.

- 

**validate** (`bool`) – If `False`, skip pydantic validation of the given row data.

Returns:

A patito model representing the given row data.

Return type:

Model

Raises:

**TypeError** – If the given type is neither a pandas or polars DataFrame.

Example

```
>>> import patito as pt
>>> import polars as pl

```