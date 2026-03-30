# Source: https://clerc.so1ve.dev/reference/api/core/TypeAlias.CommandHandlerContext.md

# Source: https://clerc.so1ve.dev/reference/api/clerc/TypeAlias.CommandHandlerContext.md

---

url: /reference/api/clerc/TypeAlias.CommandHandlerContext.md
---

# Type Alias: CommandHandlerContext\<C, GF>

```ts twoslash
// @include: imports
type CommandHandlerContext<C, GF> = DeepPrettify<
  PartialRequired<BaseContext<C, GF>, "command" | "calledAs"> & object
>;
```

Defined in: [packages/core/src/types/command.ts:54](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/command.ts#L54)

## Type Parameters

`C` *extends* [`Command`](Interface.Command.md)

[`Command`](Interface.Command.md)

`GF` *extends* [`ClercFlagsDefinition`](TypeAlias.ClercFlagsDefinition.md)

[`ClercFlagsDefinition`](TypeAlias.ClercFlagsDefinition.md)
