# Source: https://vue-macros.dev/macros/define-slots.md

---
url: /macros/define-slots.md
---
# defineSlots&#x20;

Declaring type of SFC slots in `<script setup>` using the `defineSlots`.

For Vue >= 3.3, this feature will be turned off by default.

|   Features   |     Supported      |
| :----------: | :----------------: |
|    Vue 3     | :white\_check\_mark: |
|    Nuxt 3    | :white\_check\_mark: |
| Volar Plugin | :white\_check\_mark: |
|    Vue 2     |        :x:         |

## Basic Usage

### Short Syntax

```vue twoslash
<script setup lang="ts">
defineSlots<{
  // slot name
  title: {
    // scoped slot
    foo: 'bar' | boolean
  }
}>()
</script>
```

### Full Syntax (Official Version)

```vue twoslash
<script setup lang="ts">
defineSlots<{
  title: (scope: { text: string }) => any
}>()
</script>
```

## Volar Configuration

```jsonc {3} [tsconfig.json]
{
  "vueCompilerOptions": {
    "plugins": ["vue-macros/volar"],
  },
}
```
