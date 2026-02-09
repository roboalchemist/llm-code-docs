# Source: https://ui.nuxt.com/raw/docs/components/dashboard-resize-handle.md

# DashboardResizeHandle

> A handle to resize a sidebar or panel.

## Usage

The DashboardResizeHandle component is used by the [DashboardSidebar](/docs/components/dashboard-sidebar) and [DashboardPanel](/docs/components/dashboard-panel) components.

It is automatically displayed when the `resizable` prop is set, **you don't have to add it manually**.

## Examples

### Within `resize-handle` slot

Even though this component is automatically displayed when the `resizable` prop is set, you can use the `resize-handle` slot of the [DashboardSidebar](/docs/components/dashboard-sidebar) and [DashboardPanel](/docs/components/dashboard-panel) components to customize the handle.

```vue
<template>
  <UDashboardGroup>
    <UDashboardSidebar resizable>
      <template #resize-handle="{ onMouseDown, onTouchStart, onDoubleClick }">
        <UDashboardResizeHandle
          class="after:absolute after:inset-y-0 after:right-0 after:w-px hover:after:bg-(--ui-border-accented) after:transition"
          @mousedown="onMouseDown"
          @touchstart="onTouchStart"
          @dblclick="onDoubleClick"
        />
      </template>
    </UDashboardSidebar>

    <slot />
  </UDashboardGroup>
</template>

```

```vue
<script setup lang="ts">
definePageMeta({
  layout: 'dashboard'
})
</script>

<template>
  <UDashboardPanel resizable>
    <template #resize-handle="{ onMouseDown, onTouchStart, onDoubleClick }">
      <UDashboardResizeHandle
        class="after:absolute after:inset-y-0 after:right-0 after:w-px hover:after:bg-(--ui-border-accented) after:transition"
        @mousedown="onMouseDown"
        @touchstart="onTouchStart"
        @dblclick="onDoubleClick"
      />
    </template>
  </UDashboardPanel>
</template>

```

> [!NOTE]
> In this example, we add an `after` pseudo-element to display a vertical line on hover.

## API

### Props

```ts
/**
 * Props for the DashboardResizeHandle component
 */
interface DashboardResizeHandleProps {
  /**
   * The element or component this component should render as.
   */
  as?: any;
}
```

### Slots

```ts
/**
 * Slots for the DashboardResizeHandle component
 */
interface DashboardResizeHandleSlots {
  default(): any;
}
```

## Theme

```ts [app.config.ts]
export default defineAppConfig({
  ui: {
    dashboardResizeHandle: {
      base: 'hidden lg:block touch-none select-none cursor-ew-resize relative before:absolute before:inset-y-0 before:-left-1.5 before:-right-1.5 before:z-1'
    }
  }
})
```

## Changelog

See the [releases page](https://github.com/nuxt/ui/releases) for the latest changes.
