# Source: https://react-spectrum.adobe.com/ActionMenu.md

# ActionMenu

ActionMenu combines an ActionButton with a Menu for simple "more actions" use cases.

```tsx
import {ActionMenu, MenuItem, Text, Keyboard} from '@react-spectrum/s2';
import Copy from '@react-spectrum/s2/icons/Copy';
import Cut from '@react-spectrum/s2/icons/Cut';
import Paste from '@react-spectrum/s2/icons/Paste';

<ActionMenu>
  <MenuItem
    textValue="Copy"
    onAction={() => alert('copy')}>
    <Copy />
    <Text slot="label">Copy</Text>
    <Text slot="description">Copy the selected text</Text>
    <Keyboard>âC</Keyboard>
  </MenuItem>
  <MenuItem
    textValue="Cut"
    onAction={() => alert('cut')}>
    <Cut />
    <Text slot="label">Cut</Text>
    <Text slot="description">Cut the selected text</Text>
    <Keyboard>âX</Keyboard>
  </MenuItem>
  <MenuItem
    textValue="Paste"
    onAction={() => alert('paste')}>
    <Paste />
    <Text slot="label">Paste</Text>
    <Text slot="description">Paste the copied text</Text>
    <Keyboard>âV</Keyboard>
  </MenuItem>
</ActionMenu>
```

## API

```tsx
<ActionMenu>
  <MenuItem />
</ActionMenu>
```

### ActionMenu

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `align` | `"start" | "end" | undefined` | 'start' | Alignment of the menu relative to the trigger. |
| `aria-describedby` | `string | undefined` | â | Identifies the element (or elements) that describes the object. |
| `aria-details` | `string | undefined` | â | Identifies the element (or elements) that provide a detailed, extended description for the object. |
| `aria-label` | `string | undefined` | â | Defines a string value that labels the current element. |
| `aria-labelledby` | `string | undefined` | â | Identifies the element (or elements) that labels the current element. |
| `autoFocus` | `boolean | undefined` | â | Whether the element should receive focus on render. |
| `children` | `ReactNode | ((item: T) => ReactNode)` | â | The contents of the collection. |
| `defaultOpen` | `boolean | undefined` | â | Whether the overlay is open by default (uncontrolled). |
| `direction` | `"top" | "bottom" | "start" | "end" | "left" | "right" | undefined` | 'bottom' | Where the Menu opens relative to its trigger. |
| `disabledKeys` | `Iterable<Key> | undefined` | â | The item keys that are disabled. These items cannot be selected, focused, or otherwise interacted with. |
| `id` | `string | undefined` | â | The element's unique identifier. See [MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/id). |
| `isDisabled` | `boolean | undefined` | â | Whether the button is disabled. |
| `isOpen` | `boolean | undefined` | â | Whether the overlay is open by default (controlled). |
| `isQuiet` | `boolean | undefined` | â | Whether the button should be displayed with a [quiet style](https://spectrum.adobe.com/page/action-button/#Quiet). |
| `items` | `Iterable<T> | undefined` | â | Item objects in the collection. |
| `menuSize` | `"S" | "M" | "L" | "XL" | undefined` | 'M' | The size of the Menu. |
| `onAction` | `((key: Key) => void) | undefined` | â | Handler that is called when an item is selected. |
| `onOpenChange` | `((isOpen: boolean) => void) | undefined` | â | Handler that is called when the overlay's open state changes. |
| `shouldFlip` | `boolean | undefined` | true | Whether the menu should automatically flip direction when space is limited. |
| `size` | `"S" | "M" | "L" | "XL" | "XS" | undefined` | 'M' | The size of the ActionButton. |
| `styles` | `StylesProp | undefined` | â | Spectrum-defined styles, returned by the `style()` macro. |
| `UNSAFE_className` | `UnsafeClassName | undefined` | â | Sets the CSS [className](https://developer.mozilla.org/en-US/docs/Web/API/Element/className) for the element. Only use as a **last resort**. Use the `style` macro via the `styles` prop instead. |
| `UNSAFE_style` | `CSSProperties | undefined` | â | Sets inline [style](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/style) for the element. Only use as a **last resort**. Use the `style` macro via the `styles` prop instead. |
