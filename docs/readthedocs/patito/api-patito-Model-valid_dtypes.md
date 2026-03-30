# patito.Model.valid_dtypes

*property *Model.valid_dtypes*: dict[str, List[pl.PolarsDataType | pl.List]]*

Return a list of polars dtypes which Patito considers valid for each field.

The first item of each list is the default dtype chosen by Patito.

Returns:

A dictionary mapping each column string name to a list of valid dtypes.

Raises:

**NotImplementedError** – If one or more model fields are annotated with types
    not compatible with polars.

Example

```
>>> from pprint import pprint
>>> import patito as pt

```