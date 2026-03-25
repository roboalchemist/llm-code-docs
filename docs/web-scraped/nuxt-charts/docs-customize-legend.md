# Source: https://nuxtcharts.com/docs/customize/legend

Title: Legends

URL Source: https://nuxtcharts.com/docs/customize/legend

Markdown Content:
Legends
===============

[Nuxt Charts v2](https://nuxtcharts.com/)

*   [Blocks](https://nuxtcharts.com/blocks)
*   [Docs](https://nuxtcharts.com/docs/getting-started/installation)
*   [Charts](https://nuxtcharts.com/charts)
*   [Templates](https://nuxtcharts.com/templates)
*   Apps
*   [Pricing](https://nuxtcharts.com/pricing)

menu

[](https://ui.nuxtcharts.com/)[](https://github.com/dennisadriaans/vue-chrts)[Sign In Sign In](https://nuxtcharts.com/docs/customize/legend)

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

Legends
=======

[Star](https://github.com/dennisadriaans/vue-chrts)

Learn how to customize legends in Nuxt Charts to highlight data points with custom shapes, sizes, and colors.

[Legend Visibility](https://nuxtcharts.com/docs/customize/legend#legend-visibility)
-----------------------------------------------------------------------------------

The legend is shown by default. You can hide it by setting the `hideLegend` prop to `true`.

```
<LineChart :hide-legend="true" />
```

[Legend Positioning](https://nuxtcharts.com/docs/customize/legend#legend-positioning)
-------------------------------------------------------------------------------------

Control the legend's position using the `legendPosition` prop. Supported values:

*   `topLeft`
*   `topCenter`
*   `topRight`
*   `bottomLeft`
*   `bottomCenter`
*   `bottomRight`

The legend is rendered above or below the chart depending on the position. The component uses computed properties to determine flex direction and alignment.

```
<LineChart :legend-position="LegendPosition.TopRight" />
```

[Legend Styling](https://nuxtcharts.com/docs/customize/legend#legend-styling)
-----------------------------------------------------------------------------

Customize the legend's appearance with the `legendStyle` prop, which accepts a style object. The legend also uses the CSS variable `--vis-legend-spacing` for spacing between items.

```
<LineChart :legend-style="{ background: '#fff', borderRadius: '8px' }" />
```

[Legend Spacing Variable](https://nuxtcharts.com/docs/customize/legend#legend-spacing-variable)
-----------------------------------------------------------------------------------------------

You can customize the spacing around the chart legend using the `--vis-legend-spacing` CSS variable. This controls the margin or padding applied to the legend area.

**Example:**

```
:root {
    --vis-legend-spacing: 16px;
}
```

Adjust the value as needed to fit your design.

[Legend Items](https://nuxtcharts.com/docs/customize/legend#legend-items)
-------------------------------------------------------------------------

Each legend item corresponds to a category in the `categories` prop. The color for each item is taken from the category's `color` property. If the color is an array, only the first color is used for the legend bullet.

```
const categories = {
    sales: { name: 'Sales', color: '#22c55e' },
    profit: { name: 'Profit', color: ['#3b82f6', '#a21caf'] },
}
```

[Example Usage](https://nuxtcharts.com/docs/customize/legend#example-usage)
---------------------------------------------------------------------------

```
<LineChart
    :categories="categories"
    legend-position="bottomCenter"
    :legend-style="{ padding: '8px' }"
/>
```

[Summary Table](https://nuxtcharts.com/docs/customize/legend#summary-table)
---------------------------------------------------------------------------

| Prop | Type | Description |
| --- | --- | --- |
| hideLegend | boolean | Hides the legend if true. |
| legendPosition | LegendPosition | Sets the legend's position. |
| legendStyle | object | Custom CSS styles for the legend. |
| categories | Record<string, Category> | Defines legend items and their colors. |

[Markers Learn how to customize markers in Nuxt Charts to highlight data points with custom shapes, sizes, and colors.](https://nuxtcharts.com/docs/customize/markers)[Server-side Rendering Learn how to handle server-side rendering with client-side-only charts in your Nuxt application.](https://nuxtcharts.com/docs/customize/server-side-rendering)

Browse All Documentation

Table of Contents
Table of Contents

*   [Legend Visibility](https://nuxtcharts.com/docs/customize/legend#legend-visibility)
*   [Legend Positioning](https://nuxtcharts.com/docs/customize/legend#legend-positioning)
*   [Legend Styling](https://nuxtcharts.com/docs/customize/legend#legend-styling)
*   [Legend Spacing Variable](https://nuxtcharts.com/docs/customize/legend#legend-spacing-variable)
*   [Legend Items](https://nuxtcharts.com/docs/customize/legend#legend-items)
*   [Example Usage](https://nuxtcharts.com/docs/customize/legend#example-usage)
*   [Summary Table](https://nuxtcharts.com/docs/customize/legend#summary-table)

Support Nuxt Charts

*   [Follow on X](https://x.com/DennisAdriaans)
*   [Star on GitHub](https://github.com/dennisadriaans/vue-chrts)
*   [Purchase a All-Access](https://nuxtcharts.com/pricing)

SCROLL: 0px
