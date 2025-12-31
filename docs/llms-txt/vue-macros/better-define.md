# Source: https://vue-macros.dev/features/better-define.md

---
url: /features/better-define.md
---
# betterDefine&#x20;

With enabling `betterDefine`, imported types are supported in `<script setup>` type-based-macros.

[Related issue](https://github.com/vuejs/core/issues/4294)

|  Features  |     Supported      |
| :--------: | :----------------: |
|   Vue 3    | :white\_check\_mark: |
|   Nuxt 3   | :white\_check\_mark: |
|   Vue 2    | :white\_check\_mark: |
| TypeScript | :white\_check\_mark: |

## Basic Usage

::: code-group

```vue twoslash [App.vue]
<script setup lang="ts">
// #region basic
type BaseProps = {
  title: string
}

export type { BaseProps }
// #endregion basic
// ---cut---
// @noErrors
import type { BaseProps } from './types'

interface Props extends BaseProps {
  foo: string
}
const props = defineProps<Props>()
</script>
```

<<< ./better-define.md#basic{ts} \[types.ts]

:::

## ⚠️ Limitations

### Complex types

Complex types are not supported in some key places. For example:

#### What are Complex Types?

* All utility types
  * [Built-in types](https://www.typescriptlang.org/docs/handbook/utility-types.html)
  * All types from `type-fest` package.
  * `typeof` keyword.
  * ...
* Index Signature
  ```ts
  interface Type {
    [key: string]: string
  }
  ```
* Generics will be ignored directly

#### What are Key Places?

* The names of props.

```ts
// ✅
defineProps<{
  foo: ComplexType
}>()

// ❌
defineProps<{
  [ComplexType]: string
}>()
```

* The names of emits.

```ts
interface Emits {
  (event: 'something', value: ComplexType): void // ✅
  (event: ComplexType): void // ❌
}
```
