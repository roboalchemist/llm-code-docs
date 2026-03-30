# Source: https://nuxtcharts.com/docs/charts/donut-chart

Title: Donut Chart

URL Source: https://nuxtcharts.com/docs/charts/donut-chart

Markdown Content:
The `DonutChart` component visualizes proportional data as circular segments with customizable colors and legends. Use it to display percentage-based data in Vue and Nuxt apps. [Examples ↗](https://nuxtcharts.com/charts)

Label

2 seconds ago

Label

2 seconds ago

Product A

Product B

Product C

Product D

Other

| Prop | Type | Default | Description |
| --- | --- | --- | --- |
| `type` | `DonutType` | `'full'` | The type of donut chart to render. See `DonutType` for available options (`half` or `full`). |
| `data` | `number[]` | **required** | The data to be displayed in the donut chart. Each number in the array represents a segment value. |
| `arcWidth` | `number` |  | The arc width of the chart in pixels. |
| `height` | `number` | **required** | The height of the chart in pixels. |
| `radius` | `number` | **required** | The radius of the donut in pixels. |
| `hideLegend` | `boolean` | `false` | If `true`, hides the chart legend. |
| `legendPosition` | `LegendPosition` |  | Optional position for the legend, if applicable. See `LegendPosition` for available options. |
| `legendStyle` | `string | Record<string, string>` |  | Optional style object for the legend container. Allows custom CSS styling. |
| `categories` | `Record<string, BulletLegendItemInterface>` | **required** | A record mapping category keys to `BulletLegendItemInterface` objects. This defines the visual representation and labels for each category in the chart's legend. |
| `padAngle` | `number` | `0` | Pad angle between segments in radians. |
| `tooltipTitleFormatter` | `(data: T) => string | number` | `undefined` | Custom formatter for tooltip titles. |
| `hideTooltip` | `boolean` | `false` | If `true`, hides the chart tooltip. |
| `tooltip` | `TooltipConfig` | `undefined` | Tooltip configuration (hideDelay, showDelay, followCursor). |
| `duration` | `number` | `undefined` | Animation duration in milliseconds. |

The data should be an array of numbers where each number represents a segment value:

```
type DonutChartData = number[]
```

Categories define the visual appearance and labels for each segment in the chart's legend:

```
interface BulletLegendItemInterface {
  name: string
  color: string
}

type DonutCategories = Record<string, BulletLegendItemInterface>
```

```
<script setup lang="ts">
const data = ref([35, 25, 20, 15, 5])

const labels = [
  { name: 'Product A', color: '#3b82f6' },
  { name: 'Product B', color: '#22c55e' },
  { name: 'Product C', color: '#f59e0b' },
  { name: 'Product D', color: '#a855f7' },
  { name: 'Other', color: '#06b6d4' },
]

const categories: Record<string, BulletLegendItemInterface> =
  Object.fromEntries(
    labels.map((i) => [i.name, { name: i.name, color: i.color }]),
  )
</script>

<template>
  <DonutChart
    :data="data"
    :height="260"
    :categories="categories"
    :radius="4"
    :arc-width="20"
    :pad-angle="0.1"
  />
</template>
```

The `DonutChart` uses the **keys** of the `categories` object to determine the labels shown in the default tooltip. To ensure your tooltips look "nice and cool", use display-ready strings as keys.

```
// ❌ Technical keys lead to technical tooltips
const categories = {
  cpu: { name: 'CPU Usage', color: 'red' }
}

// ✅ Display keys lead to clean tooltips
const categories = {
  'CPU Usage': { name: 'CPU Usage', color: 'red' }
}
```

### [Understanding Radius](https://nuxtcharts.com/docs/charts/donut-chart#understanding-radius)

In this component, the `radius` prop often controls the **corner radius** (segment rounding) rather than the outer radius of the chart.

*   **Keep it small:** Values between `2` and `8` provide a modern, rounded look.
*   **Avoid large values:** Setting `radius` to a high value (like `80` or `100` on a small chart) can distort the segments and break the tooltip interactive areas.

To adjust the physical dimensions of the donut, use `height` and `arcWidth` instead of `radius`:

*   **`height`**: Controls the overall size of the SVG container.
*   **`arcWidth`**: Controls the thickness of the donut ring (and the size of the inner hole).

Available donut chart types:

*   `DonutType.Half` or `'half'` - Half donut chart
*   `DonutType.Full` or `'full'` - Full donut chart (default)

Available legend positions:

*   `LegendPosition.TopRight` - Top right of the chart
*   `LegendPosition.BottomRight` - Bottom right of the chart
*   `LegendPosition.Left` - Left of the chart
*   `LegendPosition.Right` - Right of the chart

The `DonutChart` component for Vue charts can be customized using CSS variables.

| Variable | Default | Description |
| --- | --- | --- |
| `--vis-donut-background-color` | `#E7E9F3` | The background color of the donut chart. |

Example:

```
:root {
  --vis-donut-background-color: transparent !important;
}
```

[Check out examples here ↗](https://nuxtcharts.com/charts)
