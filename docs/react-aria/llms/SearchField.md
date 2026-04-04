# Source: https://react-spectrum.adobe.com/SearchField.md

# SearchField

A SearchField is a text field designed for searches.

```tsx
import {SearchField} from '@react-spectrum/s2';

<SearchField />
```

## Value

Use the `value` or `defaultValue` prop to set the text value, and `onChange` to handle user input. `onSubmit` is called when the user presses <Keyboard>Enter</Keyboard>.

```tsx
import {SearchField} from '@react-spectrum/s2';
import {style} from '@react-spectrum/s2/style' with {type: 'macro'};
import {useState} from 'react';

function Example() {
  let [search, setSearch] = useState('');
  let [submittedSearch, setSubmittedSearch] = useState('');

  return (
    <div>
      <SearchField
        label="Search"
        placeholder="Search documents"
        value={search}
        onChange={setSearch}
        onSubmit={setSubmittedSearch} />
      {/*- end highlight -*/}
      <pre className={style({font: 'body'})}>
        Value: {search}{'\n'}
        Submitted value: {submittedSearch}
      </pre>
    </div>
  );
}
```

## Forms

Use the `name` prop to submit the text value to the server. Set the `isRequired`, `minLength`, `maxLength`, `pattern`, or `type` props to validate the value, or implement custom client or server-side validation. See the [Forms](forms.md) guide to learn more.

```tsx
import {SearchField, Button, Form} from '@react-spectrum/s2';

function Example(props) {
  return (
    <Form>
      <SearchField
        {...props}
        label="Search"
        placeholder="Search documents"
        name="search"
        
      />
      <Button type="submit">Submit</Button>
    </Form>
  );
}
```

