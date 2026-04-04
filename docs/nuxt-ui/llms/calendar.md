# Source: https://ui.nuxt.com/raw/docs/components/calendar.md

# Calendar

> A calendar component for selecting single dates, multiple dates or date ranges.

## Usage

Use the `v-model` directive to control the selected date.

```vue
<script setup lang="ts">
const value = ref(new CalendarDate(2022, 2, 3))
</script>

<template>
  <UCalendar v-model="value" />
</template>
```

Use the `default-value` prop to set the initial value when you do not need to control its state.

```vue
<template>
  <UCalendar />
</template>
```

**Nuxt:**
> [!NOTE]
> See: /docs/getting-started/integrations/i18n/nuxt#locale
> This component uses the `@internationalized/date` package for locale-aware formatting. The date format is determined by the `locale` prop of the App component.

**Vue:**
> [!NOTE]
> See: /docs/getting-started/integrations/i18n/vue#locale
> This component uses the `@internationalized/date` package for locale-aware formatting. The date format is determined by the `locale` prop of the App component.

### Multiple

Use the `multiple` prop to allow multiple selections.

```vue
<script setup lang="ts">
const value = ref(new CalendarDate(2022,2,4, 2022,2,6, 2022,2,8))
</script>

<template>
  <UCalendar multiple v-model="value" />
</template>
```

### Range

Use the `range` prop to select a range of dates.

```vue
<template>
  <UCalendar range v-model="value" />
</template>
```

### Color

Use the `color` prop to change the color of the calendar.

```vue
<template>
  <UCalendar color="neutral" />
</template>
```

### Variant

Use the `variant` prop to change the variant of the calendar.

```vue
<template>
  <UCalendar variant="subtle" />
</template>
```

### Size

Use the `size` prop to change the size of the calendar.

```vue
<template>
  <UCalendar size="xl" />
</template>
```

### Disabled

Use the `disabled` prop to disable the calendar.

```vue
<template>
  <UCalendar disabled />
</template>
```

### Number Of Months

Use the `numberOfMonths` prop to change the number of months in the calendar.

```vue
<template>
  <UCalendar :number-of-months="3" />
</template>
```

### Month Controls

Use the `month-controls` prop to show the month controls. Defaults to `true`.

```vue
<template>
  <UCalendar :month-controls="false" />
</template>
```

### Year Controls

Use the `year-controls` prop to show the year controls. Defaults to `true`.

```vue
<template>
  <UCalendar :year-controls="false" />
</template>
```

### Fixed Weeks

Use the `fixed-weeks` prop to display the calendar with fixed weeks.

```vue
<template>
  <UCalendar :fixed-weeks="false" />
</template>
```

### Week Numbers `4.4+`

Use the `week-numbers` prop to display week numbers in the calendar.

```vue
<template>
  <UCalendar week-numbers fixed-weeks />
</template>
```

## Examples

### With chip events

Use the [Chip](/docs/components/chip) component to add events to specific days.

```vue [CalendarEventsExample.vue]
<script setup lang="ts">
import { CalendarDate } from '@internationalized/date'

const modelValue = shallowRef(new CalendarDate(2022, 1, 10))

function getColorByDate(date: Date) {
  const isWeekend = date.getDay() % 6 == 0
  const isDayMeeting = date.getDay() % 3 == 0

  if (isWeekend) {
    return undefined
  }

  if (isDayMeeting) {
    return 'error'
  }

  return 'success'
}
</script>

<template>
  <UCalendar v-model="modelValue">
    <template #day="{ day }">
      <UChip :show="!!getColorByDate(day.toDate('UTC'))" :color="getColorByDate(day.toDate('UTC'))" size="2xs">
        {{ day.day }}
      </UChip>
    </template>
  </UCalendar>
</template>
```

### With disabled dates

Use the `is-date-disabled` prop with a function to mark specific dates as disabled.

