# Source: https://clerc.so1ve.dev/reference/api/clerc.md

---

url: /reference/api/clerc.md
---

# clerc

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

[CommandHelpOptions](Interface.CommandHelpOptions.md)

‐

[CommandOptions](Interface.CommandOptions.md)

‐

[ContextStore](Interface.ContextStore.md)

‐

[CreateOptions](Interface.CreateOptions.md)

‐

[FlagCustomOptions](Interface.FlagCustomOptions.md)

‐

[FlagHelpOptions](Interface.FlagHelpOptions.md)

‐

[FriendlyErrorPluginOptions](Interface.FriendlyErrorPluginOptions.md)

‐

[GroupsOptions](Interface.GroupsOptions.md)

Options for defining groups in help output.

[HelpOptions](Interface.HelpOptions.md)

‐

[HelpPluginOptions](Interface.HelpPluginOptions.md)

‐

[InterceptorObject](Interface.InterceptorObject.md)

‐

[NotFoundPluginOptions](Interface.NotFoundPluginOptions.md)

‐

[ParameterCustomOptions](Interface.ParameterCustomOptions.md)

‐

[ParseOptions](Interface.ParseOptions.md)

‐

[Plugin](Interface.Plugin.md)

‐

[UpdateNotifierPluginOptions](Interface.UpdateNotifierPluginOptions.md)

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

[GroupDefinition](TypeAlias.GroupDefinition.md)

A group definition as a tuple of \[key, displayName]. The key is used in help
options to assign items to groups. The displayName is shown in the help
output.

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

[defaultFormatters](Variable.defaultFormatters.md)

‐

[DOUBLE\_DASH](Variable.DOUBLE_DASH.md)

‐

[KNOWN\_FLAG](Variable.KNOWN_FLAG.md)

‐

[PARAMETER](Variable.PARAMETER.md)

‐

[UNKNOWN\_FLAG](Variable.UNKNOWN_FLAG.md)

‐

## Functions

[Cli](Function.Cli.md)

‐

[completionsPlugin](Function.completionsPlugin.md)

‐

[createStopAtFirstParameter](Function.createStopAtFirstParameter.md)

‐

[defineCommand](Function.defineCommand.md)

‐

[definePlugin](Function.definePlugin.md)

‐

[extractParameterInfo](Function.extractParameterInfo.md)

‐

[friendlyErrorPlugin](Function.friendlyErrorPlugin.md)

‐

[helpPlugin](Function.helpPlugin.md)

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

[notFoundPlugin](Function.notFoundPlugin.md)

‐

[resolveCommand](Function.resolveCommand.md)

‐

[strictFlagsPlugin](Function.strictFlagsPlugin.md)

‐

[updateNotifierPlugin](Function.updateNotifierPlugin.md)

Plugin to check for CLI updates using update-notifier.

**Example**

```ts twoslash
// @include: imports
import { Clerc } from "@clerc/core";
import { updateNotifierPlugin } from "@clerc/plugin-update-notifier";
import pkg from "./package.json";

Clerc.create().use(updateNotifierPlugin({ pkg })).parse();
```

[versionPlugin](Function.versionPlugin.md)

‐

## References

### InvalidSchemaError

Re-exports [InvalidSchemaError](Parser.Class.InvalidSchemaError.md)
