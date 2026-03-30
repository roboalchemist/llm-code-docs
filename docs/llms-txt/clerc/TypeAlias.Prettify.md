# Source: https://clerc.so1ve.dev/reference/api/utils/TypeAlias.Prettify.md

---

url: /reference/api/utils/TypeAlias.Prettify.md
---

# Type Alias: Prettify\<T>

```ts twoslash
// @include: imports
type Prettify<T> = { [K in keyof T]: T[K] } & object;
```

Defined in: [types/type-fest.ts:7](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/utils/src/types/type-fest.ts#L7)

## Type Parameters

`T`
