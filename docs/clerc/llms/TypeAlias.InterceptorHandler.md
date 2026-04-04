# Source: https://clerc.so1ve.dev/reference/api/core/TypeAlias.InterceptorHandler.md

# Source: https://clerc.so1ve.dev/reference/api/clerc/TypeAlias.InterceptorHandler.md

---

url: /reference/api/clerc/TypeAlias.InterceptorHandler.md
---

# Type Alias: InterceptorHandler()\<C, GF>

```ts twoslash
// @include: imports
type InterceptorHandler<C, GF> = (context, next) => void | Promise<void>;
```

Defined in: [packages/core/src/types/interceptor.ts:17](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/interceptor.ts#L17)

## Type Parameters

`C` *extends* [`Command`](Interface.Command.md)

[`Command`](Interface.Command.md)

`GF` *extends* [`ClercFlagsDefinition`](TypeAlias.ClercFlagsDefinition.md)

`object`

## Parameters

`context`

[`InterceptorContext`](TypeAlias.InterceptorContext.md)<`C`, `GF`>

`next`

[`InterceptorNext`](TypeAlias.InterceptorNext.md)

## Returns

`void` | `Promise`<`void`>
