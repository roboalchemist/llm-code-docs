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

<warning>

Make sure to wrap your app with the [`App`](/docs/components/app) component which uses our [`Toaster`](https://github.com/nuxt/ui/blob/v4/src/runtime/components/Toaster.vue) component which uses the [`ToastProvider`](https://reka-ui.com/docs/components/toast#provider) component from Reka UI.

</warning>

<tip to="/docs/components/toast">

Learn how to customize the appearance and behavior of toasts in the **Toast** component documentation.

</tip>

## API

`useToast()`

The `useToast` composable provides methods to manage toast notifications globally.

### add()

`add(toast: Partial<Toast>): Toast`

Adds a new toast notification.

#### Parameters

<field-group>
<field name="toast" type="Partial<Toast>" :required="true" required="true">

A partial `Toast` object with the following properties:

<collapsible>
<field-group>
<field name="id" type="string | number">

A unique identifier for the toast. If not provided, a timestamp will be used.

</field>

<field name="open" type="boolean">

Whether the toast is open. Defaults to `true`.

</field>

<field name="..." type="Toast">

Other properties from the `Toast` interface.

</field>
</field-group>
</collapsible>
</field>
</field-group>

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

<field-group>
<field name="id" type="string | number" :required="true" required="true">

The unique identifier of the toast to update.

</field>

<field name="toast" type="Partial<Toast>" :required="true" required="true">

A partial `Toast` object with the properties to update.

</field>
</field-group>

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

<field-group>
<field name="id" type="string | number" :required="true" required="true">

The unique identifier of the toast to remove.

</field>
</field-group>

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

### `toasts`

`toasts: Ref<Toast[]>`

- Type: `Ref<Toast[]>`
- Description: A reactive array containing all current toast notifications.
