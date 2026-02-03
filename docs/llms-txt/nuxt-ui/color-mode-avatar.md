# Source: https://ui.nuxt.com/raw/docs/components/color-mode-avatar.md

# ColorModeAvatar

> An Avatar with a different source for light and dark mode.

## Usage

The ColorModeAvatar component extends the [Avatar](/docs/components/avatar) component, so you can pass any property such as `size`, `icon`, etc.

Use the `light` and `dark` props to define the source for light and dark mode.

```vue
<template>
  <UColorModeAvatar light="https://github.com/vuejs.png" dark="https://github.com/nuxt.png" />
</template>
```

> [!NOTE]
> Switch between light and dark mode to see the different images:

## API

### Props

```ts
/**
 * Props for the ColorModeAvatar component
 */
interface ColorModeAvatarProps {
  light: string;
  dark: string;
  /**
   * The element or component this component should render as.
   */
  as?: any;
  ui?: { root?: ClassNameValue; image?: ClassNameValue; fallback?: ClassNameValue; icon?: ClassNameValue; } | undefined;
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
  icon?: any;
  text?: string | undefined;
  size?: "md" | "3xs" | "2xs" | "xs" | "sm" | "lg" | "xl" | "2xl" | "3xl" | undefined;
  chip?: boolean | ChipProps | undefined;
}
```

> [!NOTE]
> See: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/img#attributes
> This component also supports all native `<img>` HTML attributes.

## Changelog

See the [releases page](https://github.com/nuxt/ui/releases) for the latest changes.
