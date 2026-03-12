# Source: https://tsdown.dev/reference/api/TypeAlias.UserConfigFn.md

---
url: /reference/api/TypeAlias.UserConfigFn.md
---
# Type Alias: UserConfigFn()

```ts
type UserConfigFn = (inlineConfig, context) => Awaitable<Arrayable<UserConfig>>
```

Defined in: [src/config/types.ts:620](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/config/types.ts#L620)

## Parameters

### inlineConfig

[`InlineConfig`](Interface.InlineConfig.md)

### context

#### ci

`boolean`

## Returns

`Awaitable`<`Arrayable`<[`UserConfig`](Interface.UserConfig.md)>>
