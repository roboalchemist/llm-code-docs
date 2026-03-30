# Source: https://python-jsonschema.readthedocs.io/en/latest/errors/

Title: Handling Validation Errors

URL Source: https://python-jsonschema.readthedocs.io/en/latest/errors/

Markdown Content:
When an invalid instance is encountered, a [`ValidationError`](https://python-jsonschema.readthedocs.io/en/latest/api/jsonschema/exceptions/#jsonschema.exceptions.ValidationError "jsonschema.exceptions.ValidationError") will be raised or returned, depending on which method or function is used.

_exception_ jsonschema.exceptions.ValidationError(_message:str_, _validator:str=<unset>_, _path:Iterable[str|int]=()_, _cause:Exception|None=None_, _context=()_, _validator\_value:Any=<unset>_, _instance:Any=<unset>_, _schema:Mapping[str_, _Any]|bool=<unset>_, _schema\_path:Iterable[str|int]=()_, _parent:\_Error|None=None_, _type\_checker:\_types.TypeChecker=<unset>_)[[source]](https://python-jsonschema.readthedocs.io/en/latest/_modules/jsonschema/exceptions/#ValidationError)
An instance was invalid under a provided schema.

The information carried by an error roughly breaks down into:

| What Happened | Why Did It Happen | What Was Being Validated |
| --- | --- | --- |
| [`message`](https://python-jsonschema.readthedocs.io/en/latest/errors/#jsonschema.exceptions.ValidationError.message "jsonschema.exceptions.ValidationError.message") | [`context`](https://python-jsonschema.readthedocs.io/en/latest/errors/#jsonschema.exceptions.ValidationError.context "jsonschema.exceptions.ValidationError.context") [`cause`](https://python-jsonschema.readthedocs.io/en/latest/errors/#jsonschema.exceptions.ValidationError.cause "jsonschema.exceptions.ValidationError.cause") | [`instance`](https://python-jsonschema.readthedocs.io/en/latest/errors/#jsonschema.exceptions.ValidationError.instance "jsonschema.exceptions.ValidationError.instance") [`json_path`](https://python-jsonschema.readthedocs.io/en/latest/errors/#jsonschema.exceptions.ValidationError.json_path "jsonschema.exceptions.ValidationError.json_path") [`path`](https://python-jsonschema.readthedocs.io/en/latest/errors/#jsonschema.exceptions.ValidationError.path "jsonschema.exceptions.ValidationError.path") [`schema`](https://python-jsonschema.readthedocs.io/en/latest/errors/#jsonschema.exceptions.ValidationError.schema "jsonschema.exceptions.ValidationError.schema") [`schema_path`](https://python-jsonschema.readthedocs.io/en/latest/errors/#jsonschema.exceptions.ValidationError.schema_path "jsonschema.exceptions.ValidationError.schema_path") [`validator`](https://python-jsonschema.readthedocs.io/en/latest/errors/#jsonschema.exceptions.ValidationError.validator "jsonschema.exceptions.ValidationError.validator") [`validator_value`](https://python-jsonschema.readthedocs.io/en/latest/errors/#jsonschema.exceptions.ValidationError.validator_value "jsonschema.exceptions.ValidationError.validator_value") |

message[¶](https://python-jsonschema.readthedocs.io/en/latest/errors/#jsonschema.exceptions.ValidationError.message "Link to this definition")
A human readable message explaining the error.

validator[¶](https://python-jsonschema.readthedocs.io/en/latest/errors/#jsonschema.exceptions.ValidationError.validator "Link to this definition")
The name of the failed [keyword](https://json-schema.org/draft/2020-12/json-schema-validation.html#name-a-vocabulary-for-structural).

validator_value[¶](https://python-jsonschema.readthedocs.io/en/latest/errors/#jsonschema.exceptions.ValidationError.validator_value "Link to this definition")
The associated value for the failed keyword in the schema.

schema[¶](https://python-jsonschema.readthedocs.io/en/latest/errors/#jsonschema.exceptions.ValidationError.schema "Link to this definition")
The full schema that this error came from. This is potentially a subschema from within the schema that was passed in originally, or even an entirely different schema if a [$ref](https://json-schema.org/draft/2020-12/json-schema-core.html#ref) was followed.

relative_schema_path[¶](https://python-jsonschema.readthedocs.io/en/latest/errors/#jsonschema.exceptions.ValidationError.relative_schema_path "Link to this definition")
A [`collections.deque`](https://docs.python.org/3/library/collections.html#collections.deque "(in Python v3.14)") containing the path to the failed keyword within the schema.

absolute_schema_path[¶](https://python-jsonschema.readthedocs.io/en/latest/errors/#jsonschema.exceptions.ValidationError.absolute_schema_path "Link to this definition")
A [`collections.deque`](https://docs.python.org/3/library/collections.html#collections.deque "(in Python v3.14)") containing the path to the failed keyword within the schema, but always relative to the _original_ schema as opposed to any subschema (i.e. the one originally passed into a validator class, _not_[`schema`](https://python-jsonschema.readthedocs.io/en/latest/errors/#jsonschema.exceptions.ValidationError.schema "jsonschema.exceptions.ValidationError.schema")).

schema_path[¶](https://python-jsonschema.readthedocs.io/en/latest/errors/#jsonschema.exceptions.ValidationError.schema_path "Link to this definition")
Same as [`relative_schema_path`](https://python-jsonschema.readthedocs.io/en/latest/errors/#jsonschema.exceptions.ValidationError.relative_schema_path "jsonschema.exceptions.ValidationError.relative_schema_path").

relative_path[¶](https://python-jsonschema.readthedocs.io/en/latest/errors/#jsonschema.exceptions.ValidationError.relative_path "Link to this definition")
A [`collections.deque`](https://docs.python.org/3/library/collections.html#collections.deque "(in Python v3.14)") containing the path to the offending element within the instance. The deque can be empty if the error happened at the root of the instance.

absolute_path[¶](https://python-jsonschema.readthedocs.io/en/latest/errors/#jsonschema.exceptions.ValidationError.absolute_path "Link to this definition")
A [`collections.deque`](https://docs.python.org/3/library/collections.html#collections.deque "(in Python v3.14)") containing the path to the offending element within the instance. The absolute path is always relative to the _original_ instance that was validated (i.e. the one passed into a validation method, _not_[`instance`](https://python-jsonschema.readthedocs.io/en/latest/errors/#jsonschema.exceptions.ValidationError.instance "jsonschema.exceptions.ValidationError.instance")). The deque can be empty if the error happened at the root of the instance.

json_path[¶](https://python-jsonschema.readthedocs.io/en/latest/errors/#jsonschema.exceptions.ValidationError.json_path "Link to this definition")
A [JSON path](https://goessner.net/articles/JsonPath/index.html) to the offending element within the instance.

path[¶](https://python-jsonschema.readthedocs.io/en/latest/errors/#jsonschema.exceptions.ValidationError.path "Link to this definition")
Same as [`relative_path`](https://python-jsonschema.readthedocs.io/en/latest/errors/#jsonschema.exceptions.ValidationError.relative_path "jsonschema.exceptions.ValidationError.relative_path").

instance[¶](https://python-jsonschema.readthedocs.io/en/latest/errors/#jsonschema.exceptions.ValidationError.instance "Link to this definition")
The instance that was being validated. This will differ from the instance originally passed into `validate` if the validator object was in the process of validating a (possibly nested) element within the top-level instance. The path within the top-level instance (i.e. [`ValidationError.path`](https://python-jsonschema.readthedocs.io/en/latest/errors/#jsonschema.exceptions.ValidationError.path "jsonschema.exceptions.ValidationError.path")) could be used to find this object, but it is provided for convenience.

context[¶](https://python-jsonschema.readthedocs.io/en/latest/errors/#jsonschema.exceptions.ValidationError.context "Link to this definition")
If the error was caused by errors in subschemas, the list of errors from the subschemas will be available on this property. The [`schema_path`](https://python-jsonschema.readthedocs.io/en/latest/errors/#jsonschema.exceptions.ValidationError.schema_path "jsonschema.exceptions.ValidationError.schema_path") and [`path`](https://python-jsonschema.readthedocs.io/en/latest/errors/#jsonschema.exceptions.ValidationError.path "jsonschema.exceptions.ValidationError.path") of these errors will be relative to the parent error.

cause[¶](https://python-jsonschema.readthedocs.io/en/latest/errors/#jsonschema.exceptions.ValidationError.cause "Link to this definition")
If the error was caused by a _non_-validation error, the exception object will be here. Currently this is only used for the exception raised by a failed format checker in [`jsonschema.FormatChecker.check`](https://python-jsonschema.readthedocs.io/en/latest/api/#jsonschema.FormatChecker.check "jsonschema.FormatChecker.check").

parent[¶](https://python-jsonschema.readthedocs.io/en/latest/errors/#jsonschema.exceptions.ValidationError.parent "Link to this definition")
A validation error which this error is the [`context`](https://python-jsonschema.readthedocs.io/en/latest/errors/#jsonschema.exceptions.ValidationError.context "jsonschema.exceptions.ValidationError.context") of. `None` if there wasn’t one.

In case an invalid schema itself is encountered, a [`SchemaError`](https://python-jsonschema.readthedocs.io/en/latest/api/jsonschema/exceptions/#jsonschema.exceptions.SchemaError "jsonschema.exceptions.SchemaError") is raised.

_exception_ jsonschema.exceptions.SchemaError(_message:str_, _validator:str=<unset>_, _path:Iterable[str|int]=()_, _cause:Exception|None=None_, _context=()_, _validator\_value:Any=<unset>_, _instance:Any=<unset>_, _schema:Mapping[str_, _Any]|bool=<unset>_, _schema\_path:Iterable[str|int]=()_, _parent:\_Error|None=None_, _type\_checker:\_types.TypeChecker=<unset>_)[[source]](https://python-jsonschema.readthedocs.io/en/latest/_modules/jsonschema/exceptions/#SchemaError)
A schema was invalid under its corresponding metaschema.

The same attributes are present as for [`ValidationError`](https://python-jsonschema.readthedocs.io/en/latest/api/jsonschema/exceptions/#jsonschema.exceptions.ValidationError "jsonschema.exceptions.ValidationError")s.

These attributes can be clarified with a short example:

schema = {
    "items": {
        "anyOf": [
            {"type": "string", "maxLength": 2},
            {"type": "integer", "minimum": 5}
        ]
    }
}
instance = [{}, 3, "foo"]
v = Draft202012Validator(schema)
errors = sorted(v.iter_errors(instance), key=lambda e: e.path)

The error messages in this situation are not very helpful on their own.

for error in errors:
    print(error.message)

outputs:

{} is not valid under any of the given schemas
3 is not valid under any of the given schemas
'foo' is not valid under any of the given schemas

If we look at [`ValidationError.path`](https://python-jsonschema.readthedocs.io/en/latest/errors/#jsonschema.exceptions.ValidationError.path "jsonschema.exceptions.ValidationError.path") on each of the errors, we can find out which elements in the instance correspond to each of the errors. In this example, [`ValidationError.path`](https://python-jsonschema.readthedocs.io/en/latest/errors/#jsonschema.exceptions.ValidationError.path "jsonschema.exceptions.ValidationError.path") will have only one element, which will be the index in our list.

for error in errors:
    print(list(error.path))

[0]
[1]
[2]

Since our schema contained nested subschemas, it can be helpful to look at the specific part of the instance and subschema that caused each of the errors. This can be seen with the [`ValidationError.instance`](https://python-jsonschema.readthedocs.io/en/latest/errors/#jsonschema.exceptions.ValidationError.instance "jsonschema.exceptions.ValidationError.instance") and [`ValidationError.schema`](https://python-jsonschema.readthedocs.io/en/latest/errors/#jsonschema.exceptions.ValidationError.schema "jsonschema.exceptions.ValidationError.schema") attributes.

With keywords like [anyOf](https://json-schema.org/draft/2020-12/json-schema-core.html#section-10.2.1.2), the [`ValidationError.context`](https://python-jsonschema.readthedocs.io/en/latest/errors/#jsonschema.exceptions.ValidationError.context "jsonschema.exceptions.ValidationError.context") attribute can be used to see the sub-errors which caused the failure. Since these errors actually came from two separate subschemas, it can be helpful to look at the [`ValidationError.schema_path`](https://python-jsonschema.readthedocs.io/en/latest/errors/#jsonschema.exceptions.ValidationError.schema_path "jsonschema.exceptions.ValidationError.schema_path") attribute as well to see where exactly in the schema each of these errors come from. In the case of sub-errors from the [`ValidationError.context`](https://python-jsonschema.readthedocs.io/en/latest/errors/#jsonschema.exceptions.ValidationError.context "jsonschema.exceptions.ValidationError.context") attribute, this path will be relative to the [`ValidationError.schema_path`](https://python-jsonschema.readthedocs.io/en/latest/errors/#jsonschema.exceptions.ValidationError.schema_path "jsonschema.exceptions.ValidationError.schema_path") of the parent error.

for error in errors:
    for suberror in sorted(error.context, key=lambda e: e.schema_path):
        print(list(suberror.schema_path), suberror.message, sep=", ")

[0, 'type'], {} is not of type 'string'
[1, 'type'], {} is not of type 'integer'
[0, 'type'], 3 is not of type 'string'
[1, 'minimum'], 3 is less than the minimum of 5
[0, 'maxLength'], 'foo' is too long
[1, 'type'], 'foo' is not of type 'integer'

The string representation of an error combines some of these attributes for easier debugging.

print(errors[1])

3 is not valid under any of the given schemas

Failed validating 'anyOf' in schema['items']:
    {'anyOf': [{'type': 'string', 'maxLength': 2},
               {'type': 'integer', 'minimum': 5}]}

On instance[1]:
    3

ErrorTrees[¶](https://python-jsonschema.readthedocs.io/en/latest/errors/#errortrees "Link to this heading")
-----------------------------------------------------------------------------------------------------------

If you want to programmatically query which validation keywords failed when validating a given instance, you may want to do so using [`jsonschema.exceptions.ErrorTree`](https://python-jsonschema.readthedocs.io/en/latest/api/jsonschema/exceptions/#jsonschema.exceptions.ErrorTree "jsonschema.exceptions.ErrorTree") objects.

_class_ jsonschema.exceptions.ErrorTree(_errors:Iterable[[ValidationError](https://python-jsonschema.readthedocs.io/en/latest/api/jsonschema/exceptions/#jsonschema.exceptions.ValidationError "jsonschema.exceptions.ValidationError")]=()_)[[source]](https://python-jsonschema.readthedocs.io/en/latest/_modules/jsonschema/exceptions/#ErrorTree)
ErrorTrees make it easier to check which validations failed.

errors[¶](https://python-jsonschema.readthedocs.io/en/latest/errors/#jsonschema.exceptions.ErrorTree.errors "Link to this definition")
The mapping of validation keywords to the error objects (usually [`jsonschema.exceptions.ValidationError`](https://python-jsonschema.readthedocs.io/en/latest/api/jsonschema/exceptions/#jsonschema.exceptions.ValidationError "jsonschema.exceptions.ValidationError")s) at this level of the tree.

 __contains__ (_index:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")|[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")_)[[source]](https://python-jsonschema.readthedocs.io/en/latest/_modules/jsonschema/exceptions/#ErrorTree.__contains__)
Check whether `instance[index]` has any errors.

 __getitem__ (_index_)[[source]](https://python-jsonschema.readthedocs.io/en/latest/_modules/jsonschema/exceptions/#ErrorTree.__getitem__)
Retrieve the child tree one level down at the given `index`.

If the index is not in the instance that this tree corresponds to and is not known by this tree, whatever error would be raised by `instance.__getitem__` will be propagated (usually this is some subclass of [`LookupError`](https://docs.python.org/3/library/exceptions.html#LookupError "(in Python v3.14)").

 __init__ (_errors:Iterable[[ValidationError](https://python-jsonschema.readthedocs.io/en/latest/api/jsonschema/exceptions/#jsonschema.exceptions.ValidationError "jsonschema.exceptions.ValidationError")]=()_)[[source]](https://python-jsonschema.readthedocs.io/en/latest/_modules/jsonschema/exceptions/#ErrorTree.__init__) __iter__ ()[[source]](https://python-jsonschema.readthedocs.io/en/latest/_modules/jsonschema/exceptions/#ErrorTree.__iter__)
Iterate (non-recursively) over the indices in the instance with errors.

 __len__ ()[[source]](https://python-jsonschema.readthedocs.io/en/latest/_modules/jsonschema/exceptions/#ErrorTree.__len__)
Return the [`total_errors`](https://python-jsonschema.readthedocs.io/en/latest/api/jsonschema/exceptions/#jsonschema.exceptions.ErrorTree.total_errors "jsonschema.exceptions.ErrorTree.total_errors").

 __repr__ ()[[source]](https://python-jsonschema.readthedocs.io/en/latest/_modules/jsonschema/exceptions/#ErrorTree.__repr__)
Return repr(self).

 __setitem__ (_index:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")|[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")_, _value:[ErrorTree](https://python-jsonschema.readthedocs.io/en/latest/api/jsonschema/exceptions/#jsonschema.exceptions.ErrorTree "jsonschema.exceptions.ErrorTree")_)[[source]](https://python-jsonschema.readthedocs.io/en/latest/_modules/jsonschema/exceptions/#ErrorTree.__setitem__)
Add an error to the tree at the given `index`.

Deprecated since version v4.20.0: Setting items on an [`ErrorTree`](https://python-jsonschema.readthedocs.io/en/latest/api/jsonschema/exceptions/#jsonschema.exceptions.ErrorTree "jsonschema.exceptions.ErrorTree") is deprecated without replacement. To populate a tree, provide all of its sub-errors when you construct the tree.

_property_ total_errors
The total number of errors in the entire tree, including children.

Consider the following example:

schema = {
    "type" : "array",
    "items" : {"type" : "number", "enum" : [1, 2, 3]},
    "minItems" : 3,
}
instance = ["spam", 2]

For clarity’s sake, the given instance has three errors under this schema:

v = Draft202012Validator(schema)
for error in sorted(v.iter_errors(["spam", 2]), key=str):
    print(error.message)

'spam' is not of type 'number'
'spam' is not one of [1, 2, 3]
['spam', 2] is too short

Let’s construct an [`jsonschema.exceptions.ErrorTree`](https://python-jsonschema.readthedocs.io/en/latest/api/jsonschema/exceptions/#jsonschema.exceptions.ErrorTree "jsonschema.exceptions.ErrorTree") so that we can query the errors a bit more easily than by just iterating over the error objects.

from jsonschema.exceptions import ErrorTree
tree = ErrorTree(v.iter_errors(instance))

As you can see, [`jsonschema.exceptions.ErrorTree`](https://python-jsonschema.readthedocs.io/en/latest/api/jsonschema/exceptions/#jsonschema.exceptions.ErrorTree "jsonschema.exceptions.ErrorTree") takes an iterable of [`ValidationError`](https://python-jsonschema.readthedocs.io/en/latest/api/jsonschema/exceptions/#jsonschema.exceptions.ValidationError "jsonschema.exceptions.ValidationError")s when constructing a tree so you can directly pass it the return value of a validator’s [`jsonschema.protocols.Validator.iter_errors`](https://python-jsonschema.readthedocs.io/en/latest/api/jsonschema/protocols/#jsonschema.protocols.Validator.iter_errors "jsonschema.protocols.Validator.iter_errors") method.

[`ErrorTree`](https://python-jsonschema.readthedocs.io/en/latest/api/jsonschema/exceptions/#jsonschema.exceptions.ErrorTree "jsonschema.exceptions.ErrorTree")s support a number of useful operations. The first one we might want to perform is to check whether a given element in our instance failed validation. We do so using the [`in`](https://docs.python.org/3/reference/expressions.html#in "(in Python v3.14)") operator:

>>> 0 in tree
True

>>> 1 in tree
False

The interpretation here is that the 0th index into the instance (`"spam"`) did have an error (in fact it had 2), while the 1th index (`2`) did not (i.e. it was valid).

If we want to see which errors a child had, we index into the tree and look at the [`ErrorTree.errors`](https://python-jsonschema.readthedocs.io/en/latest/errors/#jsonschema.exceptions.ErrorTree.errors "jsonschema.exceptions.ErrorTree.errors") attribute.

>>> sorted(tree[0].errors)
['enum', 'type']

Here we see that the [enum](https://json-schema.org/draft/2020-12/json-schema-validation.html#section-6.1.2) and [type](https://json-schema.org/draft/2020-12/json-schema-validation.html#section-6.1.1) keywords failed for index `0`. In fact [`ErrorTree.errors`](https://python-jsonschema.readthedocs.io/en/latest/errors/#jsonschema.exceptions.ErrorTree.errors "jsonschema.exceptions.ErrorTree.errors") is a dict, whose values are the [`ValidationError`](https://python-jsonschema.readthedocs.io/en/latest/api/jsonschema/exceptions/#jsonschema.exceptions.ValidationError "jsonschema.exceptions.ValidationError")s, so we can get at those directly if we want them.

>>> print(tree[0].errors["type"].message)
'spam' is not of type 'number'

Of course this means that if we want to know if a given validation keyword failed for a given index, we check for its presence in [`ErrorTree.errors`](https://python-jsonschema.readthedocs.io/en/latest/errors/#jsonschema.exceptions.ErrorTree.errors "jsonschema.exceptions.ErrorTree.errors"):

>>> "enum" in tree[0].errors
True

>>> "minimum" in tree[0].errors
False

Finally, if you were paying close enough attention, you’ll notice that we haven’t seen our [minItems](https://json-schema.org/draft/2020-12/json-schema-validation.html#section-6.4.2) error appear anywhere yet. This is because [minItems](https://json-schema.org/draft/2020-12/json-schema-validation.html#section-6.4.2) is an error that applies globally to the instance itself. So it appears in the root node of the tree.

>>> "minItems" in tree.errors
True

That’s all you need to know to use error trees.

To summarize, each tree contains child trees that can be accessed by indexing the tree to get the corresponding child tree for a given index into the instance. Each tree and child has a [`ErrorTree.errors`](https://python-jsonschema.readthedocs.io/en/latest/errors/#jsonschema.exceptions.ErrorTree.errors "jsonschema.exceptions.ErrorTree.errors") attribute, a dict, that maps the failed validation keyword to the corresponding validation error.

best_match and relevance[¶](https://python-jsonschema.readthedocs.io/en/latest/errors/#best-match-and-relevance "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------

The [`best_match`](https://python-jsonschema.readthedocs.io/en/latest/api/jsonschema/exceptions/#jsonschema.exceptions.best_match "jsonschema.exceptions.best_match") function is a simple but useful function for attempting to guess the most relevant error in a given bunch.

>>> from jsonschema import Draft202012Validator
>>> from jsonschema.exceptions import best_match

>>> schema = {
...     "type": "array",
...     "minItems": 3,
... }
>>> print(best_match(Draft202012Validator(schema).iter_errors(11)).message)
11 is not of type 'array'

jsonschema.exceptions.best_match(_errors_, _key=<function by\_relevance.<locals>.relevance>_)[[source]](https://python-jsonschema.readthedocs.io/en/latest/_modules/jsonschema/exceptions/#best_match)
Try to find an error that appears to be the best match among given errors.

In general, errors that are higher up in the instance (i.e. for which [`ValidationError.path`](https://python-jsonschema.readthedocs.io/en/latest/errors/#jsonschema.exceptions.ValidationError.path "jsonschema.exceptions.ValidationError.path") is shorter) are considered better matches, since they indicate “more” is wrong with the instance.

If the resulting match is either [oneOf](https://json-schema.org/draft/2020-12/json-schema-core.html#section-10.2.1.3) or [anyOf](https://json-schema.org/draft/2020-12/json-schema-core.html#section-10.2.1.2), the _opposite_ assumption is made – i.e. the deepest error is picked, since these keywords only need to match once, and any other errors may not be relevant.

Parameters:
*   **errors** ([_collections.abc.Iterable_](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterable "(in Python v3.14)")) – the errors to select from. Do not provide a mixture of errors from different validation attempts (i.e. from different instances or schemas), since it won’t produce sensical output.

*   **key** ([_collections.abc.Callable_](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.14)")) – the key to use when sorting errors. See [`relevance`](https://python-jsonschema.readthedocs.io/en/latest/api/jsonschema/exceptions/#jsonschema.exceptions.relevance "jsonschema.exceptions.relevance") and transitively [`by_relevance`](https://python-jsonschema.readthedocs.io/en/latest/api/jsonschema/exceptions/#jsonschema.exceptions.by_relevance "jsonschema.exceptions.by_relevance") for more details (the default is to sort with the defaults of that function). Changing the default is only useful if you want to change the function that rates errors but still want the error context descent done by this function.

Returns:
the best matching error, or `None` if the iterable was empty

Note

This function is a heuristic. Its return value may change for a given set of inputs from version to version if better heuristics are added.

jsonschema.exceptions.relevance(_validation\_error_)
A key function that sorts errors based on heuristic relevance.

If you want to sort a bunch of errors entirely, you can use this function to do so. Using this function as a key to e.g. [`sorted`](https://docs.python.org/3/library/functions.html#sorted "(in Python v3.14)") or [`max`](https://docs.python.org/3/library/functions.html#max "(in Python v3.14)") will cause more relevant errors to be considered greater than less relevant ones.

Within the different validation keywords that can fail, this function considers [anyOf](https://json-schema.org/draft/2020-12/json-schema-core.html#section-10.2.1.2) and [oneOf](https://json-schema.org/draft/2020-12/json-schema-core.html#section-10.2.1.3) to be _weak_ validation errors, and will sort them lower than other errors at the same level in the instance.

If you want to change the set of weak [or strong] validation keywords you can create a custom version of this function with [`by_relevance`](https://python-jsonschema.readthedocs.io/en/latest/api/jsonschema/exceptions/#jsonschema.exceptions.by_relevance "jsonschema.exceptions.by_relevance") and provide a different set of each.

>>> schema = {
...     "properties": {
...         "name": {"type": "string"},
...         "phones": {
...             "properties": {
...                 "home": {"type": "string"}
...             },
...         },
...     },
... }
>>> instance = {"name": 123, "phones": {"home": [123]}}
>>> errors = Draft202012Validator(schema).iter_errors(instance)
>>> [
...     e.path[-1]
...     for e in sorted(errors, key=exceptions.relevance)
... ]
['home', 'name']

jsonschema.exceptions.by_relevance(_weak=frozenset({'anyOf','oneOf'})_, _strong=frozenset({})_)[[source]](https://python-jsonschema.readthedocs.io/en/latest/_modules/jsonschema/exceptions/#by_relevance)
Create a key function that can be used to sort errors by relevance.

Parameters:
*   **weak** ([_set_](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.14)")) – a collection of validation keywords to consider to be “weak”. If there are two errors at the same level of the instance and one is in the set of weak validation keywords, the other error will take priority. By default, [anyOf](https://json-schema.org/draft/2020-12/json-schema-core.html#section-10.2.1.2) and [oneOf](https://json-schema.org/draft/2020-12/json-schema-core.html#section-10.2.1.3) are considered weak keywords and will be superseded by other same-level validation errors.

*   **strong** ([_set_](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.14)")) – a collection of validation keywords to consider to be “strong”
