# Source: https://rolldown.rs/reference/InputOptions.shimMissingExports.md

---
url: /reference/InputOptions.shimMissingExports.md
---
# shimMissingExports

* **Type**: `boolean`
* **Optional**

When `true`, creates shim variables for missing exports instead of throwing an error.

## Default

false

## Examples

### Enable shimming

```js
export default {
  shimMissingExports: true,
};
```

### Example scenario

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
