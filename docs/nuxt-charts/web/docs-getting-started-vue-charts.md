# Source: https://nuxtcharts.com/docs/getting-started/vue-charts

Title: Vue Charts

URL Source: https://nuxtcharts.com/docs/getting-started/vue-charts

Markdown Content:
This guide explains how to install and set up `vue-chrts` in your Vue.js project with Vite and Nuxt UI or TailwindCSS. `vue-chrts` is a high-level charting library built on top of [Unovis](https://unovis.dev/).

*   Vue 3 project
*   Tailwind CSS (recommended for default styling)

To use `vue-chrts`, you must install the core library along with its peer dependencies, `@unovis/ts` and `@unovis/vue`.

```
pnpm add vue-chrts @unovis/ts @unovis/vue
```

Once installed, you can import and use the chart components and constants in your Vue components:

```
<script setup lang="ts">
import { LineChart, LegendPosition } from 'vue-chrts'

const data = [
  { month: 'Jan', sales: 100 },
  { month: 'Feb', sales: 120 },
]

const categories = {
  sales: {
    name: 'Sales',
    color: '#3b82f6'
  }
}
</script>

<template>
  <LineChart
    :data="data"
    :categories="categories"
    :legendPosition="LegendPosition.TopCenter"
  />
</template>
```

If you want to customize the appearance of tooltips or other Unovis elements, you can add the following CSS variables to your global CSS file (e.g., `style.css`):

```
:root {
  --vis-tooltip-background-color: #ffffff;
  --vis-tooltip-border-color: #e2e8f0;
  --vis-tooltip-text-color: #1e293b;
  --vis-tooltip-border-radius: 8px;
}
```

`vue-chrts` is the premier library for building **Vue Charts**, optimized for both **Tailwind CSS** and **Nuxt UI**. Designed with the best developer experience in mind, it offers:

*   **Custom Tooltip Designs**: Fully customizable tooltips to match your application's design system.
*   **Flexible Legend Placement**: Support for various `LegendPosition` options including `Top`, `TopCenter`, `TopRight`, `bottomLeft`, `bottomCenter`, and `bottomRight`.
*   **Type Safety**: Fully written in TypeScript for a robust and safe development workflow.
*   **Seamless Integration**: Specifically built to work flawlessly with **Tailwind CSS** and **Nuxt UI**.
*   **User-Centric Customization**: Easy to get started with, but powerful enough for complex data visualizations.

When searching for the right **Vue Charts** solution, it's important to understand how different libraries stack up against each other. Below is a detailed comparison of popular options.

A Vue wrapper for Unovis charts specific for Vue.js projects that brings SVG charts to Vue applications with reactive data binding.

**Key Features:**

*   Reactive props and watchers for dynamic updates
*   Simple component-based integration
*   Large community and extensive examples

**Best suited for:**

*   Standard Vue SPAs requiring common chart types (line, bar, pie)
*   Projects needing quick chart implementation

**Limitations:**

*   Canvas-based rendering (limited SEO benefits)
*   Medium bundle size
*   Basic SSR support

*   Modular, framework-agnostic
*   SVG rendering options
*   **Best for**: Enterprise dashboards, complex visualizations

*   Industry standard, canvas-based
*   Minimal learning curve
*   **Best for**: Quick prototypes, simple charts

*   Built specifically for Nuxt 3
*   Tailwind CSS integration
*   **Best for**: SEO-focused pages, Nuxt applications

| Feature | Nuxt Charts | Chart.js | Unovis |
| --- | --- | --- | --- |
| **Rendering** | SVG (native) | Canvas | SVG (native) |
| **Type Safety** | ✅ Full TypeScript | Partial | ✅ Full TypeScript |
| **Style System** | Tailwind / Nuxt UI | Custom CSS | Framework-agnostic |
| **SEO Ready** | ✅ Yes | ❌ Limited | ✅ Yes |
| **Best For** | Modern Nuxt/Vue Apps | Legacy/Simple Apps | Complex Dashboards |
