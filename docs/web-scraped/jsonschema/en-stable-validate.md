# Source: https://python-jsonschema.readthedocs.io/en/stable/validate/

Title: Schema Validation

URL Source: https://python-jsonschema.readthedocs.io/en/stable/validate/

Markdown Content:
Tip

Most of the documentation for this package assumes you’re familiar with the fundamentals of writing JSON schemas themselves, and focuses on how this library helps you validate with them in Python.

If you aren’t already comfortable with writing schemas and need an introduction which teaches about JSON Schema the specification, you may find [Understanding JSON Schema](https://json-schema.org/understanding-json-schema/) to be a good read!

The Basics[¶](https://python-jsonschema.readthedocs.io/en/stable/validate/#the-basics "Link to this heading")
-------------------------------------------------------------------------------------------------------------

The simplest way to validate an instance under a given schema is to use the [`validate`](https://python-jsonschema.readthedocs.io/en/stable/api/jsonschema/validators/#jsonschema.validators.validate "jsonschema.validators.validate") function.

jsonschema.validate(_instance_, _schema_, _cls=None_, _*args_, _**kwargs_)[[source]](https://python-jsonschema.readthedocs.io/en/stable/_modules/jsonschema/validators/#validate)
Validate an instance under the given schema.

>>> validate([2, 3, 4], {"maxItems": 2})
Traceback (most recent call last):
 ...
ValidationError: [2, 3, 4] is too long

[`validate()`](https://python-jsonschema.readthedocs.io/en/stable/api/jsonschema/validators/#jsonschema.validators.validate "jsonschema.validators.validate") will first verify that the provided schema is itself valid, since not doing so can lead to less obvious error messages and fail in less obvious or consistent ways.

If you know you have a valid schema already, especially if you intend to validate multiple instances with the same schema, you likely would prefer using the [`jsonschema.protocols.Validator.validate`](https://python-jsonschema.readthedocs.io/en/stable/api/jsonschema/protocols/#jsonschema.protocols.Validator.validate "jsonschema.protocols.Validator.validate") method directly on a specific validator (e.g. `Draft202012Validator.validate`).

Parameters:
*   **instance** – The instance to validate

*   **schema** – The schema to validate with

*   **cls** ([_jsonschema.protocols.Validator_](https://python-jsonschema.readthedocs.io/en/stable/api/jsonschema/protocols/#jsonschema.protocols.Validator "jsonschema.protocols.Validator")) – The class that will be used to validate the instance.

If the `cls` argument is not provided, two things will happen in accordance with the specification. First, if the schema has a [$schema](https://json-schema.org/draft/2020-12/json-schema-core.html#section-8.1.1) keyword containing a known meta-schema [[1]](https://python-jsonschema.readthedocs.io/en/stable/validate/#id2) then the proper validator will be used. The specification recommends that all schemas contain [$schema](https://json-schema.org/draft/2020-12/json-schema-core.html#section-8.1.1) properties for this reason. If no [$schema](https://json-schema.org/draft/2020-12/json-schema-core.html#section-8.1.1) property is found, the default validator class is the latest released draft.

Any other provided positional and keyword arguments will be passed on when instantiating the `cls`.

Raises:
*   [**jsonschema.exceptions.ValidationError**](https://python-jsonschema.readthedocs.io/en/stable/api/jsonschema/exceptions/#jsonschema.exceptions.ValidationError "jsonschema.exceptions.ValidationError") – if the instance is invalid

*   [**jsonschema.exceptions.SchemaError**](https://python-jsonschema.readthedocs.io/en/stable/api/jsonschema/exceptions/#jsonschema.exceptions.SchemaError "jsonschema.exceptions.SchemaError") – if the schema itself is invalid

Footnotes

The Validator Protocol[¶](https://python-jsonschema.readthedocs.io/en/stable/validate/#the-validator-protocol "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------

[`jsonschema`](https://python-jsonschema.readthedocs.io/en/stable/api/#module-jsonschema "jsonschema") defines a [`protocol`](https://docs.python.org/3/library/typing.html#typing.Protocol "(in Python v3.14)") that all validator classes adhere to.

_class_ jsonschema.protocols.Validator(_schema:Mapping|[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")_, _resolver:Any=None_, _format\_checker:[jsonschema.FormatChecker](https://python-jsonschema.readthedocs.io/en/stable/api/#jsonschema.FormatChecker "jsonschema.FormatChecker")|[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")=None_, _*_, _registry:[referencing.jsonschema.SchemaRegistry](https://referencing.readthedocs.io/en/stable/api/#referencing.jsonschema.SchemaRegistry "(in referencing v0.37.0)")=Ellipsis_)[[source]](https://python-jsonschema.readthedocs.io/en/stable/_modules/jsonschema/protocols/#Validator)
The protocol to which all validator classes adhere.

Parameters:
*   **schema** – The schema that the validator object will validate with. It is assumed to be valid, and providing an invalid schema can lead to undefined behavior. See [`Validator.check_schema`](https://python-jsonschema.readthedocs.io/en/stable/api/jsonschema/protocols/#jsonschema.protocols.Validator.check_schema "jsonschema.protocols.Validator.check_schema") to validate a schema first.

*   **registry** – a schema registry that will be used for looking up JSON references

*   **resolver** –

a resolver that will be used to resolve [$ref](https://json-schema.org/draft/2020-12/json-schema-core.html#ref) properties (JSON references). If unprovided, one will be created.

*   **format_checker** – if provided, a checker which will be used to assert about [format](https://json-schema.org/draft/2020-12/json-schema-validation.html#name-implementation-requirements) properties present in the schema. If unprovided, _no_ format validation is done, and the presence of format within schemas is strictly informational. Certain formats require additional packages to be installed in order to assert against instances. Ensure you’ve installed [`jsonschema`](https://python-jsonschema.readthedocs.io/en/stable/api/#module-jsonschema "jsonschema") with its [extra (optional) dependencies](https://python-jsonschema.readthedocs.io/en/stable/#extras) when invoking `pip`.

Deprecated since version v4.12.0: Subclassing validator classes now explicitly warns this is not part of their public API.

FORMAT_CHECKER _:ClassVar[[jsonschema.FormatChecker](https://python-jsonschema.readthedocs.io/en/stable/api/#jsonschema.FormatChecker "jsonschema.FormatChecker")]_
A [`jsonschema.FormatChecker`](https://python-jsonschema.readthedocs.io/en/stable/api/#jsonschema.FormatChecker "jsonschema.FormatChecker") that will be used when validating [format](https://json-schema.org/draft/2020-12/json-schema-validation.html#name-implementation-requirements) keywords in JSON schemas.

ID_OF _:[\_typing.id\_of](https://python-jsonschema.readthedocs.io/en/stable/api/#jsonschema.\_typing.id\_of "jsonschema.\_typing.id\_of")_
A function which given a schema returns its ID.

META_SCHEMA _:ClassVar[Mapping]_
An object representing the validator’s meta schema (the schema that describes valid schemas in the given version).

TYPE_CHECKER _:ClassVar[[jsonschema.TypeChecker](https://python-jsonschema.readthedocs.io/en/stable/api/#jsonschema.TypeChecker "jsonschema.TypeChecker")]_
A [`jsonschema.TypeChecker`](https://python-jsonschema.readthedocs.io/en/stable/api/#jsonschema.TypeChecker "jsonschema.TypeChecker") that will be used when validating [type](https://json-schema.org/draft/2020-12/json-schema-validation.html#section-6.1.1) keywords in JSON schemas.

VALIDATORS _:ClassVar[Mapping]_
A mapping of validation keywords ([`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")s) to functions that validate the keyword with that name. For more information see [Creating or Extending Validator Classes](https://python-jsonschema.readthedocs.io/en/stable/creating/#creating-validators).

_classmethod_ check_schema(_schema:Mapping|[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://python-jsonschema.readthedocs.io/en/stable/_modules/jsonschema/protocols/#Validator.check_schema)
Validate the given schema against the validator’s [`META_SCHEMA`](https://python-jsonschema.readthedocs.io/en/stable/api/jsonschema/protocols/#jsonschema.protocols.Validator.META_SCHEMA "jsonschema.protocols.Validator.META_SCHEMA").

Raises:
[**jsonschema.exceptions.SchemaError**](https://python-jsonschema.readthedocs.io/en/stable/api/jsonschema/exceptions/#jsonschema.exceptions.SchemaError "jsonschema.exceptions.SchemaError") – if the schema is invalid

evolve(_**kwargs_)→[Validator](https://python-jsonschema.readthedocs.io/en/stable/api/jsonschema/protocols/#jsonschema.protocols.Validator "jsonschema.protocols.Validator")[[source]](https://python-jsonschema.readthedocs.io/en/stable/_modules/jsonschema/protocols/#Validator.evolve)
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

is_type(_instance:[Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")_, _type:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://python-jsonschema.readthedocs.io/en/stable/_modules/jsonschema/protocols/#Validator.is_type)
Check if the instance is of the given (JSON Schema) type.

Parameters:
*   **instance** – the value to check

*   **type** – the name of a known (JSON Schema) type

Returns:
whether the instance is of the given type

Raises:
[**jsonschema.exceptions.UnknownType**](https://python-jsonschema.readthedocs.io/en/stable/api/jsonschema/exceptions/#jsonschema.exceptions.UnknownType "jsonschema.exceptions.UnknownType") – if `type` is not a known type

is_valid(_instance:[Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://python-jsonschema.readthedocs.io/en/stable/_modules/jsonschema/protocols/#Validator.is_valid)
Check if the instance is valid under the current [`schema`](https://python-jsonschema.readthedocs.io/en/stable/api/jsonschema/protocols/#jsonschema.protocols.Validator.schema "jsonschema.protocols.Validator.schema").

Returns:
whether the instance is valid or not

>>> schema = {"maxItems" : 2}
>>> Draft202012Validator(schema).is_valid([2, 3, 4])
False

iter_errors(_instance:Any_)→Iterable[[ValidationError](https://python-jsonschema.readthedocs.io/en/stable/api/jsonschema/exceptions/#jsonschema.exceptions.ValidationError "jsonschema.exceptions.ValidationError")][[source]](https://python-jsonschema.readthedocs.io/en/stable/_modules/jsonschema/protocols/#Validator.iter_errors)
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

Deprecated since version v4.0.0: Calling this function with a second schema argument is deprecated. Use [`Validator.evolve`](https://python-jsonschema.readthedocs.io/en/stable/api/jsonschema/protocols/#jsonschema.protocols.Validator.evolve "jsonschema.protocols.Validator.evolve") instead.

schema _:Mapping|[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")_
The schema that will be used to validate instances

validate(_instance:[Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://python-jsonschema.readthedocs.io/en/stable/_modules/jsonschema/protocols/#Validator.validate)
Check if the instance is valid under the current [`schema`](https://python-jsonschema.readthedocs.io/en/stable/api/jsonschema/protocols/#jsonschema.protocols.Validator.schema "jsonschema.protocols.Validator.schema").

Raises:
[**jsonschema.exceptions.ValidationError**](https://python-jsonschema.readthedocs.io/en/stable/api/jsonschema/exceptions/#jsonschema.exceptions.ValidationError "jsonschema.exceptions.ValidationError") – if the instance is invalid

>>> schema = {"maxItems" : 2}
>>> Draft202012Validator(schema).validate([2, 3, 4])
Traceback (most recent call last):
 ...
ValidationError: [2, 3, 4] is too long

All of the [versioned validators](https://python-jsonschema.readthedocs.io/en/stable/validate/#versioned-validators) that are included with [`jsonschema`](https://python-jsonschema.readthedocs.io/en/stable/api/#module-jsonschema "jsonschema") adhere to the protocol, and any [`extensions of these validators`](https://python-jsonschema.readthedocs.io/en/stable/api/jsonschema/validators/#jsonschema.validators.extend "jsonschema.validators.extend") will as well. For more information on [`creating`](https://python-jsonschema.readthedocs.io/en/stable/api/jsonschema/validators/#jsonschema.validators.create "jsonschema.validators.create") or [`extending`](https://python-jsonschema.readthedocs.io/en/stable/api/jsonschema/validators/#jsonschema.validators.extend "jsonschema.validators.extend") validators see [Creating or Extending Validator Classes](https://python-jsonschema.readthedocs.io/en/stable/creating/#creating-validators).

Type Checking[¶](https://python-jsonschema.readthedocs.io/en/stable/validate/#type-checking "Link to this heading")
-------------------------------------------------------------------------------------------------------------------

To handle JSON Schema’s [type](https://json-schema.org/draft/2020-12/json-schema-validation.html#section-6.1.1) keyword, a [`Validator`](https://python-jsonschema.readthedocs.io/en/stable/api/jsonschema/protocols/#jsonschema.protocols.Validator "jsonschema.protocols.Validator") uses an associated [`TypeChecker`](https://python-jsonschema.readthedocs.io/en/stable/api/#jsonschema.TypeChecker "jsonschema.TypeChecker"). The type checker provides an immutable mapping between names of types and functions that can test if an instance is of that type. The defaults are suitable for most users - each of the [versioned validators](https://python-jsonschema.readthedocs.io/en/stable/validate/#versioned-validators) that are included with [`jsonschema`](https://python-jsonschema.readthedocs.io/en/stable/api/#module-jsonschema "jsonschema") have a [`TypeChecker`](https://python-jsonschema.readthedocs.io/en/stable/api/#jsonschema.TypeChecker "jsonschema.TypeChecker") that can correctly handle their respective versions.

See also

[Validating With Additional Types](https://python-jsonschema.readthedocs.io/en/stable/validate/#validating-types)

For an example of providing a custom type check.

_class_ jsonschema.TypeChecker(_type\_checkers:Mapping[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"),Callable[[[TypeChecker](https://python-jsonschema.readthedocs.io/en/stable/api/#jsonschema.TypeChecker "jsonschema.TypeChecker"),Any],[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")]]=HashTrieMap({})_)[[source]](https://python-jsonschema.readthedocs.io/en/stable/_modules/jsonschema/_types/#TypeChecker)
A [type](https://json-schema.org/draft/2020-12/json-schema-validation.html#section-6.1.1) property checker.

A [`TypeChecker`](https://python-jsonschema.readthedocs.io/en/stable/api/#jsonschema.TypeChecker "jsonschema.TypeChecker") performs type checking for a [`Validator`](https://python-jsonschema.readthedocs.io/en/stable/api/jsonschema/protocols/#jsonschema.protocols.Validator "jsonschema.protocols.Validator"), converting between the defined JSON Schema types and some associated Python types or objects.

Modifying the behavior just mentioned by redefining which Python objects are considered to be of which JSON Schema types can be done using [`TypeChecker.redefine`](https://python-jsonschema.readthedocs.io/en/stable/api/#jsonschema.TypeChecker.redefine "jsonschema.TypeChecker.redefine") or [`TypeChecker.redefine_many`](https://python-jsonschema.readthedocs.io/en/stable/api/#jsonschema.TypeChecker.redefine_many "jsonschema.TypeChecker.redefine_many"), and types can be removed via [`TypeChecker.remove`](https://python-jsonschema.readthedocs.io/en/stable/api/#jsonschema.TypeChecker.remove "jsonschema.TypeChecker.remove"). Each of these return a new [`TypeChecker`](https://python-jsonschema.readthedocs.io/en/stable/api/#jsonschema.TypeChecker "jsonschema.TypeChecker").

Parameters:
**type_checkers** – The initial mapping of types to their checking functions.

is_type(_instance_, _type:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://python-jsonschema.readthedocs.io/en/stable/_modules/jsonschema/_types/#TypeChecker.is_type)
Check if the instance is of the appropriate type.

Parameters:
*   **instance** – The instance to check

*   **type** – The name of the type that is expected.

Raises:
[**jsonschema.exceptions.UndefinedTypeCheck**](https://python-jsonschema.readthedocs.io/en/stable/api/jsonschema/exceptions/#jsonschema.exceptions.UndefinedTypeCheck "jsonschema.exceptions.UndefinedTypeCheck") – if `type` is unknown to this object.

redefine(_type:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")_, _fn_)→[TypeChecker](https://python-jsonschema.readthedocs.io/en/stable/api/#jsonschema.TypeChecker "jsonschema._types.TypeChecker")[[source]](https://python-jsonschema.readthedocs.io/en/stable/_modules/jsonschema/_types/#TypeChecker.redefine)
Produce a new checker with the given type redefined.

Parameters:
*   **type** – The name of the type to check.

*   **fn** ([_collections.abc.Callable_](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.14)")) – A callable taking exactly two parameters - the type checker calling the function and the instance to check. The function should return true if instance is of this type and false otherwise.

redefine_many(_definitions=()_)→[TypeChecker](https://python-jsonschema.readthedocs.io/en/stable/api/#jsonschema.TypeChecker "jsonschema._types.TypeChecker")[[source]](https://python-jsonschema.readthedocs.io/en/stable/_modules/jsonschema/_types/#TypeChecker.redefine_many)
Produce a new checker with the given types redefined.

Parameters:
**definitions** ([_dict_](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")) – A dictionary mapping types to their checking functions.

remove(_*types_)→[TypeChecker](https://python-jsonschema.readthedocs.io/en/stable/api/#jsonschema.TypeChecker "jsonschema._types.TypeChecker")[[source]](https://python-jsonschema.readthedocs.io/en/stable/_modules/jsonschema/_types/#TypeChecker.remove)
Produce a new checker with the given types forgotten.

Parameters:
**types** – the names of the types to remove.

Raises:
[**jsonschema.exceptions.UndefinedTypeCheck**](https://python-jsonschema.readthedocs.io/en/stable/api/jsonschema/exceptions/#jsonschema.exceptions.UndefinedTypeCheck "jsonschema.exceptions.UndefinedTypeCheck") – if any given type is unknown to this object

_exception_ jsonschema.exceptions.UndefinedTypeCheck(_type:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")_)[[source]](https://python-jsonschema.readthedocs.io/en/stable/_modules/jsonschema/exceptions/#UndefinedTypeCheck)
A type checker was asked to check a type it did not have registered.

Raised when trying to remove a type check that is not known to this TypeChecker, or when calling [`jsonschema.TypeChecker.is_type`](https://python-jsonschema.readthedocs.io/en/stable/api/#jsonschema.TypeChecker.is_type "jsonschema.TypeChecker.is_type") directly.

### Validating With Additional Types[¶](https://python-jsonschema.readthedocs.io/en/stable/validate/#validating-with-additional-types "Link to this heading")

Occasionally it can be useful to provide additional or alternate types when validating JSON Schema’s [type](https://json-schema.org/draft/2020-12/json-schema-validation.html#section-6.1.1) keyword.

[`jsonschema`](https://python-jsonschema.readthedocs.io/en/stable/api/#module-jsonschema "jsonschema") tries to strike a balance between performance in the common case and generality. For instance, JSON Schema defines a `number` type, which can be validated with a schema such as `{"type" : "number"}`. By default, this will accept instances of Python [`numbers.Number`](https://docs.python.org/3/library/numbers.html#numbers.Number "(in Python v3.14)"). This includes in particular [`int`](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")s and [`float`](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")s, along with [`decimal.Decimal`](https://docs.python.org/3/library/decimal.html#decimal.Decimal "(in Python v3.14)") objects, [`complex`](https://docs.python.org/3/library/functions.html#complex "(in Python v3.14)") numbers etc. For `integer` and `object`, however, rather than checking for [`numbers.Integral`](https://docs.python.org/3/library/numbers.html#numbers.Integral "(in Python v3.14)") and [`collections.abc.Mapping`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Mapping "(in Python v3.14)"), [`jsonschema`](https://python-jsonschema.readthedocs.io/en/stable/api/#module-jsonschema "jsonschema") simply checks for [`int`](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") and [`dict`](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)"), since the more general instance checks can introduce significant slowdown, especially given how common validating these types are.

If you _do_ want the generality, or just want to add a few specific additional types as being acceptable for a validator object, then you should update an existing [`jsonschema.TypeChecker`](https://python-jsonschema.readthedocs.io/en/stable/api/#jsonschema.TypeChecker "jsonschema.TypeChecker") or create a new one. You may then create a new [`Validator`](https://python-jsonschema.readthedocs.io/en/stable/api/jsonschema/protocols/#jsonschema.protocols.Validator "jsonschema.protocols.Validator") via [`jsonschema.validators.extend`](https://python-jsonschema.readthedocs.io/en/stable/api/jsonschema/validators/#jsonschema.validators.extend "jsonschema.validators.extend").

from jsonschema import validators

class MyInteger:
    pass

def is_my_int(checker, instance):
    return (
        Draft202012Validator.TYPE_CHECKER.is_type(instance, "number") or
        isinstance(instance, MyInteger)
    )

type_checker = Draft202012Validator.TYPE_CHECKER.redefine(
    "number", is_my_int,
)

CustomValidator = validators.extend(
    Draft202012Validator,
    type_checker=type_checker,
)
validator = CustomValidator(schema={"type" : "number"})

_exception_ jsonschema.exceptions.UnknownType(_type_, _instance_, _schema_)[[source]](https://python-jsonschema.readthedocs.io/en/stable/_modules/jsonschema/exceptions/#UnknownType)
A validator was asked to validate an instance against an unknown type.

Versioned Validators[¶](https://python-jsonschema.readthedocs.io/en/stable/validate/#versioned-validators "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------

[`jsonschema`](https://python-jsonschema.readthedocs.io/en/stable/api/#module-jsonschema "jsonschema") ships with validator classes for various versions of the JSON Schema specification. For details on the methods and attributes that each validator class provides see the [`Validator`](https://python-jsonschema.readthedocs.io/en/stable/api/jsonschema/protocols/#jsonschema.protocols.Validator "jsonschema.protocols.Validator") protocol, which each included validator class implements.

Each of the below cover a specific release of the JSON Schema specification.

_class_ jsonschema.Draft202012Validator(_schema:bool|~collections.abc.Mapping[str,~typing.Any],resolver=None,format\_checker:~jsonschema.\_format.FormatChecker|None=None,*,registry:~referencing.\_core.Registry[bool|~collections.abc.Mapping[str,~typing.Any]]=<Registry(20 resources)>,\_resolver=None_)_class_ jsonschema.Draft201909Validator(_schema:bool|~collections.abc.Mapping[str,~typing.Any],resolver=None,format\_checker:~jsonschema.\_format.FormatChecker|None=None,*,registry:~referencing.\_core.Registry[bool|~collections.abc.Mapping[str,~typing.Any]]=<Registry(20 resources)>,\_resolver=None_)_class_ jsonschema.Draft7Validator(_schema:bool|~collections.abc.Mapping[str,~typing.Any],resolver=None,format\_checker:~jsonschema.\_format.FormatChecker|None=None,*,registry:~referencing.\_core.Registry[bool|~collections.abc.Mapping[str,~typing.Any]]=<Registry(20 resources)>,\_resolver=None_)_class_ jsonschema.Draft6Validator(_schema:bool|~collections.abc.Mapping[str,~typing.Any],resolver=None,format\_checker:~jsonschema.\_format.FormatChecker|None=None,*,registry:~referencing.\_core.Registry[bool|~collections.abc.Mapping[str,~typing.Any]]=<Registry(20 resources)>,\_resolver=None_)_class_ jsonschema.Draft4Validator(_schema:bool|~collections.abc.Mapping[str,~typing.Any],resolver=None,format\_checker:~jsonschema.\_format.FormatChecker|None=None,*,registry:~referencing.\_core.Registry[bool|~collections.abc.Mapping[str,~typing.Any]]=<Registry(20 resources)>,\_resolver=None_)_class_ jsonschema.Draft3Validator(_schema:bool|~collections.abc.Mapping[str,~typing.Any],resolver=None,format\_checker:~jsonschema.\_format.FormatChecker|None=None,*,registry:~referencing.\_core.Registry[bool|~collections.abc.Mapping[str,~typing.Any]]=<Registry(20 resources)>,\_resolver=None_)
For example, if you wanted to validate a schema you created against the Draft 2020-12 meta-schema, you could use:

from jsonschema import Draft202012Validator

schema = {
    "$schema": Draft202012Validator.META_SCHEMA["$id"],

    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "email": {"type": "string"},
    },
    "required": ["email"]
}
Draft202012Validator.check_schema(schema)

Validating Formats[¶](https://python-jsonschema.readthedocs.io/en/stable/validate/#validating-formats "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------

JSON Schema defines the [format](https://json-schema.org/draft/2020-12/json-schema-validation.html#name-implementation-requirements) keyword which can be used to check if primitive types (`string`s, `number`s, `boolean`s) conform to well-defined formats. By default, as per the specification, no validation is enforced. Optionally however, validation can be enabled by hooking a [`format-checking object`](https://python-jsonschema.readthedocs.io/en/stable/api/#jsonschema.FormatChecker "jsonschema.FormatChecker") into a [`Validator`](https://python-jsonschema.readthedocs.io/en/stable/api/jsonschema/protocols/#jsonschema.protocols.Validator "jsonschema.protocols.Validator").

>>> validate("127.0.0.1", {"format" : "ipv4"})
>>> validate(
...     instance="-12",
...     schema={"format" : "ipv4"},
...     format_checker=Draft202012Validator.FORMAT_CHECKER,
... )
Traceback (most recent call last):
 ...
ValidationError: "-12" is not a "ipv4"

Some formats require additional dependencies to be installed.

The easiest way to ensure you have what is needed is to install `jsonschema` using the `format` or `format-nongpl` extras.

For example:

$ pip install jsonschema[format]

Or if you want to avoid GPL dependencies, a second extra is available:

$ pip install jsonschema[format-nongpl]

Warning

It is your own responsibility ultimately to ensure you are license-compliant, so you should be double checking your own dependencies if you rely on this extra.

The more specific list of formats along with any additional dependencies they have is shown below.

Warning

If a dependency is not installed when using a checker that requires it, validation will succeed without throwing an error, as also specified by the specification.

| Checker | Notes |
| --- | --- |
| `color` | requires [webcolors](https://pypi.org/pypi/webcolors/) |
| `date` |  |
| `date-time` | requires [rfc3339-validator](https://pypi.org/project/rfc3339-validator/) |
| `duration` | requires [isoduration](https://pypi.org/pypi/isoduration/) |
| `email` |  |
| `hostname` | requires [fqdn](https://pypi.org/pypi/fqdn/) |
| `idn-hostname` | requires [idna](https://pypi.org/pypi/idna/) |
| `ipv4` |  |
| `ipv6` | OS must have [`socket.inet_pton`](https://docs.python.org/3/library/socket.html#socket.inet_pton "(in Python v3.14)") function |
| `iri` | requires [rfc3987](https://pypi.org/pypi/rfc3987/) or [rfc3987-syntax](https://pypi.org/pypi/rfc3987-syntax/) |
| `iri-reference` | requires [rfc3987](https://pypi.org/pypi/rfc3987/) or [rfc3987-syntax](https://pypi.org/pypi/rfc3987-syntax/) |
| `json-pointer` | requires [jsonpointer](https://pypi.org/pypi/jsonpointer/) |
| `regex` |  |
| `relative-json-pointer` | requires [jsonpointer](https://pypi.org/pypi/jsonpointer/) |
| `time` | requires [rfc3339-validator](https://pypi.org/project/rfc3339-validator/) |
| `uri` | requires [rfc3987](https://pypi.org/pypi/rfc3987/) or [rfc3986-validator](https://pypi.org/project/rfc3986-validator/) |
| `uri-reference` | requires [rfc3987](https://pypi.org/pypi/rfc3987/) or [rfc3986-validator](https://pypi.org/project/rfc3986-validator/) |
| `uri-template` | requires [uri-template](https://pypi.org/pypi/uri-template/) |
| `uuid` |  |

The supported mechanism for ensuring these dependencies are present is again as shown above, not by directly installing the packages.

_class_ jsonschema.FormatChecker(_formats:[Iterable](https://docs.python.org/3/library/typing.html#typing.Iterable "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]|[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")=None_)[[source]](https://python-jsonschema.readthedocs.io/en/stable/_modules/jsonschema/_format/#FormatChecker)
A `format` property checker.

JSON Schema does not mandate that the `format` property actually do any validation. If validation is desired however, instances of this class can be hooked into validators to enable format validation.

[`FormatChecker`](https://python-jsonschema.readthedocs.io/en/stable/api/#jsonschema.FormatChecker "jsonschema.FormatChecker") objects always return `True` when asked about formats that they do not know how to validate.

To add a check for a custom format use the [`FormatChecker.checks`](https://python-jsonschema.readthedocs.io/en/stable/api/#jsonschema.FormatChecker.checks "jsonschema.FormatChecker.checks") decorator.

Parameters:
**formats** – The known formats to validate. This argument can be used to limit which formats will be used during validation.

checkers[¶](https://python-jsonschema.readthedocs.io/en/stable/validate/#jsonschema.FormatChecker.checkers "Link to this definition")
A mapping of currently known formats to tuple of functions that validate them and errors that should be caught. New checkers can be added and removed either per-instance or globally for all checkers using the [`FormatChecker.checks`](https://python-jsonschema.readthedocs.io/en/stable/api/#jsonschema.FormatChecker.checks "jsonschema.FormatChecker.checks") decorator.

_classmethod_ cls_checks(_format_, _raises=()_)[[source]](https://python-jsonschema.readthedocs.io/en/stable/_modules/jsonschema/_format/#FormatChecker.cls_checks)[¶](https://python-jsonschema.readthedocs.io/en/stable/validate/#jsonschema.FormatChecker.cls_checks "Link to this definition")
Register a decorated function as _globally_ validating a new format.

Any instance created after this function is called will pick up the supplied checker.

Parameters:
*   **format** ([_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) – the format that the decorated function will check

*   **raises** ([_Exception_](https://docs.python.org/3/library/exceptions.html#Exception "(in Python v3.14)")) – the exception(s) raised by the decorated function when an invalid instance is found. The exception object will be accessible as the [`jsonschema.exceptions.ValidationError.cause`](https://python-jsonschema.readthedocs.io/en/stable/errors/#jsonschema.exceptions.ValidationError.cause "jsonschema.exceptions.ValidationError.cause") attribute of the resulting validation error.

Deprecated since version v4.14.0: Use [`FormatChecker.checks`](https://python-jsonschema.readthedocs.io/en/stable/api/#jsonschema.FormatChecker.checks "jsonschema.FormatChecker.checks") on an instance instead.

check(_instance:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")_, _format:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://python-jsonschema.readthedocs.io/en/stable/_modules/jsonschema/_format/#FormatChecker.check)
Check whether the instance conforms to the given format.

Parameters:
*   **instance** (_any primitive type_, i.e. str, number, bool) – The instance to check

*   **format** – The format that instance should conform to

Raises:
[**FormatError**](https://python-jsonschema.readthedocs.io/en/stable/api/jsonschema/exceptions/#jsonschema.exceptions.FormatError "jsonschema.exceptions.FormatError") – if the instance does not conform to `format`

checks(_format:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")_, _raises:[type](https://docs.python.org/3/library/functions.html#type "(in Python v3.14)")[[Exception](https://docs.python.org/3/library/exceptions.html#Exception "(in Python v3.14)")]|[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[type](https://docs.python.org/3/library/functions.html#type "(in Python v3.14)")[[Exception](https://docs.python.org/3/library/exceptions.html#Exception "(in Python v3.14)")],...]=()_)→[Callable](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")[[[_F](https://python-jsonschema.readthedocs.io/en/stable/api/#jsonschema._format._F "jsonschema._format._F")],[_F](https://python-jsonschema.readthedocs.io/en/stable/api/#jsonschema._format._F "jsonschema._format._F")][[source]](https://python-jsonschema.readthedocs.io/en/stable/_modules/jsonschema/_format/#FormatChecker.checks)
Register a decorated function as validating a new format.

Parameters:
*   **format** – The format that the decorated function will check.

*   **raises** –

The exception(s) raised by the decorated function when an invalid instance is found.

The exception object will be accessible as the [`jsonschema.exceptions.ValidationError.cause`](https://python-jsonschema.readthedocs.io/en/stable/errors/#jsonschema.exceptions.ValidationError.cause "jsonschema.exceptions.ValidationError.cause") attribute of the resulting validation error.

conforms(_instance:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")_, _format:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://python-jsonschema.readthedocs.io/en/stable/_modules/jsonschema/_format/#FormatChecker.conforms)
Check whether the instance conforms to the given format.

Parameters:
*   **instance** (_any primitive type_, i.e. str, number, bool) – The instance to check

*   **format** – The format that instance should conform to

Returns:
whether it conformed

Return type:
[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

_exception_ jsonschema.exceptions.FormatError(_message_, _cause=None_)[[source]](https://python-jsonschema.readthedocs.io/en/stable/_modules/jsonschema/exceptions/#FormatError)
Validating a format failed.

### Format-Specific Notes[¶](https://python-jsonschema.readthedocs.io/en/stable/validate/#format-specific-notes "Link to this heading")

#### regex[¶](https://python-jsonschema.readthedocs.io/en/stable/validate/#regex "Link to this heading")

The JSON Schema specification [recommends (but does not require)](https://json-schema.org/draft/2020-12/json-schema-core.html#name-regular-expressions) that implementations use ECMA 262 regular expressions.

Given that there is no current library in Python capable of supporting the ECMA 262 dialect, the `regex` format will instead validate _Python_ regular expressions, which are the ones used by this implementation for other keywords like [pattern](https://json-schema.org/draft/2020-12/json-schema-validation.html#section-6.3.3) or [patternProperties](https://json-schema.org/draft/2020-12/json-schema-core.html#section-10.3.2.2).

#### email[¶](https://python-jsonschema.readthedocs.io/en/stable/validate/#email "Link to this heading")

Since in most cases “validating” an email address is an attempt instead to confirm that mail sent to it will deliver to a recipient, and that that recipient is the correct one the email is intended for, and since many valid email addresses are in many places incorrectly rejected, and many invalid email addresses are in many places incorrectly accepted, the `email` format keyword only provides a sanity check, not full [**RFC 5322**](https://datatracker.ietf.org/doc/html/rfc5322.html) validation.

The same applies to the `idn-email` format.

If you indeed want a particular well-specified set of emails to be considered valid, you can use [`FormatChecker.checks`](https://python-jsonschema.readthedocs.io/en/stable/api/#jsonschema.FormatChecker.checks "jsonschema.FormatChecker.checks") to provide your specific definition.
