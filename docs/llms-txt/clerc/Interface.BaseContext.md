# Source: https://clerc.so1ve.dev/reference/api/core/Interface.BaseContext.md

# Source: https://clerc.so1ve.dev/reference/api/clerc/Interface.BaseContext.md

---

url: /reference/api/clerc/Interface.BaseContext.md
---

# Interface: BaseContext\<C, GF>

Defined in: [packages/core/src/types/context.ts:22](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/context.ts#L22)

## Type Parameters

`C` *extends* [`Command`](Interface.Command.md)

[`Command`](Interface.Command.md)

`GF` *extends* [`ClercFlagsDefinition`](TypeAlias.ClercFlagsDefinition.md)

`object`

## Properties

&#x20;`calledAs?`

`string`

[packages/core/src/types/context.ts:27](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/context.ts#L27)

&#x20;`command?`

`C`

[packages/core/src/types/context.ts:26](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/context.ts#L26)

&#x20;`flags`

`InferFlagsWithGlobal`<`C`, `GF`>

[packages/core/src/types/context.ts:29](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/context.ts#L29)

&#x20;`ignored`

`string`\[]

[packages/core/src/types/context.ts:30](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/context.ts#L30)

&#x20;`parameters`

[`InferParameters`](TypeAlias.InferParameters.md)<`NonNullable`<`C`\[`"parameters"`]>>

[packages/core/src/types/context.ts:28](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/context.ts#L28)

&#x20;`rawParsed`

[`ParsedResult`](Parser.Interface.ParsedResult.md)<`InferFlagsWithGlobal`<`C`, `GF`>>

[packages/core/src/types/context.ts:31](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/context.ts#L31)

&#x20;`store`

`Partial`<[`ContextStore`](Interface.ContextStore.md)>

[packages/core/src/types/context.ts:32](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/context.ts#L32)
