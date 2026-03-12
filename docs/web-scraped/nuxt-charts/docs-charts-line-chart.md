# Source: https://nuxtcharts.com/docs/charts/line-chart

Title: Line Chart

URL Source: https://nuxtcharts.com/docs/charts/line-chart

Markdown Content:
Line Chart
===============

[Nuxt Charts v2](https://nuxtcharts.com/)

*   [Blocks](https://nuxtcharts.com/blocks)
*   [Docs](https://nuxtcharts.com/docs/getting-started/installation)
*   [Charts](https://nuxtcharts.com/charts)
*   [Templates](https://nuxtcharts.com/templates)
*   Apps
*   [Pricing](https://nuxtcharts.com/pricing)

menu

[](https://ui.nuxtcharts.com/)[](https://github.com/dennisadriaans/vue-chrts)[Sign In Sign In](https://nuxtcharts.com/docs/charts/line-chart)

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

Line Chart
==========

Create single and multiple line visualizations in your Nuxt application using Vue charts.

The `LineChart` component lets you quickly build interactive charts for visualizing trends over time or continuous values. It supports single or multiple lines, stacked lines, various curve types, and easy customization for Nuxt and Vue applications featuring Vue charts. [Examples ↗](https://nuxtcharts.com/charts)

[Basic Usage](https://nuxtcharts.com/docs/charts/line-chart#basic-usage)
------------------------------------------------------------------------

Preview MultiLinesLinear.vue

### Line Chart

[](https://nuxtcharts.com/blocks/line-charts)

Subscriptions

Downloads

```
<script lang="ts" setup>
defineOptions({
  tags: ['linecharts', 'multilineslinear']
})

import { useResponsiveHeight } from '~/composables/useResponsiveHeight'

withDefaults(
  defineProps<{
    showTitle?: boolean
  }>(),
  {
    showTitle: false
  }
)

const chartData = [
  {
    date: 'Jan 23',
    subscriptions: 2890,
    downloads: 2338
  },
  {
    date: 'Feb 23',
    subscriptions: 2756,
    downloads: 2103
  },
  {
    date: 'Mar 23',
    subscriptions: 3322,
    downloads: 2194
  },
  {
    date: 'Apr 23',
    subscriptions: 3470,
    downloads: 2108
  },
  {
    date: 'May 23',
    subscriptions: 3475,
    downloads: 1812
  },
  {
    date: 'Jun 23',
    subscriptions: 3129,
    downloads: 1726
  },
  {
    date: 'Jul 23',
    subscriptions: 3490,
    downloads: 1982
  },
  {
    date: 'Aug 23',
    subscriptions: 2903,
    downloads: 2012
  },
  {
    date: 'Sep 23',
    subscriptions: 2643,
    downloads: 2342
  },
  {
    date: 'Oct 23',
    subscriptions: 2837,
    downloads: 2473
  },
  {
    date: 'Nov 23',
    subscriptions: 2954,
    downloads: 3848
  },
  {
    date: 'Dec 23',
    subscriptions: 3239,
    downloads: 3736
  }
]

const categories: Record<string, BulletLegendItemInterface> = {
  subscriptions: { name: 'Subscriptions', color: '#3b82f6' },
  downloads: { name: 'Downloads', color: '#22c55e' }
}

const xFormatter = (tick: number, _i?: number, _ticks?: number[]): string => {
  return String(chartData[tick]?.date ?? '')
}

const { height } = useResponsiveHeight({
  default: 180,
  sm: 220,
  md: 260,
  lg: 300,
  xl: 340
})
</script>

<template>
  <div
    class="mx-auto max-w-3xl space-y-6 rounded-lg"
    :class="showTitle ? 'p-6' : ''"
  >
    <div class="flex items-center justify-between">
      <h3 class="text-lg font-semibold">
        Line Chart
      </h3>
      <NuxtLink to="/blocks/line-charts">
        <UButton
          icon="i-lucide-copy"
          size="sm"
          variant="soft"
          color="neutral"
        />
      </NuxtLink>
    </div>
    <LineChart
      :data="chartData"
      :height="height"
      y-label="Sales"
      :x-num-ticks="4"
      :y-num-ticks="4"
      :categories="categories"
      :x-formatter="xFormatter"
      :y-grid-line="true"
      :curve-type="CurveType.Linear"
      :legend-position="LegendPosition.TopRight"
      :hide-legend="false"
    />
  </div>
</template>
```

### [Multiple Lines](https://nuxtcharts.com/docs/charts/line-chart#multiple-lines)

Preview MultiLines.vue

### Line Chart

[](https://nuxtcharts.com/blocks/line-charts)

Desktop

Mobile

```
<script lang="ts" setup>
defineOptions({
  tags: ['linecharts', 'multilines']
})

withDefaults(
  defineProps<{
    showTitle?: boolean
  }>(),
  {
    showTitle: false
  }
)

const chartData = [
  { month: 'January', desktop: 186, mobile: 186 },
  { month: 'February', desktop: 305, mobile: 305 },
  { month: 'March', desktop: 237, mobile: 237 },
  { month: 'April', desktop: 260, mobile: 209 },
  { month: 'May', desktop: 209, mobile: 209 },
  { month: 'June', desktop: 250, mobile: 214 }
]

const categories: Record<string, BulletLegendItemInterface> = {
  desktop: { name: 'Desktop', color: '#3b82f6' },
  mobile: { name: 'Mobile', color: '#22c55e' }
}

const xFormatter = (tick: number, _i?: number, _ticks?: number[]): string => {
  return chartData[tick]?.month ?? ''
}
</script>

<template>
  <div
    class="mx-auto max-w-3xl space-y-6 rounded-lg"
    :class="showTitle ? 'p-6' : ''"
  >
    <div class="flex items-center justify-between">
      <h3 class="text-lg font-semibold">
        Line Chart
      </h3>
      <NuxtLink to="/blocks/line-charts">
        <UButton
          icon="i-lucide-copy"
          size="sm"
          variant="soft"
          color="neutral"
        />
      </NuxtLink>
    </div>
    <LineChart
      :data="chartData"
      :height="300"
      y-label="Number of visits"
      :x-num-ticks="2"
      :categories="categories"
      :x-formatter="xFormatter"
      :y-grid-line="true"
      :curve-type="CurveType.MonotoneX"
      :legend-position="LegendPosition.TopRight"
      :hide-legend="false"
    />
  </div>
</template>
```

### [Single Line](https://nuxtcharts.com/docs/charts/line-chart#single-line)

Preview SingleLine.vue

### Line Chart

[](https://nuxtcharts.com/blocks/line-charts)

Desktop

```
<script lang="ts" setup>
defineOptions({
  tags: ['linecharts', 'singleline']
})

withDefaults(
  defineProps<{
    showTitle?: boolean
  }>(),
  {
    showTitle: false
  }
)

const chartData = [
  { month: 'January', desktop: 186 },
  { month: 'February', desktop: 305 },
  { month: 'March', desktop: 237 },
  { month: 'April', desktop: 260 },
  { month: 'May', desktop: 209 },
  { month: 'June', desktop: 250 }
]

const categories: Record<string, BulletLegendItemInterface> = {
  desktop: { name: 'Desktop', color: '#22c55e' }
}

const xFormatter = (tick: number, _i?: number, _ticks?: number[]): string => {
  return chartData[tick]?.month ?? ''
}
</script>

<template>
  <div
    class="mx-auto max-w-3xl space-y-6 rounded-lg"
    :class="showTitle ? 'p-6' : ''"
  >
    <div class="flex items-center justify-between">
      <h3 class="text-lg font-semibold">
        Line Chart
      </h3>
      <NuxtLink to="/blocks/line-charts">
        <UButton
          icon="i-lucide-copy"
          size="sm"
          variant="soft"
          color="neutral"
        />
      </NuxtLink>
    </div>
    <LineChart
      :data="chartData"
      :height="300"
      x-label="Time"
      y-label="Temperature"
      :categories="categories"
      :y-num-ticks="4"
      :x-num-ticks="7"
      :x-formatter="xFormatter"
      :curve-type="CurveType.Basis"
      :legend-position="LegendPosition.TopRight"
      :hide-legend="false"
      :y-grid-line="true"
    />
  </div>
</template>
```

### [Stacked Line Chart](https://nuxtcharts.com/docs/charts/line-chart#stacked-line-chart)

To create stacked line charts, set the `stacked` prop to `true`. This will stack data series on top of each other, visualizing their cumulative total over time.

Preview Stacked.vue

### Line Chart

[](https://nuxtcharts.com/blocks/line-charts)

Desktop

Mobile

```
<script lang="ts" setup>
defineOptions({
  tags: ['linecharts', 'multilines']
})

withDefaults(
  defineProps<{
    showTitle?: boolean
  }>(),
  {
    showTitle: false
  }
)

const chartData = [
  { month: 'January', desktop: 186, mobile: 186 },
  { month: 'February', desktop: 305, mobile: 305 },
  { month: 'March', desktop: 237, mobile: 237 },
  { month: 'April', desktop: 260, mobile: 209 },
  { month: 'May', desktop: 209, mobile: 209 },
  { month: 'June', desktop: 250, mobile: 214 }
]

const categories: Record<string, BulletLegendItemInterface> = {
  desktop: { name: 'Desktop', color: '#3b82f6' },
  mobile: { name: 'Mobile', color: '#22c55e' }
}

const xFormatter = (tick: number, _i?: number, _ticks?: number[]): string => {
  return chartData[tick]?.month ?? ''
}
</script>

<template>
  <div
    class="mx-auto max-w-3xl space-y-6 rounded-lg"
    :class="showTitle ? 'p-6' : ''"
  >
    <div class="flex items-center justify-between">
      <h3 class="text-lg font-semibold">
        Line Chart
      </h3>
      <NuxtLink to="/blocks/line-charts">
        <UButton
          icon="i-lucide-copy"
          size="sm"
          variant="soft"
          color="neutral"
        />
      </NuxtLink>
    </div>
    <LineChart
      :data="chartData"
      :height="300"
      y-label="Number of visits"
      :x-num-ticks="2"
      :categories="categories"
      :x-formatter="xFormatter"
      :y-grid-line="true"
      :curve-type="CurveType.MonotoneX"
      :legend-position="LegendPosition.TopRight"
      :hide-legend="false"
    />
  </div>
</template>
```

### [Dash Array](https://nuxtcharts.com/docs/charts/line-chart#dash-array)

Preview DashArray.vue

### Line Chart

[](https://nuxtcharts.com/blocks/line-charts)

Desktop

Custom tooltip: 

```
<script lang="ts" setup>
defineOptions({
  tags: ['linecharts', 'dasharray']
})

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
</script>

<template>
  <div
    class="mx-auto max-w-3xl space-y-6 rounded-lg"
    :class="showTitle ? 'p-6' : ''"
  >
    <div class="flex items-center justify-between">
      <h3 class="text-lg font-semibold">
        Line Chart
      </h3>
      <NuxtLink to="/blocks/line-charts">
        <UButton
          icon="i-lucide-copy"
          size="sm"
          variant="soft"
          color="neutral"
        />
      </NuxtLink>
    </div>
    <LineChart
      :data="chartData"
      :height="300"
      x-label="Time"
      y-label="Temperature"
      :categories="categories"
      :y-num-ticks="4"
      :x-num-ticks="7"
      :line-dash-array="[[5, 5]]"
      :x-formatter="xFormatter"
      :legend-position="LegendPosition.TopRight"
      :hide-legend="false"
      :y-grid-line="true"
      @click="(e, data) => console.log('Chart clicked', data)"
    >
      <template #tooltip="{ values }">
        <div>Custom tooltip: {{ values }}</div>
      </template>
    </LineChart>
  </div>
</template>
```

[Props](https://nuxtcharts.com/docs/charts/line-chart#props)
------------------------------------------------------------

| Prop | Type | Default | Description |
| --- | --- | --- | --- |
| `data` | `T[]` | **Required** | Array of data points for the chart. Each element represents a data point. |
| `height` | `number` | **Required** | Height of the chart in pixels. |
| `xLabel` | `string` | `undefined` | Optional label for the x-axis. |
| `yLabel` | `string` | `undefined` | Optional label for the y-axis. |
| `padding` | `{ top: number; right: number; bottom: number; left: number; }` | `undefined` | Optional padding for the chart (top, right, bottom, left). |
| `categories` | `Record<string, BulletLegendItemInterface>` | **Required** | Series configuration: name and color for each data key. |
| `markerConfig` | `Record<string, MarkerConfig>` | `{}` | Marker configuration for each series. |
| `xFormatter` | `axisFormatter` | `undefined` | Formats X-axis labels. `(tick, i, ticks) => string` where tick can be a number or Date. |
| `yFormatter` | `axisFormatter` | `undefined` | Formats Y-axis labels. `(tick, i, ticks) => string` where tick can be a number or Date. |
| `curveType` | `CurveType` | `undefined` | Type of curve interpolation (see Curve Types section). |
| `stacked` | `boolean` | `false` | If true, the line chart will be stacked. |
| `lineWidth` | `number` | `2` | Width of the line in pixels. |
| `lineDashArray` | `number[][]` | `undefined` | SVG stroke-dasharray for dashed lines. |
| `xNumTicks` | `number` | `undefined` | Desired number of ticks on the x-axis. |
| `xExplicitTicks` | `(number | string | Date)` |
| `minMaxTicksOnly` | `boolean` | `false` | If true, only show first and last ticks on the x-axis. |
| `yNumTicks` | `number` | `undefined` | Desired number of ticks on the y-axis. |
| `hideLegend` | `boolean` | `false` | If true, hides the chart legend. |
| `hideTooltip` | `boolean` | `false` | If true, hides the chart tooltip. |
| `legendPosition` | `LegendPosition` | `undefined` | Position of the legend (see LegendPosition). |
| `legendStyle` | `string | Record<string, string>` | `undefined` | Custom CSS style for the legend container. |
| `xDomainLine` | `boolean` | `false` | Show domain (axis) line on the x-axis. |
| `yDomainLine` | `boolean` | `false` | Show domain (axis) line on the y-axis. |
| `xTickLine` | `boolean` | `false` | Show tick lines on the x-axis. |
| `yTickLine` | `boolean` | `false` | Show tick lines on the y-axis. |
| `xGridLine` | `boolean` | `false` | Show grid lines on the x-axis. |
| `yGridLine` | `boolean` | `false` | Show grid lines on the y-axis. |
| `hideXAxis` | `boolean` | `false` | If true, hides the x-axis. |
| `hideYAxis` | `boolean` | `false` | If true, hides the y-axis. |
| `xAxisConfig` | `AxisConfig` | `undefined` | Axis configuration for customizing the appearance of the x-axis. |
| `yAxisConfig` | `AxisConfig` | `undefined` | Axis configuration for customizing the appearance of the y-axis. |
| `crosshairConfig` | `CrosshairConfig` | `undefined` | Crosshair configuration for customizing the crosshair line. |
| `yDomain` | `[number | undefined, number | undefined]` | `undefined` | Domain for the y-axis. |
| `xDomain` | `[number | undefined, number | undefined]` | `undefined` | Domain for the x-axis. |
| `yExplicitTicks` | `(number | string | Date)[]` | `undefined` | Force specific ticks on the y-axis. |
| `xMinMaxTicksOnly` | `boolean` | `false` | If true, only show first and last ticks on the x-axis. |
| `yMinMaxTicksOnly` | `boolean` | `false` | If true, only show first and last ticks on the y-axis. |
| `minMaxTicksOnlyShowGridLines` | `boolean` | `false` | Show grid lines for min and max axis ticks. |
| `xMinMaxTicksOnlyShowGridLines` | `boolean` | `false` | Show grid lines for min and max x-axis ticks. |
| `yMinMaxTicksOnlyShowGridLines` | `boolean` | `false` | Show grid lines for min and max y-axis ticks. |
| `tooltipTitleFormatter` | `(data: T) => string | number` | `undefined` | Custom formatter for tooltip titles. |
| `tooltip` | `TooltipConfig` | `undefined` | Tooltip configuration (hideDelay, showDelay, followCursor). |
| `duration` | `number` | `undefined` | Animation duration in milliseconds. |

[Data Format](https://nuxtcharts.com/docs/charts/line-chart#data-format)
------------------------------------------------------------------------

The data should be an array of objects where each object represents a data point:

types.ts

```
interface LineChartData {
  [key: string]: string | number
}
```

[Categories Format](https://nuxtcharts.com/docs/charts/line-chart#categories-format)
------------------------------------------------------------------------------------

Categories define the visual appearance and metadata for each line:

types.ts

```
interface LineCategory {
  name: string
  color: string
}

interface LineCategories {
  [key: string]: LineCategory
}
```

[Curve Types](https://nuxtcharts.com/docs/charts/line-chart#curve-types)
------------------------------------------------------------------------

Available curve types for line interpolation in your Vue charts. These interpolation options give you precise control over how your data is visualized in Vue and Nuxt applications:

*   `linear` - Straight lines between points
*   `linearClosed` - Closed straight lines
*   `basis` - B-spline curves
*   `basisClosed` - Closed B-spline curves
*   `basisOpen` - Open B-spline curves
*   `bundle` - Bundle spline curves
*   `cardinal` - Cardinal spline curves
*   `cardinalClosed` - Closed cardinal spline curves
*   `cardinalOpen` - Open cardinal spline curves
*   `catmullRom` - Catmull-Rom spline curves
*   `catmullRomClosed` - Closed Catmull-Rom spline curves
*   `catmullRomOpen` - Open Catmull-Rom spline curves
*   `monotoneX` - Monotone cubic interpolation (X axis)
*   `monotoneY` - Monotone cubic interpolation (Y axis)
*   `natural` - Natural cubic spline
*   `step` - Step function
*   `stepBefore` - Step function (step before)
*   `stepAfter` - Step function (step after)

[Examples](https://nuxtcharts.com/docs/charts/line-chart#examples)
------------------------------------------------------------------

[Check out examples here ↗](https://nuxtcharts.com/charts)

[Bar Chart Implement vertical, horizontal, grouped, and stacked bar charts in your Nuxt application.](https://nuxtcharts.com/docs/charts/bar-chart)[Donut Chart Implement circular data visualizations with the Donut Chart component.](https://nuxtcharts.com/docs/charts/donut-chart)

Browse All Documentation

Table of Contents
Table of Contents

*   [Basic Usage](https://nuxtcharts.com/docs/charts/line-chart#basic-usage)
    *   [Multiple Lines](https://nuxtcharts.com/docs/charts/line-chart#multiple-lines)
    *   [Single Line](https://nuxtcharts.com/docs/charts/line-chart#single-line)
    *   [Stacked Line Chart](https://nuxtcharts.com/docs/charts/line-chart#stacked-line-chart)
    *   [Dash Array](https://nuxtcharts.com/docs/charts/line-chart#dash-array)

*   [Props](https://nuxtcharts.com/docs/charts/line-chart#props)
*   [Data Format](https://nuxtcharts.com/docs/charts/line-chart#data-format)
*   [Categories Format](https://nuxtcharts.com/docs/charts/line-chart#categories-format)
*   [Curve Types](https://nuxtcharts.com/docs/charts/line-chart#curve-types)
*   [Examples](https://nuxtcharts.com/docs/charts/line-chart#examples)

Support Nuxt Charts

*   [Follow on X](https://x.com/DennisAdriaans)
*   [Star on GitHub](https://github.com/dennisadriaans/vue-chrts)
*   [Purchase a All-Access](https://nuxtcharts.com/pricing)

SCROLL: 0px
