# Source: https://vue-macros.dev/macros/short-vmodel.md

---
url: /macros/short-vmodel.md
---
# shortVmodel&#x20;

A shorthand for `v-model`.

`v-model` -> `::` / `$` / `*`

If you have any questions about this feature, you can comment on [RFC Discussion](https://github.com/vuejs/rfcs/discussions/395).

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
   * @default '$'
   */
  prefix?: '::' | '$' | '*'
}
```

## Usage

### `$` Dollar Sign (Default)

```vue
<template>
  <input $="msg" />
  <!-- => <input v-model="msg" /> -->
  <demo $msg="msg" />
  <!-- => <input v-model:msg="msg" /> -->
</template>
```

### `::` Double Binding

```vue
<template>
  <!-- prettier-ignore -->
  <input ::="msg" />
  <!-- => <input v-model="msg" /> -->
  <demo ::msg="msg" />
  <!-- => <input v-model:msg="msg" /> -->
</template>
```

### `*` Asterisk Sign

```vue
<template>
  <input *="msg" />
  <!-- => <input v-model="msg" /> -->
  <demo *msg="msg" />
  <!-- => <input v-model:msg="msg" /> -->
</template>
```

## Volar Configuration

```jsonc {3,5-7} [tsconfig.json]
{
  "vueCompilerOptions": {
    "plugins": ["vue-macros/volar"],
    "vueMacros": {
      "shortVmodel": {
        "prefix": "$",
      },
    },
  },
}
```

## Known Issues

* Prettier will format `::=` to `:=` (e.g. `<div ::="msg" />` -> `<div :="msg" />`). The comment `<!-- prettier-ignore -->` is required if prefix is `::`.
