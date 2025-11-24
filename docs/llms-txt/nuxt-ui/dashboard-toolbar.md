# Source: https://ui.nuxt.com/raw/docs/components/dashboard-toolbar.md

# DashboardToolbar

> A toolbar to display under the navbar in a dashboard.

## Usage

The DashboardToolbar component is used to display a toolbar under the [DashboardNavbar](/docs/components/dashboard-navbar) component.

Use it inside the `header` slot of the [DashboardPanel](/docs/components/dashboard-panel) component:

```vue [pages/index.vue]
<script setup lang="ts">
definePageMeta({
  layout: 'dashboard'
})
</script>

<template>
  <UDashboardPanel>
    <template #header>
      <UDashboardNavbar />

      <UDashboardToolbar />
    </template>
  </UDashboardPanel>
</template>
```

Use the `left`, `default` and `right` slots to customize the toolbar.

```vue [DashboardToolbarExample.vue]
<script setup lang="ts">
import type { NavigationMenuItem } from '@nuxt/ui'

const items: NavigationMenuItem[][] = [[{
  label: 'General',
  icon: 'i-lucide-user',
  active: true
}, {
  label: 'Members',
  icon: 'i-lucide-users'
}, {
  label: 'Notifications',
  icon: 'i-lucide-bell'
}], [{
  label: 'Documentation',
  icon: 'i-lucide-book-open',
  to: 'https://ui.nuxt.com/docs',
  target: '_blank'
}, {
  label: 'Help & Feedback',
  icon: 'i-lucide-help-circle',
  to: 'https://github.com/nuxt/ui/issues',
  target: '_blank'
}]]
</script>

<template>
  <UDashboardToolbar>
    <UNavigationMenu :items="items" highlight class="flex-1" />
  </UDashboardToolbar>
</template>
```

<note>

In this example, we use the [NavigationMenu](/docs/components/navigation-menu) component to render some links.

</note>

## API

### Props

```ts
/**
 * Props for the DashboardToolbar component
 */
interface DashboardToolbarProps {
  /**
   * The element or component this component should render as.
   */
  as?: any;
  ui?: { root?: ClassNameValue; left?: ClassNameValue; right?: ClassNameValue; } | undefined;
}
```

### Slots

```ts
/**
 * Slots for the DashboardToolbar component
 */
interface DashboardToolbarSlots {
  default(): any;
  left(): any;
  right(): any;
}
```

## Theme

```ts [app.config.ts]
export default defineAppConfig({
  ui: {
    dashboardToolbar: {
      slots: {
        root: 'shrink-0 flex items-center justify-between border-b border-default px-4 sm:px-6 gap-1.5 overflow-x-auto min-h-[49px]',
        left: 'flex items-center gap-1.5',
        right: 'flex items-center gap-1.5'
      }
    }
  }
})
```

## Changelog

<component-changelog>



</component-changelog>
