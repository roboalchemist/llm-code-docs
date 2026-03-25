# patito.Model.validate

*classmethod *Model.validate(*dataframe*)

Validate the schema and content of the given dataframe.

Parameters:

**dataframe** (`Union`[`DataFrame`, `DataFrame`]) – Polars DataFrame to be validated.

Raises:

**patito.exceptions.ValidationError** – If the given dataframe does not match
    the given schema.

Examples

Return type:

`None`

```
>>> import patito as pt
>>> import polars as pl

```