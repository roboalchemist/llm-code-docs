# Source: https://nuxtcharts.com/docs/getting-started/installation

Title: Installation

URL Source: https://nuxtcharts.com/docs/getting-started/installation

Markdown Content:
Installation
===============

[Nuxt Charts v2](https://nuxtcharts.com/)

*   [Blocks](https://nuxtcharts.com/blocks)
*   [Docs](https://nuxtcharts.com/docs/getting-started/installation)
*   [Charts](https://nuxtcharts.com/charts)
*   [Templates](https://nuxtcharts.com/templates)
*   Apps
*   [Pricing](https://nuxtcharts.com/pricing)

menu

[](https://ui.nuxtcharts.com/)[](https://github.com/dennisadriaans/vue-chrts)[Sign In Sign In](https://nuxtcharts.com/docs/getting-started/installation)

*   Getting Started

    *   [Installation](https://nuxtcharts.com/docs/getting-started/installation)
    *   [CLI](https://nuxtcharts.com/docs/getting-started/cli)
    *   [Vue Charts](https://nuxtcharts.com/docs/getting-started/vue-charts)

*   Charts

    *   [Area Chart](https://nuxtcharts.com/docs/charts/area-chart)
    *   [Bar Chart](https://nuxtcharts.com/docs/charts/bar-chart)
    *   [Line Chart](https://nuxtcharts.com/docs/charts/line-chart)
    *   [Donut Chart](https://nuxtcharts.com/docs/charts/donut-chart)
    *   [Bubble Chart](https://nuxtcharts.com/docs/charts/bubble-chart)
    *   [Gantt Charts](https://nuxtcharts.com/docs/charts/gantt-chart)

*   Components

    *   [Progress Circle](https://nuxtcharts.com/docs/components/progress-circle)
    *   [Status Tracker](https://nuxtcharts.com/docs/components/status-tracker)
    *   [Category Distribution](https://nuxtcharts.com/docs/components/category-distribution)
    *   [Code Block](https://nuxtcharts.com/docs/components/code-block)
    *   [Calendar](https://nuxtcharts.com/docs/components/calendar)

*   Maps

    *   [Dotted Map](https://nuxtcharts.com/docs/maps/dotted-map)
    *   [TopoJSON Map](https://nuxtcharts.com/docs/maps/topojson-map)

*   Customize

    *   [Tooltips](https://nuxtcharts.com/docs/customize/tooltips)
    *   [Theming](https://nuxtcharts.com/docs/customize/theming)
    *   [Markers](https://nuxtcharts.com/docs/customize/markers)
    *   [Legends](https://nuxtcharts.com/docs/customize/legend)
    *   [Server-side Rendering](https://nuxtcharts.com/docs/customize/server-side-rendering)

Installation
============

Get started with Nuxt Charts or Vue Charts.

[1. Install dependencies](https://nuxtcharts.com/docs/getting-started/installation#_1-install-dependencies)
-----------------------------------------------------------------------------------------------------------

Use your preferred package manager to install the library:

Nuxt Vue

```
pnpm add nuxt-charts
```

```
pnpm add vue-chrts @unovis/ts @unovis/vue
```

**Warning!** If you're using **pnpm** in a Nuxt project, set `shamefully-hoist=true` in your `.npmrc` to avoid the "to-px" error, or install `@unovis/ts` as a dependency.

[2. Configuration (Nuxt only)](https://nuxtcharts.com/docs/getting-started/installation#_2-configuration-nuxt-only)
-------------------------------------------------------------------------------------------------------------------

If you are using Nuxt, add the module to your `nuxt.config.ts`:

nuxt.config.ts

```
export default defineNuxtConfig({
    modules: ["nuxt-charts"]
})
```

_For Vue-only projects, no additional configuration is required._

[3. Test installation](https://nuxtcharts.com/docs/getting-started/installation#_3-test-installation)
-----------------------------------------------------------------------------------------------------

Nuxt Vue

```
<script setup lang="ts">
const data = [
  { month: 'Jan', sales: 100, profit: 50 },
  { month: 'Feb', sales: 120, profit: 55 },
  { month: 'Mar', sales: 180, profit: 80 },
  { month: 'Apr', sales: 110, profit: 40 },
  { month: 'May', sales: 90, profit: 30 },
]

const categories = {
  sales: {
    name: 'Sales',
    color: '#3b82f6',
  },
  profit: {
    name: 'Profit',
    color: '#10b981',
  },
}

const xFormatter = (i: number) => data[i].month
</script>

<template>
  <LineChart
    :data="data"
    :categories="categories"
    :height="300"
    :xFormatter="xFormatter"
    xLabel="Month"
    yLabel="Amount"
  />
</template>
```

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

[4. Customize CSS variables](https://nuxtcharts.com/docs/getting-started/installation#_4-customize-css-variables)
-----------------------------------------------------------------------------------------------------------------

Check the [Unovis documentation](https://unovis.dev/docs/guides/theming) for all options.

/assets/css/main.css

```
:root {
  --vis-color0: oklch(0.72 0.192 149.58) !important;
  --vis-color1: oklch(0.63 0.1963 157.86) !important;

  --tooltip-label-color: rgba(255, 255, 255, 0.5) !important;
  --tooltip-value-color: rgba(255, 255, 255, 1) !important;

  --vis-axis-grid-color: rgba(255, 255, 255, 0.1) !important;
  
  --vis-tooltip-background-color: #121212 !important;
  --vis-tooltip-border-color: none !important;

  --tooltip-label-color: rgba(255, 255, 255, 0.5);
  --tooltip-value-color: rgba(255, 255, 255, 1);

  --vis-tooltip-text-color: rgba(255, 255, 255, 0.5) !important;
  --vis-axis-tick-label-color: rgba(255, 255, 255, 0.5) !important;
  --vis-legend-label-color: rgba(255, 255, 255, 0.75) !important;

  --vis-axis-label-color: rgba(255, 255, 255, 0.5) !important;
  --vis-legend-label-color: rgba(255, 255, 255, 0.5) !important;
}
```

[Library Comparison](https://nuxtcharts.com/docs/getting-started/installation#library-comparison)
-------------------------------------------------------------------------------------------------

When searching for the right charting solution, it's important to understand how different libraries stack up.

| Feature | Nuxt Charts | Chart.js | Unovis |
| --- | --- | --- | --- |
| **Rendering** | SVG (native) | Canvas | SVG (native) |
| **Type Safety** | ✅ Full TypeScript | Partial | ✅ Full TypeScript |
| **Style System** | Tailwind / Nuxt UI | Custom CSS | Framework-agnostic |
| **SEO Ready** | ✅ Yes | ❌ Limited | ✅ Yes |
| **Best For** | Modern Nuxt/Vue Apps | Legacy/Simple Apps | Complex Dashboards |

[CLI How to install and use the Nuxt Charts CLI for chart management.](https://nuxtcharts.com/docs/getting-started/cli)

Browse All Documentation

Table of Contents
Table of Contents

*   [1. Install dependencies](https://nuxtcharts.com/docs/getting-started/installation#_1-install-dependencies)
*   [2. Configuration (Nuxt only)](https://nuxtcharts.com/docs/getting-started/installation#_2-configuration-nuxt-only)
*   [3. Test installation](https://nuxtcharts.com/docs/getting-started/installation#_3-test-installation)
*   [4. Customize CSS variables](https://nuxtcharts.com/docs/getting-started/installation#_4-customize-css-variables)
*   [Library Comparison](https://nuxtcharts.com/docs/getting-started/installation#library-comparison)

Support Nuxt Charts

*   [Follow on X](https://x.com/DennisAdriaans)
*   [Star on GitHub](https://github.com/dennisadriaans/vue-chrts)
*   [Purchase a All-Access](https://nuxtcharts.com/pricing)

SCROLL: 0px
