# Source: https://rolldown.rs/reference/InputOptions.moduleTypes.md

---
url: /reference/InputOptions.moduleTypes.md
---
# moduleTypes

* **Type**: [`ModuleTypes`](TypeAlias.ModuleTypes.md)
* **Optional**

Maps file patterns to module types, controlling how files are processed.

This is conceptually similar to [esbuild's `loader`](https://esbuild.github.io/api/#loader) option, allowing you to specify how each file extensions should be handled.

See [the In-Depth Guide](/in-depth/module-types) for more details.

## Example

```js
import { defineConfig } from 'rolldown'

export default defineConfig({
  moduleTypes: {
    '.frag': 'text',
  }
})
```
