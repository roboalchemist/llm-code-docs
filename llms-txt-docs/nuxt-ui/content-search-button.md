# Source: https://ui.nuxt.com/raw/docs/components/content-search-button.md

# ContentSearchButton

> A pre-styled Button to open the ContentSearch modal.

<warning to="/docs/getting-started/integrations/content">

This component is only available when the `@nuxt/content` module is installed.

</warning>

## Usage

The ContentSearchButton component is used to open the [ContentSearch](/docs/components/content-search) modal.

```vue
<template>
  <UContentSearchButton />
</template>
```

It extends the [Button](/docs/components/button) component, so you can pass any property such as `color`, `variant`, `size`, etc.

```vue
<template>
  <UContentSearchButton variant="subtle" />
</template>
```

<note to="#collapsed">

The button defaults to `color="neutral"` and `variant="outline"` when not collapsed, `variant="ghost"` when collapsed.

</note>

### Collapsed

Use the `collapsed` prop to show the button's label and [kbds](#kbds). Defaults to `true`.

```vue
<template>
  <UContentSearchButton :collapsed="false" />
</template>
```

### Kbds

Use the `kbds` prop to display keyboard keys in the button. Defaults to `['meta', 'K']` to match the default shortcut of the [ContentSearch](/docs/components/content-search#shortcut) component.

```vue
<template>
  <UContentSearchButton :collapsed="false" />
</template>
```

## API

### Props

```ts
/**
 * Props for the ContentSearchButton component
 */
interface ContentSearchButtonProps {
  /**
   * The icon displayed in the button.
   */
  icon?: string | object | undefined;
  /**
   * The label displayed in the button.
   */
  label?: string | undefined;
  /**
   * The color of the button.
   * @default "\"neutral\""
   */
  color?: "error" | "neutral" | "primary" | "secondary" | "success" | "info" | "warning" | undefined;
  /**
   * The variant of the button.
   * Defaults to 'outline' when not collapsed, 'ghost' when collapsed.
   */
  variant?: "solid" | "outline" | "soft" | "subtle" | "ghost" | "link" | undefined;
  /**
   * Whether the button is collapsed.
   * @default "true"
   */
  collapsed?: boolean | undefined;
  /**
   * Display a tooltip on the button when is collapsed with the button label.
   * This has priority over the global `tooltip` prop.
   * @default "false"
   */
  tooltip?: boolean | TooltipProps | undefined;
  /**
   * The keyboard keys to display in the button.
   * `{ variant: 'subtle' }`{lang="ts-type"}
   * @default "[\"meta\", \"k\"]"
   */
  kbds?: (string | undefined)[] | KbdProps[] | undefined;
  ui?: ({ base?: ClassNameValue; trailing?: ClassNameValue; } & { base?: ClassNameValue; label?: ClassNameValue; leadingIcon?: ClassNameValue; leadingAvatar?: ClassNameValue; leadingAvatarSize?: ClassNameValue; trailingIcon?: ClassNameValue; }) | undefined;
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
  name?: string | undefined;
  /**
   * The type of the button when not a link.
   */
  type?: "reset" | "submit" | "button" | undefined;
  download?: any;
  hreflang?: string | undefined;
  media?: string | undefined;
  ping?: string | undefined;
  referrerpolicy?: HTMLAttributeReferrerPolicy | undefined;
  onClick?: ((event: MouseEvent) => void | Promise<void>) | ((event: MouseEvent) => void | Promise<void>)[] | undefined;
  /**
   * The element or component this component should render as when not a link.
   */
  as?: any;
  /**
   * Force the link to be active independent of the current route.
   */
  active?: boolean | undefined;
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
  activeColor?: "error" | "neutral" | "primary" | "secondary" | "success" | "info" | "warning" | undefined;
  activeVariant?: "solid" | "outline" | "soft" | "subtle" | "ghost" | "link" | undefined;
  size?: "xs" | "sm" | "md" | "lg" | "xl" | undefined;
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
   * Display an avatar on the left side.
   */
  avatar?: AvatarProps | undefined;
  /**
   * When `true`, the icon will be displayed on the left side.
   */
  leading?: boolean | undefined;
  /**
   * Display an icon on the left side.
   */
  leadingIcon?: string | object | undefined;
  /**
   * When `true`, the icon will be displayed on the right side.
   */
  trailing?: boolean | undefined;
  /**
   * Display an icon on the right side.
   */
  trailingIcon?: string | object | undefined;
  /**
   * When `true`, the loading icon will be displayed.
   */
  loading?: boolean | undefined;
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
 * Slots for the ContentSearchButton component
 */
interface ContentSearchButtonSlots {
  leading(): any;
  default(): any;
  trailing(): any;
}
```

## Theme

```ts [app.config.ts]
export default defineAppConfig({
  ui: {
    contentSearchButton: {
      slots: {
        base: '',
        trailing: 'hidden lg:flex items-center gap-0.5 ms-auto'
      }
    }
  }
})
```

## Changelog

<component-changelog prefix="content">



</component-changelog>
