# Source: https://clerc.so1ve.dev/reference/api/parser.md

---

url: /reference/api/parser.md
---

# @clerc/parser

## Classes

[InvalidSchemaError](Class.InvalidSchemaError.md)

‐

## Interfaces

[FlagDefaultValueFunction](Interface.FlagDefaultValueFunction.md)

‐

[ObjectInputType](Interface.ObjectInputType.md)

‐

[ParsedResult](Interface.ParsedResult.md)

The parsed result.

[ParserOptions](Interface.ParserOptions.md)

Configuration options for the parser.

[TypeFunction](Interface.TypeFunction.md)

Defines how a string input is converted to the target type T.

## Type Aliases

[BaseFlagOptions](TypeAlias.BaseFlagOptions.md)

‐

[FlagDefaultValue](TypeAlias.FlagDefaultValue.md)

‐

[FlagDefinitionValue](TypeAlias.FlagDefinitionValue.md)

‐

[FlagOptions](TypeAlias.FlagOptions.md)

‐

[FlagsDefinition](TypeAlias.FlagsDefinition.md)

‐

[IgnoreFunction](TypeAlias.IgnoreFunction.md)

A callback function to conditionally stop parsing. When it returns true,
parsing stops and remaining arguments are preserved in `ignored`.

[InferFlags](TypeAlias.InferFlags.md)

An advanced utility type that infers the exact type of the `flags` object in
the parsed result, based on the provided `flags` configuration object T.

[RawInputType](TypeAlias.RawInputType.md)

‐

[TypeValue](TypeAlias.TypeValue.md)

‐

## Variables

[DOUBLE\_DASH](Variable.DOUBLE_DASH.md)

‐

[KNOWN\_FLAG](Variable.KNOWN_FLAG.md)

‐

[PARAMETER](Variable.PARAMETER.md)

‐

[UNKNOWN\_FLAG](Variable.UNKNOWN_FLAG.md)

‐

## Functions

[appendDotValues](Function.appendDotValues.md)

Similar to setDotValues but handles duplicate keys by converting to arrays.
Does NOT apply type conversion - value is set as-is. Useful for flags that
can be specified multiple times.

[coerceObjectValue](Function.coerceObjectValue.md)

Default value coercion for Object type. Converts "true" / "" to true, "false"
to false, other values remain unchanged.

[createParser](Function.createParser.md)

‐

[inferDefault](Function.inferDefault.md)

Infers the implicit default value for a flag type based on its type
constructor. This is useful for help output to show the default values of
types that have built-in defaults.

* Boolean: false
* \[Boolean] (Counter): 0
* \[T] (Array): \[]
* Object: {}
* Others: undefined (no implicit default)

[parse](Function.parse.md)

‐

[setDotValues](Function.setDotValues.md)

Sets a value at a nested path in an object, creating intermediate objects as
needed. Does NOT apply type conversion - value is set as-is. Overwrites
existing values.
