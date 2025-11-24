# Source: https://ui.nuxt.com/raw/docs/components/input-time.md

# InputTime

> An input for selecting a time.

## Usage

Use the `v-model` directive to control the selected date.

```vue
<template>
  <UInputTime />
</template>
```

Use the `default-value` prop to set the initial value when you do not need to control its state.

```vue
<template>
  <UInputTime />
</template>
```

<note>

This component relies on the [`@internationalized/date`](https://react-spectrum.adobe.com/internationalized/date/index.html) package which provides objects and functions for representing and manipulating dates and times in a locale-aware manner.

</note>

### Hour Cycle

Use the `hour-cycle` prop to change the hour cycle of the InputTime. Defaults to `12`.

```vue
<template>
  <UInputTime :hour-cycle="24" />
</template>
```

### Color

Use the `color` prop to change the color of the InputTime.

```vue
<template>
  <UInputTime color="neutral" highlight />
</template>
```

<note>

The `highlight` prop is used here to show the focus state. It's used internally when a validation error occurs.

</note>

### Variant

Use the `variant` prop to change the variant of the InputTime.

```vue
<template>
  <UInputTime variant="subtle" />
</template>
```

### Size

Use the `size` prop to change the size of the InputTime.

```vue
<template>
  <UInputTime size="xl" />
</template>
```

### Icon

Use the `icon` prop to show an [Icon](/docs/components/icon) inside the InputTime.

```vue
<template>
  <UInputTime icon="i-lucide-clock" />
</template>
```

<note>

Use the `leading` and `trailing` props to set the icon position or the `leading-icon` and `trailing-icon` props to set a different icon for each position.

</note>

### Avatar

Use the `avatar` prop to show an [Avatar](/docs/components/avatar) inside the InputTime.

```vue
<template>
  <UInputTime size="md" variant="outline" />
</template>
```

### Disabled

Use the `disabled` prop to disable the InputTime.

```vue
<template>
  <UInputTime disabled />
</template>
```

## Examples

### Within a FormField

You can use the InputTime within a [FormField](/docs/components/form-field) component to display a label, help text, required indicator, etc.

```vue [InputTimeFormFieldExample.vue]
<script setup lang="ts">
import { Time } from '@internationalized/date'

const time = shallowRef(new Time(12, 30, 0))
</script>

<template>
  <UFormField label="Time" help="Specify the time" required>
    <UInputTime v-model="time" />
  </UFormField>
</template>
```

## API

### Props

```ts
/**
 * Props for the InputTime component
 */
interface InputTimeProps {
  /**
   * The element or component this component should render as.
   */
  as?: any;
  color?: "error" | "primary" | "secondary" | "success" | "info" | "warning" | "neutral" | undefined;
  variant?: "outline" | "soft" | "subtle" | "ghost" | "none" | undefined;
  size?: "xs" | "sm" | "md" | "lg" | "xl" | undefined;
  /**
   * Highlight the ring color like a focus state.
   */
  highlight?: boolean | undefined;
  autofocus?: boolean | undefined;
  /**
   * @default "0"
   */
  autofocusDelay?: number | undefined;
  ui?: { base?: ClassNameValue; leading?: ClassNameValue; leadingIcon?: ClassNameValue; leadingAvatar?: ClassNameValue; leadingAvatarSize?: ClassNameValue; trailing?: ClassNameValue; trailingIcon?: ClassNameValue; segment?: ClassNameValue; } | undefined;
  /**
   * The default value for the calendar
   */
  defaultValue?: TimeValue | undefined;
  /**
   * The default placeholder date
   */
  defaultPlaceholder?: TimeValue | undefined;
  /**
   * The placeholder date, which is used to determine what time to display when no time is selected. This updates as the user navigates the field
   */
  placeholder?: TimeValue | undefined;
  /**
   * The controlled checked state of the field. Can be bound as `v-model`.
   */
  modelValue?: TimeValue | null | undefined;
  /**
   * The hour cycle used for formatting times. Defaults to the local preference
   */
  hourCycle?: HourCycle;
  /**
   * The stepping interval for the time fields. Defaults to `1`.
   */
  step?: DateStep | undefined;
  /**
   * The granularity to use for formatting times. Defaults to minute if a Time is provided, otherwise defaults to minute. The field will render segments for each part of the date up to and including the specified granularity
   */
  granularity?: "hour" | "minute" | "second" | undefined;
  /**
   * Whether or not to hide the time zone segment of the field
   */
  hideTimeZone?: boolean | undefined;
  /**
   * The maximum date that can be selected
   */
  maxValue?: TimeValue | undefined;
  /**
   * The minimum date that can be selected
   */
  minValue?: TimeValue | undefined;
  /**
   * Whether or not the time field is disabled
   */
  disabled?: boolean | undefined;
  /**
   * Whether or not the time field is readonly
   */
  readonly?: boolean | undefined;
  /**
   * Id of the element
   */
  id?: string | undefined;
  /**
   * The name of the field. Submitted with its owning form as part of a name/value pair.
   */
  name?: string | undefined;
  /**
   * When `true`, indicates that the user must set the value before the owning form can be submitted.
   */
  required?: boolean | undefined;
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

### Slots

```ts
/**
 * Slots for the InputTime component
 */
interface InputTimeSlots {
  leading(): any;
  default(): any;
  trailing(): any;
}
```

### Emits

```ts
/**
 * Emitted events for the InputTime component
 */
interface InputTimeEmits {
  blur: (payload: [event: FocusEvent]) => void;
  change: (payload: [event: Event]) => void;
  focus: (payload: [event: FocusEvent]) => void;
  update:modelValue: (payload: [date: TimeValue | undefined]) => void;
  update:placeholder: (payload: [date: TimeValue]) => void;
}
```

## Theme

```ts [app.config.ts]
export default defineAppConfig({
  ui: {
    inputTime: {
      slots: {
        base: [
          'group relative inline-flex items-center rounded-md select-none',
          'transition-colors'
        ],
        leading: 'absolute inset-y-0 start-0 flex items-center',
        leadingIcon: 'shrink-0 text-dimmed',
        leadingAvatar: 'shrink-0',
        leadingAvatarSize: '',
        trailing: 'absolute inset-y-0 end-0 flex items-center',
        trailingIcon: 'shrink-0 text-dimmed',
        segment: [
          'rounded text-center outline-hidden data-placeholder:text-dimmed data-[segment=literal]:text-muted data-invalid:text-error data-disabled:cursor-not-allowed data-disabled:opacity-75',
          'transition-colors'
        ]
      },
      variants: {
        fieldGroup: {
          horizontal: {
            root: 'group has-focus-visible:z-[1]',
            base: 'group-not-only:group-first:rounded-e-none group-not-only:group-last:rounded-s-none group-not-last:group-not-first:rounded-none'
          },
          vertical: {
            root: 'group has-focus-visible:z-[1]',
            base: 'group-not-only:group-first:rounded-b-none group-not-only:group-last:rounded-t-none group-not-last:group-not-first:rounded-none'
          }
        },
        size: {
          xs: {
            base: [
              'px-2 py-1 text-xs gap-1',
              'gap-0.25'
            ],
            leading: 'ps-2',
            trailing: 'pe-2',
            leadingIcon: 'size-4',
            leadingAvatarSize: '3xs',
            trailingIcon: 'size-4',
            segment: 'not-data-[segment=literal]:w-6'
          },
          sm: {
            base: [
              'px-2.5 py-1.5 text-xs gap-1.5',
              'gap-0.5'
            ],
            leading: 'ps-2.5',
            trailing: 'pe-2.5',
            leadingIcon: 'size-4',
            leadingAvatarSize: '3xs',
            trailingIcon: 'size-4',
            segment: 'not-data-[segment=literal]:w-6'
          },
          md: {
            base: [
              'px-2.5 py-1.5 text-sm gap-1.5',
              'gap-0.5'
            ],
            leading: 'ps-2.5',
            trailing: 'pe-2.5',
            leadingIcon: 'size-5',
            leadingAvatarSize: '2xs',
            trailingIcon: 'size-5',
            segment: 'not-data-[segment=literal]:w-7'
          },
          lg: {
            base: [
              'px-3 py-2 text-sm gap-2',
              'gap-0.75'
            ],
            leading: 'ps-3',
            trailing: 'pe-3',
            leadingIcon: 'size-5',
            leadingAvatarSize: '2xs',
            trailingIcon: 'size-5',
            segment: 'not-data-[segment=literal]:w-7'
          },
          xl: {
            base: [
              'px-3 py-2 text-base gap-2',
              'gap-0.75'
            ],
            leading: 'ps-3',
            trailing: 'pe-3',
            leadingIcon: 'size-6',
            leadingAvatarSize: 'xs',
            trailingIcon: 'size-6',
            segment: 'not-data-[segment=literal]:w-8'
          }
        },
        variant: {
          outline: 'text-highlighted bg-default ring ring-inset ring-accented',
          soft: 'text-highlighted bg-elevated/50 hover:bg-elevated focus:bg-elevated disabled:bg-elevated/50',
          subtle: 'text-highlighted bg-elevated ring ring-inset ring-accented',
          ghost: 'text-highlighted bg-transparent hover:bg-elevated focus:bg-elevated disabled:bg-transparent dark:disabled:bg-transparent',
          none: 'text-highlighted bg-transparent'
        },
        color: {
          primary: '',
          secondary: '',
          success: '',
          info: '',
          warning: '',
          error: '',
          neutral: ''
        },
        leading: {
          true: ''
        },
        trailing: {
          true: ''
        },
        loading: {
          true: ''
        },
        highlight: {
          true: ''
        },
        type: {
          file: 'file:me-1.5 file:font-medium file:text-muted file:outline-none'
        }
      },
      compoundVariants: [
        {
          variant: 'outline',
          class: {
            segment: 'focus:bg-elevated'
          }
        },
        {
          variant: 'soft',
          class: {
            segment: 'focus:bg-accented/50 group-hover:focus:bg-accented'
          }
        },
        {
          variant: 'subtle',
          class: {
            segment: 'focus:bg-accented'
          }
        },
        {
          variant: 'ghost',
          class: {
            segment: 'focus:bg-elevated group-hover:focus:bg-accented'
          }
        },
        {
          variant: 'none',
          class: {
            segment: 'focus:bg-elevated'
          }
        },
        {
          color: 'primary',
          variant: [
            'outline',
            'subtle'
          ],
          class: 'focus-visible:ring-2 focus-visible:ring-inset focus-visible:ring-primary'
        },
        {
          color: 'secondary',
          variant: [
            'outline',
            'subtle'
          ],
          class: 'focus-visible:ring-2 focus-visible:ring-inset focus-visible:ring-secondary'
        },
        {
          color: 'success',
          variant: [
            'outline',
            'subtle'
          ],
          class: 'focus-visible:ring-2 focus-visible:ring-inset focus-visible:ring-success'
        },
        {
          color: 'info',
          variant: [
            'outline',
            'subtle'
          ],
          class: 'focus-visible:ring-2 focus-visible:ring-inset focus-visible:ring-info'
        },
        {
          color: 'warning',
          variant: [
            'outline',
            'subtle'
          ],
          class: 'focus-visible:ring-2 focus-visible:ring-inset focus-visible:ring-warning'
        },
        {
          color: 'error',
          variant: [
            'outline',
            'subtle'
          ],
          class: 'focus-visible:ring-2 focus-visible:ring-inset focus-visible:ring-error'
        },
        {
          color: 'primary',
          highlight: true,
          class: 'ring ring-inset ring-primary'
        },
        {
          color: 'secondary',
          highlight: true,
          class: 'ring ring-inset ring-secondary'
        },
        {
          color: 'success',
          highlight: true,
          class: 'ring ring-inset ring-success'
        },
        {
          color: 'info',
          highlight: true,
          class: 'ring ring-inset ring-info'
        },
        {
          color: 'warning',
          highlight: true,
          class: 'ring ring-inset ring-warning'
        },
        {
          color: 'error',
          highlight: true,
          class: 'ring ring-inset ring-error'
        },
        {
          color: 'neutral',
          variant: [
            'outline',
            'subtle'
          ],
          class: 'focus-visible:ring-2 focus-visible:ring-inset focus-visible:ring-inverted'
        },
        {
          color: 'neutral',
          highlight: true,
          class: 'ring ring-inset ring-inverted'
        },
        {
          leading: true,
          size: 'xs',
          class: 'ps-7'
        },
        {
          leading: true,
          size: 'sm',
          class: 'ps-8'
        },
        {
          leading: true,
          size: 'md',
          class: 'ps-9'
        },
        {
          leading: true,
          size: 'lg',
          class: 'ps-10'
        },
        {
          leading: true,
          size: 'xl',
          class: 'ps-11'
        },
        {
          trailing: true,
          size: 'xs',
          class: 'pe-7'
        },
        {
          trailing: true,
          size: 'sm',
          class: 'pe-8'
        },
        {
          trailing: true,
          size: 'md',
          class: 'pe-9'
        },
        {
          trailing: true,
          size: 'lg',
          class: 'pe-10'
        },
        {
          trailing: true,
          size: 'xl',
          class: 'pe-11'
        },
        {
          loading: true,
          leading: true,
          class: {
            leadingIcon: 'animate-spin'
          }
        },
        {
          loading: true,
          leading: false,
          trailing: true,
          class: {
            trailingIcon: 'animate-spin'
          }
        }
      ],
      defaultVariants: {
        size: 'md',
        color: 'primary',
        variant: 'outline'
      }
    }
  }
})
```

## Changelog

<component-changelog>



</component-changelog>
