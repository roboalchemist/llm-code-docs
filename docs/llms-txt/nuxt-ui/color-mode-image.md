# Source: https://ui.nuxt.com/raw/docs/components/color-mode-image.md

# ColorModeImage

> An image element with a different source for light and dark mode.

## Usage

The ColorModeImage component uses the `<NuxtImg>` component when [`@nuxt/image`](https://github.com/nuxt/image) is installed, falling back to `img` otherwise.

```vue
<template>
  <UColorModeImage light="https://picsum.photos/id/29/400" dark="https://picsum.photos/id/46/400" :width="200" :height="200" />
</template>
```

<note>

Switch between light and dark mode to see the different images: <u-color-mode-select size="sm">



</u-color-mode-select>
</note>

## API

### Props

```ts
/**
 * Props for the ColorModeImage component
 */
interface ColorModeImageProps {
  dark: string;
  light: string;
  alt?: string | undefined;
  crossorigin?: "" | "anonymous" | "use-credentials" | undefined;
  decoding?: "async" | "auto" | "sync" | undefined;
  height?: Numberish | undefined;
  loading?: "lazy" | "eager" | undefined;
  referrerpolicy?: HTMLAttributeReferrerPolicy | undefined;
  sizes?: string | undefined;
  srcset?: string | undefined;
  usemap?: string | undefined;
  width?: Numberish | undefined;
}
```

<callout icon="i-simple-icons-mdnwebdocs" target="_blank" to="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/img#attributes">

This component also supports all native `<img>` HTML attributes.

</callout>

## Changelog

<component-changelog prefix="color-mode">



</component-changelog>
