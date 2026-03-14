# Source: https://clerc.so1ve.dev/reference/api/utils/TypeAlias.MaybeAsyncGetter.md

---

url: /reference/api/utils/TypeAlias.MaybeAsyncGetter.md
---

# Type Alias: MaybeAsyncGetter\<T>

```ts twoslash
// @include: imports
type MaybeAsyncGetter<T> = T | () => T | Promise<T>;
```

Defined in: [types/index.ts:4](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/utils/src/types/index.ts#L4)

## Type Parameters

`T`
