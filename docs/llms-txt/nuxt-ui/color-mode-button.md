# Source: https://ui.nuxt.com/raw/docs/components/color-mode-button.md

# ColorModeButton

> A Button to switch between light and dark mode.

## Usage

The ColorModeButton component extends the [Button](/docs/components/button) component, so you can pass any property such as `color`, `variant`, `size`, etc.

```vue
<template>
  <UColorModeButton />
</template>
```

<note>

The button defaults to `color="neutral"` and `variant="ghost"`.

</note>

## Examples

### With custom icons

<framework-only>
<template v-slot:nuxt="">
<div>

Use the `app.config.ts` to customize the icon with the `ui.icons` property:

```ts [app.config.ts]
export default defineAppConfig({
  ui: {
    icons: {
      light: 'i-ph-sun',
      dark: 'i-ph-moon'
    }
  }
})
```

</div>
</template>

<template v-slot:vue="">
<div>

Use the `vite.config.ts` to customize the icon with the `ui.icons` property:

```ts [vite.config.ts]
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import ui from '@nuxt/ui/vite'

export default defineConfig({
  plugins: [
    vue(),
    ui({
      ui: {
        icons: {
          light: 'i-ph-sun',
          dark: 'i-ph-moon'
        }
      }
    })
  ]
})
```

</div>
</template>
</framework-only>

### With fallback slot

