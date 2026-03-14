# Source: https://nuxtcharts.com/docs/customize/theming

Title: Theming

URL Source: https://nuxtcharts.com/docs/customize/theming

Markdown Content:
Theming
===============

[Nuxt Charts v2](https://nuxtcharts.com/)

*   [Blocks](https://nuxtcharts.com/blocks)
*   [Docs](https://nuxtcharts.com/docs/getting-started/installation)
*   [Charts](https://nuxtcharts.com/charts)
*   [Templates](https://nuxtcharts.com/templates)
*   Apps
*   [Pricing](https://nuxtcharts.com/pricing)

menu

[](https://ui.nuxtcharts.com/)[](https://github.com/dennisadriaans/vue-chrts)[Sign In Sign In](https://nuxtcharts.com/docs/customize/theming)

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

Theming
=======

Learn how to customize Nuxt Charts appearance using CSS variables for theming and dark mode support.

[Add Global CSS Variables](https://nuxtcharts.com/docs/customize/theming#add-global-css-variables)
--------------------------------------------------------------------------------------------------

Check the Unovis documentation for more information [here](https://unovis.dev/docs/guides/theming).

assets/css/main.css

```
:root {
    /* Chart Fallback Colors */
  --vis-color0: oklch(0.63 0.1363 157.86) !important;
  --vis-color1: oklch(0.76 0.1782 153.61) !important;
  --vis-color2: oklch(0.70 0.15 270) !important;
  --vis-color3: oklch(0.75 0.15 60) !important;
  --vis-color4: oklch(0.68 0.15 330) !important;

    /* Legend */
  --vis-legend-item-spacing: 0px !important;
  --vis-legend-spacing: 16px !important;
  --vis-legend-label-color: var(--ui-text-muted) !important;

  /* Axis */
  --vis-axis-grid-color: rgba(0, 0, 0, 0.1) !important;
  --vis-axis-tick-label-color: var(--ui-text-muted) !important;
  --vis-axis-label-color: var(--ui-text-muted) !important;
  --vis-axis-tick-color: var(--ui-text-muted) !important;
  --vis-axis-domain-line-dasharray: none !important;
  --vis-axis-tick-label-weight: 400 !important;

  /* Timeline */
  --vis-timeline-row-even-fill-color: #f9fafb !important;
  --vis-timeline-row-odd-fill-color: transparent !important;
  --vis-timeline-label-color: var(--ui-text-muted) !important;
}

/* Dark mode example: override theme variables */
.dark {
  --custom-primary: oklch(0.72 0.192 149.58);
  --custom-secondary: oklch(0.63 0.1963 157.86);
  /* ...override other variables for dark mode as needed... */
}
```

[Tooltips How to customize and use tooltips in Nuxt Charts.](https://nuxtcharts.com/docs/customize/tooltips)[Markers Learn how to customize markers in Nuxt Charts to highlight data points with custom shapes, sizes, and colors.](https://nuxtcharts.com/docs/customize/markers)

Browse All Documentation

Table of Contents
Table of Contents

*   [Add Global CSS Variables](https://nuxtcharts.com/docs/customize/theming#add-global-css-variables)

Support Nuxt Charts

*   [Follow on X](https://x.com/DennisAdriaans)
*   [Star on GitHub](https://github.com/dennisadriaans/vue-chrts)
*   [Purchase a All-Access](https://nuxtcharts.com/pricing)

SCROLL: 0px
