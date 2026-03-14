# Source: https://nuxtcharts.com/docs/components/category-distribution

Title: Category Distribution

URL Source: https://nuxtcharts.com/docs/components/category-distribution

Markdown Content:
Category Distribution
===============

[Nuxt Charts v2](https://nuxtcharts.com/)

*   [Blocks](https://nuxtcharts.com/blocks)
*   [Docs](https://nuxtcharts.com/docs/getting-started/installation)
*   [Charts](https://nuxtcharts.com/charts)
*   [Templates](https://nuxtcharts.com/templates)
*   Apps
*   [Pricing](https://nuxtcharts.com/pricing)

menu

[](https://ui.nuxtcharts.com/)[](https://github.com/dennisadriaans/vue-chrts)[Sign In Sign In](https://nuxtcharts.com/docs/components/category-distribution)

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

Category Distribution
=====================

[Star](https://github.com/dennisadriaans/vue-chrts)

A component to visualize categorical data

The `CategoryDistribution` component is a clean component to displaying categorical data.

[Example](https://nuxtcharts.com/docs/components/category-distribution#example)
-------------------------------------------------------------------------------

Here's an example of the `CategoryDistribution` in action, monitoring a fictional marketing service.

Preview CategoryDistribution.vue Terminal

100+8.2%

Marketing

Sales

Development

Support

```
<script setup lang="ts">
const exampleCategories = [
  { label: 'Marketing', percentage: 40, color: '#6366f1', value: 4000 },
  { label: 'Sales', percentage: 25, color: '#22d3ee', value: 2500 },
  { label: 'Development', percentage: 20, color: '#10b981', value: 2000 },
  { label: 'Support', percentage: 15, color: '#f59e42', value: 1500 },
]

const exampleTrend = {
  value: '+8.2%',
  direction: 'up' as const,
}
</script>

<template>
  <div class="bg-elevated/50 w-full py-8">
    <CategoryDistribution
      :primary-value="100"
      :gap="2"
      :categories="exampleCategories"
      :trend="exampleTrend"
      legend-class="mt-4"
      class="mx-auto w-full max-w-lg"
    />
  </div>
</template>
```

```
nuxt-charts add CategoryDistribution
```

[](https://nuxtcharts.com/docs/getting-started/cli)Learn how to use the **Nuxt Charts CLI** to get premium components.

[Props](https://nuxtcharts.com/docs/components/category-distribution#props)
---------------------------------------------------------------------------

| Prop | Type | Default | Description |
| --- | --- | --- | --- |
| `primaryValue` | `string | number` | — | The main value to display |
| `gap` | `string | number` | 0 | The gap between the items |
| `categories` | `CategoryItem[]` | — | Array of category items |
| `trend` | `TrendIndicator` | — | Optional trend indicator object |
| `legendClass` | `string` | `''` | Additional classes for the legend |
| `showFullLabel` | `boolean` | `false` | Show full label instead of truncated |

[Status Tracker A component to visualize the status of a service over a period of time.](https://nuxtcharts.com/docs/components/status-tracker)[Code Block A syntax-highlighted code block with a built-in theme switcher and one-click copy.](https://nuxtcharts.com/docs/components/code-block)

Browse All Documentation

Table of Contents
Table of Contents

*   [Example](https://nuxtcharts.com/docs/components/category-distribution#example)
*   [Props](https://nuxtcharts.com/docs/components/category-distribution#props)

Support Nuxt Charts

*   [Follow on X](https://x.com/DennisAdriaans)
*   [Star on GitHub](https://github.com/dennisadriaans/vue-chrts)
*   [Purchase a All-Access](https://nuxtcharts.com/pricing)

SCROLL: 0px
