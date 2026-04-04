# Source: https://rspack.dev/api/runtime-api/module-variables.md

CC 4.0 License> The content of this section is derived from the content of the following links and is subject to the CC BY 4.0 license.
> 
> - [https://webpack.js.org/api/module-variables/](https://webpack.js.org/api/module-variables/)
> 
> The following contents can be assumed to be the result of modifications and deletions based on the original contents if not specifically stated.
> 
> 


# Module variables

This section covers all variables available in code compiled with Rspack. Modules will be able to access specific data from the compilation process through `module` and other variables.

## CommonJS

### module.loaded

`false` means that the module is being executed, `true` the synchronous execution has been completed.

### module.id

Current module ID.

```js title=src/main.js
module.id === require.resolve('./src/main.js'); // true
```

### module.hot

Indicates whether or not hot module replacement is enabled and provides an interface to the process. See the [HMR API page](/api/runtime-api/hmr.md) for details.

### global

See [node.js global](https://nodejs.org/api/globals.html#globals_global) for details.

Rspack will replace the global with a proxy object and handle compatibility issues in it.

```js title=Source
global['property']
```
```js title=Compiled
__webpack_require__.g['property'];

// webpack/runtime/global
__webpack_require__.g = (function () {
  // compatibility code
})();
```

### \_\_filename

Depends on the configuration [`node.__filename`](/config/node.md#node__filename).

- `false`: undefined
- `mock`: equal to `'/index.js'`
- `true`: [NodeJs \_\_filename](https://nodejs.org/api/modules.html#__filename)

If used inside an expression that is parsed by the Parser, the configuration option is treated as `true`.

```js title=Source
__filename
```
```js title=Compiled
'src/main.js';
```

### \_\_dirname

Depends on the configuration [`node.__dirname`](/config/node.md#node__dirname).

- `false`: undefined
- `mock`: equal to `'/index.js'`
- `true`: [NodeJs \_\_dirname](https://nodejs.org/api/modules.html#__dirname)

If used inside an expression that is parsed by the Parser, the configuration option is treated as `true`.

```js title=Source
__dirname
```
```js title=Compiled
'src';
```

## import.meta (ESM)

The `import.meta` exposes context-specific metadata to a JavaScript module, such as the URL of the module. It is only available in ESM.

> Please note that Rspack does not support direct access to `import.meta`. Instead, you should access its properties or use destructuring assignment. E.g.,

```js title="Source"
import.meta
typeof import.meta
```
```js title="Compiled"
{
} // Warning: Direct access to import.meta is not supported (only property access or destructuring is supported)
('object');
```

### import.meta.url

Returns the absolute `file:` URL of the module.

```js title=Source
import.meta.url
typeof import.meta.url
```
```js title=Compiled
'file://project_root/src/main.js';
'string';
```

### import.meta.webpackContext

Rspack/Webpack specific
`import.meta.webpackContext` is a function specific to webpack that allows you to dynamically import a set of modules.

You can use `import.meta.webpackContext` in your code, and Rspack will parse and reference the matching modules during the build process.

- **Type:**

```ts
function webpackContext(
  /**
   * A directory to search.
   */
  request: string,
  options?: {
    /**
     * Whether subdirectories should be searched.
     * @default true
     */
    recursive?: boolean;
    /**
     * A regular expression to match files.
     * @default /^\.\/.*$/ (any file)
     */
    regExp?: RegExp;
    /**
     * Module loading mode.
     * @default 'sync'
     */
    mode?: 'sync' | 'eager' | 'weak' | 'lazy' | 'lazy-once';
    include?: RegExp;
    exclude?: RegExp;
    preload?: boolean | number;
    prefetch?: boolean | number;
    chunkName?: string;
    exports?: string | string[][];
  },
): Context;
```

- **Example:**

```js
// Create a context, with files from the test directory that
// can be required with a module specifier ending with `.test.js`.
const context = import.meta.webpackContext('./test', {
  recursive: false,
  regExp: /\.test\.js$/,
});
```

```js
// Create a context with all files in the parent folder and
// descending folders ending with `.stories.js`.
const context = import.meta.webpackContext('../', {
  recursive: true,
  regExp: /\.stories\.js$/,
});
```

```js
// If mode is set to 'lazy', the underlying modules will be loaded asynchronously
const context = import.meta.webpackContext('./locales', {
  recursive: true,
  regExp: /\.json$/,
  mode: 'lazy',
});
```

:::tip
Rspack uses static analysis to parse the parameters of `import.meta.webpackContext()` during compilation. Therefore, the parameters must be [literals](https://developer.mozilla.org/en-US/docs/Glossary/Literal).

For example, the value of `regExp` cannot be a variable, nor can it be the value generated by `new RegExp()`. It can only be a regular expression literal.
:::

### context API

The context returned by `import.meta.webpackContext()` is a function that takes a `request` argument (module path).

This function has three properties: `resolve`, `keys`, and `id`.

- `resolve` is a function and returns the module id of the parsed module specifier.
- `keys` is a function that returns an array of all possible requests that the context module can handle.
- `id` is the module id of the context module. This may be useful for `module.hot.accept`.

This can be useful if you want to require all files in a directory or matching a pattern.

Consider a scenario where you have a folder structure like this:

```
src
├── components
│   ├── Button.js
│   ├── Header.js
│   └── Footer.js
```

You can use `import.meta.webpackContext()` to dynamically import all component files in the folder:

```js
const componentsContext = import.meta.webpackContext('./components', {
  recursive: false,
  regExp: /\.js$/,
});

componentsContext.keys().forEach((fileName) => {
  const componentModule = componentsContext(fileName);

  // Here you can use your module, for example console.log
  console.log(componentModule);
});
```

`import.meta.webpackContext()` streamlines the process of module importation especially when you have a lot of files to manage. When using it, please avoid matching unnecessary files, as this might lead to significantly increased build time and output size.

### import.meta.webpackHot

Rspack/Webpack specific
An alias for [`module.hot`](#modulehot), however `import.meta.webpackHot` can be used in strict ESM while `module.hot` can't.

## Runtime

### \_\_webpack\_hash\_\_

Rspack/Webpack specific
It provides access to the hash of the compilation.

```js title=Source
__webpack_hash__
```
```js title=Compiled
__webpack_require__.h();

// webpack/runtime/get_full_hash
__webpack_require__.h = function () {
  return '9210c6f859a51c6f9a62';
};
```

### \_\_webpack\_runtime\_id\_\_

Rspack/Webpack specific
Access the runtime id of current entry.

```js title=Source
__webpack_runtime_id__
```
```js title=Compiled
__webpack_require__.j;

// webpack/runtime/runtime_id
__webpack_require__.j = '909';
```

### \_\_webpack\_public\_path\_\_

Rspack/Webpack specific
Equals the configuration option's [`output.publicPath`](/config/output.md#outputpublicpath).

```js title=Source
__webpack_public_path__
```
```js title=Compiled
__webpack_require__.p;

// output.publicPath !== "auto"
__webpack_require__.p = 'output.publicPath';
// output.publicPath === "auto"
__webpack_require__.p = 'calculated from document/location';
```

> See [Dynamically set publicPath](/guide/features/asset-base-path.md#dynamically-set-publicpath) for more information about the usage of `__webpack_public_path__`.

### \_\_webpack\_base\_uri\_\_

Rspack/Webpack specific
Get or change base URI at runtime.

```js title=Source
__webpack_base_uri__
```
```js title=Compiled
__webpack_require__.b;

// chunk loading
__webpack_require__.b = document.baseURI || self.location.href;
```

### \_\_webpack\_nonce\_\_

Rspack/Webpack specific
Rspack is capable of adding a nonce to all scripts that it loads.
To activate this feature, set a `__webpack_nonce__` variable and include it in your entry script.

```js title=Source
__webpack_nonce__ = 'your_nonce_code';
```
```js title=Compiled
__webpack_require__.nc = '2312312';

// webpack/runtime/load_script
if (__webpack_require__.nc) {
  script.setAttribute('nonce', __webpack_require__.nc);
}
```

## Modules

### \_\_webpack\_modules\_\_

Rspack/Webpack specific
Access to the internal object of all modules.

```js title=Source
__webpack_modules__
```
```js title=Compiled
var __webpack_modules__ = {
  'main.js': function () {
    __webpack_require__.m;
  },
};
__webpack_require__.m = __webpack_modules__;
```

### \_\_webpack\_module\_\_

Rspack/Webpack specific
It provides access to the the current `module`. `module` is not available in strict ESM.

```js title=Source
__webpack_module__
```
```js title=Compiled
"main.js": function(renamed_module) {
  renamed_module
}
```

### \_\_webpack\_module\_\_.id

Rspack/Webpack specific
It provides access to the ID of current module (`module.id`). `module` is not available in strict ESM.

```js title=Source
__webpack_module__.id
```
```js title=Compiled
"main.js": function(renamed_module) {
  renamed_module.id
}
```

### \_\_webpack\_require\_\_

Rspack/Webpack specific
The raw require function.
This expression isn't parsed by the Parser for dependencies.

```js title=Source
__webpack_require__('./dep.js')
```
```js title=Compiled
"main.js": function(_, __, renamed_require) {
  renamed_require('./dep.js')
}
```

### \_\_non\_webpack\_require\_\_

Rspack/Webpack specific
Generates a `require` function that is not parsed by webpack.
Can be used to do cool stuff with a global require function if available.

```js title=Source
__non_webpack_require__('outer.js')
```
```js title=Compiled
"main.js": function(_, __, __webpack_require__) {
  require('outer.js')
}
```

### \_\_webpack\_is\_included\_\_

Rspack/Webpack specific
Test whether or not the given module is bundled by webpack.

```js title=Source
if (__webpack_is_included__('./dep.js')) {
  // do something
}
```
```js title=Compiled
if (true) {
  // do something
}
```

### \_\_resourceQuery

Rspack/Webpack specific
The resource query of the current module.
If the following `require` call was made, then the query string would be available in `file.js`.

```js
require('file.js?test');
```

```js title=Source
__resourceQuery
```
```js title=Compiled
'?test';
```

### \_\_webpack\_exports\_info\_\_

[Added in v1.0.0](https://github.com/web-infra-dev/rspack/releases/tag/v1.0.0)Rspack/Webpack specific
In modules, `__webpack_exports_info__` is available to allow exports introspection:

- `__webpack_exports_info__` is always `true`
- `__webpack_exports_info__.<exportName>.used` is `false` when the export is known to be unused, `true` otherwise
- `__webpack_exports_info__.<exportName>.useInfo` is
  - `false` when the export is known to be unused
  - `true` when the export is known to be used
  - `null` when the export usage could depend on runtime conditions
  - `undefined` when no info is available
- `__webpack_exports_info__.<exportName>.provideInfo` is
  - `false` when the export is known to be not provided
  - `true` when the export is known to be provided
  - `null` when the export provision could depend on runtime conditions
  - `undefined` when no info is available
- Accessing the info from nested exports is possible: i. e. `__webpack_exports_info__.<exportName>.<exportProperty1>.<exportProperty2>.used`
- Check whether exports can be mangled with `__webpack_exports_info__.<exportName>.canMangle`

```js title=Source
if (__webpack_exports_info__.someUsedExport.used) { }
if (__webpack_exports_info__.someUnusedExport.used) { }
```
```js title=Compiled
if (true) {
}
if (false) {
}
```

## Chunks

### \_\_webpack\_chunkname\_\_

Rspack/Webpack specific
Get current chunk name.

```js title=Source
__webpack_chunkname__
```
```js title=Compiled
__webpack_require__.cn;

// webpack/runtime/chunk_name
__webpack_require__.cn = 'main';
```

### \_\_webpack\_chunk\_load\_\_

Rspack/Webpack specific
The internal chunk loading function. Takes one argument:

- `chunkId`: the id for the chunk to load.

```js title=Source
__webpack_chunk_load__
```
```js title=Compiled
__webpack_require__.e;

// webpack/runtime/ensure_chunk
__webpack_require__.e = function (chunkId) {
  // return chunk loading promise
};
```

Example to load chunks from alternate public path when one failed:

```js
const originalLoad = __webpack_chunk_load__;
const publicPaths = ['a', 'b', 'c'];
__webpack_chunk_load__ = async (id) => {
  let error;
  for (const path of publicPaths) {
    __webpack_public_path__ = path;
    try {
      return await originalLoad(id);
    } catch (e) {
      error = e;
    }
  }
  throw error;
};
import('./module-a').then((moduleA) => {
  // now webpack will use the custom __webpack_chunk_load__ to load chunk
});
```

### \_\_webpack\_get\_script\_filename\_\_

[Added in v1.0.0](https://github.com/web-infra-dev/rspack/releases/tag/v1.0.0)Rspack/Webpack specific
It provides filename of the chunk by its id.

```js title=Source
__webpack_get_script_filename__
```
```js title=Compiled
__webpack_require__.u;

// webpack/runtime/get_chunk_filename
__webpack_require__.u = function (chunkId) {
  // ...
};
```

It is assignable, which allows changing the filename used by the runtime. For example, it can be used to determine the final path when loading chunks.

```js
const oldFn = __webpack_get_script_filename__;

__webpack_get_script_filename__ = (chunkId) => {
  const filename = oldFn(chunkId);
  return filename + '.changed';
};
```

## Module Federation

### \_\_webpack\_share\_scopes\_\_

Rspack/Webpack specific
This object is used as a shared scope in the remote container and is filled with the provided modules from a host

### \_\_webpack\_init\_sharing\_\_

Rspack/Webpack specific
This method is used to initialize modules of a shared scope in the host container.

## System.js

### \_\_system\_context\_\_

Rspack/Webpack specific
Context from System.js when `output.library.type="system"`

## Rspack

### \_\_rspack\_version\_\_

Rspack only
Current Rspack version, default to version in `@rspack/core/package.json`, can
be modified through output.bundlerInfo.version.

```js title=Source
__rspack_version__
```
```js title=Compiled
__webpack_require__.rv;

// webpack/runtime/rspack_version
__webpack_require__.rv = '0.7.4';
```

### \_\_rspack\_unique\_id\_\_

[Added in v1.0.0](https://github.com/web-infra-dev/rspack/releases/tag/v1.0.0)Rspack only
The ID of the current bundler, the value is `bundler={bundler}@{version}`:

- `bundler`: Default to `"rspack"` and can be modified through [output.bundlerInfo.bundler](/config/output.md#outputbundlerinfo).
- `version`: Default to version in `@rspack/core/package.json` and can be modified through [output.bundlerInfo.version](/config/output.md#outputbundlerinfo).

```js title=Source
__rspack_unique_id__
```
```js title=Compiled
__webpack_require__.ruid;

// webpack/runtime/rspack_unique_id
__webpack_require__.ruid = 'bundler=rspack@0.7.4';
```
