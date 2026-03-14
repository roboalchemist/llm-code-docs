# Source: https://python-jsonschema.readthedocs.io/en/stable/api/

Title: API Reference

URL Source: https://python-jsonschema.readthedocs.io/en/stable/api/

Markdown Content:
Submodules[¶](https://python-jsonschema.readthedocs.io/en/stable/api/#submodules "Link to this heading")
--------------------------------------------------------------------------------------------------------

*   [`jsonschema.validators`](https://python-jsonschema.readthedocs.io/en/stable/api/jsonschema/validators/)
*   [`jsonschema.exceptions`](https://python-jsonschema.readthedocs.io/en/stable/api/jsonschema/exceptions/)
*   [`jsonschema.protocols`](https://python-jsonschema.readthedocs.io/en/stable/api/jsonschema/protocols/)

[`jsonschema`](https://python-jsonschema.readthedocs.io/en/stable/api/#module-jsonschema "jsonschema")[¶](https://python-jsonschema.readthedocs.io/en/stable/api/#module-jsonschema "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

An implementation of JSON Schema for Python.

The main functionality is provided by the validator classes for each of the supported JSON Schema versions.

Most commonly, [`jsonschema.validators.validate`](https://python-jsonschema.readthedocs.io/en/stable/api/jsonschema/validators/#jsonschema.validators.validate "jsonschema.validators.validate") is the quickest way to simply validate a given instance under a schema, and will create a validator for you.

_class_ jsonschema.FormatChecker(_formats:[Iterable](https://docs.python.org/3/library/typing.html#typing.Iterable "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]|[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")=None_)[[source]](https://python-jsonschema.readthedocs.io/en/stable/_modules/jsonschema/_format/#FormatChecker)[¶](https://python-jsonschema.readthedocs.io/en/stable/api/#jsonschema.FormatChecker "Link to this definition")
A `format` property checker.

JSON Schema does not mandate that the `format` property actually do any validation. If validation is desired however, instances of this class can be hooked into validators to enable format validation.

[`FormatChecker`](https://python-jsonschema.readthedocs.io/en/stable/api/#jsonschema.FormatChecker "jsonschema.FormatChecker") objects always return `True` when asked about formats that they do not know how to validate.

To add a check for a custom format use the [`FormatChecker.checks`](https://python-jsonschema.readthedocs.io/en/stable/api/#jsonschema.FormatChecker.checks "jsonschema.FormatChecker.checks") decorator.

Parameters:
**formats** – The known formats to validate. This argument can be used to limit which formats will be used during validation.

check(_instance:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")_, _format:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://python-jsonschema.readthedocs.io/en/stable/_modules/jsonschema/_format/#FormatChecker.check)[¶](https://python-jsonschema.readthedocs.io/en/stable/api/#jsonschema.FormatChecker.check "Link to this definition")
Check whether the instance conforms to the given format.

Parameters:
*   **instance** (_any primitive type_, i.e. str, number, bool) – The instance to check

*   **format** – The format that instance should conform to

Raises:
[**FormatError**](https://python-jsonschema.readthedocs.io/en/stable/api/jsonschema/exceptions/#jsonschema.exceptions.FormatError "jsonschema.exceptions.FormatError") – if the instance does not conform to `format`

checks(_format:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")_, _raises:[type](https://docs.python.org/3/library/functions.html#type "(in Python v3.14)")[[Exception](https://docs.python.org/3/library/exceptions.html#Exception "(in Python v3.14)")]|[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[type](https://docs.python.org/3/library/functions.html#type "(in Python v3.14)")[[Exception](https://docs.python.org/3/library/exceptions.html#Exception "(in Python v3.14)")],...]=()_)→[Callable](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")[[[_F](https://python-jsonschema.readthedocs.io/en/stable/api/#jsonschema._format._F "jsonschema._format._F")],[_F](https://python-jsonschema.readthedocs.io/en/stable/api/#jsonschema._format._F "jsonschema._format._F")][[source]](https://python-jsonschema.readthedocs.io/en/stable/_modules/jsonschema/_format/#FormatChecker.checks)[¶](https://python-jsonschema.readthedocs.io/en/stable/api/#jsonschema.FormatChecker.checks "Link to this definition")
Register a decorated function as validating a new format.

Parameters:
*   **format** – The format that the decorated function will check.

*   **raises** –

The exception(s) raised by the decorated function when an invalid instance is found.

The exception object will be accessible as the [`jsonschema.exceptions.ValidationError.cause`](https://python-jsonschema.readthedocs.io/en/stable/errors/#jsonschema.exceptions.ValidationError.cause "jsonschema.exceptions.ValidationError.cause") attribute of the resulting validation error.

conforms(_instance:[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")_, _format:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://python-jsonschema.readthedocs.io/en/stable/_modules/jsonschema/_format/#FormatChecker.conforms)[¶](https://python-jsonschema.readthedocs.io/en/stable/api/#jsonschema.FormatChecker.conforms "Link to this definition")
Check whether the instance conforms to the given format.

Parameters:
*   **instance** (_any primitive type_, i.e. str, number, bool) – The instance to check

*   **format** – The format that instance should conform to

Returns:
whether it conformed

Return type:
[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

_exception_ jsonschema.SchemaError(_message:str_, _validator:str=<unset>_, _path:Iterable[str|int]=()_, _cause:Exception|None=None_, _context=()_, _validator\_value:Any=<unset>_, _instance:Any=<unset>_, _schema:Mapping[str_, _Any]|bool=<unset>_, _schema\_path:Iterable[str|int]=()_, _parent:\_Error|None=None_, _type\_checker:\_types.TypeChecker=<unset>_)[[source]](https://python-jsonschema.readthedocs.io/en/stable/_modules/jsonschema/exceptions/#SchemaError)[¶](https://python-jsonschema.readthedocs.io/en/stable/api/#jsonschema.SchemaError "Link to this definition")
A schema was invalid under its corresponding metaschema.

_class_ jsonschema.TypeChecker(_type\_checkers:Mapping[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"),Callable[[[TypeChecker](https://python-jsonschema.readthedocs.io/en/stable/api/#jsonschema.TypeChecker "jsonschema.TypeChecker"),Any],[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")]]=HashTrieMap({})_)[[source]](https://python-jsonschema.readthedocs.io/en/stable/_modules/jsonschema/_types/#TypeChecker)[¶](https://python-jsonschema.readthedocs.io/en/stable/api/#jsonschema.TypeChecker "Link to this definition")
A [type](https://json-schema.org/draft/2020-12/json-schema-validation.html#section-6.1.1) property checker.

A [`TypeChecker`](https://python-jsonschema.readthedocs.io/en/stable/api/#jsonschema.TypeChecker "jsonschema.TypeChecker") performs type checking for a [`Validator`](https://python-jsonschema.readthedocs.io/en/stable/api/jsonschema/protocols/#jsonschema.protocols.Validator "jsonschema.protocols.Validator"), converting between the defined JSON Schema types and some associated Python types or objects.

Modifying the behavior just mentioned by redefining which Python objects are considered to be of which JSON Schema types can be done using [`TypeChecker.redefine`](https://python-jsonschema.readthedocs.io/en/stable/api/#jsonschema.TypeChecker.redefine "jsonschema.TypeChecker.redefine") or [`TypeChecker.redefine_many`](https://python-jsonschema.readthedocs.io/en/stable/api/#jsonschema.TypeChecker.redefine_many "jsonschema.TypeChecker.redefine_many"), and types can be removed via [`TypeChecker.remove`](https://python-jsonschema.readthedocs.io/en/stable/api/#jsonschema.TypeChecker.remove "jsonschema.TypeChecker.remove"). Each of these return a new [`TypeChecker`](https://python-jsonschema.readthedocs.io/en/stable/api/#jsonschema.TypeChecker "jsonschema.TypeChecker").

Parameters:
**type_checkers** – The initial mapping of types to their checking functions.

is_type(_instance_, _type:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://python-jsonschema.readthedocs.io/en/stable/_modules/jsonschema/_types/#TypeChecker.is_type)[¶](https://python-jsonschema.readthedocs.io/en/stable/api/#jsonschema.TypeChecker.is_type "Link to this definition")
Check if the instance is of the appropriate type.

Parameters:
*   **instance** – The instance to check

*   **type** – The name of the type that is expected.

Raises:
[**jsonschema.exceptions.UndefinedTypeCheck**](https://python-jsonschema.readthedocs.io/en/stable/api/jsonschema/exceptions/#jsonschema.exceptions.UndefinedTypeCheck "jsonschema.exceptions.UndefinedTypeCheck") – if `type` is unknown to this object.

redefine(_type:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")_, _fn_)→[TypeChecker](https://python-jsonschema.readthedocs.io/en/stable/api/#jsonschema.TypeChecker "jsonschema._types.TypeChecker")[[source]](https://python-jsonschema.readthedocs.io/en/stable/_modules/jsonschema/_types/#TypeChecker.redefine)[¶](https://python-jsonschema.readthedocs.io/en/stable/api/#jsonschema.TypeChecker.redefine "Link to this definition")
Produce a new checker with the given type redefined.

Parameters:
*   **type** – The name of the type to check.

*   **fn** ([_collections.abc.Callable_](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.14)")) – A callable taking exactly two parameters - the type checker calling the function and the instance to check. The function should return true if instance is of this type and false otherwise.

redefine_many(_definitions=()_)→[TypeChecker](https://python-jsonschema.readthedocs.io/en/stable/api/#jsonschema.TypeChecker "jsonschema._types.TypeChecker")[[source]](https://python-jsonschema.readthedocs.io/en/stable/_modules/jsonschema/_types/#TypeChecker.redefine_many)[¶](https://python-jsonschema.readthedocs.io/en/stable/api/#jsonschema.TypeChecker.redefine_many "Link to this definition")
Produce a new checker with the given types redefined.

Parameters:
**definitions** ([_dict_](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")) – A dictionary mapping types to their checking functions.

remove(_*types_)→[TypeChecker](https://python-jsonschema.readthedocs.io/en/stable/api/#jsonschema.TypeChecker "jsonschema._types.TypeChecker")[[source]](https://python-jsonschema.readthedocs.io/en/stable/_modules/jsonschema/_types/#TypeChecker.remove)[¶](https://python-jsonschema.readthedocs.io/en/stable/api/#jsonschema.TypeChecker.remove "Link to this definition")
Produce a new checker with the given types forgotten.

Parameters:
**types** – the names of the types to remove.

Raises:
[**jsonschema.exceptions.UndefinedTypeCheck**](https://python-jsonschema.readthedocs.io/en/stable/api/jsonschema/exceptions/#jsonschema.exceptions.UndefinedTypeCheck "jsonschema.exceptions.UndefinedTypeCheck") – if any given type is unknown to this object

jsonschema.validate(_instance_, _schema_, _cls=None_, _*args_, _**kwargs_)[[source]](https://python-jsonschema.readthedocs.io/en/stable/_modules/jsonschema/validators/#validate)[¶](https://python-jsonschema.readthedocs.io/en/stable/api/#jsonschema.validate "Link to this definition")
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

If the `cls` argument is not provided, two things will happen in accordance with the specification. First, if the schema has a [$schema](https://json-schema.org/draft/2020-12/json-schema-core.html#section-8.1.1) keyword containing a known meta-schema [[1]](https://python-jsonschema.readthedocs.io/en/stable/api/#id2) then the proper validator will be used. The specification recommends that all schemas contain [$schema](https://json-schema.org/draft/2020-12/json-schema-core.html#section-8.1.1) properties for this reason. If no [$schema](https://json-schema.org/draft/2020-12/json-schema-core.html#section-8.1.1) property is found, the default validator class is the latest released draft.

Any other provided positional and keyword arguments will be passed on when instantiating the `cls`.

Raises:
*   [**jsonschema.exceptions.ValidationError**](https://python-jsonschema.readthedocs.io/en/stable/api/jsonschema/exceptions/#jsonschema.exceptions.ValidationError "jsonschema.exceptions.ValidationError") – if the instance is invalid

*   [**jsonschema.exceptions.SchemaError**](https://python-jsonschema.readthedocs.io/en/stable/api/jsonschema/exceptions/#jsonschema.exceptions.SchemaError "jsonschema.exceptions.SchemaError") – if the schema itself is invalid

Footnotes

jsonschema._format._F _=~\_F_[¶](https://python-jsonschema.readthedocs.io/en/stable/api/#jsonschema._format._F "Link to this definition")
A format checker callable.

jsonschema._typing.id_of[¶](https://python-jsonschema.readthedocs.io/en/stable/api/#jsonschema._typing.id_of "Link to this definition")
alias of [`Callable`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.14)")[[[`bool`](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") | [`Mapping`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Mapping "(in Python v3.14)")[[`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")]], [`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")]
