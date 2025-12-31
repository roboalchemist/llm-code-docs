# Source: https://react-spectrum.adobe.com/ColorSlider.md

# ColorSlider

A ColorSlider allows users to adjust an individual channel of a color value.

```tsx
import {ColorSlider} from '@react-spectrum/s2';

<ColorSlider />
```

## Value

Use the `value` or `defaultValue` prop to set the color value, and the `channel` prop to specify which color channel to display. The value may be a string or `Color` object, parsed using the `parseColor` function.

The `onChange` event is called as the user drags, and `onChangeEnd` is called when the thumb is released. These are always called with a `Color` object.

```tsx
import {ColorSlider, parseColor} from '@react-spectrum/s2';
import {style} from '@react-spectrum/s2/style' with {type: 'macro'};
import {useState} from 'react';

function Example() {
  let [currentValue, setCurrentValue] = useState(parseColor('hsl(50, 100%, 50%)'));
  let [finalValue, setFinalValue] = useState(currentValue);

  return (
    <>
      <ColorSlider
        channel="hue"
        /*- begin highlight -*/
        value={currentValue}
        onChange={setCurrentValue}
        onChangeEnd={setFinalValue} />
        {/*- end highlight -*/}
      <pre className={style({font: 'body'})}>
        onChange value: {currentValue.toString('hex')}{'\n'}
        onChangeEnd value: {finalValue.toString('hex')}
      </pre>
    </>
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
| `channel` | `ColorChannel` | â | The color channel that the slider manipulates. |
| `colorSpace` | `ColorSpace | undefined` | â | The color space that the slider operates in. The `channel` must be in this color space. If not provided, this defaults to the color space of the `color` or `defaultColor` value. |
| `contextualHelp` | `ReactNode` | â | A ContextualHelp element to place next to the label. |
| `defaultValue` | `string | Color | undefined` | â | The default value (uncontrolled). |
| `form` | `string | undefined` | â | The `<form>` element to associate the input with. The value of this attribute must be the id of a `<form>` in the same document. See [MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#form). |
| `id` | `string | undefined` | â | The element's unique identifier. See [MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/id). |
| `isDisabled` | `boolean | undefined` | â | Whether the whole Slider is disabled. |
| `label` | `string | undefined` | â |  |
| `name` | `string | undefined` | â | The name of the input element, used when submitting an HTML form. See [MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#htmlattrdefname). |
| `onChange` | `((value: Color) => void) | undefined` | â | Handler that is called when the value changes, as the user drags. |
| `onChangeEnd` | `((value: Color) => void) | undefined` | â | Handler that is called when the user stops dragging. |
| `orientation` | `Orientation | undefined` | 'horizontal' | The orientation of the Slider. |
| `slot` | `string | null | undefined` | â | A slot name for the component. Slots allow the component to receive props from a parent component. An explicit `null` value indicates that the local props completely override all props received from a parent. |
| `styles` | `StylesProp | undefined` | â | Spectrum-defined styles, returned by the `style()` macro. |
| `UNSAFE_className` | `UnsafeClassName | undefined` | â | Sets the CSS [className](https://developer.mozilla.org/en-US/docs/Web/API/Element/className) for the element. Only use as a **last resort**. Use the `style` macro via the `styles` prop instead. |
| `UNSAFE_style` | `CSSProperties | undefined` | â | Sets inline [style](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/style) for the element. Only use as a **last resort**. Use the `style` macro via the `styles` prop instead. |
| `value` | `string | Color | undefined` | â | The current value (controlled). |

## Related Types

### Color

### parseColor