## API

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `aria-activedescendant` | `string | undefined` | â | Identifies the currently active element when DOM focus is on a composite widget, textbox, group, or application. |
| `aria-autocomplete` | `"none" | "list" | "inline" | "both" | undefined` | â | Indicates whether inputting text could trigger display of one or more predictions of the user's intended value for an input and specifies how predictions would be presented if they are made. |
| `aria-controls` | `string | undefined` | â | Identifies the element (or elements) whose contents or presence are controlled by the current element. |
| `aria-describedby` | `string | undefined` | â | Identifies the element (or elements) that describes the object. |
| `aria-details` | `string | undefined` | â | Identifies the element (or elements) that provide a detailed, extended description for the object. |
| `aria-errormessage` | `string | undefined` | â | Identifies the element that provides an error message for the object. |
| `aria-haspopup` | `boolean | "dialog" | "menu" | "true" | "false" | "listbox" | "tree" | "grid" | undefined` | â | Indicates the availability and type of interactive popup element, such as menu or dialog, that can be triggered by an element. |
| `aria-label` | `string | undefined` | â | Defines a string value that labels the current element. |
| `aria-labelledby` | `string | undefined` | â | Identifies the element (or elements) that labels the current element. |
| `autoComplete` | `string | undefined` | â | Describes the type of autocomplete functionality the input should provide if any. See [MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#htmlattrdefautocomplete). |
| `autoCorrect` | `string | undefined` | â | An attribute that takes as its value a space-separated string that describes what, if any, type of autocomplete functionality the input should provide. See [MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#autocomplete). |
| `autoFocus` | `boolean | undefined` | â | Whether the element should receive focus on render. |
| `contextualHelp` | `ReactNode` | â | A ContextualHelp element to place next to the label. |
| `defaultValue` | `string | undefined` | â | The default value (uncontrolled). |
| `description` | `ReactNode` | â | A description for the field. Provides a hint such as specific requirements for what to choose. |
| `enterKeyHint` | `"search" | "enter" | "done" | "go" | "next" | "previous" | "send" | undefined` | â | An enumerated attribute that defines what action label or icon to preset for the enter key on virtual keyboards. See [MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/enterkeyhint). |
| `errorMessage` | `ReactNode | ((v: ValidationResult) => ReactNode)` | â | An error message for the field. |
| `excludeFromTabOrder` | `boolean | undefined` | â | Whether to exclude the element from the sequential tab order. If true, the element will not be focusable via the keyboard by tabbing. This should be avoided except in rare scenarios where an alternative means of accessing the element or its functionality via the keyboard is available. |
| `form` | `string | undefined` | â | The `<form>` element to associate the input with. The value of this attribute must be the id of a `<form>` in the same document. See [MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#form). |
| `id` | `string | undefined` | â | The element's unique identifier. See [MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/id). |
| `inputMode` | `"text" | "numeric" | "search" | "none" | "url" | "tel" | "email" | "decimal" | undefined` | â | Hints at the type of data that might be entered by the user while editing the element or its contents. See [MDN](https://html.spec.whatwg.org/multipage/interaction.html#input-modalities:-the-inputmode-attribute). |
| `isDisabled` | `boolean | undefined` | â | Whether the input is disabled. |
| `isInvalid` | `boolean | undefined` | â | Whether the input value is invalid. |
| `isReadOnly` | `boolean | undefined` | â | Whether the input can be selected but not changed by the user. |
| `isRequired` | `boolean | undefined` | â | Whether user input is required on the input before form submission. |
| `label` | `ReactNode` | â | The content to display as the label. |
| `labelAlign` | `Alignment | undefined` | 'start' | The label's horizontal alignment relative to the element it is labeling. |
| `labelPosition` | `LabelPosition | undefined` | 'top' | The label's overall position relative to the element it is labeling. |
| `maxLength` | `number | undefined` | â | The maximum number of characters supported by the input. See [MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#htmlattrdefmaxlength). |
| `minLength` | `number | undefined` | â | The minimum number of characters required by the input. See [MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#htmlattrdefminlength). |
| `name` | `string | undefined` | â | The name of the input element, used when submitting an HTML form. See [MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#htmlattrdefname). |
| `necessityIndicator` | `NecessityIndicator | undefined` | 'icon' | Whether the required state should be shown as an icon or text. |
| `onBeforeInput` | `FormEventHandler<HTMLInputElement> | undefined` | â | Handler that is called when the input value is about to be modified. See [MDN](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/beforeinput_event). |
| `onBlur` | `((e: FocusEvent<HTMLInputElement, Element>) => void) | undefined` | â | Handler that is called when the element loses focus. |
| `onChange` | `((value: string) => void) | undefined` | â | Handler that is called when the value changes. |
| `onClear` | `(() => void) | undefined` | â | Handler that is called when the clear button is pressed. |
| `onCompositionEnd` | `CompositionEventHandler<HTMLInputElement> | undefined` | â | Handler that is called when a text composition system completes or cancels the current text composition session. See [MDN](https://developer.mozilla.org/en-US/docs/Web/API/Element/compositionend_event). |
| `onCompositionStart` | `CompositionEventHandler<HTMLInputElement> | undefined` | â | Handler that is called when a text composition system starts a new text composition session. See [MDN](https://developer.mozilla.org/en-US/docs/Web/API/Element/compositionstart_event). |
| `onCompositionUpdate` | `CompositionEventHandler<HTMLInputElement> | undefined` | â | Handler that is called when a new character is received in the current text composition session. See [MDN](https://developer.mozilla.org/en-US/docs/Web/API/Element/compositionupdate_event). |
| `onCopy` | `ClipboardEventHandler<HTMLInputElement> | undefined` | â | Handler that is called when the user copies text. See [MDN](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/oncopy). |
| `onCut` | `ClipboardEventHandler<HTMLInputElement> | undefined` | â | Handler that is called when the user cuts text. See [MDN](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/oncut). |
| `onFocus` | `((e: FocusEvent<HTMLInputElement, Element>) => void) | undefined` | â | Handler that is called when the element receives focus. |
| `onFocusChange` | `((isFocused: boolean) => void) | undefined` | â | Handler that is called when the element's focus status changes. |
| `onInput` | `FormEventHandler<HTMLInputElement> | undefined` | â | Handler that is called when the input value is modified. See [MDN](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/input_event). |
| `onKeyDown` | `((e: KeyboardEvent) => void) | undefined` | â | Handler that is called when a key is pressed. |
| `onKeyUp` | `((e: KeyboardEvent) => void) | undefined` | â | Handler that is called when a key is released. |
| `onPaste` | `ClipboardEventHandler<HTMLInputElement> | undefined` | â | Handler that is called when the user pastes text. See [MDN](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/onpaste). |
| `onSelect` | `ReactEventHandler<HTMLInputElement> | undefined` | â | Handler that is called when text in the input is selected. See [MDN](https://developer.mozilla.org/en-US/docs/Web/API/Element/select_event). |
| `onSubmit` | `((value: string) => void) | undefined` | â | Handler that is called when the SearchField is submitted. |
| `pattern` | `string | undefined` | â | Regex pattern that the value of the input must match to be valid. See [MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#htmlattrdefpattern). |
| `placeholder` | `string | undefined` | â | Temporary text that occupies the text input when it is empty. See [MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/placeholder). |
| `size` | `"S" | "M" | "L" | "XL" | undefined` | 'M' | The size of the SearchField. |
| `slot` | `string | null | undefined` | â | A slot name for the component. Slots allow the component to receive props from a parent component. An explicit `null` value indicates that the local props completely override all props received from a parent. |
| `spellCheck` | `string | undefined` | â | An enumerated attribute that defines whether the element may be checked for spelling errors. See [MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/spellcheck). |
| `styles` | `StylesProp | undefined` | â | Spectrum-defined styles, returned by the `style()` macro. |
| `type` | `"text" | "search" | (string & {}) | "url" | "tel" | "email" | "password" | undefined` | 'search' | The type of input to render. See [MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#htmlattrdeftype). |
| `UNSAFE_className` | `UnsafeClassName | undefined` | â | Sets the CSS [className](https://developer.mozilla.org/en-US/docs/Web/API/Element/className) for the element. Only use as a **last resort**. Use the `style` macro via the `styles` prop instead. |
| `UNSAFE_style` | `CSSProperties | undefined` | â | Sets inline [style](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/style) for the element. Only use as a **last resort**. Use the `style` macro via the `styles` prop instead. |
| `validate` | `((value: string) => ValidationError | true | null | undefined) | undefined` | â | A function that returns an error message if a given value is invalid. Validation errors are displayed to the user when the form is submitted if `validationBehavior="native"`. For realtime validation, use the `isInvalid` prop instead. |
| `validationBehavior` | `"aria" | "native" | undefined` | 'native' | Whether to use native HTML form validation to prevent form submission when the value is missing or invalid, or mark the field as required or invalid via ARIA. |
| `value` | `string | undefined` | â | The current value (controlled). |
