# Source: https://vue-macros.dev/macros/define-props.md

---
url: /macros/define-props.md
---
# defineProps&#x20;

Correct types of destructured props using `$defineProps`.

See also [Vue issue](https://github.com/vuejs/core/issues/6876), [Reactivity Transform RFC](https://github.com/vuejs/rfcs/blob/reactivity-transform/active-rfcs/0000-reactivity-transform.md#defineprops-destructure-details).

|         Features          |     Supported      |
| :-----------------------: | :----------------: |
|           Vue 3           | :white\_check\_mark: |
|          Nuxt 3           | :white\_check\_mark: |
|           Vue 2           | :white\_check\_mark: |
| TypeScript / Volar Plugin | :white\_check\_mark: |

::: warning

[Reactivity Transform](../features/reactivity-transform.md) is required. You should enable it first.

:::

## Basic Usage

```vue twoslash
<script setup lang="ts">
const { foo } = $defineProps<{
  //     ^?
  foo: string[]
}>()

const fooRef = $$(foo)
//     ^?
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
