# Source: https://nuxtcharts.com/docs/maps/topojson-map

Title: TopoJSON Map

URL Source: https://nuxtcharts.com/docs/maps/topojson-map

Markdown Content:
TopoJSON Map
===============

[Nuxt Charts v2](https://nuxtcharts.com/)

*   [Blocks](https://nuxtcharts.com/blocks)
*   [Docs](https://nuxtcharts.com/docs/getting-started/installation)
*   [Charts](https://nuxtcharts.com/charts)
*   [Templates](https://nuxtcharts.com/templates)
*   Apps
*   [Pricing](https://nuxtcharts.com/pricing)

menu

[](https://ui.nuxtcharts.com/)[](https://github.com/dennisadriaans/vue-chrts)[Sign In Sign In](https://nuxtcharts.com/docs/maps/topojson-map)

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

TopoJSON Map
============

[Star](https://github.com/dennisadriaans/vue-chrts)

Display interactive geographic maps with points, links, and areas using TopoJSON component for Vue.

Render country or regional maps from TopoJSON data. Add points for locations, links for connections, and color areas for choropleth visualizations.

[Plain Map](https://nuxtcharts.com/docs/maps/topojson-map#plain-map)
--------------------------------------------------------------------

Standard map showing only geographic areas with choropleth coloring.

Preview TopoJSON.vue

```
<script setup lang="ts">
import { WorldMapTopoJSON } from "@unovis/ts/maps";
import { geoMercator } from "d3-geo";

const hoveredArea = ref<string>();

const ChoroplethMapData = computed(() => [
  { id: "NL", count: 94, name: "Netherlands" },
  { id: "US", count: 91, name: "United States" },
  { id: "DE", count: 71, name: "Germany" },
  { id: "BR", count: 60, name: "Brazil" },
  { id: "FR", count: 59, name: "France" },
  { id: "ID", count: 48, name: "Indonesia" },
  { id: "KE", count: 42, name: "Kenya" },
  { id: "GB", count: 35, name: "United Kingdom" },
  { id: "CA", count: 30, name: "Canada" },
]);

const worldData = computed(() => ({
  areas: ChoroplethMapData.value.map((d) => ({
    id: d.id,
    count: d.count,
    name: d.name,
  })),
}));

const maxCount = Math.max(...worldData.value.areas.map((d) => d.count));

const areaColor = computed(() => {
  return (d: any) => {
    if (!d.count) return "var(--ui-color-primary-900)";
    const t = d.count / maxCount;

    if (t > 0.8) return "var(--ui-color-primary-800)";
    if (t > 0.6) return "var(--ui-color-primary-700)";
    if (t > 0.4) return "var(--ui-color-primary-600)";
    if (t > 0.2) return "var(--ui-color-primary-500)";
    return "#dbeafe";
  };
});

const customProjection = geoMercator().center([0, 0]);
</script>

<template>
  <div class="py-6">
    <TopoJSONMap
      :height="400"
      map-feature-key="countries"
      :projection="customProjection"
      :data="worldData"
      :topo-json="WorldMapTopoJSON"
      :area-color="areaColor"
      :zoom-factor="1.1"
      @mouseenter="(d: any) => (hoveredArea = d.id)"
      @mouseleave="() => (hoveredArea = undefined)"
    />
  </div>
</template>

<style>
:root {
  --vis-map-feature-color: var(--ui-bg-elevated);
  --vis-map-boundary-color: var(--ui-border-accented);
}
</style>
```

[Map with Points](https://nuxtcharts.com/docs/maps/topojson-map#map-with-points)
--------------------------------------------------------------------------------

Add point markers to specific geographic coordinates.

Preview TopoJSON.vue

```
<script setup lang="ts">
import { WorldMapTopoJSON } from "@unovis/ts/maps";
import { geoMercator } from "d3-geo";

const worldData = computed(() => ({
  areas: [
    { id: "NL", count: 94, name: "Netherlands" },
    { id: "US", count: 91, name: "United States" },
    { id: "DE", count: 71, name: "Germany" },
    { id: "BR", count: 60, name: "Brazil" },
    { id: "FR", count: 59, name: "France" },
    { id: "ID", count: 48, name: "Indonesia" },
    { id: "KE", count: 42, name: "Kenya" },
    { id: "GB", count: 35, name: "United Kingdom" },
    { id: "CA", count: 30, name: "Canada" },
  ],
  points: [
    {
      id: "ams",
      latitude: 52.3676,
      longitude: 4.9041,
      color: "var(--ui-bg-inverted)",
    },
    {
      id: "nyc",
      latitude: 40.7128,
      longitude: -74.006,
      color: "var(--ui-bg-inverted)",
    },
    {
      id: "tyo",
      latitude: 35.6762,
      longitude: 139.6503,
      color: "var(--ui-bg-inverted)",
    },
  ],
}));

const customProjection = geoMercator().center([0, 0]);
</script>

<template>
  <div class="py-6">
    <TopoJSONMap
      :height="400"
      map-feature-key="countries"
      :projection="customProjection"
      :data="worldData"
      :topo-json="WorldMapTopoJSON"
      :zoom-factor="1.1"
    />
  </div>
</template>
```

[Map with Links](https://nuxtcharts.com/docs/maps/topojson-map#map-with-links)
------------------------------------------------------------------------------

Connect points with curved line segments to show relationships or movement.

Preview TopoJSON.vue

```
<script setup lang="ts">
import { WorldMapTopoJSON } from "@unovis/ts/maps";
import { geoMercator } from "d3-geo";

const worldData = computed(() => ({
  areas: [
    { id: "NL", count: 94, name: "Netherlands" },
    { id: "US", count: 91, name: "United States" },
    { id: "DE", count: 71, name: "Germany" },
    { id: "BR", count: 60, name: "Brazil" },
    { id: "FR", count: 59, name: "France" },
    { id: "ID", count: 48, name: "Indonesia" },
    { id: "KE", count: 42, name: "Kenya" },
    { id: "GB", count: 35, name: "United Kingdom" },
    { id: "CA", count: 30, name: "Canada" },
  ],
  points: [
    { id: "ams", latitude: 52.3676, longitude: 4.9041, label: "Amsterdam" },
    { id: "nyc", latitude: 40.7128, longitude: -74.006, label: "New York" },
    { id: "tyo", latitude: 35.6762, longitude: 139.6503, label: "Tokyo" },
  ],
  links: [
    { source: "ams", target: "nyc" },
    { source: "tyo", target: "ams" },
  ],
}));

const customProjection = geoMercator().center([0, 0]);
</script>

<template>
  <div class="py-6">
    <TopoJSONMap
      :height="400"
      map-feature-key="countries"
      :projection="customProjection"
      :data="worldData"
      :topo-json="WorldMapTopoJSON"
      :zoom-factor="1.1"
    />
  </div>
</template>
```

[Props](https://nuxtcharts.com/docs/maps/topojson-map#props)
------------------------------------------------------------

| Prop | Type | Default | Description |
| --- | --- | --- | --- |
| `data` | `MapData` | **Required** | Map data containing points, links, and/or areas. |
| `width` | `number | string` | `undefined` | Width of the map container. |
| `height` | `number | string` | `undefined` | Height of the map container. |
| `disableZoom` | `boolean` | `false` | If true, disables zoom functionality. |
| `zoomFactor` | `number` | `undefined` | Initial zoom factor. |
| `zoomExtent` | `[number, number]` | `undefined` | Zoom limits min, max. |
| `zoomDuration` | `number` | `undefined` | Zoom animation duration in milliseconds. |
| `mapFitToPoints` | `boolean` | `false` | If true, fits the map view to show all points. |
| `pointColor` | `string | ((d: MapPoint) => string)` | `undefined` | Color for points. |
| `pointRadius` | `number | ((d: MapPoint) => number)` | `undefined` | Radius of points in pixels. |
| `pointStrokeWidth` | `number | ((d: MapPoint) => number)` | `undefined` | Stroke width for points. |
| `pointCursor` | `string | ((d: MapPoint) => string)` | `undefined` | Cursor style when hovering points. |
| `pointLabel` | `(d: MapPoint) => string` | `undefined` | Accessor for point labels. |
| `linkColor` | `string | ((d: MapLink) => string)` | `undefined` | Color for links. |
| `linkWidth` | `number | ((d: MapLink) => number)` | `undefined` | Width of links in pixels. |
| `linkCursor` | `string | ((d: MapLink) => string)` | `undefined` | Cursor style when hovering links. |
| `areaColor` | `string | ((d: MapArea) => string)` | `undefined` | Color for map areas. |
| `areaCursor` | `string | ((d: MapArea) => string)` | `undefined` | Cursor style when hovering areas. |
| `heatmapMode` | `boolean` | `false` | Enable heatmap visualization for points. |
| `heatmapModeBlurStdDeviation` | `number` | `undefined` | Blur amount for heatmap. |
| `heatmapModeZoomLevelThreshold` | `number` | `undefined` | Zoom level at which heatmap switches to points. |
| `projection` | `GeoProjection` | `undefined` | Custom D3 geo projection. |

[Dotted Map Create stylized dotted world maps with customizable pins and regions.](https://nuxtcharts.com/docs/maps/dotted-map)[Tooltips How to customize and use tooltips in Nuxt Charts.](https://nuxtcharts.com/docs/customize/tooltips)

Browse All Documentation

Table of Contents
Table of Contents

*   [Plain Map](https://nuxtcharts.com/docs/maps/topojson-map#plain-map)
*   [Map with Points](https://nuxtcharts.com/docs/maps/topojson-map#map-with-points)
*   [Map with Links](https://nuxtcharts.com/docs/maps/topojson-map#map-with-links)
*   [Props](https://nuxtcharts.com/docs/maps/topojson-map#props)

Support Nuxt Charts

*   [Follow on X](https://x.com/DennisAdriaans)
*   [Star on GitHub](https://github.com/dennisadriaans/vue-chrts)
*   [Purchase a All-Access](https://nuxtcharts.com/pricing)

SCROLL: 0px
