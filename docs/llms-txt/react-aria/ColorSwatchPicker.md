# Source: https://react-spectrum.adobe.com/ColorSwatchPicker.md

# ColorSwatchPicker

A ColorSwatchPicker displays a list of color swatches and allows a user to select one of them.

```tsx
import {ColorSwatchPicker, ColorSwatch} from '@react-spectrum/s2';

<ColorSwatchPicker>
  <ColorSwatch color="#f00" />
  <ColorSwatch color="#0f0" />
  <ColorSwatch color="#00f" />
  <ColorSwatch color="#ff0" />
  <ColorSwatch color="#f0f" />
  <ColorSwatch color="#0ff" />
</ColorSwatchPicker>
```

## Value

Use the `value` or `defaultValue` prop to set the selected color, and `onChange` to handle selection changes.  The value may be a string or `Color` object, parsed using the `parseColor` function.

```tsx
import {ColorSwatchPicker, ColorSwatch, parseColor} from '@react-spectrum/s2';
import {style} from '@react-spectrum/s2/style' with {type: 'macro'};
import {useState} from 'react';

function Example() {
  let [value, setValue] = useState(parseColor('#e11d48'));

  return (
    <>
      {/*- begin highlight -*/}
      <ColorSwatchPicker value={value} onChange={setValue}>
      {/*- end highlight -*/}
        <ColorSwatch color="#e11d48" />
        <ColorSwatch color="#f97316" />
        <ColorSwatch color="#eab308" />
        <ColorSwatch color="#22c55e" />
        <ColorSwatch color="#3b82f6" />
        <ColorSwatch color="#8b5cf6" />
        <ColorSwatch color="#ec4899" />
      </ColorSwatchPicker>
      <pre className={style({font: 'body'})}>Selected color: {value.toString('rgb')}</pre>
    </>
  );
}
```

<InlineAlert variant="notice">
  <Heading>Color swatches must be unique</Heading>
  <Content>Equivalent colors in different color spaces are considered duplicates. For example, the values `#f00`, `hsl(0, 100%, 50%)`, and `hsb(0, 100%, 100%)` are all the same color. This is required for predictable selection behavior.</Content>
</InlineAlert>

## API

```tsx
<ColorSwatchPicker>
  <ColorSwatch />
</ColorSwatchPicker>
```

### ColorSwatchPicker

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `children` | `ReactNode` | â | The ColorSwatches within the ColorSwatchPicker. |
| `defaultValue` | `string | Color | undefined` | â | The default value (uncontrolled). |
| `density` | `"compact" | "regular" | "spacious" | undefined` | 'regular' | The amount of padding between the swatches. |
| `onChange` | `((value: Color) => void) | undefined` | â | Handler that is called when the value changes. |
| `rounding` | `"full" | "none" | "default" | undefined` | 'none' | The corner rounding of the color swatches. |
| `size` | `"S" | "M" | "L" | "XS" | undefined` | 'M' | The size of the color swatches. |
| `slot` | `string | null | undefined` | â | A slot name for the component. Slots allow the component to receive props from a parent component. An explicit `null` value indicates that the local props completely override all props received from a parent. |
| `styles` | `StylesProp | undefined` | â | Spectrum-defined styles, returned by the `style()` macro. |
| `UNSAFE_className` | `UnsafeClassName | undefined` | â | Sets the CSS [className](https://developer.mozilla.org/en-US/docs/Web/API/Element/className) for the element. Only use as a **last resort**. Use the `style` macro via the `styles` prop instead. |
| `UNSAFE_style` | `CSSProperties | undefined` | â | Sets inline [style](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/style) for the element. Only use as a **last resort**. Use the `style` macro via the `styles` prop instead. |
| `value` | `string | Color | undefined` | â | The current value (controlled). |

## Related Types

### Color

### parseColor
