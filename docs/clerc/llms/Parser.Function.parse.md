# Source: https://clerc.so1ve.dev/reference/api/core/Parser.Function.parse.md

# Source: https://clerc.so1ve.dev/reference/api/clerc/Parser.Function.parse.md

---

url: /reference/api/clerc/Parser.Function.parse.md
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

`T` *extends* [`FlagsDefinition`](Parser.TypeAlias.FlagsDefinition.md)

## Parameters

`args`

`string`\[]

`options`

[`ParserOptions`](Parser.Interface.ParserOptions.md)<`T`>

## Returns

[`ParsedResult`](Parser.Interface.ParsedResult.md)<{ \[K in string | number | symbol]: \_InferFlags\<T>\[K] }>
