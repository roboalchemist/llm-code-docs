# Source: https://ui.nuxt.com/raw/docs/components/content-toc.md

# ContentToc

> A sticky Table of Contents with automatic active anchor link highlighting.

<warning to="/docs/getting-started/integrations/content">

This component is only available when the `@nuxt/content` module is installed.

</warning>

## Usage

Use the `links` prop with the `page?.body?.toc?.links` you get when fetching a page.

```vue [ContentTocExample.vue]
<script setup lang="ts">
const route = useRoute()

const { data: page } = await useAsyncData(route.path, () => queryCollection('docs').path(route.path).first())
if (!page.value) {
  throw createError({ statusCode: 404, statusMessage: 'Page not found', fatal: true })
}
</script>

<template>
  <UContentToc :links="page?.body?.toc?.links" />
</template>
```

### Title

Use the `title` prop to change the title of the Table of Contents.

```vue
<template>
  <UContentToc title="On this page" />
</template>
```

### Color

Use the `color` prop to change the color of the links.

```vue
<template>
  <UContentToc color="neutral" />
</template>
```

### Highlight

Use the `highlight` prop to display a highlighted border for the active item.

Use the `highlight-color` prop to change the color of the border. It defaults to the `color` prop.

```vue
<template>
  <UContentToc highlight highlight-color="neutral" color="neutral" />
</template>
```

## Examples

### Within a page

Use the ContentToc component in a page to display the Table of Contents:

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
 * Props for the ContentToc component
 */
interface ContentTocProps {
  /**
   * The element or component this component should render as.
   * @default "\"nav\""
   */
  as?: any;
  /**
   * The icon displayed to collapse the content.
   */
  trailingIcon?: string | object | undefined;
  /**
   * The title of the table of contents.
   */
  title?: string | undefined;
  color?: "primary" | "secondary" | "success" | "info" | "warning" | "error" | "neutral" | undefined;
  /**
   * Display a line next to the active link.
   */
  highlight?: boolean | undefined;
  highlightColor?: "primary" | "secondary" | "success" | "info" | "warning" | "error" | "neutral" | undefined;
  links?: ContentTocLink[] | undefined;
  ui?: { root?: ClassNameValue; container?: ClassNameValue; top?: ClassNameValue; bottom?: ClassNameValue; trigger?: ClassNameValue; title?: ClassNameValue; trailing?: ClassNameValue; trailingIcon?: ClassNameValue; content?: ClassNameValue; list?: ClassNameValue; listWithChildren?: ClassNameValue; item?: ClassNameValue; itemWithChildren?: ClassNameValue; link?: ClassNameValue; linkText?: ClassNameValue; indicator?: ClassNameValue; } | undefined;
  /**
   * The open state of the collapsible when it is initially rendered. <br> Use when you do not need to control its open state.
   */
  defaultOpen?: boolean | undefined;
  /**
   * The controlled open state of the collapsible. Can be binded with `v-model`.
   */
  open?: boolean | undefined;
}
```

### Slots

```ts
/**
 * Slots for the ContentToc component
 */
interface ContentTocSlots {
  leading(): any;
  default(): any;
  trailing(): any;
  content(): any;
  link(): any;
  top(): any;
  bottom(): any;
}
```

### Emits

```ts
/**
 * Emitted events for the ContentToc component
 */
interface ContentTocEmits {
  update:open: (payload: [value: boolean]) => void;
  move: (payload: [id: string]) => void;
}
```

## Theme

```ts [app.config.ts]
export default defineAppConfig({
  ui: {
    contentToc: {
      slots: {
        root: 'sticky top-(--ui-header-height) z-10 bg-default/75 lg:bg-[initial] backdrop-blur -mx-4 px-4 sm:px-6 sm:-mx-6 overflow-y-auto max-h-[calc(100vh-var(--ui-header-height))]',
        container: 'pt-4 sm:pt-6 pb-2.5 sm:pb-4.5 lg:py-8 border-b border-dashed border-default lg:border-0 flex flex-col',
        top: '',
        bottom: 'hidden lg:flex lg:flex-col gap-6',
        trigger: 'group text-sm font-semibold flex-1 flex items-center gap-1.5 py-1.5 -mt-1.5 focus-visible:outline-primary',
        title: 'truncate',
        trailing: 'ms-auto inline-flex gap-1.5 items-center',
        trailingIcon: 'size-5 transform transition-transform duration-200 shrink-0 group-data-[state=open]:rotate-180 lg:hidden',
        content: 'data-[state=open]:animate-[collapsible-down_200ms_ease-out] data-[state=closed]:animate-[collapsible-up_200ms_ease-out] overflow-hidden focus:outline-none',
        list: 'min-w-0',
        listWithChildren: 'ms-3',
        item: 'min-w-0',
        itemWithChildren: '',
        link: 'group relative text-sm flex items-center focus-visible:outline-primary py-1',
        linkText: 'truncate',
        indicator: 'absolute ms-2.5 transition-[translate,height] duration-200 h-(--indicator-size) translate-y-(--indicator-position) w-px rounded-full'
      },
      variants: {
        color: {
          primary: '',
          secondary: '',
          success: '',
          info: '',
          warning: '',
          error: '',
          neutral: ''
        },
        highlightColor: {
          primary: {
            indicator: 'bg-primary'
          },
          secondary: {
            indicator: 'bg-secondary'
          },
          success: {
            indicator: 'bg-success'
          },
          info: {
            indicator: 'bg-info'
          },
          warning: {
            indicator: 'bg-warning'
          },
          error: {
            indicator: 'bg-error'
          },
          neutral: {
            indicator: 'bg-inverted'
          }
        },
        active: {
          false: {
            link: [
              'text-muted hover:text-default',
              'transition-colors'
            ]
          }
        },
        highlight: {
          true: {
            list: 'ms-2.5 ps-4 border-s border-default',
            item: '-ms-px'
          }
        },
        body: {
          true: {
            bottom: 'mt-6'
          }
        }
      },
      compoundVariants: [
        {
          color: 'primary',
          active: true,
          class: {
            link: 'text-primary',
            linkLeadingIcon: 'text-primary'
          }
        },
        {
          color: 'secondary',
          active: true,
          class: {
            link: 'text-secondary',
            linkLeadingIcon: 'text-secondary'
          }
        },
        {
          color: 'success',
          active: true,
          class: {
            link: 'text-success',
            linkLeadingIcon: 'text-success'
          }
        },
        {
          color: 'info',
          active: true,
          class: {
            link: 'text-info',
            linkLeadingIcon: 'text-info'
          }
        },
        {
          color: 'warning',
          active: true,
          class: {
            link: 'text-warning',
            linkLeadingIcon: 'text-warning'
          }
        },
        {
          color: 'error',
          active: true,
          class: {
            link: 'text-error',
            linkLeadingIcon: 'text-error'
          }
        },
        {
          color: 'neutral',
          active: true,
          class: {
            link: 'text-highlighted',
            linkLeadingIcon: 'text-highlighted'
          }
        }
      ],
      defaultVariants: {
        color: 'primary',
        highlightColor: 'primary'
      }
    }
  }
})
```

## Changelog

<component-changelog prefix="content">



</component-changelog>
