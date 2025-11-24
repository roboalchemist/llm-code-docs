# Source: https://ui.nuxt.com/raw/docs/components/icon.md

# Icon

> A component to display any icon from Iconify or another component.

## Usage

Use the `name` prop to display an icon:

```vue
<template>
  <UIcon name="i-lucide-lightbulb" class="size-5" />
</template>
```

<framework-only>
<template v-slot:nuxt="">
<caution to="/docs/getting-started/integrations/icons/nuxt#collections">

It's highly recommended to install the icons collections you need, read more about this.

</caution>
</template>
</framework-only>

## Examples

### SVG

You can also pass a Vue component into the `name` prop:

```vue [IconSvgExample.vue]
<script setup lang="ts">
import { h } from 'vue'

const IconLightbulb = () => h(
  'svg',
  { xmlns: 'http://www.w3.org/2000/svg', viewBox: '0 0 24 24' },
  [
    h(
      'path',
      {
        'fill': 'none',
        'stroke': 'currentColor',
        'stroke-linecap': 'round',
        'stroke-linejoin': 'round',
        'stroke-width': 2,
        'd': 'M15 14c.2-1 .7-1.7 1.5-2.5c1-.9 1.5-2.2 1.5-3.5A6 6 0 0 0 6 8c0 1 .2 2.2 1.5 3.5c.7.7 1.3 1.5 1.5 2.5m0 4h6m-5 4h4'
      }
    )
  ]
)
</script>

<template>
  <UIcon :name="IconLightbulb" class="size-5" />
</template>
```

You can define your icon components yourself, or use [`unplugin-icons`](https://github.com/unplugin/unplugin-icons) to import them directly from SVG files:

```vue
<script setup lang="ts">
import IconLightbulb from '~icons/lucide/lightbulb'
</script>

<template>
  <UIcon :name="IconLightbulb" class="size-5" />
</template>
```

## API

### Props

```ts
/**
 * Props for the Icon component
 */
interface IconProps {
  name: string | object;
  mode?: "svg" | "css" | undefined;
  size?: string | number | undefined;
  customize?: ((content: string, name?: string | undefined, prefix?: string | undefined, provider?: string | undefined) => string) | undefined;
}
```

## Changelog

<component-changelog>



</component-changelog>
