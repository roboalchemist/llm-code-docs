# Source: https://python-jsonschema.readthedocs.io/en/stable/creating/

Title: Creating or Extending Validator Classes

URL Source: https://python-jsonschema.readthedocs.io/en/stable/creating/

Markdown Content:
jsonschema.validators.create(_meta\_schema:referencing.jsonschema.ObjectSchema_, _validators:Mapping[str_, _\_typing.SchemaKeywordValidator]|Iterable[tuple[str_, _\_typing.SchemaKeywordValidator]]=()_, _version:str|None=None_, _type\_checker:\_types.TypeChecker=<TypeChecker types={'array'_, _'boolean'_, _'integer'_, _'null'_, _'number'_, _'object'_, _'string'}>_, _format\_checker:\_format.FormatChecker=<FormatChecker checkers=['date'_, _'email'_, _'idn-email'_, _'idn-hostname'_, _'ipv4'_, _'ipv6'_, _'regex'_, _'uuid']>_, _id\_of:\_typing.id\_of=<function \_dollar\_id>_, _applicable\_validators:\_typing.ApplicableValidators=operator.methodcaller('items')_)→[type](https://docs.python.org/3/library/functions.html#type "(in Python v3.14)")[[Validator](https://python-jsonschema.readthedocs.io/en/stable/api/jsonschema/protocols/#jsonschema.protocols.Validator "jsonschema.protocols.Validator")][[source]](https://python-jsonschema.readthedocs.io/en/stable/_modules/jsonschema/validators/#create)
Create a new validator class.

Parameters:
*   **meta_schema** – the meta schema for the new validator class

*   **validators** –

a mapping from names to callables, where each callable will validate the schema property with the given name.

Each callable should take 4 arguments:

> 1.   a validator instance,
> 
>     2.   the value of the property being validated within the instance
> 
>     3.   the instance
> 
>     4.   the schema

*   **version** – an identifier for the version that this validator class will validate. If provided, the returned validator class will have its `__name__` set to include the version, and also will have [`jsonschema.validators.validates`](https://python-jsonschema.readthedocs.io/en/stable/api/jsonschema/validators/#jsonschema.validators.validates "jsonschema.validators.validates") automatically called for the given version.

*   **type_checker** –

a type checker, used when applying the [type](https://json-schema.org/draft/2020-12/json-schema-validation.html#section-6.1.1) keyword.

If unprovided, a [`jsonschema.TypeChecker`](https://python-jsonschema.readthedocs.io/en/stable/api/#jsonschema.TypeChecker "jsonschema.TypeChecker") will be created with a set of default types typical of JSON Schema drafts.

*   **format_checker** –

a format checker, used when applying the [format](https://json-schema.org/draft/2020-12/json-schema-validation.html#name-implementation-requirements) keyword.

If unprovided, a [`jsonschema.FormatChecker`](https://python-jsonschema.readthedocs.io/en/stable/api/#jsonschema.FormatChecker "jsonschema.FormatChecker") will be created with a set of default formats typical of JSON Schema drafts.

*   **id_of** – A function that given a schema, returns its ID.

*   **applicable_validators** – A function that, given a schema, returns the list of applicable schema keywords and associated values which will be used to validate the instance. This is mostly used to support pre-draft 7 versions of JSON Schema which specified behavior around ignoring keywords if they were siblings of a `$ref` keyword. If you’re not attempting to implement similar behavior, you can typically ignore this argument and leave it at its default.

Returns:
a new [`jsonschema.protocols.Validator`](https://python-jsonschema.readthedocs.io/en/stable/api/jsonschema/protocols/#jsonschema.protocols.Validator "jsonschema.protocols.Validator") class

jsonschema.validators.extend(_validator_, _validators=()_, _version=None_, _type\_checker=None_, _format\_checker=None_)[[source]](https://python-jsonschema.readthedocs.io/en/stable/_modules/jsonschema/validators/#extend)
Create a new validator class by extending an existing one.

Parameters:
*   **validator** ([_jsonschema.protocols.Validator_](https://python-jsonschema.readthedocs.io/en/stable/api/jsonschema/protocols/#jsonschema.protocols.Validator "jsonschema.protocols.Validator")) – an existing validator class

*   **validators** ([_collections.abc.Mapping_](https://docs.python.org/3/library/collections.abc.html#collections.abc.Mapping "(in Python v3.14)")) –

a mapping of new validator callables to extend with, whose structure is as in [`create`](https://python-jsonschema.readthedocs.io/en/stable/api/jsonschema/validators/#jsonschema.validators.create "jsonschema.validators.create").

Note

Any validator callables with the same name as an existing one will (silently) replace the old validator callable entirely, effectively overriding any validation done in the “parent” validator class.

If you wish to instead extend the behavior of a parent’s validator callable, delegate and call it directly in the new validator function by retrieving it using `OldValidator.VALIDATORS["validation_keyword_name"]`. 
*   **version** ([_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) – a version for the new validator class

*   **type_checker** ([_jsonschema.TypeChecker_](https://python-jsonschema.readthedocs.io/en/stable/api/#jsonschema.TypeChecker "jsonschema.TypeChecker")) –

a type checker, used when applying the [type](https://json-schema.org/draft/2020-12/json-schema-validation.html#section-6.1.1) keyword.

If unprovided, the type checker of the extended [`jsonschema.protocols.Validator`](https://python-jsonschema.readthedocs.io/en/stable/api/jsonschema/protocols/#jsonschema.protocols.Validator "jsonschema.protocols.Validator") will be carried along.

*   **format_checker** ([_jsonschema.FormatChecker_](https://python-jsonschema.readthedocs.io/en/stable/api/#jsonschema.FormatChecker "jsonschema.FormatChecker")) –

a format checker, used when applying the [format](https://json-schema.org/draft/2020-12/json-schema-validation.html#name-implementation-requirements) keyword.

If unprovided, the format checker of the extended [`jsonschema.protocols.Validator`](https://python-jsonschema.readthedocs.io/en/stable/api/jsonschema/protocols/#jsonschema.protocols.Validator "jsonschema.protocols.Validator") will be carried along.

Returns:
a new [`jsonschema.protocols.Validator`](https://python-jsonschema.readthedocs.io/en/stable/api/jsonschema/protocols/#jsonschema.protocols.Validator "jsonschema.protocols.Validator") class extending the one provided

Note

Meta Schemas

The new validator class will have its parent’s meta schema.

If you wish to change or extend the meta schema in the new validator class, modify `META_SCHEMA` directly on the returned class. Note that no implicit copying is done, so a copy should likely be made before modifying it, in order to not affect the old validator.

jsonschema.validators.validator_for(_schema_, _default:type[Validator]|\_utils.Unset=<unset>_)→[type](https://docs.python.org/3/library/functions.html#type "(in Python v3.14)")[[Validator](https://python-jsonschema.readthedocs.io/en/stable/api/jsonschema/protocols/#jsonschema.protocols.Validator "jsonschema.protocols.Validator")][[source]](https://python-jsonschema.readthedocs.io/en/stable/_modules/jsonschema/validators/#validator_for)
Retrieve the validator class appropriate for validating the given schema.

Uses the [$schema](https://json-schema.org/draft/2020-12/json-schema-core.html#section-8.1.1) keyword that should be present in the given schema to look up the appropriate validator class.

Parameters:
*   **schema** ([_collections.abc.Mapping_](https://docs.python.org/3/library/collections.abc.html#collections.abc.Mapping "(in Python v3.14)")_or_[_bool_](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")) – the schema to look at

*   **default** –

the default to return if the appropriate validator class cannot be determined.

If unprovided, the default is to return the latest supported draft.

Examples

The [$schema](https://json-schema.org/draft/2020-12/json-schema-core.html#section-8.1.1) JSON Schema keyword will control which validator class is returned:

>>> schema = {
...     "$schema": "https://json-schema.org/draft/2020-12/schema",
...     "type": "integer",
... }
>>> jsonschema.validators.validator_for(schema)
<class 'jsonschema.validators.Draft202012Validator'>

Here, a draft 7 schema instead will return the draft 7 validator:

>>> schema = {
...     "$schema": "http://json-schema.org/draft-07/schema#",
...     "type": "integer",
... }
>>> jsonschema.validators.validator_for(schema)
<class 'jsonschema.validators.Draft7Validator'>

Schemas with no `$schema` keyword will fallback to the default argument:

>>> schema = {"type": "integer"}
>>> jsonschema.validators.validator_for(
...     schema, default=Draft7Validator,
... )
<class 'jsonschema.validators.Draft7Validator'>

or if none is provided, to the latest version supported. Always including the keyword when authoring schemas is highly recommended.

jsonschema.validators.validates(_version_)[[source]](https://python-jsonschema.readthedocs.io/en/stable/_modules/jsonschema/validators/#validates)
Register the decorated validator for a `version` of the specification.

Registered validators and their meta schemas will be considered when parsing [$schema](https://json-schema.org/draft/2020-12/json-schema-core.html#section-8.1.1) keywords’ URIs.

Parameters:
**version** ([_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) – An identifier to use as the version’s name

Returns:
a class decorator to decorate the validator with the version

Return type:
[collections.abc.Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.14)")

Creating Validation Errors[¶](https://python-jsonschema.readthedocs.io/en/stable/creating/#creating-validation-errors "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------

Any validating function that validates against a subschema should call `descend`, rather than `iter_errors`. If it recurses into the instance, or schema, it should pass one or both of the `path` or `schema_path` arguments to `descend` in order to properly maintain where in the instance or schema respectively the error occurred.

The Validator Protocol[¶](https://python-jsonschema.readthedocs.io/en/stable/creating/#the-validator-protocol "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------

`jsonschema` defines a [`protocol`](https://docs.python.org/3/library/typing.html#typing.Protocol "(in Python v3.14)"), [`jsonschema.protocols.Validator`](https://python-jsonschema.readthedocs.io/en/stable/api/jsonschema/protocols/#jsonschema.protocols.Validator "jsonschema.protocols.Validator") which can be used in type annotations to describe the type of a validator.

For full details, see [The Validator Protocol](https://python-jsonschema.readthedocs.io/en/stable/validate/#validator-protocol).
