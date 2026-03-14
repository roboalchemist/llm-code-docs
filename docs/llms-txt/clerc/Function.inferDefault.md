# Source: https://clerc.so1ve.dev/reference/api/parser/Function.inferDefault.md

# Source: https://clerc.so1ve.dev/reference/api/core/Function.inferDefault.md

# Source: https://clerc.so1ve.dev/reference/api/clerc/Function.inferDefault.md

---

url: /reference/api/clerc/Function.inferDefault.md
---

# Function: inferDefault()

```ts twoslash
// @include: imports
function inferDefault(type): unknown;
```

Defined in: [packages/parser/src/utils.ts:22](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/utils.ts#L22)

Infers the implicit default value for a flag type based on its type
constructor. This is useful for help output to show the default values of
types that have built-in defaults.

* Boolean: false
* \[Boolean] (Counter): 0
* \[T] (Array): \[]
* Object: {}
* Others: undefined (no implicit default)

## Parameters

`type`

[`TypeValue`](Parser.TypeAlias.TypeValue.md)

The type value (constructor or array of constructor)

## Returns

`unknown`

The inferred default value, or undefined if no implicit default
