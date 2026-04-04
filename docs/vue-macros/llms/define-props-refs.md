# Source: https://vue-macros.dev/macros/define-props-refs.md

---
url: /macros/define-props-refs.md
---
# definePropsRefs&#x20;

Returns refs from `defineProps` instead of a reactive object. It can be destructured without losing reactivity.

`toRefs(defineProps())` => `definePropsRefs()`

|         Features          |     Supported      |
| :-----------------------: | :----------------: |
|           Vue 3           | :white\_check\_mark: |
|          Nuxt 3           | :white\_check\_mark: |
|           Vue 2           | :white\_check\_mark: |
| TypeScript / Volar Plugin | :white\_check\_mark: |

## Basic Usage

```vue twoslash {2-3,8}
<script setup lang="ts">
// ✅ won't lose reactivity with destructuring
const { foo, bar } = definePropsRefs<{
  foo: string
  bar: number
}>()

console.log(foo.value, bar.value)
//           ^?
</script>
```

## With Default Value

```vue twoslash {2-3,8}
<script setup lang="ts">
import { withDefaults } from 'vue-macros/macros' with { type: 'macro' }

const { foo } = withDefaults(
  definePropsRefs<{
    foo?: string
  }>(),
  { foo: 'test' },
)

console.log(foo.value)
//           ^?
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