As the button is wrapped in a [ClientOnly](https://nuxt.com/docs/api/components/client-only) component, you can pass a `fallback` slot to display a placeholder while the component is loading.

```vue
<template>
  <UColorModeButton>
    <template #fallback>
      <UButton loading variant="ghost" color="neutral" />
    </template></UColorModeButton>
</template>
```

## API

### Props

```ts
/**
 * Props for the ColorModeButton component
 */
interface ColorModeButtonProps {
  /**
   * @default "\"neutral\""
   */
  color?: "primary" | "secondary" | "success" | "info" | "warning" | "error" | "neutral" | undefined;
  /**
   * @default "\"ghost\""
   */
  variant?: "link" | "ghost" | "solid" | "outline" | "soft" | "subtle" | undefined;
  /**
   * The element or component this component should render as when not a link.
   */
  as?: any;
  /**
   * Display an icon on the right side.
   */
  trailingIcon?: string | object | undefined;
  ui?: { base?: ClassNameValue; label?: ClassNameValue; leadingIcon?: ClassNameValue; leadingAvatar?: ClassNameValue; leadingAvatarSize?: ClassNameValue; trailingIcon?: ClassNameValue; } | undefined;
  name?: string | undefined;
  /**
   * Force the link to be active independent of the current route.
   */
  active?: boolean | undefined;
  /**
   * When `true`, the icon will be displayed on the right side.
   */
  trailing?: boolean | undefined;
  /**
   * When `true`, the loading icon will be displayed.
   */
  loading?: boolean | undefined;
  referrerpolicy?: HTMLAttributeReferrerPolicy | undefined;
  onClick?: ((event: MouseEvent) => void | Promise<void>) | ((event: MouseEvent) => void | Promise<void>)[] | undefined;
  /**
   * Display an icon based on the `leading` and `trailing` props.
   */
  icon?: string | object | undefined;
  size?: "md" | "xs" | "sm" | "lg" | "xl" | undefined;
  /**
   * Display an avatar on the left side.
   */
  avatar?: AvatarProps | undefined;
  /**
   * Route Location the link should navigate to when clicked on.
   */
  to?: string | RouteLocationAsRelativeGeneric | RouteLocationAsPathGeneric | undefined;
  /**
   * Class to apply when the link is active
   */
  activeClass?: string | undefined;
  /**
   * Class to apply when the link is exact active
   */
  exactActiveClass?: string | undefined;
  /**
   * Value passed to the attribute `aria-current` when the link is exact active.
   */
  ariaCurrentValue?: "page" | "step" | "location" | "date" | "time" | "true" | "false" | undefined;
  /**
   * Pass the returned promise of `router.push()` to `document.startViewTransition()` if supported.
   */
  viewTransition?: boolean | undefined;
  /**
   * Calls `router.replace` instead of `router.push`.
   */
  replace?: boolean | undefined;
  /**
   * An alias for `to`. If used with `to`, `href` will be ignored
   */
  href?: string | RouteLocationAsRelativeGeneric | RouteLocationAsPathGeneric | undefined;
  /**
   * Forces the link to be considered as external (true) or internal (false). This is helpful to handle edge-cases
   */
  external?: boolean | undefined;
  /**
   * Where to display the linked URL, as the name for a browsing context.
   */
  target?: "_blank" | "_parent" | "_self" | "_top" | (string & {}) | null | undefined;
  /**
   * A rel attribute value to apply on the link. Defaults to "noopener noreferrer" for external links.
   */
  rel?: (string & {}) | "noopener" | "noreferrer" | "nofollow" | "sponsored" | "ugc" | null | undefined;
  /**
   * If set to true, no rel attribute will be added to the link
   */
  noRel?: boolean | undefined;
  /**
   * A class to apply to links that have been prefetched.
   */
  prefetchedClass?: string | undefined;
  /**
   * When enabled will prefetch middleware, layouts and payloads of links in the viewport.
   */
  prefetch?: boolean | undefined;
  /**
   * Allows controlling when to prefetch links. By default, prefetch is triggered only on visibility.
   */
  prefetchOn?: "visibility" | "interaction" | Partial<{ visibility: boolean; interaction: boolean; }> | undefined;
  /**
   * Escape hatch to disable `prefetch` attribute.
   */
  noPrefetch?: boolean | undefined;
  /**
   * An option to either add or remove trailing slashes in the `href` for this specific link.
   * Overrides the global `trailingSlash` option if provided.
   */
  trailingSlash?: "append" | "remove" | undefined;
  autofocus?: Booleanish | undefined;
  disabled?: boolean | undefined;
  form?: string | undefined;
  formaction?: string | undefined;
  formenctype?: string | undefined;
  formmethod?: string | undefined;
  formnovalidate?: Booleanish | undefined;
  formtarget?: string | undefined;
  /**
   * The type of the button when not a link.
   */
  type?: "reset" | "submit" | "button" | undefined;
  download?: any;
  hreflang?: string | undefined;
  media?: string | undefined;
  ping?: string | undefined;
  /**
   * Will only be active if the current route is an exact match.
   */
  exact?: boolean | undefined;
  /**
   * Allows controlling how the current route query sets the link as active.
   */
  exactQuery?: boolean | "partial" | undefined;
  /**
   * Will only be active if the current route hash is an exact match.
   */
  exactHash?: boolean | undefined;
  /**
   * The class to apply when the link is inactive.
   */
  inactiveClass?: string | undefined;
  label?: string | undefined;
  activeColor?: "primary" | "secondary" | "success" | "info" | "warning" | "error" | "neutral" | undefined;
  activeVariant?: "link" | "ghost" | "solid" | "outline" | "soft" | "subtle" | undefined;
  /**
   * Render the button with equal padding on all sides.
   */
  square?: boolean | undefined;
  /**
   * Render the button full width.
   */
  block?: boolean | undefined;
  /**
   * Set loading state automatically based on the `@click` promise state
   */
  loadingAuto?: boolean | undefined;
  /**
   * When `true`, the icon will be displayed on the left side.
   */
  leading?: boolean | undefined;
  /**
   * Display an icon on the left side.
   */
  leadingIcon?: string | object | undefined;
  /**
   * The icon when the `loading` prop is `true`.
   */
  loadingIcon?: string | object | undefined;
}
```

<callout icon="i-simple-icons-mdnwebdocs" target="_blank" to="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/button#attributes">

This component also supports all native `<button>` HTML attributes.

</callout>

### Slots

```ts
/**
 * Slots for the ColorModeButton component
 */
interface ColorModeButtonSlots {
}
```

## Changelog

<component-changelog prefix="color-mode">



</component-changelog>
