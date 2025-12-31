# Source: https://react-spectrum.adobe.com/TextArea.md

# TextArea

A textarea allows a user to input mult-line text.

```tsx
import {TextArea} from '@react-spectrum/s2';

<TextArea />
```

## Value

Use the `value` or `defaultValue` prop to set the text value, and `onChange` to handle user input.

```tsx
import {TextArea} from '@react-spectrum/s2';
import {useState} from 'react';

function Example() {
  let [name, setName] = useState('');

  return (
    <>
      <TextArea
        label="Comment"
        placeholder="Share your thoughts!"
        value={name}
        onChange={setName} />
      {/*- end highlight -*/}
      <p>Your comment: {name}</p>
    </>
  );
}
```

## Forms

Use the `name` prop to submit the text value to the server. Set the `isRequired`, `minLength`, or `maxLength` props to validate the value, or implement custom client or server-side validation. See the [Forms](forms.md) guide to learn more.

```tsx
import {TextArea, Button, Form} from '@react-spectrum/s2';

function Example(props) {
  return (
    <Form>
      <TextArea
        {...props}
        label="Comment"
        placeholder="Share your thoughts!"
        name="email"
        description="Please provide at least 10 characters."
        
      />
      <Button type="submit">Submit</Button>
    </Form>
  );
}
```

