# Source: https://react-spectrum.adobe.com/Toast.md

# Toast



```tsx
import {ToastContainer, ButtonGroup, Button, ToastQueue} from '@react-spectrum/s2';

function App(props) {
  return (
    <>
      <ToastContainer {...props} />
      <ButtonGroup>
        <Button
          onPress={() => ToastQueue.neutral('Toast available')}
          variant="secondary">
          Show Neutral Toast
        </Button>
        <Button
          onPress={() => ToastQueue.positive('Toast is done!')}
          variant="primary">
          Show Positive Toast
        </Button>
        <Button
          onPress={() => ToastQueue.negative('Toast is burned!')}
          variant="negative">
          Show Negative Toast
        </Button>
        <Button
          onPress={() => ToastQueue.info('Toastingâ¦')}
          variant="accent">
          Show Info Toast
        </Button>
      </ButtonGroup>
    </>
  );
}
```

## Actions

Use the `actionLabel` and `onAction` options to add an action button to the toast. Set `shouldCloseOnAction` to true to close the toast when the user presses the button.

```tsx
import {Button, ToastQueue} from '@react-spectrum/s2';

<Button
  onPress={() => ToastQueue.info('An update is available', {
    /*- begin highlight -*/
    actionLabel: 'Update',
    onAction: () => alert('Updating!'),
    shouldCloseOnAction: true
    /*- end highlight -*/
  })}>
  Show actionable toast
</Button>
```

## Dismissal

Use the `timeout` option to automatically hide a toast after a delay. For accessibility, toasts have a minimum timeout of 5 seconds, and actionable toasts will not auto dismiss. Timers will pause when the user focuses or hovers over a toast.

```tsx
import {Button, ToastQueue} from '@react-spectrum/s2';

<Button
  onPress={() => ToastQueue.positive('Toast is done!', {
    /*- begin highlight -*/
    timeout: 5000
    /*- end highlight -*/
  })}>
  Show auto-dismissing toast
</Button>
```

### Programmatic dismissal

Use the close function returned by `ToastQueue` to programmatically dismiss a toast that is no longer relevant. The `onClose` event is triggered when a toast is dismissed, either by user action or programmatically.

```tsx
import {Button, ToastQueue, Text} from '@react-spectrum/s2';
import {useState} from 'react';

function Example() {
  let [close, setClose] = useState<(() => void) | null>(null);

  return (
    <Button
      onPress={() => {
        /*- begin highlight -*/
        if (!close) {
          let close = ToastQueue.negative('Unable to save', {
            onClose: () => setClose(null)
          });
          setClose(() => close);
        } else {
          close();
        }
        /*- end highlight -*/
      }}>
      <Text>{close ? 'Hide Toast' : 'Show Toast'}</Text>
    </Button>
  );
}
```

## API

