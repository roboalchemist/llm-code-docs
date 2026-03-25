# patito.Model.rename

*classmethod *Model.rename(*mapping*)

Return a new model class where the specified fields have been renamed.

Parameters:

**mapping** (`Dict`[`str`, `str`]) – A dictionary where the keys are the old field names
and the values are the new names.

Return type:

`Type`[`Model`]

Returns:

A new model class where the given fields have been renamed.

Raises:

**ValueError** – If non-existent fields are renamed.

Example

```
>>> class MyModel(Model):
...     a: int
...     b: int
...

```