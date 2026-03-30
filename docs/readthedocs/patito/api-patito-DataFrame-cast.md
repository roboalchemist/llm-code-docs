# patito.DataFrame.cast

DataFrame.cast(*strict=False*)

Cast columns to dtypes specified by the associated Patito model.

Parameters:

**strict** (`bool`) – If set to `False`, columns which are technically compliant with
the specified field type, will not be casted. For example, a column
annotated with `int` is technically compliant with `pl.UInt8`, even
if `pl.Int64` is the default dtype associated with `int`-annotated
fields. If `strict` is set to `True`, the resulting dtypes will
be forced to the default dtype associated with each python type.

Returns:

A dataframe with columns casted to the correct dtypes.

Return type:

DataFrame[Model]

Examples

Create a simple model:

```
>>> import patito as pt
>>> import polars as pl
>>> class Product(pt.Model):
...     name: str
...     cent_price: int = pt.Field(dtype=pl.UInt16)
...

```