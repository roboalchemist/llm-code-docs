# Source: https://rolldown.rs/reference/InputOptions.plugins.md

---
url: /reference/InputOptions.plugins.md
---
# plugins

* **Type**: [`RolldownPluginOption`](TypeAlias.RolldownPluginOption.md)
* **Optional**

The list of plugins to use.

Falsy plugins will be ignored, which can be used to easily activate or deactivate plugins. Nested plugins will be flattened. Async plugins will be awaited and resolved.

See [Plugin API document](/apis/plugin-api) for more details about creating plugins.

## Example

```js
import { defineConfig } from 'rolldown'

export default defineConfig({
  plugins: [
    examplePlugin1(),
    // Conditional plugins
    process.env.ENV1 && examplePlugin2(),
    // Nested plugins arrays are flattened
    [examplePlugin3(), examplePlugin4()],
  ]
})
```
