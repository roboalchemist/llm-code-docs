# patito.Model.suffix

*classmethod *Model.suffix(*suffix*)

Return a new model where all field names have been suffixed.

Parameters:

**suffix** (`str`) – String suffix to add to all field names.

Return type:

`Type`[`Model`]

Returns:

New model class with all the same fields only suffixed with the given
suffix.

Example

```
>>> class MyModel(Model):
...     a: int
...     b: int
...

```