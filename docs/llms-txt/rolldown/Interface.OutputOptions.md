# Source: https://rolldown.rs/reference/Interface.OutputOptions.md

---
url: /reference/Interface.OutputOptions.md
---
# Interface: OutputOptions

## Properties

### ~~advancedChunks?~~

* **Type**: object with the properties below
* **Optional**

#### ~~groups?~~

* **Type**: [`CodeSplittingGroup`](TypeAlias.CodeSplittingGroup.md)\[]
* **Optional**

#### ~~includeDependenciesRecursively?~~

* **Type**: `boolean`
* **Optional**

#### ~~maxModuleSize?~~

* **Type**: `number`
* **Optional**

#### ~~maxSize?~~

* **Type**: `number`
* **Optional**

#### ~~minModuleSize?~~

* **Type**: `number`
* **Optional**

#### ~~minShareCount?~~

* **Type**: `number`
* **Optional**

#### ~~minSize?~~

* **Type**: `number`
* **Optional**

#### Deprecated

Please use [`output.codeSplitting`](#codesplitting) instead.

Allows you to do manual chunking.

:::warning
If `advancedChunks` and `codeSplitting` are both specified, `advancedChunks` option will be ignored.
:::

***

### assetFileNames?

* **Type**: `string` | (`chunkInfo`) => `string`
* **Optional**

The pattern to use for naming custom emitted assets to include in the build output, or a function that is called per asset with [`PreRenderedAsset`](Interface.PreRenderedAsset.md) to return such a pattern.

Patterns support the following placeholders:

* `[extname]`: The file extension of the asset including a leading dot, e.g. `.css`.
* `[ext]`: The file extension without a leading dot, e.g. css.
* `[hash]`: A hash based on the content of the asset. You can also set a specific hash length via e.g. `[hash:10]`. By default, it will create a base-64 hash. If you need a reduced character set, see [`output.hashCharacters`](#hashcharacters).
* `[name]`: The file name of the asset excluding any extension.

Forward slashes (`/`) can be used to place files in sub-directories.

See also [`output.chunkFileNames`](#chunkfilenames), [`output.entryFileNames`](#entryfilenames).

#### Default

```ts
'assets/[name]-[hash][extname]'
```

***

### banner?

* **Type**: `string` | (`chunk`) => `string` | `Promise`<`string`>
* **Optional**

A string to prepend to the bundle before [`renderChunk`](Interface.Plugin.md#renderchunk) hook.

See [`output.intro`](#intro), [`output.postBanner`](#postbanner) as well.

:::warning

When using `output.banner` with minification enabled, the banner content may be stripped out unless it is formatted as a legal comment. To ensure your banner persists through minification, do either:

* Use [`output.postBanner`](/reference/OutputOptions.postBanner) instead, which are added after minification, or
* Use one of these comment formats:
  * Comments starting with `/*!` (e.g., `/*! My banner */`)
  * Comments containing `@license` (e.g., `/* @license My banner */`)
  * Comments containing `@preserve` (e.g., `/* @preserve My banner */`)
  * Comments starting with `//!` (for single-line comments)

The latter way's behavior is controlled by the [`output.legalComments`](/reference/OutputOptions.legalComments) option, which defaults to `'inline'` and preserves these special comment formats.

:::

#### Examples

##### Adding shebang for CLI tools

```js
export default {
  output: {
    banner: (chunk) => {
      // Add shebang only to the CLI entry point
      if (chunk.name === 'cli') {
        return '#!/usr/bin/env node';
      }
      return '';
    },
  },
};
```

##### Adding "use strict" directive

```js
export default {
  output: {
    format: 'cjs',
    banner: '"use strict";',
  },
};
```

***

### chunkFileNames?

* **Type**: `string` | (`chunkInfo`) => `string`
* **Optional**

The pattern to use for naming shared chunks created when code-splitting, or a function that is called per chunk with [`PreRenderedChunk`](Interface.PreRenderedChunk.md) to return such a pattern.

Patterns support the following placeholders:

* `[format]`: The rendering format defined in the output options. The value is any of [`InternalModuleFormat`](TypeAlias.InternalModuleFormat.md).
* `[hash]`: A hash based only on the content of the final generated chunk, including transformations in `renderChunk` and any referenced file hashes. You can also set a specific hash length via e.g. `[hash:10]`. By default, it will create a base-64 hash. If you need a reduced character set, see [`output.hashCharacters`](#hashcharacters).
* `[name]`: The name of the chunk. This can be explicitly set via the [`output.codeSplitting`](#codesplitting) option or when the chunk is created by a plugin via `this.emitFile`. Otherwise, it will be derived from the chunk contents.

Forward slashes (`/`) can be used to place files in sub-directories.

See also [`output.assetFileNames`](#assetfilenames), [`output.entryFileNames`](#entryfilenames).

#### Default

```ts
'[name]-[hash].js'
```

***

### cleanDir?

* **Type**: `boolean`
* **Optional**

Clean output directory ([`output.dir`](#dir)) before emitting output.

#### Default

false

#### Examples

##### Basic usage

```js
export default {
  output: {
    cleanDir: true,
  },
};
```

##### Multiple outputs in one config

When multiple outputs share the same directory, only set `cleanDir: true` for the first output:

```js
export default {
  output: [
    {
      dir: 'dist',
      format: 'es',
      cleanDir: true, // Clean on first output
    },
    {
      dir: 'dist',
      format: 'cjs',
      // cleanDir defaults to false, so files from first output are preserved
    },
  ],
};
```

##### Multiple configurations

When multiple configurations share the same directory, only set `cleanDir: true` for the first configuration:

```js
export default [
  {
    input: 'src/index.js',
    output: {
      dir: 'dist',
      cleanDir: true, // Clean on first configuration
    },
  },
  {
    input: 'src/other.js',
    output: {
      dir: 'dist',
      // cleanDir defaults to false, so files from first config are preserved
    },
  },
];
```

##### Different directories in multiple outputs

When multiple outputs use different directories, you can safely use `cleanDir: true` for each:

```js
export default {
  output: [
    {
      dir: 'dist/es',
      format: 'es',
      cleanDir: true, // Safe - different directory
    },
    {
      dir: 'dist/cjs',
      format: 'cjs',
      cleanDir: true, // Safe - different directory
    },
  ],
};
```

#### In-depth

##### Execution timing

The timing of the directory cleanup is important for plugin compatibility:

* The cleanup occurs **before** the `generateBundle` hook is called
* Files created by plugins during `generateBundle` or `writeBundle` hooks are **not** deleted
* This ensures that plugin-generated files are preserved even when `cleanDir` is enabled

For advanced use cases involving multiple outputs with the same `output.dir`, consider using a separate cleanup script for more control over the cleanup process.

##### ⚠️ Multiple configurations behavior

When using multiple configurations or outputs, the `cleanDir` option will be executed **separately for each configuration/output** following the order they are defined.

**The two patterns:**

* **Multiple configurations**: `export default defineConfig([{ output: { cleanDir: true, ... } }, { output: {...} }])`
* **Multiple outputs in one config**: `defineConfig({ output: [{ cleanDir: true, ... }, { ... }] })`

**The problem:**

If multiple outputs share the same `output.dir` and have `cleanDir: true`, later outputs may clean files generated by earlier outputs. This happens because each output executes its cleanup independently.

**Best practice:**

To avoid this issue, only set `cleanDir: true` for the first output, or use different output directories. This ensures that all generated files are preserved.

***

### codeSplitting?

* **Type**: `boolean` | [`CodeSplittingOptions`](TypeAlias.CodeSplittingOptions.md)
* **Optional**

Controls how code splitting is performed.

* `true`: Default behavior, automatic code splitting. **(default)**
* `false`: Inline all dynamic imports into a single bundle (equivalent to deprecated `inlineDynamicImports: true`).
* `object`: Advanced manual code splitting configuration.

For deeper understanding, please refer to the in-depth [documentation](/in-depth/manual-code-splitting).

:::warning

Be aware that manual code splitting can change the behavior of the application if side effects are triggered before the corresponding modules are actually used. You can change the chunking configuration to group some modules so that the modules are reordered, or you can use the [`output.strictExecutionOrder`](/reference/OutputOptions.strictExecutionOrder) option to ensure that modules are executed in the order they are imported with the cost of a slight increase in bundle size.

:::

#### Example

**Basic vendor chunk**

```js
export default defineConfig({
  output: {
    codeSplitting: {
      minSize: 20000,
      groups: [
        {
          name: 'vendor',
          test: /node_modules/,
        },
      ],
    },
  },
});
```

**Multiple chunk groups with priorities**

```js
export default defineConfig({
  output: {
    codeSplitting: {
      groups: [
        {
          name: 'react-vendor',
          test: /node_modules[\\/]react/,
          priority: 20,
        },
        {
          name: 'ui-vendor',
          test: /node_modules[\\/]antd/,
          priority: 15,
        },
        {
          name: 'vendor',
          test: /node_modules/,
          priority: 10,
        },
        {
          name: 'common',
          minShareCount: 2,
          minSize: 10000,
          priority: 5,
        },
      ],
    },
  },
});
```

**Size-based splitting**

```js
export default defineConfig({
  output: {
    codeSplitting: {
      groups: [
        {
          name: 'large-libs',
          test: /node_modules/,
          minSize: 100000, // 100KB
          maxSize: 250000, // 250KB
          priority: 10,
        },
      ],
    },
  },
});
```

#### Default

```ts
true
```

***

### comments?

* **Type**: `boolean` | [`CommentsOptions`](Interface.CommentsOptions.md)
* **Optional**

Control which comments are preserved in the output.

* `true`: Preserve legal, annotation, and JSDoc comments (default)
* `false`: Strip all comments
* Object: Granular control over comment categories

Note: Regular line and block comments without these markers
are always removed regardless of this option.

When both `legalComments` and `comments.legal` are set, `comments.legal` takes priority.

::: warning
Some comments may be still removed due to some known bugs: [#7257](https://github.com/rolldown/rolldown/issues/7257), [#7387](https://github.com/rolldown/rolldown/issues/7387)
:::

#### Default

```ts
true
```

***

### dir?

* **Type**: `string`
* **Optional**

The directory in which all generated chunks are placed.

The [`output.file`](#file) option can be used instead if only a single chunk is generated.

The output directory will be generated if it does not already exist, but it will not be cleared if it already contains some files. Any generated files will silently overwrite existing files with the same name. If you want the output directory to only contain files from the current run, you can use [`output.cleanDir`](/reference/OutputOptions.cleanDir) option.

#### Default

```ts
'dist'
```

***

### dynamicImportInCjs?

* **Type**: `boolean`
* **Optional**

Whether to keep external dynamic imports as `import(...)` expressions in CommonJS output.

If set to `false`, external dynamic imports will be rewritten to use `require(...)` calls.
This may be necessary to support environments that do not support dynamic `import()` in CommonJS modules like old Node.js versions.

#### Default

```ts
true
```

***

### entryFileNames?

* **Type**: `string` | (`chunkInfo`) => `string`
* **Optional**

The pattern to use for chunks created from entry points, or a function that is called per entry chunk with [`PreRenderedChunk`](Interface.PreRenderedChunk.md) to return such a pattern.

Patterns support the following placeholders:

* `[format]`: The rendering format defined in the output options. The value is any of [`InternalModuleFormat`](TypeAlias.InternalModuleFormat.md).
* `[hash]`: A hash based only on the content of the final generated chunk, including transformations in `renderChunk` and any referenced file hashes. You can also set a specific hash length via e.g. `[hash:10]`. By default, it will create a base-64 hash. If you need a reduced character set, see [`output.hashCharacters`](#hashcharacters).
* `[name]`: The file name (without extension) of the entry point, unless the object form of input was used to define a different name.

Forward slashes (`/`) can be used to place files in sub-directories. This pattern will also be used for every file when setting the [`output.preserveModules`](#preservemodules) option.

See also [`output.assetFileNames`](#assetfilenames), [`output.chunkFileNames`](#chunkfilenames).

#### Default

```ts
'[name].js'
```

***

### esModule?

* **Type**: `boolean` | `"if-default-prop"`
* **Optional**

Whether to add a `__esModule: true` property when generating exports for non-ES [formats](#format).

This property signifies that the exported value is the namespace of an ES module and that the default export of this module corresponds to the `.default` property of the exported object.

* `true`: Always add the property when using [named exports mode](#exports), which is similar to what other tools do.
* `"if-default-prop"`: Only add the property when using [named exports mode](#exports) and there also is a default export. The subtle difference is that if there is no default export, consumers of the CommonJS version of your library will get all named exports as default export instead of an error or `undefined`.
* `false`: Never add the property even if the default export would become a property `.default`.

#### Default

'if-default-prop'

#### Interaction with Consuming Tools

Different tools handle the `__esModule` marker differently when importing your bundle:

* **Rolldown**: Use heuristics based on Node.js's behavior. See the [Bundling CJS](/in-depth/bundling-cjs#ambiguous-default-import-from-cjs-modules) guide for more details.
* **esbuild**: Use heuristics based on Node.js's behavior.
* **Node.js**: Does not respect `__esModule`. The default export is the `module.exports` value.
* **Babel**: Respects `__esModule`.

***

### exports?

* **Type**: `"auto"` | `"named"` | `"default"` | `"none"`
* **Optional**

Which exports mode to use.

When `'auto'` is used, Rolldown will automatically determine the export mode based on the exports of the `input` modules. If the `input` modules have a single default export, then `'default'` mode is used. If the `input` modules have named exports, then `'named'` mode is used. If there are no exports, then `'none'` mode is used.

`'default'` can only be used when the `input` modules have a single default export. `'none'` can only be used when the `input` modules have no exports. Otherwise, Rolldown will throw an error.

The difference between `'default'` and `'named'` affects how other people can consume your bundle. If you use `'default'`, a CommonJS user could do this, for example:

```js
// your-lib package entry
export default 'Hello world';

// a CommonJS consumer
/* require( "your-lib" ) returns "Hello world" */
const hello = require('your-lib');
```

With `'named'`, a user would do this instead:

```js
// your-lib package entry
export const hello = 'Hello world';

// a CommonJS consumer
/* require( "your-lib" ) returns {hello: "Hello world"} */
const hello = require('your-lib').hello;
/* or using destructuring */
const { hello } = require('your-lib');
```

The wrinkle is that if you use `'named'` exports but also have a default export, a user would have to do something like this to use the default export:

```js
// your-lib package entry
export default 'foo';
export const bar = 'bar';

// a CommonJS consumer
/* require( "your-lib" ) returns {default: "foo", bar: "bar"} */
const foo = require('your-lib').default;
const bar = require('your-lib').bar;
/* or using destructuring */
const { default: foo, bar } = require('your-lib');
```

::: tip

There are many tools that are capable of resolving a CommonJS `require(...)` call with an ES module. If you are generating CommonJS output that is meant to be interchangeable with ESM output for those tools, you should always use `'named'` export mode. The reason is that most of those tools will by default return the namespace of an ES module on `require` where the default export is the `.default` property.

In other words for those tools, you cannot create a package interface where `const lib = require("your-lib")` yields the same as `import lib from "your-lib"`. With `'named'` export mode however, `const {lib} = require("your-lib")` will be equivalent to `import {lib} from "your-lib"`.

:::

#### Default

```ts
'auto'
```

***

### extend?

* **Type**: `boolean`
* **Optional**

Whether to extend the global variable defined by the [`name`](#name) option in `umd` or `iife` [formats](#format).

When `true`, the global variable will be defined as `global.name = global.name || {}`.
When `false`, the global defined by name will be overwritten like `global.name = {}`.

#### Default

```ts
false
```

***

### externalLiveBindings?

* **Type**: `boolean`
* **Optional**

Whether to generate code to support live bindings for [external](Interface.InputOptions.md#external) imports.

With the default value of `true`, Rolldown will generate code to support live bindings for external imports.

When set to `false`, Rolldown will assume that exports from external modules do not change. This will allow Rolldown to generate smaller code. Note that this can cause issues when there are circular dependencies involving an external dependency.

#### Default

true

#### Example

```js
// input
export { x } from 'external';
```

```js
// CJS output with externalLiveBindings: true
var external = require('external');

Object.defineProperty(exports, 'x', {
  enumerable: true,
  get: function () {
    return external.x;
  },
});
```

```js
// CJS output with externalLiveBindings: false
var external = require('external');

exports.x = external.x;
```

***

### file?

* **Type**: `string`
* **Optional**

The file path for the single generated chunk.

The [`output.dir`](#dir) option should be used instead if multiple chunks are generated.

***

### footer?

* **Type**: `string` | (`chunk`) => `string` | `Promise`<`string`>
* **Optional**

A string to append to the bundle before [`renderChunk`](Interface.Plugin.md#renderchunk) hook.

See [`output.outro`](#outro), [`output.postFooter`](#postfooter) as well.

:::warning

When using `output.footer` with minification enabled, the footer content may be stripped out unless it is formatted as a legal comment. To ensure your footer persists through minification, do either:

* Use [`output.postFooter`](/reference/OutputOptions.postFooter) instead, which is added after minification, or
* Use one of these comment formats:
  * Comments starting with `/*!` (e.g., `/*! My footer */`)
  * Comments containing `@license` (e.g., `/* @license My footer */`)
  * Comments containing `@preserve` (e.g., `/* @preserve My footer */`)
  * Comments starting with `//!` (for single-line comments)

The latter way's behavior is controlled by the [`output.legalComments`](/reference/OutputOptions.legalComments) option, which defaults to `'inline'` and preserves these special comment formats.

:::

#### Examples

##### Expose the default export as `module.exports` for CJS output with all named exports as properties

```js
export default {
  output: {
    format: 'cjs',
    exports: 'named',
    footer: (chunk) => {
      if (chunk.isEntry) {
        return `
module.exports = exports.default;
module.exports.default = module.exports;
module.exports.foo = module.exports.default.foo;`;
      }
      return '';
    },
  },
};
```

***

### format?

* **Type**: `"es"` | `"cjs"` | `"iife"` | `"umd"` | `"module"` | `"esm"` | `"commonjs"`
* **Optional**

Expected format of generated code.

* `'es'`, `'esm'` and `'module'` are the same format, all stand for ES module.
* `'cjs'` and `'commonjs'` are the same format, all stand for CommonJS module.
* `'iife'` stands for [Immediately Invoked Function Expression](https://developer.mozilla.org/en-US/docs/Glossary/IIFE).
* `'umd'` stands for [Universal Module Definition](https://github.com/umdjs/umd).

#### Default

'es'

#### In-depth

##### ES Module

[ES modules](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules) (ESM) are the official JavaScript module standard. When `output.format: 'es'` is used, the bundle will use `export` syntax like this:

```js
function exportedFunction() {
  /* ... */
}
let exportedValue = '/* ... */';

export { exportedFunction, exportedValue };
```

To load ES modules, use `<script type="module">` in browsers, or `.mjs` extension (or `"type": "module"` in package.json) in Node.js. See [Node.js ES modules documentation](https://nodejs.org/api/esm.html#enabling) for details.

ES modules are the recommended format for most use cases. They are part of the JavaScript specification, work across browsers and Node.js, and enable static analysis for tree-shaking and other optimizations.

##### CommonJS Module

[CommonJS](https://nodejs.org/docs/latest/api/modules.html#modules-commonjs-modules) is the module format that Node.js originally supported before ES modules. When `output.format: 'cjs'` is used, the bundle will use `exports` variable like this:

```js
function exportedFunction() {
  /* ... */
}
let exportedValue = '/* ... */';

exports.exportedFunction = exportedFunction;
exports.exportedValue = exportedValue;
```

Entry points with ES module exports will be converted to use getters on `exports` to preserve [live binding semantics](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import#imported_values_can_only_be_modified_by_the_exporter).

CommonJS is useful when targeting Node.js environments that don't support ES modules, or when integrating with older packages that expect CommonJS. For most use cases, `es` format is preferred because it's the JavaScript standard, has better interoperability across environments, and enables static analysis for tree-shaking.

##### IIFE

IIFE stands for ["immediately-invoked function expression"](https://developer.mozilla.org/en-US/docs/Glossary/IIFE). When `output.format: 'iife'` is used, the bundle will be wrapped with an IIFE like this (assuming [`output.name: 'MyLibrary'`](/reference/OutputOptions.name) is set):

```js
var MyLibrary = (function () {
  function exportedFunction() {
    /* ... */
  }
  let exportedValue = '/* ... */';

  return { exportedFunction, exportedValue };
})();
```

When using `<script>` tags without `type="module"`, code executes in the global scope, which means variables from different scripts can conflict with each other. IIFE solves this by creating a private function scope that encapsulates all internal variables, while exposing only a single global variable (e.g., `jQuery`, `_`, `React`).

IIFE is useful for drop-in scripts and widgets that need to work anywhere with a single `<script>` tag, or for libraries that want to expose one clean global (like analytics snippets or embeddable widgets). For most use cases, especially libraries, `es` format is preferred because it's the JavaScript standard, has better interoperability across environments, and enables static analysis for tree-shaking.

##### UMD

[Universal Module Definition](https://github.com/umdjs/umd) is a pattern that works across multiple environments: [AMD](https://github.com/amdjs/amdjs-api/blob/master/AMD.md) (RequireJS), CommonJS (Node.js), and browser globals. When `output.format: 'umd'` is used, the bundle will be wrapped with code that detects the environment like this (assuming [`output.name: 'MyLibrary'`](/reference/OutputOptions.name) is set):

```js
(function (global, factory) {
  typeof exports === 'object' && typeof module !== 'undefined'
    ? factory(exports)
    : typeof define === 'function' && define.amd
      ? define(['exports'], factory)
      : ((global = typeof globalThis !== 'undefined' ? globalThis : global || self),
        factory((global.myBundle = {})));
})(this, function (exports) {
  function exportedFunction() {
    /* ... */
  }
  let exportedValue = '/* ... */';

  exports.exportedFunction = exportedFunction;
  exports.exportedValue = exportedValue;
});
```

UMD was popular before ES modules became widely supported, as it allowed a single build to work everywhere. Today, UMD is largely unnecessary as ES modules are supported in all modern browsers and Node.js, and bundlers handle module interop automatically. The format also adds runtime overhead and is harder to statically analyze. For new projects, use `es` format instead.

***

### generatedCode?

* **Type**: `Partial`<[`GeneratedCodeOptions`](Interface.GeneratedCodeOptions.md)>
* **Optional**

Which language features Rolldown can safely use in generated code.

This will not transpile any user code but only change the code Rolldown uses in wrappers and helpers.

***

### globals?

* **Type**: `Record`<`string`, `string`> | (`name`) => `string`
* **Optional**

Specifies `id: variableName` pairs necessary for [external](Interface.InputOptions.md#external) imports in `umd` / `iife` [formats](#format).

#### Example

```js
export default defineConfig({
  external: ['jquery'],
  output: {
    format: 'iife',
    name: 'MyBundle',
    globals: {
      jquery: '$',
    }
  }
});
```

```js
// input
import $ from 'jquery';
```

```js
// output
var MyBundle = (function ($) {
  // ...
})($);
```

***

### hashCharacters?

* **Type**: `"base64"` | `"base36"` | `"hex"`
* **Optional**

Specify the character set that Rolldown is allowed to use in file hashes.

* `'base64'`: Uses url-safe base64 characters (0-9, a-z, A-Z, -, \_). This will produce the shortest hashes.
* `'base36'`: Uses alphanumeric characters (0-9, a-z)
* `'hex'`: Uses hexadecimal characters (0-9, a-f)

#### Default

```ts
'base64'
```

***

### ~~inlineDynamicImports?~~

* **Type**: `boolean`
* **Optional**

#### Deprecated

Please use `codeSplitting: false` instead.

Whether to inline dynamic imports instead of creating new chunks to create a single bundle.

This option can be used only when a single input is provided.

#### Default

```ts
false
```

***

### intro?

* **Type**: `string` | (`chunk`) => `string` | `Promise`<`string`>
* **Optional**

A string to prepend inside any [format](#format)-specific wrapper.

See [`output.banner`](#banner), [`output.postBanner`](#postbanner) as well.

The variables declared in `intro` are scoped to the bundle and won't pollute the global scope. For example, with `format: 'iife'`:

```js
// banner is placed here, outside the IIFE (global scope)
var MyBundle = (function () {
  // intro is placed here, inside the IIFE (local scope)
  var __DEV__ = true; // This won't leak to global scope

  // ... bundle code ...

  // outro is placed here
})();
// footer is placed here
```

#### Examples

##### Polyfilling globalThis

```js
export default {
  output: {
    intro: `
var globalThis = (function() {
  if (typeof globalThis !== 'undefined') return globalThis;
  if (typeof self !== 'undefined') return self;
  if (typeof window !== 'undefined') return window;
  if (typeof global !== 'undefined') return global;
  throw new Error('Unable to locate global object');
})();`,
  },
};
```

***

### keepNames?

* **Type**: `boolean`
* **Optional**

Keep `name` property of functions and classes after bundling.

When enabled, the bundler will preserve the original `name` property value of functions and
classes in the output. This is useful for debugging and some frameworks that rely on it for
registration and binding purposes.

Consider the following input files:

::: code-group

```js [lib.js]
export class Test {}
console.log(Test.name); // Expected: "Test"

export function test() {}
console.log(test.name); // Expected: "test"
```

```js [main.js (entry)]
import { Test as T, test as t } from './lib';

export class Test extends T {}

export function test() {}
```

:::

Output with `keepNames: false` (default):

```js
var Test$1 = class {};
console.log(Test$1.name); // "Test$1" - not the original name!
function test$1() {}
console.log(test$1.name); // "test$1" - not the original name!

var Test = class extends Test$1 {};
function test() {}

export { Test, test };
```

Output with `keepNames: true`:

```js
// NOTE: `__name` is a helper function that sets `name` property

var Test$1 = class {
  static {
    __name(this, 'Test');
  }
};
console.log(Test$1.name); // "Test" - preserved!
function test$1() {}
__name(test$1, 'test');
console.log(test$1.name); // "test" - preserved!

var Test = class extends Test$1 {};
function test() {}

export { Test, test };
```

#### Default

```ts
false
```

***

### ~~legalComments?~~

* **Type**: `"none"` | `"inline"`
* **Optional**

Controls how legal comments are preserved in the output.

* `none`: no legal comments
* `inline`: preserve legal comments that contain `@license`, `@preserve` or starts with `//!` `/*!`

#### Deprecated

Use `comments.legal` instead. When both `legalComments` and `comments.legal` are set, `comments.legal` takes priority.

***

### ~~manualChunks()?~~

* **Type**: (`moduleId`, `meta`) => `string` | `undefined` | `null` | `void`
* **Optional**

Allows you to do manual chunking. Provided for Rollup compatibility.

You could use this option for migration purpose. Under the hood,

```js
{
  manualChunks: (moduleId, meta) => {
    if (moduleId.includes('node_modules')) {
      return 'vendor';
    }
    return null;
  }
}
```

will be transformed to

```js
{
  codeSplitting: {
    groups: [
      {
        name(moduleId) {
          if (moduleId.includes('node_modules')) {
            return 'vendor';
          }
          return null;
        },
      },
    ],
  }
}

```

Note that unlike Rollup, object form is not supported.

#### Parameters

##### moduleId

`string`

##### meta

###### getModuleInfo

(`moduleId`) => [`ModuleInfo`](Interface.ModuleInfo.md) | `null`

#### Returns

`string` | `undefined` | `null` | `void`

#### Deprecated

Please use [`output.codeSplitting`](#codesplitting) instead.

:::warning
If `manualChunks` and `codeSplitting` are both specified, `manualChunks` option will be ignored.
:::

***

### minify?

* **Type**: `boolean` | [`MinifyOptions`](TypeAlias.MinifyOptions.md) | `"dce-only"`
* **Optional**

Control code minification

Rolldown uses Oxc Minifier under the hood. See Oxc's [minification documentation](https://oxc.rs/docs/guide/usage/minifier#features) for more details.

* `true`: Enable full minification including code compression and dead code elimination
* `false`: Disable minification
* `'dce-only'`: Only perform dead code elimination without code compression (default)
* `MinifyOptions`: Fine-grained control over minification settings

#### Default

```ts
'dce-only'
```

***

### minifyInternalExports?

* **Type**: `boolean`
* **Optional**

Whether to minify internal exports as single letter variables to allow for better minification.

#### Default

`true` for format `es` or if `output.minify` is `true` or object, `false` otherwise

#### In-depth

For example, if you have the following code:

```js
// main.js
import './lib.js';

// lib.js
import('./dynamic.js');
export const importantValue = 42;

// dynamic.js
import { importantValue } from './lib.js';
console.log(importantValue);
```

The output with `minifyInternalExports: false` will be:

```js
// main.js
import('./dynamic-CCJ-yTfk.js');
const importantValue = 42;

export { importantValue };

// dynamic-CCJ-yTfk.js
import { importantValue } from './index.js';

console.log(importantValue);
```

On the other hand, the output with `minifyInternalExports: true` will be:

```js
// main.js
import('./dynamic-CCJ-yTfk.js');
const importantValue = 42;

export { importantValue as t };

// dynamic-CCJ-yTfk.js
import { t as importantValue } from './index.js';

console.log(importantValue);
```

Even though it appears that setting this option to `true` makes the output larger, it actually makes it smaller if a minifier is used. In this case, `export { importantValue as t }` can become e.g., `export{t as e}` or even `export{t}`, while otherwise it would produce `export{ a as importantValue }` because a minifier usually will not change export signatures.

***

### name?

* **Type**: `string`
* **Optional**

Specifies the global variable name that contains the exports of `umd` / `iife` [formats](#format).

#### Example

```js
export default defineConfig({
  output: {
    format: 'iife',
    name: 'MyBundle',
  }
});
```

```js
// output
var MyBundle = (function () {
  // ...
})();
```

Namespaces are supported i.e., your name can contain dots. The resulting bundle will contain the setup necessary for the namespacing.

```js
// output for `name: 'a.b.c'`
this.a = this.a || {};
this.a.b = this.a.b || {};
this.a.b.c = (function () {
  // ...
})();
```

***

### outro?

* **Type**: `string` | (`chunk`) => `string` | `Promise`<`string`>
* **Optional**

A string to append inside any [format](#format)-specific wrapper.

See [`output.footer`](#footer), [`output.postFooter`](#postfooter) as well.

This means `outro` code has access to the bundle's internal scope and can reference private variables and functions. For example, with `format: 'iife'`:

```js
// banner is placed here
var MyBundle = (function () {
  // intro is placed here
  var privateVar = 'internal'; // Only accessible inside IIFE

  // ... bundle code ...

  // outro is placed here - can access privateVar
  console.log(privateVar); // Works!
})();
// footer is placed here (global scope) - cannot access privateVar
```

#### Examples

##### Freeze exports

```js
export default {
  output: {
    format: 'iife',
    name: 'MyLib',
    outro: `
// Freeze the exported API to prevent modifications
if (typeof Object.freeze === 'function') {
  Object.freeze(exports);
}`,
  },
};
```

***

### paths?

* **Type**: `Record`<`string`, `string`> | (`id`) => `string`
* **Optional**

Maps [external](Interface.InputOptions.md#external) module IDs to paths.

Allows customizing the path used when importing external dependencies.
This is particularly useful for loading dependencies from CDNs or custom locations.

* Object form: Maps module IDs to their replacement paths
* Function form: Takes a module ID and returns its replacement path

#### Examples

```js
{
  paths: {
    'd3': 'https://cdn.jsdelivr.net/npm/d3@7'
  }
}
```

```js
{
  paths: (id) => {
    if (id.startsWith('lodash')) {
      return `https://cdn.jsdelivr.net/npm/${id}`
    }
    return id
  }
}
```

***

### plugins?

* **Type**: `RolldownOutputPluginOption`
* **Optional**

The list of plugins to use only for this output.

#### See

[`plugins`](Interface.InputOptions.md#plugins)

***

### polyfillRequire?

* **Type**: `boolean`
* **Optional**

Whether to add a polyfill for `require()` function in non-CommonJS formats.

This option is useful when you want to inject your own `require` implementation.

#### Default

```ts
true
```

***

### postBanner?

* **Type**: `string` | (`chunk`) => `string` | `Promise`<`string`>
* **Optional**

A string to prepend to the bundle after [`renderChunk`](Interface.Plugin.md#renderchunk) hook and minification.

See [`output.banner`](#banner), [`output.intro`](#intro) as well.

#### Examples

##### Adding build info

```js
import pkg from './package.json' with { type: 'json' };
import { execSync } from 'node:child_process';

const gitHash = execSync('git rev-parse --short HEAD').toString().trim();

export default {
  output: {
    minify: true,
    postBanner: `/* ${pkg.name}@${pkg.version} (${gitHash}) */`,
  },
};
```

***

### postFooter?

* **Type**: `string` | (`chunk`) => `string` | `Promise`<`string`>
* **Optional**

A string to append to the bundle after [`renderChunk`](Interface.Plugin.md#renderchunk) hook and minification.

See [`output.footer`](#footer), [`output.outro`](#outro) as well.

#### Examples

##### Build timestamp

```js
export default {
  output: {
    minify: true,
    postFooter: `/* built: ${Date.now()} */`,
  },
};
```

***

### preserveModules?

* **Type**: `boolean`
* **Optional**

Whether to use preserve modules mode.

Instead of creating as few chunks as possible, this mode will create separate chunks for all modules using the original module names as file names. Tree-shaking will still be applied, suppressing files that are not used by the provided entry points or do not have side effects when executed and removing unused exports of files that are not entry points. On the other hand, if plugins emit additional "virtual" files to achieve certain results, those files will be emitted as actual files using a pattern [`${output.virtualDirname}/fileName.js`](/reference/OutputOptions.virtualDirname).

It is therefore not recommended to blindly use this option to transform an entire file structure to another format if you directly want to import from those files as expected exports may be missing. In that case, you should rather designate all files explicitly as entry points by adding them to the [`input`](/reference/InputOptions.input) option object. See the [glob pattern example](/reference/InputOptions.input#in-depth) for how to do this dynamically.

#### Default

```ts
false
```

***

### preserveModulesRoot?

* **Type**: `string`
* **Optional**

A directory path to input modules that should be stripped away from [`output.dir`](#dir) when using [preserve modules mode](#preservemodules).

This option is particularly useful when the output directory structure may change. This can happen when third-party modules are not marked [`external`](/reference/InputOptions.external), or while developing in a monorepo of multiple packages that rely on one another and are not marked [`external`](/reference/InputOptions.external).

#### Examples

```js
import { defineConfig } from 'rolldown';

export default defineConfig({
  input: ['src/module.js', `src/another/module.js`],
  output: {
    dir: 'dist',
    preserveModules: true,
    preserveModulesRoot: 'src',
  },
});
```

This setting ensures that the input modules will be output to the paths `dist/module.js` and `dist/another/module.js`.

***

### sanitizeFileName?

* **Type**: `boolean` | (`name`) => `string`
* **Optional**

Whether to enable chunk name sanitization (removal of non-URL-safe characters like `\0`, `?` and `*`).

Set `false` to disable the sanitization. You can also provide a custom sanitization function.

#### Default

```ts
true
```

***

### sourcemap?

* **Type**: `boolean` | `"inline"` | `"hidden"`
* **Optional**

Whether to generate sourcemaps.

* `false`: No sourcemap will be generated.
* `true`: A separate sourcemap file will be generated.
* `'inline'`: The sourcemap will be appended to the output file as a data URL.
* `'hidden'`: A separate sourcemap file will be generated, but the link to the sourcemap (`//# sourceMappingURL` comment) will not be included in the output file.

#### Default

```ts
false
```

***

### sourcemapBaseUrl?

* **Type**: `string`
* **Optional**

The base URL for the links to the sourcemap file in the output file.

By default, relative URLs are generated. If this option is set, an absolute URL with that base URL will be generated. This is useful when deploying source maps to a different location than your code, such as a CDN or separate debugging server.

***

### sourcemapDebugIds?

* **Type**: `boolean`
* **Optional**

Whether to include [debug IDs](https://github.com/tc39/ecma426/blob/main/proposals/debug-id.md) in the sourcemap.

When `true`, a unique debug ID will be emitted in source and sourcemaps which streamlines identifying sourcemaps across different builds.

#### Default

```ts
false
```

***

### sourcemapIgnoreList?

* **Type**: `boolean` | `string` | `RegExp` | (`relativeSourcePath`, `sourcemapPath`) => `boolean`
* **Optional**

Control which source files are included in the sourcemap ignore list.

Files in the ignore list are excluded from debugger stepping and error stack traces.

* `false`: Include no source files in the ignore list
* `true`: Include all source files in the ignore list
* `string`: Files containing this string in their path will be included in the ignore list
* `RegExp`: Files matching this regular expression will be included in the ignore list
* `function`: Custom function to determine if a source should be ignored

:::tip Performance
Using static values (`boolean`, `string`, or `RegExp`) is significantly more performant than functions.
Calling JavaScript functions from Rust has extremely high overhead, so prefer static patterns when possible.
:::

#### Type Declaration

`boolean`

`string` | `RegExp`

(`relativeSourcePath`, `sourcemapPath`) => `boolean`

#### Parameters

##### relativeSourcePath

`string`

The relative path from the generated `.map` file to the corresponding source file.

##### sourcemapPath

`string`

The fully resolved path of the generated sourcemap file.

#### Returns

`boolean`

#### Example

```js
// ✅ Preferred: Use RegExp for better performance
sourcemapIgnoreList: /node_modules/

// ✅ Preferred: Use string pattern for better performance
sourcemapIgnoreList: "vendor"

// ! Use sparingly: Function calls have high overhead
sourcemapIgnoreList: (source, sourcemapPath) => {
  return source.includes('node_modules') || source.includes('.min.');
}
```

#### Default

```ts
/node_modules/
```

***

### sourcemapPathTransform()?

* **Type**: (`relativeSourcePath`, `sourcemapPath`) => `string`
* **Optional**

A transformation to apply to each path in a sourcemap.

#### Parameters

##### relativeSourcePath

`string`

The relative path from the generated `.map` file to the corresponding source file.

##### sourcemapPath

`string`

The fully resolved path of the generated sourcemap file.

#### Returns

`string`

#### Example

```js
export default defineConfig({
  output: {
    sourcemap: true,
    sourcemapPathTransform: (source, sourcemapPath) => {
      // Remove 'src/' prefix from all source paths
      return source.replace(/^src//, '');
    },
  },
});
```

***

### strict?

* **Type**: `boolean` | `"auto"`
* **Optional**

Whether to always output `"use strict"` directive in non-ES module outputs.

* `true` - Always emit `"use strict"` at the top of the output (not applicable for ESM format since ESM is always strict).
* `false` - Never emit `"use strict"` in the output.
* `'auto'` - Respect the `"use strict"` directives from the source code.

See [In-depth directive guide](/in-depth/directives) for more details.

#### Default

```ts
'auto'
```

***

### strictExecutionOrder?

* **Type**: `boolean`
* **Optional**

Lets modules be executed in the order they are declared.

This is done by injecting runtime helpers to ensure that modules are executed in the order they are imported. External modules won't be affected.

> \[!WARNING]
> Enabling this option may negatively increase bundle size. It is recommended to use this option only when absolutely necessary.

#### Default

```ts
false
```

***

### topLevelVar?

* **Type**: `boolean`
* **Optional**

Whether to use `var` declarations at the top level scope instead of function / class / let / const expressions.

Enabling this option can improve runtime performance of the generated code in certain environments.

#### Default

false

#### In-depth

Multiple JavaScript engines have had and continue to have performance issues with [Temporal dead zone (TDZ)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let#temporal_dead_zone_tdz) checks. These checks validate that a let, const, or class symbol isn't used before it's initialized.

Related issues:

* V8: https://issues.chromium.org/issues/42203665
* JavaScriptCore: https://bugs.webkit.org/show\_bug.cgi?id=199866 (fixed)

***

### virtualDirname?

* **Type**: `string`
* **Optional**

Specifies the directory name for "virtual" files that might be emitted by plugins when using [preserve modules mode](#preservemodules).

#### Default

```ts
'_virtual'
```
