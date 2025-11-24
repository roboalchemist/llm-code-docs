# Source: https://ui.nuxt.com/raw/docs/components/page-anchors.md

# PageAnchors

> A list of anchors to be displayed in the page.

## Usage

Use the PageAnchors component to display a list of links.

```vue
<template>
  <UPageAnchors />
</template>
```

### Links

Use the `links` prop as an array of objects with the following properties:

- `label: string`
- `icon?: string`
- `class?: any`
- `ui?: { item?: ClassNameValue, link?: ClassNameValue, linkLabel?: ClassNameValue, linkLabelExternalIcon?: ClassNameValue, linkLeading?: ClassNameValue, linkLeadingIcon?: ClassNameValue }`

You can pass any property from the [Link](/docs/components/link#props) component such as `to`, `target`, etc.

```vue
<script setup lang="ts">
import type { PageAnchor } from '@nuxt/ui'
</script>

<template>
  <UPageAnchors />
</template>
```

## Examples

<note>

While these examples use [Nuxt Content](https://content.nuxt.com), the components can be integrated with any content management system.

</note>

### Within a layout

Use the PageAnchors component inside the [PageAside](/docs/components/page-aside) component to display a list of links above the navigation.

```vue [layouts/docs.vue]
<script setup lang="ts">
import type { PageAnchor } from '@nuxt/ui'
import type { ContentNavigationItem } from '@nuxt/content'

const navigation = inject<ContentNavigationItem[]>('navigation')

const links: PageAnchor[] = [{
  label: 'Documentation',
  icon: 'i-lucide-book-open',
  to: '/docs/getting-started'
}, {
  label: 'Components',
  icon: 'i-lucide-box',
  to: '/docs/components'
}, {
  label: 'Figma Kit',
  icon: 'i-simple-icons-figma',
  to: 'https://go.nuxt.com/figma-ui',
  target: '_blank'
}, {
  label: 'Releases',
  icon: 'i-lucide-rocket',
  to: 'https://github.com/nuxt/ui/releases',
  target: '_blank'
}]
</script>

<template>
  <UPage>
    <template #left>
      <UPageAside>
        <UPageAnchors :links="links" />

        <USeparator type="dashed" />

        <UContentNavigation :navigation="navigation" />
      </UPageAside>
    </template>

    <slot />
  </UPage>
</template>
```

## API

### Props

```ts
/**
 * Props for the PageAnchors component
 */
interface PageAnchorsProps {
  /**
   * The element or component this component should render as.
   * @default "\"nav\""
   */
  as?: any;
  links?: PageAnchor[] | undefined;
  ui?: { root?: ClassNameValue; list?: ClassNameValue; item?: ClassNameValue; link?: ClassNameValue; linkLeading?: ClassNameValue; linkLeadingIcon?: ClassNameValue; linkLabel?: ClassNameValue; linkLabelExternalIcon?: ClassNameValue; } | undefined;
}
```

### Slots

```ts
/**
 * Slots for the PageAnchors component
 */
interface PageAnchorsSlots {
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
    pageAnchors: {
      slots: {
        root: '',
        list: '',
        item: 'relative',
        link: 'group text-sm flex items-center gap-1.5 py-1 focus-visible:outline-primary',
        linkLeading: 'rounded-md p-1 inline-flex ring-inset ring',
        linkLeadingIcon: 'size-4 shrink-0',
        linkLabel: 'truncate',
        linkLabelExternalIcon: 'size-3 absolute top-0 text-dimmed'
      },
      variants: {
        active: {
          true: {
            link: 'text-primary font-semibold',
            linkLeading: 'bg-primary ring-primary text-inverted'
          },
          false: {
            link: [
              'text-muted hover:text-default font-medium',
              'transition-colors'
            ],
            linkLeading: [
              'bg-elevated/50 ring-accented text-dimmed group-hover:bg-primary group-hover:ring-primary group-hover:text-inverted',
              'transition'
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
