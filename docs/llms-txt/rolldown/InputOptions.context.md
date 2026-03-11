# Source: https://rolldown.rs/reference/InputOptions.context.md

---
url: /reference/InputOptions.context.md
---
# context

* **Type**: `string`
* **Optional**

The value of `this` at the top level of each module. **Normally, you don't need to set this option.**

## Default

```ts
undefined
```

## Example

**Set custom context**

```js
export default {
  context: 'globalThis',
  output: {
    format: 'iife',
  },
};
```

## In-depth

The `context` option controls what `this` refers to in the top-level scope of the input modules.

In ES modules, the `this` value is `undefined` by specification. This option allows you to set a different value. For example, if your input modules expect `this` to be `window` like in non-ES module scripts, you can set `context` to `'window'`.

Note that if the input module is detected as CommonJS, Rolldown will use `exports` as the `this` value regardless of this option.
