# Source: https://vue-macros.dev/guide/eslint-integration.md

---
url: /guide/eslint-integration.md
---
# &#x20;ESLint Integration&#x20;

## Installation

::: code-group

```bash [pnpm]
pnpm add -D @vue-macros/eslint-config
```

```bash [yarn]
yarn add -D @vue-macros/eslint-config
```

```bash [npm]
npm i -D @vue-macros/eslint-config
```

:::

## Configuration

### Flat Configuration

```js [eslint.config.js]
import vueMacros from '@vue-macros/eslint-config/flat'
export default [
  vueMacros,
  // ...your other configurations
]
```

### Legacy Configuration

```jsonc [.eslintrc]
{
  "extends": [
    "@vue-macros/eslint-config",
    // ...your other configurations
  ],
}
```
