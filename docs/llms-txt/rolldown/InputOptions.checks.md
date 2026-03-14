# Source: https://rolldown.rs/reference/InputOptions.checks.md

---
url: /reference/InputOptions.checks.md
---
# checks

* **Type**: object with the properties below
* **Optional**

Controls which warnings are emitted during the build process. Each option can be set to `true` (emit warning) or `false` (suppress warning).

## cannotCallNamespace?

* **Type**: `boolean`
* **Optional**

Whether to emit warnings when a namespace is called as a function.

A module namespace object is an object and not a function. Calling it as a function will cause a runtime error.

::: code-group

```js [main.js]
import * as utils from './utils.js';

// This will trigger the warning
// because `utils` is a namespace object, not a function
utils();
```

```js [utils.js]
export function greet() {
  return 'Hello';
}
```

:::

### Default

```ts
true
```

## circularDependency?

* **Type**: `boolean`
* **Optional**

Whether to emit warnings when detecting circular dependency.

Circular dependencies lead to a bigger bundle size and sometimes cause execution order issues and are better to avoid.

::: code-group

```js [a.js]
import { b } from './b.js';
export const a = 'a' + b;
```

```js [b.js]
import { a } from './a.js';
export const b = 'b' + a;
```

```js [main.js]
import { a } from './a.js';
console.log(a);
```

:::

In this example, `a.js` imports from `b.js`, and `b.js` imports from `a.js`, creating a circular dependency.

### Default

```ts
false
```

## commonJsVariableInEsm?

* **Type**: `boolean`
* **Optional**

Whether to emit warnings when a CommonJS variable is used in an ES module.

CommonJS variables like `module` and `exports` are treated as global variables in ES modules and may not work as expected.

```js
export const version = '1.0.0';

module.exports = { legacy: true }; // This triggers the warning
```

### Default

```ts
true
```

## configurationFieldConflict?

* **Type**: `boolean`
* **Optional**

Whether to emit warnings when a config value is overridden by another config value with a higher priority.

::: code-group

```js [rolldown.config.js]
export default {
  transform: {
    jsx: 'preserve',
  },
};
```

```json [tsconfig.json]
{
  "compilerOptions": {
    "jsx": "react"
  }
}
```

:::

### Default

```ts
true
```

## couldNotCleanDirectory?

* **Type**: `boolean`
* **Optional**

Whether to emit warnings when Rolldown could not clean the output directory.

See [`output.cleanDir`](/reference/OutputOptions.cleanDir).

### Default

```ts
true
```

## duplicateShebang?

* **Type**: `boolean`
* **Optional**

Whether to emit warnings when both the code and postBanner contain shebang

Having multiple shebangs in a file is a syntax error.

### Default

```ts
true
```

## emptyImportMeta?

* **Type**: `boolean`
* **Optional**

Whether to emit warnings when `import.meta` is not supported with the output format and is replaced with an empty object (`{}`).

See [`import.meta` in Non-ESM Output Formats page](/in-depth/non-esm-output-formats#import-meta) for more details.

### Default

```ts
true
```

## eval?

* **Type**: `boolean`
* **Optional**

Whether to emit warnings when detecting uses of direct `eval`s.

See [Avoiding Direct `eval` in Troubleshooting page](/guide/troubleshooting#avoiding-direct-eval) for more details.

### Default

```ts
true
```

## filenameConflict?

* **Type**: `boolean`
* **Optional**

Whether to emit warnings when files generated have the same name with different contents.

For example, this warning happens with the following config:

```js [rolldown.config.js]
export default {
  input: ['src/entry1.js', 'src/entry2.js'],
  output: {
    // Both entries will try to use the same filename
    entryFileNames: 'bundle.js',
  },
};
```

### Default

```ts
true
```

## importIsUndefined?

* **Type**: `boolean`
* **Optional**

Whether to emit warnings when an imported variable is not exported.

If the code is importing a variable that is not exported by the imported module, the value will always be `undefined`. This might be a mistake in the code.

::: code-group

```js [main.js]
import * as utils from './utils.js'; // 'nonExistent' is not exported
console.log(utils.nonExistent); // Always undefined
```

```js [utils.js]
export const helper = () => 'help';
```

:::

### Default

```ts
true
```

## ineffectiveDynamicImport?

* **Type**: `boolean`
* **Optional**

Whether to emit warnings when a module is dynamically imported but also statically imported, making the dynamic import ineffective for code splitting.

### Default

```ts
true
```

## missingGlobalName?

* **Type**: `boolean`
* **Optional**

Whether to emit warnings when the `output.globals` option is missing when needed.

See [`output.globals`](/reference/OutputOptions.globals).

### Default

```ts
true
```

## missingNameOptionForIifeExport?

* **Type**: `boolean`
* **Optional**

Whether to emit warnings when the `output.name` option is missing when needed.

See [`output.name`](/reference/OutputOptions.name).

### Default

```ts
true
```

## mixedExports?

* **Type**: `boolean`
* **Optional**

Whether to emit warnings when the way to export values is ambiguous.

See [`output.exports`](/reference/OutputOptions.exports).

### Default

```ts
true
```

## pluginTimings?

* **Type**: `boolean`
* **Optional**

Whether to emit warnings when plugins take significant time during the build process.

When enabled, Rolldown measures time spent in each plugin hook. If plugins significantly impact build performance, a warning is emitted with a breakdown of plugin timings.

**How it works:**

1. **Minimum build time**: To avoid noisy warnings for fast builds, the warning is only triggered if Rolldown's internal build time (Rust side) exceeds **3 seconds**.

2. **Detection threshold**: A warning is triggered when plugin time (total build time minus link stage time) exceeds 100x the link stage time. This threshold was determined by studying plugin impact on real-world projects.

3. **Identifying plugins**: When the threshold is exceeded, Rolldown reports up to 5 plugins that take longer than the average plugin time, sorted by duration. Each plugin shows its percentage of total plugin time. Only plugins with total duration of at least 1 second are included in the report.

> \[!WARNING]
> For hooks using [`this.resolve()`](/reference/Interface.PluginContext#resolve) or [`this.load()`](/reference/Interface.PluginContext#load), the reported time includes waiting for other plugins, which may overestimate that plugin's actual cost.
>
> Additionally, since plugin hooks execute concurrently, the statistics represent accumulated time rather than wall-clock time. The measured duration also includes Rust-side processing overhead, Tokio async scheduling overhead, NAPI data conversion overhead, and JavaScript event loop overhead.

### Default

```ts
true
```

## preferBuiltinFeature?

* **Type**: `boolean`
* **Optional**

Whether to emit warnings when a plugin that is covered by a built-in feature is used.

Using built-in features is generally more performant than using plugins.

### Default

```ts
true
```

## toleratedTransform?

* **Type**: `boolean`
* **Optional**

Whether to emit warnings when detecting tolerated transform.

### Default

```ts
true
```

## unresolvedEntry?

* **Type**: `boolean`
* **Optional**

Whether to emit warnings when an entrypoint cannot be resolved.

### Default

```ts
true
```

## unresolvedImport?

* **Type**: `boolean`
* **Optional**

Whether to emit warnings when an import cannot be resolved.

### Default

```ts
true
```

## unsupportedTsconfigOption?

* **Type**: `boolean`
* **Optional**

Whether to emit warnings when a tsconfig option or combination of options is not supported.

### Default

```ts
true
```
