# Source: https://ui.nuxt.com/raw/docs/components/page-aside.md

# PageAside

> A sticky aside to display your page navigation.

## Usage

The PageAside component is a sticky `<aside>` element that is only displayed starting from the [`lg` breakpoint](https://tailwindcss.com/docs/breakpoints).

<tip to="/docs/getting-started/theme/css-variables#header">

The PageAside component uses the `--ui-header-height` CSS variable to position itself correctly below the [Header](/docs/components/header).

</tip>

Use it inside the `left` or `right` slot of the [Page](/docs/components/page) component:

```vue
<template>
  <UPage>
    <template #left>
      <UPageAside />
    </template>
  </UPage>
</template>
```

## Examples

<note>

While these examples use [Nuxt Content](https://content.nuxt.com), the components can be integrated with any content management system.

</note>

### Within a layout

Use the PageAside component in a layout to display the navigation:

```vue [layouts/docs.vue]
<script setup lang="ts">
import type { ContentNavigationItem } from '@nuxt/content'

const navigation = inject<Ref<ContentNavigationItem[]>>('navigation')
</script>

<template>
  <UPage>
    <template #left>
      <UPageAside>
        <UContentNavigation :navigation="navigation" />
      </UPageAside>
    </template>

    <slot />
  </UPage>
</template>
```

<note>

In this example, we use the `ContentNavigation` component to display the navigation injected in `app.vue`.

</note>

## API

### Props

```ts
/**
 * Props for the PageAside component
 */
interface PageAsideProps {
  /**
   * The element or component this component should render as.
   * @default "\"aside\""
   */
  as?: any;
  ui?: { root?: ClassNameValue; container?: ClassNameValue; top?: ClassNameValue; topHeader?: ClassNameValue; topBody?: ClassNameValue; topFooter?: ClassNameValue; } | undefined;
}
```

### Slots

```ts
/**
 * Slots for the PageAside component
 */
interface PageAsideSlots {
  top(): any;
  default(): any;
  bottom(): any;
}
```

## Theme

```ts [app.config.ts]
export default defineAppConfig({
  ui: {
    pageAside: {
      slots: {
        root: 'hidden overflow-y-auto lg:block lg:max-h-[calc(100vh-var(--ui-header-height))] lg:sticky lg:top-(--ui-header-height) py-8 lg:ps-4 lg:-ms-4 lg:pe-6.5',
        container: 'relative',
        top: 'sticky -top-8 -mt-8 pointer-events-none z-[1]',
        topHeader: 'h-8 bg-default -mx-4 px-4',
        topBody: 'bg-default relative pointer-events-auto flex flex-col -mx-4 px-4',
        topFooter: 'h-8 bg-gradient-to-b from-default -mx-4 px-4'
      }
    }
  }
})
```

## Changelog

<component-changelog>



</component-changelog>
