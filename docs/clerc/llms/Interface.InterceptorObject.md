# Source: https://clerc.so1ve.dev/reference/api/core/Interface.InterceptorObject.md

# Source: https://clerc.so1ve.dev/reference/api/clerc/Interface.InterceptorObject.md

---

url: /reference/api/clerc/Interface.InterceptorObject.md
---

# Interface: InterceptorObject\<C, GF>

Defined in: [packages/core/src/types/interceptor.ts:28](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/interceptor.ts#L28)

## Type Parameters

`C` *extends* [`Command`](Interface.Command.md)

[`Command`](Interface.Command.md)

`GF` *extends* [`ClercFlagsDefinition`](TypeAlias.ClercFlagsDefinition.md)

`object`

## Properties

&#x20;`enforce?`

`"pre"` | `"normal"` | `"post"`

[packages/core/src/types/interceptor.ts:32](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/interceptor.ts#L32)

&#x20;`handler`

[`InterceptorHandler`](TypeAlias.InterceptorHandler.md)<`C`, `GF`>

[packages/core/src/types/interceptor.ts:33](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/interceptor.ts#L33)
