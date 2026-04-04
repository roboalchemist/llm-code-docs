# Source: https://vue-macros.dev/features/script-lang.md

---
url: /features/script-lang.md
---
# scriptLang&#x20;

Set the default language for `<script>` block.

::: tip
Convert `<script setup>` to `<script setup lang="ts">`.
:::

|   Features   |     Supported      |
| :----------: | :----------------: |
|    Vue 3     | :white\_check\_mark: |
|    Nuxt 3    | :white\_check\_mark: |
|    Vue 2     | :white\_check\_mark: |
| Volar Plugin | :white\_check\_mark: |

## Options

```ts
interface Options {
  /**
   * @default 'ts'
   */
  defaultLang?: 'ts' | 'tsx' | 'jsx' | string
}
```

## Usage

```vue twoslash
<script setup>
defineProps<{
  foo: string
}>()
</script>
```

## Volar Configuration

```jsonc {3,5-7} [tsconfig.json]
{
  "vueCompilerOptions": {
    "plugins": ["vue-macros/volar"],
    "vueMacros": {
      "scriptLang": {
        "defaultLang": "ts",
      },
    },
  },
}
```
