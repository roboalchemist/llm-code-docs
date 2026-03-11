# Source: https://rolldown.rs/reference/Function.transformSync.md

---
url: /reference/Function.transformSync.md
---
# Function: transformSync()

* **Exported from**: `rolldown/utils`
* **Type**: (`filename`: `string`, `sourceText`: `string`, `options?`: [`TransformOptions`](Interface.TransformOptions-1.md) | `null`, `cache?`: [`TsconfigCache`](Class.TsconfigCache.md) | `null`) => [`TransformResult`](TypeAlias.TransformResult-1.md)
* **Experimental**

Transpile a JavaScript or TypeScript into a target ECMAScript version.

## Parameters

### filename

`string`

The name of the file being transformed. If this is a
relative path, consider setting the [`TransformOptions#cwd`](Interface.TransformOptions-1.md#cwd) option.

### sourceText

`string`

The source code to transform.

### options?

The transform options including tsconfig and inputMap. See [`TransformOptions`](Interface.TransformOptions-1.md) for more information.

[`TransformOptions`](Interface.TransformOptions-1.md) | `null`

### cache?

Optional tsconfig cache for reusing resolved tsconfig across multiple transforms.
Only used when `options.tsconfig` is `true`.

[`TsconfigCache`](Class.TsconfigCache.md) | `null`

## Returns

[`TransformResult`](TypeAlias.TransformResult-1.md)

an object containing the transformed code, source maps, and any errors
that occurred during parsing or transformation.
