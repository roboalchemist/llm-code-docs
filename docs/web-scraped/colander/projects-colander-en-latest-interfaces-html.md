# Source: https://docs.pylonsproject.org/projects/colander/en/latest/interfaces.html

Title: Interfaces — colander 2.0 documentation

URL Source: https://docs.pylonsproject.org/projects/colander/en/latest/interfaces.html

Markdown Content:
colander.interfaces.Preparer(_value_)[¶](https://docs.pylonsproject.org/projects/colander/en/latest/interfaces.html#colander.interfaces.Preparer "Link to this definition")
A preparer is called after deserialization of a value but before that value is validated.

Any modifications to `value` required should be made by returning the modified value rather than modifying in-place.

If no modification is required, then `value` should be returned as-is.

colander.interfaces.Validator(_node_, _value_)[¶](https://docs.pylonsproject.org/projects/colander/en/latest/interfaces.html#colander.interfaces.Validator "Link to this definition")
A validator is called after preparation of the deserialized value.

If `value` is not valid, raise a [`colander.Invalid`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.Invalid "colander.Invalid") instance as an exception after.

`node` is a [`colander.SchemaNode`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.SchemaNode "colander.SchemaNode") instance, for use when raising a [`colander.Invalid`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.Invalid "colander.Invalid") exception.

_class_ colander.interfaces.Type[¶](https://docs.pylonsproject.org/projects/colander/en/latest/interfaces.html#colander.interfaces.Type "Link to this definition")deserialize(_node_, _cstruct_)[¶](https://docs.pylonsproject.org/projects/colander/en/latest/interfaces.html#colander.interfaces.Type.deserialize "Link to this definition")
Deserialze the [cstruct](https://docs.pylonsproject.org/projects/colander/en/latest/glossary.html#term-cstruct) represented by `cstruct` to an [appstruct](https://docs.pylonsproject.org/projects/colander/en/latest/glossary.html#term-appstruct). The deserialization should be composed of one or more objects which can be serialized by the [`colander.interfaces.Type.serialize()`](https://docs.pylonsproject.org/projects/colander/en/latest/interfaces.html#colander.interfaces.Type.serialize "colander.interfaces.Type.serialize") method of this type.

`node` is a [`colander.SchemaNode`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.SchemaNode "colander.SchemaNode") instance.

`cstruct` is a [cstruct](https://docs.pylonsproject.org/projects/colander/en/latest/glossary.html#term-cstruct).

If the object cannot be deserialized for any reason, a [`colander.Invalid`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.Invalid "colander.Invalid") exception should be raised.

serialize(_node_, _appstruct_)[¶](https://docs.pylonsproject.org/projects/colander/en/latest/interfaces.html#colander.interfaces.Type.serialize "Link to this definition")
Serialize the [appstruct](https://docs.pylonsproject.org/projects/colander/en/latest/glossary.html#term-appstruct) represented by `appstruct` to a [cstruct](https://docs.pylonsproject.org/projects/colander/en/latest/glossary.html#term-cstruct). The serialization should be composed of one or more objects which can be deserialized by the [`colander.interfaces.Type.deserialize()`](https://docs.pylonsproject.org/projects/colander/en/latest/interfaces.html#colander.interfaces.Type.deserialize "colander.interfaces.Type.deserialize") method of this type.

`node` is a [`colander.SchemaNode`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.SchemaNode "colander.SchemaNode") instance.

`appstruct` is an [appstruct](https://docs.pylonsproject.org/projects/colander/en/latest/glossary.html#term-appstruct).

If `appstruct` is the special value [`colander.null`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.null "colander.null"), the type should serialize a null value.

If the object cannot be serialized for any reason, a [`colander.Invalid`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.Invalid "colander.Invalid") exception should be raised.
