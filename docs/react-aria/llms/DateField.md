# Source: https://react-spectrum.adobe.com/DateField.md

# DateField

DateFields allow users to enter and edit date and time values using a keyboard.
Each part of a date value is displayed in an individually editable segment.

```tsx
import {DateField} from '@react-spectrum/s2';

<DateField />
```

## Value

Use the `value` or `defaultValue` prop to set the date value, using objects in the [@internationalized/date](react-aria:internationalized/date/.md) package. This library supports parsing date strings in multiple formats, manipulation across international calendar systems, time zones, etc.

```tsx
import {parseDate, getLocalTimeZone, CalendarDate} from '@internationalized/date';
import {useDateFormatter} from 'react-aria';
import {DateField} from '@react-spectrum/s2';
import {useState} from 'react';

function Example() {
  let [date, setDate] = useState<CalendarDate | null>(parseDate('2020-02-03'));
  let formatter = useDateFormatter({ dateStyle: 'full' });

  return (
    <>
      <DateField
        value={date}
        onChange={setDate} />
      {/*- end highlight -*/}
      <p>Selected date: {date ? formatter.format(date.toDate(getLocalTimeZone())) : '--'}</p>
    </>
  );
}
```

### Format options

The date format is automatically determined based on the user's locale. `DateField` supports several props to control how values are displayed.

```tsx
import {parseZonedDateTime} from '@internationalized/date';
import {DateField} from '@react-spectrum/s2';

<DateField
  
  defaultValue={parseZonedDateTime('2025-02-03T08:45:00[America/Los_Angeles]')} />
```

### International calendars

By default, `DateField` displays the value using the calendar system for the user's locale. Use `<Provider>` to override the calendar system by setting the [Unicode calendar locale extension](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/calendar#adding_a_calendar_in_the_locale_string). The `onChange` event always receives a date in the same calendar as the `value` or `defaultValue` (Gregorian if no value is provided), regardless of the displayed locale.

```tsx
import {Provider, DateField} from '@react-spectrum/s2';
import {parseZonedDateTime} from '@internationalized/date';

<Provider>
  <DateField defaultValue={parseZonedDateTime('2025-02-03T08:45:00[America/Los_Angeles]')} />
</Provider>
```

## Forms

Use the `name` prop to submit the selected date to the server as an [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) string. Set the `isRequired`, `minValue`, or `maxValue` props to validate the value, or implement custom client or server-side validation. See the [Forms](forms.md) guide to learn more.

```tsx
import {today, getLocalTimeZone} from '@internationalized/date';
import {DateField, Form, Button} from '@react-spectrum/s2';

function Example(props) {
  return (
    <Form>
      <DateField
        {...props}
        label="Appointment date"
        name="date"
        
        minValue={today(getLocalTimeZone())}
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
| `defaultValue` | `T | null | undefined` | â | The default value (uncontrolled). |
| `description` | `ReactNode` | â | A description for the field. Provides a hint such as specific requirements for what to choose. |
| `errorMessage` | `ReactNode | ((v: ValidationResult) => ReactNode)` | â | An error message for the field. |
| `form` | `string | undefined` | â | The `<form>` element to associate the input with. The value of this attribute must be the id of a `<form>` in the same document. See [MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#form). |
| `granularity` | `Granularity | undefined` | â | Determines the smallest unit that is displayed in the date picker. By default, this is `"day"` for dates, and `"minute"` for times. |
| `hideTimeZone` | `boolean | undefined` | false | Whether to hide the time zone abbreviation. |
| `hourCycle` | `24 | 12 | undefined` | â | Whether to display the time in 12 or 24 hour format. By default, this is determined by the user's locale. |
| `id` | `string | undefined` | â | The element's unique identifier. See [MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/id). |
| `isDateUnavailable` | `((date: DateValue) => boolean) | undefined` | â | Callback that is called for each date of the calendar. If it returns true, then the date is unavailable. |
| `isDisabled` | `boolean | undefined` | â | Whether the input is disabled. |
| `isInvalid` | `boolean | undefined` | â | Whether the input value is invalid. |
| `isReadOnly` | `boolean | undefined` | â | Whether the input can be selected but not changed by the user. |
| `isRequired` | `boolean | undefined` | â | Whether user input is required on the input before form submission. |
| `label` | `ReactNode` | â | The content to display as the label. |
| `labelAlign` | `Alignment | undefined` | 'start' | The label's horizontal alignment relative to the element it is labeling. |
| `labelPosition` | `LabelPosition | undefined` | 'top' | The label's overall position relative to the element it is labeling. |
| `maxValue` | `DateValue | null | undefined` | â | The maximum allowed date that a user may select. |
| `minValue` | `DateValue | null | undefined` | â | The minimum allowed date that a user may select. |
| `name` | `string | undefined` | â | The name of the input element, used when submitting an HTML form. See [MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#htmlattrdefname). |
| `necessityIndicator` | `NecessityIndicator | undefined` | 'icon' | Whether the required state should be shown as an icon or text. |
| `onBlur` | `((e: FocusEvent<Element>) => void) | undefined` | â | Handler that is called when the element loses focus. |
| `onChange` | `((value: MappedDateValue<T> | null) => void) | undefined` | â | Handler that is called when the value changes. |
| `onFocus` | `((e: FocusEvent<Element>) => void) | undefined` | â | Handler that is called when the element receives focus. |
| `onFocusChange` | `((isFocused: boolean) => void) | undefined` | â | Handler that is called when the element's focus status changes. |
| `onKeyDown` | `((e: KeyboardEvent) => void) | undefined` | â | Handler that is called when a key is pressed. |
| `onKeyUp` | `((e: KeyboardEvent) => void) | undefined` | â | Handler that is called when a key is released. |
| `placeholderValue` | `T | null | undefined` | â | A placeholder date that influences the format of the placeholder shown when no value is selected. Defaults to today's date at midnight. |
| `shouldForceLeadingZeros` | `boolean | undefined` | â | Whether to always show leading zeros in the month, day, and hour fields. By default, this is determined by the user's locale. |
| `size` | `"S" | "M" | "L" | "XL" | undefined` | 'M' | The size of the DateField. |
| `slot` | `string | null | undefined` | â | A slot name for the component. Slots allow the component to receive props from a parent component. An explicit `null` value indicates that the local props completely override all props received from a parent. |
| `styles` | `StylesProp | undefined` | â | Spectrum-defined styles, returned by the `style()` macro. |
| `UNSAFE_className` | `UnsafeClassName | undefined` | â | Sets the CSS [className](https://developer.mozilla.org/en-US/docs/Web/API/Element/className) for the element. Only use as a **last resort**. Use the `style` macro via the `styles` prop instead. |
| `UNSAFE_style` | `CSSProperties | undefined` | â | Sets inline [style](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/style) for the element. Only use as a **last resort**. Use the `style` macro via the `styles` prop instead. |
| `validate` | `((value: MappedDateValue<T>) => ValidationError | true | null | undefined) | undefined` | â | A function that returns an error message if a given value is invalid. Validation errors are displayed to the user when the form is submitted if `validationBehavior="native"`. For realtime validation, use the `isInvalid` prop instead. |
| `validationBehavior` | `"aria" | "native" | undefined` | 'native' | Whether to use native HTML form validation to prevent form submission when the value is missing or invalid, or mark the field as required or invalid via ARIA. |
| `value` | `T | null | undefined` | â | The current value (controlled). |
