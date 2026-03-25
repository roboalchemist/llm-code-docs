# patito.Model.non_nullable_columns

*property *Model.non_nullable_columns*: set[str]*

Return names of those columns that are non-nullable in the schema.

Returns:

Set of column name strings.

Example

```
>>> from typing import Optional
>>> import patito as pt
>>> class MyModel(pt.Model):
...     nullable_field: Optional[int]
...     inferred_nullable_field: int = None
...     non_nullable_field: int
...     another_non_nullable_field: str
...
>>> sorted(MyModel.non_nullable_columns)
['another_non_nullable_field', 'non_nullable_field']

```