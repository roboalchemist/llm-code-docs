# Source: https://rolldown.rs/reference/InputOptions.resolve.md

---
url: /reference/InputOptions.resolve.md
---
# resolve

* **Type**: object with the properties below
* **Optional**

Options for built-in module resolution feature.

## alias?

* **Type**: `Record`<`string`, `string` | `false` | `string`\[]>
* **Optional**

Substitute one package for another.

One use case for this feature is replacing a node-only package with a browser-friendly package in third-party code that you don't control.

### Example

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

## aliasFields?

* **Type**: `string`\[]\[]
* **Optional**

Fields in package.json to check for aliased paths.

This option is expected to be used for `browser` field support.

### Default

* `[['browser']]` for `browser` platform
* `[]` for other platforms

## conditionNames?

* **Type**: `string`\[]
* **Optional**

Condition names to use when resolving exports in package.json.

### Default

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

## exportsFields?

* **Type**: `string`\[]\[]
* **Optional**

Fields in package.json to check for exports.

### Default

`[['exports']]`

## extensionAlias?

* **Type**: `Record`<`string`, `string`\[]>
* **Optional**

Map of extensions to alternative extensions.

With writing `import './foo.js'` in a file, you want to resolve it to `foo.ts` instead of `foo.js`.
You can achieve this by setting: `extensionAlias: { '.js': ['.ts', '.js'] }`.

## extensions?

* **Type**: `string`\[]
* **Optional**

Extensions to try when resolving files. These are tried in order from first to last.

### Default

`['.tsx', '.ts', '.jsx', '.js', '.json']`

## mainFields?

* **Type**: `string`\[]
* **Optional**

Fields in package.json to check for entry points.

### Default

Defaults based on platform:

* `node` platform: `['main', 'module']`
* `browser` platform: `['browser', 'module', 'main']`
* `neutral` platform: `[]`

## mainFiles?

* **Type**: `string`\[]
* **Optional**

Filenames to try when resolving directories.

### Default

```ts
['index']
```

## modules?

* **Type**: `string`\[]
* **Optional**

Directories to search for modules.

### Default

```ts
['node_modules']
```

## symlinks?

* **Type**: `boolean`
* **Optional**

Whether to follow symlinks when resolving modules.

### Default

```ts
true
```

## ~~tsconfigFilename?~~

* **Type**: `string`
* **Optional**

### Deprecated

Use the top-level [`tsconfig`](./InputOptions.tsconfig) option instead.
