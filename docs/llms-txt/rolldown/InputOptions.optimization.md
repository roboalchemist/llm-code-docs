# Source: https://rolldown.rs/reference/InputOptions.optimization.md

---
url: /reference/InputOptions.optimization.md
---
# optimization

* **Type**: object with the properties below
* **Optional**

Configure optimization features for the bundler.

## inlineConst?

* **Type**: `boolean` | { `mode?`: `"all"` | `"smart"`; `pass?`: `number`; }
* **Optional**

Inline imported constant values during bundling instead of preserving variable references.

When enabled, constant values from imported modules will be inlined at their usage sites,
potentially reducing bundle size and improving runtime performance by eliminating variable lookups.

**Options:**

* `true`: equivalent to `{ mode: 'all', pass: 1 }`, enabling constant inlining for all eligible constants with a single pass.
* `false`: Disable constant inlining
* `{ mode: 'smart' | 'all', pass?: number }`:
  * `mode: 'smart'`: Only inline constants in specific scenarios where it is likely to reduce bundle size and improve performance.
    Smart mode inlines constants in these specific scenarios:
    1. `if (test) {} else {}` - condition expressions in if statements
    2. `test ? a : b` - condition expressions in ternary operators
    3. `test1 || test2` - logical OR expressions
    4. `test1 && test2` - logical AND expressions
    5. `test1 ?? test2` - nullish coalescing expressions
* `mode: 'all'`: Inline all imported constants wherever they are used.
* `pass`: Number of passes to perform for inlining constants.

### Example

```js
// Input files:
// constants.js
export const API_URL = 'https://api.example.com';

// main.js
import { API_URL } from './constants.js';
console.log(API_URL);

// With inlineConst: true, the bundled output becomes:
console.log('https://api.example.com');

// Instead of:
const API_URL = 'https://api.example.com';
console.log(API_URL);
```

### Default

```ts
{ mode: 'smart', pass: 1 }
```

## pifeForModuleWrappers?

* **Type**: `boolean`
* **Optional**

Use PIFE pattern for module wrappers.

Enabling this option improves the start up performance of the generated bundle with the cost of a slight increase in bundle size.

::: tip What is PIFE?

PIFE is the abbreviation of "Possibly-Invoked Function Expressions". It is a function expression wrapped with a parenthesized expression.

PIFEs annotate functions that are likely to be invoked eagerly. When [V8 JavaScript engine](https://v8.dev/) (the engine used in Chrome and Node.js) encounters such expressions, it compiles them eagerly (rather than compiling it later). See [V8's blog post](https://v8.dev/blog/preparser#pife) for more details.

:::

### Default

```ts
true
```
