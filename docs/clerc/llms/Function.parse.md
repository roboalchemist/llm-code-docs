# Source: https://clerc.so1ve.dev/reference/api/parser/Function.parse.md

---

url: /reference/api/parser/Function.parse.md
---

# Function: parse()

```ts twoslash
// @include: imports
function parse<T>(
  args,
  options,
): ParsedResult<{ [K in string | number | symbol]: _InferFlags<T>[K] }>;
```

Defined in: [packages/parser/src/parse.ts:332](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/parse.ts#L332)

## Type Parameters

`T` *extends* [`FlagsDefinition`](TypeAlias.FlagsDefinition.md)

## Parameters

`args`

`string`\[]

`options`

[`ParserOptions`](Interface.ParserOptions.md)<`T`>

## Returns

[`ParsedResult`](Interface.ParsedResult.md)<{ \[K in string | number | symbol]: \_InferFlags\<T>\[K] }>
