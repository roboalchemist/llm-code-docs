# Source: https://clerc.so1ve.dev/reference/api/parser/Function.createParser.md

---

url: /reference/api/parser/Function.createParser.md
---

# Function: createParser()

```ts twoslash
// @include: imports
function createParser<T>(options): object;
```

Defined in: [packages/parser/src/parse.ts:28](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/parse.ts#L28)

## Type Parameters

`T` *extends* [`FlagsDefinition`](TypeAlias.FlagsDefinition.md)

## Parameters

`options`

[`ParserOptions`](Interface.ParserOptions.md)<`T`>

## Returns

`object`

`parse`

`ParseFunction`<`T`>

[packages/parser/src/parse.ts:30](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/parse.ts#L30)
