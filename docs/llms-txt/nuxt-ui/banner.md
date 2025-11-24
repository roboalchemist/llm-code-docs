# Source: https://ui.nuxt.com/raw/docs/components/banner.md

# Banner

> Display a banner at the top of your website to inform users about important information.

## Usage

### Title

Use the `title` prop to display a title on the Banner.

```vue
<template>
  <UBanner title="This is a banner with an important message." />
</template>
```

### Icon

Use the `icon` prop to display an icon on the Banner.

```vue
<template>
  <UBanner icon="i-lucide-info" title="This is a banner with an icon." />
</template>
```

### Color

Use the `color` prop to change the color of the Banner.

```vue
<template>
  <UBanner color="neutral" icon="i-lucide-info" title="This is a banner with an icon." />
</template>
```

### Close

Use the `close` prop to display a [Button](/docs/components/button) to dismiss the Banner. Defaults to `false`.

<tip>

A `close` event will be emitted when the close button is clicked.

</tip>

```vue [BannerExample.vue]
<script setup lang="ts">
import type { BannerProps } from '@nuxt/ui'

const { id = 'example' } = defineProps<{
  id?: string
  title?: string
  color?: BannerProps['color']
  closeIcon?: string
}>()

function onClose() {
  localStorage.removeItem(`banner-${id}`)

  setTimeout(() => {
    document.querySelector('html')?.classList.remove('hide-banner')
  }, 1000)
}

onBeforeMount(() => {
  localStorage.removeItem(`banner-${id}`)
})
</script>

<template>
  <UBanner
    :id="id"
    :title="title || 'This is a closable banner'"
    :color="color"
    :close-icon="closeIcon"
    close
    @close="onClose"
  />
</template>
```

<note>

When closed, `banner-${id}` will be stored in the local storage to prevent it from being displayed again. <br />

 For the example above, `banner-example` will be stored in the local storage.

</note>

### Close Icon

Use the `close-icon` prop to customize the close button [Icon](/docs/components/icon). Defaults to `i-lucide-x`.

```vue [BannerExample.vue]
<script setup lang="ts">
import type { BannerProps } from '@nuxt/ui'

const { id = 'example' } = defineProps<{
  id?: string
  title?: string
  color?: BannerProps['color']
  closeIcon?: string
}>()

function onClose() {
  localStorage.removeItem(`banner-${id}`)

  setTimeout(() => {
    document.querySelector('html')?.classList.remove('hide-banner')
  }, 1000)
}

onBeforeMount(() => {
  localStorage.removeItem(`banner-${id}`)
})
</script>

<template>
  <UBanner
    :id="id"
    :title="title || 'This is a closable banner'"
    :color="color"
    :close-icon="closeIcon"
    close
    @close="onClose"
  />
</template>
```

<framework-only>
<template v-slot:nuxt="">
<tip to="/docs/getting-started/integrations/icons/nuxt#theme">

You can customize this icon globally in your `app.config.ts` under `ui.icons.close` key.

</tip>
</template>

<template v-slot:vue="">
<tip to="/docs/getting-started/integrations/icons/vue#theme">

You can customize this icon globally in your `vite.config.ts` under `ui.icons.close` key.

</tip>
</template>
</framework-only>

### Actions

Use the `actions` prop to add some [Button](/docs/components/button) actions to the Banner.

```vue
<template>
  <UBanner title="This is a banner with actions." />
</template>
```

<note>

The action buttons default to `color="neutral"` and `size="xs"`. You can customize these values by passing them directly to each action button.

</note>

### Link

