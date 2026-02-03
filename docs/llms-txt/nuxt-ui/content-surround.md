# Source: https://ui.nuxt.com/raw/docs/components/content-surround.md

# ContentSurround

> A pair of prev and next links to navigate between pages.

> [!WARNING]
> See: /docs/getting-started/integrations/content
> This component is only available when the `@nuxt/content` module is installed.

## Usage

Use the `surround` prop with the `surround` value you get when fetching a page surround.

```vue [ContentSurroundExample.vue]
<script setup lang="ts">
const route = useRoute()

const { data: surround } = await useAsyncData(`${route.path}-surround`, () => {
  return queryCollectionItemSurroundings('docs', route.path, {
    fields: ['description']
  })
})
</script>

<template>
  <UContentSurround :surround="(surround as any)" />
</template>
```

### Prev / Next

Use the `prev-icon` and `next-icon` props to customize the buttons [Icon](/docs/components/icon).

```vue
<script setup lang="ts">
import type { ContentSurroundLink } from '@nuxt/ui'
</script>

<template>
  <UContentSurround prev-icon="i-lucide-chevron-left" next-icon="i-lucide-chevron-right" />
</template>
```

## Examples

### Within a page

Use the ContentSurround component in a page to display the prev and next links:

```vue [pages/[...slug].vue]
<script setup lang="ts">
const route = useRoute()

const { data: page } = await useAsyncData(route.path, () => queryCollection('docs').path(route.path).first())
if (!page.value) {
  throw createError({ statusCode: 404, statusMessage: 'Page not found', fatal: true })
}
</script>

<template>
  <UPage v-if="page">
    <UPageHeader :title="page.title" />

    <UPageBody>
      <ContentRenderer v-if="page.body" :value="page" />

      <USeparator v-if="surround?.filter(Boolean).length" />

      <UContentSurround :surround="(surround as any)" />
    </UPageBody>

    <template v-if="page?.body?.toc?.links?.length" #right>
      <UContentToc :links="page.body.toc.links" />
    </template>
  </UPage>
</template>
```

## API

### Props

```ts
/**
 * Props for the ContentSurround component
 */
interface ContentSurroundProps {
  /**
   * The element or component this component should render as.
   */
  as?: any;
  /**
   * The icon displayed in the prev link.
   */
  prevIcon?: any;
  /**
   * The icon displayed in the next link.
   */
  nextIcon?: any;
  surround?: T[] | undefined;
  ui?: { root?: ClassNameValue; link?: ClassNameValue; linkLeading?: ClassNameValue; linkLeadingIcon?: ClassNameValue; linkTitle?: ClassNameValue; linkDescription?: ClassNameValue; } | undefined;
}
```

### Slots

```ts
/**
 * Slots for the ContentSurround component
 */
interface ContentSurroundSlots {
  link(): any;
  link-leading(): any;
  link-title(): any;
  link-description(): any;
}
```

## Theme

```ts [app.config.ts]
export default defineAppConfig({
  ui: {
    contentSurround: {
      slots: {
        root: 'grid grid-cols-1 sm:grid-cols-2 gap-8',
        link: [
          'group block px-6 py-8 rounded-lg border border-default hover:bg-elevated/50 focus-visible:outline-primary',
          'transition-colors'
        ],
        linkLeading: [
          'inline-flex items-center rounded-full p-1.5 bg-elevated group-hover:bg-primary/10 ring ring-accented mb-4 group-hover:ring-primary/50',
          'transition'
        ],
        linkLeadingIcon: [
          'size-5 shrink-0 text-highlighted group-hover:text-primary',
          'transition-[color,translate]'
        ],
        linkTitle: 'font-medium text-[15px] text-highlighted mb-1 truncate',
        linkDescription: 'text-sm text-muted line-clamp-2'
      },
      variants: {
        direction: {
          left: {
            linkLeadingIcon: [
              'group-active:-translate-x-0.5'
            ]
          },
          right: {
            link: 'text-right',
            linkLeadingIcon: [
              'group-active:translate-x-0.5'
            ]
          }
        }
      }
    }
  }
})
```

## Changelog

See the [releases page](https://github.com/nuxt/ui/releases) for the latest changes.
