# Source: https://clerc.so1ve.dev/reference/api/utils/Function.camelCase.md

---

url: /reference/api/utils/Function.camelCase.md
---

# Function: camelCase()

```ts twoslash
// @include: imports
function camelCase(str): string;
```

Defined in: [index.ts:19](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/utils/src/index.ts#L19)

Converts a dash- or space-separated string to camelCase.

Not using regexp for better performance, because this function is used in
parser.

## Parameters

`str`

`string`

## Returns

`string`
