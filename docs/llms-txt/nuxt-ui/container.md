# Source: https://ui.nuxt.com/raw/docs/components/container.md

# Container

> A container lets you center and constrain the width of your content.

## Usage

Use the default slot to center and constrain the width of your content.

<tip to="/docs/getting-started/theme/css-variables#container">

Its max width is controlled by the `--ui-container` CSS variable.

</tip>

```vue [ContainerExample.vue]
<template>
  <UContainer>
    <Placeholder class="h-32" />
  </UContainer>
</template>
```

## API

### Props

```ts
/**
 * Props for the Container component
 */
interface ContainerProps {
  /**
   * The element or component this component should render as.
   */
  as?: any;
}
```

### Slots

```ts
/**
 * Slots for the Container component
 */
interface ContainerSlots {
  default(): any;
}
```

## Theme

```ts [app.config.ts]
export default defineAppConfig({
  ui: {
    container: {
      base: 'w-full max-w-(--ui-container) mx-auto px-4 sm:px-6 lg:px-8'
    }
  }
})
```

## Changelog

<component-changelog>



</component-changelog>
