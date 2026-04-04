# Source: https://vue-macros.dev/volar/script-sfc.md

---
url: /volar/script-sfc.md
---
# scriptSFC&#x20;

Enabled Volar support for `.ts` | `.tsx` files.

|   Features   |     Supported      |
| :----------: | :----------------: |
| Volar Plugin | :white\_check\_mark: |

## Basic Usage

### With `jsxDirective`

::: code-group

```tsx [App.tsx]
export default ({ foo }: { foo: number }) => (
  <div v-if={foo === 1}>{foo}</div>
  //                     ^ will be inferred as 1
)
```

:::

## Volar Configuration

```jsonc {3,5} [tsconfig.json]
{
  "vueCompilerOptions": {
    "plugins": ["@vue-macros/volar"],
    "vueMacros": {
      "scriptSFC": true,
    },
  },
}
```
