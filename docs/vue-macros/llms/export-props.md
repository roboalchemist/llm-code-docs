# Source: https://vue-macros.dev/features/export-props.md

---
url: /features/export-props.md
---
# exportProps&#x20;

[Svelte-like Declaring props](https://svelte.dev/docs#component-format-script-1-export-creates-a-component-prop) for Vue.

|   Features   |     Supported      |
| :----------: | :----------------: |
|    Vue 3     | :white\_check\_mark: |
|    Nuxt 3    |     :question:     |
|    Vue 2     | :white\_check\_mark: |
| Volar Plugin | :white\_check\_mark: |

## Pre-requisite

[Reactivity Transform](./reactivity-transform.md) is required to use this feature, but it is enabled by default in Vue Macros.

`export let` will be changed to `defineModel`, which is supported in Vue 3.4+.

## Usage

Using export syntax to declare props.

```vue twoslash
<script setup lang="ts">
export let foo: string
export const bar: number = 1 // with default value
</script>
```

## Volar Configuration

```jsonc {3,5} [tsconfig.json]
{
  "vueCompilerOptions": {
    "plugins": ["vue-macros/volar"],
    "vueMacros": {
      "exportProps": true,
    },
  },
}
```
