# Source: https://clerc.so1ve.dev/reference/api/core/TypeAlias.MakeEmitterEvents.md

# Source: https://clerc.so1ve.dev/reference/api/clerc/TypeAlias.MakeEmitterEvents.md

---

url: /reference/api/clerc/TypeAlias.MakeEmitterEvents.md
---

# Type Alias: MakeEmitterEvents\<Commands, GlobalFlags>

```ts twoslash
// @include: imports
type MakeEmitterEvents<Commands, GlobalFlags> = {
  [K in keyof Commands]: [CommandHandlerContext<Commands[K], GlobalFlags>];
};
```

Defined in: [packages/core/src/types/command.ts:47](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/command.ts#L47)

## Type Parameters

`Commands` *extends* [`CommandsRecord`](TypeAlias.CommandsRecord.md)

‐

`GlobalFlags` *extends* [`ClercFlagsDefinition`](TypeAlias.ClercFlagsDefinition.md)

[`ClercFlagsDefinition`](TypeAlias.ClercFlagsDefinition.md)
