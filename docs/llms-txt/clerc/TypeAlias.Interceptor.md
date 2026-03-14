# Source: https://clerc.so1ve.dev/reference/api/core/TypeAlias.Interceptor.md

# Source: https://clerc.so1ve.dev/reference/api/clerc/TypeAlias.Interceptor.md

---

url: /reference/api/clerc/TypeAlias.Interceptor.md
---

# Type Alias: Interceptor\<C, GF>

```ts twoslash
// @include: imports
type Interceptor<C, GF> = InterceptorHandler<C, GF> | InterceptorObject<C, GF>;
```

Defined in: [packages/core/src/types/interceptor.ts:36](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/interceptor.ts#L36)

## Type Parameters

`C` *extends* [`Command`](Interface.Command.md)

[`Command`](Interface.Command.md)

`GF` *extends* [`ClercFlagsDefinition`](TypeAlias.ClercFlagsDefinition.md)

`object`
