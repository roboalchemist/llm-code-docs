# Source: https://react-spectrum.adobe.com/ProgressBar.md

# ProgressBar

ProgressBars show the progression of a system operation: downloading, uploading, processing, etc., in a visual way.
They can represent either determinate or indeterminate progress.

```tsx
import {ProgressBar} from '@react-spectrum/s2';

<ProgressBar />
```

## Value

By default, the `value` prop is a percentage between 0 and 100. Use the `minValue`, and `maxValue` props to set a custom value scale.

```tsx
import {ProgressBar} from '@react-spectrum/s2';

<ProgressBar />
```

## API

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `aria-describedby` | `string | undefined` | â | Identifies the element (or elements) that describes the object. |
| `aria-details` | `string | undefined` | â | Identifies the element (or elements) that provide a detailed, extended description for the object. |
| `aria-label` | `string | undefined` | â | Defines a string value that labels the current element. |
| `aria-labelledby` | `string | undefined` | â | Identifies the element (or elements) that labels the current element. |
| `formatOptions` | `Intl.NumberFormatOptions | undefined` | \{style: 'percent'} | The display format of the value label. |
| `id` | `string | undefined` | â | The element's unique identifier. See [MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/id). |
| `isIndeterminate` | `boolean | undefined` | â | Whether presentation is indeterminate when progress isn't known. |
| `label` | `ReactNode` | â | The content to display as the label. |
| `labelPosition` | `LabelPosition | undefined` | 'top' | The label's overall position relative to the element it is labeling. |
| `maxValue` | `number | undefined` | 100 | The largest value allowed for the input. |
| `minValue` | `number | undefined` | 0 | The smallest value allowed for the input. |
| `size` | `"S" | "M" | "L" | "XL" | undefined` | 'M' | The size of the ProgressBar. |
| `slot` | `string | null | undefined` | â | A slot name for the component. Slots allow the component to receive props from a parent component. An explicit `null` value indicates that the local props completely override all props received from a parent. |
| `staticColor` | `"black" | "white" | "auto" | undefined` | â | The static color style to apply. Useful when the button appears over a color background. |
| `styles` | `StylesProp | undefined` | â | Spectrum-defined styles, returned by the `style()` macro. |
| `UNSAFE_className` | `UnsafeClassName | undefined` | â | Sets the CSS [className](https://developer.mozilla.org/en-US/docs/Web/API/Element/className) for the element. Only use as a **last resort**. Use the `style` macro via the `styles` prop instead. |
| `UNSAFE_style` | `CSSProperties | undefined` | â | Sets inline [style](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/style) for the element. Only use as a **last resort**. Use the `style` macro via the `styles` prop instead. |
| `value` | `number | undefined` | 0 | The current value (controlled). |
| `valueLabel` | `ReactNode` | â | The content to display as the value's label (e.g. 1 of 4). |
