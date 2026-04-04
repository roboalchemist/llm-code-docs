# Source: https://nuxtcharts.com/docs/charts/bar-chart

Title: Bar Chart

URL Source: https://nuxtcharts.com/docs/charts/bar-chart

Markdown Content:
Bar Chart
===============

[Nuxt Charts v2](https://nuxtcharts.com/)

*   [Blocks](https://nuxtcharts.com/blocks)
*   [Docs](https://nuxtcharts.com/docs/getting-started/installation)
*   [Charts](https://nuxtcharts.com/charts)
*   [Templates](https://nuxtcharts.com/templates)
*   Apps
*   [Pricing](https://nuxtcharts.com/pricing)

menu

[](https://ui.nuxtcharts.com/)[](https://github.com/dennisadriaans/vue-chrts)[Sign In Sign In](https://nuxtcharts.com/docs/charts/bar-chart)

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

Bar Chart
=========

Implement vertical, horizontal, grouped, and stacked bar charts in your Nuxt application.

The `BarChart` component displays categorical data as vertical or horizontal bars. As a strong chart type for Vue charts, it supports grouped, stacked, and combined layouts for flexible data visualization in Nuxt and Vue projects. [Examples ↗](https://nuxtcharts.com/charts)

[Basic Usage](https://nuxtcharts.com/docs/charts/bar-chart#basic-usage)
-----------------------------------------------------------------------

Preview Vertical.vue

### Bar Chart

[](https://nuxtcharts.com/blocks/bar-charts)

Desktop

```
<script lang="ts" setup>
defineOptions({
  tags: ['barcharts', 'vertical']
})

withDefaults(
  defineProps<{
    showTitle?: boolean
  }>(),
  {
    showTitle: false
  }
)

const RevenueData = [
  { month: 'January', desktop: 186, mobile: 80 },
  { month: 'February', desktop: 305, mobile: 200 },
  { month: 'March', desktop: 237, mobile: 120 },
  { month: 'April', desktop: 73, mobile: 190 },
  { month: 'May', desktop: 209, mobile: 130 },
  { month: 'June', desktop: 214, mobile: 140 }
]

const RevenueCategories = computed(() => ({
  desktop: {
    name: 'Desktop',
    color: '#22c55e'
  }
}))

const xFormatter = (i: number): string => `${RevenueData[i]?.month}`
const yFormatter = (tick: number) => tick.toString()
</script>

<template>
  <div
    class="mx-auto max-w-3xl space-y-6 rounded-lg"
    :class="showTitle ? 'p-6' : ''"
  >
    <div class="flex items-center justify-between">
      <h3 class="text-lg font-semibold">
        Bar Chart
      </h3>
      <NuxtLink to="/blocks/bar-charts">
        <UButton
          icon="i-lucide-copy"
          size="sm"
          variant="soft"
          color="neutral"
        />
      </NuxtLink>
    </div>
    <BarChart
      :data="RevenueData"
      :height="300"
      :categories="RevenueCategories"
      :y-axis="['desktop']"
      :x-num-ticks="6"
      :radius="4"
      :y-grid-line="true"
      :x-formatter="xFormatter"
      :y-formatter="yFormatter"
      :legend-position="LegendPosition.TopRight"
      :hide-legend="false"
    />
  </div>
</template>
```

### [Stacked Horizontal Bar Chart](https://nuxtcharts.com/docs/charts/bar-chart#stacked-horizontal-bar-chart)

Preview StackedHorizontal.vue

Development

Security

Testing

Monitoring

Marketing

Sales

Design

```
<script lang="ts" setup>
defineOptions({
  tags: ['barcharts', 'stackedhorizontal']
})

const RevenueData = [
  { month: 'January', desktop: 186, mobile: 80 },
  { month: 'February', desktop: 305, mobile: 200 },
  { month: 'March', desktop: 237, mobile: 120 },
  { month: 'April', desktop: 73, mobile: 190 },
  { month: 'May', desktop: 209, mobile: 130 },
  { month: 'June', desktop: 214, mobile: 140 }
]
const RevenueCategoriesMultple = {
  desktop: { name: 'Desktop', color: '#3b82f6' },
  mobile: { name: 'Mobile', color: '#22c55e' }
}

const yFormatter = (i: number): string => `${RevenueData[i]?.month}`
</script>

<template>
  <BarChart
    :data="RevenueData"
    :stacked="true"
    :height="300"
    :categories="RevenueCategoriesMultple"
    :y-axis="['desktop', 'mobile']"
    :group-padding="0"
    :bar-padding="0.2"
    :x-num-ticks="6"
    :radius="4"
    :orientation="Orientation.Horizontal"
    :x-formatter="(i) => i"
    :y-formatter="yFormatter"
    :legend-position="LegendPosition.TopRight"
    :hide-legend="false"
    :x-grid-line="true"
  />
</template>
```

### [Grouped Bar Chart](https://nuxtcharts.com/docs/charts/bar-chart#grouped-bar-chart)

Preview Group.vue

### Bar Chart

[](https://nuxtcharts.com/blocks/bar-charts)

Desktop

Mobile

```
<script lang="ts" setup>
defineOptions({
  tags: ['barcharts', 'group']
})

withDefaults(
  defineProps<{
    showTitle?: boolean
  }>(),
  {
    showTitle: false
  }
)

type RevenueDataItem = {
  month: string
  desktop: number
  mobile: number
}

const RevenueData: RevenueDataItem[] = [
  { month: 'January', desktop: 186, mobile: 80 },
  { month: 'February', desktop: 305, mobile: 200 },
  { month: 'March', desktop: 237, mobile: 120 },
  { month: 'April', desktop: 73, mobile: 190 },
  { month: 'May', desktop: 209, mobile: 130 },
  { month: 'June', desktop: 214, mobile: 140 }
]

const RevenueCategoriesMultple = {
  desktop: { name: 'Desktop', color: '#3b82f6' },
  mobile: { name: 'Mobile', color: '#22c55e' }
}

const xFormatter = (i: number): string => `${RevenueData[i]?.month}`
const yFormatter = (tick: number) => tick.toString()
</script>

<template>
  <div
    class="mx-auto max-w-3xl space-y-6 rounded-lg"
    :class="showTitle ? 'p-6' : ''"
  >
    <div class="flex items-center justify-between">
      <h3 class="text-lg font-semibold">
        Bar Chart
      </h3>
      <NuxtLink to="/blocks/bar-charts">
        <UButton
          icon="i-lucide-copy"
          size="sm"
          variant="soft"
          color="neutral"
        />
      </NuxtLink>
    </div>
    <BarChart
      :data="RevenueData"
      :height="300"
      :categories="RevenueCategoriesMultple"
      :y-axis="['desktop', 'mobile']"
      :group-padding="0"
      :bar-padding="0.2"
      :x-num-ticks="6"
      :radius="4"
      :x-formatter="xFormatter"
      :y-formatter="yFormatter"
      :legend-position="LegendPosition.TopRight"
      :hide-legend="false"
      :y-grid-line="true"
    />
  </div>
</template>
```

### [Stacked Bar Chart](https://nuxtcharts.com/docs/charts/bar-chart#stacked-bar-chart)

To create stacked bar charts, set the `stacked` prop to `true`. This will stack data series on top of each other instead of grouping them side by side.

Preview Stacked.vue

### Bar Chart

[](https://nuxtcharts.com/blocks/bar-charts)

Desktop

Mobile

```
<script lang="ts" setup>
defineOptions({
  tags: ['barcharts', 'stacked']
})

withDefaults(
  defineProps<{
    showTitle?: boolean
  }>(),
  {
    showTitle: false
  }
)

type RevenueDataItem = {
  month: string
  desktop: number
  mobile: number
}

const RevenueData: RevenueDataItem[] = [
  { month: 'January', desktop: 186, mobile: 80 },
  { month: 'February', desktop: 305, mobile: 200 },
  { month: 'March', desktop: 237, mobile: 120 },
  { month: 'April', desktop: 73, mobile: 190 },
  { month: 'May', desktop: 209, mobile: 130 },
  { month: 'June', desktop: 214, mobile: 140 }
]
const RevenueCategoriesMultple = {
  desktop: { name: 'Desktop', color: '#3b82f6' },
  mobile: { name: 'Mobile', color: '#22c55e' }
}
const xFormatter = (i: number): string => `${RevenueData[i]?.month}`
const yFormatter = (tick: number, _i?: number, _ticks?: number[]) =>
  tick.toString()
</script>

<template>
  <div
    class="mx-auto max-w-3xl space-y-6 rounded-lg"
    :class="showTitle ? 'p-6' : ''"
  >
    <div class="flex items-center justify-between">
      <h3 class="text-lg font-semibold">
        Bar Chart
      </h3>
      <NuxtLink to="/blocks/bar-charts">
        <UButton
          icon="i-lucide-copy"
          size="sm"
          variant="soft"
          color="neutral"
        />
      </NuxtLink>
    </div>
    <BarChart
      :data="RevenueData"
      :stacked="true"
      :height="300"
      :categories="RevenueCategoriesMultple"
      :y-axis="['desktop', 'mobile']"
      :group-padding="0"
      :bar-padding="0.2"
      :x-num-ticks="6"
      :radius="4"
      :x-formatter="xFormatter"
      :y-formatter="yFormatter"
      :legend-position="LegendPosition.TopRight"
      :hide-legend="false"
      :y-grid-line="true"
    />
  </div>
</template>
```

### [Chart with Value Labels](https://nuxtcharts.com/docs/charts/bar-chart#chart-with-value-labels)

Preview Stacked.vue

Desktop

Mobile

```
<script lang="ts" setup>
defineOptions({
  tags: ['barcharts', 'withvaluelabel']
})

type DataProps = {
  month?: string
  desktop?: number
  mobile?: number
  date?: string
  value?: number
  visitors?: number
}

const RevenueCategoriesMultiple = {
  desktop: { name: 'Desktop', color: '#3b82f6' },
  mobile: { name: 'Mobile', color: '#22c55e' }
}

const RevenueData: DataProps[] = [
  { month: 'january', desktop: 186, mobile: 80 },
  { month: 'february', desktop: 305, mobile: 200 },
  { month: 'march', desktop: 237, mobile: 120 },
  { month: 'april', desktop: 73, mobile: 190 },
  { month: 'may', desktop: 209, mobile: 130 },
  { month: 'jun', desktop: 214, mobile: 140 }
]

const options = {
  data: RevenueData,
  categories: RevenueCategoriesMultiple,
  valueLabel: {
    label: d => d.y.toString(),
    labelSpacing: 16,
    labelFontSize: 10,
    color: 'var(--ui-text)'

  },
  xNumTicks: 6,
  xAxis: 'month' as keyof DataProps,
  groupPadding: 0,
  barPadding: 0.2,
  xFormatter: (tick: number, i?: number) =>
    `${RevenueData[typeof i !== 'undefined' ? i : tick]?.month}`,
  yFormatter: (tick: number, i?: number) =>
    `${typeof i !== 'undefined' ? tick : tick}`
}
</script>

<template>
  <div>
    <BarChart
      :height="300"
      :y-axis="['desktop', 'mobile']"
      v-bind="options"
    />
  </div>
</template>
```

[Props](https://nuxtcharts.com/docs/charts/bar-chart#props)
-----------------------------------------------------------

| Prop | Type | Default | Description |
| --- | --- | --- | --- |
| `data` | `T[]` | **Required** | Array of data points for the chart. Each element represents a data point. |
| `height` | `number` | **Required** | Height of the chart in pixels. |
| `categories` | `Record<string, BulletLegendItemInterface>` | **Required** | Series configuration: name and color for each data key. |
| `stacked` | `boolean` | `false` | If true, displays stacked bars instead of grouped bars. |
| `stackAndGrouped` | `boolean` | `false` | If true, enables both stacked and grouped bars. |
| `yAxis` | `(keyof T)[]` | **Required** | Array of property keys from the data object to display on the y-axis. |
| `xAxis` | `keyof T` | `undefined` | The data key for the x-axis (required for stackAndGrouped or with valueLabel). |
| `xLabel` | `string` | `undefined` | Optional label for the x-axis. |
| `yLabel` | `string` | `undefined` | Optional label for the y-axis. |
| `padding` | `{ top: number; right: number; bottom: number; left: number; }` | `undefined` | Optional padding for the chart (top, right, bottom, left). |
| `xFormatter` | `axisFormatter` | `undefined` | Formats x-axis labels. `(tick, i, ticks) => string` where tick can be a number or Date. |
| `yFormatter` | `axisFormatter` | `undefined` | Formats y-axis labels. `(tick, i, ticks) => string` where tick can be a number or Date. |
| `xNumTicks` | `number` | `undefined` | Desired number of ticks on the x-axis. |
| `yNumTicks` | `number` | `undefined` | Desired number of ticks on the y-axis. |
| `xExplicitTicks` | `(number | string | Date)` |
| `minMaxTicksOnly` | `boolean` | `false` | If true, only show first and last ticks on the x-axis. |
| `groupPadding` | `number` | `undefined` | Padding between groups of bars in pixels. |
| `barPadding` | `number` | `0` | Fractional padding between bars (0-1). |
| `radius` | `boolean | number` | `2` | Rounded corners for top bars (boolean or pixel value). |
| `hideLegend` | `boolean` | `false` | If true, hides the chart legend. |
| `hideTooltip` | `boolean` | `false` | If true, hides the chart tooltip. |
| `legendPosition` | `LegendPosition` | `undefined` | Position of the legend (see LegendPosition). |
| `legendStyle` | `string | Record<string, string>` | `undefined` | Custom CSS style for the legend container. |
| `orientation` | `Orientation` | `'vertical'` | Orientation of the bars (vertical or horizontal). |
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
| `stackedGroupedSpacing` | `number` | `undefined` | Spacing between stacked and grouped bars (only for stackAndGrouped). |
| `valueLabel` | `ValueLabel` | `undefined` | Configuration for value label display (see ValueLabel). |
| `tooltipTitleFormatter` | `(data: T) => string | number` | `undefined` | Custom formatter for tooltip titles. |
| `tooltip` | `TooltipConfig` | `undefined` | Tooltip configuration (hideDelay, showDelay, followCursor). |
| `duration` | `number` | `undefined` | Animation duration in milliseconds. |

[Data Format](https://nuxtcharts.com/docs/charts/bar-chart#data-format)
-----------------------------------------------------------------------

The data for Vue charts should be an array of objects where each object represents a data point:

types.ts

```
interface ChartData {
  [key: string]: string | number
}
```

[Categories Format](https://nuxtcharts.com/docs/charts/bar-chart#categories-format)
-----------------------------------------------------------------------------------

Categories define the visual appearance and metadata for each data series:

types.ts

```
interface Category {
  name: string
  color: string
}

interface Categories {
  [key: string]: Category
}
```

[Examples](https://nuxtcharts.com/docs/charts/bar-chart#examples)
-----------------------------------------------------------------

[Check out examples here ↗](https://nuxtcharts.com/charts)

[Area Chart Learn how to implement and customize Area Charts in your Nuxt application using Vue charts.](https://nuxtcharts.com/docs/charts/area-chart)[Line Chart Create single and multiple line visualizations in your Nuxt application using Vue charts.](https://nuxtcharts.com/docs/charts/line-chart)

Browse All Documentation

Table of Contents
Table of Contents

*   [Basic Usage](https://nuxtcharts.com/docs/charts/bar-chart#basic-usage)
    *   [Stacked Horizontal Bar Chart](https://nuxtcharts.com/docs/charts/bar-chart#stacked-horizontal-bar-chart)
    *   [Grouped Bar Chart](https://nuxtcharts.com/docs/charts/bar-chart#grouped-bar-chart)
    *   [Stacked Bar Chart](https://nuxtcharts.com/docs/charts/bar-chart#stacked-bar-chart)
    *   [Chart with Value Labels](https://nuxtcharts.com/docs/charts/bar-chart#chart-with-value-labels)

*   [Props](https://nuxtcharts.com/docs/charts/bar-chart#props)
*   [Data Format](https://nuxtcharts.com/docs/charts/bar-chart#data-format)
*   [Categories Format](https://nuxtcharts.com/docs/charts/bar-chart#categories-format)
*   [Examples](https://nuxtcharts.com/docs/charts/bar-chart#examples)

Support Nuxt Charts

*   [Follow on X](https://x.com/DennisAdriaans)
*   [Star on GitHub](https://github.com/dennisadriaans/vue-chrts)
*   [Purchase a All-Access](https://nuxtcharts.com/pricing)

SCROLL: 0px
