# Source: https://clerc.so1ve.dev/reference/api/core/Parser.Interface.ParserOptions.md

# Source: https://clerc.so1ve.dev/reference/api/clerc/Parser.Interface.ParserOptions.md

---

url: /reference/api/clerc/Parser.Interface.ParserOptions.md
---

# Interface: ParserOptions\<T>

Defined in: [packages/parser/src/types.ts:92](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/types.ts#L92)

Configuration options for the parser.

## Type Parameters

`T` *extends* [`FlagsDefinition`](Parser.TypeAlias.FlagsDefinition.md)

`object`

## Properties

&#x20;`delimiters?`

`string`\[]

Delimiters to split flag names and values.

**Default**

```ts twoslash
// @include: imports
["=", ":"];
```

[packages/parser/src/types.ts:105](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/types.ts#L105)

&#x20;`flags?`

`T`

Detailed configuration for flags. Supports the full object syntax or a type
constructor as a shorthand. The key is the flag name (e.g., "file" for
"--file").

[packages/parser/src/types.ts:98](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/types.ts#L98)

&#x20;`ignore?`

[`IgnoreFunction`](Parser.TypeAlias.IgnoreFunction.md)

A callback function to conditionally stop parsing. When it returns true,
parsing stops and remaining arguments are preserved in `ignored`.

[packages/parser/src/types.ts:111](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/types.ts#L111)
