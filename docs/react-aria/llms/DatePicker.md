# Source: https://react-spectrum.adobe.com/DatePicker.md

# DatePicker

DatePickers combine a DateField and a Calendar popover to allow users to enter or select a date and time value.

```tsx
import {DatePicker} from '@react-spectrum/s2';

<DatePicker />
```

## Value

Use the `value` or `defaultValue` prop to set the date value, using objects in the [@internationalized/date](react-aria:internationalized/date/.md) package. This library supports parsing date strings in multiple formats, manipulation across international calendar systems, time zones, etc.

```tsx
import {parseDate, getLocalTimeZone, CalendarDate} from '@internationalized/date';
import {useDateFormatter} from 'react-aria';
import {DatePicker} from '@react-spectrum/s2';
import {useState} from 'react';

function Example() {
  let [date, setDate] = useState<CalendarDate | null>(parseDate('2020-02-03'));
  let formatter = useDateFormatter({ dateStyle: 'full' });
  
  return (
    <>
      <DatePicker
        value={date}
        onChange={setDate} />
        {/*- end highlight -*/}
      <p>Selected date: {date ? formatter.format(date.toDate(getLocalTimeZone())) : '--'}</p>
    </>
  );
}
```

### Format options

The date format is automatically determined based on the user's locale. `DatePicker` supports several props to control how values are displayed.

```tsx
import {parseZonedDateTime} from '@internationalized/date';
import {DatePicker} from '@react-spectrum/s2';

<DatePicker
  
  defaultValue={parseZonedDateTime('2025-02-03T08:45:00[America/Los_Angeles]')} />
```

### International calendars

By default, `DatePicker` displays the value using the calendar system for the user's locale. Use `<Provider>` to override the calendar system by setting the [Unicode calendar locale extension](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/calendar#adding_a_calendar_in_the_locale_string). The `onChange` event always receives a date in the same calendar as the `value` or `defaultValue` (Gregorian if no value is provided), regardless of the displayed locale.

```tsx
import {Provider, DatePicker} from '@react-spectrum/s2';
import {parseZonedDateTime} from '@internationalized/date';

<Provider>
  <DatePicker defaultValue={parseZonedDateTime('2025-02-03T08:45:00[America/Los_Angeles]')} />
</Provider>
```

## Forms

Use the `name` prop to submit the selected date to the server as an [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) string. Set the `isRequired`, `minValue`, or `maxValue` props to validate the value, or implement custom client or server-side validation. The `isDateUnavailable` callback prevents certain dates from being selected. See the [Forms](forms.md) guide to learn more.

```tsx
import {isWeekend, today, getLocalTimeZone} from '@internationalized/date';
import {DatePicker, Form, Button, useLocale} from '@react-spectrum/s2';

function Example(props) {
  let {locale} = useLocale();
  let now = today(getLocalTimeZone());
  let disabledRanges = [
    [now, now.add({ days: 5 })],
    [now.add({ days: 14 }), now.add({ days: 16 })],
    [now.add({ days: 23 }), now.add({ days: 24 })]
  ];

  return (
    <Form>
      <DatePicker
        {...props}
        label="Appointment date"
        name="date"
        
        minValue={today(getLocalTimeZone())}
        isDateUnavailable={date => (
          isWeekend(date, locale) ||
          disabledRanges.some((interval) =>
            date.compare(interval[0]) >= 0 && date.compare(interval[1]) <= 0
          )
        )}
      />
      <Button type="submit">Submit</Button>
    </Form>
  );
}
```

