# Source: https://react-spectrum.adobe.com/Disclosure.md

# Disclosure

A disclosure is a collapsible section of content. It is composed of a header with a heading and trigger button, and a panel that contains the content.

```tsx
import {Disclosure, DisclosureTitle, DisclosurePanel} from '@react-spectrum/s2';
import {style} from '@react-spectrum/s2/style' with {type: 'macro'};

<Disclosure
  styles={style({width: 250})}
  >
  <DisclosureTitle>System Requirements</DisclosureTitle>
  <DisclosurePanel>Details about system requirements here.</DisclosurePanel>
</Disclosure>
```

## Expanding

Use the `isExpanded` or `defaultExpanded` prop to set the expanded state, and `onExpandedChange` to handle user interactions.

```tsx
import {Disclosure, DisclosureTitle, DisclosurePanel} from '@react-spectrum/s2';
import {useState} from 'react';
import {style} from '@react-spectrum/s2/style' with {type: 'macro'};

function Example() {
  let [isExpanded, setIsExpanded] = useState(true);

  return (
    <Disclosure
      styles={style({width: 250})}
      /*- begin highlight -*/
      isExpanded={isExpanded}
      onExpandedChange={setIsExpanded}>
      {/*- end highlight -*/}
      <DisclosureTitle>Download, Install, and Set Up</DisclosureTitle>
      <DisclosurePanel>Instructions on how to download, install, and set up</DisclosurePanel>
    </Disclosure>
  );
}
```

## Content

Use `DisclosureHeader` to add additional elements alongside the title, such as action buttons or icons.

```tsx
import {Disclosure, DisclosureTitle, DisclosurePanel, DisclosureHeader, ActionButton} from '@react-spectrum/s2';
import {style} from '@react-spectrum/s2/style' with {type: 'macro'};

<Disclosure styles={style({width: 250})}>
  {/*- begin highlight -*/}
  <DisclosureHeader>
    <DisclosureTitle>Project Settings</DisclosureTitle>
    <ActionButton>Edit</ActionButton>
  </DisclosureHeader>
  {/*- end highlight -*/}
  <DisclosurePanel>
    Configure your project settings including name, description, and permissions.
  </DisclosurePanel>
</Disclosure>
```

## API

```tsx
<Disclosure>
  <DisclosureHeader>
    <DisclosureTitle />
  </DisclosureHeader>
  <DisclosurePanel />
</Disclosure>
```

