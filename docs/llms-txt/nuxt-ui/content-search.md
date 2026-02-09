# Source: https://ui.nuxt.com/raw/docs/components/content-search.md

# ContentSearch

> A ready to use CommandPalette to add to your documentation.

> [!WARNING]
> See: /docs/getting-started/integrations/content
> This component is only available when the `@nuxt/content` module is installed.

## Usage

The ContentSearch component extends the [CommandPalette](/docs/components/command-palette) component, so you can pass any property such as `icon`, `placeholder`, etc.

Use the `files` and `navigation` props with the `files` and `navigation` values you fetched using the `queryCollectionSearchSections` and `queryCollectionNavigation` composables from `@nuxt/content`.

```vue [ContentSearchExample.vue]
<script setup lang="ts">
import type { ContentNavigationItem } from '@nuxt/content'

const { data: files } = useLazyAsyncData('content-search-example', () => queryCollectionSearchSections('docs'), {
  server: false
})

const navigation = inject<Ref<ContentNavigationItem[]>>('navigation')

const searchTerm = ref('')
</script>

<template>
  <ClientOnly>
    <LazyUContentSearch
      v-model:search-term="searchTerm"
      open
      :autofocus="false"
      :files="files"
      :navigation="navigation"
      :fuse="{ resultLimit: 42 }"
    />
  </ClientOnly>
</template>
```

> [!TIP]
> You can open the CommandPalette by pressing  , by using the [ContentSearchButton](/docs/components/content-search-button) component or by using the `useContentSearch` composable: `const { open } = useContentSearch()`.

### Shortcut

Use the `shortcut` prop to change the shortcut used in [defineShortcuts](/docs/composables/define-shortcuts) to open the ContentSearch component. Defaults to `meta_k` (<kbd value="meta">



</kbd>

 <kbd value="K">



</kbd>

).

```vue [app.vue]
<template>
  <UApp>
    <ClientOnly>
      <LazyUContentSearch
        v-model:search-term="searchTerm"
        shortcut="meta_k"
        :files="files"
        :navigation="navigation"
        :fuse="{ resultLimit: 42 }"
      />
    </ClientOnly>
  </UApp>
</template>
```

### Color Mode

By default, a group of commands will be added to the command palette so you can switch between light and dark mode. This will only take effect if the `colorMode` is not forced in a specific page which can be achieved through `definePageMeta`:

```vue [pages/index.vue]
<script setup lang="ts">
definePageMeta({
  colorMode: 'dark'
})
</script>
```

You can disable this behavior by setting the `color-mode` prop to `false`:

```vue [app.vue]
<template>
  <UApp>
    <ClientOnly>
      <LazyUContentSearch
        v-model:search-term="searchTerm"
        :color-mode="false"
        :files="files"
        :navigation="navigation"
        :fuse="{ resultLimit: 42 }"
      />
    </ClientOnly>
  </UApp>
</template>
```

## Examples

### Within `app.vue`

Use the ContentSearch component in your `app.vue` or in a layout:

```vue [app.vue]
<script setup lang="ts">
const { data: navigation } = await useAsyncData('navigation', () => queryCollectionNavigation('content'))
const { data: files } = useLazyAsyncData('search', () => queryCollectionSearchSections('content'), {
  server: false
})

const links = [{
  label: 'Docs',
  icon: 'i-lucide-book',
  to: '/docs/getting-started'
}, {
  label: 'Components',
  icon: 'i-lucide-box',
  to: '/docs/components'
}, {
  label: 'Showcase',
  icon: 'i-lucide-presentation',
  to: '/showcase'
}]

const searchTerm = ref('')
</script>

<template>
  <UApp>
    <ClientOnly>
      <LazyUContentSearch
        v-model:search-term="searchTerm"
        :files="files"
        shortcut="meta_k"
        :navigation="navigation"
        :links="links"
        :fuse="{ resultLimit: 42 }"
      />
    </ClientOnly>
  </UApp>
</template>
```

