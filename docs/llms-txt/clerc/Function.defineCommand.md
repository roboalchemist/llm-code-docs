# Source: https://clerc.so1ve.dev/reference/api/core/Function.defineCommand.md

# Source: https://clerc.so1ve.dev/reference/api/clerc/Function.defineCommand.md

---

url: /reference/api/clerc/Function.defineCommand.md
---

# Function: defineCommand()

```ts twoslash
// @include: imports
function defineCommand<Name, Parameters, Flags>(
  command,
  handler?,
): CommandWithHandler<Name, Parameters, Flags>;
```

Defined in: [packages/core/src/helpers.ts:9](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/helpers.ts#L9)

## Type Parameters

`Name` *extends* `string`

`Parameters` *extends* readonly [`ParameterDefinitionValue`](TypeAlias.ParameterDefinitionValue.md)\[]

`Flags` *extends* [`ClercFlagsDefinition`](TypeAlias.ClercFlagsDefinition.md)

## Parameters

`command`

[`Command`](Interface.Command.md)<`Name`, `Parameters`, `Flags`>

`handler?`

`NoInfer`<[`CommandHandler`](TypeAlias.CommandHandler.md)<[`Command`](Interface.Command.md)<`Name`, `Parameters`, `Flags`>>>

## Returns

[`CommandWithHandler`](TypeAlias.CommandWithHandler.md)<`Name`, `Parameters`, `Flags`>
