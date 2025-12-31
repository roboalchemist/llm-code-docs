# Source: https://vue-macros.dev/features/boolean-prop.md

---
url: /features/boolean-prop.md
---
# booleanProp&#x20;

Convert `<Comp checked />` to `<Comp :checked="true" />`.

Convert `<Comp !checked />` to `<Comp :checked="false" />`.

|   Features   |     Supported      |
| :----------: | :----------------: |
|    Vue 3     | :white\_check\_mark: |
|    Nuxt 3    | :white\_check\_mark: |
|    Vue 2     |        :x:         |
| Volar Plugin | :white\_check\_mark: |

## Options

```ts
interface Options {
  /**
   * @default '!'
   */
  negativePrefix?: string
}
```

## Usage

```vue twoslash
<script setup>
import type { FunctionalComponent } from 'vue'

export const Comp: FunctionalComponent<
  {
    checked: true,
    enabled: false,
  },
> = () => null
// ---cut---
// @noErrors
import Comp from './Comp.vue'
</script>

<template>
  <Comp checked !enabled />
  //             ^?
</template>
```

```vue twoslash
<script setup lang="ts">
// Comp.vue
defineProps<{
  checked: true
  enabled: false
}>()
</script>
```

## Volar Configuration

```jsonc {3,5} [tsconfig.json]
{
  "vueCompilerOptions": {
    "plugins": ["vue-macros/volar"],
    "vueMacros": {
      "booleanProp": true,
    },
  },
}
```
