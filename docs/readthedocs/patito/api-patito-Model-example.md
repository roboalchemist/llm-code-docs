# patito.Model.example

*classmethod *Model.example(***kwargs*)

Produce model instance with filled dummy data for all unspecified fields.

The type annotation of unspecified field is used to fill in type-correct
dummy data, e.g. `-1` for `int`, `"dummy_string"` for `str`, and so
on…

The first item of `typing.Literal` annotations are used for dummy values.

Parameters:

****kwargs** (`Any`) – Provide explicit values for any fields which should not be
filled with dummy data.

Returns:

A pydantic model object filled with dummy data for all unspecified
model fields.

Return type:

Model

Raises:

**TypeError** – If one or more of the provided keyword arguments do not match any
    fields on the model.

Example

```
>>> from typing import Literal
>>> import patito as pt

```