## API

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `aria-describedby` | `string | undefined` | â | Identifies the element (or elements) that describes the object. |
| `aria-details` | `string | undefined` | â | Identifies the element (or elements) that provide a detailed, extended description for the object. |
| `aria-label` | `string | undefined` | â | Defines a string value that labels the current element. |
| `aria-labelledby` | `string | undefined` | â | Identifies the element (or elements) that labels the current element. |
| `autoComplete` | `string | undefined` | â | Describes the type of autocomplete functionality the input should provide if any. See [MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#htmlattrdefautocomplete). |
| `autoFocus` | `boolean | undefined` | â | Whether the element should receive focus on render. |
| `contextualHelp` | `ReactNode` | â | A ContextualHelp element to place next to the label. |
| `createCalendar` | `((identifier: CalendarIdentifier) => Calendar) | undefined` | â | A function to create a new [Calendar](https://react-spectrum.adobe.com/internationalized/date/Calendar.html) object for a given calendar identifier. If not provided, the `createCalendar` function from `@internationalized/date` will be used. |
| `defaultOpen` | `boolean | undefined` | â | Whether the overlay is open by default (uncontrolled). |
| `defaultValue` | `T | null | undefined` | â | The default value (uncontrolled). |
| `description` | `ReactNode` | â | A description for the field. Provides a hint such as specific requirements for what to choose. |
| `errorMessage` | `ReactNode | ((v: ValidationResult) => ReactNode)` | â | An error message for the field. |
| `firstDayOfWeek` | `"sun" | "mon" | "tue" | "wed" | "thu" | "fri" | "sat" | undefined` | â | The day that starts the week. |
| `form` | `string | undefined` | â | The `<form>` element to associate the input with. The value of this attribute must be the id of a `<form>` in the same document. See [MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#form). |
| `granularity` | `Granularity | undefined` | â | Determines the smallest unit that is displayed in the date picker. By default, this is `"day"` for dates, and `"minute"` for times. |
| `hideTimeZone` | `boolean | undefined` | false | Whether to hide the time zone abbreviation. |
| `hourCycle` | `24 | 12 | undefined` | â | Whether to display the time in 12 or 24 hour format. By default, this is determined by the user's locale. |
| `id` | `string | undefined` | â | The element's unique identifier. See [MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/id). |
| `isDateUnavailable` | `((date: DateValue) => boolean) | undefined` | â | Callback that is called for each date of the calendar. If it returns true, then the date is unavailable. |
| `isDisabled` | `boolean | undefined` | â | Whether the input is disabled. |
| `isInvalid` | `boolean | undefined` | â | Whether the input value is invalid. |
| `isOpen` | `boolean | undefined` | â | Whether the overlay is open by default (controlled). |
| `isReadOnly` | `boolean | undefined` | â | Whether the input can be selected but not changed by the user. |
| `isRequired` | `boolean | undefined` | â | Whether user input is required on the input before form submission. |
| `label` | `ReactNode` | â | The content to display as the label. |
| `labelAlign` | `Alignment | undefined` | 'start' | The label's horizontal alignment relative to the element it is labeling. |
| `labelPosition` | `LabelPosition | undefined` | 'top' | The label's overall position relative to the element it is labeling. |
| `maxValue` | `DateValue | null | undefined` | â | The maximum allowed date that a user may select. |
| `maxVisibleMonths` | `number | undefined` | 1 | The maximum number of months to display at once in the calendar popover, if screen space permits. |
| `minValue` | `DateValue | null | undefined` | â | The minimum allowed date that a user may select. |
| `name` | `string | undefined` | â | The name of the input element, used when submitting an HTML form. See [MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#htmlattrdefname). |
| `necessityIndicator` | `NecessityIndicator | undefined` | 'icon' | Whether the required state should be shown as an icon or text. |
| `onBlur` | `((e: FocusEvent<Element>) => void) | undefined` | â | Handler that is called when the element loses focus. |
| `onChange` | `((value: MappedDateValue<T> | null) => void) | undefined` | â | Handler that is called when the value changes. |
| `onFocus` | `((e: FocusEvent<Element>) => void) | undefined` | â | Handler that is called when the element receives focus. |
| `onFocusChange` | `((isFocused: boolean) => void) | undefined` | â | Handler that is called when the element's focus status changes. |
| `onKeyDown` | `((e: KeyboardEvent) => void) | undefined` | â | Handler that is called when a key is pressed. |
| `onKeyUp` | `((e: KeyboardEvent) => void) | undefined` | â | Handler that is called when a key is released. |
| `onOpenChange` | `((isOpen: boolean) => void) | undefined` | â | Handler that is called when the overlay's open state changes. |
| `pageBehavior` | `PageBehavior | undefined` | visible | Controls the behavior of paging. Pagination either works by advancing the visible page by visibleDuration (default) or one unit of visibleDuration. |
| `placeholderValue` | `T | null | undefined` | â | A placeholder date that influences the format of the placeholder shown when no value is selected. Defaults to today's date at midnight. |
| `shouldCloseOnSelect` | `boolean | (() => boolean) | undefined` | true | Determines whether the date picker popover should close automatically when a date is selected. |
| `shouldFlip` | `boolean | undefined` | true | Whether the element should flip its orientation (e.g. top to bottom or left to right) when there is insufficient room for it to render completely. |
| `shouldForceLeadingZeros` | `boolean | undefined` | â | Whether to always show leading zeros in the month, day, and hour fields. By default, this is determined by the user's locale. |
| `size` | `"S" | "M" | "L" | "XL" | undefined` | 'M' | The size of the DateField. |
| `slot` | `string | null | undefined` | â | A slot name for the component. Slots allow the component to receive props from a parent component. An explicit `null` value indicates that the local props completely override all props received from a parent. |
| `styles` | `StylesProp | undefined` | â | Spectrum-defined styles, returned by the `style()` macro. |
| `UNSAFE_className` | `UnsafeClassName | undefined` | â | Sets the CSS [className](https://developer.mozilla.org/en-US/docs/Web/API/Element/className) for the element. Only use as a **last resort**. Use the `style` macro via the `styles` prop instead. |
| `UNSAFE_style` | `CSSProperties | undefined` | â | Sets inline [style](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/style) for the element. Only use as a **last resort**. Use the `style` macro via the `styles` prop instead. |
| `validate` | `((value: MappedDateValue<T>) => ValidationError | true | null | undefined) | undefined` | â | A function that returns an error message if a given value is invalid. Validation errors are displayed to the user when the form is submitted if `validationBehavior="native"`. For realtime validation, use the `isInvalid` prop instead. |
| `validationBehavior` | `"aria" | "native" | undefined` | 'native' | Whether to use native HTML form validation to prevent form submission when the value is missing or invalid, or mark the field as required or invalid via ARIA. |
| `value` | `T | null | undefined` | â | The current value (controlled). |
