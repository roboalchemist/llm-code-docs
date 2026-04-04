# Source: https://vue-macros.dev/features/export-render.md

---
url: /features/export-render.md
---
# exportRender&#x20;

Transform the default export statement, in `<script setup>` of Vue SFC, as a component render function.

|   Features   |     Supported      |
| :----------: | :----------------: |
|    Vue 3     | :white\_check\_mark: |
|    Nuxt 3    |     :question:     |
|    Vue 2     | :white\_check\_mark: |
| Volar Plugin | :white\_check\_mark: |

::: tip

This feature depends on `defineRender`, and make sure `defineRender` is not disabled.

:::

## Usage

```vue
<script setup lang="tsx">
// JSX passed directly
export default <div>ok</div>

// Or using render function
export default () => <div>ok</div>
</script>
```

## Volar Configuration

```jsonc {3,7} [tsconfig.json]
{
  "vueCompilerOptions": {
    "plugins": ["vue-macros/volar"],
    "vueMacros": {
      "exportRender": true,
    },
  },
}
```
