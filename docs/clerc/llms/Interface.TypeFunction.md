# Source: https://clerc.so1ve.dev/reference/api/parser/Interface.TypeFunction.md

---

url: /reference/api/parser/Interface.TypeFunction.md
---

# Interface: TypeFunction()\<T>

Defined in: [packages/parser/src/types.ts:17](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/types.ts#L17)

Defines how a string input is converted to the target type T.

## Type Parameters

`T`

`unknown`

The target type.

```ts twoslash
// @include: imports
TypeFunction(value): T;
```

Defined in: [packages/parser/src/types.ts:18](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/types.ts#L18)

Defines how a string input is converted to the target type T.

## Parameters

`value`

`string`

## Returns

`T`

## Properties

&#x20;`display?`

`string`

Optional display name for the type, useful in help output. If provided,
this will be shown instead of the function name.

[packages/parser/src/types.ts:23](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/types.ts#L23)
