# patito.Model.prefix

*classmethod *Model.prefix(*prefix*)

Return a new model where all field names have been prefixed.

Parameters:

**prefix** (`str`) – String prefix to add to all field names.

Return type:

`Type`[`Model`]

Returns:

New model class with all the same fields only prefixed with the given prefix.

Example

```
>>> class MyModel(Model):
...     a: int
...     b: int
...

```