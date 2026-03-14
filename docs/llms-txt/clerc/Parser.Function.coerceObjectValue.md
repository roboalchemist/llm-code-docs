# Source: https://clerc.so1ve.dev/reference/api/core/Parser.Function.coerceObjectValue.md

# Source: https://clerc.so1ve.dev/reference/api/clerc/Parser.Function.coerceObjectValue.md

---

url: /reference/api/clerc/Parser.Function.coerceObjectValue.md
---

# Function: coerceObjectValue()

```ts twoslash
// @include: imports
function coerceObjectValue(value): string | boolean;
```

Defined in: [packages/parser/src/utils.ts:77](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/utils.ts#L77)

Default value coercion for Object type. Converts "true" / "" to true, "false"
to false, other values remain unchanged.

## Parameters

`value`

`string`

The raw string value from CLI

## Returns

`string` | `boolean`

Coerced value (boolean or string)
