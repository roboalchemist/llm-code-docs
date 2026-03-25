# patito.Model.columns

*property *Model.columns*: List[str]*

Return the name of the dataframe columns specified by the fields of the model.

Returns:

List of column names.

Example

```
>>> import patito as pt
>>> class Product(pt.Model):
...     name: str
...     price: int
...
>>> Product.columns
['name', 'price']

```