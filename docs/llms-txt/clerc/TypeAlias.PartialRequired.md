# Source: https://clerc.so1ve.dev/reference/api/utils/TypeAlias.PartialRequired.md

---

url: /reference/api/utils/TypeAlias.PartialRequired.md
---

# Type Alias: PartialRequired\<T, K>

```ts twoslash
// @include: imports
type PartialRequired<T, K> = T & { [P in K]-?: T[P] };
```

Defined in: [types/index.ts:6](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/utils/src/types/index.ts#L6)

## Type Parameters

`T`

`K` *extends* keyof `T`