```vue [CalendarDisabledDatesExample.vue]
<script setup lang="ts">
import type { DateValue } from '@internationalized/date'
import { CalendarDate } from '@internationalized/date'

const modelValue = shallowRef({
  start: new CalendarDate(2022, 1, 1),
  end: new CalendarDate(2022, 1, 9)
})

const isDateDisabled = (date: DateValue) => {
  return date.day >= 10 && date.day <= 16
}
</script>

<template>
  <UCalendar v-model="modelValue" :is-date-disabled="isDateDisabled" range />
</template>
```

### With unavailable dates

Use the `is-date-unavailable` prop with a function to mark specific dates as unavailable.

```vue [CalendarUnavailableDatesExample.vue]
<script setup lang="ts">
import type { DateValue } from '@internationalized/date'
import { CalendarDate } from '@internationalized/date'

const modelValue = shallowRef({
  start: new CalendarDate(2022, 1, 1),
  end: new CalendarDate(2022, 1, 9)
})

const isDateUnavailable = (date: DateValue) => {
  return date.day >= 10 && date.day <= 16
}
</script>

<template>
  <UCalendar v-model="modelValue" :is-date-unavailable="isDateUnavailable" range />
</template>
```

### With min/max dates

Use the `min-value` and `max-value` props to limit the dates.

```vue [CalendarMinMaxDatesExample.vue]
<script setup lang="ts">
import { CalendarDate } from '@internationalized/date'

const modelValue = shallowRef(new CalendarDate(2023, 9, 10))
const minDate = new CalendarDate(2023, 9, 1)
const maxDate = new CalendarDate(2023, 9, 30)
</script>

<template>
  <UCalendar v-model="modelValue" :min-value="minDate" :max-value="maxDate" />
</template>
```

### With other calendar systems

You can use other calenders from `@internationalized/date` to implement a different calendar system.

```vue [CalendarOtherSystemExample.vue]
<script lang="ts" setup>
import { CalendarDate, HebrewCalendar } from '@internationalized/date'

const hebrewDate = shallowRef(new CalendarDate(new HebrewCalendar(), 5781, 1, 1))
</script>

<template>
  <UCalendar v-model="hebrewDate" />
</template>
```

> [!NOTE]
> See: https://react-spectrum.adobe.com/internationalized/date/Calendar.html#implementations
> You can check all the available calendars on `@internationalized/date` docs.

### With external controls

You can control the calendar with external controls by manipulating the date passed in the `v-model`.

```vue [CalendarExternalControlsExample.vue]
<script setup lang="ts">
import { CalendarDate } from '@internationalized/date'

const date = shallowRef(new CalendarDate(2025, 4, 2))
</script>

<template>
  <div class="flex flex-col gap-4">
    <UCalendar v-model="date" :month-controls="false" :year-controls="false" />

    <div class="flex justify-between gap-4">
      <UButton color="neutral" variant="outline" @click="date = date.subtract({ months: 1 })">
        Prev
      </UButton>

      <UButton color="neutral" variant="outline" @click="date = date.add({ months: 1 })">
        Next
      </UButton>
    </div>
  </div>
</template>
```

### As a DatePicker

Use a [Button](/docs/components/button) and a [Popover](/docs/components/popover) component to create a date picker.

```vue [CalendarDatePickerExample.vue]
<script setup lang="ts">
import { CalendarDate, DateFormatter, getLocalTimeZone } from '@internationalized/date'

const df = new DateFormatter('en-US', {
  dateStyle: 'medium'
})

const modelValue = shallowRef(new CalendarDate(2022, 1, 10))
</script>

<template>
  <UPopover>
    <UButton color="neutral" variant="subtle" icon="i-lucide-calendar">
      {{ modelValue ? df.format(modelValue.toDate(getLocalTimeZone())) : 'Select a date' }}
    </UButton>

    <template #content>
      <UCalendar v-model="modelValue" class="p-2" />
    </template>
  </UPopover>
</template>
```

### As a DateRangePicker

Use a [Button](/docs/components/button) and a [Popover](/docs/components/popover) component to create a date range picker.

