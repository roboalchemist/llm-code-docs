# Source: https://clerc.so1ve.dev/reference/api/core/Parser.Interface.ParsedResult.md

# Source: https://clerc.so1ve.dev/reference/api/clerc/Parser.Interface.ParsedResult.md

---

url: /reference/api/clerc/Parser.Interface.ParsedResult.md
---

# Interface: ParsedResult\<TFlags>

Defined in: [packages/parser/src/types.ts:124](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/types.ts#L124)

The parsed result.

## Type Parameters

`TFlags` *extends* `Record`<`string`, `any`>

The specific flags type inferred from ParserOptions.

## Properties

&#x20;`doubleDash`

`string`\[]

Arguments after the `--` delimiter.

[packages/parser/src/types.ts:132](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/types.ts#L132)

&#x20;`flags`

`TFlags`

The parsed flags. This is a strongly-typed object whose structure is
inferred from the `flags` configuration in ParserOptions.

[packages/parser/src/types.ts:137](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/types.ts#L137)

&#x20;`ignored`

`string`\[]

Arguments that were not parsed due to ignore callback.

[packages/parser/src/types.ts:153](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/types.ts#L153)

&#x20;`missingRequiredFlags`

`string`\[]

List of required flags that were not provided.

[packages/parser/src/types.ts:157](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/types.ts#L157)

&#x20;`parameters`

`string`\[]

Positional arguments or commands.

[packages/parser/src/types.ts:128](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/types.ts#L128)

&#x20;`raw`

`string`\[]

The raw command-line arguments.

[packages/parser/src/types.ts:141](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/types.ts#L141)

&#x20;`rawUnknown`

`string`\[]

Raw arguments for unknown flags (original string form).

[packages/parser/src/types.ts:149](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/types.ts#L149)

&#x20;`unknown`

`Record`<`string`, [`RawInputType`](Parser.TypeAlias.RawInputType.md)>

Unknown flags encountered during parsing.

[packages/parser/src/types.ts:145](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/types.ts#L145)
