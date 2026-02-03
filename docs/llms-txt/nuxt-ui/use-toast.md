# Source: https://ui.nuxt.com/raw/docs/composables/use-toast.md

# useToast

> A composable to display toast notifications in your app.

## Usage

Use the auto-imported `useToast` composable to display [Toast](/docs/components/toast) notifications.

```vue
<script setup lang="ts">
const toast = useToast()
</script>
```

- The `useToast` composable uses Nuxt's `useState` to manage the toast state, ensuring reactivity across your application.
- A maximum of 5 toasts are displayed at a time. When adding a new toast that would exceed this limit, the oldest toast is automatically removed.
- When removing a toast, there's a 200ms delay before it's actually removed from the state, allowing for exit animations.

> [!WARNING]
> Make sure to wrap your app with the [`App`](/docs/components/app) component which uses our [`Toaster`](https://github.com/nuxt/ui/blob/v4/src/runtime/components/Toaster.vue) component which uses the [`ToastProvider`](https://reka-ui.com/docs/components/toast#provider) component from Reka UI.

> [!TIP]
> See: /docs/components/toast
> Learn how to customize the appearance and behavior of toasts in the Toast component documentation.

## API

`useToast()`

The `useToast` composable provides methods to manage toast notifications globally.

### add()

`add(toast: Partial<Toast>): Toast`

Adds a new toast notification.

#### Parameters

A partial  object with the following properties:

A unique identifier for the toast. If not provided, a timestamp will be used.

Whether the toast is open. Defaults to .

The title displayed in the toast.

The description displayed in the toast.

The icon displayed in the toast.

The avatar displayed in the toast. See .

The color of the toast.

The orientation between the content and the actions. Defaults to .

Customize or hide the close button (with  value). Defaults to .

The icon displayed in the close button.

The actions displayed in the toast. See .

Customize or hide the progress bar (with  value). Defaults to .

The duration in milliseconds before the toast auto-closes. Can also be set globally on the  component.

A callback function invoked when the toast is clicked.

A callback function invoked when the toast open state changes. Useful to perform an action when the toast closes (expired or dismissed).

**Returns:** The complete `Toast` object that was added.

```vue
<script setup lang="ts">
const toast = useToast()

function showToast() {
  toast.add({
    title: 'Success',
    description: 'Your action was completed successfully.',
    color: 'success'
  })
}
</script>
```

### update()

`update(id: string | number, toast: Partial<Toast>): void`

Updates an existing toast notification.

#### Parameters

The unique identifier of the toast to update.

A partial  object with the properties to update.

```vue
<script setup lang="ts">
const toast = useToast()

function updateToast(id: string | number) {
  toast.update(id, {
    title: 'Updated Toast',
    description: 'This toast has been updated.'
  })
}
</script>
```

### remove()

`remove(id: string | number): void`

Removes a toast notification.

#### Parameters

The unique identifier of the toast to remove.

```vue
<script setup lang="ts">
const toast = useToast()

function removeToast(id: string | number) {
  toast.remove(id)
}
</script>
```

### clear()

`clear(): void`

Removes all toast notifications.

```vue
<script setup lang="ts">
const toast = useToast()

function clearAllToasts() {
  toast.clear()
}
</script>
```

### toasts

`toasts: Ref<Toast[]>`

A reactive array containing all current toast notifications.

```vue
<script setup lang="ts">
const { toasts } = useToast()
</script>

<template>
  <div>
    <pre>{{ toasts }}</pre>
  </div>
</template>
```
