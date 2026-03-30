# Source: https://clerc.so1ve.dev/reference/api/core/Namespace.Parser.md

# Source: https://clerc.so1ve.dev/reference/api/clerc/Namespace.Parser.md

---

url: /reference/api/clerc/Namespace.Parser.md
---

# Parser

## Classes

[InvalidSchemaError](Parser.Class.InvalidSchemaError.md)

‐

## Interfaces

[FlagDefaultValueFunction](Parser.Interface.FlagDefaultValueFunction.md)

‐

[ObjectInputType](Parser.Interface.ObjectInputType.md)

‐

[ParsedResult](Parser.Interface.ParsedResult.md)

The parsed result.

[ParserOptions](Parser.Interface.ParserOptions.md)

Configuration options for the parser.

[TypeFunction](Parser.Interface.TypeFunction.md)

Defines how a string input is converted to the target type T.

## Type Aliases

[BaseFlagOptions](Parser.TypeAlias.BaseFlagOptions.md)

‐

[FlagDefaultValue](Parser.TypeAlias.FlagDefaultValue.md)

‐

[FlagDefinitionValue](Parser.TypeAlias.FlagDefinitionValue.md)

‐

[FlagOptions](Parser.TypeAlias.FlagOptions.md)

‐

[FlagsDefinition](Parser.TypeAlias.FlagsDefinition.md)

‐

[IgnoreFunction](Parser.TypeAlias.IgnoreFunction.md)

A callback function to conditionally stop parsing. When it returns true,
parsing stops and remaining arguments are preserved in `ignored`.

[InferFlags](Parser.TypeAlias.InferFlags.md)

An advanced utility type that infers the exact type of the `flags` object in
the parsed result, based on the provided `flags` configuration object T.

[RawInputType](Parser.TypeAlias.RawInputType.md)

‐

[TypeValue](Parser.TypeAlias.TypeValue.md)

‐

## Functions

[appendDotValues](Parser.Function.appendDotValues.md)

Similar to setDotValues but handles duplicate keys by converting to arrays.
Does NOT apply type conversion - value is set as-is. Useful for flags that
can be specified multiple times.

[coerceObjectValue](Parser.Function.coerceObjectValue.md)

Default value coercion for Object type. Converts "true" / "" to true, "false"
to false, other values remain unchanged.

[createParser](Parser.Function.createParser.md)

‐

[parse](Parser.Function.parse.md)

‐

[setDotValues](Parser.Function.setDotValues.md)

Sets a value at a nested path in an object, creating intermediate objects as
needed. Does NOT apply type conversion - value is set as-is. Overwrites
existing values.

## References

### DOUBLE\_DASH

Re-exports [DOUBLE\_DASH](Variable.DOUBLE_DASH.md)

***

### inferDefault

Re-exports [inferDefault](Function.inferDefault.md)

***

### KNOWN\_FLAG

Re-exports [KNOWN\_FLAG](Variable.KNOWN_FLAG.md)

***

### PARAMETER

Re-exports [PARAMETER](Variable.PARAMETER.md)

***

### UNKNOWN\_FLAG

Re-exports [UNKNOWN\_FLAG](Variable.UNKNOWN_FLAG.md)
