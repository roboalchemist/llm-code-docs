# Source: https://react-spectrum.adobe.com/StatusLight.md

# StatusLight

Status lights are used to color code categories and labels commonly found in data visualization.
When status lights have a semantic meaning, they should use semantic variant colors.

```tsx
import {StatusLight} from '@react-spectrum/s2';

<StatusLight />
```

## API

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `aria-describedby` | `string | undefined` | â | Identifies the element (or elements) that describes the object. |
| `aria-details` | `string | undefined` | â | Identifies the element (or elements) that provide a detailed, extended description for the object. |
| `aria-label` | `string | undefined` | â | Defines a string value that labels the current element. |
| `aria-labelledby` | `string | undefined` | â | Identifies the element (or elements) that labels the current element. |
| `children` | `ReactNode` | â | The content to display as the label. |
| `id` | `string | undefined` | â | The element's unique identifier. See [MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/id). |
| `role` | `"status" | undefined` | â | An accessibility role for the status light. Should be set when the status can change at runtime, and no more than one status light will update simultaneously. For cases where multiple statuses can change at the same time, use a Toast instead. |
| `size` | `"S" | "M" | "L" | "XL" | undefined` | 'M' | The size of the StatusLight. |
| `slot` | `string | null | undefined` | â | A slot name for the component. Slots allow the component to receive props from a parent component. An explicit `null` value indicates that the local props completely override all props received from a parent. |
| `styles` | `StylesProp | undefined` | â | Spectrum-defined styles, returned by the `style()` macro. |
| `UNSAFE_className` | `UnsafeClassName | undefined` | â | Sets the CSS [className](https://developer.mozilla.org/en-US/docs/Web/API/Element/className) for the element. Only use as a **last resort**. Use the `style` macro via the `styles` prop instead. |
| `UNSAFE_style` | `CSSProperties | undefined` | â | Sets inline [style](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/style) for the element. Only use as a **last resort**. Use the `style` macro via the `styles` prop instead. |
| `variant` | `"informative" | "neutral" | "positive" | "notice" | "negative" | "yellow" | "chartreuse" | "celery" | "seafoam" | "cyan" | "indigo" | "purple" | "fuchsia" | "magenta" | "pink" | "turquoise" | "brown" | "cinnamon" | "silver" | undefined` | 'neutral' | The variant changes the color of the status light. When status lights have a semantic meaning, they should use the variant for semantic colors. |
