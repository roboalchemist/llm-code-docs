# Source: https://python-jsonschema.readthedocs.io/en/latest/api/jsonschema/protocols/

Title: jsonschema.protocols

URL Source: https://python-jsonschema.readthedocs.io/en/latest/api/jsonschema/protocols/

Markdown Content:
typing.Protocol classes for jsonschema interfaces.

_class_ jsonschema.protocols.Validator(_schema:Mapping|[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")_, _resolver:Any=None_, _format\_checker:[jsonschema.FormatChecker](https://python-jsonschema.readthedocs.io/en/latest/api/#jsonschema.FormatChecker "jsonschema.FormatChecker")|[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")=None_, _*_, _registry:[referencing.jsonschema.SchemaRegistry](https://referencing.readthedocs.io/en/stable/api/#referencing.jsonschema.SchemaRegistry "(in referencing v0.37.0)")=Ellipsis_)[[source]](https://python-jsonschema.readthedocs.io/en/latest/_modules/jsonschema/protocols/#Validator)[¶](https://python-jsonschema.readthedocs.io/en/latest/api/jsonschema/protocols/#jsonschema.protocols.Validator "Link to this definition")
The protocol to which all validator classes adhere.

Parameters:
*   **schema** – The schema that the validator object will validate with. It is assumed to be valid, and providing an invalid schema can lead to undefined behavior. See [`Validator.check_schema`](https://python-jsonschema.readthedocs.io/en/latest/api/jsonschema/protocols/#jsonschema.protocols.Validator.check_schema "jsonschema.protocols.Validator.check_schema") to validate a schema first.

*   **registry** – a schema registry that will be used for looking up JSON references

*   **resolver** –

a resolver that will be used to resolve [$ref](https://json-schema.org/draft/2020-12/json-schema-core.html#ref) properties (JSON references). If unprovided, one will be created.

Deprecated since version v4.18.0: [`RefResolver`](https://python-jsonschema.readthedocs.io/en/latest/api/jsonschema/validators/#jsonschema.validators._RefResolver "jsonschema.validators._RefResolver") has been deprecated in favor of [`referencing`](https://referencing.readthedocs.io/en/stable/api/#module-referencing "(in referencing v0.37.0)"), and with it, this argument.

*   **format_checker** – if provided, a checker which will be used to assert about [format](https://json-schema.org/draft/2020-12/json-schema-validation.html#name-implementation-requirements) properties present in the schema. If unprovided, _no_ format validation is done, and the presence of format within schemas is strictly informational. Certain formats require additional packages to be installed in order to assert against instances. Ensure you’ve installed [`jsonschema`](https://python-jsonschema.readthedocs.io/en/latest/api/#module-jsonschema "jsonschema") with its [extra (optional) dependencies](https://python-jsonschema.readthedocs.io/en/latest/#extras) when invoking `pip`.

Deprecated since version v4.12.0: Subclassing validator classes now explicitly warns this is not part of their public API.

FORMAT_CHECKER _:ClassVar[[jsonschema.FormatChecker](https://python-jsonschema.readthedocs.io/en/latest/api/#jsonschema.FormatChecker "jsonschema.FormatChecker")]_[¶](https://python-jsonschema.readthedocs.io/en/latest/api/jsonschema/protocols/#jsonschema.protocols.Validator.FORMAT_CHECKER "Link to this definition")
A [`jsonschema.FormatChecker`](https://python-jsonschema.readthedocs.io/en/latest/api/#jsonschema.FormatChecker "jsonschema.FormatChecker") that will be used when validating [format](https://json-schema.org/draft/2020-12/json-schema-validation.html#name-implementation-requirements) keywords in JSON schemas.

ID_OF _:[\_typing.id\_of](https://python-jsonschema.readthedocs.io/en/latest/api/#jsonschema.\_typing.id\_of "jsonschema.\_typing.id\_of")_[¶](https://python-jsonschema.readthedocs.io/en/latest/api/jsonschema/protocols/#jsonschema.protocols.Validator.ID_OF "Link to this definition")
A function which given a schema returns its ID.

META_SCHEMA _:ClassVar[Mapping]_[¶](https://python-jsonschema.readthedocs.io/en/latest/api/jsonschema/protocols/#jsonschema.protocols.Validator.META_SCHEMA "Link to this definition")
An object representing the validator’s meta schema (the schema that describes valid schemas in the given version).

TYPE_CHECKER _:ClassVar[[jsonschema.TypeChecker](https://python-jsonschema.readthedocs.io/en/latest/api/#jsonschema.TypeChecker "jsonschema.TypeChecker")]_[¶](https://python-jsonschema.readthedocs.io/en/latest/api/jsonschema/protocols/#jsonschema.protocols.Validator.TYPE_CHECKER "Link to this definition")
A [`jsonschema.TypeChecker`](https://python-jsonschema.readthedocs.io/en/latest/api/#jsonschema.TypeChecker "jsonschema.TypeChecker") that will be used when validating [type](https://json-schema.org/draft/2020-12/json-schema-validation.html#section-6.1.1) keywords in JSON schemas.

VALIDATORS _:ClassVar[Mapping]_[¶](https://python-jsonschema.readthedocs.io/en/latest/api/jsonschema/protocols/#jsonschema.protocols.Validator.VALIDATORS "Link to this definition")
A mapping of validation keywords ([`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")s) to functions that validate the keyword with that name. For more information see [Creating or Extending Validator Classes](https://python-jsonschema.readthedocs.io/en/latest/creating/#creating-validators).

_classmethod_ check_schema(_schema:Mapping|[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://python-jsonschema.readthedocs.io/en/latest/_modules/jsonschema/protocols/#Validator.check_schema)[¶](https://python-jsonschema.readthedocs.io/en/latest/api/jsonschema/protocols/#jsonschema.protocols.Validator.check_schema "Link to this definition")
Validate the given schema against the validator’s [`META_SCHEMA`](https://python-jsonschema.readthedocs.io/en/latest/api/jsonschema/protocols/#jsonschema.protocols.Validator.META_SCHEMA "jsonschema.protocols.Validator.META_SCHEMA").

Raises:
[**jsonschema.exceptions.SchemaError**](https://python-jsonschema.readthedocs.io/en/latest/api/jsonschema/exceptions/#jsonschema.exceptions.SchemaError "jsonschema.exceptions.SchemaError") – if the schema is invalid

evolve(_**kwargs_)→[Validator](https://python-jsonschema.readthedocs.io/en/latest/api/jsonschema/protocols/#jsonschema.protocols.Validator "jsonschema.protocols.Validator")[[source]](https://python-jsonschema.readthedocs.io/en/latest/_modules/jsonschema/protocols/#Validator.evolve)[¶](https://python-jsonschema.readthedocs.io/en/latest/api/jsonschema/protocols/#jsonschema.protocols.Validator.evolve "Link to this definition")
Create a new validator like this one, but with given changes.

Preserves all other attributes, so can be used to e.g. create a validator with a different schema but with the same [$ref](https://json-schema.org/draft/2020-12/json-schema-core.html#ref) resolution behavior.

>>> validator = Draft202012Validator({})
>>> validator.evolve(schema={"type": "number"})
Draft202012Validator(schema={'type': 'number'}, format_checker=None)

The returned object satisfies the validator protocol, but may not be of the same concrete class! In particular this occurs when a [$ref](https://json-schema.org/draft/2020-12/json-schema-core.html#ref) occurs to a schema with a different [$schema](https://json-schema.org/draft/2020-12/json-schema-core.html#section-8.1.1) than this one (i.e. for a different draft).

>>> validator.evolve(
...     schema={"$schema": Draft7Validator.META_SCHEMA["$id"]}
... )
Draft7Validator(schema=..., format_checker=None)

is_type(_instance:[Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")_, _type:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://python-jsonschema.readthedocs.io/en/latest/_modules/jsonschema/protocols/#Validator.is_type)[¶](https://python-jsonschema.readthedocs.io/en/latest/api/jsonschema/protocols/#jsonschema.protocols.Validator.is_type "Link to this definition")
Check if the instance is of the given (JSON Schema) type.

Parameters:
*   **instance** – the value to check

*   **type** – the name of a known (JSON Schema) type

Returns:
whether the instance is of the given type

Raises:
[**jsonschema.exceptions.UnknownType**](https://python-jsonschema.readthedocs.io/en/latest/api/jsonschema/exceptions/#jsonschema.exceptions.UnknownType "jsonschema.exceptions.UnknownType") – if `type` is not a known type

is_valid(_instance:[Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://python-jsonschema.readthedocs.io/en/latest/_modules/jsonschema/protocols/#Validator.is_valid)[¶](https://python-jsonschema.readthedocs.io/en/latest/api/jsonschema/protocols/#jsonschema.protocols.Validator.is_valid "Link to this definition")
Check if the instance is valid under the current [`schema`](https://python-jsonschema.readthedocs.io/en/latest/api/jsonschema/protocols/#jsonschema.protocols.Validator.schema "jsonschema.protocols.Validator.schema").

Returns:
whether the instance is valid or not

>>> schema = {"maxItems" : 2}
>>> Draft202012Validator(schema).is_valid([2, 3, 4])
False

iter_errors(_instance:Any_)→Iterable[[ValidationError](https://python-jsonschema.readthedocs.io/en/latest/api/jsonschema/exceptions/#jsonschema.exceptions.ValidationError "jsonschema.exceptions.ValidationError")][[source]](https://python-jsonschema.readthedocs.io/en/latest/_modules/jsonschema/protocols/#Validator.iter_errors)[¶](https://python-jsonschema.readthedocs.io/en/latest/api/jsonschema/protocols/#jsonschema.protocols.Validator.iter_errors "Link to this definition")
Lazily yield each of the validation errors in the given instance.

>>> schema = {
...     "type" : "array",
...     "items" : {"enum" : [1, 2, 3]},
...     "maxItems" : 2,
... }
>>> v = Draft202012Validator(schema)
>>> for error in sorted(v.iter_errors([2, 3, 4]), key=str):
...     print(error.message)
4 is not one of [1, 2, 3]
[2, 3, 4] is too long

Deprecated since version v4.0.0: Calling this function with a second schema argument is deprecated. Use [`Validator.evolve`](https://python-jsonschema.readthedocs.io/en/latest/api/jsonschema/protocols/#jsonschema.protocols.Validator.evolve "jsonschema.protocols.Validator.evolve") instead.

schema _:Mapping|[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")_[¶](https://python-jsonschema.readthedocs.io/en/latest/api/jsonschema/protocols/#jsonschema.protocols.Validator.schema "Link to this definition")
The schema that will be used to validate instances

validate(_instance:[Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://python-jsonschema.readthedocs.io/en/latest/_modules/jsonschema/protocols/#Validator.validate)[¶](https://python-jsonschema.readthedocs.io/en/latest/api/jsonschema/protocols/#jsonschema.protocols.Validator.validate "Link to this definition")
Check if the instance is valid under the current [`schema`](https://python-jsonschema.readthedocs.io/en/latest/api/jsonschema/protocols/#jsonschema.protocols.Validator.schema "jsonschema.protocols.Validator.schema").

Raises:
[**jsonschema.exceptions.ValidationError**](https://python-jsonschema.readthedocs.io/en/latest/api/jsonschema/exceptions/#jsonschema.exceptions.ValidationError "jsonschema.exceptions.ValidationError") – if the instance is invalid

>>> schema = {"maxItems" : 2}
>>> Draft202012Validator(schema).validate([2, 3, 4])
Traceback (most recent call last):
 ...
ValidationError: [2, 3, 4] is too long
