# Source: https://rolldown.rs/reference/Function.parseAst.md

---
url: /reference/Function.parseAst.md
---
# Function: parseAst()

* **Exported from**: `rolldown/parseAst`
* **Type**: (`sourceText`: `string`, `options?`: `ParserOptions` | `null`, `filename?`: `string`) => `Program`

Parse code synchronously and return the AST.

This function is similar to Rollup's `parseAst` function.
Prefer using [`parseSync`](Function.parseSync.md) instead of this function as it has more information in the return value.

## Parameters

### sourceText

`string`

### options?

`ParserOptions` | `null`

### filename?

`string`

## Returns

`Program`
