# Source: https://rolldown.rs/reference/Function.parse.md

---
url: /reference/Function.parse.md
---
# Function: parse()

* **Exported from**: `rolldown/utils`
* **Type**: (`filename`: `string`, `sourceText`: `string`, `options?`: [`ParserOptions`](Interface.ParserOptions.md) | `null`) => `Promise`<[`ParseResult`](Interface.ParseResult.md)>

Parse JS/TS source asynchronously on a separate thread.

Note that not all of the workload can happen on a separate thread.
Parsing on Rust side does happen in a separate thread, but deserialization of the AST to JS objects
has to happen on current thread. This synchronous deserialization work typically outweighs
the asynchronous parsing by a factor of between 3 and 20.

i.e. the majority of the workload cannot be parallelized by using this method.

Generally [`parseSync`](Function.parseSync.md) is preferable to use as it does not have the overhead of spawning a thread.
If you need to parallelize parsing multiple files, it is recommended to use worker threads.

## Parameters

### filename

`string`

### sourceText

`string`

### options?

[`ParserOptions`](Interface.ParserOptions.md) | `null`

## Returns

`Promise`<[`ParseResult`](Interface.ParseResult.md)>
