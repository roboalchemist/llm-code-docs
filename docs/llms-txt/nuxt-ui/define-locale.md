# Source: https://ui.nuxt.com/raw/docs/composables/define-locale.md

# defineLocale

> A utility to create a custom locale for your app.

## Usage

Use the `defineLocale` utility to create a custom locale with your own translations.

```vue
<script setup lang="ts">
import type { Messages } from '@nuxt/ui'

const locale = defineLocale<Messages>({
  name: 'My custom locale',
  code: 'en',
  dir: 'ltr',
  messages: {
    // implement pairs
  }
})
</script>

<template>
  <UApp :locale="locale">
    <NuxtPage />
  </UApp>
</template>
```

> [!TIP]
> See: /docs/getting-started/integrations/i18n
> Learn more about internationalization in the i18n integration documentation.

## API

`defineLocale<M>(options: DefineLocaleOptions<M>): Locale<M>`

Creates a new locale object with the provided options.

#### Parameters

The locale configuration object with the following properties:

The display name of the locale (e.g., , ).

The ISO code of the locale (e.g., , , ).

The text direction of the locale. Defaults to .

The translation messages object. Use the  type from  for type safety.

**Returns:** A `Locale<M>` object that can be passed to the `locale` prop of the [App](/docs/components/app) component.

## Example

Here's a complete example of creating a custom locale:

```vue
<script setup lang="ts">
import type { Messages } from '@nuxt/ui'

const locale = defineLocale<Messages>({
  name: 'Español',
  code: 'es',
  dir: 'ltr',
  messages: {
    alert: {
      close: 'Cerrar'
    },
    modal: {
      close: 'Cerrar'
    },
    commandPalette: {
      back: 'Atrás',
      close: 'Cerrar',
      noData: 'Sin datos',
      noMatch: 'Sin resultados',
      placeholder: 'Escribe un comando o busca…'
    }
    // ... other component messages
  }
})
</script>

<template>
  <UApp :locale="locale">
    <NuxtPage />
  </UApp>
</template>
```

> [!NOTE]
> You can look at the [built-in locales](https://github.com/nuxt/ui/tree/v4/src/runtime/locale) for reference on how to structure the messages object.
