# patito.DataFrame.fill_null

DataFrame.fill_null(*value=None*, *strategy=None*, *limit=None*, *matches_supertype=True*)

Fill null values using a filling strategy, literal, or `Expr`.

If `"default"` is provided as the strategy, the model fields with default
values are used to fill missing values.

Parameters:

- 

**value** (`Optional`[`Any`]) – Value used to fill null values.

- 

**strategy** (`Optional`[`Literal`[`'forward'`, `'backward'`, `'min'`, `'max'`, `'mean'`, `'zero'`, `'one'`, `'defaults'`]]) – Accepts the same arguments as `polars.DataFrame.fill_null` in
addition to `"defaults"` which will use the field’s default value if
provided.

- 

**limit** (`Optional`[`int`]) – The number of consecutive null values to forward/backward fill.
Only valid if `strategy` is `"forward"` or `"backward"`.

- 

**matches_supertype** (`bool`) – Fill all matching supertype of the fill `value`.

Returns:

A new dataframe with nulls filled in according to the
provided `strategy` parameter.

Return type:

DataFrame[Model]

Example

```
>>> import patito as pt
>>> class Product(pt.Model):
...     name: str
...     price: int = 19
...
>>> df = Product.DataFrame(
...     {"name": ["apple", "banana"], "price": [10, None]}
... )
>>> df.fill_null(strategy="defaults")
shape: (2, 2)
┌────────┬───────┐
│ name   ┆ price │
│ ---    ┆ ---   │
│ str    ┆ i64   │
╞════════╪═══════╡
│ apple  ┆ 10    │
│ banana ┆ 19    │
└────────┴───────┘

```