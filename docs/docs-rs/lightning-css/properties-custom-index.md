lightningcss::properties

# Module custom

Source

## Structs§

CustomPropertyA CSS custom property, representing any unknown property.EnvironmentVariableA CSS environment variable reference.FunctionA custom CSS function.TokenListA raw list of CSS tokens, with embedded parsed values.UnparsedPropertyA known property with an unparsed value.VariableA CSS variable reference.

## Enums§

CustomPropertyNameA CSS custom property name.EnvironmentVariableNameA CSS environment variable name.TokenA raw CSS token.TokenOrValueA raw CSS token, or a parsed value.UAEnvironmentVariableA UA-defined environment variable name.UnresolvedColorA color value with an unresolved alpha value (e.g. a variable).
These can be converted from the modern slash syntax to older comma syntax.
This can only be done when the only unresolved component is the alpha
since variables can resolve to multiple tokens.
