# Source: https://rolldown.rs/reference/TypeAlias.ObjectHook.md

---
url: /reference/TypeAlias.ObjectHook.md
---
# Type Alias: ObjectHook\<T, O>

* **Type**: `T` | { `handler`: `T`; } & { `order?`: `PluginOrder`; } & `O`

A hook in a function or an object form with additional properties.

## Type Parameters

### T

`T`

The type of the hook function.

### O

`O` = { }

Additional properties that are specific to some hooks.

## Additional Properties

### order

* Type: `"pre" | "post" | null`

If there are several plugins implementing this hook, either run this plugin first (`"pre"`), last (`"post"`), or in the user-specified position (no value or `null`).

If several plugins use `"pre"` or `"post"`, Rolldown runs them in the user-specified order. This option can be used for all plugin hooks.

#### Example

```js
export default function resolveFirst() {
  return {
    name: 'resolve-first',
    resolveId: {
      order: 'pre',
      handler(source) {
        if (source === 'external') {
          return { id: source, external: true };
        }
        return null;
      },
    },
  };
}
```

### filter

* Type: [`HookFilter`](/reference/Interface.HookFilter) | `TopLevelFilterExpression`\[] (depends on hook)

Run this plugin hook only when the specified filter returns true. This property is only available for [`resolveId`](/reference/Interface.Plugin#resolveid), [`load`](/reference/Interface.Plugin#load), [`transform`](/reference/Interface.Plugin#transform) hooks.

#### Example

```js
export default function jsxAdditionalTransform() {
  return {
    name: 'jsxAdditionalTransform',
    transform: {
      filter: {
        id: '*.jsx',
        code: '<Custom',
      },
      handler(code) {
        // transform <Custom /> here
      },
    },
  };
}
```

### ~~sequential~~

* Type: `boolean`

#### Deprecated

This option is only for Rollup plugin compatibility. Hooks always work as `sequential: true`.
