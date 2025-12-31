# Source: https://react-spectrum.adobe.com/Checkbox.md

# Checkbox

Checkboxes allow users to select multiple items from a list of individual items,
or to mark one individual item as selected.

```tsx
import {Checkbox} from '@react-spectrum/s2';

<Checkbox />
```

## Selection

Use the `isSelected` or `defaultSelected` prop to set the selection state, and `onChange` to handle selection changes. The `isIndeterminate` prop overrides the selection state regardless of user interaction.

```tsx
import {Checkbox} from '@react-spectrum/s2';
import {useState} from 'react';

function Example(props) {
  let [selected, setSelection] = useState(false);

  return (
    <>
      <Checkbox 
        {...props}
        isSelected={selected}
        onChange={setSelection}
        
      >
        Subscribe
      </Checkbox>
      <p>{`You are ${props.isIndeterminate ? 'partially subscribed' : selected ? 'subscribed' : 'unsubscribed'}`}</p>
    </>
  );
}
```

## Forms

Use the `name` and `value` props to submit the checkbox to the server. Set the `isRequired` prop to validate the user selects the checkbox, or implement custom client or server-side validation. See the [Forms](forms.md) guide to learn more.

```tsx
import {Checkbox, Button, Form} from '@react-spectrum/s2';

<Form>
  <Checkbox
    name="terms"
    value="agree"
    isRequired>
    {/*- end highlight -*/}
    I agree to the terms
  </Checkbox>
  <Button type="submit">Submit</Button>
</Form>
```

## API

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `aria-controls` | `string | undefined` | â | Identifies the element (or elements) whose contents or presence are controlled by the current element. |
| `aria-describedby` | `string | undefined` | â | Identifies the element (or elements) that describes the object. |
| `aria-details` | `string | undefined` | â | Identifies the element (or elements) that provide a detailed, extended description for the object. |
| `aria-errormessage` | `string | undefined` | â | Identifies the element that provides an error message for the object. |
| `aria-label` | `string | undefined` | â | Defines a string value that labels the current element. |
| `aria-labelledby` | `string | undefined` | â | Identifies the element (or elements) that labels the current element. |
| `autoFocus` | `boolean | undefined` | â | Whether the element should receive focus on render. |
| `children` | `ReactNode` | â | The label for the element. |
| `defaultSelected` | `boolean | undefined` | â | Whether the element should be selected (uncontrolled). |
| `excludeFromTabOrder` | `boolean | undefined` | â | Whether to exclude the element from the sequential tab order. If true, the element will not be focusable via the keyboard by tabbing. This should be avoided except in rare scenarios where an alternative means of accessing the element or its functionality via the keyboard is available. |
| `form` | `string | undefined` | â | The `<form>` element to associate the input with. The value of this attribute must be the id of a `<form>` in the same document. See [MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#form). |
| `id` | `string | undefined` | â | The element's unique identifier. See [MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/id). |
| `inputRef` | `RefObject<HTMLInputElement | null> | undefined` | â | A ref for the HTML input element. |
| `isDisabled` | `boolean | undefined` | â | Whether the input is disabled. |
| `isEmphasized` | `boolean | undefined` | â | Whether the Checkbox should be displayed with an emphasized style. |
| `isIndeterminate` | `boolean | undefined` | â | Indeterminism is presentational only. The indeterminate visual representation remains regardless of user interaction. |
| `isInvalid` | `boolean | undefined` | â | Whether the input value is invalid. |
| `isReadOnly` | `boolean | undefined` | â | Whether the input can be selected but not changed by the user. |
| `isRequired` | `boolean | undefined` | â | Whether user input is required on the input before form submission. |
| `isSelected` | `boolean | undefined` | â | Whether the element should be selected (controlled). |
| `name` | `string | undefined` | â | The name of the input element, used when submitting an HTML form. See [MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#htmlattrdefname). |
| `onBlur` | `((e: FocusEvent<Element>) => void) | undefined` | â | Handler that is called when the element loses focus. |
| `onChange` | `((isSelected: boolean) => void) | undefined` | â | Handler that is called when the element's selection state changes. |
| `onFocus` | `((e: FocusEvent<Element>) => void) | undefined` | â | Handler that is called when the element receives focus. |
| `onFocusChange` | `((isFocused: boolean) => void) | undefined` | â | Handler that is called when the element's focus status changes. |
| `onKeyDown` | `((e: KeyboardEvent) => void) | undefined` | â | Handler that is called when a key is pressed. |
| `onKeyUp` | `((e: KeyboardEvent) => void) | undefined` | â | Handler that is called when a key is released. |
| `onPress` | `((e: PressEvent) => void) | undefined` | â | Handler that is called when the press is released over the target. |
| `onPressChange` | `((isPressed: boolean) => void) | undefined` | â | Handler that is called when the press state changes. |
| `onPressEnd` | `((e: PressEvent) => void) | undefined` | â | Handler that is called when a press interaction ends, either over the target or when the pointer leaves the target. |
| `onPressStart` | `((e: PressEvent) => void) | undefined` | â | Handler that is called when a press interaction starts. |
| `onPressUp` | `((e: PressEvent) => void) | undefined` | â | Handler that is called when a press is released over the target, regardless of whether it started on the target or not. |
| `size` | `"S" | "M" | "L" | "XL" | undefined` | 'M' | The size of the Checkbox. |
| `slot` | `string | null | undefined` | â | A slot name for the component. Slots allow the component to receive props from a parent component. An explicit `null` value indicates that the local props completely override all props received from a parent. |
| `styles` | `StylesProp | undefined` | â | Spectrum-defined styles, returned by the `style()` macro. |
| `UNSAFE_className` | `UnsafeClassName | undefined` | â | Sets the CSS [className](https://developer.mozilla.org/en-US/docs/Web/API/Element/className) for the element. Only use as a **last resort**. Use the `style` macro via the `styles` prop instead. |
| `UNSAFE_style` | `CSSProperties | undefined` | â | Sets inline [style](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/style) for the element. Only use as a **last resort**. Use the `style` macro via the `styles` prop instead. |
| `validate` | `((value: boolean) => ValidationError | true | null | undefined) | undefined` | â | A function that returns an error message if a given value is invalid. Validation errors are displayed to the user when the form is submitted if `validationBehavior="native"`. For realtime validation, use the `isInvalid` prop instead. |
| `validationBehavior` | `"aria" | "native" | undefined` | 'native' | Whether to use native HTML form validation to prevent form submission when the value is missing or invalid, or mark the field as required or invalid via ARIA. |
| `value` | `string | undefined` | â | The value of the input element, used when submitting an HTML form. See [MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#htmlattrdefvalue). |
