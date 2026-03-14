# Source: https://clerc.so1ve.dev/reference/api/utils/TypeAlias.UnionToIntersection.md

---

url: /reference/api/utils/TypeAlias.UnionToIntersection.md
---

# Type Alias: UnionToIntersection\<U>

```ts twoslash
// @include: imports
type UnionToIntersection<U> = U extends any
  ? (k) => void
  : never extends (k) => void
    ? I
    : never;
```

Defined in: [types/index.ts:10](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/utils/src/types/index.ts#L10)

## Type Parameters

`U`
