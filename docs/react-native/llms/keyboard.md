# Source: https://reactnative.dev/docs/keyboard.md

# Keyboard

`Keyboard` module to control keyboard events.

### Usage[​](#usage "Direct link to Usage")

The Keyboard module allows you to listen for native events and react to them, as well as make changes to the keyboard, like dismissing it.

***

# Reference

## Methods[​](#methods "Direct link to Methods")

### `addListener()`[​](#addlistener "Direct link to addlistener")

tsx

```
static addListener: (
  eventType: KeyboardEventName,
  listener: KeyboardEventListener,
) => EmitterSubscription;
```

The `addListener` function connects a JavaScript function to an identified native keyboard notification event.

This function then returns the reference to the listener.

**Parameters:**

| Name              | Type     | Description                                                                    |
| ----------------- | -------- | ------------------------------------------------------------------------------ |
| eventNameRequired | string   | The string that identifies the event you're listening for. See the list below. |
| callbackRequired  | function | The function to be called when the event fires                                 |

**`eventName`**

This can be any of the following:

* `keyboardWillShow`
* `keyboardDidShow`
* `keyboardWillHide`
* `keyboardDidHide`
* `keyboardWillChangeFrame`
* `keyboardDidChangeFrame`

note

Only `keyboardDidShow` and `keyboardDidHide` events are available on Android. The events will not be fired when using Android 10 or below if your activity has `android:windowSoftInputMode` set to `adjustResize` or `adjustNothing`.

***

### `dismiss()`[​](#dismiss "Direct link to dismiss")

tsx

```
static dismiss();
```

Dismisses the active keyboard and removes focus.

***

### `scheduleLayoutAnimation`[​](#schedulelayoutanimation "Direct link to schedulelayoutanimation")

tsx

```
static scheduleLayoutAnimation(event: KeyboardEvent);
```

Useful for syncing TextInput (or other keyboard accessory view) size of position changes with keyboard movements.

***

### `isVisible()`[​](#isvisible "Direct link to isvisible")

tsx

```
static isVisible(): boolean;
```

Whether the keyboard is last known to be visible.

***

### `metrics()`[​](#metrics "Direct link to metrics")

tsx

```
static metrics(): KeyboardMetrics | undefined;
```

Return the metrics of the soft-keyboard if visible.
