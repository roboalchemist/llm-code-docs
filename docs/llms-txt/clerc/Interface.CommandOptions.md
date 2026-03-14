# Source: https://clerc.so1ve.dev/reference/api/core/Interface.CommandOptions.md

# Source: https://clerc.so1ve.dev/reference/api/clerc/Interface.CommandOptions.md

---

url: /reference/api/clerc/Interface.CommandOptions.md
---

# Interface: CommandOptions\<Parameters, Flags>

Defined in: [packages/core/src/types/command.ts:10](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/command.ts#L10)

## Extends

* [`CommandCustomOptions`](Interface.CommandCustomOptions.md)

## Extended by

* [`Command`](Interface.Command.md)

## Type Parameters

`Parameters` *extends* readonly [`ParameterDefinitionValue`](TypeAlias.ParameterDefinitionValue.md)\[]

readonly [`ParameterDefinitionValue`](TypeAlias.ParameterDefinitionValue.md)\[]

`Flags` *extends* [`ClercFlagsDefinition`](TypeAlias.ClercFlagsDefinition.md)

[`ClercFlagsDefinition`](TypeAlias.ClercFlagsDefinition.md)

## Properties

&#x20;`alias?`

`MaybeArray`<`string`>

‐

‐

[packages/core/src/types/command.ts:15](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/command.ts#L15)

&#x20;`completions?`

`object`

Completions options for the command.

[`CommandCustomOptions`](Interface.CommandCustomOptions.md).[`completions`](Interface.CommandCustomOptions.md#completions)

[packages/plugin-completions/src/index.ts:17](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-completions/src/index.ts#L17)

`completions.handler?`

(`command`) => `void`

Handler to provide custom completions for the command.

‐

[packages/plugin-completions/src/index.ts:27](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-completions/src/index.ts#L27)

`completions.show?`

`boolean`

Whether to show the command in completions output.

**Default**

```ts twoslash
// @include: imports
true;
```

‐

[packages/plugin-completions/src/index.ts:23](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-completions/src/index.ts#L23)

&#x20;`flags?`

`Flags`

‐

‐

[packages/core/src/types/command.ts:17](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/command.ts#L17)

&#x20;`help?`

[`CommandHelpOptions`](Interface.CommandHelpOptions.md)

Help options for the command.

[`CommandCustomOptions`](Interface.CommandCustomOptions.md).[`help`](Interface.CommandCustomOptions.md#help)

[packages/plugin-help/src/index.ts:47](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-help/src/index.ts#L47)

&#x20;`ignore?`

[`IgnoreFunction`](Parser.TypeAlias.IgnoreFunction.md)

A callback function to conditionally stop parsing. When it returns true,
parsing stops and remaining arguments are preserved in ignored.

‐

[packages/core/src/types/command.ts:23](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/command.ts#L23)

&#x20;`parameters?`

`Parameters`

‐

‐

[packages/core/src/types/command.ts:16](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/command.ts#L16)