> [!TIP]
> It is recommended to wrap the `ContentSearch` component in a [ClientOnly](https://nuxt.com/docs/api/components/client-only) component so it's not rendered on the server.

## API

### Props

```ts
/**
 * Props for the ContentSearch component
 */
interface ContentSearchProps {
  size?: "sm" | "md" | "xs" | "lg" | "xl" | undefined;
  /**
   * The icon displayed in the input.
   */
  icon?: any;
  /**
   * The placeholder text for the input.
   */
  placeholder?: string | undefined;
  /**
   * Automatically focus the input when component is mounted.
   */
  autofocus?: boolean | undefined;
  /**
   * When `true`, the loading icon will be displayed.
   */
  loading?: boolean | undefined;
  /**
   * The icon when the `loading` prop is `true`.
   */
  loadingIcon?: any;
  /**
   * Display a close button in the input (useful when inside a Modal for example).
   * `{ size: 'md', color: 'neutral', variant: 'ghost' }`{lang="ts-type"}
   * @default "true"
   */
  close?: boolean | Omit<ButtonProps, LinkPropsKeys> | undefined;
  /**
   * The icon displayed in the close button.
   */
  closeIcon?: any;
  /**
   * Keyboard shortcut to open the search (used by [`defineShortcuts`](https://ui.nuxt.com/docs/composables/define-shortcuts))
   * @default "\"meta_k\""
   */
  shortcut?: string | undefined;
  /**
   * Links group displayed as the first group in the command palette.
   */
  links?: T[] | undefined;
  navigation?: ContentNavigationItem[] | undefined;
  /**
   * Custom groups displayed between navigation and color mode group.
   */
  groups?: CommandPaletteGroup<ContentSearchItem>[] | undefined;
  files?: ContentSearchFile[] | undefined;
  /**
   * Options for [useFuse](https://vueuse.org/integrations/useFuse) passed to the [CommandPalette](https://ui.nuxt.com/docs/components/command-palette).
   */
  fuse?: n<T> | undefined;
  /**
   * When `true`, the theme command will be added to the groups.
   * @default "true"
   */
  colorMode?: boolean | undefined;
  ui?: ({ modal?: ClassNameValue; input?: ClassNameValue; } & { root?: ClassNameValue; input?: ClassNameValue; close?: ClassNameValue; back?: ClassNameValue; content?: ClassNameValue; footer?: ClassNameValue; viewport?: ClassNameValue; group?: ClassNameValue; empty?: ClassNameValue; label?: ClassNameValue; item?: ClassNameValue; itemLeadingIcon?: ClassNameValue; itemLeadingAvatar?: ClassNameValue; itemLeadingAvatarSize?: ClassNameValue; itemLeadingChip?: ClassNameValue; itemLeadingChipSize?: ClassNameValue; itemTrailing?: ClassNameValue; itemTrailingIcon?: ClassNameValue; itemTrailingHighlightedIcon?: ClassNameValue; itemTrailingKbds?: ClassNameValue; itemTrailingKbdsSize?: ClassNameValue; itemWrapper?: ClassNameValue; itemLabel?: ClassNameValue; itemDescription?: ClassNameValue; itemLabelBase?: ClassNameValue; itemLabelPrefix?: ClassNameValue; itemLabelSuffix?: ClassNameValue; }) | undefined;
  title?: string | undefined;
  description?: string | undefined;
  /**
   * Render an overlay behind the modal.
   */
  overlay?: boolean | undefined;
  /**
   * Animate the modal when opening or closing.
   */
  transition?: boolean | undefined;
  /**
   * The content of the modal.
   */
  content?: (Omit<DialogContentProps, "as" | "asChild" | "forceMount"> & Partial<EmitsToProps<DialogContentImplEmits>>) | undefined;
  /**
   * When `false`, the modal will not close when clicking outside or pressing escape.
   */
  dismissible?: boolean | undefined;
  /**
   * When `true`, the modal will take up the full screen.
   * @default "false"
   */
  fullscreen?: boolean | undefined;
  /**
   * The modality of the dialog When set to `true`, <br>
   * interaction with outside elements will be disabled and only dialog content will be visible to screen readers.
   */
  modal?: boolean | undefined;
  /**
   * Render the modal in a portal.
   */
  portal?: string | boolean | HTMLElement | undefined;
  /**
   * @default "\"\""
   */
  searchTerm?: string | undefined;
}
```

### Slots

```ts
/**
 * Slots for the ContentSearch component
 */
interface ContentSearchSlots {
  empty(): any;
  footer(): any;
  back(): any;
  close(): any;
  item(): any;
  item-leading(): any;
  item-label(): any;
  item-description(): any;
  item-trailing(): any;
  content(): any;
}
```

### Emits

```ts
/**
 * Emitted events for the ContentSearch component
 */
interface ContentSearchEmits {
  update:searchTerm: (payload: [value: string]) => void;
}
```

### Expose

When accessing the component via a template ref, you can use the following:

<table>
<thead>
  <tr>
    <th>
      Name
    </th>
    
    <th>
      Type
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code className="language-ts-type shiki shiki-themes material-theme-lighter material-theme material-theme-palenight" language="ts-type" style="">
        <span class="sBMFI">
          commandPaletteRef
        </span>
      </code>
    </td>
    
    <td>
      <code className="language-ts-type shiki shiki-themes material-theme-lighter material-theme material-theme-palenight" language="ts-type" style="">
        <span class="sBMFI">
          Ref
        </span>
        
        <span class="sMK4o">
          <
        </span>
        
        <span class="sBMFI">
          InstanceType
        </span>
        
        <span class="sMK4o">
          <typeof
        </span>
        
        <span class="sTEyZ">
          UCommandPalette
        </span>
        
        <span class="sMK4o">
          >
        </span>
        
        <span class="sMK4o">
          |
        </span>
        
        <span class="sBMFI">
          null
        </span>
        
        <span class="sMK4o">
          >
        </span>
      </code>
    </td>
  </tr>
</tbody>
</table>

## Theme

```ts [app.config.ts]
export default defineAppConfig({
  ui: {
    contentSearch: {
      slots: {
        modal: '',
        input: ''
      },
      variants: {
        fullscreen: {
          false: {
            modal: 'sm:max-w-3xl h-full sm:h-[28rem]'
          }
        },
        size: {
          xs: {
            input: '[&>input]:text-sm'
          },
          sm: {
            input: '[&>input]:text-sm'
          },
          md: {
            input: '[&>input]:text-base/5'
          },
          lg: {
            input: '[&>input]:text-base/5'
          },
          xl: {
            input: '[&>input]:text-lg'
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

See the [releases page](https://github.com/nuxt/ui/releases) for the latest changes.
