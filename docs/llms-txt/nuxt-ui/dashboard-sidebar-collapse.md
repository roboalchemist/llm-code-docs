# Source: https://ui.nuxt.com/raw/docs/components/dashboard-sidebar-collapse.md

# DashboardSidebarCollapse

> A Button to collapse the sidebar on desktop.

## Usage

The DashboardSidebarCollapse component is used to collapse/expand the [DashboardSidebar](/docs/components/dashboard-sidebar) component **when its collapsible prop is set**.

```vue
<template>
  <UDashboardSidebarCollapse />
</template>
```

It extends the [Button](/docs/components/button) component, so you can pass any property such as `color`, `variant`, `size`, etc.

```vue
<template>
  <UDashboardSidebarCollapse variant="subtle" />
</template>
```

<note>

The button defaults to `color="neutral"` and `variant="ghost"`.

</note>

## Examples

### Within `header` slot

You can put this component in the `header` slot of the [DashboardSidebar](/docs/components/dashboard-sidebar) component and use the `collapsed` prop to hide the left part of the header for example:

```vue [layouts/dashboard.vue]
<template>
  <UDashboardGroup>
    <UDashboardSidebar collapsible>
      <template #header="{ collapsed }">
        <Logo v-if="!collapsed" />

        <UDashboardSidebarCollapse variant="subtle" />
      </template>
    </UDashboardSidebar>

    <slot />
  </UDashboardGroup>
</template>
```

### Within `leading` slot

You can put this component in the `leading` slot of the [DashboardNavbar](/docs/components/dashboard-navbar) component to display it before the title for example:

```vue [pages/index.vue]
<script setup lang="ts">
definePageMeta({
  layout: 'dashboard'
})
</script>

<template>
  <UDashboardPanel>
    <template #header>
      <UDashboardNavbar title="Home">
        <template #leading>
          <UDashboardSidebarCollapse variant="subtle" />
        </template>
      </UDashboardNavbar>
    </template>
  </UDashboardPanel>
</template>
```

## API

### Props

```ts
/**
 * Props for the DashboardSidebarCollapse component
 */
interface DashboardSidebarCollapseProps {
  /**
   * @default "\"neutral\""
   */
  color?: "error" | "neutral" | "primary" | "secondary" | "success" | "info" | "warning" | undefined;
  /**
   * @default "\"ghost\""
   */
  variant?: "link" | "ghost" | "solid" | "outline" | "soft" | "subtle" | undefined;
  /**
   * The side of the sidebar to collapse.
   * @default "\"left\""
   */
  side?: "left" | "right" | undefined;
  ui?: { base?: ClassNameValue; label?: ClassNameValue; leadingIcon?: ClassNameValue; leadingAvatar?: ClassNameValue; leadingAvatarSize?: ClassNameValue; trailingIcon?: ClassNameValue; } | undefined;
  /**
   * The element or component this component should render as when not a link.
   */
  as?: any;
  name?: string | undefined;
  form?: string | undefined;
  label?: string | undefined;
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
  ariaCurrentValue?: "time" | "page" | "step" | "location" | "date" | "true" | "false" | undefined;
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
  referrerpolicy?: HTMLAttributeReferrerPolicy | undefined;
  onClick?: ((event: MouseEvent) => void | Promise<void>) | ((event: MouseEvent) => void | Promise<void>)[] | undefined;
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
  activeVariant?: "link" | "ghost" | "solid" | "outline" | "soft" | "subtle" | undefined;
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
   * Display an icon based on the `leading` and `trailing` props.
   */
  icon?: string | object | undefined;
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

## Theme

```ts [app.config.ts]
export default defineAppConfig({
  ui: {
    dashboardSidebarCollapse: {
      base: 'hidden lg:flex',
      variants: {
        side: {
          left: '',
          right: ''
        }
      }
    }
  }
})
```

## Changelog

<component-changelog>



</component-changelog>
