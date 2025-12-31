# Source: https://react-spectrum.adobe.com/ColorArea.md

# ColorArea

A ColorArea allows users to adjust two channels of an RGB, HSL or HSB color value against a two-dimensional gradient background.

```tsx
import {ColorArea} from '@react-spectrum/s2';

<ColorArea />
```

## Value

Use the `value` or `defaultValue` prop to set the color value, and the `xChannel` and `yChannel` props to specify which color channels to display. The value may be a string or `Color` object, parsed using the `parseColor` function.

The `onChange` event is called as the user drags, and `onChangeEnd` is called when the thumb is released. These are always called with a `Color` object.

```tsx
import {ColorArea, parseColor} from '@react-spectrum/s2';
import {style} from '@react-spectrum/s2/style' with {type: 'macro'};
import {useState} from 'react';

function Example() {
  let [currentValue, setCurrentValue] = useState(parseColor('#9B80FF'));
  let [finalValue, setFinalValue] = useState(currentValue);

  return (
    <>
      <ColorArea
        xChannel="red"
        yChannel="green"
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
| `colorSpace` | `ColorSpace | undefined` | â | The color space that the color area operates in. The `xChannel` and `yChannel` must be in this color space. If not provided, this defaults to the color space of the `color` or `defaultColor` value. |
| `defaultValue` | `string | Color | undefined` | â | The default value (uncontrolled). |
| `form` | `string | undefined` | â | The `<form>` element to associate the ColorArea with. The value of this attribute must be the id of a `<form>` in the same document. See [MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#form). |
| `id` | `string | undefined` | â | The element's unique identifier. See [MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/id). |
| `isDisabled` | `boolean | undefined` | â | Whether the ColorArea is disabled. |
| `onChange` | `((value: Color) => void) | undefined` | â | Handler that is called when the value changes, as the user drags. |
| `onChangeEnd` | `((value: Color) => void) | undefined` | â | Handler that is called when the user stops dragging. |
| `slot` | `string | null | undefined` | â | A slot name for the component. Slots allow the component to receive props from a parent component. An explicit `null` value indicates that the local props completely override all props received from a parent. |
| `styles` | `StylesProp | undefined` | â | Spectrum-defined styles, returned by the `style()` macro. |
| `UNSAFE_className` | `UnsafeClassName | undefined` | â | Sets the CSS [className](https://developer.mozilla.org/en-US/docs/Web/API/Element/className) for the element. Only use as a **last resort**. Use the `style` macro via the `styles` prop instead. |
| `UNSAFE_style` | `CSSProperties | undefined` | â | Sets inline [style](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/style) for the element. Only use as a **last resort**. Use the `style` macro via the `styles` prop instead. |
| `value` | `string | Color | undefined` | â | The current value (controlled). |
| `xChannel` | `ColorChannel | undefined` | â | Color channel for the horizontal axis. |
| `xName` | `string | undefined` | â | The name of the x channel input element, used when submitting an HTML form. See [MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#htmlattrdefname). |
| `yChannel` | `ColorChannel | undefined` | â | Color channel for the vertical axis. |
| `yName` | `string | undefined` | â | The name of the y channel input element, used when submitting an HTML form. See [MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#htmlattrdefname). |

## Related Types

### Color

### parseColor
