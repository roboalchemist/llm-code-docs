# Source: https://ui.nuxt.com/raw/docs/components/page-links.md

# PageLinks

> A list of links to be displayed in the page.

## Usage

Use the PageLinks component to display a list of links.

```vue
<template>
  <UPageLinks />
</template>
```

### Links

Use the `links` prop as an array of objects with the following properties:

- `label: string`
- `icon?: string`
- `class?: any`
- `ui?: { item?: ClassNameValue, link?: ClassNameValue, linkLabel?: ClassNameValue, linkLabelExternalIcon?: ClassNameValue, linkLeadingIcon?: ClassNameValue }`

You can pass any property from the [Link](/docs/components/link#props) component such as `to`, `target`, etc.

```vue
<script setup lang="ts">
import type { PageLink } from '@nuxt/ui'
</script>

<template>
  <UPageLinks />
</template>
```

### Title

Use the `title` prop to display a title above the links.

```vue
<script setup lang="ts">
import type { PageLink } from '@nuxt/ui'
</script>

<template>
  <UPageLinks title="Community" />
</template>
```

## Examples

<note>

While these examples use [Nuxt Content](https://content.nuxt.com), the components can be integrated with any content management system.

</note>

### Within a page

Use the PageLinks component in the `bottom` slot of the ContentToc component to display a list of links below the table of contents.

```vue [pages/[...slug].vue]
<script setup lang="ts">
import type { PageLink } from '@nuxt/ui'

const route = useRoute()

definePageMeta({
  layout: 'docs'
})

const { data: page } = await useAsyncData(route.path, () => {
  return queryCollection('docs').path(route.path).first()
})

const { data: surround } = await useAsyncData(`${route.path}-surround`, () => {
  return queryCollectionItemSurroundings('content', route.path)
})

const links = computed<PageLink[]>(() => [{
  icon: 'i-lucide-file-pen',
  label: 'Edit this page',
  to: `https://github.com/nuxt/ui/edit/v4/docs/content/${page?.value?.stem}.md`,
  target: '_blank'
}, {
  icon: 'i-lucide-star',
  label: 'Star on GitHub',
  to: 'https://github.com/nuxt/ui',
  target: '_blank'
}, {
  label: 'Releases',
  icon: 'i-lucide-rocket',
  to: 'https://github.com/nuxt/ui/releases'
}])
</script>

<template>
  <UPage>
    <UPageHeader :title="page.title" :description="page.description" />

    <UPageBody>
      <ContentRenderer :value="page" />

      <USeparator />

      <UContentSurround :surround="surround" />
    </UPageBody>

    <template #right>
      <UContentToc :links="page.body.toc.links">
        <template #bottom>
          <USeparator type="dashed" />

          <UPageLinks title="Community" :links="links" />
        </template>
      </UContentToc>
    </template>
  </UPage>
</template>
```

## API

### Props

```ts
/**
 * Props for the PageLinks component
 */
interface PageLinksProps {
  /**
   * The element or component this component should render as.
   * @default "\"nav\""
   */
  as?: any;
  title?: string | undefined;
  links?: PageLink[] | undefined;
  ui?: { root?: ClassNameValue; title?: ClassNameValue; list?: ClassNameValue; item?: ClassNameValue; link?: ClassNameValue; linkLeadingIcon?: ClassNameValue; linkLabel?: ClassNameValue; linkLabelExternalIcon?: ClassNameValue; } | undefined;
}
```

### Slots

```ts
/**
 * Slots for the PageLinks component
 */
interface PageLinksSlots {
  title(): any;
  link(): any;
  link-leading(): any;
  link-label(): any;
  link-trailing(): any;
}
```

## Theme

```ts [app.config.ts]
export default defineAppConfig({
  ui: {
    pageLinks: {
      slots: {
        root: 'flex flex-col gap-3',
        title: 'text-sm font-semibold flex items-center gap-1.5',
        list: 'flex flex-col gap-2',
        item: 'relative',
        link: 'group text-sm flex items-center gap-1.5 focus-visible:outline-primary',
        linkLeadingIcon: 'size-5 shrink-0',
        linkLabel: 'truncate',
        linkLabelExternalIcon: 'size-3 absolute top-0 text-dimmed'
      },
      variants: {
        active: {
          true: {
            link: 'text-primary font-medium'
          },
          false: {
            link: [
              'text-muted hover:text-default',
              'transition-colors'
            ]
          }
        }
      }
    }
  }
})
```

## Changelog

<component-changelog>



</component-changelog>
