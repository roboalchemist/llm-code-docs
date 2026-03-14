# Source: https://nuxtcharts.com/docs/charts/bubble-chart

Title: Bubble Chart

URL Source: https://nuxtcharts.com/docs/charts/bubble-chart

Markdown Content:
Bubble Chart
===============

[Nuxt Charts v2](https://nuxtcharts.com/)

*   [Blocks](https://nuxtcharts.com/blocks)
*   [Docs](https://nuxtcharts.com/docs/getting-started/installation)
*   [Charts](https://nuxtcharts.com/charts)
*   [Templates](https://nuxtcharts.com/templates)
*   Apps
*   [Pricing](https://nuxtcharts.com/pricing)

menu

[](https://ui.nuxtcharts.com/)[](https://github.com/dennisadriaans/vue-chrts)[Sign In Sign In](https://nuxtcharts.com/docs/charts/bubble-chart)

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

Bubble Chart
============

Learn how to implement and customize Bubble Charts in your Nuxt application.

The `BubbleChart` component visualizes three variables by mapping data to x/y positions and bubble size, ideal for displaying multi-dimensional datasets.

[Basic Usage](https://nuxtcharts.com/docs/charts/bubble-chart#basic-usage)
--------------------------------------------------------------------------

Preview Basic.vue

Drama

Action/Thriller

Comedy

Documentary

Romance

Sci-Fi/Fantasy

Horror

```
<script lang="ts" setup>
defineOptions({
  tags: ['bubblecharts', 'basic']
})

const bubbleChartData = [
  {
    id: 'Drama-Jan',
    title: 'Drama',
    month: 1,
    viewingHours: 2.8,
    subscribers: 45
  },
  {
    id: 'Drama-Feb',
    title: 'Drama',
    month: 2,
    viewingHours: 2.9,
    subscribers: 48
  },
  {
    id: 'Drama-Mar',
    title: 'Drama',
    month: 3,
    viewingHours: 3.1,
    subscribers: 52
  },
  {
    id: 'Drama-Apr',
    title: 'Drama',
    month: 4,
    viewingHours: 2.7,
    subscribers: 46
  },
  {
    id: 'Drama-May',
    title: 'Drama',
    month: 5,
    viewingHours: 3.2,
    subscribers: 55
  },
  {
    id: 'Drama-Jun',
    title: 'Drama',
    month: 6,
    viewingHours: 3.0,
    subscribers: 50
  },
  {
    id: 'Drama-Jul',
    title: 'Drama',
    month: 7,
    viewingHours: 3.3,
    subscribers: 58
  },
  {
    id: 'Drama-Aug',
    title: 'Drama',
    month: 8,
    viewingHours: 3.1,
    subscribers: 53
  },
  {
    id: 'Drama-Sep',
    title: 'Drama',
    month: 9,
    viewingHours: 2.9,
    subscribers: 49
  },
  {
    id: 'Drama-Oct',
    title: 'Drama',
    month: 10,
    viewingHours: 3.4,
    subscribers: 60
  },
  {
    id: 'Drama-Nov',
    title: 'Drama',
    month: 11,
    viewingHours: 3.5,
    subscribers: 62
  },
  {
    id: 'Drama-Dec',
    title: 'Drama',
    month: 12,
    viewingHours: 3.6,
    subscribers: 65
  },

  // Action/Thriller
  {
    id: 'Action-Jan',
    title: 'Action/Thriller',
    month: 1,
    viewingHours: 2.5,
    subscribers: 42
  },
  {
    id: 'Action-Feb',
    title: 'Action/Thriller',
    month: 2,
    viewingHours: 2.6,
    subscribers: 44
  },
  {
    id: 'Action-Mar',
    title: 'Action/Thriller',
    month: 3,
    viewingHours: 2.8,
    subscribers: 48
  },
  {
    id: 'Action-Apr',
    title: 'Action/Thriller',
    month: 4,
    viewingHours: 2.4,
    subscribers: 40
  },
  {
    id: 'Action-May',
    title: 'Action/Thriller',
    month: 5,
    viewingHours: 2.9,
    subscribers: 50
  },
  {
    id: 'Action-Jun',
    title: 'Action/Thriller',
    month: 6,
    viewingHours: 2.7,
    subscribers: 46
  },
  {
    id: 'Action-Jul',
    title: 'Action/Thriller',
    month: 7,
    viewingHours: 3.0,
    subscribers: 52
  },
  {
    id: 'Action-Aug',
    title: 'Action/Thriller',
    month: 8,
    viewingHours: 2.8,
    subscribers: 48
  },
  {
    id: 'Action-Sep',
    title: 'Action/Thriller',
    month: 9,
    viewingHours: 2.6,
    subscribers: 44
  },
  {
    id: 'Action-Oct',
    title: 'Action/Thriller',
    month: 10,
    viewingHours: 3.1,
    subscribers: 54
  },
  {
    id: 'Action-Nov',
    title: 'Action/Thriller',
    month: 11,
    viewingHours: 3.2,
    subscribers: 56
  },
  {
    id: 'Action-Dec',
    title: 'Action/Thriller',
    month: 12,
    viewingHours: 3.3,
    subscribers: 58
  },

  // Comedy
  {
    id: 'Comedy-Jan',
    title: 'Comedy',
    month: 1,
    viewingHours: 2.2,
    subscribers: 38
  },
  {
    id: 'Comedy-Feb',
    title: 'Comedy',
    month: 2,
    viewingHours: 2.3,
    subscribers: 40
  },
  {
    id: 'Comedy-Mar',
    title: 'Comedy',
    month: 3,
    viewingHours: 2.5,
    subscribers: 43
  },
  {
    id: 'Comedy-Apr',
    title: 'Comedy',
    month: 4,
    viewingHours: 2.1,
    subscribers: 36
  },
  {
    id: 'Comedy-May',
    title: 'Comedy',
    month: 5,
    viewingHours: 2.6,
    subscribers: 45
  },
  {
    id: 'Comedy-Jun',
    title: 'Comedy',
    month: 6,
    viewingHours: 2.4,
    subscribers: 42
  },
  {
    id: 'Comedy-Jul',
    title: 'Comedy',
    month: 7,
    viewingHours: 2.7,
    subscribers: 47
  },
  {
    id: 'Comedy-Aug',
    title: 'Comedy',
    month: 8,
    viewingHours: 2.5,
    subscribers: 44
  },
  {
    id: 'Comedy-Sep',
    title: 'Comedy',
    month: 9,
    viewingHours: 2.3,
    subscribers: 40
  },
  {
    id: 'Comedy-Oct',
    title: 'Comedy',
    month: 10,
    viewingHours: 2.8,
    subscribers: 49
  },
  {
    id: 'Comedy-Nov',
    title: 'Comedy',
    month: 11,
    viewingHours: 2.9,
    subscribers: 51
  },
  {
    id: 'Comedy-Dec',
    title: 'Comedy',
    month: 12,
    viewingHours: 3.0,
    subscribers: 53
  },

  // Documentary
  {
    id: 'Doc-Jan',
    title: 'Documentary',
    month: 1,
    viewingHours: 1.8,
    subscribers: 30
  },
  {
    id: 'Doc-Feb',
    title: 'Documentary',
    month: 2,
    viewingHours: 1.9,
    subscribers: 32
  },
  {
    id: 'Doc-Mar',
    title: 'Documentary',
    month: 3,
    viewingHours: 2.1,
    subscribers: 35
  },
  {
    id: 'Doc-Apr',
    title: 'Documentary',
    month: 4,
    viewingHours: 1.7,
    subscribers: 28
  },
  {
    id: 'Doc-May',
    title: 'Documentary',
    month: 5,
    viewingHours: 2.2,
    subscribers: 37
  },
  {
    id: 'Doc-Jun',
    title: 'Documentary',
    month: 6,
    viewingHours: 2.0,
    subscribers: 34
  },
  {
    id: 'Doc-Jul',
    title: 'Documentary',
    month: 7,
    viewingHours: 2.3,
    subscribers: 39
  },
  {
    id: 'Doc-Aug',
    title: 'Documentary',
    month: 8,
    viewingHours: 2.1,
    subscribers: 36
  },
  {
    id: 'Doc-Sep',
    title: 'Documentary',
    month: 9,
    viewingHours: 1.9,
    subscribers: 32
  },
  {
    id: 'Doc-Oct',
    title: 'Documentary',
    month: 10,
    viewingHours: 2.4,
    subscribers: 41
  },
  {
    id: 'Doc-Nov',
    title: 'Documentary',
    month: 11,
    viewingHours: 2.5,
    subscribers: 43
  },
  {
    id: 'Doc-Dec',
    title: 'Documentary',
    month: 12,
    viewingHours: 2.6,
    subscribers: 45
  },

  // Romance
  {
    id: 'Romance-Jan',
    title: 'Romance',
    month: 1,
    viewingHours: 1.9,
    subscribers: 32
  },
  {
    id: 'Romance-Feb',
    title: 'Romance',
    month: 2,
    viewingHours: 2.4,
    subscribers: 41
  },
  {
    id: 'Romance-Mar',
    title: 'Romance',
    month: 3,
    viewingHours: 2.2,
    subscribers: 38
  },
  {
    id: 'Romance-Apr',
    title: 'Romance',
    month: 4,
    viewingHours: 1.8,
    subscribers: 30
  },
  {
    id: 'Romance-May',
    title: 'Romance',
    month: 5,
    viewingHours: 2.3,
    subscribers: 40
  },
  {
    id: 'Romance-Jun',
    title: 'Romance',
    month: 6,
    viewingHours: 2.1,
    subscribers: 36
  },
  {
    id: 'Romance-Jul',
    title: 'Romance',
    month: 7,
    viewingHours: 2.4,
    subscribers: 42
  },
  {
    id: 'Romance-Aug',
    title: 'Romance',
    month: 8,
    viewingHours: 2.2,
    subscribers: 38
  },
  {
    id: 'Romance-Sep',
    title: 'Romance',
    month: 9,
    viewingHours: 2.0,
    subscribers: 34
  },
  {
    id: 'Romance-Oct',
    title: 'Romance',
    month: 10,
    viewingHours: 2.5,
    subscribers: 44
  },
  {
    id: 'Romance-Nov',
    title: 'Romance',
    month: 11,
    viewingHours: 2.6,
    subscribers: 46
  },
  {
    id: 'Romance-Dec',
    title: 'Romance',
    month: 12,
    viewingHours: 2.7,
    subscribers: 48
  },

  // Sci-Fi/Fantasy
  {
    id: 'SciFi-Jan',
    title: 'Sci-Fi/Fantasy',
    month: 1,
    viewingHours: 2.1,
    subscribers: 35
  },
  {
    id: 'SciFi-Feb',
    title: 'Sci-Fi/Fantasy',
    month: 2,
    viewingHours: 2.2,
    subscribers: 37
  },
  {
    id: 'SciFi-Mar',
    title: 'Sci-Fi/Fantasy',
    month: 3,
    viewingHours: 2.4,
    subscribers: 41
  },
  {
    id: 'SciFi-Apr',
    title: 'Sci-Fi/Fantasy',
    month: 4,
    viewingHours: 2.0,
    subscribers: 33
  },
  {
    id: 'SciFi-May',
    title: 'Sci-Fi/Fantasy',
    month: 5,
    viewingHours: 2.5,
    subscribers: 43
  },
  {
    id: 'SciFi-Jun',
    title: 'Sci-Fi/Fantasy',
    month: 6,
    viewingHours: 2.3,
    subscribers: 39
  },
  {
    id: 'SciFi-Jul',
    title: 'Sci-Fi/Fantasy',
    month: 7,
    viewingHours: 2.6,
    subscribers: 45
  },
  {
    id: 'SciFi-Aug',
    title: 'Sci-Fi/Fantasy',
    month: 8,
    viewingHours: 2.4,
    subscribers: 42
  },
  {
    id: 'SciFi-Sep',
    title: 'Sci-Fi/Fantasy',
    month: 9,
    viewingHours: 2.2,
    subscribers: 38
  },
  {
    id: 'SciFi-Oct',
    title: 'Sci-Fi/Fantasy',
    month: 10,
    viewingHours: 2.7,
    subscribers: 47
  },
  {
    id: 'SciFi-Nov',
    title: 'Sci-Fi/Fantasy',
    month: 11,
    viewingHours: 2.8,
    subscribers: 49
  },
  {
    id: 'SciFi-Dec',
    title: 'Sci-Fi/Fantasy',
    month: 12,
    viewingHours: 2.9,
    subscribers: 51
  },

  // Horror
  {
    id: 'Horror-Jan',
    title: 'Horror',
    month: 1,
    viewingHours: 1.5,
    subscribers: 25
  },
  {
    id: 'Horror-Feb',
    title: 'Horror',
    month: 2,
    viewingHours: 1.6,
    subscribers: 27
  },
  {
    id: 'Horror-Mar',
    title: 'Horror',
    month: 3,
    viewingHours: 1.7,
    subscribers: 29
  },
  {
    id: 'Horror-Apr',
    title: 'Horror',
    month: 4,
    viewingHours: 1.4,
    subscribers: 23
  },
  {
    id: 'Horror-May',
    title: 'Horror',
    month: 5,
    viewingHours: 1.8,
    subscribers: 30
  },
  {
    id: 'Horror-Jun',
    title: 'Horror',
    month: 6,
    viewingHours: 1.6,
    subscribers: 27
  },
  {
    id: 'Horror-Jul',
    title: 'Horror',
    month: 7,
    viewingHours: 1.9,
    subscribers: 32
  },
  {
    id: 'Horror-Aug',
    title: 'Horror',
    month: 8,
    viewingHours: 1.7,
    subscribers: 29
  },
  {
    id: 'Horror-Sep',
    title: 'Horror',
    month: 9,
    viewingHours: 1.6,
    subscribers: 27
  },
  {
    id: 'Horror-Oct',
    title: 'Horror',
    month: 10,
    viewingHours: 2.3,
    subscribers: 39
  },
  {
    id: 'Horror-Nov',
    title: 'Horror',
    month: 11,
    viewingHours: 2.0,
    subscribers: 34
  },
  {
    id: 'Horror-Dec',
    title: 'Horror',
    month: 12,
    viewingHours: 1.8,
    subscribers: 30
  }
]

const categories1 = {
  'Drama': { name: 'Drama', color: 'var(--color-red-400)' },
  'Action/Thriller': {
    name: 'Action/Thriller',
    color: 'var(--color-orange-400)'
  },
  'Comedy': { name: 'Comedy', color: 'var(--color-yellow-400)' },
  'Documentary': { name: 'Documentary', color: 'var(--color-blue-400)' },
  'Romance': { name: 'Romance', color: 'var(--color-pink-400)' },
  'Sci-Fi/Fantasy': {
    name: 'Sci-Fi/Fantasy',
    color: 'var(--color-green-400)'
  },
  'Horror': { name: 'Horror', color: 'var(--color-purple-400)' }
}

const monthNames = [
  'Jan',
  'Feb',
  'Mar',
  'Apr',
  'May',
  'Jun',
  'Jul',
  'Aug',
  'Sep',
  'Oct',
  'Nov',
  'Dec'
]

function formatNumber(tick: number | Date): string {
  return typeof tick === 'number' ? tick.toFixed(1) : String(tick)
}

const xAccessor1 = (d: any) => d.month
const yAccessor1 = (d: any) => d.viewingHours
const sizeAccessor1 = (d: any) => d.subscribers
</script>

<template>
  <BubbleChart
    :data="bubbleChartData"
    :height="230"
    :categories="categories1"
    category-key="title"
    :x-accessor="xAccessor1"
    :y-accessor="yAccessor1"
    :y-domain-line="false"
    :size-accessor="sizeAccessor1"
    :legend-position="LegendPosition.BottomRight"
    :x-num-ticks="12"
    :x-formatter="(tick: number) => monthNames[tick - 1] ?? String(tick)"
    :y-formatter="(v: number | Date) => `${formatNumber(v)}B hrs`"
  />
</template>
```

[Props](https://nuxtcharts.com/docs/charts/bubble-chart#props)
--------------------------------------------------------------

| Prop | Type | Default | Description |
| --- | --- | --- | --- |
| `data` | `T[]` | **Required** | Array of data points for the chart. Each element represents a data point. |
| `height` | `number` | **Required** | Height of the chart in pixels. |
| `categories` | `Record<string, BulletLegendItemInterface>` | **Required** | Series configuration: name and color for each data key. Each unique value in your data's categoryKey field must have a corresponding entry with a color. |
| `categoryKey` | `keyof T` | **Required** | Key to access the category from the data item. |
| `xAccessor` | `NumericAccessor<T>` | `undefined` | Accessor for x value (index, property, etc). If not provided, defaults to d.beakLength. |
| `yAccessor` | `NumericAccessor<T>` | `undefined` | Accessor for y value. If not provided, defaults to d.flipperLength. |
| `sizeAccessor` | `NumericAccessor<T>` | `undefined` | Accessor for bubble size. If not provided, defaults to 1. |
| `xLabel` | `string` | `undefined` | Optional label for the x-axis. |
| `yLabel` | `string` | `undefined` | Optional label for the y-axis. |
| `padding` | `{ top: number; right: number; bottom: number; left: number; }` | `undefined` | Optional padding for the chart (top, right, bottom, left). |
| `xFormatter` | `axisFormatter` | `undefined` | Formats X-axis labels. `(tick, i, ticks) => string` where tick can be a number or Date. |
| `yFormatter` | `axisFormatter` | `undefined` | Formats Y-axis labels. `(tick, i, ticks) => string` where tick can be a number or Date. |
| `labelPosition` | `Position` | `Position.Bottom` | Label position for bubbles. |
| `sizeRange` | `[number, number]` | `[1, 20]` | Range for bubble sizes. |
| `opacity` | `number` | `undefined` | Opacity for bubbles. |
| `xExplicitTicks` | `(number | string | Date)` |
| `minMaxTicksOnly` | `boolean` | `false` | Only show min/max ticks for x axis. |
| `xNumTicks` | `number` | `undefined` | Desired number of ticks on the x-axis. |
| `yNumTicks` | `number` | `undefined` | Desired number of ticks on the y-axis. |
| `hideLegend` | `boolean` | `false` | If true, hides the chart legend. |
| `hideTooltip` | `boolean` | `false` | If true, hides the tooltip. |
| `legendPosition` | `LegendPosition` | `undefined` | Position of the legend (see LegendPosition). |
| `legendStyle` | `Record<string, string>` | `undefined` | Optional inline CSS styles for the legend container. |
| `sizeOptions` | `SizeOptions` | `undefined` | Options for controlling bubble sizes (minRadius, maxRadius). |
| `xDomainLine` | `boolean` | `false` | Show domain (axis) line on the x-axis. |
| `yDomainLine` | `boolean` | `false` | Show domain (axis) line on the y-axis. |
| `xTickLine` | `boolean` | `false` | Show tick lines on the x-axis. |
| `yTickLine` | `boolean` | `false` | Show tick lines on the y-axis. |
| `xGridLine` | `boolean` | `false` | Show grid lines on the x-axis. |
| `yGridLine` | `boolean` | `false` | Show grid lines on the y-axis. |
| `hideXAxis` | `boolean` | `false` | If true, hides the x-axis. |
| `hideYAxis` | `boolean` | `false` | If true, hides the y-axis. |
| `crosshairConfig` | `CrosshairConfig` | `undefined` | Crosshair configuration for customizing the crosshair line. |
| `xAxisConfig` | `AxisConfig` | `undefined` | Axis configuration for customizing the appearance of the x-axis. |
| `yAxisConfig` | `AxisConfig` | `undefined` | Axis configuration for customizing the appearance of the y-axis. |
| `tooltipTitleFormatter` | `(data: T) => string | number` | `undefined` | Custom formatter for tooltip titles. |
| `tooltip` | `TooltipConfig` | `undefined` | Tooltip configuration (hideDelay, showDelay, followCursor). |
| `duration` | `number` | `undefined` | Animation duration in milliseconds. |

[Data Format](https://nuxtcharts.com/docs/charts/bubble-chart#data-format)
--------------------------------------------------------------------------

The data for your Vue charts should be an array of objects where each object represents a bubble.

types.ts

```
interface BubbleChartData {
  id: string
  title: string
  month: number
  viewingHours: number
  subscribers: number
  [key: string]: any
}
```

[Categories Format](https://nuxtcharts.com/docs/charts/bubble-chart#categories-format)
--------------------------------------------------------------------------------------

Categories define the visual appearance and metadata for each bubble series.

types.ts

```
interface BubbleCategory {
  name: string
  color: string
}

interface BubbleCategories {
  [key: string]: BubbleCategory
}
```

[Donut Chart Implement circular data visualizations with the Donut Chart component.](https://nuxtcharts.com/docs/charts/donut-chart)[Gantt Charts A Gantt Chart or timeline that displays a list of events in chronological order.](https://nuxtcharts.com/docs/charts/gantt-chart)

Browse All Documentation

Table of Contents
Table of Contents

*   [Basic Usage](https://nuxtcharts.com/docs/charts/bubble-chart#basic-usage)
*   [Props](https://nuxtcharts.com/docs/charts/bubble-chart#props)
*   [Data Format](https://nuxtcharts.com/docs/charts/bubble-chart#data-format)
*   [Categories Format](https://nuxtcharts.com/docs/charts/bubble-chart#categories-format)

Support Nuxt Charts

*   [Follow on X](https://x.com/DennisAdriaans)
*   [Star on GitHub](https://github.com/dennisadriaans/vue-chrts)
*   [Purchase a All-Access](https://nuxtcharts.com/pricing)

SCROLL: 0px
