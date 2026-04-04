# Source: https://rolldown.rs/reference/InputOptions.experimental.md

---
url: /reference/InputOptions.experimental.md
---
# experimental

* **Type**: object with the properties below
* **Optional**
* **Experimental**

Experimental features that may change in future releases and can introduce behavior change without a major version bump.

## attachDebugInfo?

* **Type**: `"none"` | `"simple"` | `"full"`
* **Optional**

Attach debug information to the output bundle.

Available modes:

* `none`: No debug information is attached.
* `simple`: Attach comments indicating which files the bundled code comes from. These comments could be removed by the minifier.
* `full`: Attach detailed debug information to the output bundle. These comments are using legal comment syntax, so they won't be removed by the minifier.

### Default

'simple'

### In-depth

Each chunk will include a comment explaining the reason why it was created:

| Reason                | Format                                                                 | Description                                                                                       |
| --------------------- | ---------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| User-defined Entry    | `User-defined Entry: [Entry-Module-Id: <path>] [Name: Some("<name>")]` | Explicit entry point from build config                                                            |
| Dynamic Entry         | `Dynamic Entry: [Entry-Module-Id: <path>] [Name: None]`                | Chunk created from `import()` expression                                                          |
| Common Chunk          | `Common Chunk: [Shared-By: <entry1>, <entry2>, ...]`                   | Shared modules extracted for multiple entries                                                     |
| Manual Code Splitting | `ManualCodeSplitting: [Group-Name: <name>]`                            | Chunk created by [`output.codeSplitting`](/reference/OutputOptions.codeSplitting) option          |
| Preserve Modules      | `Enabling Preserve Module: [User-defined: <bool>] [Module-Id: <path>]` | Per-module chunk from [`output.preserveModules`](/reference/OutputOptions.preserveModules) option |

When rolldown optimized away empty facade chunks (entry chunks with no modules of their own), the target chunk will include `Eliminated Facade Chunk: [Chunk-Name: <name>] [Entry-Module-Id: <path>]`.

## chunkImportMap?

* **Type**: `boolean` | { `baseUrl?`: `string`; `fileName?`: `string`; }
* **Optional**

Enables automatic generation of a chunk import map asset during build.

This map only includes chunks with hashed filenames, where keys are derived from the facade module
name or primary chunk name. It produces stable and unique hash-based filenames, effectively preventing
cascading cache invalidation caused by content hashes and maximizing browser cache reuse.

The output defaults to `importmap.json` unless overridden via `fileName`. A base URL prefix
(default `"/"`) can be applied to all paths. The resulting JSON is a valid import map and can be
directly injected into HTML via `<script type="importmap">`.

### Example

```js
{
  experimental: {
    chunkImportMap: {
      baseUrl: '/',
      fileName: 'importmap.json'
    }
  },
  plugins: [
    {
      name: 'inject-import-map',
      generateBundle(_, bundle) {
        const chunkImportMap = bundle['importmap.json'];
        if (chunkImportMap?.type === 'asset') {
          const htmlPath = path.resolve('index.html');
          let html = fs.readFileSync(htmlPath, 'utf-8');

          html = html.replace(
            /<script\s+type="importmap"[^>]*>[\s\S]*?</script>/i,
            `<script type="importmap">${chunkImportMap.source}</script>`
          );

          fs.writeFileSync(htmlPath, html);
          delete bundle['importmap.json'];
        }
      }
    }
  ]
}
```

