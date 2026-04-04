# Source: https://vue-macros.dev/macros/define-render.md

---
url: /macros/define-render.md
---
# defineRender&#x20;

Defining render function in `<script setup>` using the `defineRender`.

|  Features  |     Supported      |
| :--------: | :----------------: |
|   Vue 3    | :white\_check\_mark: |
|   Nuxt 3   | :white\_check\_mark: |
|   Vue 2    | :white\_check\_mark: |
| TypeScript | :white\_check\_mark: |

We need more feedback on [RFC Discussion](https://github.com/vuejs/rfcs/discussions/585)!

## Basic Usage

```vue twoslash
<script setup lang="tsx">
// JSX passed directly
defineRender(
  <div>
    <span>Hello</span>
  </div>,
)

// Or using render function
defineRender(() => {
  return (
    <div>
      <h1>Hello World</h1>
    </div>
  )
})
</script>
```
