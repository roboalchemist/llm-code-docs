# Source: https://rolldown.rs/reference/Function.parseAstAsync.md

---
url: /reference/Function.parseAstAsync.md
---
# Function: parseAstAsync()

* **Exported from**: `rolldown/parseAst`
* **Type**: (`sourceText`: `string`, `options?`: `ParserOptions` | `null`, `filename?`: `string`) => `Promise`<`Program`>

Parse code asynchronously and return the AST.

This function is similar to Rollup's `parseAstAsync` function.
Prefer using parseAsync instead of this function as it has more information in the return value.

## Parameters

### sourceText

`string`

### options?

`ParserOptions` | `null`

### filename?

`string`

## Returns

`Promise`<`Program`>
