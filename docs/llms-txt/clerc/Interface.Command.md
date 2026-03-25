# Source: https://clerc.so1ve.dev/reference/api/core/Interface.Command.md

# Source: https://clerc.so1ve.dev/reference/api/clerc/Interface.Command.md

---

url: /reference/api/clerc/Interface.Command.md
---

# Interface: Command\<Name, Parameters, Flags>

Defined in: [packages/core/src/types/command.ts:26](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/command.ts#L26)

## Extends

* [`CommandOptions`](Interface.CommandOptions.md)<`Parameters`, `Flags`>

## Type Parameters

`Name` *extends* `string`

`string`

`Parameters` *extends* readonly [`ParameterDefinitionValue`](TypeAlias.ParameterDefinitionValue.md)\[]

readonly [`ParameterDefinitionValue`](TypeAlias.ParameterDefinitionValue.md)\[]

`Flags` *extends* [`ClercFlagsDefinition`](TypeAlias.ClercFlagsDefinition.md)

[`ClercFlagsDefinition`](TypeAlias.ClercFlagsDefinition.md)

## Properties

&#x20;`alias?`

`MaybeArray`<`string`>

‐

[`CommandOptions`](Interface.CommandOptions.md).[`alias`](Interface.CommandOptions.md#alias)

[packages/core/src/types/command.ts:15](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/command.ts#L15)

&#x20;`completions?`

`object`

Completions options for the command.

[`CommandOptions`](Interface.CommandOptions.md).[`completions`](Interface.CommandOptions.md#completions)

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

&#x20;`description?`

`string`

‐

‐

[packages/core/src/types/command.ts:33](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/command.ts#L33)

&#x20;`flags?`

`Flags`

‐

[`CommandOptions`](Interface.CommandOptions.md).[`flags`](Interface.CommandOptions.md#flags-1)

[packages/core/src/types/command.ts:17](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/command.ts#L17)

&#x20;`help?`

[`CommandHelpOptions`](Interface.CommandHelpOptions.md)

Help options for the command.

[`CommandOptions`](Interface.CommandOptions.md).[`help`](Interface.CommandOptions.md#help)

[packages/plugin-help/src/index.ts:47](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-help/src/index.ts#L47)

&#x20;`ignore?`

[`IgnoreFunction`](Parser.TypeAlias.IgnoreFunction.md)

A callback function to conditionally stop parsing. When it returns true,
parsing stops and remaining arguments are preserved in ignored.

[`CommandOptions`](Interface.CommandOptions.md).[`ignore`](Interface.CommandOptions.md#ignore)

[packages/core/src/types/command.ts:23](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/command.ts#L23)

&#x20;`name`

`Name`

‐

‐

[packages/core/src/types/command.ts:32](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/command.ts#L32)

&#x20;`parameters?`

`Parameters`

‐

[`CommandOptions`](Interface.CommandOptions.md).[`parameters`](Interface.CommandOptions.md#parameters-1)

[packages/core/src/types/command.ts:16](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/command.ts#L16)
