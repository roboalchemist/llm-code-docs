# Source: https://rolldown.rs/reference/InputOptions.transform.md

---
url: /reference/InputOptions.transform.md
---
# transform

* **Type**: object with the properties below
* **Optional**

Configure how the code is transformed. This process happens after the `transform` hook.

## Example

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

## In-depth

Rolldown uses Oxc under the hood for transformation.

While Oxc does not support lowering the latest decorators proposal yet, Rolldown is able to bundle them.

See [Oxc Transformer's document](https://oxc.rs/docs/guide/usage/transformer) for more details.

## assumptions?

* **Type**: `CompilerAssumptions`
* **Optional**

Set assumptions in order to produce smaller output.

### Inherited from

`Omit.assumptions`

## decorator?

* **Type**: `DecoratorOptions`
* **Optional**

Decorator plugin

### Inherited from

`Omit.decorator`

## define?

* **Type**: `Record`<`string`, `string`>
* **Optional**

Replace global variables or [property accessors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Property_accessors) with the provided values.

See Oxc's [`define` option](https://oxc.rs/docs/guide/usage/transformer/global-variable-replacement.html#define) for more details.

### Example

**Replace the global variable `IS_PROD` with `true`**

```js [rolldown.config.js]
export default defineConfig({
  transform: { define: { IS_PROD: 'true' } }
})
```

Result:

```js
// Input
if (IS_PROD) {
  console.log('Production mode')
}

// After bundling
if (true) {
  console.log('Production mode')
}
```

**Replace the property accessor `process.env.NODE_ENV` with `'production'`**

```js [rolldown.config.js]
export default defineConfig({
  transform: { define: { 'process.env.NODE_ENV': "'production'" } }
})
```

Result:

```js
// Input
if (process.env.NODE_ENV === 'production') {
  console.log('Production mode')
}

// After bundling
if ('production' === 'production') {
  console.log('Production mode')
}
```

## dropLabels?

* **Type**: `string`\[]
* **Optional**

Remove labeled statements with these label names.

Labeled statements are JavaScript statements prefixed with a label identifier.
This option allows you to strip specific labeled statements from the output,
which is useful for removing debug-only code in production builds.

### Example

```js rolldown.config.js
export default defineConfig({
  transform: { dropLabels: ['DEBUG', 'DEV'] }
})
```

Result:

```js
// Input
DEBUG: console.log('Debug info');
DEV: {
  console.log('Development mode');
}
console.log('Production code');

// After bundling
console.log('Production code');
```

## helpers?

* **Type**: `Helpers`
* **Optional**

Behaviour for runtime helpers.

### Inherited from

`Omit.helpers`

## inject?

* **Type**: `Record`<`string`, `string` | \[`string`, `string`]>
* **Optional**

Inject import statements on demand.

The API is aligned with `@rollup/plugin-inject`.

See Oxc's [`inject` option](https://oxc.rs/docs/guide/usage/transformer/global-variable-replacement.html#inject) for more details.

### Supported patterns

```js
{
  // import { Promise } from 'es6-promise'
  Promise: ['es6-promise', 'Promise'],

  // import { Promise as P } from 'es6-promise'
  P: ['es6-promise', 'Promise'],

  // import $ from 'jquery'
  $: 'jquery',

  // import * as fs from 'node:fs'
  fs: ['node:fs', '*'],

  // Inject shims for property access pattern
  'Object.assign': path.resolve( 'src/helpers/object-assign.js' ),
}
```

## jsx?

* **Type**: `false` | `"react"` | `"react-jsx"` | `"preserve"` | `JsxOptions`
* **Optional**

Controls how JSX syntax is transformed.

* If set to `false`, an error will be thrown if JSX syntax is encountered.
* If set to `'react'`, JSX syntax will be transformed to classic runtime React code.
* If set to `'react-jsx'`, JSX syntax will be transformed to automatic runtime React code.
* If set to `'preserve'`, JSX syntax will be preserved as-is.

## plugins?

* **Type**: `PluginsOptions`
* **Optional**

Third-party plugins to use.

### See

<https://oxc.rs/docs/guide/usage/transformer/plugins>

### Inherited from

`Omit.plugins`

## target?

* **Type**: `string` | `string`\[]
* **Optional**

Sets the target environment for the generated JavaScript.

The lowest target is `es2015`.

Example:

* `'es2015'`
* `['es2020', 'chrome58', 'edge16', 'firefox57', 'node12', 'safari11']`

### Default

`esnext` (No transformation)

### See

<https://oxc.rs/docs/guide/usage/transformer/lowering#target>

### Inherited from

`Omit.target`

## typescript?

* **Type**: `TypeScriptOptions`
* **Optional**

Configure how TypeScript is transformed.

### See

<https://oxc.rs/docs/guide/usage/transformer/typescript>

### Inherited from

`Omit.typescript`