### ToastContainer

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `aria-describedby` | `string | undefined` | â | Identifies the element (or elements) that describes the object. |
| `aria-details` | `string | undefined` | â | Identifies the element (or elements) that provide a detailed, extended description for the object. |
| `aria-label` | `string | undefined` | "Notifications" | An accessibility label for the toast region. |
| `aria-labelledby` | `string | undefined` | â | Identifies the element (or elements) that labels the current element. |
| `dir` | `string | undefined` | â |  |
| `hidden` | `boolean | undefined` | â |  |
| `inert` | `boolean | undefined` | â |  |
| `lang` | `string | undefined` | â |  |
| `onAnimationEnd` | `AnimationEventHandler<HTMLDivElement> | undefined` | â |  |
| `onAnimationEndCapture` | `AnimationEventHandler<HTMLDivElement> | undefined` | â |  |
| `onAnimationIteration` | `AnimationEventHandler<HTMLDivElement> | undefined` | â |  |
| `onAnimationIterationCapture` | `AnimationEventHandler<HTMLDivElement> | undefined` | â |  |
| `onAnimationStart` | `AnimationEventHandler<HTMLDivElement> | undefined` | â |  |
| `onAnimationStartCapture` | `AnimationEventHandler<HTMLDivElement> | undefined` | â |  |
| `onAuxClick` | `MouseEventHandler<HTMLDivElement> | undefined` | â |  |
| `onAuxClickCapture` | `MouseEventHandler<HTMLDivElement> | undefined` | â |  |
| `onClick` | `MouseEventHandler<HTMLDivElement> | undefined` | â |  |
| `onClickCapture` | `MouseEventHandler<HTMLDivElement> | undefined` | â |  |
| `onContextMenu` | `MouseEventHandler<HTMLDivElement> | undefined` | â |  |
| `onContextMenuCapture` | `MouseEventHandler<HTMLDivElement> | undefined` | â |  |
| `onDoubleClick` | `MouseEventHandler<HTMLDivElement> | undefined` | â |  |
| `onDoubleClickCapture` | `MouseEventHandler<HTMLDivElement> | undefined` | â |  |
| `onGotPointerCapture` | `PointerEventHandler<HTMLDivElement> | undefined` | â |  |
| `onGotPointerCaptureCapture` | `PointerEventHandler<HTMLDivElement> | undefined` | â |  |
| `onLostPointerCapture` | `PointerEventHandler<HTMLDivElement> | undefined` | â |  |
| `onLostPointerCaptureCapture` | `PointerEventHandler<HTMLDivElement> | undefined` | â |  |
| `onMouseDown` | `MouseEventHandler<HTMLDivElement> | undefined` | â |  |
| `onMouseDownCapture` | `MouseEventHandler<HTMLDivElement> | undefined` | â |  |
| `onMouseEnter` | `MouseEventHandler<HTMLDivElement> | undefined` | â |  |
| `onMouseLeave` | `MouseEventHandler<HTMLDivElement> | undefined` | â |  |
| `onMouseMove` | `MouseEventHandler<HTMLDivElement> | undefined` | â |  |
| `onMouseMoveCapture` | `MouseEventHandler<HTMLDivElement> | undefined` | â |  |
| `onMouseOut` | `MouseEventHandler<HTMLDivElement> | undefined` | â |  |
| `onMouseOutCapture` | `MouseEventHandler<HTMLDivElement> | undefined` | â |  |
| `onMouseOver` | `MouseEventHandler<HTMLDivElement> | undefined` | â |  |
| `onMouseOverCapture` | `MouseEventHandler<HTMLDivElement> | undefined` | â |  |
| `onMouseUp` | `MouseEventHandler<HTMLDivElement> | undefined` | â |  |
| `onMouseUpCapture` | `MouseEventHandler<HTMLDivElement> | undefined` | â |  |
| `onPointerCancel` | `PointerEventHandler<HTMLDivElement> | undefined` | â |  |
| `onPointerCancelCapture` | `PointerEventHandler<HTMLDivElement> | undefined` | â |  |
| `onPointerDown` | `PointerEventHandler<HTMLDivElement> | undefined` | â |  |
| `onPointerDownCapture` | `PointerEventHandler<HTMLDivElement> | undefined` | â |  |
| `onPointerEnter` | `PointerEventHandler<HTMLDivElement> | undefined` | â |  |
| `onPointerLeave` | `PointerEventHandler<HTMLDivElement> | undefined` | â |  |
| `onPointerMove` | `PointerEventHandler<HTMLDivElement> | undefined` | â |  |
| `onPointerMoveCapture` | `PointerEventHandler<HTMLDivElement> | undefined` | â |  |
| `onPointerOut` | `PointerEventHandler<HTMLDivElement> | undefined` | â |  |
| `onPointerOutCapture` | `PointerEventHandler<HTMLDivElement> | undefined` | â |  |
| `onPointerOver` | `PointerEventHandler<HTMLDivElement> | undefined` | â |  |
| `onPointerOverCapture` | `PointerEventHandler<HTMLDivElement> | undefined` | â |  |
| `onPointerUp` | `PointerEventHandler<HTMLDivElement> | undefined` | â |  |
| `onPointerUpCapture` | `PointerEventHandler<HTMLDivElement> | undefined` | â |  |
| `onScroll` | `UIEventHandler<HTMLDivElement> | undefined` | â |  |
| `onScrollCapture` | `UIEventHandler<HTMLDivElement> | undefined` | â |  |
| `onTouchCancel` | `TouchEventHandler<HTMLDivElement> | undefined` | â |  |
| `onTouchCancelCapture` | `TouchEventHandler<HTMLDivElement> | undefined` | â |  |
| `onTouchEnd` | `TouchEventHandler<HTMLDivElement> | undefined` | â |  |
| `onTouchEndCapture` | `TouchEventHandler<HTMLDivElement> | undefined` | â |  |
| `onTouchMove` | `TouchEventHandler<HTMLDivElement> | undefined` | â |  |
| `onTouchMoveCapture` | `TouchEventHandler<HTMLDivElement> | undefined` | â |  |
| `onTouchStart` | `TouchEventHandler<HTMLDivElement> | undefined` | â |  |
| `onTouchStartCapture` | `TouchEventHandler<HTMLDivElement> | undefined` | â |  |
| `onTransitionCancel` | `TransitionEventHandler<HTMLDivElement> | undefined` | â |  |
| `onTransitionCancelCapture` | `TransitionEventHandler<HTMLDivElement> | undefined` | â |  |
| `onTransitionEnd` | `TransitionEventHandler<HTMLDivElement> | undefined` | â |  |
| `onTransitionEndCapture` | `TransitionEventHandler<HTMLDivElement> | undefined` | â |  |
| `onTransitionRun` | `TransitionEventHandler<HTMLDivElement> | undefined` | â |  |
| `onTransitionRunCapture` | `TransitionEventHandler<HTMLDivElement> | undefined` | â |  |
| `onTransitionStart` | `TransitionEventHandler<HTMLDivElement> | undefined` | â |  |
| `onTransitionStartCapture` | `TransitionEventHandler<HTMLDivElement> | undefined` | â |  |
| `onWheel` | `WheelEventHandler<HTMLDivElement> | undefined` | â |  |
| `onWheelCapture` | `WheelEventHandler<HTMLDivElement> | undefined` | â |  |
| `placement` | `ToastPlacement | undefined` | "bottom" | Placement of the toast container on the page. |
| `translate` | `"yes" | "no" | undefined` | â |  |

### ToastQueue

#### Toast Options

| Name | Type | Description |
|------|------|-------------|
| `actionLabel` | `string | undefined` | A label for the action button within the toast. |
| `onAction` | `(() => void) | undefined` | Handler that is called when the action button is pressed. |
| `shouldCloseOnAction` | `boolean | undefined` | Whether the toast should automatically close when an action is performed. |
| `onClose` | `(() => void) | undefined` | Handler that is called when the toast is closed, either by the user or after a timeout. |
| `timeout` | `number | undefined` | A timeout to automatically close the toast after, in milliseconds. |
| `id` | `string | undefined` | The element's unique identifier. See [MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/id). |
