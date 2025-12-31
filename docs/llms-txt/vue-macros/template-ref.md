# Source: https://vue-macros.dev/volar/template-ref.md

---
url: /volar/template-ref.md
---
# templateRef&#x20;

Automatically infer type for `templateRef` (from [VueUse](https://vueuse.org/core/templateRef/))
and `useTemplateRef` (Vue 3.5+).

::: warning

This feature is officially supported since Volar (`vue-tsc`) v2.1.0.
Vue Macros is no longer offering this feature as a plugin.

:::

| Features |     Supported      |
| :------: | :----------------: |
|  Volar   | :white\_check\_mark: |

## Basic Usage

::: code-group

```vue [App.vue] twoslash
<script setup lang="ts">
// #region comp
import { defineComponent } from 'vue'

export const Comp = defineComponent({
  setup() {
    return { foo: 1 }
  },
})
// #endregion comp
// ---cut---
import { templateRef } from '@vueuse/core'
// @noErrors
import { Comp } from './Comp.ts'

const comp = templateRef('comp')
comp.value?.foo
//           ^?
</script>

<template>
  <Comp ref="comp" />
</template>
```

<<< ./template-ref.md#comp{ts} \[Comp.ts]

:::

## Volar Configuration

No configuration required.
