# Source: https://clerc.so1ve.dev/reference/api/core/Parser.TypeAlias.IgnoreFunction.md

# Source: https://clerc.so1ve.dev/reference/api/clerc/Parser.TypeAlias.IgnoreFunction.md

---

url: /reference/api/clerc/Parser.TypeAlias.IgnoreFunction.md
---

# Type Alias: IgnoreFunction()

```ts twoslash
// @include: imports
type IgnoreFunction = (type, arg) => boolean;
```

Defined in: [packages/parser/src/types.ts:35](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/types.ts#L35)

A callback function to conditionally stop parsing. When it returns true,
parsing stops and remaining arguments are preserved in `ignored`.

## Parameters

`type`

| *typeof* [`KNOWN_FLAG`](Variable.KNOWN_FLAG.md) | *typeof* [`UNKNOWN_FLAG`](Variable.UNKNOWN_FLAG.md) | *typeof* [`PARAMETER`](Variable.PARAMETER.md)

The type of the current argument: 'known-flag' or
'unknown-flag' for flags, 'parameter' for positional arguments

`arg`

`string`

The current argument being processed

## Returns

`boolean`

True to stop parsing, false to continue
