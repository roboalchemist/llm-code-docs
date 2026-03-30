# Source: https://tsdown.dev/reference/api/TypeAlias.TsdownInputOption.md

---
url: /reference/api/TypeAlias.TsdownInputOption.md
---
# Type Alias: TsdownInputOption

```ts
type TsdownInputOption = Arrayable<string | Record<string, Arrayable<string>>>
```

Defined in: [src/config/types.ts:71](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/config/types.ts#L71)

Extended input option that supports glob negation patterns.

When using object form, values can be:

* A single glob pattern string
* An array of glob patterns, including negation patterns (prefixed with `!`)

## Example

```ts
entry: {
  // Single pattern
  "utils/*": "./src/utils/*.ts",
  // Array with negation pattern to exclude files
  "hooks/*": ["./src/hooks/*.ts", "!./src/hooks/index.ts"],
}
```
