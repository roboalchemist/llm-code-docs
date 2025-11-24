# Source: https://ui.nuxt.com/raw/docs/components/breadcrumb.md

# Breadcrumb

> A hierarchy of links to navigate through a website.

## Usage

Use the Breadcrumb component to show the current page's location in your site's hierarchy.

```vue
<script setup lang="ts">
const items = ref<undefined>([
  {
    label: 'Docs',
    icon: 'i-lucide-book-open',
    to: '/docs',
  },
  {
    label: 'Components',
    icon: 'i-lucide-box',
    to: '/docs/components',
  },
  {
    label: 'Breadcrumb',
    icon: 'i-lucide-link',
    to: '/docs/components/breadcrumb',
  },
])
</script>

<template>
  <UBreadcrumb :items="items" />
</template>
```

### Items

Use the `items` prop as an array of objects with the following properties:

- `label?: string`
- `icon?: string`
- `avatar?: AvatarProps`
- [`slot?: string`](#with-custom-slot)
- `class?: any`
- `ui?: { item?: ClassNameValue, link?: ClassNameValue, linkLeadingIcon?: ClassNameValue, linkLeadingAvatar?: ClassNameValue, linkLabel?: ClassNameValue, separator?: ClassNameValue, separatorIcon?: ClassNameValue }`

You can pass any property from the [Link](/docs/components/link#props) component such as `to`, `target`, etc.

```vue
<script setup lang="ts">
import type { BreadcrumbItem } from '@nuxt/ui'

const items = ref<BreadcrumbItem[]>([
  {
    label: 'Docs',
    icon: 'i-lucide-book-open',
    to: '/docs',
  },
  {
    label: 'Components',
    icon: 'i-lucide-box',
    to: '/docs/components',
  },
  {
    label: 'Breadcrumb',
    icon: 'i-lucide-link',
    to: '/docs/components/breadcrumb',
  },
])
</script>

<template>
  <UBreadcrumb :items="items" />
</template>
```

<note>

A `span` is rendered instead of a link when the `to` property is not defined.

</note>

### Separator Icon

Use the `separator-icon` prop to customize the [Icon](/docs/components/icon) between each item. Defaults to `i-lucide-chevron-right`.

```vue
<script setup lang="ts">
import type { BreadcrumbItem } from '@nuxt/ui'

const items = ref<BreadcrumbItem[]>([
  {
    label: 'Docs',
    icon: 'i-lucide-book-open',
    to: '/docs',
  },
  {
    label: 'Components',
    icon: 'i-lucide-box',
    to: '/docs/components',
  },
  {
    label: 'Breadcrumb',
    icon: 'i-lucide-link',
    to: '/docs/components/breadcrumb',
  },
])
</script>

<template>
  <UBreadcrumb separator-icon="i-lucide-arrow-right" :items="items" />
</template>
```

<framework-only>
<template v-slot:nuxt="">
<tip to="/docs/getting-started/integrations/icons/nuxt#theme">

You can customize this icon globally in your `app.config.ts` under `ui.icons.chevronRight` key.

</tip>
</template>

<template v-slot:vue="">
<tip to="/docs/getting-started/integrations/icons/vue#theme">

You can customize this icon globally in your `vite.config.ts` under `ui.icons.chevronRight` key.

</tip>
</template>
</framework-only>

## Examples

### With separator slot

Use the `#separator` slot to customize the separator between each item.

```vue [BreadcrumbSeparatorSlotExample.vue]
<script setup lang="ts">
import type { BreadcrumbItem } from '@nuxt/ui'

const items: BreadcrumbItem[] = [
  {
    label: 'Docs',
    to: '/docs'
  },
  {
    label: 'Components',
    to: '/docs/components'
  },
  {
    label: 'Breadcrumb',
    to: '/docs/components/breadcrumb'
  }
]
</script>

<template>
  <UBreadcrumb :items="items">
    <template #separator>
      <span class="mx-2 text-muted">/</span>
    </template>
  </UBreadcrumb>
</template>
```

### With custom slot

Use the `slot` property to customize a specific item.

You will have access to the following slots:

- `#{{ item.slot }}`
- `#{{ item.slot }}-leading`
- `#{{ item.slot }}-label`
- `#{{ item.slot }}-trailing`

```vue [BreadcrumbCustomSlotExample.vue]
<script setup lang="ts">
import type { BreadcrumbItem } from '@nuxt/ui'

const items = [
  {
    label: 'Home',
    to: '/'
  },
  {
    slot: 'dropdown' as const,
    icon: 'i-lucide-ellipsis',
    children: [
      {
        label: 'Documentation',
        to: '/docs'
      },
      {
        label: 'Themes'
      },
      {
        label: 'GitHub'
      }
    ]
  },
  {
    label: 'Components',
    to: '/docs/components'
  },
  {
    label: 'Breadcrumb',
    to: '/docs/components/breadcrumb'
  }
] satisfies BreadcrumbItem[]
</script>

<template>
  <UBreadcrumb :items="items">
    <template #dropdown="{ item }">
      <UDropdownMenu :items="item.children">
        <UButton :icon="item.icon" color="neutral" variant="link" class="p-0.5" />
      </UDropdownMenu>
    </template>
  </UBreadcrumb>
</template>
```

<tip to="#slots">

You can also use the `#item`, `#item-leading`, `#item-label` and `#item-trailing` slots to customize all items.

</tip>

## API

### Props

```ts
/**
 * Props for the Breadcrumb component
 */
interface BreadcrumbProps {
  /**
   * The element or component this component should render as.
   * @default "\"nav\""
   */
  as?: any;
  items?: BreadcrumbItem[] | undefined;
  /**
   * The icon to use as a separator.
   */
  separatorIcon?: string | object | undefined;
  /**
   * The key used to get the label from the item.
   * @default "\"label\""
   */
  labelKey?: GetItemKeys<BreadcrumbItem> | undefined;
  ui?: { root?: ClassNameValue; list?: ClassNameValue; item?: ClassNameValue; link?: ClassNameValue; linkLeadingIcon?: ClassNameValue; linkLeadingAvatar?: ClassNameValue; linkLeadingAvatarSize?: ClassNameValue; linkLabel?: ClassNameValue; separator?: ClassNameValue; separatorIcon?: ClassNameValue; } | undefined;
}
```

### Slots

```ts
/**
 * Slots for the Breadcrumb component
 */
interface BreadcrumbSlots {
  item(): any;
  item-leading(): any;
  item-label(): any;
  item-trailing(): any;
  separator(): any;
}
```

## Theme

```ts [app.config.ts]
export default defineAppConfig({
  ui: {
    breadcrumb: {
      slots: {
        root: 'relative min-w-0',
        list: 'flex items-center gap-1.5',
        item: 'flex min-w-0',
        link: 'group relative flex items-center gap-1.5 text-sm min-w-0 focus-visible:outline-primary',
        linkLeadingIcon: 'shrink-0 size-5',
        linkLeadingAvatar: 'shrink-0',
        linkLeadingAvatarSize: '2xs',
        linkLabel: 'truncate',
        separator: 'flex',
        separatorIcon: 'shrink-0 size-5 text-muted'
      },
      variants: {
        active: {
          true: {
            link: 'text-primary font-semibold'
          },
          false: {
            link: 'text-muted font-medium'
          }
        },
        disabled: {
          true: {
            link: 'cursor-not-allowed opacity-75'
          }
        },
        to: {
          true: ''
        }
      },
      compoundVariants: [
        {
          disabled: false,
          active: false,
          to: true,
          class: {
            link: [
              'hover:text-default',
              'transition-colors'
            ]
          }
        }
      ]
    }
  }
})
```

## Changelog

<component-changelog>



</component-changelog>
