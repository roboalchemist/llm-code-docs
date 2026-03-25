# Source: https://clerc.so1ve.dev/reference/api/utils/Variable.isTruthy.md

---

url: /reference/api/utils/Variable.isTruthy.md
---

# Variable: isTruthy()

```ts twoslash
// @include: imports
const isTruthy: <T>(item) => item is Exclude<T, false | null | undefined>;
```

Defined in: [index.ts:91](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/utils/src/index.ts#L91)

## Type Parameters

`T`

## Parameters

`item`

`T`

## Returns

item is Exclude\<T, false | null | undefined>
