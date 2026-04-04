# Source: https://nuxtcharts.com/docs/customize/tooltips

Title: Tooltips

URL Source: https://nuxtcharts.com/docs/customize/tooltips

Markdown Content:
Here’s a simple custom tooltip component you can use:

Desktop

Use this component in your chart’s `tooltip` slot as shown above.

This gives you full control over Nuxt Charts tooltips.

assets/css/main.css

```
:root {
  /* Tooltip - Default padding */
  --vis-tooltip-padding: 0 0 .5rem 0 !important;

  /* Tooltip - Title */
  --vis-tooltip-title-color: var(--ui-text) !important;
  --vis-tooltip-title-text-transform: capitalize !important;
  --vis-tooltip-title-border-bottom: 1px solid var(--ui-border) !important;
  --vis-tooltip-title-margin-bottom: 0.25rem !important;
  --vis-tooltip-title-padding-bottom: 0.25rem !important;
  --vis-tooltip-title-padding: 0.75rem !important;
  --vis-tooltip-title-font-size: 0.875rem !important;
  --vis-tooltip-title-line-height: 100% !important;
  --vis-tooltip-title-font-weight: 600 !important;

  /* Tooltip - Entry */
  --vis-tooltip-entry-padding-right: 1rem !important;
  --vis-tooltip-entry-padding-left: 1rem !important;

  /* Tooltip - Dot */
  --vis-tooltip-dot-width: 8px !important;
  --vis-tooltip-dot-height: 8px !important;
  --vis-tooltip-dot-border-radius: 4px !important;
  --vis-tooltip-dot-margin-right: 8px !important;

  /* Tooltip - Label */
  --vis-tooltip-label-font-weight: 400 !important;
  --vis-tooltip-label-font-size: 0.875rem !important;
  --vis-tooltip-label-margin-right: 1rem !important;
  --vis-tooltip-label-color: var(--ui-text-muted) !important;

  /* Tooltip - Value */
  --vis-tooltip-value-font-size: 0.875rem !important;
  --vis-tooltip-value-font-weight: 600 !important;
  --vis-tooltip-value-color: var(--ui-text) !important;

  /* Tooltip - Container */
  --vis-tooltip-box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1) !important;
  --vis-tooltip-border-radius: 8px !important;
  --vis-tooltip-border-color: var(--ui-border) !important;
  --vis-tooltip-background-color: var(--ui-bg) !important;
  --vis-tooltip-text-color: var(--ui-text) !important;
  --vis-tooltip-divider: var(--ui-border) !important;
}
```

This gives you full control over tooltip customization.

You can disable tooltips entirely by setting the `hideTooltip` boolean property to `true`:

```
<AreaChart :hideTooltip="true" />
```

You can provide a custom tooltip by using the `tooltip` slot:

AreaChart.vue

```
<AreaChart>
  <template #tooltip="{ values }">
    <CustomTooltip :values="values" />
  </template>
</AreaChart>
```

AreaChart.vue

```
<script setup lang="ts">
const data = [
  { month: 'Jan', value: 75 },
  { month: 'Feb', value: 120 },
  { month: 'Mar', value: 180 },
  { month: 'Apr', value: 110 },
  { month: 'May', value: 90 },
  { month: 'Jun', value: 130 },
]

const categories = {
  value: {
    name: 'Desktop',
    color: '#3b82f6',
  },
}

const xFormatter = (i: number) => data[i].month
</script>

<template>
  <AreaChart
    :data="data"
    :categories="categories"
    :height="260"
    :xFormatter="xFormatter"
    xLabel="Month"
    yLabel="Value"
  >
    <template #tooltip="{ values }">
      <CustomTooltip :values="values" />
    </template>
  </AreaChart>
</template>
```
