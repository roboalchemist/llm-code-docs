# patito.Model.dtypes

*property *Model.dtypes*: dict[str, Type[polars.datatypes.classes.DataType]]*

Return the polars dtypes of the dataframe.

Unless Field(dtype=…) is specified, the highest signed column dtype
is chosen for integer and float columns.

Returns:

A dictionary mapping string column names to polars dtype classes.

Example

```
>>> import patito as pt
>>> class Product(pt.Model):
...     name: str
...     ideal_temperature: int
...     price: float
...
>>> Product.dtypes
{'name': Utf8, 'ideal_temperature': Int64, 'price': Float64}

```