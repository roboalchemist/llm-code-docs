# Source: https://clerc.so1ve.dev/reference/api/core.md

---

url: /reference/api/core.md
---

# @clerc/core

## Namespaces

[Parser](Namespace.Parser.md)

‐

[Types](Namespace.Types.md)

‐

## Classes

[Clerc](Class.Clerc.md)

‐

[InvalidCommandError](Class.InvalidCommandError.md)

‐

[InvalidParametersError](Class.InvalidParametersError.md)

‐

[MissingRequiredFlagError](Class.MissingRequiredFlagError.md)

‐

[MissingRequiredMetadataError](Class.MissingRequiredMetadataError.md)

‐

[NoCommandSpecifiedError](Class.NoCommandSpecifiedError.md)

‐

[NoSuchCommandError](Class.NoSuchCommandError.md)

‐

## Interfaces

[BaseContext](Interface.BaseContext.md)

‐

[Command](Interface.Command.md)

‐

[CommandCustomOptions](Interface.CommandCustomOptions.md)

‐

[CommandOptions](Interface.CommandOptions.md)

‐

[ContextStore](Interface.ContextStore.md)

‐

[CreateOptions](Interface.CreateOptions.md)

‐

[FlagCustomOptions](Interface.FlagCustomOptions.md)

‐

[InterceptorObject](Interface.InterceptorObject.md)

‐

[ParameterCustomOptions](Interface.ParameterCustomOptions.md)

‐

[ParseOptions](Interface.ParseOptions.md)

‐

[Plugin](Interface.Plugin.md)

‐

## Type Aliases

[ClercFlagDefinitionValue](TypeAlias.ClercFlagDefinitionValue.md)

‐

[ClercFlagOptions](TypeAlias.ClercFlagOptions.md)

‐

[ClercFlagsDefinition](TypeAlias.ClercFlagsDefinition.md)

‐

[CommandHandler](TypeAlias.CommandHandler.md)

‐

[CommandHandlerContext](TypeAlias.CommandHandlerContext.md)

‐

[CommandsMap](TypeAlias.CommandsMap.md)

‐

[CommandsRecord](TypeAlias.CommandsRecord.md)

‐

[CommandWithHandler](TypeAlias.CommandWithHandler.md)

‐

[ErrorHandler](TypeAlias.ErrorHandler.md)

‐

[InferParameters](TypeAlias.InferParameters.md)

‐

[Interceptor](TypeAlias.Interceptor.md)

‐

[InterceptorContext](TypeAlias.InterceptorContext.md)

‐

[InterceptorHandler](TypeAlias.InterceptorHandler.md)

‐

[InterceptorNext](TypeAlias.InterceptorNext.md)

Function to call the next interceptor in the chain. **MUST** be awaited.

[MakeEmitterEvents](TypeAlias.MakeEmitterEvents.md)

‐

[ParameterDefinitionValue](TypeAlias.ParameterDefinitionValue.md)

‐

[ParameterOptions](TypeAlias.ParameterOptions.md)

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

[createStopAtFirstParameter](Function.createStopAtFirstParameter.md)

‐

[defineCommand](Function.defineCommand.md)

‐

[definePlugin](Function.definePlugin.md)

‐

[extractParameterInfo](Function.extractParameterInfo.md)

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

[normalizeFlagValue](Function.normalizeFlagValue.md)

‐

[normalizeParameterValue](Function.normalizeParameterValue.md)

‐

[resolveCommand](Function.resolveCommand.md)

‐

## References

### InvalidSchemaError

Re-exports [InvalidSchemaError](Parser.Class.InvalidSchemaError.md)
