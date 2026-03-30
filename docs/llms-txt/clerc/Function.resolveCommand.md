# Source: https://clerc.so1ve.dev/reference/api/core/Function.resolveCommand.md

# Source: https://clerc.so1ve.dev/reference/api/clerc/Function.resolveCommand.md

---

url: /reference/api/clerc/Function.resolveCommand.md
---

# Function: resolveCommand()

```ts twoslash
// @include: imports
function resolveCommand(
  commandsMap,
  parameters,
):
  | [
      Command<
        string,
        readonly ParameterDefinitionValue[],
        ClercFlagsDefinition
      >,
      string,
    ]
  | [undefined, undefined];
```

Defined in: [packages/core/src/command.ts:3](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/command.ts#L3)

## Parameters

`commandsMap`

[`CommandsMap`](TypeAlias.CommandsMap.md)

`parameters`

`string`\[]

## Returns

| \[[`Command`](Interface.Command.md)<`string`, readonly [`ParameterDefinitionValue`](TypeAlias.ParameterDefinitionValue.md)\[], [`ClercFlagsDefinition`](TypeAlias.ClercFlagsDefinition.md)>, `string`]
| \[`undefined`, `undefined`]