You can pass any property from the [`<NuxtLink>`](https://nuxt.com/docs/api/components/nuxt-link) component such as `to`, `target`, `rel`, etc.

```vue
<template>
  <UBanner to="https://nuxtlabs.com/" target="_blank" title="NuxtLabs is joining Vercel!" color="primary" />
</template>
```

<note>

The `NuxtLink` component will inherit all other attributes you pass to the `User` component.

</note>

## Examples

### Within `app.vue`

Use the Banner component in your `app.vue` or in a layout:

```vue [app.vue]
<template>
  <UApp>
    <UBanner icon="i-lucide-construction" title="Nuxt UI v4 has been released!" />

    <UHeader />

    <UMain>
      <NuxtLayout>
        <NuxtPage />
      </NuxtLayout>
    </UMain>

    <UFooter />
  </UApp>
</template>
```

## API

### Props

```ts
/**
 * Props for the Banner component
 */
interface BannerProps {
  /**
   * The element or component this component should render as.
   */
  as?: any;
  /**
   * A unique id saved to local storage to remember if the banner has been dismissed.
   * Change this value to show the banner again.
   */
  id?: string | undefined;
  /**
   * The icon displayed next to the title.
   */
  icon?: string | object | undefined;
  title?: string | undefined;
  /**
   * Display a list of actions next to the title.
   * `{ color: 'neutral', size: 'xs' }`{lang="ts-type"}
   */
  actions?: ButtonProps[] | undefined;
  to?: string | RouteLocationAsRelativeGeneric | RouteLocationAsPathGeneric | undefined;
  target?: "_blank" | "_parent" | "_self" | "_top" | (string & {}) | null | undefined;
  color?: "error" | "primary" | "secondary" | "success" | "info" | "warning" | "neutral" | undefined;
  /**
   * Display a close button to dismiss the banner.
   * `{ size: 'md', color: 'neutral', variant: 'ghost' }`{lang="ts-type"}
   */
  close?: boolean | Partial<ButtonProps> | undefined;
  /**
   * The icon displayed in the close button.
   */
  closeIcon?: string | object | undefined;
  ui?: { root?: ClassNameValue; container?: ClassNameValue; left?: ClassNameValue; center?: ClassNameValue; right?: ClassNameValue; icon?: ClassNameValue; title?: ClassNameValue; actions?: ClassNameValue; close?: ClassNameValue; } | undefined;
}
```

### Slots

```ts
/**
 * Slots for the Banner component
 */
interface BannerSlots {
  leading(): any;
  title(): any;
  actions(): any;
  close(): any;
}
```

### Emits

```ts
/**
 * Emitted events for the Banner component
 */
interface BannerEmits {
  close: (payload: []) => void;
}
```

## Theme

```ts [app.config.ts]
export default defineAppConfig({
  ui: {
    banner: {
      slots: {
        root: [
          'relative z-50 w-full',
          'transition-colors'
        ],
        container: 'flex items-center justify-between gap-3 h-12',
        left: 'hidden lg:flex-1 lg:flex lg:items-center',
        center: 'flex items-center gap-1.5 min-w-0',
        right: 'lg:flex-1 flex items-center justify-end',
        icon: 'size-5 shrink-0 text-inverted pointer-events-none',
        title: 'text-sm text-inverted font-medium truncate',
        actions: 'flex gap-1.5 shrink-0 isolate',
        close: 'text-inverted hover:bg-default/10 focus-visible:bg-default/10 -me-1.5 lg:me-0'
      },
      variants: {
        color: {
          primary: {
            root: 'bg-primary'
          },
          secondary: {
            root: 'bg-secondary'
          },
          success: {
            root: 'bg-success'
          },
          info: {
            root: 'bg-info'
          },
          warning: {
            root: 'bg-warning'
          },
          error: {
            root: 'bg-error'
          },
          neutral: {
            root: 'bg-inverted'
          }
        },
        to: {
          true: ''
        }
      },
      compoundVariants: [
        {
          color: 'primary',
          to: true,
          class: {
            root: 'hover:bg-primary/90'
          }
        },
        {
          color: 'secondary',
          to: true,
          class: {
            root: 'hover:bg-secondary/90'
          }
        },
        {
          color: 'success',
          to: true,
          class: {
            root: 'hover:bg-success/90'
          }
        },
        {
          color: 'info',
          to: true,
          class: {
            root: 'hover:bg-info/90'
          }
        },
        {
          color: 'warning',
          to: true,
          class: {
            root: 'hover:bg-warning/90'
          }
        },
        {
          color: 'error',
          to: true,
          class: {
            root: 'hover:bg-error/90'
          }
        },
        {
          color: 'neutral',
          to: true,
          class: {
            root: 'hover:bg-inverted/90'
          }
        }
      ],
      defaultVariants: {
        color: 'primary'
      }
    }
  }
})
```

## Changelog

<component-changelog>



</component-changelog>