### Disclosure

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `children` | `React.ReactNode` | â | The contents of the disclosure, consisting of a DisclosureTitle and DisclosurePanel. |
| `defaultExpanded` | `boolean | undefined` | â | Whether the disclosure is expanded by default (uncontrolled). |
| `density` | `"compact" | "regular" | "spacious" | undefined` | 'regular' | The amount of space between the disclosures. |
| `id` | `Key | undefined` | â | An id for the disclosure when used within a DisclosureGroup, matching the id used in `expandedKeys`. |
| `isDisabled` | `boolean | undefined` | â | Whether the disclosure is disabled. |
| `isExpanded` | `boolean | undefined` | â | Whether the disclosure is expanded (controlled). |
| `isQuiet` | `boolean | undefined` | â | Whether the disclosure should be displayed with a quiet style. |
| `onExpandedChange` | `((isExpanded: boolean) => void) | undefined` | â | Handler that is called when the disclosure's expanded state changes. |
| `size` | `"S" | "M" | "L" | "XL" | undefined` | 'M' | The size of the disclosure. |
| `slot` | `string | null | undefined` | â | A slot name for the component. Slots allow the component to receive props from a parent component. An explicit `null` value indicates that the local props completely override all props received from a parent. |
| `styles` | `StylesProp | undefined` | â | Spectrum-defined styles, returned by the `style()` macro. |
| `UNSAFE_className` | `UnsafeClassName | undefined` | â | Sets the CSS [className](https://developer.mozilla.org/en-US/docs/Web/API/Element/className) for the element. Only use as a **last resort**. Use the `style` macro via the `styles` prop instead. |
| `UNSAFE_style` | `React.CSSProperties | undefined` | â | Sets inline [style](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/style) for the element. Only use as a **last resort**. Use the `style` macro via the `styles` prop instead. |

### DisclosureHeader

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `children` | `React.ReactNode` | â |  |
| `id` | `string | undefined` | â | The element's unique identifier. See [MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/id). |
| `UNSAFE_className` | `UnsafeClassName | undefined` | â | Sets the CSS [className](https://developer.mozilla.org/en-US/docs/Web/API/Element/className) for the element. Only use as a **last resort**. Use the `style` macro via the `styles` prop instead. |
| `UNSAFE_style` | `React.CSSProperties | undefined` | â | Sets inline [style](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/style) for the element. Only use as a **last resort**. Use the `style` macro via the `styles` prop instead. |

### DisclosureTitle

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `children` | `React.ReactNode` | â | The contents of the disclosure header. |
| `id` | `string | undefined` | â | The element's unique identifier. See [MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/id). |
| `level` | `number | undefined` | 3 | The heading level of the disclosure header. |
| `UNSAFE_className` | `UnsafeClassName | undefined` | â | Sets the CSS [className](https://developer.mozilla.org/en-US/docs/Web/API/Element/className) for the element. Only use as a **last resort**. Use the `style` macro via the `styles` prop instead. |
| `UNSAFE_style` | `React.CSSProperties | undefined` | â | Sets inline [style](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/style) for the element. Only use as a **last resort**. Use the `style` macro via the `styles` prop instead. |

### DisclosurePanel

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `aria-describedby` | `string | undefined` | â | Identifies the element (or elements) that describes the object. |
| `aria-details` | `string | undefined` | â | Identifies the element (or elements) that provide a detailed, extended description for the object. |
| `aria-label` | `string | undefined` | â | Defines a string value that labels the current element. |
| `aria-labelledby` | `string | undefined` | â | Identifies the element (or elements) that labels the current element. |
| `children` | `React.ReactNode` | â |  |
| `dir` | `string | undefined` | â |  |
| `hidden` | `boolean | undefined` | â |  |
| `id` | `string | undefined` | â | The element's unique identifier. See [MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/id). |
| `inert` | `boolean | undefined` | â |  |
| `label` | `React.ReactNode` | â | The content to display as the label. |
| `labelElementType` | `React.ElementType | undefined` | 'label' | The HTML element used to render the label, e.g. 'label', or 'span'. |
| `lang` | `string | undefined` | â |  |
| `onAnimationEnd` | `React.AnimationEventHandler<HTMLDivElement> | undefined` | â |  |
| `onAnimationEndCapture` | `React.AnimationEventHandler<HTMLDivElement> | undefined` | â |  |
| `onAnimationIteration` | `React.AnimationEventHandler<HTMLDivElement> | undefined` | â |  |
| `onAnimationIterationCapture` | `React.AnimationEventHandler<HTMLDivElement> | undefined` | â |  |
| `onAnimationStart` | `React.AnimationEventHandler<HTMLDivElement> | undefined` | â |  |
| `onAnimationStartCapture` | `React.AnimationEventHandler<HTMLDivElement> | undefined` | â |  |
| `onAuxClick` | `React.MouseEventHandler<HTMLDivElement> | undefined` | â |  |
| `onAuxClickCapture` | `React.MouseEventHandler<HTMLDivElement> | undefined` | â |  |
| `onClick` | `React.MouseEventHandler<HTMLDivElement> | undefined` | â |  |
| `onClickCapture` | `React.MouseEventHandler<HTMLDivElement> | undefined` | â |  |
| `onContextMenu` | `React.MouseEventHandler<HTMLDivElement> | undefined` | â |  |
| `onContextMenuCapture` | `React.MouseEventHandler<HTMLDivElement> | undefined` | â |  |
| `onDoubleClick` | `React.MouseEventHandler<HTMLDivElement> | undefined` | â |  |
| `onDoubleClickCapture` | `React.MouseEventHandler<HTMLDivElement> | undefined` | â |  |
| `onGotPointerCapture` | `React.PointerEventHandler<HTMLDivElement> | undefined` | â |  |
| `onGotPointerCaptureCapture` | `React.PointerEventHandler<HTMLDivElement> | undefined` | â |  |
| `onLostPointerCapture` | `React.PointerEventHandler<HTMLDivElement> | undefined` | â |  |
| `onLostPointerCaptureCapture` | `React.PointerEventHandler<HTMLDivElement> | undefined` | â |  |
| `onMouseDown` | `React.MouseEventHandler<HTMLDivElement> | undefined` | â |  |
| `onMouseDownCapture` | `React.MouseEventHandler<HTMLDivElement> | undefined` | â |  |
| `onMouseEnter` | `React.MouseEventHandler<HTMLDivElement> | undefined` | â |  |
| `onMouseLeave` | `React.MouseEventHandler<HTMLDivElement> | undefined` | â |  |
| `onMouseMove` | `React.MouseEventHandler<HTMLDivElement> | undefined` | â |  |
| `onMouseMoveCapture` | `React.MouseEventHandler<HTMLDivElement> | undefined` | â |  |
| `onMouseOut` | `React.MouseEventHandler<HTMLDivElement> | undefined` | â |  |
| `onMouseOutCapture` | `React.MouseEventHandler<HTMLDivElement> | undefined` | â |  |
| `onMouseOver` | `React.MouseEventHandler<HTMLDivElement> | undefined` | â |  |
| `onMouseOverCapture` | `React.MouseEventHandler<HTMLDivElement> | undefined` | â |  |
| `onMouseUp` | `React.MouseEventHandler<HTMLDivElement> | undefined` | â |  |
| `onMouseUpCapture` | `React.MouseEventHandler<HTMLDivElement> | undefined` | â |  |
| `onPointerCancel` | `React.PointerEventHandler<HTMLDivElement> | undefined` | â |  |
| `onPointerCancelCapture` | `React.PointerEventHandler<HTMLDivElement> | undefined` | â |  |
| `onPointerDown` | `React.PointerEventHandler<HTMLDivElement> | undefined` | â |  |
| `onPointerDownCapture` | `React.PointerEventHandler<HTMLDivElement> | undefined` | â |  |
| `onPointerEnter` | `React.PointerEventHandler<HTMLDivElement> | undefined` | â |  |
| `onPointerLeave` | `React.PointerEventHandler<HTMLDivElement> | undefined` | â |  |
| `onPointerMove` | `React.PointerEventHandler<HTMLDivElement> | undefined` | â |  |
| `onPointerMoveCapture` | `React.PointerEventHandler<HTMLDivElement> | undefined` | â |  |
| `onPointerOut` | `React.PointerEventHandler<HTMLDivElement> | undefined` | â |  |
| `onPointerOutCapture` | `React.PointerEventHandler<HTMLDivElement> | undefined` | â |  |
| `onPointerOver` | `React.PointerEventHandler<HTMLDivElement> | undefined` | â |  |
| `onPointerOverCapture` | `React.PointerEventHandler<HTMLDivElement> | undefined` | â |  |
| `onPointerUp` | `React.PointerEventHandler<HTMLDivElement> | undefined` | â |  |
| `onPointerUpCapture` | `React.PointerEventHandler<HTMLDivElement> | undefined` | â |  |
| `onScroll` | `React.UIEventHandler<HTMLDivElement> | undefined` | â |  |
| `onScrollCapture` | `React.UIEventHandler<HTMLDivElement> | undefined` | â |  |
| `onTouchCancel` | `React.TouchEventHandler<HTMLDivElement> | undefined` | â |  |
| `onTouchCancelCapture` | `React.TouchEventHandler<HTMLDivElement> | undefined` | â |  |
| `onTouchEnd` | `React.TouchEventHandler<HTMLDivElement> | undefined` | â |  |
| `onTouchEndCapture` | `React.TouchEventHandler<HTMLDivElement> | undefined` | â |  |
| `onTouchMove` | `React.TouchEventHandler<HTMLDivElement> | undefined` | â |  |
| `onTouchMoveCapture` | `React.TouchEventHandler<HTMLDivElement> | undefined` | â |  |
| `onTouchStart` | `React.TouchEventHandler<HTMLDivElement> | undefined` | â |  |
| `onTouchStartCapture` | `React.TouchEventHandler<HTMLDivElement> | undefined` | â |  |
| `onTransitionCancel` | `React.TransitionEventHandler<HTMLDivElement> | undefined` | â |  |
| `onTransitionCancelCapture` | `React.TransitionEventHandler<HTMLDivElement> | undefined` | â |  |
| `onTransitionEnd` | `React.TransitionEventHandler<HTMLDivElement> | undefined` | â |  |
| `onTransitionEndCapture` | `React.TransitionEventHandler<HTMLDivElement> | undefined` | â |  |
| `onTransitionRun` | `React.TransitionEventHandler<HTMLDivElement> | undefined` | â |  |
| `onTransitionRunCapture` | `React.TransitionEventHandler<HTMLDivElement> | undefined` | â |  |
| `onTransitionStart` | `React.TransitionEventHandler<HTMLDivElement> | undefined` | â |  |
| `onTransitionStartCapture` | `React.TransitionEventHandler<HTMLDivElement> | undefined` | â |  |
| `onWheel` | `React.WheelEventHandler<HTMLDivElement> | undefined` | â |  |
| `onWheelCapture` | `React.WheelEventHandler<HTMLDivElement> | undefined` | â |  |
| `role` | `"region" | "group" | undefined` | 'group' | The accessibility role for the disclosure's panel. |
| `translate` | `"yes" | "no" | undefined` | â |  |
| `UNSAFE_className` | `UnsafeClassName | undefined` | â | Sets the CSS [className](https://developer.mozilla.org/en-US/docs/Web/API/Element/className) for the element. Only use as a **last resort**. Use the `style` macro via the `styles` prop instead. |
| `UNSAFE_style` | `React.CSSProperties | undefined` | â | Sets inline [style](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/style) for the element. Only use as a **last resort**. Use the `style` macro via the `styles` prop instead. |
