# Source: https://clerc.so1ve.dev/reference/api/parser/Function.appendDotValues.md

---

url: /reference/api/parser/Function.appendDotValues.md
---

# Function: appendDotValues()

```ts twoslash
// @include: imports
function appendDotValues(obj, path, value): void;
```

Defined in: [packages/parser/src/utils.ts:117](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/utils.ts#L117)

Similar to setDotValues but handles duplicate keys by converting to arrays.
Does NOT apply type conversion - value is set as-is. Useful for flags that
can be specified multiple times.

## Parameters

`obj`

`any`

The target object

`path`

`string`

Dot-separated path (e.g., "foo.bar")

`value`

`any`

The value to set or append (used as-is, no type conversion)

## Returns

`void`
