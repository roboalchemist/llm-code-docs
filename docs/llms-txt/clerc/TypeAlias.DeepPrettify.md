# Source: https://clerc.so1ve.dev/reference/api/utils/TypeAlias.DeepPrettify.md

---

url: /reference/api/utils/TypeAlias.DeepPrettify.md
---

# Type Alias: DeepPrettify\<T, E>

```ts twoslash
// @include: imports
type DeepPrettify<T, E> = ConditionalDeepPrettify<
  T,
  E | NonRecursiveType | MapsSetsOrArrays,
  object
>;
```

Defined in: [types/type-fest.ts:32](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/utils/src/types/type-fest.ts#L32)

## Type Parameters

`T`

‐

`E`

`never`
