# Source: https://clerc.so1ve.dev/reference/api/core/Parser.TypeAlias.BaseFlagOptions.md

# Source: https://clerc.so1ve.dev/reference/api/clerc/Parser.TypeAlias.BaseFlagOptions.md

---

url: /reference/api/clerc/Parser.TypeAlias.BaseFlagOptions.md
---

# Type Alias: BaseFlagOptions\<T>

```ts twoslash
// @include: imports
type BaseFlagOptions<T> = FlagRequiredOrDefault & object;
```

Defined in: [packages/parser/src/types.ts:58](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/types.ts#L58)

## Type Declaration

`short?`

`string`

Short flag alias (single character).

[packages/parser/src/types.ts:70](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/types.ts#L70)

`type`

`T`

The type constructor or a function to convert the string value. To
support multiple occurrences of a flag (e.g., --file a --file b), wrap
the type in an array: \[String], \[Number]. e.g., String, Number, \[String],
(val) => val.split(',')

[packages/parser/src/types.ts:66](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/types.ts#L66)

## Type Parameters

`T` *extends* [`TypeValue`](Parser.TypeAlias.TypeValue.md)

[`TypeValue`](Parser.TypeAlias.TypeValue.md)
