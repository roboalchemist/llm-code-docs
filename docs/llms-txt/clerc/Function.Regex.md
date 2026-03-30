# Source: https://clerc.so1ve.dev/reference/api/advanced-types/Function.Regex.md

---

url: /reference/api/advanced-types/Function.Regex.md
---

# Function: Regex()

```ts twoslash
// @include: imports
function Regex(pattern, description?): TypeFunction<string>;
```

Defined in: [packages/advanced-types/src/index.ts:74](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/advanced-types/src/index.ts#L74)

Creates a regex type function that validates the input against the provided
pattern.

## Parameters

`pattern`

`RegExp`

The regular expression pattern to validate against

`description?`

`string`

Optional description for display purposes

## Returns

`TypeFunction`<`string`>

A TypeFunction that validates the input value

## Throws

If the value does not match the regex pattern
