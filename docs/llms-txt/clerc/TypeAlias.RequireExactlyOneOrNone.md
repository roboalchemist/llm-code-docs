# Source: https://clerc.so1ve.dev/reference/api/utils/TypeAlias.RequireExactlyOneOrNone.md

---

url: /reference/api/utils/TypeAlias.RequireExactlyOneOrNone.md
---

# Type Alias: RequireExactlyOneOrNone\<T, Keys>

```ts twoslash
// @include: imports
type RequireExactlyOneOrNone<T, Keys> =
  | ({
      [K in Keys]-?: Required<Pick<T, K>> &
        Partial<Record<Exclude<Keys, K>, never>>;
    }[Keys] &
      Omit<T, Keys>)
  | (Partial<Record<Keys, never>> & Omit<T, Keys>);
```

Defined in: [types/type-fest.ts:46](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/utils/src/types/type-fest.ts#L46)

## Type Parameters

`T`

‐

`Keys` *extends* keyof `T`

keyof `T`