> \[!TIP]
> If you want to learn more, you can check out the example here: [examples/chunk-import-map](https://github.com/rolldown/rolldown/tree/main/examples/chunk-import-map)

### Default

```ts
false
```

## chunkModulesOrder?

* **Type**: `"exec-order"` | `"module-id"`
* **Optional**

Control which order should be used when rendering modules in a chunk.

Available options:

* `exec-order`: Almost equivalent to the topological order of the module graph, but specially handling when module graph has cycle.
* `module-id`: This is more friendly for gzip compression, especially for some javascript static asset lib (e.g. icon library)

> \[!NOTE]
> Try to sort the modules by their module id if possible (Since rolldown scope hoist all modules in the chunk, we only try to sort those modules by module id if we could ensure runtime behavior is correct after sorting).

### Default

```ts
'exec-order'
```

## chunkOptimization?

* **Type**: `boolean`
* **Optional**

Control whether to optimize chunks by allowing entry chunks to have different exports than the underlying entry module.
This optimization can reduce the number of generated chunks.

When enabled, rolldown will try to insert common modules directly into existing chunks rather than creating
separate chunks for them, which can result in fewer output files and better performance.

This optimization is automatically disabled when any module uses top-level await (TLA) or contains TLA dependencies,
as it could affect execution order guarantees.

### Default

```ts
true
```

## incrementalBuild?

* **Type**: `boolean`
* **Optional**

Enable incremental build support. Required to be used with `watch` mode.

### Default

```ts
false
```

## lazyBarrel?

* **Type**: `boolean`
* **Optional**

Control whether to enable lazy barrel optimization.

Lazy barrel optimization avoids compiling unused re-export modules in side-effect-free barrel modules,
significantly improving build performance for large codebases with many barrel modules.

### See

[Lazy Barrel Documentation](/in-depth/lazy-barrel-optimization)

### Default

```ts
false
```

## nativeMagicString?

* **Type**: `boolean`
* **Optional**

Use native Rust implementation of MagicString for source map generation.

[MagicString](https://github.com/rich-harris/magic-string) is a JavaScript library commonly used by bundlers
for string manipulation and source map generation. When enabled, rolldown will use a native Rust
implementation of MagicString instead of the JavaScript version, providing significantly better performance
during source map generation and code transformation.

**Benefits**

* **Improved Performance**: The native Rust implementation is typically faster than the JavaScript version,
  especially for large codebases with extensive source maps.
* **Background Processing**: Source map generation is performed asynchronously in a background thread,
  allowing the main bundling process to continue without blocking. This parallel processing can significantly
  reduce overall build times when working with JavaScript transform hooks.
* **Better Integration**: Seamless integration with rolldown's native Rust architecture.

### Example

```js
export default {
  experimental: {
    nativeMagicString: true
  },
  output: {
    sourcemap: true
  }
}
```

> \[!NOTE]
> This is an experimental feature. While it aims to provide identical behavior to the JavaScript
> implementation, there may be edge cases. Please report any discrepancies you encounter.
> For a complete working example, see [examples/native-magic-string](https://github.com/rolldown/rolldown/tree/main/examples/native-magic-string)

### Default

```ts
false
```

## resolveNewUrlToAsset?

* **Type**: `boolean`
* **Optional**

When enabled, `new URL()` calls will be transformed to a stable asset URL which includes the updated name and content hash.
It is necessary to pass `import.meta.url` as the second argument to the
`new URL` constructor, otherwise no transform will be applied.
:::warning
JavaScript and TypeScript files referenced via `new URL('./file.js', import.meta.url)` or `new URL('./file.ts', import.meta.url)` will **not** be transformed or bundled. The file will be copied as-is, meaning TypeScript files remain untransformed and dependencies are not resolved.

The expected behavior for JS/TS files is still being discussed and may
change in future releases. See [#7258](https://github.com/rolldown/rolldown/issues/7258) for more context.
:::

### Example

```js
// main.js
const url = new URL('./styles.css', import.meta.url);
console.log(url);

// Example output after bundling WITHOUT the option (default)
const url = new URL('./styles.css', import.meta.url);
console.log(url);

// Example output after bundling WITH `experimental.resolveNewUrlToAsset` set to `true`
const url = new URL('assets/styles-CjdrdY7X.css', import.meta.url);
console.log(url);
```

### Default

```ts
false
```
