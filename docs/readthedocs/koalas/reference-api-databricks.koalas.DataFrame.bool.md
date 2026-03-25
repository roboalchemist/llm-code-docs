# databricks.koalas.DataFrame.bool

`DataFrame.``bool`() → bool

Return the bool of a single element in the current object.

This must be a boolean scalar value, either True or False. Raise a ValueError if
the object does not have exactly 1 element, or that element is not boolean

Returns

bool

Examples

```
>>> ks.DataFrame({'a': [True]}).bool()
True

```