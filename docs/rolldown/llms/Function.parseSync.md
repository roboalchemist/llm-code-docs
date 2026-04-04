# Source: https://rolldown.rs/reference/Function.parseSync.md

---
url: /reference/Function.parseSync.md
---
# Function: parseSync()

* **Exported from**: `rolldown/utils`
* **Type**: (`filename`: `string`, `sourceText`: `string`, `options?`: [`ParserOptions`](Interface.ParserOptions.md) | `null`) => [`ParseResult`](Interface.ParseResult.md)

Parse JS/TS source synchronously on current thread.

This is generally preferable over [`parse`](Function.parse.md) (async) as it does not have the overhead
of spawning a thread, and the majority of the workload cannot be parallelized anyway
(see [`parse`](Function.parse.md) documentation for details).

If you need to parallelize parsing multiple files, it is recommended to use worker threads
with `parseSync` rather than using [`parse`](Function.parse.md).

## Parameters

### filename

`string`

### sourceText

`string`

### options?

[`ParserOptions`](Interface.ParserOptions.md) | `null`

## Returns

[`ParseResult`](Interface.ParseResult.md)
