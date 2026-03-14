# Source: https://clerc.so1ve.dev/reference/api/core/Types.Function.Enum.md

# Source: https://clerc.so1ve.dev/reference/api/clerc/Types.Function.Enum.md

---

url: /reference/api/clerc/Types.Function.Enum.md
---

# Function: Enum()

```ts twoslash
// @include: imports
function Enum<T>(...values): TypeFunction<T>;
```

Defined in: [packages/advanced-types/src/index.ts:23](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/advanced-types/src/index.ts#L23)

Creates a Enum type function that validates the input against allowed values.
The display name will be formatted as "value1 | value2 | ..." for help
output.

## Type Parameters

`T` *extends* `string`

## Parameters

...`values`

`T`\[]

Array of allowed string values

## Returns

[`TypeFunction`](Parser.Interface.TypeFunction.md)<`T`>

A TypeFunction that validates and returns the input value

## Example

```typescript twoslash
// @include: imports
const format = Enum(["json", "yaml", "xml"]);
// Help output will show: json | yaml | xml
```

## Throws

If the value is not in the allowed values list
