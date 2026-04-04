# Source: https://docs.pylonsproject.org/projects/colander/en/latest/api.html

Title: Colander API — colander 2.0 documentation

URL Source: https://docs.pylonsproject.org/projects/colander/en/latest/api.html

Markdown Content:
Exceptions[¶](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#module-colander "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------

_class_ colander.Invalid(_node_, _msg=None_, _value=None_)[¶](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.Invalid "Link to this definition")
Raised by data types / validators

Raised if the value for a particular node is not valid.

The constructor receives a mandatory `node` argument. This must be an instance of the [`colander.SchemaNode`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.SchemaNode "colander.SchemaNode") class, or at least something with the same interface.

The constructor also receives an optional `msg` keyword argument, defaulting to `None`. The `msg` argument is a freeform field indicating the error circumstance.

The constructor additionally may receive an optional `value` keyword, indicating the value related to the error.

pos[¶](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.Invalid.pos "Link to this definition")
An integer representing the position of this exception's schema node relative to all other child nodes of this exception's parent schema node. For example, if this exception is related to the third child node of its parent's schema, `pos` might be the integer `3`. `pos` may also be `None`, in which case this exception is the root exception.

children[¶](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.Invalid.children "Link to this definition")
A list of child exceptions. Each element in this list (if any) will also be an [`colander.Invalid`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.Invalid "colander.Invalid") exception, recursively, representing the error circumstances for a particular schema deserialization.

msg[¶](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.Invalid.msg "Link to this definition")
A `str` or `unicode` object, or a _translation string_ instance representing a freeform error value set by a particular type during an unsuccessful deserialization. If this exception is only structural (only exists to be a parent to some inner child exception), this value will be `None`.

node[¶](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.Invalid.node "Link to this definition")
The schema node to which this exception relates.

value[¶](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.Invalid.value "Link to this definition")
An attribute not used internally by Colander, but which can be used by higher-level systems to attach arbitrary values to Colander exception nodes. For example, In the system named Deform, which uses Colander schemas to define HTML form renderings, the `value` is used when raising an exception from a widget as the value which should be redisplayed when an error is shown.

add(_exc_, _pos=None_)[¶](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.Invalid.add "Link to this definition")
Add a child exception to the list of children for this exception.

`exc` must be an instance of [`colander.Invalid`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.Invalid "colander.Invalid") or a subclass.

`pos` is a value important for accurate error reporting.

If it is provided, it must be an integer representing the position of `exc` relative to all other subexceptions of this exception node. For example, if the exception being added is about the third child of the exception which is `self`, `pos` might be passed as `3`.

If `pos` is provided, it will be assigned to the `pos` attribute of the provided `exc` object.

asdict(_translate=None_, _separator=';'_)[¶](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.Invalid.asdict "Link to this definition")
Return a dict holding a basic error report for this exception.

The values in the dict will **not** be language-translated by default.

If `translate` is supplied, it must be a callable taking a translation string as its sole argument and returning a localized, interpolated string. If so, the values in returned dict **will** be language-translated.

If `separator` is supplied, error messages are joined with that.

messages()[¶](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.Invalid.messages "Link to this definition")
Return an iterable of error messages for this exception.

Uses the `msg` attribute of this error node.

If the `msg` attribute is iterable, return it.

If it is not iterable, and is non-`None`, return a single-element list containing the `msg` value.

If the value is `None`, an empty list is returned.

paths()[¶](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.Invalid.paths "Link to this definition")
A generator yielding each path through the exception graph.

Each yielded path is represented as a tuple of exception nodes.

Within each tuple, the leftmost item will represent the root schema node, the rightmost item will represent the leaf schema node.

_class_ colander.UnsupportedFields(_node_, _fields_, _msg=None_)[¶](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.UnsupportedFields "Link to this definition")
Raised by a mapping schema which finds unknown fields cstruct.

fields[¶](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.UnsupportedFields.fields "Link to this definition")
The `dict` with all detected extra fields and their values.

Nodes that contain extra fields can be located by the position of this exception in the exception tree hierarchy.

_class_ colander.UnboundDeferredError[¶](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.UnboundDeferredError "Link to this definition")
Raised by [`SchemaNode.deserialize()`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.SchemaNode.deserialize "colander.SchemaNode.deserialize")

Raised when an attempt is made to deserialize a node which has an unbound [`deferred`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.deferred "colander.deferred") validator.

Validators[¶](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#validators "Link to this heading")
--------------------------------------------------------------------------------------------------------------------

> _class_ colander.All(_*validators_)[¶](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.All "Link to this definition")
> Composite validator
> 
> 
> Succeeds if none of its subvalidators raises [`colander.Invalid`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.Invalid "colander.Invalid").
> 
> _class_ colander.Any(_*validators_)[¶](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.Any "Link to this definition")
> Composite validator
> 
> 
> Succeeds if at least one of its subvalidators does not raise [`colander.Invalid`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.Invalid "colander.Invalid").
> 
> _class_ colander.Range(_min=None_, _max=None_, _min\_err='${val}is less than minimum value${min}'_, _max\_err='${val}is greater than maximum value${max}'_)[¶](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.Range "Link to this definition")
> Enforces that a value lies within a given range.
> 
> 
> Raises if the value it is less than `min` or greater than `max`.
> 
> 
> If `min` is not specified, or is specified as `None`, no lower bound is checked.
> 
> 
> If `max` is not specified, or is specified as `None`, no upper bound is checked.
> 
> 
> `min_err` is used to form the `msg` of the [`colander.Invalid`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.Invalid "colander.Invalid") error when reporting a validation failure where the value is less than minimum. If `min_err` is specified, it must be a string. The string may contain the replacement targets `${min}` and `${val}`, representing the minimum value and the provided value respectively. If not provided, `min_err` defaults to 
> ```
> '${val} is less than minimum value
> ${min}'
> ```
> .
> 
> 
> `max_err` is used to form the `msg` of the [`colander.Invalid`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.Invalid "colander.Invalid") error when reporting a validation failure where the value exceeds the maximum. If `max_err` is specified, it must be a string. The string may contain the replacement targets `${max}` and `${val}`, representing the maximum value and the provided value respectively. If it is not provided, it defaults to 
> ```
> '${val} is greater than maximum value
> ${max}'
> ```
> .
> 
> _class_ colander.Length(_min=None_, _max=None_, _min\_err='Shorter than minimum length${min}'_, _max\_err='Longer than maximum length${max}'_)[¶](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.Length "Link to this definition")
> Enforces that the length of a value falls within a given range.
> 
> 
> Raises if the value's length does not fall within the range described by the supplied `min` and `max` arguments.
> 
> 
> The value can be any sequence, most often a string.
> 
> 
> If `min` is not specified, or is specified as `None`, no lower bound on the length is checked.
> 
> 
> If `max` is not specified, or is specified as `None`, no upper bound on the length is checked.
> 
> 
> The default error messages are "Shorter than minimum length ${min}" and "Longer than maximum length ${max}". These can be customized:
> 
> 
> `min_err` is used to form the `msg` of the [`colander.Invalid`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.Invalid "colander.Invalid") error when reporting a validation failure where the value's length is less than `min`. If `min_err` is specified, it must be a string. The string may contain the replacement target `${min}`.
> 
> 
> `max_err` is used to form the `msg` of the [`colander.Invalid`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.Invalid "colander.Invalid") error when reporting a validation failure where the value's length is greater than `max`. If `max_err` is specified, it must be a string. The string may contain the replacement target `${max}`.
> 
> _class_ colander.OneOf(_choices_, _msg\_err='"${val}"is not one of${choices}'_)[¶](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.OneOf "Link to this definition")
> Enforces that a value is one of a fixed set of values.
> 
> 
> `msg_err` is used to form the `msg` of the [`colander.Invalid`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.Invalid "colander.Invalid") error when reporting a validation failure. If `msg_err` is specified, it must be a string. The string may contain the replacement targets `${choices}` and `${val}`, representing the set of forbidden values and the provided value respectively.
> 
> _class_ colander.NoneOf(_choices_, _msg\_err='"${val}"must not be one of${choices}'_)[¶](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.NoneOf "Link to this definition")
> Enforces that a value is _not_ one of a fixed set of values.
> 
> 
> `msg_err` is used to form the `msg` of the [`colander.Invalid`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.Invalid "colander.Invalid") error when reporting a validation failure. If `msg_err` is specified, it must be a string. The string may contain the replacement targets `${choices}` and `${val}`, representing the set of forbidden values and the provided value respectively.
> 
> _class_ colander.ContainsOnly(_choices_)[¶](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.ContainsOnly "Link to this definition")
> Enforces that each element in a sequence value is one of a fixeed set.
> 
> 
> Useful when attached to a schemanode with, e.g., a [`colander.Set`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.Set "colander.Set") or another sequencetype.
> 
> _class_ colander.Function(_function_, _msg=None_, _message=None_)[¶](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.Function "Link to this definition")
> Validator accepting a function and an optional message.
> 
> 
> `function` is called with `value` during validation.
> 
> 
> If `function` returns anything falsey (`None`, `False`, the empty string, `0`, an object with a `__nonzero__` that returns `False`, etc.), raise [`colander.Invalid`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.Invalid "colander.Invalid") (validation fails);
> 
> 
> The `msg` of the raised exception will be the value of the `msg` argument passed to this class' constructor.
> 
> 
> If `function` returns a `str` object that is _not_ the empty string, raise [`colander.Invalid`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.Invalid "colander.Invalid") using the string value returned from the function as the exception message (validation fails).
> 
> 
> If `function` returns anything which is truthy _except_ a string object (e.g., `True`, the integer `1`, an object with a `__nonzero__` that returns `True`, etc), do **not** raise [`colander.Invalid`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.Invalid "colander.Invalid") (validation succeeds).
> 
> 
> The default value for the `msg` when not provided via the constructor is `Invalid value`.
> 
> 
> The `message` parameter is deprecated: use `msg` instead.
> 
> _class_ colander.Regex(_regex_, _msg=None_, _flags=0_)[¶](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.Regex "Link to this definition")
> Regular expression validator.
> 
> 
> `regex` is a regular expression pattern that will be compiled and matched against `value` when validator is called.
> 
> 
> The compiled regex uses Python's `re.match()`, which only matches at the beginning of the string and not at the beginning of each line.
> 
> 
> To match the entire string, enclose the regular expression with `^` and `$`.
> 
> 
> If `msg` is supplied, it will be the error message to be used; otherwise, defaults to 'String does not match expected pattern'.
> 
> 
> The `regex` expression behaviour can be modified by specifying any `flags` value taken by `re.compile`.
> 
> 
> The `regex` argument may also be a pattern object (the result of `re.compile`) instead of a string.
> 
> 
> When called with `value` matching the regular expression, no exception is raised (validation succeeds);
> 
> 
> If `value` does not match the regular expression, raises [`colander.Invalid`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.Invalid "colander.Invalid") with the `msg` error message.
> 
> _class_ colander.Email(_msg=None_)[¶](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.Email "Link to this definition")
> Email address validator.
> 
> 
> If `msg` is supplied, it will be the error message to be used when raising [`colander.Invalid`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.Invalid "colander.Invalid"); otherwise, defaults to 'Invalid email address'.
> 
> _class_ colander.DataURL(_url\_err='Not a data URL'_, _mimetype\_err='Invalid MIME type'_, _base64\_err='Invalid Base64 encoded data'_)[¶](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.DataURL "Link to this definition")
> Data URL validator.
> 
> 
> If `url_msg` is supplied, it will be the error message to be used when raising [`colander.Invalid`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.Invalid "colander.Invalid") for a syntactically incorrect data URL, defaults to 'Not a data URL'.
> 
> 
> If, however, the data URL string is syntactically correct but contains an invalid MIME type, uses the supplied `mimetype_err` message (defaults to Invalid MIME type')
> 
> 
> If the data URL string is an incorrectly encoded Base64 value, passes the uses the supplied `base64_err` message (defaults to 'Invalid Base64 encoded data').
> 
> colander.luhnok(_node_, _value_)[¶](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.luhnok "Link to this definition")
> Enforces that the value passes a luhn mod-10 checksum (credit cards).
> 
> 
> `value` must be a string, not an integer.
> 
> colander.url[¶](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.url "Link to this definition")
> A validator which ensures the value is a URL (via regex).
> 
> colander.uuid[¶](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.uuid "Link to this definition")
> A UUID hexadecimal string validator via regular expression using [`colander.Regex`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.Regex "colander.Regex").

Types[¶](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#types "Link to this heading")
----------------------------------------------------------------------------------------------------------

> _class_ colander.Mapping(_unknown='ignore'_)[¶](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.Mapping "Link to this definition")
> A type which represents a mapping of names to nodes.
> 
> 
> The subnodes of the [`colander.SchemaNode`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.SchemaNode "colander.SchemaNode") that wraps this type imply the named keys and values in the mapping.
> 
> 
> The constructor of this type accepts one extra optional keyword argument that other types do not: `unknown`. An attribute of the same name can be set on a type instance to control the behavior after construction.
> 
> unknown
> `unknown` controls the behavior of this type when an unknown key is encountered in the cstruct passed to the `deserialize` method of this instance. All the potential values of `unknown` are strings. They are:
> 
> 
> *   `ignore` means that keys that are not present in the schema associated with this type will be ignored during deserialization.
> 
> *   `raise` will cause a [`colander.Invalid`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.Invalid "colander.Invalid") exception to be raised when unknown keys are present in the cstruct during deserialization.
> 
> *   `preserve` will preserve the 'raw' unknown keys and values in the appstruct returned by deserialization.
> 
> 
> 
> Default: `ignore`.
> 
> 
> Special behavior is exhibited when a subvalue of a mapping is present in the schema but is missing from the mapping passed to either the `serialize` or `deserialize` method of this class. In this case, the [`colander.null`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.null "colander.null") value will be passed to the `serialize` or `deserialize` method of the schema node representing the subvalue of the mapping respectively. During serialization, this will result in the behavior described in [Serializing The Null Value](https://docs.pylonsproject.org/projects/colander/en/latest/null_and_drop.html#serializing-null) for the subnode. During deserialization, this will result in the behavior described in [Deserializing The Null Value](https://docs.pylonsproject.org/projects/colander/en/latest/null_and_drop.html#deserializing-null) for the subnode.
> 
> 
> If the [`colander.null`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.null "colander.null") value is passed to the serialize method of this class, a dictionary will be returned, where each of the values in the returned dictionary is the serialized representation of the null value for its type.
> 
> _class_ colander.Tuple[¶](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.Tuple "Link to this definition")
> A type which represents a fixed-length sequence of nodes.
> 
> 
> The subnodes of the [`colander.SchemaNode`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.SchemaNode "colander.SchemaNode") that wraps this type imply the positional elements of the tuple in the order they are added.
> 
> 
> This type is willing to serialize and deserialized iterables that, when converted to a tuple, have the same number of elements as the number of the associated node's subnodes.
> 
> 
> If the [`colander.null`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.null "colander.null") value is passed to the serialize method of this class, the [`colander.null`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.null "colander.null") value will be returned.
> 
> _class_ colander.Set[¶](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.Set "Link to this definition")
> A type representing a non-overlapping set of items. Deserializes an iterable to a `set` object.
> 
> 
> If the [`colander.null`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.null "colander.null") value is passed to the serialize method of this class, the [`colander.null`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.null "colander.null") value will be returned.
> 
> _class_ colander.List[¶](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.List "Link to this definition")
> Type representing an ordered sequence of items.
> 
> 
> Deserializes an iterable to a `list` object.
> 
> 
> If the [`colander.null`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.null "colander.null") value is passed to the serialize method of this class, the [`colander.null`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.null "colander.null") value will be returned.
> 
> _class_ colander.Sequence(_accept\_scalar=False_)[¶](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.Sequence "Link to this definition")
> A type which represents a variable-length sequence of nodes, all of which must be of the same type.
> 
> 
> The type of the first subnode of the [`colander.SchemaNode`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.SchemaNode "colander.SchemaNode") that wraps this type is considered the sequence type.
> 
> 
> The optional `accept_scalar` argument to this type's constructor indicates what should happen if the value found during serialization or deserialization does not have an `__iter__` method or is a mapping type.
> 
> 
> If `accept_scalar` is `True` and the value does not have an `__iter__` method or is a mapping type, the value will be turned into a single element list.
> 
> 
> If `accept_scalar` is `False` and the value does not have an `__iter__` method or is a mapping type, an [`colander.Invalid`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.Invalid "colander.Invalid") error will be raised during serialization and deserialization.
> 
> 
> The default value of `accept_scalar` is `False`.
> 
> 
> If the [`colander.null`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.null "colander.null") value is passed to the serialize method of this class, the [`colander.null`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.null "colander.null") value is returned.
> 
> colander.Seq[¶](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.Seq "Link to this definition")
> alias of [`Sequence`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.Sequence "colander.Sequence")
> 
> _class_ colander.String(_encoding=None_, _allow\_empty=False_)[¶](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.String "Link to this definition")
> A type representing a text string.
> 
> 
> It is always an error to deserialize a non-text/binary type. Binary types are only accepted if the `encoding` argument is specified.
> 
> 
> This type constructor accepts two arguments:
> 
> `encoding`
> Represents the encoding which should be applied to value serialization and deserialization, for example `utf-8`. If `encoding` is passed as `None`, the `serialize` method of this type will not do any special encoding of the appstruct it is provided, nor will the `deserialize` method of this type do any special decoding of the cstruct it is provided; inputs and outputs will be assumed to be text. `encoding` defaults to `None`.
> 
> 
> If `encoding` is `None`:
> 
> 
> *   Any value to `serialize` is run through the `str` function to convert to text, and the result is returned.
> 
> *   A text input value to `deserialize` is returned untouched.
> 
> 
> 
> If `encoding` is not `None`:
> 
> 
> *   Any value to `serialize` is run through the `str` function to convert to text. The value is then encoded to binary with the encoding parameter (`bytes(value, encoding)`) and the result (a `bytes` object) is returned.
> 
> *   A text input value to `deserialize` is returned untouched.
> 
> *   A binary input value to `deserialize` is decoded to text using the encoding parameter (`str(value, encoding)`) and the result is returned.
> 
> 
> 
> A corollary: If a `bytes` (as opposed to a `str` object) is provided as a value to either the serialize or deserialize method of this type, and the type also has an non-`None``encoding`, the string must be encoded with the type's encoding. If this is not true, an [`colander.Invalid`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.Invalid "colander.Invalid") error will result.
> 
> `allow_empty`
> Boolean, if True allows deserialization of an empty string. If False (default), empty strings will deserialize to [`colander.null`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.null "colander.null")
> 
> 
> The subnodes of the [`colander.SchemaNode`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.SchemaNode "colander.SchemaNode") that wraps this type are ignored.
> 
> colander.Str[¶](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.Str "Link to this definition")
> alias of [`String`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.String "colander.String")
> 
> _class_ colander.Integer(_strict=False_)[¶](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.Integer "Link to this definition")
> A type representing an integer.
> 
> 
> If the [`colander.null`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.null "colander.null") value is passed to the serialize method of this class, the [`colander.null`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.null "colander.null") value will be returned.
> 
> 
> The Integer constructor takes an optional argument `strict`, which if enabled will verify that the number passed to serialize/deserialize is an integer, and not a float that would get truncated.
> 
> 
> The subnodes of the [`colander.SchemaNode`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.SchemaNode "colander.SchemaNode") that wraps this type are ignored.
> 
> colander.Int[¶](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.Int "Link to this definition")
> alias of [`Integer`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.Integer "colander.Integer")
> 
> _class_ colander.Float[¶](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.Float "Link to this definition")
> A type representing a float.
> 
> 
> If the [`colander.null`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.null "colander.null") value is passed to the serialize method of this class, the [`colander.null`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.null "colander.null") value will be returned.
> 
> 
> The subnodes of the [`colander.SchemaNode`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.SchemaNode "colander.SchemaNode") that wraps this type are ignored.
> 
> _class_ colander.Decimal(_quant=None_, _rounding=None_, _normalize=False_)[¶](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.Decimal "Link to this definition")
> A type representing a decimal floating point. Deserialization returns an instance of the Python `decimal.Decimal` type.
> 
> 
> If the [`colander.null`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.null "colander.null") value is passed to the serialize method of this class, the [`colander.null`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.null "colander.null") value will be returned.
> 
> 
> The Decimal constructor takes three optional arguments, `quant`, `rounding` and `normalize`. If supplied, `quant` should be a string, (e.g. `1.00`). If supplied, `rounding` should be one of the Python `decimal` module rounding options (e.g. `decimal.ROUND_UP`, `decimal.ROUND_DOWN`, etc). The serialized and deserialized result will be quantized and rounded via `result.quantize(decimal.Decimal(quant), rounding)`. `rounding` is ignored if `quant` is not supplied. If `normalize` is `True`, the serialized and deserialized result will be normalized by stripping the rightmost trailing zeros.
> 
> 
> The subnodes of the [`colander.SchemaNode`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.SchemaNode "colander.SchemaNode") that wraps this type are ignored.
> 
> _class_ colander.Boolean(_false\_choices=('false','0')_, _true\_choices=()_, _false\_val='false'_, _true\_val='true'_)[¶](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.Boolean "Link to this definition")
> A type representing a boolean object.
> 
> 
> The constructor accepts these keyword arguments:
> 
> 
> *   `false_choices`: The set of strings representing a `False` value on deserialization.
> 
> *   `true_choices`: The set of strings representing a `True` value on deserialization.
> 
> *   `false_val`: The value returned on serialization of a False value.
> 
> *   `true_val`: The value returned on serialization of a True value.
> 
> 
> 
> During deserialization, a value contained in `false_choices`, will be considered `False`.
> 
> 
> The behaviour for values not contained in `false_choices` depends on `true_choices`: if it's empty, any value is considered `True`; otherwise, only values contained in `true_choices` are considered `True`, and an Invalid exception would be raised for values outside of both `false_choices` and `true_choices`.
> 
> 
> Serialization will produce `true_val` or `false_val` based on the value.
> 
> 
> If the [`colander.null`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.null "colander.null") value is passed to the serialize method of this class, the [`colander.null`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.null "colander.null") value will be returned.
> 
> 
> The subnodes of the [`colander.SchemaNode`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.SchemaNode "colander.SchemaNode") that wraps this type are ignored.
> 
> colander.Bool[¶](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.Bool "Link to this definition")
> alias of [`Boolean`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.Boolean "colander.Boolean")
> 
> _class_ colander.GlobalObject(_package_)[¶](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.GlobalObject "Link to this definition")
> A type representing an importable Python object. This type serializes 'global' Python objects (objects which can be imported) to dotted Python names.
> 
> 
> Two dotted name styles are supported during deserialization:
> 
> 
> *   `pkg_resources`-style dotted names where non-module attributes of a module are separated from the rest of the path using a ':' e.g. `package.module:attr`.
> 
> *   `zope.dottedname`-style dotted names where non-module attributes of a module are separated from the rest of the path using a '.' e.g. `package.module.attr`.
> 
> 
> 
> These styles can be used interchangeably. If the serialization contains a `:` (colon), the `pkg_resources` resolution mechanism will be chosen, otherwise the `zope.dottedname` resolution mechanism will be chosen.
> 
> 
> The constructor accepts a single argument named `package` which should be a Python module or package object; it is used when _relative_ dotted names are supplied to the `deserialize` method. A serialization which has a `.` (dot) or `:` (colon) as its first character is treated as relative. E.g. if `.minidom` is supplied to `deserialize`, and the `package` argument to this type was passed the `xml` module object, the resulting import would be for `xml.minidom`. If a relative package name is supplied to `deserialize`, and no `package` was supplied to the constructor, an [`colander.Invalid`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.Invalid "colander.Invalid") error will be raised.
> 
> 
> If the [`colander.null`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.null "colander.null") value is passed to the serialize method of this class, the [`colander.null`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.null "colander.null") value will be returned.
> 
> 
> The subnodes of the [`colander.SchemaNode`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.SchemaNode "colander.SchemaNode") that wraps this type are ignored.
> 
> _class_ colander.DateTime(_default\_tzinfo=datetime.timezone.utc_, _format=None_)[¶](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.DateTime "Link to this definition")
> A type representing a Python `datetime.datetime` object.
> 
> 
> This type serializes python `datetime.datetime` objects to a [ISO8601](https://en.wikipedia.org/wiki/ISO_8601) string format. The format includes the date, the time, and the timezone of the datetime.
> 
> 
> The constructor accepts an argument named `default_tzinfo` which should be a Python `tzinfo` object. If `default_tzinfo` is not specified the default tzinfo will be equivalent to UTC (Zulu time). The `default_tzinfo` tzinfo object is used to convert 'naive' datetimes to a timezone-aware representation during serialization. If `default_tzinfo` is explicitly set to `None` then no default tzinfo will be applied to naive datetimes.
> 
> 
> You can adjust the error message reported by this class by changing its `err_template` attribute in a subclass on an instance of this class. By default, the `err_template` attribute is the string `Invalid date`. This string is used as the interpolation subject of a dictionary composed of `val` and `err`. `val` and `err` are the unvalidatable value and the exception caused trying to convert the value, respectively. These may be used in an overridden err_template as `${val}` and `${err}` respectively as necessary, e.g. 
> ```
> _('${val} cannot be
> parsed as an iso8601 date: ${err}')
> ```
> .
> 
> 
> For convenience, this type is also willing to coerce `datetime.date` objects to a DateTime ISO string representation during serialization. It does so by using midnight of the day as the time, and uses the `default_tzinfo` to give the serialization a timezone.
> 
> 
> Likewise, for convenience, during deserialization, this type will convert `YYYY-MM-DD` ISO8601 values to a datetime object. It does so by using midnight of the day as the time, and uses the `default_tzinfo` to give the serialization a timezone.
> 
> 
> If the [`colander.null`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.null "colander.null") value is passed to the serialize method of this class, the [`colander.null`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.null "colander.null") value will be returned.
> 
> 
> The subnodes of the [`colander.SchemaNode`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.SchemaNode "colander.SchemaNode") that wraps this type are ignored.
> 
> _class_ colander.Date(_format=None_)[¶](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.Date "Link to this definition")
> A type representing a Python `datetime.date` object.
> 
> 
> This type serializes python `datetime.date` objects to a [ISO8601](https://en.wikipedia.org/wiki/ISO_8601) string format. The format includes the date only.
> 
> 
> The constructor accepts no arguments.
> 
> 
> You can adjust the error message reported by this class by changing its `err_template` attribute in a subclass on an instance of this class. By default, the `err_template` attribute is the string `Invalid date`. This string is used as the interpolation subject of a dictionary composed of `val` and `err`. `val` and `err` are the unvalidatable value and the exception caused trying to convert the value, respectively. These may be used in an overridden err_template as `${val}` and `${err}` respectively as necessary, e.g. 
> ```
> _('${val} cannot be
> parsed as an iso8601 date: ${err}')
> ```
> .
> 
> 
> For convenience, this type is also willing to coerce `datetime.datetime` objects to a date-only ISO string representation during serialization. It does so by stripping off any time information, converting the `datetime.datetime` into a date before serializing.
> 
> 
> Likewise, for convenience, this type is also willing to coerce ISO representations that contain time info into a `datetime.date` object during deserialization. It does so by throwing away any time information related to the serialized value during deserialization.
> 
> 
> If the [`colander.null`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.null "colander.null") value is passed to the serialize method of this class, the [`colander.null`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.null "colander.null") value will be returned.
> 
> 
> The subnodes of the [`colander.SchemaNode`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.SchemaNode "colander.SchemaNode") that wraps this type are ignored.
> 
> _class_ colander.Time[¶](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.Time "Link to this definition")
> A type representing a Python `datetime.time` object.
> 
> 
> 
> Note
> 
> 
> This type is new as of Colander 0.9.3.
> 
> 
> This type serializes python `datetime.time` objects to a [ISO8601](https://en.wikipedia.org/wiki/ISO_8601) string format. The format includes the time only.
> 
> 
> The constructor accepts no arguments.
> 
> 
> You can adjust the error message reported by this class by changing its `err_template` attribute in a subclass on an instance of this class. By default, the `err_template` attribute is the string `Invalid date`. This string is used as the interpolation subject of a dictionary composed of `val` and `err`. `val` and `err` are the unvalidatable value and the exception caused trying to convert the value, respectively. These may be used in an overridden err_template as `${val}` and `${err}` respectively as necessary, e.g. 
> ```
> _('${val} cannot be
> parsed as an iso8601 date: ${err}')
> ```
> .
> 
> 
> For convenience, this type is also willing to coerce `datetime.datetime` objects to a time-only ISO string representation during serialization. It does so by stripping off any date information, converting the `datetime.datetime` into a time before serializing.
> 
> 
> Likewise, for convenience, this type is also willing to coerce ISO representations that contain time info into a `datetime.time` object during deserialization. It does so by throwing away any date information related to the serialized value during deserialization.
> 
> 
> If the [`colander.null`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.null "colander.null") value is passed to the serialize method of this class, the [`colander.null`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.null "colander.null") value will be returned.
> 
> 
> The subnodes of the [`colander.SchemaNode`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.SchemaNode "colander.SchemaNode") that wraps this type are ignored.
> 
> _class_ colander.Enum(_enum\_cls_, _attr=None_, _typ=None_)[¶](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.Enum "Link to this definition")
> A type representing a Python `enum.Enum` object.
> 
> 
> The constructor accepts three arguments named `enum_cls`, `attr`, and `typ`.
> 
> 
> `enum_cls` is a mandatory argument and it should be a subclass of `enum.Enum`. This argument represents the appstruct's type.
> 
> 
> `attr` is an optional argument. Its default is `name`. It is used to pick a serialized value from an enum instance. A serialized value must be unique.
> 
> 
> `typ` is an optional argument, and it should be an instance of `colander.SchemaType`. This argument represents the cstruct's type. If `typ` is not specified, a plain `colander.String` is used.
