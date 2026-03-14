# Source: https://clerc.so1ve.dev/reference/api/utils/TypeAlias.CamelCase.md

---

url: /reference/api/utils/TypeAlias.CamelCase.md
---

# Type Alias: CamelCase\<S>

```ts twoslash
// @include: imports
type CamelCase<S> = S extends `${infer Head} ${infer Tail}`
  ? `${Head}${Capitalize<CamelCase<Tail>>}`
  : S extends `${infer Head}-${infer Tail}`
    ? `${Head}${Capitalize<CamelCase<Tail>>}`
    : S;
```

Defined in: [types/index.ts:16](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/utils/src/types/index.ts#L16)

## Type Parameters

`S` *extends* `string`