## API

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `about` | `string | undefined` | â |  |
| `accessKey` | `string | undefined` | â |  |
| `aria-activedescendant` | `string | undefined` | â | Identifies the currently active element when DOM focus is on a composite widget, textbox, group, or application. |
| `aria-atomic` | `(boolean | "true" | "false") | undefined` | â | Indicates whether assistive technologies will present all, or only parts of, the changed region based on the change notifications defined by the aria-relevant attribute. |
| `aria-autocomplete` | `"none" | "list" | "inline" | "both" | undefined` | â | Indicates whether inputting text could trigger display of one or more predictions of the user's intended value for an input and specifies how predictions would be presented if they are made. |
| `aria-braillelabel` | `string | undefined` | â | Indicates an element is being modified and that assistive technologies MAY want to wait until the modifications are complete before exposing them to the user. |
| `aria-brailleroledescription` | `string | undefined` | â | Defines a human-readable, author-localized abbreviated description for the role of an element, which is intended to be converted into Braille. |
| `aria-busy` | `(boolean | "true" | "false") | undefined` | â |  |
| `aria-checked` | `boolean | "true" | "false" | "mixed" | undefined` | â | Indicates the current "checked" state of checkboxes, radio buttons, and other widgets. |
| `aria-colcount` | `number | undefined` | â | Defines the total number of columns in a table, grid, or treegrid. |
| `aria-colindex` | `number | undefined` | â | Defines an element's column index or position with respect to the total number of columns within a table, grid, or treegrid. |
| `aria-colindextext` | `string | undefined` | â | Defines a human readable text alternative of aria-colindex. |
| `aria-colspan` | `number | undefined` | â | Defines the number of columns spanned by a cell or gridcell within a table, grid, or treegrid. |
| `aria-controls` | `string | undefined` | â | Identifies the element (or elements) whose contents or presence are controlled by the current element. |
| `aria-current` | `boolean | "time" | "true" | "false" | "page" | "step" | "location" | "date" | undefined` | â | Indicates the element that represents the current item within a container or set of related elements. |
| `aria-describedby` | `string | undefined` | â | Identifies the element (or elements) that describes the object. |
| `aria-description` | `string | undefined` | â | Defines a string value that describes or annotates the current element. |
| `aria-details` | `string | undefined` | â | Identifies the element that provides a detailed, extended description for the object. |
| `aria-disabled` | `(boolean | "true" | "false") | undefined` | â | Indicates that the element is perceivable but disabled, so it is not editable or otherwise operable. |
| `aria-dropeffect` | `"copy" | "link" | "move" | "none" | "execute" | "popup" | undefined` | â | Indicates what functions can be performed when a dragged object is released on the drop target. |
| `aria-errormessage` | `string | undefined` | â | Identifies the element that provides an error message for the object. |
| `aria-expanded` | `(boolean | "true" | "false") | undefined` | â | Indicates whether the element, or another grouping element it controls, is currently expanded or collapsed. |
| `aria-flowto` | `string | undefined` | â | Identifies the next element (or elements) in an alternate reading order of content which, at the user's discretion, allows assistive technology to override the general default of reading in document source order. |
| `aria-grabbed` | `(boolean | "true" | "false") | undefined` | â | Indicates an element's "grabbed" state in a drag-and-drop operation. |
| `aria-haspopup` | `boolean | "dialog" | "menu" | "true" | "false" | "listbox" | "tree" | "grid" | undefined` | â | Indicates the availability and type of interactive popup element, such as menu or dialog, that can be triggered by an element. |
| `aria-hidden` | `(boolean | "true" | "false") | undefined` | â | Indicates whether the element is exposed to an accessibility API. |
| `aria-invalid` | `boolean | "true" | "false" | "grammar" | "spelling" | undefined` | â | Indicates the entered value does not conform to the format expected by the application. |
| `aria-keyshortcuts` | `string | undefined` | â | Indicates keyboard shortcuts that an author has implemented to activate or give focus to an element. |
| `aria-label` | `string | undefined` | â | Defines a string value that labels the current element. |
| `aria-labelledby` | `string | undefined` | â | Identifies the element (or elements) that labels the current element. |
| `aria-level` | `number | undefined` | â | Defines the hierarchical level of an element within a structure. |
| `aria-live` | `"off" | "assertive" | "polite" | undefined` | â | Indicates that an element will be updated, and describes the types of updates the user agents, assistive technologies, and user can expect from the live region. |
| `aria-modal` | `(boolean | "true" | "false") | undefined` | â | Indicates whether an element is modal when displayed. |
| `aria-multiline` | `(boolean | "true" | "false") | undefined` | â | Indicates whether a text box accepts multiple lines of input or only a single line. |
| `aria-multiselectable` | `(boolean | "true" | "false") | undefined` | â | Indicates that the user may select more than one item from the current selectable descendants. |
| `aria-orientation` | `"horizontal" | "vertical" | undefined` | â | Indicates whether the element's orientation is horizontal, vertical, or unknown/ambiguous. |
| `aria-owns` | `string | undefined` | â | Identifies an element (or elements) in order to define a visual, functional, or contextual parent/child relationship between DOM elements where the DOM hierarchy cannot be used to represent the relationship. |
| `aria-placeholder` | `string | undefined` | â | Defines a short hint (a word or short phrase) intended to aid the user with data entry when the control has no value. A hint could be a sample value or a brief description of the expected format. |
| `aria-posinset` | `number | undefined` | â | Defines an element's number or position in the current set of listitems or treeitems. Not required if all elements in the set are present in the DOM. |
| `aria-pressed` | `boolean | "true" | "false" | "mixed" | undefined` | â | Indicates the current "pressed" state of toggle buttons. |
| `aria-readonly` | `(boolean | "true" | "false") | undefined` | â | Indicates that the element is not editable, but is otherwise operable. |
| `aria-relevant` | `"text" | "all" | "additions" | "additions removals" | "additions text" | "removals" | "removals additions" | "removals text" | "text additions" | "text removals" | undefined` | â | Indicates what notifications the user agent will trigger when the accessibility tree within a live region is modified. |
| `aria-required` | `(boolean | "true" | "false") | undefined` | â | Indicates that user input is required on the element before a form may be submitted. |
| `aria-roledescription` | `string | undefined` | â | Defines a human-readable, author-localized description for the role of an element. |
| `aria-rowcount` | `number | undefined` | â | Defines the total number of rows in a table, grid, or treegrid. |
| `aria-rowindex` | `number | undefined` | â | Defines an element's row index or position with respect to the total number of rows within a table, grid, or treegrid. |
| `aria-rowindextext` | `string | undefined` | â | Defines a human readable text alternative of aria-rowindex. |
| `aria-rowspan` | `number | undefined` | â | Defines the number of rows spanned by a cell or gridcell within a table, grid, or treegrid. |
| `aria-selected` | `(boolean | "true" | "false") | undefined` | â | Indicates the current "selected" state of various widgets. |
| `aria-setsize` | `number | undefined` | â | Defines the number of items in the current set of listitems or treeitems. Not required if all elements in the set are present in the DOM. |
| `aria-sort` | `"none" | "ascending" | "descending" | "other" | undefined` | â | Indicates if items in a table or grid are sorted in ascending or descending order. |
| `aria-valuemax` | `number | undefined` | â | Defines the maximum allowed value for a range widget. |
| `aria-valuemin` | `number | undefined` | â | Defines the minimum allowed value for a range widget. |
| `aria-valuenow` | `number | undefined` | â | Defines the current value for a range widget. |
| `aria-valuetext` | `string | undefined` | â | Defines the human readable text alternative of aria-valuenow for a range widget. |
| `autoCapitalize` | `(string & {}) | "none" | "off" | "on" | "sentences" | "words" | "characters" | undefined` | â |  |
| `autoComplete` | `string | undefined` | â |  |
| `autoCorrect` | `string | undefined` | â |  |
| `autoFocus` | `boolean | undefined` | â |  |
| `autoSave` | `string | undefined` | â |  |
| `children` | `React.ReactNode` | â |  |
| `className` | `ClassNameOrFunction<InputRenderProps> | undefined` | 'react-aria-TextArea' | The CSS [className](https://developer.mozilla.org/en-US/docs/Web/API/Element/className) for the element. A function may be provided to compute the class based on component state. |
| `color` | `string | undefined` | â |  |
| `cols` | `number | undefined` | â |  |
| `content` | `string | undefined` | â |  |
| `contentEditable` | `(boolean | "true" | "false") | "inherit" | "plaintext-only" | undefined` | â |  |
| `contextMenu` | `string | undefined` | â |  |
| `dangerouslySetInnerHTML` | `{ __html: string | TrustedHTML; } | undefined` | â |  |
| `datatype` | `string | undefined` | â |  |
| `defaultChecked` | `boolean | undefined` | â |  |
| `defaultValue` | `string | number | readonly string[] | undefined` | â |  |
| `dir` | `string | undefined` | â |  |
| `dirName` | `string | undefined` | â |  |
| `disabled` | `boolean | undefined` | â |  |
| `draggable` | `(boolean | "true" | "false") | undefined` | â |  |
| `enterKeyHint` | `"search" | "enter" | "done" | "go" | "next" | "previous" | "send" | undefined` | â |  |
| `exportparts` | `string | undefined` | â |  |
| `form` | `string | undefined` | â |  |
| `hidden` | `boolean | undefined` | â |  |
| `id` | `string | undefined` | â |  |
| `inert` | `boolean | undefined` | â |  |
| `inlist` | `any` | â |  |
| `inputMode` | `"text" | "numeric" | "search" | "none" | "url" | "tel" | "email" | "decimal" | undefined` | â | Hints at the type of data that might be entered by the user while editing the element or its contents |
| `is` | `string | undefined` | â | Specify that a standard HTML element should behave like a defined custom built-in element |
| `itemID` | `string | undefined` | â |  |
| `itemProp` | `string | undefined` | â |  |
| `itemRef` | `string | undefined` | â |  |
| `itemScope` | `boolean | undefined` | â |  |
| `itemType` | `string | undefined` | â |  |
| `lang` | `string | undefined` | â |  |
| `maxLength` | `number | undefined` | â |  |
| `minLength` | `number | undefined` | â |  |
| `name` | `string | undefined` | â |  |
| `nonce` | `string | undefined` | â |  |
| `onAbort` | `React.ReactEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onAbortCapture` | `React.ReactEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onAnimationEnd` | `React.AnimationEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onAnimationEndCapture` | `React.AnimationEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onAnimationIteration` | `React.AnimationEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onAnimationIterationCapture` | `React.AnimationEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onAnimationStart` | `React.AnimationEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onAnimationStartCapture` | `React.AnimationEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onAuxClick` | `React.MouseEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onAuxClickCapture` | `React.MouseEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onBeforeInput` | `React.InputEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onBeforeInputCapture` | `React.FormEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onBeforeToggle` | `React.ToggleEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onBlur` | `React.FocusEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onBlurCapture` | `React.FocusEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onCanPlay` | `React.ReactEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onCanPlayCapture` | `React.ReactEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onCanPlayThrough` | `React.ReactEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onCanPlayThroughCapture` | `React.ReactEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onChange` | `React.ChangeEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onChangeCapture` | `React.FormEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onClick` | `React.MouseEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onClickCapture` | `React.MouseEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onCompositionEnd` | `React.CompositionEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onCompositionEndCapture` | `React.CompositionEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onCompositionStart` | `React.CompositionEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onCompositionStartCapture` | `React.CompositionEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onCompositionUpdate` | `React.CompositionEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onCompositionUpdateCapture` | `React.CompositionEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onContextMenu` | `React.MouseEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onContextMenuCapture` | `React.MouseEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onCopy` | `React.ClipboardEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onCopyCapture` | `React.ClipboardEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onCut` | `React.ClipboardEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onCutCapture` | `React.ClipboardEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onDoubleClick` | `React.MouseEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onDoubleClickCapture` | `React.MouseEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onDrag` | `React.DragEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onDragCapture` | `React.DragEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onDragEnd` | `React.DragEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onDragEndCapture` | `React.DragEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onDragEnter` | `React.DragEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onDragEnterCapture` | `React.DragEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onDragExit` | `React.DragEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onDragExitCapture` | `React.DragEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onDragLeave` | `React.DragEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onDragLeaveCapture` | `React.DragEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onDragOver` | `React.DragEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onDragOverCapture` | `React.DragEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onDragStart` | `React.DragEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onDragStartCapture` | `React.DragEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onDrop` | `React.DragEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onDropCapture` | `React.DragEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onDurationChange` | `React.ReactEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onDurationChangeCapture` | `React.ReactEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onEmptied` | `React.ReactEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onEmptiedCapture` | `React.ReactEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onEncrypted` | `React.ReactEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onEncryptedCapture` | `React.ReactEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onEnded` | `React.ReactEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onEndedCapture` | `React.ReactEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onError` | `React.ReactEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onErrorCapture` | `React.ReactEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onFocus` | `React.FocusEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onFocusCapture` | `React.FocusEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onGotPointerCapture` | `React.PointerEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onGotPointerCaptureCapture` | `React.PointerEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onHoverChange` | `((isHovering: boolean) => void) | undefined` | â | Handler that is called when the hover state changes. |
| `onHoverEnd` | `((e: HoverEvent) => void) | undefined` | â | Handler that is called when a hover interaction ends. |
| `onHoverStart` | `((e: HoverEvent) => void) | undefined` | â | Handler that is called when a hover interaction starts. |
| `onInput` | `React.FormEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onInputCapture` | `React.FormEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onInvalid` | `React.FormEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onInvalidCapture` | `React.FormEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onKeyDown` | `React.KeyboardEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onKeyDownCapture` | `React.KeyboardEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onKeyPress` | `React.KeyboardEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onKeyPressCapture` | `React.KeyboardEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onKeyUp` | `React.KeyboardEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onKeyUpCapture` | `React.KeyboardEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onLoad` | `React.ReactEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onLoadCapture` | `React.ReactEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onLoadedData` | `React.ReactEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onLoadedDataCapture` | `React.ReactEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onLoadedMetadata` | `React.ReactEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onLoadedMetadataCapture` | `React.ReactEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onLoadStart` | `React.ReactEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onLoadStartCapture` | `React.ReactEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onLostPointerCapture` | `React.PointerEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onLostPointerCaptureCapture` | `React.PointerEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onMouseDown` | `React.MouseEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onMouseDownCapture` | `React.MouseEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onMouseEnter` | `React.MouseEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onMouseLeave` | `React.MouseEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onMouseMove` | `React.MouseEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onMouseMoveCapture` | `React.MouseEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onMouseOut` | `React.MouseEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onMouseOutCapture` | `React.MouseEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onMouseOver` | `React.MouseEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onMouseOverCapture` | `React.MouseEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onMouseUp` | `React.MouseEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onMouseUpCapture` | `React.MouseEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onPaste` | `React.ClipboardEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onPasteCapture` | `React.ClipboardEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onPause` | `React.ReactEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onPauseCapture` | `React.ReactEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onPlay` | `React.ReactEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onPlayCapture` | `React.ReactEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onPlaying` | `React.ReactEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onPlayingCapture` | `React.ReactEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onPointerCancel` | `React.PointerEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onPointerCancelCapture` | `React.PointerEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onPointerDown` | `React.PointerEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onPointerDownCapture` | `React.PointerEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onPointerEnter` | `React.PointerEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onPointerLeave` | `React.PointerEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onPointerMove` | `React.PointerEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onPointerMoveCapture` | `React.PointerEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onPointerOut` | `React.PointerEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onPointerOutCapture` | `React.PointerEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onPointerOver` | `React.PointerEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onPointerOverCapture` | `React.PointerEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onPointerUp` | `React.PointerEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onPointerUpCapture` | `React.PointerEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onProgress` | `React.ReactEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onProgressCapture` | `React.ReactEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onRateChange` | `React.ReactEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onRateChangeCapture` | `React.ReactEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onReset` | `React.FormEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onResetCapture` | `React.FormEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onScroll` | `React.UIEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onScrollCapture` | `React.UIEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onScrollEnd` | `React.UIEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onScrollEndCapture` | `React.UIEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onSeeked` | `React.ReactEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onSeekedCapture` | `React.ReactEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onSeeking` | `React.ReactEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onSeekingCapture` | `React.ReactEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onSelect` | `React.ReactEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onSelectCapture` | `React.ReactEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onStalled` | `React.ReactEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onStalledCapture` | `React.ReactEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onSubmit` | `React.FormEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onSubmitCapture` | `React.FormEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onSuspend` | `React.ReactEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onSuspendCapture` | `React.ReactEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onTimeUpdate` | `React.ReactEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onTimeUpdateCapture` | `React.ReactEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onToggle` | `React.ToggleEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onTouchCancel` | `React.TouchEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onTouchCancelCapture` | `React.TouchEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onTouchEnd` | `React.TouchEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onTouchEndCapture` | `React.TouchEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onTouchMove` | `React.TouchEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onTouchMoveCapture` | `React.TouchEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onTouchStart` | `React.TouchEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onTouchStartCapture` | `React.TouchEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onTransitionCancel` | `React.TransitionEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onTransitionCancelCapture` | `React.TransitionEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onTransitionEnd` | `React.TransitionEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onTransitionEndCapture` | `React.TransitionEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onTransitionRun` | `React.TransitionEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onTransitionRunCapture` | `React.TransitionEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onTransitionStart` | `React.TransitionEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onTransitionStartCapture` | `React.TransitionEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onVolumeChange` | `React.ReactEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onVolumeChangeCapture` | `React.ReactEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onWaiting` | `React.ReactEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onWaitingCapture` | `React.ReactEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onWheel` | `React.WheelEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `onWheelCapture` | `React.WheelEventHandler<HTMLTextAreaElement> | undefined` | â |  |
| `part` | `string | undefined` | â |  |
| `placeholder` | `string | undefined` | â |  |
| `popover` | `"" | "auto" | "manual" | undefined` | â |  |
| `popoverTarget` | `string | undefined` | â |  |
| `popoverTargetAction` | `"show" | "hide" | "toggle" | undefined` | â |  |
| `prefix` | `string | undefined` | â |  |
| `property` | `string | undefined` | â |  |
| `radioGroup` | `string | undefined` | â |  |
| `readOnly` | `boolean | undefined` | â |  |
| `rel` | `string | undefined` | â |  |
| `required` | `boolean | undefined` | â |  |
| `resource` | `string | undefined` | â |  |
| `results` | `number | undefined` | â |  |
| `rev` | `string | undefined` | â |  |
| `role` | `React.AriaRole | undefined` | â |  |
| `rows` | `number | undefined` | â |  |
| `security` | `string | undefined` | â |  |
| `slot` | `string | undefined` | â |  |
| `spellCheck` | `(boolean | "true" | "false") | undefined` | â |  |
| `style` | `(React.CSSProperties | ((values: InputRenderProps & { defaultStyle: React.CSSProperties; }) => React.CSSProperties | undefined)) | undefined` | â | The inline [style](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/style) for the element. A function may be provided to compute the style based on component state. |
| `suppressContentEditableWarning` | `boolean | undefined` | â |  |
| `suppressHydrationWarning` | `boolean | undefined` | â |  |
| `tabIndex` | `number | undefined` | â |  |
| `title` | `string | undefined` | â |  |
| `translate` | `"yes" | "no" | undefined` | â |  |
| `typeof` | `string | undefined` | â |  |
| `unselectable` | `"off" | "on" | undefined` | â |  |
| `value` | `string | number | readonly string[] | undefined` | â |  |
| `vocab` | `string | undefined` | â |  |
| `wrap` | `string | undefined` | â |  |
