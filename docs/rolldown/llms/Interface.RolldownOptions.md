# Source: https://rolldown.rs/reference/Interface.RolldownOptions.md

---
url: /reference/Interface.RolldownOptions.md
---
# Interface: RolldownOptions

## Extends

* [`InputOptions`](Interface.InputOptions.md)

## Properties

### checks?

* **Type**: [`ChecksOptions`](Interface.ChecksOptions.md)
* **Optional**

Controls which warnings are emitted during the build process. Each option can be set to `true` (emit warning) or `false` (suppress warning).

#### Inherited from

[`InputOptions`](Interface.InputOptions.md).[`checks`](Interface.InputOptions.md#checks)

***

### context?

* **Type**: `string`
* **Optional**

The value of `this` at the top level of each module. **Normally, you don't need to set this option.**

#### Default

```ts
undefined
```

#### Example

**Set custom context**

```js
export default {
  context: 'globalThis',
  output: {
    format: 'iife',
  },
};
```

#### In-depth

The `context` option controls what `this` refers to in the top-level scope of the input modules.

In ES modules, the `this` value is `undefined` by specification. This option allows you to set a different value. For example, if your input modules expect `this` to be `window` like in non-ES module scripts, you can set `context` to `'window'`.

Note that if the input module is detected as CommonJS, Rolldown will use `exports` as the `this` value regardless of this option.

#### Inherited from

[`InputOptions`](Interface.InputOptions.md).[`context`](Interface.InputOptions.md#context)

***

### cwd?

* **Type**: `string`
* **Optional**

The working directory to use when resolving relative paths in the configuration.

#### Default

```ts
process.cwd()
```

#### Inherited from

[`InputOptions`](Interface.InputOptions.md).[`cwd`](Interface.InputOptions.md#cwd)

***

### devtools?

* **Type**: object with the properties below
* **Optional**
* **Experimental**

Devtools integration options.

#### sessionId?

* **Type**: `string`
* **Optional**

#### Inherited from

[`InputOptions`](Interface.InputOptions.md).[`devtools`](Interface.InputOptions.md#devtools)

***

### experimental?

* **Type**: object with the properties below
* **Optional**
* **Experimental**

Experimental features that may change in future releases and can introduce behavior change without a major version bump.

#### attachDebugInfo?

* **Type**: `"none"` | `"simple"` | `"full"`
* **Optional**

Attach debug information to the output bundle.

Available modes:

* `none`: No debug information is attached.
* `simple`: Attach comments indicating which files the bundled code comes from. These comments could be removed by the minifier.
* `full`: Attach detailed debug information to the output bundle. These comments are using legal comment syntax, so they won't be removed by the minifier.

##### Default

'simple'

##### In-depth

Each chunk will include a comment explaining the reason why it was created:

| Reason                | Format                                                                 | Description                                                                                       |
| --------------------- | ---------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| User-defined Entry    | `User-defined Entry: [Entry-Module-Id: <path>] [Name: Some("<name>")]` | Explicit entry point from build config                                                            |
| Dynamic Entry         | `Dynamic Entry: [Entry-Module-Id: <path>] [Name: None]`                | Chunk created from `import()` expression                                                          |
| Common Chunk          | `Common Chunk: [Shared-By: <entry1>, <entry2>, ...]`                   | Shared modules extracted for multiple entries                                                     |
| Manual Code Splitting | `ManualCodeSplitting: [Group-Name: <name>]`                            | Chunk created by [`output.codeSplitting`](/reference/OutputOptions.codeSplitting) option          |
| Preserve Modules      | `Enabling Preserve Module: [User-defined: <bool>] [Module-Id: <path>]` | Per-module chunk from [`output.preserveModules`](/reference/OutputOptions.preserveModules) option |

When rolldown optimized away empty facade chunks (entry chunks with no modules of their own), the target chunk will include `Eliminated Facade Chunk: [Chunk-Name: <name>] [Entry-Module-Id: <path>]`.

#### chunkImportMap?

* **Type**: `boolean` | { `baseUrl?`: `string`; `fileName?`: `string`; }
* **Optional**

Enables automatic generation of a chunk import map asset during build.

This map only includes chunks with hashed filenames, where keys are derived from the facade module
name or primary chunk name. It produces stable and unique hash-based filenames, effectively preventing
cascading cache invalidation caused by content hashes and maximizing browser cache reuse.

The output defaults to `importmap.json` unless overridden via `fileName`. A base URL prefix
(default `"/"`) can be applied to all paths. The resulting JSON is a valid import map and can be
directly injected into HTML via `<script type="importmap">`.

##### Example

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

##### Default

```ts
false
```

#### chunkModulesOrder?

* **Type**: `"exec-order"` | `"module-id"`
* **Optional**

Control which order should be used when rendering modules in a chunk.

Available options:

* `exec-order`: Almost equivalent to the topological order of the module graph, but specially handling when module graph has cycle.
* `module-id`: This is more friendly for gzip compression, especially for some javascript static asset lib (e.g. icon library)

> \[!NOTE]
> Try to sort the modules by their module id if possible (Since rolldown scope hoist all modules in the chunk, we only try to sort those modules by module id if we could ensure runtime behavior is correct after sorting).

##### Default

```ts
'exec-order'
```

#### chunkOptimization?

* **Type**: `boolean`
* **Optional**

Control whether to optimize chunks by allowing entry chunks to have different exports than the underlying entry module.
This optimization can reduce the number of generated chunks.

When enabled, rolldown will try to insert common modules directly into existing chunks rather than creating
separate chunks for them, which can result in fewer output files and better performance.

This optimization is automatically disabled when any module uses top-level await (TLA) or contains TLA dependencies,
as it could affect execution order guarantees.

##### Default

```ts
true
```

#### incrementalBuild?

* **Type**: `boolean`
* **Optional**

Enable incremental build support. Required to be used with `watch` mode.

##### Default

```ts
false
```

#### lazyBarrel?

* **Type**: `boolean`
* **Optional**

Control whether to enable lazy barrel optimization.

Lazy barrel optimization avoids compiling unused re-export modules in side-effect-free barrel modules,
significantly improving build performance for large codebases with many barrel modules.

##### See

[Lazy Barrel Documentation](/in-depth/lazy-barrel-optimization)

##### Default

```ts
false
```

#### nativeMagicString?

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

##### Example

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

##### Default

```ts
false
```

#### resolveNewUrlToAsset?

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

##### Example

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

##### Default

```ts
false
```

#### Inherited from

[`InputOptions`](Interface.InputOptions.md).[`experimental`](Interface.InputOptions.md#experimental)

***

### external?

* **Type**: `string` | `RegExp` | (`string` | `RegExp`)\[] | [`ExternalOptionFunction`](TypeAlias.ExternalOptionFunction.md)
* **Optional**

Specifies which modules should be treated as external and not bundled. External modules will be left as import statements in the output.
When creating an `iife` or `umd` bundle, you will need to provide global variable names to replace your external imports via the [`output.globals`](/reference/OutputOptions.globals) option.

#### How Matching Works

The `external` option is checked **twice** during module resolution, against two different kinds of IDs:

1. **First check — raw import specifier** (e.g. `'lodash'`, `'./utils'`) is tested before any resolution happens, with `isResolved: false`. To mark `import "dependency"` as external, use `"dependency"` exactly as written in the import statement. If it matches, the module is immediately marked as external — **plugins and the internal resolver are skipped entirely**.

2. **Second check — resolved ID** (e.g. `'/project/node_modules/vue/dist/vue.runtime.esm-bundler.js'`) is tested after plugins and the internal resolver have run, with `isResolved: true`. If it matches, the module is marked as external.

The second check only runs if the first did not match. In both cases, [`makeAbsoluteExternalsRelative`](/reference/InputOptions.makeAbsoluteExternalsRelative) applies uniformly to determine whether absolute IDs are re-relativized in the output.

See the [External Modules guide](/in-depth/external-modules) for a detailed explanation of the full resolution flow and how the output path is determined.

#### Examples

##### String pattern

```js
export default {
  external: 'react',
};
```

##### Regular expression

```js
export default {
  external: /^react\//,
};
```

##### Array of patterns

```js
export default {
  external: ['react', 'react-dom', /^lodash/],
};
```

##### Function

```js
export default {
  external: (id) => {
    return !id.startsWith('.') && !id.startsWith('/');
  },
};
```

::: warning Performance Overhead

Using the function form has significant performance overhead because Rolldown is written in Rust and must call JavaScript functions from Rust for every module in your dependency graph.

Unless the logic relies on values other than `id`, it is recommended to use non-function values.

:::

#### Caveats

##### Avoid `/node_modules/` for npm packages

Because the pattern `/node_modules/` can only match on the **second check** (the resolved absolute path), the full resolved path like `/path/to/node_modules/vue/dist/vue.runtime.esm-bundler.js` ends up in the output verbatim. This makes the output non-portable.

Instead, match packages by name or use a pattern for bare module IDs:

```js
export default {
  // Exact package names
  external: ['vue', 'react', 'react-dom'],

  // Package name patterns
  external: [/^vue/, /^react/, /^@mui/],

  // All bare module IDs (not starting with `.` or `/`)
  external: /^[^./]/,
};
```

#### Inherited from

[`InputOptions`](Interface.InputOptions.md).[`external`](Interface.InputOptions.md#external)

***

### input?

* **Type**: `string` | `string`\[] | `Record`<`string`, `string`>
* **Optional**

Defines entries and location(s) of entry modules for the bundle. Relative paths are resolved based on the [`cwd`](Interface.InputOptions.md#cwd) option.

#### Examples

##### Single entry

```js
export default defineConfig({
  input: 'src/index.js',
});
```

##### Multiple entries

```js
export default defineConfig({
  input: ['src/index.js', 'src/vendor.js'],
});
```

##### Named multiple entries

```js
export default defineConfig({
  input: {
    index: 'src/index.js',
    utils: 'src/utils/index.js',
    'components/Foo': 'src/components/Foo.js',
  },
});
```

#### In-depth

`input` allows you to specify one or more [entries](/glossary/entry) with [names](/glossary/entry-name) for the bundling process.

When multiple entries are specified (either as an array or an object), Rolldown will create separate [entry chunks](/glossary/entry-chunk) for each entry. If a module is referenced from multiple entries, Rolldown will share the code of that module for those entries.

The generated chunk names will follow the [`output.chunkFileNames`](/reference/OutputOptions.chunkFileNames) option. When using the object form, the `[name]` portion of the file name will be the name of the object property while for the array form, it will be the file name of the entry point. Note that it is possible when using the object form to put entry points into different sub-folders by adding a `/` to the name.

If you want to convert a set of files to another format while maintaining the file structure and export signatures, the recommended way—instead of using [`output.preserveModules`](/reference/OutputOptions.preserveModules) that may tree-shake exports as well as emit virtual files created by plugins—is to turn every file into an entry point. You can do so dynamically e.g. via the [`tinyglobby`](https://github.com/SuperchupuDev/tinyglobby) package:

```js
import { defineConfig } from 'rolldown';
import { globSync } from 'tinyglobby';
import path from 'node:path';

export default defineConfig({
  input: Object.fromEntries(
    globSync('src/**/*.js').map((file) => [
      // This removes `src/` as well as the file extension from each
      // file, so e.g. src/nested/foo.js becomes nested/foo, and
      // normalizes Windows backslashes to forward slashes.
      path
        .relative('src', file.slice(0, file.length - path.extname(file).length))
        .split(path.sep)
        .join('/'),
      // This expands the relative paths to absolute paths, so e.g.
      // src/nested/foo.js becomes /project/src/nested/foo.js
      path.resolve(file),
    ]),
  ),
  output: {
    dir: 'dist',
    format: 'esm',
  },
});
```

#### Inherited from

[`InputOptions`](Interface.InputOptions.md).[`input`](Interface.InputOptions.md#input)

***

### logLevel?

* **Type**: `"info"` | `"debug"` | `"warn"` | `"silent"`
* **Optional**

Controls the verbosity of console logging during the build.

The default logLevel of "info" means that info and warnings logs will be processed while debug logs will be swallowed, which means that they are neither passed to plugin [`onLog`](/reference/Interface.Plugin#onlog) hooks nor the [`onLog`](/reference/InputOptions.onLog) option or printed to the console.

#### Default

```ts
'info'
```

#### Inherited from

[`InputOptions`](Interface.InputOptions.md).[`logLevel`](Interface.InputOptions.md#loglevel)

***

### makeAbsoluteExternalsRelative?

* **Type**: `false` | `true` | `"ifRelativeSource"`
* **Optional**

Determines if absolute external paths should be converted to relative paths in the output.

This does not only apply to paths that are absolute in the source but also to paths that are resolved to an absolute path by either a plugin or Rolldown core.

Despite the name, this option controls two things:

1. **Resolve-time normalization** — whether relative specifiers (e.g. `'./utils'`) are normalized to absolute paths internally for deduplication. Without normalization, `'./utils'` imported from different directories may collapse into one external module because they share the same raw string.
2. **Render-time output** — whether a resolved module ID (the absolute path after resolution) gets converted to a relative path in the output. It does not affect bare specifiers (e.g. `'lodash'`) or IDs that are already relative.

Both behaviors depend on the **original import specifier** (what you wrote in source code, e.g. `'./utils'`) vs the **resolved module ID** (the absolute path after resolution, e.g. `'/project/src/utils.js'`). See the [External Modules guide](/in-depth/external-modules) for how this fits into the full resolution flow.

#### Values

##### `"ifRelativeSource"` (default)

Only convert the resolved absolute ID to a relative path if the **original import specifier** was relative.

```js
// Original: relative specifier → converted to relative in output
import './lib/utils.js'; // → import './lib/utils.js'

// Original: absolute specifier → kept absolute in output
import '/project/lib/utils.js'; // → import '/project/lib/utils.js'
```

The idea: if you wrote a relative import, you probably want a relative import in the output. If you wrote an absolute import, you probably meant it to stay absolute.

##### `true`

Always convert resolved absolute IDs to relative paths:

```js
// Both become relative in output
import './lib/utils.js'; // → import './lib/utils.js'
import '/project/lib/utils.js'; // → import '../lib/utils.js'
```

When converting an absolute path to a relative path, Rolldown does *not* take the [`file`](/reference/OutputOptions.file) or [`dir`](/reference/OutputOptions.dir) options into account, because those may not be present e.g. for builds using the JavaScript API. Instead, it assumes that the root of the generated bundle is located at the common shared parent directory of all entry points.

If the output chunk is itself nested in a subdirectory by choosing e.g. `chunkFileNames: "chunks/[name].js"`, the relative path is adjusted accordingly.

##### `false`

Never convert. Resolved absolute IDs are kept as-is. Relative specifiers are also **not** normalized to absolute paths internally, which means two files importing `'./utils'` from different directories may be treated as the same external module.

```js
import './lib/utils.js'; // → import './lib/utils.js' (as-is)
import '/project/lib/utils.js'; // → import '/project/lib/utils.js' (as-is)
```

::: warning Deduplication issue with `false`
Setting `makeAbsoluteExternalsRelative: false` disables the normalization of relative specifiers. This means `'./utils'` imported from `src/a.js` and `'./utils'` imported from `src/b/c.js` may be treated as the same external module, even though they refer to different files. Use `false` only if you are certain all your external specifiers are already unique (e.g. bare package names).
:::

#### Example

Given `import '/project/lib/utils.js'` (absolute specifier) in an external module, with output at `dist/index.js`:

| `makeAbsoluteExternalsRelative` | Output path               |
| ------------------------------- | ------------------------- |
| `true`                          | `'../lib/utils.js'`       |
| `"ifRelativeSource"` (default)  | `'/project/lib/utils.js'` |
| `false`                         | `'/project/lib/utils.js'` |

Given `import './lib/utils.js'` (relative specifier) with a flat output at `dist/index.js`:

| `makeAbsoluteExternalsRelative` | Output path        |
| ------------------------------- | ------------------ |
| `true`                          | `'./lib/utils.js'` |
| `"ifRelativeSource"` (default)  | `'./lib/utils.js'` |
| `false`                         | `'./lib/utils.js'` |

The same relative specifier with a nested chunk at `dist/chunks/index.js`:

| `makeAbsoluteExternalsRelative` | Output path         |
| ------------------------------- | ------------------- |
| `true`                          | `'../lib/utils.js'` |
| `"ifRelativeSource"` (default)  | `'../lib/utils.js'` |
| `false`                         | `'./lib/utils.js'`  |

With `true` or `"ifRelativeSource"`, relative specifiers are normalized to absolute paths internally, then re-relativized from the output chunk's location — so the path adjusts correctly for nested chunks. With `false`, the raw specifier is kept as-is with no adjustment.

#### Inherited from

[`InputOptions`](Interface.InputOptions.md).[`makeAbsoluteExternalsRelative`](Interface.InputOptions.md#makeabsoluteexternalsrelative)

***

### moduleTypes?

* **Type**: [`ModuleTypes`](TypeAlias.ModuleTypes.md)
* **Optional**

Maps file patterns to module types, controlling how files are processed.

This is conceptually similar to [esbuild's `loader`](https://esbuild.github.io/api/#loader) option, allowing you to specify how each file extensions should be handled.

See [the In-Depth Guide](/in-depth/module-types) for more details.

#### Example

```js
import { defineConfig } from 'rolldown'

export default defineConfig({
  moduleTypes: {
    '.frag': 'text',
  }
})
```

#### Inherited from

[`InputOptions`](Interface.InputOptions.md).[`moduleTypes`](Interface.InputOptions.md#moduletypes)

***

### onLog()?

* **Type**: (`level`, `log`, `defaultHandler`) => `void`
* **Optional**

A function that intercepts log messages. If not supplied, logs are printed to the console.

This handler will not be invoked if logs are filtered out by the [`logLevel`](/reference/InputOptions.logLevel) option. I.e. by default, `"debug"` logs will be swallowed.

If the default handler is not invoked, the log will not be printed to the console. Moreover, you can change the log level by invoking the default handler with a different level. Using the additional level `"error"` will turn the log into a thrown error that has all properties of the log attached.

#### Parameters

##### level

`"info"` | `"debug"` | `"warn"`

##### log

[`RolldownLog`](Interface.RolldownLog.md)

##### defaultHandler

[`LogOrStringHandler`](TypeAlias.LogOrStringHandler.md)

#### Returns

`void`

#### Example

```js
export default defineConfig({
  onLog(level, log, defaultHandler) {
    if (log.code === 'CIRCULAR_DEPENDENCY') {
      return; // Ignore circular dependency warnings
    }
    if (level === 'warn') {
      defaultHandler('error', log); // turn other warnings into errors
    } else {
      defaultHandler(level, log); // otherwise, just print the log
    }
  }
})
```

#### Inherited from

[`InputOptions`](Interface.InputOptions.md).[`onLog`](Interface.InputOptions.md#onlog)

***

### ~~onwarn()?~~

* **Type**: (`warning`, `defaultHandler`) => `void`
* **Optional**

A function that will intercept warning messages.

If the default handler is invoked, the log will be handled as a warning. If both an `onLog` and `onwarn` handler are provided, the `onwarn` handler will only be invoked if `onLog` calls its default handler with a `level` of `"warn"`.

#### Parameters

##### warning

[`RolldownLog`](Interface.RolldownLog.md)

##### defaultHandler

(`warning`) => `void`

#### Returns

`void`

#### Deprecated

This is a legacy API. Consider using [`onLog`](Interface.InputOptions.md#onlog) instead for better control over all log types.

To migrate from `onwarn` to `onLog`, check the `level` parameter to filter for warnings:

```js
// Before: Using `onwarn`
export default {
  onwarn(warning, defaultHandler) {
    // Suppress certain warnings
    if (warning.code === 'CIRCULAR_DEPENDENCY') return;
    // Handle other warnings with default behavior
    defaultHandler(warning);
  },
};
```

```js
// After: Using `onLog`
export default {
  onLog(level, log, defaultHandler) {
    // Handle only warnings (same behavior as `onwarn`)
    if (level === 'warn') {
      // Suppress certain warnings
      if (log.code === 'CIRCULAR_DEPENDENCY') return;
      // Handle other warnings with default behavior
      defaultHandler(level, log);
    } else {
      // Let other log levels pass through
      defaultHandler(level, log);
    }
  },
};
```

#### Inherited from

[`InputOptions`](Interface.InputOptions.md).[`onwarn`](Interface.InputOptions.md#onwarn)

***

### optimization?

* **Type**: [`OptimizationOptions`](TypeAlias.OptimizationOptions.md)
* **Optional**

Configure optimization features for the bundler.

#### Inherited from

[`InputOptions`](Interface.InputOptions.md).[`optimization`](Interface.InputOptions.md#optimization)

***

### output?

* **Type**: [`OutputOptions`](Interface.OutputOptions.md) | [`OutputOptions`](Interface.OutputOptions.md)\[]
* **Optional**

***

### platform?

* **Type**: `"node"` | `"browser"` | `"neutral"`
* **Optional**

Expected platform where the code run.

When the platform is set to neutral:

* When bundling is enabled the default output format is set to esm, which uses the export syntax introduced with ECMAScript 2015 (i.e. ES6). You can change the output format if this default is not appropriate.
* The main fields setting is empty by default. If you want to use npm-style packages, you will likely have to configure this to be something else such as main for the standard main field used by node.
* The conditions setting does not automatically include any platform-specific values.

#### Default

* `'node'` if the format is `'cjs'`
* `'browser'` for other formats

#### Examples

##### Browser platform

```js
export default {
  platform: 'browser',
  output: {
    format: 'esm',
  },
};
```

##### Node.js platform

```js
export default {
  platform: 'node',
  output: {
    format: 'cjs',
  },
};
```

##### Platform-neutral

```js
export default {
  platform: 'neutral',
  output: {
    format: 'esm',
  },
};
```

#### In-depth

The platform setting provides sensible defaults for module resolution and environment-specific behavior, similar to esbuild's `platform` option.

##### `'node'`

Optimized for Node.js environments:

* **Conditions**: Includes `'node'`, `'import'`, `'require'` based on output format
* **Main fields**: `['main', 'module']`
* **Target**: Node.js runtime behavior
* **process.env handling**: Preserves `process.env.NODE_ENV` and other Node.js globals

##### `'browser'`

Optimized for browser environments:

* **Conditions**: Includes `'browser'`, `'import'`, `'module'`, `'default'`
* **Main fields**: `['browser', 'module', 'main']` - prefers browser-specific entry points
* **Target**: Browser runtime behavior
* **Built-ins**: Node.js built-in modules are not polyfilled by default

:::tip
For browser builds, you may want to use [rolldown-plugin-node-polyfills](https://github.com/rolldown/rolldown-plugin-node-polyfills) to polyfill Node.js built-ins if needed.
:::

##### `'neutral'`

Platform-agnostic configuration:

* **Default format**: Always `'esm'`
* **Conditions**: Only includes format-specific conditions, no platform-specific ones
* **Main fields**: Empty by default - relies on package.json `"exports"` field
* **Use cases**: Universal libraries that run in multiple environments

##### Difference from esbuild

Notable differences from esbuild's `platform` option:

* The default output format is always `'esm'` regardless of platform (in esbuild, Node.js defaults to `'cjs'`)

##### Choosing a Platform

**Use `'browser'`** when:

* Building for web applications
* Targeting modern browsers with ES modules support
* Need browser-specific package entry points

**Use `'node'`** when:

* Building server-side applications
* Creating CLI tools
* Need Node.js-specific features and modules

**Use `'neutral'`** when:

* Building universal libraries
* Want maximum portability
* Avoiding platform-specific assumptions

#### Inherited from

[`InputOptions`](Interface.InputOptions.md).[`platform`](Interface.InputOptions.md#platform)

***

### plugins?

* **Type**: [`RolldownPluginOption`](TypeAlias.RolldownPluginOption.md)
* **Optional**

The list of plugins to use.

Falsy plugins will be ignored, which can be used to easily activate or deactivate plugins. Nested plugins will be flattened. Async plugins will be awaited and resolved.

See [Plugin API document](/apis/plugin-api) for more details about creating plugins.

#### Example

```js
import { defineConfig } from 'rolldown'

export default defineConfig({
  plugins: [
    examplePlugin1(),
    // Conditional plugins
    process.env.ENV1 && examplePlugin2(),
    // Nested plugins arrays are flattened
    [examplePlugin3(), examplePlugin4()],
  ]
})
```

#### Inherited from

[`InputOptions`](Interface.InputOptions.md).[`plugins`](Interface.InputOptions.md#plugins)

***

### preserveEntrySignatures?

* **Type**: `false` | `"strict"` | `"allow-extension"` | `"exports-only"`
* **Optional**

Controls how entry chunk exports are preserved.

This determines whether Rolldown needs to create facade chunks (additional wrapper chunks) to maintain the exact export signatures of entry modules, or whether it can combine entry modules with other chunks for optimization.

#### Default

`'exports-only'`

#### Values

##### `'exports-only'`

Follows `'strict'` behavior for entry modules that have exports, but allows `'allow-extension'` behavior for entry modules without exports.

##### `'strict'`

Entry chunks will exactly match the exports of their corresponding entry modules. If additional internal bindings need to be exposed (for example, when modules are shared between chunks), Rolldown will create facade chunks to maintain the exact export signature.

**Use case:** This is the recommended setting for **libraries** where you need guaranteed, stable export signatures.

##### `'allow-extension'`

Entry chunks can expose all exports from the corresponding entry module, and may also include additional exports from other modules if they're bundled together. This allows more optimization opportunities but may expose internal implementation details.

##### `false`

Provides maximum flexibility. Entry chunks can be merged freely with other chunks regardless of export signatures. This can lead to better optimization but may change the exposed exports significantly.

**Use case:** This is the recommended setting for **application** where you don't need guaranteed, stable export signatures.

#### Understanding Facade Chunks

A facade chunk is a small wrapper chunk that Rolldown creates to preserve the exact export signature of an entry module when the actual implementation has been bundled into another chunk.

**Example scenario:**

If you have two entry points that share code, and `preserveEntrySignatures` is set to `'strict'`, Rolldown might:

1. Bundle the shared code into a common chunk
2. Create facade chunks for each entry point that re-export from the common chunk
3. This ensures each entry point maintains its exact original export signature

#### In-depth

##### Override per Entry Point

The `preserveEntrySignatures` option is a global setting. The only way to override it for individual entry chunks is to use the plugin API and emit those chunks via [`this.emitFile`](/reference/Interface.PluginContext#emitfile) instead of using the [`input`](/reference/InputOptions.input) option.

###### Practical Example: Mixed Library and Application Build

```js
// rolldown.config.js
export default {
  preserveEntrySignatures: 'exports-only', // Default for most entries
  plugins: [
    {
      name: 'custom-entries',
      buildStart() {
        // Library entry that needs strict signature preservation
        this.emitFile({
          type: 'chunk',
          id: 'src/library/index.js',
          fileName: 'library.js',
          preserveEntrySignature: 'strict',
        });

        // Application entry that can be optimized
        this.emitFile({
          type: 'chunk',
          id: 'src/app/main.js',
          fileName: 'app.js',
          preserveEntrySignature: false,
        });
      },
    },
  ],
};
```

When using `this.emitFile` with type `'chunk'`, you can specify:

* **`preserveEntrySignature`**: Override the global setting
  * `false`: Maximum optimization, merge chunks freely
  * `'strict'`: Exact export signature preservation
  * `'allow-extension'`: Allow additional exports from merged chunks
  * `'exports-only'`: Strict only for modules with exports

* **`fileName`**: Custom output filename for the entry chunk

* **`id`**: Module ID or path to use as the entry point

##### When to Use Each Setting

* **`'strict'`**: Building libraries, need guaranteed export signatures
* **`'exports-only'`**: Most applications, balanced approach (default)
* **`'allow-extension'`**: Advanced optimizations, okay with exposing extra exports
* **`false`**: Maximum bundle size reduction, export signatures don't matter

#### Inherited from

[`InputOptions`](Interface.InputOptions.md).[`preserveEntrySignatures`](Interface.InputOptions.md#preserveentrysignatures)

***

### resolve?

* **Type**: object with the properties below
* **Optional**

Options for built-in module resolution feature.

#### alias?

* **Type**: `Record`<`string`, `string` | `false` | `string`\[]>
* **Optional**

Substitute one package for another.

One use case for this feature is replacing a node-only package with a browser-friendly package in third-party code that you don't control.

##### Example

```js
resolve: {
  alias: {
    '@': '/src',
    'utils': './src/utils',
  }
}
```

> \[!WARNING]
> `resolve.alias` will not call [`resolveId`](/reference/Interface.Plugin#resolveid) hooks of other plugin.
> If you want to call `resolveId` hooks of other plugin, use `viteAliasPlugin` from `rolldown/experimental` instead.
> You could find more discussion in [this issue](https://github.com/rolldown/rolldown/issues/3615)

#### aliasFields?

* **Type**: `string`\[]\[]
* **Optional**

Fields in package.json to check for aliased paths.

This option is expected to be used for `browser` field support.

##### Default

* `[['browser']]` for `browser` platform
* `[]` for other platforms

#### conditionNames?

* **Type**: `string`\[]
* **Optional**

Condition names to use when resolving exports in package.json.

##### Default

Defaults based on platform and import kind:

* `browser` platform
  * `["import", "browser", "default"]` for import statements
  * `["require", "browser", "default"]` for require() calls
* `node` platform
  * `["import", "node", "default"]` for import statements
  * `["require", "node", "default"]` for require() calls
* `neutral` platform
  * `["import", "default"]` for import statements
  * `["require", "default"]` for require() calls

#### exportsFields?

* **Type**: `string`\[]\[]
* **Optional**

Fields in package.json to check for exports.

##### Default

`[['exports']]`

#### extensionAlias?

* **Type**: `Record`<`string`, `string`\[]>
* **Optional**

Map of extensions to alternative extensions.

With writing `import './foo.js'` in a file, you want to resolve it to `foo.ts` instead of `foo.js`.
You can achieve this by setting: `extensionAlias: { '.js': ['.ts', '.js'] }`.

#### extensions?

* **Type**: `string`\[]
* **Optional**

Extensions to try when resolving files. These are tried in order from first to last.

##### Default

`['.tsx', '.ts', '.jsx', '.js', '.json']`

#### mainFields?

* **Type**: `string`\[]
* **Optional**

Fields in package.json to check for entry points.

##### Default

Defaults based on platform:

* `node` platform: `['main', 'module']`
* `browser` platform: `['browser', 'module', 'main']`
* `neutral` platform: `[]`

#### mainFiles?

* **Type**: `string`\[]
* **Optional**

Filenames to try when resolving directories.

##### Default

```ts
['index']
```

#### modules?

* **Type**: `string`\[]
* **Optional**

Directories to search for modules.

##### Default

```ts
['node_modules']
```

#### symlinks?

* **Type**: `boolean`
* **Optional**

Whether to follow symlinks when resolving modules.

##### Default

```ts
true
```

#### ~~tsconfigFilename?~~

* **Type**: `string`
* **Optional**

##### Deprecated

Use the top-level [`tsconfig`](Interface.InputOptions.md#tsconfig) option instead.

#### Inherited from

[`InputOptions`](Interface.InputOptions.md).[`resolve`](Interface.InputOptions.md#resolve)

***

### shimMissingExports?

* **Type**: `boolean`
* **Optional**

When `true`, creates shim variables for missing exports instead of throwing an error.

#### Default

false

#### Examples

##### Enable shimming

```js
export default {
  shimMissingExports: true,
};
```

##### Example scenario

**module-a.js:**

```js
export { nonExistent } from './module-b.js';
```

**module-b.js:**

```js
// nonExistent is not actually exported here
export const something = 'value';
```

With `shimMissingExports: false` (default), this would throw an error. With `shimMissingExports: true`, Rolldown will create a shim variable:

```js
// Bundled output (simplified)
const nonExistent = undefined;
export { nonExistent, something };
```

#### Inherited from

[`InputOptions`](Interface.InputOptions.md).[`shimMissingExports`](Interface.InputOptions.md#shimmissingexports)

***

### transform?

* **Type**: [`TransformOptions`](Interface.TransformOptions.md)
* **Optional**

Configure how the code is transformed. This process happens after the `transform` hook.

#### Example

**Enable legacy decorators**

```js
export default defineConfig({
  transform: {
    decorator: {
      legacy: true,
    },
  },
})
```

Note that if you have correct `tsconfig.json` file, Rolldown will automatically detect and enable legacy decorators support.

#### In-depth

Rolldown uses Oxc under the hood for transformation.

While Oxc does not support lowering the latest decorators proposal yet, Rolldown is able to bundle them.

See [Oxc Transformer's document](https://oxc.rs/docs/guide/usage/transformer) for more details.

#### Inherited from

[`InputOptions`](Interface.InputOptions.md).[`transform`](Interface.InputOptions.md#transform)

***

### treeshake?

* **Type**: `boolean` | [`TreeshakingOptions`](TypeAlias.TreeshakingOptions.md)
* **Optional**

Controls tree-shaking (dead code elimination).

See the [In-depth Dead Code Elimination Guide](/in-depth/dead-code-elimination) for more details.

When `false`, tree-shaking will be disabled.
When `true`, it is equivalent to setting each options to the default value.

#### Default

```ts
true
```

#### Inherited from

[`InputOptions`](Interface.InputOptions.md).[`treeshake`](Interface.InputOptions.md#treeshake)

***

### tsconfig?

* **Type**: `string` | `boolean`
* **Optional**

Configures TypeScript configuration file resolution and usage.

#### Options

##### Auto-discovery mode (`true`)

When set to `true`, Rolldown enables auto-discovery mode (similar to Vite). For each module, both the resolver and transformer will find the nearest `tsconfig.json`.

If the tsconfig has `references` and certain conditions are met (the file extension is allowed and the tsconfig's `include`/`exclude` patterns don't match the file), then the referenced tsconfigs will be searched for a match. If no match is found, it falls back to the original tsconfig.

```js
export default {
  tsconfig: true,
};
```

##### Explicit path (`string`)

Specifies the path to a specific TypeScript configuration file. You may provide a relative path (resolved relative to `cwd`) or an absolute path.

If the tsconfig has `references`, this mode behaves like auto-discovery mode for reference resolution.

```js
export default {
  tsconfig: './tsconfig.json',
};
```

```js
export default {
  tsconfig: '/absolute/path/to/tsconfig.json',
};
```

:::tip
Rolldown respects `references` and `include`/`exclude` patterns in tsconfig, while esbuild does not. If you need esbuild-compatible behavior, specify a tsconfig without `references`. You can use [`extends`](https://www.typescriptlang.org/tsconfig/#extends) to share the options between the two.
:::

#### What's used from tsconfig

When a tsconfig is resolved, Rolldown uses different parts for different purposes:

##### Resolver

Uses the following for module path mapping:

* `compilerOptions.paths`: Path mapping for module resolution
* `compilerOptions.baseUrl`: Base directory for path resolution

##### Transformer

Uses select compiler options including:

* `jsx`: JSX transformation mode
* `experimentalDecorators`: Enable decorator support
* `emitDecoratorMetadata`: Emit decorator metadata
* `verbatimModuleSyntax`: Module syntax preservation
* `useDefineForClassFields`: Class field semantics
* And other TypeScript-specific options

##### Example

```json
{
  "compilerOptions": {
    "target": "ES2020",
    "module": "ESNext",
    "jsx": "react-jsx",
    "baseUrl": ".",
    "paths": {
      "@/*": ["src/*"],
      "@components/*": ["src/components/*"]
    }
  }
}
```

With this configuration:

* JSX will use React's automatic runtime
* Path aliases like `@/utils` will resolve to `src/utils`

#### Priority

Top-level `transform` options always take precedence over tsconfig settings:

```js
export default {
  tsconfig: './tsconfig.json', // Has jsx: 'react-jsx'
  transform: {
    jsx: {
      mode: 'classic', // This takes precedence
    },
  },
};
```

:::tip
For TypeScript projects, it's recommended to use `tsconfig: true` for auto-discovery or specify an explicit path to ensure consistent compilation behavior and enable path mapping.
:::

#### Default

```ts
true
```

#### Inherited from

[`InputOptions`](Interface.InputOptions.md).[`tsconfig`](Interface.InputOptions.md#tsconfig)

***

### watch?

* **Type**: `false` | [`WatcherOptions`](Interface.WatcherOptions.md)
* **Optional**
* **Experimental**

Watch mode related options.

These options only take effect when running with the [`--watch`](/apis/cli#w-watch) flag, or using [`watch()`](Function.watch.md) API.

#### Inherited from

[`InputOptions`](Interface.InputOptions.md).[`watch`](Interface.InputOptions.md#watch)
