# Source: https://nuxtcharts.com/docs/components/status-tracker

Title: Status Tracker

URL Source: https://nuxtcharts.com/docs/components/status-tracker

Markdown Content:
Status Tracker
===============

[Nuxt Charts v2](https://nuxtcharts.com/)

*   [Blocks](https://nuxtcharts.com/blocks)
*   [Docs](https://nuxtcharts.com/docs/getting-started/installation)
*   [Charts](https://nuxtcharts.com/charts)
*   [Templates](https://nuxtcharts.com/templates)
*   Apps
*   [Pricing](https://nuxtcharts.com/pricing)

menu

[](https://ui.nuxtcharts.com/)[](https://github.com/dennisadriaans/vue-chrts)[Sign In Sign In](https://nuxtcharts.com/docs/components/status-tracker)

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

Status Tracker
==============

A component to visualize the status of a service over a period of time.

The `StatusTracker` component is a clean component to displaying the operational status of services over time. It's designed to be highly reusable and customizable.

[Example](https://nuxtcharts.com/docs/components/status-tracker#example)
------------------------------------------------------------------------

Here's an example of the `StatusTracker` in action, monitoring a fictional service.

Preview Example.vue Terminal

api.example.com

99.9% uptime

90 days ago Today

```
<script lang="ts" setup>
const statusData = computed(() => {
  const statusHistory = Array.from({ length: 300 }, () => ({
    status: 'online',
  }))
  statusHistory[250]!.status = 'offline'
  return statusHistory
})
</script>

<template>
  <StatusTracker
    :status-data="statusData"
    :operational-status="true"
    :bar-width="4"
    :bar-gap="1"
    domain="example.com"
    uptime="99.9%"
  />
</template>
```

```
nuxt-charts add StatusTracker
```

[](https://nuxtcharts.com/docs/getting-started/cli)Learn how to use the **Nuxt Charts CLI** to get premium components.

[Props](https://nuxtcharts.com/docs/components/status-tracker#props)
--------------------------------------------------------------------

| Prop | Type | Default | Description |
| --- | --- | --- | --- |
| `bar-width` | `number` | `4` | Width of each status bar |
| `bar-gap` | `number` | `1` | Gap between status bars |
| `operational-status` | `boolean` | `true` | Current operational status |
| `domain` | `string` | `''` | Domain being monitored |
| `uptime` | `string` | `''` | Uptime percentage display |
| `status-data` | `Array` | `[]` | Array of status objects with `status` property |

[Progress Circle Display circular progress indicators with the ProgressCircle component.](https://nuxtcharts.com/docs/components/progress-circle)[Category Distribution A component to visualize categorical data](https://nuxtcharts.com/docs/components/category-distribution)

Browse All Documentation

Table of Contents
Table of Contents

*   [Example](https://nuxtcharts.com/docs/components/status-tracker#example)
*   [Props](https://nuxtcharts.com/docs/components/status-tracker#props)

Support Nuxt Charts

*   [Follow on X](https://x.com/DennisAdriaans)
*   [Star on GitHub](https://github.com/dennisadriaans/vue-chrts)
*   [Purchase a All-Access](https://nuxtcharts.com/pricing)

SCROLL: 0px
