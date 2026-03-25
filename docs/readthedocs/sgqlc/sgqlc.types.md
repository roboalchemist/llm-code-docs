# sgqlc.types module

## GraphQL Types in Python

This module fulfill two purposes:

- 

declare GraphQL schema in Python, just declare classes inheriting
`Type`, `Interface` and fill them with
`Field` (or base types: `str`, `int`, `float`,
`bool`). You may as well declare `Enum` with
`__choices__` or `Union` and `__types__`. Then
`__str__()` will provide nice printout and `__repr__()` will
return the GraphQL declarations (which can be tweaked with
`__to_graphql__()`, giving indent details). `__bytes__()` is
also provided, mapping to a compact `__to_graphql__()` version,
without indent.

- 

Interpret GraphQL JSON data, by instantiating the declared classes
with such information. While for scalar types it’s just a
pass-thru, for `Type` and `Interface` these will use
the fields to provide native object with attribute or key access
mapping to JSON, instead of `json_data['key']['other']` you may
use `obj.key.other`. Newly declared types, such as `DateTime`
will take care to generate native Python objects (ie:
`datetime.datetime`). Setting such attributes will also update
the backing store object, including converting back to valid JSON
values.