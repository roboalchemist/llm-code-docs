# patito.Model.drop

*classmethod *Model.drop(*name*)

Return a new model where one or more fields are excluded.

Parameters:

**name** (`Union`[`str`, `Iterable`[`str`]]) – A single string field name, or a list of such field names,
which will be dropped.

Return type:

`Type`[`Model`]

Returns:

New model class where the given fields have been removed.

Examples

```
>>> class MyModel(Model):
...     a: int
...     b: int
...     c: int
...

```