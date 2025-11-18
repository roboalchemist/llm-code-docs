# Source: https://ui.nuxt.com/raw/docs/components/error.md

# Error

> A pre-built error component with NuxtError support.

## Usage

The Error component works together with the [Header](/docs/components/header) component to create a full-height layout that extends to the viewport's available height.

<tip to="/docs/getting-started/theme/css-variables#header">

The Error component uses the `--ui-header-height` CSS variable to position itself correctly below the [Header](/docs/components/header).

</tip>

### Error

Use the `error` prop to display an error message.

<note target="_blank" to="https://nuxt.com/docs/guide/directory-structure/error">

In most cases, you will receive the `error` prop in your `error.vue` file.

</note>

```vue
<template>
  <UError />
</template>
```

### Clear

Use the `clear` prop to customize or hide the clear button (with `false` value).

You can pass any property from the [Button](/docs/components/button) component to customize it.

```vue
<template>
  <UError />
</template>
```

### Redirect

Use the `redirect` prop to redirect the user to a different page when the clear button is clicked. Defaults to `/`.

```vue
<template>
  <UError redirect="/docs/getting-started" />
</template>
```

## Examples

### Within `error.vue`

Use the Error component in your `error.vue`:

```vue [error.vue]
<script setup lang="ts">
import type { NuxtError } from '#app'

const props = defineProps<{
  error: NuxtError
}>()
</script>

<template>
  <UApp>
    <UHeader />

    <UError :error="error" />

    <UFooter />
  </UApp>
</template>
```

<tip>

You might want to replicate the code of your `app.vue` inside your `error.vue` file to have the same layout and features, here is an example: [https://github.com/nuxt/ui/blob/v4/docs/app/error.vue](https://github.com/nuxt/ui/blob/v4/docs/app/error.vue)

</tip>

<note>

You can read more about how to handle errors in the [Nuxt documentation](https://nuxt.com/docs/getting-started/error-handling#error-page), but when using `nuxt generate` it is recommended to add `fatal: true` inside your `createError` call to make sure the error page is displayed:

```vue [pages/[...slug].vue]
<script setup lang="ts">
const route = useRoute()

const { data: page } = await useAsyncData(route.path, () => {
  return queryCollection('docs').path(route.path).first()
})
if (!page.value) {
  throw createError({ statusCode: 404, statusMessage: 'Page not found', fatal: true })
}
</script>
```

</note>

## API

### Props

```ts
/**
 * Props for the Error component
 */
interface ErrorProps {
  /**
   * The element or component this component should render as.
   */
  as?: any;
  error?: Partial<NuxtError<unknown> & { message: string; }> | undefined;
  /**
   * The URL to redirect to when the error is cleared.
   * @default "\"/\""
   */
  redirect?: string | undefined;
  /**
   * Display a button to clear the error in the links slot.
   * `{ size: 'lg', color: 'primary', variant: 'solid', label: 'Back to home' }`{lang="ts-type"}
   * @default "true"
   */
  clear?: boolean | Partial<ButtonProps> | undefined;
  ui?: { root?: ClassNameValue; statusCode?: ClassNameValue; statusMessage?: ClassNameValue; message?: ClassNameValue; links?: ClassNameValue; } | undefined;
}
```

### Slots

```ts
/**
 * Slots for the Error component
 */
interface ErrorSlots {
  default(): any;
  statusCode(): any;
  statusMessage(): any;
  message(): any;
  links(): any;
}
```

## Theme

```ts [app.config.ts]
export default defineAppConfig({
  ui: {
    error: {
      slots: {
        root: 'min-h-[calc(100vh-var(--ui-header-height))] flex flex-col items-center justify-center text-center',
        statusCode: 'text-base font-semibold text-primary',
        statusMessage: 'mt-2 text-4xl sm:text-5xl font-bold text-highlighted text-balance',
        message: 'mt-4 text-lg text-muted text-balance',
        links: 'mt-8 flex items-center justify-center gap-6'
      }
    }
  }
})
```

## Changelog

<component-changelog>



</component-changelog>
