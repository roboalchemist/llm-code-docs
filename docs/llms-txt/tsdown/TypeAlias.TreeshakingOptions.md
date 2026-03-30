# Source: https://tsdown.dev/reference/api/TypeAlias.TreeshakingOptions.md

---
url: /reference/api/TypeAlias.TreeshakingOptions.md
---
# Type Alias: TreeshakingOptions

```ts
type TreeshakingOptions = object
```

Defined in: node\_modules/.pnpm/rolldown@1.0.0-rc.9/node\_modules/rolldown/dist/shared/define-config-cG45vHwf.d.mts:2285

When passing an object, you can fine-tune the tree-shaking behavior.

## Properties

### annotations?

```ts
optional annotations: boolean;
```

Defined in: node\_modules/.pnpm/rolldown@1.0.0-rc.9/node\_modules/rolldown/dist/shared/define-config-cG45vHwf.d.mts:2361

Whether to respect `/*@__PURE__*/` annotations and other tree-shaking hints in the code.

See [related Oxc documentation](https://oxc.rs/docs/guide/usage/minifier/dead-code-elimination#pure-annotations) for more details.

#### Default

```ts
true
```

***

### commonjs?

```ts
optional commonjs: boolean;
```

Defined in: node\_modules/.pnpm/rolldown@1.0.0-rc.9/node\_modules/rolldown/dist/shared/define-config-cG45vHwf.d.mts:2410

Whether to enable tree-shaking for CommonJS modules. When `true`, unused exports from CommonJS modules can be eliminated from the bundle, similar to ES modules. When disabled, CommonJS modules will always be included in their entirety.

This option allows rolldown to analyze `exports.property` assignments in CommonJS modules and remove unused exports while preserving the module's side effects.

#### Example

```js
// source.js (CommonJS)
exports.used = 'This will be kept'
exports.unused = 'This will be tree-shaken away'

// main.js
import { used } from './source.js'
// With commonjs: true, only the 'used' export is included in the bundle
// With commonjs: false, both exports are included
```

#### Default

```ts
true
```

***

### invalidImportSideEffects?

```ts
optional invalidImportSideEffects: boolean;
```

Defined in: node\_modules/.pnpm/rolldown@1.0.0-rc.9/node\_modules/rolldown/dist/shared/define-config-cG45vHwf.d.mts:2391

Whether to assume that invalid import statements might have side effects.

See [related Oxc documentation](https://oxc.rs/docs/guide/usage/minifier/dead-code-elimination#ignoring-invalid-import-statement-side-effects) for more details.

#### Default

```ts
false
```

***

### manualPureFunctions?

```ts
optional manualPureFunctions: readonly string[];
```

Defined in: node\_modules/.pnpm/rolldown@1.0.0-rc.9/node\_modules/rolldown/dist/shared/define-config-cG45vHwf.d.mts:2375

Array of function names that should be considered pure (no side effects) even if they can't be automatically detected as pure.

See [related Oxc documentation](https://oxc.rs/docs/guide/usage/minifier/dead-code-elimination#define-pure-functions) for more details.

#### Example

```js
treeshake: {
  manualPureFunctions: ['console.log', 'debug.trace']
}
```

#### Default

```ts
;[]
```

***

### moduleSideEffects?

```ts
optional moduleSideEffects: ModuleSideEffectsOption;
```

Defined in: node\_modules/.pnpm/rolldown@1.0.0-rc.9/node\_modules/rolldown/dist/shared/define-config-cG45vHwf.d.mts:2353

**Values:**

* **`true`**: All modules are assumed to have side effects and will be included in the bundle even if none of their exports are used.
* **`false`**: No modules have side effects. This enables aggressive tree-shaking, removing any modules whose exports are not used.
* **`string[]`**: Array of module IDs that have side effects. Only modules in this list will be preserved if unused; all others can be tree-shaken when their exports are unused.
* **`'no-external'`**: Assumes no external modules have side effects while preserving the default behavior for local modules.
* **`ModuleSideEffectsRule[]`**: Array of rules with `test`, `external`, and `sideEffects` properties for fine-grained control.
* **`function`**: Function that receives `(id, external)` and returns whether the module has side effects.

**Important:** Setting this to `false` or using an array/string assumes that your modules and their dependencies have no side effects other than their exports. Only use this if you're certain that removing unused modules won't break your application.

> \[!NOTE]
> **Performance: Prefer `ModuleSideEffectsRule[]` over functions**
>
> When possible, use rule-based configuration instead of functions. Rules are processed entirely in Rust, while JavaScript functions require runtime calls between Rust and JavaScript, which can hurt CPU utilization during builds.
>
> **Functions should be a last resort**: Only use the function signature when your logic cannot be expressed with patterns or simple string matching.
>
> **Rule advantages**: `ModuleSideEffectsRule[]` provides better performance by avoiding Rust-JavaScript runtime calls, clearer intent, and easier maintenance.

#### Example

```js
// Assume no modules have side effects (aggressive tree-shaking)
treeshake: {
  moduleSideEffects: false
}

// Only specific modules have side effects (string array)
treeshake: {
  moduleSideEffects: [
    'lodash',
    'react-dom',
  ]
}

// Use rules for pattern matching and granular control
treeshake: {
  moduleSideEffects: [
    { test: /^node:/, sideEffects: true },
    { test: /\.css$/, sideEffects: true },
    { test: /some-package/, sideEffects: false, external: false },
  ]
}

// Custom function to determine side effects
treeshake: {
  moduleSideEffects: (id, external) => {
    if (external) return false; // external modules have no side effects
    return id.includes('/side-effects/') || id.endsWith('.css');
  }
}

// Assume no external modules have side effects
treeshake: {
  moduleSideEffects: 'no-external',
}
```

**Common Use Cases:**

* **CSS files**: `{ test: /\.css$/, sideEffects: true }` - preserve CSS imports
* **Polyfills**: Add specific polyfill modules to the array
* **Plugins**: Modules that register themselves globally on import
* **Library development**: Set to `false` for libraries where unused exports should be removed

#### Default

```ts
true
```

***

### propertyReadSideEffects?

```ts
optional propertyReadSideEffects: false | "always";
```

Defined in: node\_modules/.pnpm/rolldown@1.0.0-rc.9/node\_modules/rolldown/dist/shared/define-config-cG45vHwf.d.mts:2420

Controls whether reading properties from objects is considered to have side effects.

Set to `false` for more aggressive tree-shaking behavior.

See [related Oxc documentation](https://oxc.rs/docs/guide/usage/minifier/dead-code-elimination#ignoring-property-read-side-effects) for more details.

#### Default

```ts
'always'
```

***

### propertyWriteSideEffects?

```ts
optional propertyWriteSideEffects: false | "always";
```

Defined in: node\_modules/.pnpm/rolldown@1.0.0-rc.9/node\_modules/rolldown/dist/shared/define-config-cG45vHwf.d.mts:2428

Controls whether writing properties to objects is considered to have side effects.

Set to `false` for more aggressive behavior.

#### Default

```ts
'always'
```

***

### unknownGlobalSideEffects?

```ts
optional unknownGlobalSideEffects: boolean;
```

Defined in: node\_modules/.pnpm/rolldown@1.0.0-rc.9/node\_modules/rolldown/dist/shared/define-config-cG45vHwf.d.mts:2383

Whether to assume that accessing unknown global properties might have side effects.

See [related Oxc documentation](https://oxc.rs/docs/guide/usage/minifier/dead-code-elimination#ignoring-global-variable-access-side-effects) for more details.

#### Default

```ts
true
```
