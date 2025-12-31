# Source: https://react-spectrum.adobe.com/ActionButtonGroup.md

# ActionButtonGroup

An ActionButtonGroup is a grouping of related ActionButtons.

```tsx
import {ActionButtonGroup, ActionButton, Text} from '@react-spectrum/s2';
import Cut from '@react-spectrum/s2/icons/Cut';
import Copy from '@react-spectrum/s2/icons/Copy';
import Paste from '@react-spectrum/s2/icons/Paste';

<ActionButtonGroup>
  <ActionButton>
    <Cut />
    <Text>Cut</Text>
  </ActionButton>
  <ActionButton>
    <Copy />
    <Text>Copy</Text>
  </ActionButton>
  <ActionButton>
    <Paste />
    <Text>Paste</Text>
  </ActionButton>
</ActionButtonGroup>
```

## API

```tsx
<ActionButtonGroup>
  <ActionButton />
</ActionButtonGroup>
```

### ActionButtonGroup

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `aria-describedby` | `string | undefined` | â | Identifies the element (or elements) that describes the object. |
| `aria-details` | `string | undefined` | â | Identifies the element (or elements) that provide a detailed, extended description for the object. |
| `aria-label` | `string | undefined` | â | Defines a string value that labels the current element. |
| `aria-labelledby` | `string | undefined` | â | Identifies the element (or elements) that labels the current element. |
| `children` | `ReactNode` | â | The children of the group. |
| `density` | `"compact" | "regular" | undefined` | "regular" | Spacing between the buttons. |
| `isDisabled` | `boolean | undefined` | â | Whether the group is disabled. |
| `isJustified` | `boolean | undefined` | â | Whether the buttons should divide the container width equally. |
| `isQuiet` | `boolean | undefined` | â | Whether the button should be displayed with a [quiet style](https://spectrum.adobe.com/page/action-button/#Quiet). |
| `orientation` | `"horizontal" | "vertical" | undefined` | 'horizontal' | The axis the group should align with. |
| `size` | `"S" | "M" | "L" | "XL" | "XS" | undefined` | "M" | Size of the buttons. |
| `slot` | `string | null | undefined` | â | A slot name for the component. Slots allow the component to receive props from a parent component. An explicit `null` value indicates that the local props completely override all props received from a parent. |
| `staticColor` | `"black" | "white" | "auto" | undefined` | â | The static color style to apply. Useful when the ActionButtonGroup appears over a color background. |
| `styles` | `StylesPropWithHeight | undefined` | â | Spectrum-defined styles, returned by the `style()` macro. |
| `UNSAFE_className` | `UnsafeClassName | undefined` | â | Sets the CSS [className](https://developer.mozilla.org/en-US/docs/Web/API/Element/className) for the element. Only use as a **last resort**. Use the `style` macro via the `styles` prop instead. |
| `UNSAFE_style` | `CSSProperties | undefined` | â | Sets inline [style](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/style) for the element. Only use as a **last resort**. Use the `style` macro via the `styles` prop instead. |
