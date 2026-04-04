# Source: https://rolldown.rs/reference/Function.withFilter.md

---
url: /reference/Function.withFilter.md
---
# Function: withFilter()

* **Exported from**: `rolldown/filter`
* **Type**: (`pluginOption`: `T`, `filterObject`: `OverrideFilterObject` | `OverrideFilterObject`\[]) => `T`

A helper function to add plugin hook filters to a plugin or an array of plugins.

## Type Parameters

### A

`A`

### T

`T` *extends* [`RolldownPluginOption`](TypeAlias.RolldownPluginOption.md)<`A`>

## Parameters

### pluginOption

`T`

### filterObject

`OverrideFilterObject` | `OverrideFilterObject`\[]

## Returns

`T`

## Example

```ts
import yaml from '@rollup/plugin-yaml';
import { defineConfig } from 'rolldown';
import { withFilter } from 'rolldown/filter';

export default defineConfig({
  plugins: [
    // Run the transform hook of the `yaml` plugin
    // only for modules which end in `.yaml`
    withFilter(
      yaml({}),
      { transform: { id: /\.yaml$/ } },
    ),
  ],
});
```
