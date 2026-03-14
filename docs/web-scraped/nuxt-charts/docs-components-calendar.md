# Source: https://nuxtcharts.com/docs/components/calendar

Title: Calendar

URL Source: https://nuxtcharts.com/docs/components/calendar

Markdown Content:
The `ProCalendar` component is a versatile and reusable calendar for Nuxt applications, built with Nuxt UI and `dayjs`. It supports single date, multiple dates, and range selection, time picking, internationalization, and extensive customization.

Here's an example of the `ProCalendar` in action:

March 2026

Sun

Mon

Tue

Wed

Thu

Fri

Sat

[](https://nuxtcharts.com/docs/getting-started/cli)
Learn how to use the **Nuxt Charts CLI** to get premium components.

| Prop | Type | Default | Description |
| --- | --- | --- | --- |
| `selectionMode` | `'single'` | `'range'` | `'multiple'` | `'single'` | The selection mode for dates. |
| `initialDate` | `Date` | `undefined` | The initially selected date (for `single` and `multiple` modes). |
| `initialStartDate` | `Date` | `undefined` | The initially selected start date (for `range` mode). |
| `initialEndDate` | `Date` | `undefined` | The initially selected end date (for `range` mode). |
| `showTimePicker` | `boolean` | `false` | If `true`, the time picker is displayed. |
| `timeSlots` | `string[]` | `['09:00', ...]` | An array of time slots to display in the time picker. |
| `initialTime` | `string` | `undefined` | The initially selected time. |
| `dateFormat` | `string` | `'dddd, MMMM D, YYYY'` | The format for displaying selected dates. |
| `timeFormat` | `string` | `'HH:mm'` | The format for displaying selected times. |
| `weekDayLabels` | `[string, string, string, string, string, string, string]` | `['Sun', 'Mon', ...]` | An array of labels for the days of the week. |
| `orientation` | `'vertical'` | `'horizontal'` | `'horizontal'` | The orientation of the calendar and time picker. |
| `visibleMonths` | `number` | `1` | The number of months to display at once. |
| `locale` | `string` | `'en'` | The locale for `dayjs` (e.g., `'en'`, `'es'`, `'fr'`). |
| `disabledDates` | `Date[]` | `undefined` | An array of dates to disable. |
| `minDate` | `Date` | `undefined` | The minimum selectable date. |
| `maxDate` | `Date` | `undefined` | The maximum selectable date. |
| `classNames` | `object` | `{}` | An object with classes to customize the calendar's appearance. |

| Event | Payload | Description |
| --- | --- | --- |
| `date-select` | `Date` | `Date[]` | Emitted when a date is selected. The payload is a `Date` object in `single` mode and an array of `Date` objects in `multiple` mode. |
| `range-select` | `{ start: Date | null, end: Date | null }` | Emitted when a date range is selected in `range` mode. |
| `time-select` | `string` | Emitted when a time is selected from the time picker. |
| `month-change` | `Dayjs` | Emitted when the displayed month changes. The payload is a `dayjs` object. |
| `year-change` | `number` | Emitted when the displayed year changes. |

You can customize the calendar's appearance by passing a `classNames` object with the following keys:

*   `container`: The main container of the calendar.
*   `header`: The header section with the month and navigation buttons.
*   `weekdays`: The container for the weekday labels.
*   `day`: A single day in the calendar grid.
*   `today`: A class for the current day.
*   `selected`: A class for selected dates.
*   `disabled`: A class for disabled dates.
*   `inRange`: A class for dates within a selected range.

Example:

```
<template>
  <ProCalendar :class-names="customClasses" />
</template>

<script setup lang="ts">
const customClasses = {
  header: 'bg-gray-200 dark:bg-gray-800',
  selected: '!bg-green-500 text-white',
}
</script>
```

To use the calendar in different locales, import the desired locale from `dayjs` and pass the `locale` prop. For example, for Spanish:

```
<script setup>
import 'dayjs/locale/es'
</script>

<template>
  <ProCalendar locale="es" />
</template>
```

```
<template>
  <Calendar />
</template>
```
