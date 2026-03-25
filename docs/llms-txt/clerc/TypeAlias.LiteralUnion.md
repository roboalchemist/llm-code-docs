# Source: https://clerc.so1ve.dev/reference/api/utils/TypeAlias.LiteralUnion.md

---

url: /reference/api/utils/TypeAlias.LiteralUnion.md
---

# Type Alias: LiteralUnion\<LiteralType, BaseType>

```ts twoslash
// @include: imports
type LiteralUnion<LiteralType, BaseType> =
  | LiteralType
  | (BaseType & Record<never, never>);
```

Defined in: [types/type-fest.ts:3](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/utils/src/types/type-fest.ts#L3)

## Type Parameters

`LiteralType`

`BaseType`
