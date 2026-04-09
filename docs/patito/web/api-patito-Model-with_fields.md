# patito.Model.with_fields

*classmethod *Model.with_fields(***field_definitions*)

Return a new model class where the given fields have been added.

Parameters:

****field_definitions** (`Any`) – the keywords are of the form:
`field_name=(field_type, field_default)`.
Specify `...` if no default value is provided.
For instance, `column_name=(int, ...)` will create a new non-optional
integer field named `"column_name"`.

Return type:

`Type`[`Model`]

Returns:

A new model with all the original fields and the additional field
definitions.

Example

```
>>> class MyModel(Model):
...     a: int
...
>>> class ExpandedModel(MyModel):
...     b: int
...
>>> MyModel.with_fields(b=(int, ...)).columns == ExpandedModel.columns
True

```