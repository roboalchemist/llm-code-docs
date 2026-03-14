# Source: https://nuxtcharts.com/docs/components/code-block

Title: Code Block

URL Source: https://nuxtcharts.com/docs/components/code-block

Markdown Content:
The `CodeBlock` component renders syntax-highlighted code using the project's built-in code editor, with a color-mode theme switcher and a copy-to-clipboard button built right in.

Counter.vue

```
<script setup lang="ts">
const count = ref(0)
</script>

<template>
  <div class="flex flex-col items-center gap-4 p-8">
    <p class="text-lg font-semibold">Count: {{ count }}</p>
    <UButton @click="count++">Increment</UButton>
  </div>
</template>
```

[](https://nuxtcharts.com/docs/getting-started/cli)
Learn how to use the **Nuxt Charts CLI** to get premium components.

| Prop | Type | Default | Description |
| --- | --- | --- | --- |
| `code` | `string` | — | The source code to display. |
| `language` | `string` | `'text'` | Language for syntax highlighting (e.g. `vue`, `typescript`, `bash`). |
| `filename` | `string` | `undefined` | Filename shown in the header. Falls back to `language`. |
| `showLineNumbers` | `boolean` | `false` | Display line numbers. |
| `darkTheme` | `string` | `'github-dark'` | Shiki theme used in dark color mode. |
| `lightTheme` | `string` | `'github-light'` | Shiki theme used in light color mode. |
| `maxHeight` | `string | number` | `undefined` | Max height of the code area (e.g. `400` or `'50vh'`). Scrollable when exceeded. |
| `loading` | `boolean` | `false` | Shows a loading spinner instead of code. |

By default the component automatically switches between `github-light` and `github-dark` based on the user's color mode. Override per-instance with `theme`, or set separate `darkTheme` / `lightTheme` props:

```
<template>
  <!-- Fixed theme -->
  <CodeBlock theme="nord" language="typescript" :code="tsCode" />

  <!-- Per color mode -->
  <CodeBlock dark-theme="one-dark-pro" light-theme="github-light" language="vue" :code="code" />
</template>
```

The `CodeBlock` component is optimized for Nuxt projects using Shiki, but it also supports standard Vue projects via the `lowlight` engine.

```
<template>
  <!-- Uses Shiki (default) -->
  <CodeBlock 
    :code="code" 
    language="vue" 
  />
</template>
```

This component requires the [`nuxt-shiki`](https://github.com/antfu/nuxt-shiki) module. Add it to `nuxt.config.ts`:

nuxt.config.ts

```
export default defineNuxtConfig({
  modules: ['nuxt-shiki'],
  shiki: {
    bundledThemes: ['github-dark', 'github-light'],
    bundledLangs: ['vue', 'typescript', 'javascript', 'css', 'json', 'bash'],
  }
})
```

### [Standard Vue Projects](https://nuxtcharts.com/docs/components/code-block#standard-vue-projects)

If you are using this in a non-Nuxt environment, ensure you have the following dependencies installed:

```
pnpm add lowlight hast-util-to-html highlight.js
```
