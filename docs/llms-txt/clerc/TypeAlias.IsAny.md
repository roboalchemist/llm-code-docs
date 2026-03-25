# Source: https://clerc.so1ve.dev/reference/api/utils/TypeAlias.IsAny.md

---

url: /reference/api/utils/TypeAlias.IsAny.md
---

# Type Alias: IsAny\<T>

```ts twoslash
// @include: imports
type IsAny<T> = 0 extends 1 & T ? true : false;
```

Defined in: [types/type-fest.ts:38](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/utils/src/types/type-fest.ts#L38)

## Type Parameters

`T`
