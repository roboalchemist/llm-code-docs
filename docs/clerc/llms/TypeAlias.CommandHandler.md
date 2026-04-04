# Source: https://clerc.so1ve.dev/reference/api/core/TypeAlias.CommandHandler.md

# Source: https://clerc.so1ve.dev/reference/api/clerc/TypeAlias.CommandHandler.md

---

url: /reference/api/clerc/TypeAlias.CommandHandler.md
---

# Type Alias: CommandHandler()\<C, GF>

```ts twoslash
// @include: imports
type CommandHandler<C, GF> = (context) => void;
```

Defined in: [packages/core/src/types/command.ts:62](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/command.ts#L62)

## Type Parameters

`C` *extends* [`Command`](Interface.Command.md)

[`Command`](Interface.Command.md)

`GF` *extends* [`ClercFlagsDefinition`](TypeAlias.ClercFlagsDefinition.md)

[`ClercFlagsDefinition`](TypeAlias.ClercFlagsDefinition.md)

## Parameters

`context`

[`CommandHandlerContext`](TypeAlias.CommandHandlerContext.md)<`C`, `GF`>

## Returns

`void`
