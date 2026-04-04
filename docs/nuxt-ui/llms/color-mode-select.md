# Source: https://ui.nuxt.com/raw/docs/components/color-mode-select.md

# ColorModeSelect

> A Select to switch between system, dark & light mode.

## Usage

The ColorModeSelect component extends the [SelectMenu](/docs/components/select-menu) component, so you can pass any property such as `color`, `variant`, `size`, etc.

```vue
<template>
  <UColorModeSelect />
</template>
```

## Examples

### With custom icons

**Nuxt:**
Use the app.config.ts to customize the icon with the ui.icons property:
```ts
export default defineAppConfig({
  ui: {
    icons: {
      system: 'i-ph-desktop',
      light: 'i-ph-sun',
      dark: 'i-ph-moon'
    }
  }
})

```

**Vue:**
Use the vite.config.ts to customize the icon with the ui.icons property:
```ts
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

## API

### Props

```ts
/**
 * Props for the ColorModeSelect component
 */
interface ColorModeSelectProps {
  /**
   * The open state of the combobox when it is initially rendered. <br> Use when you do not need to control its open state.
   */
  defaultOpen?: boolean | undefined;
  /**
   * The controlled open state of the Combobox. Can be binded with `v-model:open`.
   */
  open?: boolean | undefined;
  /**
   * The icon displayed to open the menu.
   */
  trailingIcon?: any;
  color?: "primary" | "secondary" | "success" | "info" | "warning" | "error" | "neutral" | undefined;
  /**
   * Highlight the ring color like a focus state.
   */
  highlight?: boolean | undefined;
  ui?: { base?: ClassNameValue; leading?: ClassNameValue; leadingIcon?: ClassNameValue; leadingAvatar?: ClassNameValue; leadingAvatarSize?: ClassNameValue; trailing?: ClassNameValue; trailingIcon?: ClassNameValue; value?: ClassNameValue; placeholder?: ClassNameValue; arrow?: ClassNameValue; content?: ClassNameValue; viewport?: ClassNameValue; group?: ClassNameValue; empty?: ClassNameValue; label?: ClassNameValue; separator?: ClassNameValue; item?: ClassNameValue; itemLeadingIcon?: ClassNameValue; itemLeadingAvatar?: ClassNameValue; itemLeadingAvatarSize?: ClassNameValue; itemLeadingChip?: ClassNameValue; itemLeadingChipSize?: ClassNameValue; itemTrailing?: ClassNameValue; itemTrailingIcon?: ClassNameValue; itemWrapper?: ClassNameValue; itemLabel?: ClassNameValue; itemDescription?: ClassNameValue; input?: ClassNameValue; focusScope?: ClassNameValue; trailingClear?: ClassNameValue; } | undefined;
  /**
   * The name of the field. Submitted with its owning form as part of a name/value pair.
   */
  name?: string | undefined;
  /**
   * When `true`, the icon will be displayed on the right side.
   */
  trailing?: boolean | undefined;
  /**
   * The content of the menu.
   */
  content?: (Omit<ComboboxContentProps, "as" | "asChild" | "forceMount"> & Partial<EmitsToProps<DismissableLayerEmits>>) | undefined;
  /**
   * When `true`, the loading icon will be displayed.
   */
  loading?: boolean | undefined;
  size?: "md" | "xs" | "sm" | "lg" | "xl" | undefined;
  /**
   * Display an avatar on the left side.
   */
  avatar?: AvatarProps | undefined;
  variant?: "ghost" | "outline" | "soft" | "subtle" | "none" | undefined;
  autofocus?: boolean | undefined;
  /**
   * When `true`, prevents the user from interacting with listbox
   */
  disabled?: boolean | undefined;
  form?: string | undefined;
  formaction?: string | undefined;
  formenctype?: string | undefined;
  formmethod?: string | undefined;
  formnovalidate?: Booleanish | undefined;
  formtarget?: string | undefined;
  /**
   * When `true`, the icon will be displayed on the left side.
   */
  leading?: boolean | undefined;
  /**
   * Display an icon on the left side.
   */
  leadingIcon?: any;
  /**
   * The icon when the `loading` prop is `true`.
   */
  loadingIcon?: any;
  /**
   * Whether to reset the searchTerm when the Combobox input blurred
   */
  resetSearchTermOnBlur?: boolean | undefined;
  /**
   * Whether to reset the searchTerm when the Combobox value is selected
   */
  resetSearchTermOnSelect?: boolean | undefined;
  /**
   * When `true` the `modelValue` will be reset to `null` (or `[]` if `multiple`)
   */
  resetModelValueOnClear?: boolean | undefined;
  /**
   * When `true`, hover over item will trigger highlight
   */
  highlightOnHover?: boolean | undefined;
  /**
   * Use this to compare objects by a particular field, or pass your own comparison function for complete control over how objects are compared.
   */
  by?: string | ((a: SelectMenuItem[], b: SelectMenuItem[]) => boolean) | undefined;
  /**
   * The value of the SelectMenu when initially rendered. Use when you do not need to control the state of the SelectMenu.
   */
  defaultValue?: SelectMenuItem | undefined;
  /**
   * Whether multiple options can be selected or not.
   */
  multiple?: false | undefined;
  required?: boolean | undefined;
  id?: string | undefined;
  /**
   * The placeholder text when the select is empty.
   */
  placeholder?: string | undefined;
  /**
   * Whether to display the search input or not.
   * Can be an object to pass additional props to the input.
   * `{ placeholder: 'Search...', variant: 'none' }`{lang="ts-type"}
   * @default "false"
   */
  searchInput?: boolean | InputProps<AcceptableValue> | undefined;
  /**
   * The icon displayed when an item is selected.
   */
  selectedIcon?: any;
  /**
   * Display a clear button to reset the model value.
   * Can be an object to pass additional props to the Button.
   */
  clear?: boolean | Partial<Omit<ButtonProps, LinkPropsKeys>> | undefined;
  /**
   * The icon displayed in the clear button.
   */
  clearIcon?: any;
  /**
   * Display an arrow alongside the menu.
   */
  arrow?: boolean | Omit<ComboboxArrowProps, "as" | "asChild"> | undefined;
  /**
   * Render the menu in a portal.
   */
  portal?: string | boolean | HTMLElement | undefined;
  /**
   * Enable virtualization for large lists.
   * Note: when enabled, all groups are flattened into a single list due to a limitation of Reka UI (https://github.com/unovue/reka-ui/issues/1885).
   */
  virtualize?: boolean | { overscan?: number | undefined; estimateSize?: number | ((index: number) => number) | undefined; } | undefined;
  /**
   * When `items` is an array of objects, select the field to use as the value instead of the object itself.
   */
  valueKey?: undefined;
  /**
   * When `items` is an array of objects, select the field to use as the label.
   */
  labelKey?: GetItemKeys<SelectMenuItem[]> | undefined;
  /**
   * When `items` is an array of objects, select the field to use as the description.
   */
  descriptionKey?: GetItemKeys<SelectMenuItem[]> | undefined;
  modelModifiers?: Omit<ModelModifiers<SelectMenuItem>, "lazy"> | undefined;
  /**
   * Determines if custom user input that does not exist in options can be added.
   */
  createItem?: boolean | "always" | { position?: "top" | "bottom" | undefined; when?: "empty" | "always" | undefined; } | undefined;
  /**
   * Fields to filter items by.
   */
  filterFields?: string[] | undefined;
  /**
   * When `true`, disable the default filters, useful for custom filtering (useAsyncData, useFetch, etc.).
   */
  ignoreFilter?: boolean | undefined;
  autofocusDelay?: number | undefined;
}
```

## Changelog

See the [releases page](https://github.com/nuxt/ui/releases) for the latest changes.
