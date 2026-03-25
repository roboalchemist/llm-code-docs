# Source: https://clerc.so1ve.dev/reference/api/utils/TypeAlias.RequireExactlyOne.md

---

url: /reference/api/utils/TypeAlias.RequireExactlyOne.md
---

# Type Alias: RequireExactlyOne\<T, Keys>

```ts twoslash
// @include: imports
type RequireExactlyOne<T, Keys> = {
  [K in Keys]-?: Required<Pick<T, K>> &
    Partial<Record<Exclude<Keys, K>, never>>;
}[Keys] &
  Omit<T, Keys>;
```

Defined in: [types/type-fest.ts:40](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/utils/src/types/type-fest.ts#L40)

## Type Parameters

`T`

‐

`Keys` *extends* keyof `T`

keyof `T`
