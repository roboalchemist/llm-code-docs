# patito.Model.example_value

*classmethod *Model.example_value(*field*)

Return a valid example value for the given model field.

Parameters:

**field** (`str`) – Field name identifier.

Return type:

`Union`[`date`, `datetime`, `float`, `int`, `str`, `None`]

Returns:

A single value which is consistent with the given field definition.

Raises:

**NotImplementedError** – If the given field has no example generator.

Example

```
>>> from typing import Literal
>>> import patito as pt

```