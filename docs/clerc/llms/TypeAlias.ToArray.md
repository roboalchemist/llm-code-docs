# Source: https://clerc.so1ve.dev/reference/api/utils/TypeAlias.ToArray.md

---

url: /reference/api/utils/TypeAlias.ToArray.md
---

# Type Alias: ToArray\<T>

```ts twoslash
// @include: imports
type ToArray<T> = T extends any[] ? T : [T];
```

Defined in: [types/index.ts:1](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/utils/src/types/index.ts#L1)

## Type Parameters

`T`
