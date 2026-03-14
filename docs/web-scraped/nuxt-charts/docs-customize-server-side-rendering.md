# Source: https://nuxtcharts.com/docs/customize/server-side-rendering

Title: Server-side Rendering

URL Source: https://nuxtcharts.com/docs/customize/server-side-rendering

Markdown Content:
**Warning!** Nuxt Charts is based on Unovis, which uses D3.js and is not optimized for server-side rendering.

The Nuxt module optimizes dependencies to minimize SSR errors. If you still encounter SSR issues with charts, use the instructions below.

Create chart components with the `.client.vue` suffix to prevent them from being imported on the server side.

MyChart.client.vue

```
<template>
  <LineChart
    :data="data"
    :height="275"
    y-label="Sales"
    :x-num-ticks="4"
    :y-num-ticks="4"
    :categories="categories"
    :x-formatter="xFormatter"
    :grid-line-y="true"
    :legend-position="LegendPosition.TopRight"
  />
</template>
```

Wrap your chart components with the `<ClientOnly>` tag to ensure they only render on the client side.

client-only.vue

```
<ClientOnly>
  <YourChartComponent />
</ClientOnly>
```

**Warning!** Don't wrap individual chart components inside a component that already uses charts. Instead, wrap the entire parent component.

wrong-approach.vue

```
<div>
  <h2 class="font-bold text-lg text-highlighted tracking-wide py-1">
    This will fail
  </h2>
  <ClientOnly>
    <LineChart 
      :data="data"
      :height="275"
      y-label="Sales"
      :x-num-ticks="4"
      :y-num-ticks="4"
      :categories="categories"
      :x-formatter="xFormatter"
      :grid-line-y="true"
      :legend-position="LegendPosition.TopRight"
    />
  </ClientOnly>
</div>
```

correct-approach.vue

```
<div>
  <ClientOnly>
    <MyChartWrapperComponent />
  </ClientOnly>
</div>
```

You can disable server-side rendering for your entire Nuxt app by setting `ssr: false` in your `nuxt.config.ts`:

nuxt.config.ts

```
export default defineNuxtConfig({
  ssr: false
})
```

**Note!** Disabling SSR globally is only recommended if your entire application does not require server-side rendering. For most use cases, prefer the `.client.vue` convention or `<ClientOnly>` wrapper for specific components.

You can dynamically import chart components using `defineAsyncComponent` to ensure they are only loaded on the client. This is especially useful for SSR compatibility:

async-component.ts

```
const MyChart = defineAsyncComponent(() => import('./MyChart.vue'))
```

✅ Use the `.client.vue` naming convention for chart components.

✅ Wrap entire components that contain charts with the `<ClientOnly>` tag.

❌ Don't nest `<ClientOnly>` tags within components that already use charts.
