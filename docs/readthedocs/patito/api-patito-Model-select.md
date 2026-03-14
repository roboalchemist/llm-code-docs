# patito.Model.select

*classmethod *Model.select(*fields*)

Create a new model consisting of only a subset of the model fields.

Parameters:

**fields** (`Union`[`str`, `Iterable`[`str`]]) – A single field name as a string or a collection of strings.

Return type:

`Type`[`Model`]

Returns:

A new model containing only the fields specified by `fields`.

Raises:

**ValueError** – If one or more non-existent fields are selected.

Example

```
>>> class MyModel(Model):
...     a: int
...     b: int
...     c: int
...

```