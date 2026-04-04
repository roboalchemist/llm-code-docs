# Source: https://clerc.so1ve.dev/reference/api/parser/TypeAlias.FlagOptions.md

---

url: /reference/api/parser/TypeAlias.FlagOptions.md
---

# Type Alias: FlagOptions

```ts twoslash
// @include: imports
type FlagOptions =
  | (BaseFlagOptions<BooleanConstructor> & object)
  | (BaseFlagOptions & object);
```

Defined in: [packages/parser/src/types.ts:72](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/types.ts#L72)
