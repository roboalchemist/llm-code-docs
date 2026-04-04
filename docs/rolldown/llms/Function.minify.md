# Source: https://rolldown.rs/reference/Function.minify.md

---
url: /reference/Function.minify.md
---
# Function: minify()

* **Exported from**: `rolldown/utils`
* **Type**: (`filename`: `string`, `sourceText`: `string`, `options?`: [`MinifyOptions`](Interface.MinifyOptions.md) | `null`) => `Promise`<[`MinifyResult`](Interface.MinifyResult.md)>
* **Experimental**

Minify asynchronously.

Note: This function can be slower than [`minifySync`](Function.minifySync.md) due to the overhead of spawning a thread.

## Parameters

### filename

`string`

### sourceText

`string`

### options?

[`MinifyOptions`](Interface.MinifyOptions.md) | `null`

## Returns

`Promise`<[`MinifyResult`](Interface.MinifyResult.md)>
