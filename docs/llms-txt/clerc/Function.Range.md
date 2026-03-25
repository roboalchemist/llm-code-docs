# Source: https://clerc.so1ve.dev/reference/api/advanced-types/Function.Range.md

---

url: /reference/api/advanced-types/Function.Range.md
---

# Function: Range()

```ts twoslash
// @include: imports
function Range(min, max): TypeFunction<number>;
```

Defined in: [packages/advanced-types/src/index.ts:49](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/advanced-types/src/index.ts#L49)

Creates a range type function that validates the input is a number within the
specified range.

## Parameters

`min`

`number`

The minimum acceptable value (inclusive)

`max`

`number`

The maximum acceptable value (inclusive)

## Returns

`TypeFunction`<`number`>

A TypeFunction that validates the input value

## Throws

If the value is not a number or is outside the specified
range