```vue [CalendarDateRangePickerExample.vue]
<script setup lang="ts">
import { CalendarDate, DateFormatter, getLocalTimeZone } from '@internationalized/date'

const df = new DateFormatter('en-US', {
  dateStyle: 'medium'
})

const modelValue = shallowRef({
  start: new CalendarDate(2022, 1, 20),
  end: new CalendarDate(2022, 2, 10)
})
</script>

<template>
  <UPopover>
    <UButton color="neutral" variant="subtle" icon="i-lucide-calendar">
      <template v-if="modelValue.start">
        <template v-if="modelValue.end">
          {{ df.format(modelValue.start.toDate(getLocalTimeZone())) }} - {{ df.format(modelValue.end.toDate(getLocalTimeZone())) }}
        </template>

        <template v-else>
          {{ df.format(modelValue.start.toDate(getLocalTimeZone())) }}
        </template>
      </template>
      <template v-else>
        Pick a date
      </template>
    </UButton>

    <template #content>
      <UCalendar v-model="modelValue" class="p-2" :number-of-months="2" range />
    </template>
  </UPopover>
</template>
```

## API

### Props

```ts
/**
 * Props for the Calendar component
 */
interface CalendarProps {
  /**
   * The element or component this component should render as.
   */
  as?: any;
  /**
   * The icon to use for the next year control.
   */
  nextYearIcon?: any;
  /**
   * Configure the next year button.
   * `{ color: 'neutral', variant: 'ghost' }`{lang="ts-type"}
   */
  nextYear?: Omit<ButtonProps, LinkPropsKeys> | undefined;
  /**
   * The icon to use for the next month control.
   */
  nextMonthIcon?: any;
  /**
   * Configure the next month button.
   * `{ color: 'neutral', variant: 'ghost' }`{lang="ts-type"}
   */
  nextMonth?: Omit<ButtonProps, LinkPropsKeys> | undefined;
  /**
   * The icon to use for the previous year control.
   */
  prevYearIcon?: any;
  /**
   * Configure the prev year button.
   * `{ color: 'neutral', variant: 'ghost' }`{lang="ts-type"}
   */
  prevYear?: Omit<ButtonProps, LinkPropsKeys> | undefined;
  /**
   * The icon to use for the previous month control.
   */
  prevMonthIcon?: any;
  /**
   * Configure the prev month button.
   * `{ color: 'neutral', variant: 'ghost' }`{lang="ts-type"}
   */
  prevMonth?: Omit<ButtonProps, LinkPropsKeys> | undefined;
  color?: "primary" | "secondary" | "success" | "info" | "warning" | "error" | "neutral" | undefined;
  variant?: "solid" | "outline" | "soft" | "subtle" | undefined;
  size?: "md" | "xs" | "sm" | "lg" | "xl" | undefined;
  /**
   * Whether or not a range of dates can be selected
   */
  range?: R | undefined;
  /**
   * Whether or not multiple dates can be selected
   */
  multiple?: M | undefined;
  /**
   * Show month controls
   * @default "true"
   */
  monthControls?: boolean | undefined;
  /**
   * Show year controls
   * @default "true"
   */
  yearControls?: boolean | undefined;
  defaultValue?: CalendarDate | CalendarDateTime | ZonedDateTime | DateRange | DateValue[];
  modelValue?: null | CalendarDate | CalendarDateTime | ZonedDateTime | DateRange | DateValue[];
  weekNumbers?: boolean | undefined;
  ui?: { root?: ClassNameValue; header?: ClassNameValue; body?: ClassNameValue; heading?: ClassNameValue; grid?: ClassNameValue; gridRow?: ClassNameValue; gridWeekDaysRow?: ClassNameValue; gridBody?: ClassNameValue; headCell?: ClassNameValue; headCellWeek?: ClassNameValue; cell?: ClassNameValue; cellTrigger?: ClassNameValue; cellWeek?: ClassNameValue; } | undefined;
  defaultPlaceholder?: CalendarDate | CalendarDateTime | ZonedDateTime;
  placeholder?: CalendarDate | CalendarDateTime | ZonedDateTime;
  /**
   * When combined with `isDateUnavailable`, determines whether non-contiguous ranges, i.e. ranges containing unavailable dates, may be selected.
   */
  allowNonContiguousRanges?: boolean | undefined;
  /**
   * This property causes the previous and next buttons to navigate by the number of months displayed at once, rather than one month
   */
  pagedNavigation?: boolean | undefined;
  /**
   * Whether or not to prevent the user from deselecting a date without selecting another date first
   */
  preventDeselect?: boolean | undefined;
  /**
   * The maximum number of days that can be selected in a range
   */
  maximumDays?: number | undefined;
  /**
   * The day of the week to start the calendar on
   */
  weekStartsOn?: 0 | 1 | 2 | 4 | 5 | 3 | 6 | undefined;
  /**
   * The format to use for the weekday strings provided via the weekdays slot prop
   */
  weekdayFormat?: WeekDayFormat | undefined;
  /**
   * Whether or not to always display 6 weeks in the calendar
   * @default "true"
   */
  fixedWeeks?: boolean | undefined;
  maxValue?: CalendarDate | CalendarDateTime | ZonedDateTime;
  minValue?: CalendarDate | CalendarDateTime | ZonedDateTime;
  /**
   * The number of months to display at once
   */
  numberOfMonths?: number | undefined;
  /**
   * Whether or not the calendar is disabled
   */
  disabled?: boolean | undefined;
  /**
   * Whether or not the calendar is readonly
   */
  readonly?: boolean | undefined;
  /**
   * If true, the calendar will focus the selected day, today, or the first day of the month depending on what is visible when the calendar is mounted
   */
  initialFocus?: boolean | undefined;
  /**
   * A function that returns whether or not a date is disabled
   */
  isDateDisabled?: Matcher | undefined;
  /**
   * A function that returns whether or not a date is unavailable
   */
  isDateUnavailable?: Matcher | undefined;
  /**
   * A function that returns whether or not a date is hightable
   */
  isDateHighlightable?: Matcher | undefined;
  /**
   * A function that returns the next page of the calendar. It receives the current placeholder as an argument inside the component.
   */
  nextPage?: ((placeholder: DateValue) => DateValue) | undefined;
  /**
   * A function that returns the previous page of the calendar. It receives the current placeholder as an argument inside the component.
   */
  prevPage?: ((placeholder: DateValue) => DateValue) | undefined;
  /**
   * Whether or not to disable days outside the current view.
   */
  disableDaysOutsideCurrentView?: boolean | undefined;
  /**
   * Which part of the range should be fixed
   */
  fixedDate?: "start" | "end" | undefined;
}
```

