# Source: https://clerc.so1ve.dev/reference/api/core/TypeAlias.CommandWithHandler.md

# Source: https://clerc.so1ve.dev/reference/api/clerc/TypeAlias.CommandWithHandler.md

---

url: /reference/api/clerc/TypeAlias.CommandWithHandler.md
---

# Type Alias: CommandWithHandler\<Name, Parameters, Flags>

```ts twoslash
// @include: imports
type CommandWithHandler<Name, Parameters, Flags> = Command<
  Name,
  Parameters,
  Flags
> &
  object;
```

Defined in: [packages/core/src/types/command.ts:36](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/command.ts#L36)

## Type Declaration

`handler?`

[`CommandHandler`](TypeAlias.CommandHandler.md)<[`Command`](Interface.Command.md)<`Name`, `Parameters`, `Flags`>>

[packages/core/src/types/command.ts:42](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/command.ts#L42)

## Type Parameters

`Name` *extends* `string`

`string`

`Parameters` *extends* readonly [`ParameterDefinitionValue`](TypeAlias.ParameterDefinitionValue.md)\[]

readonly [`ParameterDefinitionValue`](TypeAlias.ParameterDefinitionValue.md)\[]

`Flags` *extends* [`ClercFlagsDefinition`](TypeAlias.ClercFlagsDefinition.md)

[`ClercFlagsDefinition`](TypeAlias.ClercFlagsDefinition.md)
