# Source: https://ui.nuxt.com/raw/docs/components/avatar.md

# Avatar

> An img element with fallback and Nuxt Image support.

## Usage

The Avatar uses the `<NuxtImg>` component when [`@nuxt/image`](https://github.com/nuxt/image) is installed, falling back to `img` otherwise.

```vue
<template>
  <UAvatar src="https://github.com/benjamincanac.png" />
</template>
```

<note>

You can pass any property from the HTML `<img>` element such as `alt`, `loading`, etc.

</note>

### Src

Use the `src` prop to set the image URL.

```vue
<template>
  <UAvatar src="https://github.com/benjamincanac.png" />
</template>
```

### Size

Use the `size` prop to set the size of the Avatar.

```vue
<template>
  <UAvatar src="https://github.com/benjamincanac.png" size="xl" />
</template>
```

<note>

The `<img>` element's `width` and `height` are automatically set based on the `size` prop.

</note>

### Icon

Use the `icon` prop to display a fallback [Icon](/docs/components/icon).

```vue
<template>
  <UAvatar icon="i-lucide-image" size="md" />
</template>
```

### Text

Use the `text` prop to display a fallback text.

```vue
<template>
  <UAvatar text="+1" size="md" />
</template>
```

### Alt

When no icon or text is provided, the **initials** of the `alt` prop is used as fallback.

```vue
<template>
  <UAvatar alt="Benjamin Canac" size="md" />
</template>
```

<note>

The `alt` prop is passed to the `img` element as the `alt` attribute.

</note>

### Chip

Use the `chip` prop to display a chip around the Avatar.

```vue
<template>
  <UAvatar src="https://github.com/benjamincanac.png" />
</template>
```

## Examples

### With tooltip

You can use a [Tooltip](/docs/components/tooltip) component to display a tooltip when hovering the Avatar.

```vue [AvatarTooltipExample.vue]
<template>
  <UTooltip text="Benjamin Canac">
    <UAvatar
      src="https://github.com/benjamincanac.png"
      alt="Benjamin Canac"
    />
  </UTooltip>
</template>
```

### With mask

You can use a CSS mask to display an Avatar with a custom shape instead of a simple circle.

```vue [AvatarMaskExample.vue]
<template>
  <UAvatar class="rounded-none squircle" src="https://avatars.githubusercontent.com/u/739984?v=4" alt="Benjamin Canac" />
</template>

<style>
.squircle {
  mask-image: url("data:image/svg+xml,%3csvg width='200' height='200' xmlns='http://www.w3.org/2000/svg'%3e%3cpath d='M100 0C20 0 0 20 0 100s20 100 100 100 100-20 100-100S180 0 100 0Z'/%3e%3c/svg%3e");
  mask-size: contain;
  mask-position: center;
  mask-repeat: no-repeat;
}
</style>
```

## API

### Props

```ts
/**
 * Props for the Avatar component
 */
interface AvatarProps {
  /**
   * The element or component this component should render as.
   */
  as?: any;
  src?: string | undefined;
  alt?: string | undefined;
  icon?: string | object | undefined;
  text?: string | undefined;
  size?: "2xs" | "xs" | "sm" | "md" | "lg" | "xl" | "3xs" | "2xl" | "3xl" | undefined;
  chip?: boolean | ChipProps | undefined;
  ui?: { root?: ClassNameValue; image?: ClassNameValue; fallback?: ClassNameValue; icon?: ClassNameValue; } | undefined;
  loading?: "lazy" | "eager" | undefined;
  referrerpolicy?: HTMLAttributeReferrerPolicy | undefined;
  crossorigin?: "" | "anonymous" | "use-credentials" | undefined;
  decoding?: "async" | "auto" | "sync" | undefined;
  height?: Numberish | undefined;
  sizes?: string | undefined;
  srcset?: string | undefined;
  usemap?: string | undefined;
  width?: Numberish | undefined;
}
```

<callout icon="i-simple-icons-mdnwebdocs" target="_blank" to="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/img#attributes">

This component also supports all native `<img>` HTML attributes.

</callout>

## Theme

```ts [app.config.ts]
export default defineAppConfig({
  ui: {
    avatar: {
      slots: {
        root: 'inline-flex items-center justify-center shrink-0 select-none rounded-full align-middle bg-elevated',
        image: 'h-full w-full rounded-[inherit] object-cover',
        fallback: 'font-medium leading-none text-muted truncate',
        icon: 'text-muted shrink-0'
      },
      variants: {
        size: {
          '3xs': {
            root: 'size-4 text-[8px]'
          },
          '2xs': {
            root: 'size-5 text-[10px]'
          },
          xs: {
            root: 'size-6 text-xs'
          },
          sm: {
            root: 'size-7 text-sm'
          },
          md: {
            root: 'size-8 text-base'
          },
          lg: {
            root: 'size-9 text-lg'
          },
          xl: {
            root: 'size-10 text-xl'
          },
          '2xl': {
            root: 'size-11 text-[22px]'
          },
          '3xl': {
            root: 'size-12 text-2xl'
          }
        }
      },
      defaultVariants: {
        size: 'md'
      }
    }
  }
})
```

## Changelog

<component-changelog>



</component-changelog>
