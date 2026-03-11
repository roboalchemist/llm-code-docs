# Source: https://rolldown.rs/reference/InputOptions.platform.md

---
url: /reference/InputOptions.platform.md
---
# platform

* **Type**: `"node"` | `"browser"` | `"neutral"`
* **Optional**

Expected platform where the code run.

When the platform is set to neutral:

* When bundling is enabled the default output format is set to esm, which uses the export syntax introduced with ECMAScript 2015 (i.e. ES6). You can change the output format if this default is not appropriate.
* The main fields setting is empty by default. If you want to use npm-style packages, you will likely have to configure this to be something else such as main for the standard main field used by node.
* The conditions setting does not automatically include any platform-specific values.

## Default

* `'node'` if the format is `'cjs'`
* `'browser'` for other formats

## Examples

### Browser platform

```js
export default {
  platform: 'browser',
  output: {
    format: 'esm',
  },
};
```

### Node.js platform

```js
export default {
  platform: 'node',
  output: {
    format: 'cjs',
  },
};
```

### Platform-neutral

```js
export default {
  platform: 'neutral',
  output: {
    format: 'esm',
  },
};
```

## In-depth

The platform setting provides sensible defaults for module resolution and environment-specific behavior, similar to esbuild's `platform` option.

### `'node'`

Optimized for Node.js environments:

* **Conditions**: Includes `'node'`, `'import'`, `'require'` based on output format
* **Main fields**: `['main', 'module']`
* **Target**: Node.js runtime behavior
* **process.env handling**: Preserves `process.env.NODE_ENV` and other Node.js globals

### `'browser'`

Optimized for browser environments:

* **Conditions**: Includes `'browser'`, `'import'`, `'module'`, `'default'`
* **Main fields**: `['browser', 'module', 'main']` - prefers browser-specific entry points
* **Target**: Browser runtime behavior
* **Built-ins**: Node.js built-in modules are not polyfilled by default

:::tip
For browser builds, you may want to use [rolldown-plugin-node-polyfills](https://github.com/rolldown/rolldown-plugin-node-polyfills) to polyfill Node.js built-ins if needed.
:::

### `'neutral'`

Platform-agnostic configuration:

* **Default format**: Always `'esm'`
* **Conditions**: Only includes format-specific conditions, no platform-specific ones
* **Main fields**: Empty by default - relies on package.json `"exports"` field
* **Use cases**: Universal libraries that run in multiple environments

### Difference from esbuild

Notable differences from esbuild's `platform` option:

* The default output format is always `'esm'` regardless of platform (in esbuild, Node.js defaults to `'cjs'`)

### Choosing a Platform

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