### Slots

```ts
/**
 * Slots for the Calendar component
 */
interface CalendarSlots {
  heading(): any;
  day(): any;
  week-day(): any;
}
```

### Emits

```ts
/**
 * Emitted events for the Calendar component
 */
interface CalendarEmits {
  update:modelValue: (payload: [date: CalendarModelValue<R, M>]) => void;
  update:placeholder: (payload: [date: DateValue] & [date: DateValue]) => void;
  update:validModelValue: (payload: [date: DateRange]) => void;
  update:startValue: (payload: [date: DateValue | undefined]) => void;
}
```

## Theme

```ts [app.config.ts]
export default defineAppConfig({
  ui: {
    calendar: {
      slots: {
        root: '',
        header: 'flex items-center justify-between',
        body: 'flex flex-col space-y-4 pt-4 sm:flex-row sm:space-x-4 sm:space-y-0',
        heading: 'text-center font-medium truncate mx-auto',
        grid: 'w-full border-collapse select-none space-y-1 focus:outline-none',
        gridRow: 'grid grid-cols-7 place-items-center',
        gridWeekDaysRow: 'mb-1 grid w-full grid-cols-7',
        gridBody: 'grid',
        headCell: 'rounded-md',
        headCellWeek: 'rounded-md text-muted',
        cell: 'relative text-center',
        cellTrigger: [
          'm-0.5 relative flex items-center justify-center rounded-full whitespace-nowrap focus-visible:ring-2 focus:outline-none data-disabled:text-muted data-unavailable:line-through data-unavailable:text-muted data-unavailable:pointer-events-none data-today:font-semibold data-[outside-view]:text-muted',
          'transition'
        ],
        cellWeek: 'relative text-center text-muted'
      },
      variants: {
        color: {
          primary: {
            headCell: 'text-primary',
            cellTrigger: 'focus-visible:ring-primary'
          },
          secondary: {
            headCell: 'text-secondary',
            cellTrigger: 'focus-visible:ring-secondary'
          },
          success: {
            headCell: 'text-success',
            cellTrigger: 'focus-visible:ring-success'
          },
          info: {
            headCell: 'text-info',
            cellTrigger: 'focus-visible:ring-info'
          },
          warning: {
            headCell: 'text-warning',
            cellTrigger: 'focus-visible:ring-warning'
          },
          error: {
            headCell: 'text-error',
            cellTrigger: 'focus-visible:ring-error'
          },
          neutral: {
            headCell: 'text-highlighted',
            cellTrigger: 'focus-visible:ring-inverted'
          }
        },
        variant: {
          solid: '',
          outline: '',
          soft: '',
          subtle: ''
        },
        size: {
          xs: {
            heading: 'text-xs',
            cell: 'text-xs',
            cellWeek: 'text-xs',
            headCell: 'text-[10px]',
            headCellWeek: 'text-[10px]',
            cellTrigger: 'size-7',
            body: 'space-y-2 pt-2'
          },
          sm: {
            heading: 'text-xs',
            headCell: 'text-xs',
            headCellWeek: 'text-xs',
            cellWeek: 'text-xs',
            cell: 'text-xs',
            cellTrigger: 'size-7'
          },
          md: {
            heading: 'text-sm',
            headCell: 'text-xs',
            headCellWeek: 'text-xs',
            cellWeek: 'text-xs',
            cell: 'text-sm',
            cellTrigger: 'size-8'
          },
          lg: {
            heading: 'text-md',
            headCell: 'text-md',
            headCellWeek: 'text-md',
            cellTrigger: 'size-9 text-md'
          },
          xl: {
            heading: 'text-lg',
            headCell: 'text-lg',
            headCellWeek: 'text-lg',
            cellTrigger: 'size-10 text-lg'
          }
        },
        weekNumbers: {
          true: {
            gridRow: 'grid-cols-8',
            gridWeekDaysRow: 'grid-cols-8 [&>*:first-child]:col-start-2'
          }
        }
      },
      compoundVariants: [
        {
          color: 'primary',
          variant: 'solid',
          class: {
            cellTrigger: 'data-[selected]:bg-primary data-[selected]:text-inverted data-today:not-data-[selected]:text-primary data-[highlighted]:bg-primary/20 hover:not-data-[selected]:bg-primary/20'
          }
        },
        {
          color: 'secondary',
          variant: 'solid',
          class: {
            cellTrigger: 'data-[selected]:bg-secondary data-[selected]:text-inverted data-today:not-data-[selected]:text-secondary data-[highlighted]:bg-secondary/20 hover:not-data-[selected]:bg-secondary/20'
          }
        },
        {
          color: 'success',
          variant: 'solid',
          class: {
            cellTrigger: 'data-[selected]:bg-success data-[selected]:text-inverted data-today:not-data-[selected]:text-success data-[highlighted]:bg-success/20 hover:not-data-[selected]:bg-success/20'
          }
        },
        {
          color: 'info',
          variant: 'solid',
          class: {
            cellTrigger: 'data-[selected]:bg-info data-[selected]:text-inverted data-today:not-data-[selected]:text-info data-[highlighted]:bg-info/20 hover:not-data-[selected]:bg-info/20'
          }
        },
        {
          color: 'warning',
          variant: 'solid',
          class: {
            cellTrigger: 'data-[selected]:bg-warning data-[selected]:text-inverted data-today:not-data-[selected]:text-warning data-[highlighted]:bg-warning/20 hover:not-data-[selected]:bg-warning/20'
          }
        },
        {
          color: 'error',
          variant: 'solid',
          class: {
            cellTrigger: 'data-[selected]:bg-error data-[selected]:text-inverted data-today:not-data-[selected]:text-error data-[highlighted]:bg-error/20 hover:not-data-[selected]:bg-error/20'
          }
        },
        {
          color: 'primary',
          variant: 'outline',
          class: {
            cellTrigger: 'data-[selected]:ring data-[selected]:ring-inset data-[selected]:ring-primary/50 data-[selected]:text-primary data-today:not-data-[selected]:text-primary data-[highlighted]:bg-primary/10 hover:not-data-[selected]:bg-primary/10'
          }
        },
        {
          color: 'secondary',
          variant: 'outline',
          class: {
            cellTrigger: 'data-[selected]:ring data-[selected]:ring-inset data-[selected]:ring-secondary/50 data-[selected]:text-secondary data-today:not-data-[selected]:text-secondary data-[highlighted]:bg-secondary/10 hover:not-data-[selected]:bg-secondary/10'
          }
        },
        {
          color: 'success',
          variant: 'outline',
          class: {
            cellTrigger: 'data-[selected]:ring data-[selected]:ring-inset data-[selected]:ring-success/50 data-[selected]:text-success data-today:not-data-[selected]:text-success data-[highlighted]:bg-success/10 hover:not-data-[selected]:bg-success/10'
          }
        },
        {
          color: 'info',
          variant: 'outline',
          class: {
            cellTrigger: 'data-[selected]:ring data-[selected]:ring-inset data-[selected]:ring-info/50 data-[selected]:text-info data-today:not-data-[selected]:text-info data-[highlighted]:bg-info/10 hover:not-data-[selected]:bg-info/10'
          }
        },
        {
          color: 'warning',
          variant: 'outline',
          class: {
            cellTrigger: 'data-[selected]:ring data-[selected]:ring-inset data-[selected]:ring-warning/50 data-[selected]:text-warning data-today:not-data-[selected]:text-warning data-[highlighted]:bg-warning/10 hover:not-data-[selected]:bg-warning/10'
          }
        },
        {
          color: 'error',
          variant: 'outline',
          class: {
            cellTrigger: 'data-[selected]:ring data-[selected]:ring-inset data-[selected]:ring-error/50 data-[selected]:text-error data-today:not-data-[selected]:text-error data-[highlighted]:bg-error/10 hover:not-data-[selected]:bg-error/10'
          }
        },
        {
          color: 'primary',
          variant: 'soft',
          class: {
            cellTrigger: 'data-[selected]:bg-primary/10 data-[selected]:text-primary data-today:not-data-[selected]:text-primary data-[highlighted]:bg-primary/20 hover:not-data-[selected]:bg-primary/20'
          }
        },
        {
          color: 'secondary',
          variant: 'soft',
          class: {
            cellTrigger: 'data-[selected]:bg-secondary/10 data-[selected]:text-secondary data-today:not-data-[selected]:text-secondary data-[highlighted]:bg-secondary/20 hover:not-data-[selected]:bg-secondary/20'
          }
        },
        {
          color: 'success',
          variant: 'soft',
          class: {
            cellTrigger: 'data-[selected]:bg-success/10 data-[selected]:text-success data-today:not-data-[selected]:text-success data-[highlighted]:bg-success/20 hover:not-data-[selected]:bg-success/20'
          }
        },
        {
          color: 'info',
          variant: 'soft',
          class: {
            cellTrigger: 'data-[selected]:bg-info/10 data-[selected]:text-info data-today:not-data-[selected]:text-info data-[highlighted]:bg-info/20 hover:not-data-[selected]:bg-info/20'
          }
        },
        {
          color: 'warning',
          variant: 'soft',
          class: {
            cellTrigger: 'data-[selected]:bg-warning/10 data-[selected]:text-warning data-today:not-data-[selected]:text-warning data-[highlighted]:bg-warning/20 hover:not-data-[selected]:bg-warning/20'
          }
        },
        {
          color: 'error',
          variant: 'soft',
          class: {
            cellTrigger: 'data-[selected]:bg-error/10 data-[selected]:text-error data-today:not-data-[selected]:text-error data-[highlighted]:bg-error/20 hover:not-data-[selected]:bg-error/20'
          }
        },
        {
          color: 'primary',
          variant: 'subtle',
          class: {
            cellTrigger: 'data-[selected]:bg-primary/10 data-[selected]:text-primary data-[selected]:ring data-[selected]:ring-inset data-[selected]:ring-primary/25 data-today:not-data-[selected]:text-primary data-[highlighted]:bg-primary/20 hover:not-data-[selected]:bg-primary/20'
          }
        },
        {
          color: 'secondary',
          variant: 'subtle',
          class: {
            cellTrigger: 'data-[selected]:bg-secondary/10 data-[selected]:text-secondary data-[selected]:ring data-[selected]:ring-inset data-[selected]:ring-secondary/25 data-today:not-data-[selected]:text-secondary data-[highlighted]:bg-secondary/20 hover:not-data-[selected]:bg-secondary/20'
          }
        },
        {
          color: 'success',
          variant: 'subtle',
          class: {
            cellTrigger: 'data-[selected]:bg-success/10 data-[selected]:text-success data-[selected]:ring data-[selected]:ring-inset data-[selected]:ring-success/25 data-today:not-data-[selected]:text-success data-[highlighted]:bg-success/20 hover:not-data-[selected]:bg-success/20'
          }
        },
        {
          color: 'info',
          variant: 'subtle',
          class: {
            cellTrigger: 'data-[selected]:bg-info/10 data-[selected]:text-info data-[selected]:ring data-[selected]:ring-inset data-[selected]:ring-info/25 data-today:not-data-[selected]:text-info data-[highlighted]:bg-info/20 hover:not-data-[selected]:bg-info/20'
          }
        },
        {
          color: 'warning',
          variant: 'subtle',
          class: {
            cellTrigger: 'data-[selected]:bg-warning/10 data-[selected]:text-warning data-[selected]:ring data-[selected]:ring-inset data-[selected]:ring-warning/25 data-today:not-data-[selected]:text-warning data-[highlighted]:bg-warning/20 hover:not-data-[selected]:bg-warning/20'
          }
        },
        {
          color: 'error',
          variant: 'subtle',
          class: {
            cellTrigger: 'data-[selected]:bg-error/10 data-[selected]:text-error data-[selected]:ring data-[selected]:ring-inset data-[selected]:ring-error/25 data-today:not-data-[selected]:text-error data-[highlighted]:bg-error/20 hover:not-data-[selected]:bg-error/20'
          }
        },
        {
          color: 'neutral',
          variant: 'solid',
          class: {
            cellTrigger: 'data-[selected]:bg-inverted data-[selected]:text-inverted data-today:not-data-[selected]:text-highlighted data-[highlighted]:bg-inverted/20 hover:not-data-[selected]:bg-inverted/10'
          }
        },
        {
          color: 'neutral',
          variant: 'outline',
          class: {
            cellTrigger: 'data-[selected]:ring data-[selected]:ring-inset data-[selected]:ring-accented data-[selected]:text-default data-[selected]:bg-default data-today:not-data-[selected]:text-highlighted data-[highlighted]:bg-inverted/10 hover:not-data-[selected]:bg-inverted/10'
          }
        },
        {
          color: 'neutral',
          variant: 'soft',
          class: {
            cellTrigger: 'data-[selected]:bg-elevated data-[selected]:text-default data-today:not-data-[selected]:text-highlighted data-[highlighted]:bg-inverted/20 hover:not-data-[selected]:bg-inverted/10'
          }
        },
        {
          color: 'neutral',
          variant: 'subtle',
          class: {
            cellTrigger: 'data-[selected]:bg-elevated data-[selected]:text-default data-[selected]:ring data-[selected]:ring-inset data-[selected]:ring-accented data-today:not-data-[selected]:text-highlighted data-[highlighted]:bg-inverted/20 hover:not-data-[selected]:bg-inverted/10'
          }
        }
      ],
      defaultVariants: {
        size: 'md',
        color: 'primary',
        variant: 'solid'
      }
    }
  }
})
```

## Changelog

See the [releases page](https://github.com/nuxt/ui/releases) for the latest changes.
