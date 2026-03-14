# Source: https://rolldown.rs/reference/Function.replacePlugin.md

---
url: /reference/Function.replacePlugin.md
---
# Function: replacePlugin()

* **Exported from**: `rolldown/plugins`
* **Type**: (`values`: `Record`<`string`, `string`>, `options`: `Omit`<`BindingReplacePluginConfig`, `"values"`>) => `BuiltinPlugin`

Replaces targeted strings in files while bundling.

## Parameters

### values?

`Record`<`string`, `string`> = `{}`

### options?

`Omit`<`BindingReplacePluginConfig`, `"values"`> = `{}`

## Returns

`BuiltinPlugin`

## Examples

**Basic usage**

```js
replacePlugin({
  'process.env.NODE_ENV': JSON.stringify('production'),
   __buildVersion: 15
})
```

**With options**

```js
replacePlugin({
  'process.env.NODE_ENV': JSON.stringify('production'),
  __buildVersion: 15
}, {
  preventAssignment: false,
})
```

## See

https://rolldown.rs/builtin-plugins/replace
