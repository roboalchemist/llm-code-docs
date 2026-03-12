# Source: https://nuxtcharts.com/docs/components/progress-circle

Title: Progress Circle

URL Source: https://nuxtcharts.com/docs/components/progress-circle

Markdown Content:
Progress Circle
===============

[Nuxt Charts v2](https://nuxtcharts.com/)

*   [Blocks](https://nuxtcharts.com/blocks)
*   [Docs](https://nuxtcharts.com/docs/getting-started/installation)
*   [Charts](https://nuxtcharts.com/charts)
*   [Templates](https://nuxtcharts.com/templates)
*   Apps
*   [Pricing](https://nuxtcharts.com/pricing)

menu

[](https://ui.nuxtcharts.com/)[](https://github.com/dennisadriaans/vue-chrts)[Sign In Sign In](https://nuxtcharts.com/docs/components/progress-circle)

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

Progress Circle
===============

Display circular progress indicators with the ProgressCircle component.

The `ProgressCircle` component provides a visually appealing way to represent progress in a circular format

[Example](https://nuxtcharts.com/docs/components/progress-circle#example)
-------------------------------------------------------------------------

Here’s an example of the `ProgressCircle` in action, displaying simple progress.

Preview Example.vue Terminal

Progress Example

```
<div class="flex flex-col items-center justify-center space-y-2">
  <ProgressCircle
    :value="88"
    :size="80"
    :stroke-width="8"
    :show-label="true"
  />
  <span class="text-center">Progress Example</span>
</div>
```

```
nuxt-charts add ProgressCircle
```

[](https://nuxtcharts.com/docs/getting-started/cli)Learn how to use the **Nuxt Charts CLI** to get premium components.

[Props](https://nuxtcharts.com/docs/components/progress-circle#props)
---------------------------------------------------------------------

| Prop | Type | Default | Description |
| --- | --- | --- | --- |
| `value` | `number` | `0` | The progress value (0-100) |
| `size` | `number` | `60` | The diameter of the circle in pixels |
| `stroke-width` | `number` | `4` | The thickness of the progress stroke |
| `show-label` | `boolean` | `false` | Whether to display the percentage label |

[Gantt Charts A Gantt Chart or timeline that displays a list of events in chronological order.](https://nuxtcharts.com/docs/charts/gantt-chart)[Status Tracker A component to visualize the status of a service over a period of time.](https://nuxtcharts.com/docs/components/status-tracker)

Browse All Documentation

Table of Contents
Table of Contents

*   [Example](https://nuxtcharts.com/docs/components/progress-circle#example)
*   [Props](https://nuxtcharts.com/docs/components/progress-circle#props)

Support Nuxt Charts

*   [Follow on X](https://x.com/DennisAdriaans)
*   [Star on GitHub](https://github.com/dennisadriaans/vue-chrts)
*   [Purchase a All-Access](https://nuxtcharts.com/pricing)

SCROLL: 0px
