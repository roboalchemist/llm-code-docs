# patito.Field

*class *patito.Field(*default=PydanticUndefined*, ***, *default_factory=None*, *alias=None*, *title=None*, *description=None*, *exclude=None*, *include=None*, *const=None*, *gt=None*, *ge=None*, *lt=None*, *le=None*, *multiple_of=None*, *allow_inf_nan=None*, *max_digits=None*, *decimal_places=None*, *min_items=None*, *max_items=None*, *unique_items=None*, *min_length=None*, *max_length=None*, *allow_mutation=True*, *regex=None*, *discriminator=None*, *repr=True*, ***extra*)

Annotate model field with additional type and validation information.

This class is built on `pydantic.Field` and you can find its full documentation
here [https://pydantic-docs.helpmanual.io/usage/schema/#field-customization].
Patito adds additional parameters which are used when validating dataframes,
these are documented here.

Parameters:

- 

**constraints** (*Union**[**polars.Expression**, **List**[**polars.Expression**]*) – A single
constraint or list of constraints, expressed as a polars expression objects.
All rows must satisfy the given constraint. You can refer to the given column
with `pt.field`, which will automatically be replaced with
`polars.col(<field_name>)` before evaluation.

- 

**unique** (*bool*) – All row values must be unique.

- 

**dtype** (*polars.datatype.DataType*) – The given dataframe column must have the given
polars dtype, for instance `polars.UInt64` or `pl.Float32`.

- 

**gt** (`Optional`[`float`]) – All values must be greater than `gt`.

- 

**ge** (`Optional`[`float`]) – All values must be greater than or equal to `ge`.

- 

**lt** (`Optional`[`float`]) – All values must be less than `lt`.

- 

**le** (`Optional`[`float`]) – All values must be less than or equal to `lt`.

- 

**multiple_of** (`Optional`[`float`]) – All values must be multiples of the given value.

- 

**const** (*bool*) – If set to `True` all values must be equal to the provided
default value, the first argument provided to the `Field` constructor.

- 

**regex** (*str*) – UTF-8 string column must match regex pattern for all row values.

- 

**min_length** (*int*) – Minimum length of all string values in a UTF-8 column.

- 

**max_length** (*int*) – Maximum length of all string values in a UTF-8 column.

Returns:

Object used to represent additional constraints put upon the given
field.

Return type:

FieldInfo

Examples

```
>>> import patito as pt
>>> import polars as pl
>>> class Product(pt.Model):
...     # Do not allow duplicates
...     product_id: int = pt.Field(unique=True)
...
...     # Price must be stored as unsigned 16-bit integers
...     price: int = pt.Field(dtype=pl.UInt16)
...
...     # The product name should be from 3 to 128 characters long
...     name: str = pt.Field(min_length=3, max_length=128)
...
...     # Represent colors in the form of upper cased hex colors
...     brand_color: str = pt.Field(regex=r"^\#[0-9A-F]{6}$")
...
>>> Product.DataFrame(
...     {
...         "product_id": [1, 1],
...         "price": [400, 600],
...         "brand_color": ["#ab00ff", "AB00FF"],
...     }
... ).validate()
Traceback (most recent call last):
  ...
patito.exceptions.ValidationError: 4 validation errors for Product
name
  Missing column (type=type_error.missingcolumns)
product_id
  2 rows with duplicated values. (type=value_error.rowvalue)
price
  Polars dtype Int64 does not match model field type.           (type=type_error.columndtype)
brand_color
  2 rows with out of bound values. (type=value_error.rowvalue)

```