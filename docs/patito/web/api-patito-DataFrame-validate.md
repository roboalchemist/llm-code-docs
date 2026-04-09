# patito.DataFrame.validate

DataFrame.validate()

Validate the schema and content of the dataframe.

You must invoke `.set_model()` before invoking `.validate()` in order
to specify how the dataframe should be validated.

Returns:

The original dataframe, if correctly validated.

Return type:

DataFrame[Model]

Raises:

- 

**TypeError** – If `DataFrame.set_model()` has not been invoked prior to
    validation. Note that `patito.Model.DataFrame` automatically invokes
    `DataFrame.set_model()` for you.

- 

**patito.exceptions.ValidationError** – If the dataframe does not match the
    specified schema.

Examples

```
>>> import patito as pt

```