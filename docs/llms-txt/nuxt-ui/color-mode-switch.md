# Source: https://ui.nuxt.com/raw/docs/components/color-mode-switch.md

# ColorModeSwitch

> A switch to toggle between light and dark mode.

## Usage

The ColorModeSwitch component extends the [Switch](/docs/components/switch) component, so you can pass any property such as `color`, `size`, etc.

```vue
<template>
  <UColorModeSwitch />
</template>
```

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

## API

### Props

```ts
/**
 * Props for the ColorModeSwitch component
 */
interface ColorModeSwitchProps {
  /**
   * The element or component this component should render as.
   */
  as?: any;
  color?: "primary" | "secondary" | "success" | "info" | "warning" | "error" | "neutral" | undefined;
  ui?: { root?: ClassNameValue; base?: ClassNameValue; container?: ClassNameValue; thumb?: ClassNameValue; icon?: ClassNameValue; wrapper?: ClassNameValue; label?: ClassNameValue; description?: ClassNameValue; } | undefined;
  /**
   * The name of the field. Submitted with its owning form as part of a name/value pair.
   */
  name?: string | undefined;
  /**
   * When `true`, the loading icon will be displayed.
   */
  loading?: boolean | undefined;
  size?: "md" | "xs" | "sm" | "lg" | "xl" | undefined;
  autofocus?: Booleanish | undefined;
  /**
   * When `true`, prevents the user from interacting with the switch.
   */
  disabled?: boolean | undefined;
  form?: string | undefined;
  formaction?: string | undefined;
  formenctype?: string | undefined;
  formmethod?: string | undefined;
  formnovalidate?: Booleanish | undefined;
  formtarget?: string | undefined;
  label?: string | undefined;
  /**
   * The icon when the `loading` prop is `true`.
   */
  loadingIcon?: string | object | undefined;
  /**
   * The state of the switch when it is initially rendered. Use when you do not need to control its state.
   */
  defaultValue?: boolean | undefined;
  /**
   * When `true`, indicates that the user must set the value before the owning form can be submitted.
   */
  required?: boolean | undefined;
  id?: string | undefined;
  /**
   * The value given as data when submitted with a `name`.
   */
  value?: string | undefined;
  description?: string | undefined;
}
```

## Changelog

<component-changelog prefix="color-mode">



</component-changelog>
