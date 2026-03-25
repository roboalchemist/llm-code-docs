# Source: https://clerc.so1ve.dev/reference/api/core/TypeAlias.InterceptorContext.md

# Source: https://clerc.so1ve.dev/reference/api/clerc/TypeAlias.InterceptorContext.md

---

url: /reference/api/clerc/TypeAlias.InterceptorContext.md
---

# Type Alias: InterceptorContext\<C, GF>

```ts twoslash
// @include: imports
type InterceptorContext<C, GF> = DeepPrettify<BaseContext<C, GF>>;
```

Defined in: [packages/core/src/types/interceptor.ts:7](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/interceptor.ts#L7)

## Type Parameters

`C` *extends* [`Command`](Interface.Command.md)

[`Command`](Interface.Command.md)

`GF` *extends* [`ClercFlagsDefinition`](TypeAlias.ClercFlagsDefinition.md)

`object`
