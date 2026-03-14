# Source: https://nuxtcharts.com/docs/customize/markers

Title: Markers

URL Source: https://nuxtcharts.com/docs/customize/markers

Markdown Content:
Markers
===============

[Nuxt Charts v2](https://nuxtcharts.com/)

*   [Blocks](https://nuxtcharts.com/blocks)
*   [Docs](https://nuxtcharts.com/docs/getting-started/installation)
*   [Charts](https://nuxtcharts.com/charts)
*   [Templates](https://nuxtcharts.com/templates)
*   Apps
*   [Pricing](https://nuxtcharts.com/pricing)

menu

[](https://ui.nuxtcharts.com/)[](https://github.com/dennisadriaans/vue-chrts)[Sign In Sign In](https://nuxtcharts.com/docs/customize/markers)

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

Markers
=======

Learn how to customize markers in Nuxt Charts to highlight data points with custom shapes, sizes, and colors.

[Customizing Markers in Nuxt Charts](https://nuxtcharts.com/docs/customize/markers#customizing-markers-in-nuxt-charts)
----------------------------------------------------------------------------------------------------------------------

Markers highlight data points on your charts. Nuxt Charts allows you to customize marker type, size, color, and stroke to match your data and design.

[Basic Marker Configuration](https://nuxtcharts.com/docs/customize/markers#basic-marker-configuration)
------------------------------------------------------------------------------------------------------

You can configure markers using the `:marker-config` prop. For example:

Preview Markers.vue

Desktop

```
<script lang="ts" setup>
import type { MarkerConfig } from '~/types/types'

const chartData = [
  { month: 'January', desktop: 120 },
  { month: 'February', desktop: 185 },
  { month: 'March', desktop: 160 },
  { month: 'April', desktop: 220 },
  { month: 'May', desktop: 195 },
  { month: 'June', desktop: 270 }
]

const categories: Record<string, BulletLegendItemInterface> = {
  desktop: { name: 'Desktop', color: '#22c55e' }
}

const xFormatter = (tick: number, _i?: number, _ticks?: number[]): string => {
  return chartData[tick]?.month ?? ''
}

const markerConfig: MarkerConfig = {
  id: 'main-chart',
  config: {
    desktop: {
      type: 'circle',
      size: 16,
      color: '#22c55e',
      strokeColor: '#22c55e',
      strokeWidth: 2
    }
  }
}
</script>

<template>
  <LineChart
    :data="chartData"
    :height="300"
    x-label="Time"
    y-label="Temperature"
    :categories="categories"
    :y-num-ticks="4"
    :x-num-ticks="7"
    :x-formatter="xFormatter"
    :legend-position="LegendPosition.TopRight"
    :hide-legend="false"
    :y-grid-line="true"
    :marker-config="markerConfig"
    @click="(e, data) => console.log('Chart clicked', data)"
  />
</template>

<style scoped>
/* Stroke maps to color key in categories */
/* The color should match the color defined in categories */
#main-chart:deep(*[stroke='#22c55e']) {
  marker: url('#main-chart-desktop');
}
</style>
```

[Required Marker Styles](https://nuxtcharts.com/docs/customize/markers#required-marker-styles)
----------------------------------------------------------------------------------------------

To ensure markers display correctly, add the following CSS to your component:

marker-styles.vue

```
<style scoped>
/* Stroke maps to color key in categories */
/* The color should match the color defined in categories */
.markers:deep(*[stroke='#3b82f6']) {
  marker: url('#circle-marker-desktop');
}
</style>
```

[Custom Marker Example](https://nuxtcharts.com/docs/customize/markers#custom-marker-example)
--------------------------------------------------------------------------------------------

You can fully customize markers for each series or data point. See the example below for a custom marker configuration.

[Theming Learn how to customize Nuxt Charts appearance using CSS variables for theming and dark mode support.](https://nuxtcharts.com/docs/customize/theming)[Legends Learn how to customize legends in Nuxt Charts to highlight data points with custom shapes, sizes, and colors.](https://nuxtcharts.com/docs/customize/legend)

Browse All Documentation

Table of Contents
Table of Contents

*   [Customizing Markers in Nuxt Charts](https://nuxtcharts.com/docs/customize/markers#customizing-markers-in-nuxt-charts)
*   [Basic Marker Configuration](https://nuxtcharts.com/docs/customize/markers#basic-marker-configuration)
*   [Required Marker Styles](https://nuxtcharts.com/docs/customize/markers#required-marker-styles)
*   [Custom Marker Example](https://nuxtcharts.com/docs/customize/markers#custom-marker-example)

Support Nuxt Charts

*   [Follow on X](https://x.com/DennisAdriaans)
*   [Star on GitHub](https://github.com/dennisadriaans/vue-chrts)
*   [Purchase a All-Access](https://nuxtcharts.com/pricing)

SCROLL: 0px
