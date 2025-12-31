# Source: https://vue-macros.dev/macros/short-emits.md

---
url: /macros/short-emits.md
---
# shortEmits&#x20;

Simplify the definition of emits.

For Vue >= 3.3, this feature will be turned off by default.

|  Features  |     Supported      |
| :--------: | :----------------: |
|   Vue 3    | :white\_check\_mark: |
|   Vue 2    | :white\_check\_mark: |
| TypeScript | :white\_check\_mark: |

## Basic Usage

```vue twoslash
<script setup lang="ts">
import { defineEmits } from 'vue-macros/macros'

const emits = defineEmits<{
  // tuple
  'update:modelValue': [val: string]
  // function
  update: (val: string) => void
}>()
</script>
```

Using type `ShortEmits` or for short `SE`.

```vue twoslash
<script setup lang="ts">
const emits = defineEmits<
  SE<{
    // tuple
    'update:modelValue': [val: string]
    // function
    update: (val: string) => void
  }>
>()
</script>
```

## Difference with Official Version

* function style of declaration is not supported by official version.
