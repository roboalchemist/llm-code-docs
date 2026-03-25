# Source: https://clerc.so1ve.dev/reference/api/core/Parser.Function.setDotValues.md

# Source: https://clerc.so1ve.dev/reference/api/clerc/Parser.Function.setDotValues.md

---

url: /reference/api/clerc/Parser.Function.setDotValues.md
---

# Function: setDotValues()

```ts twoslash
// @include: imports
function setDotValues(obj, path, value): void;
```

Defined in: [packages/parser/src/utils.ts:96](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/utils.ts#L96)

Sets a value at a nested path in an object, creating intermediate objects as
needed. Does NOT apply type conversion - value is set as-is. Overwrites
existing values.

## Parameters

`obj`

`any`

The target object

`path`

`string`

Dot-separated path (e.g., "foo.bar.baz")

`value`

`any`

The value to set (used as-is, no type conversion)

## Returns

`void`
