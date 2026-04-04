# Source: https://reactnative.dev/docs/modal.md

# Modal

The Modal component is a basic way to present content above an enclosing view.

## Example[​](#example "Direct link to Example")

***

# Reference

## Props[​](#props "Direct link to Props")

### [View Props](/docs/view.md#props)[​](#view-props "Direct link to view-props")

Inherits [View Props](/docs/view.md#props).

***

### 🗑️ `animated`[​](#️-animated "Direct link to ️-animated")

Deprecated

Use the [`animationType`](/docs/modal.md#animationtype) prop instead.

***

### `animationType`[​](#animationtype "Direct link to animationtype")

The `animationType` prop controls how the modal animates.

Possible values:

* `slide` slides in from the bottom
* `fade` fades into view
* `none` appears without an animation

| Type                                | Default |
| ----------------------------------- | ------- |
| enum(`'none'`, `'slide'`, `'fade'`) | `none`  |

***

### `backdropColor`[​](#backdropcolor "Direct link to backdropcolor")

The `backdropColor` of the modal (or background color of the modal's container.) Defaults to `white` if not provided and transparent is `false`. Ignored if `transparent` is `true`.

| Type                     | Default |
| ------------------------ | ------- |
| [color](/docs/colors.md) | white   |

***

### `hardwareAccelerated`Android[​](#hardwareaccelerated-android "Direct link to hardwareaccelerated-android")

The `hardwareAccelerated` prop controls whether to force hardware acceleration for the underlying window.

| Type | Default |
| ---- | ------- |
| bool | `false` |

***

### `navigationBarTranslucent`Android[​](#navigationbartranslucent-android "Direct link to navigationbartranslucent-android")

The `navigationBarTranslucent` prop determines whether your modal should go under the system navigation bar. However, `statusBarTranslucent` also needs to be set to `true` to make navigation bar translucent.

| Type | Default |
| ---- | ------- |
| bool | `false` |

***

### `onDismiss`iOS[​](#ondismiss-ios "Direct link to ondismiss-ios")

The `onDismiss` prop allows passing a function that will be called once the modal has been dismissed.

| Type     |
| -------- |
| function |

***

### `onOrientationChange`iOS[​](#onorientationchange-ios "Direct link to onorientationchange-ios")

The `onOrientationChange` callback is called when the orientation changes while the modal is being displayed. The orientation provided is only 'portrait' or 'landscape'. This callback is also called on initial render, regardless of the current orientation.

| Type     |
| -------- |
| function |

***

### `allowSwipeDismissal`iOS[​](#allowswipedismissal-ios "Direct link to allowswipedismissal-ios")

Controls whether the modal can be dismissed by swiping down on iOS. This requires you to implement the `onRequestClose` prop to handle the dismissal.

| Type | Default |
| ---- | ------- |
| bool | `false` |

***

### `ref`[​](#ref "Direct link to ref")

A ref setter that will be assigned an [element node](/docs/element-nodes.md) when mounted.

***

### `onRequestClose`[​](#onrequestclose "Direct link to onrequestclose")

The `onRequestClose` callback is called when the user taps the hardware back button on Android or the menu button on Apple TV. Because of this required prop, be aware that `BackHandler` events will not be emitted as long as the modal is open. On iOS, this callback is called when a Modal is being dismissed using a drag gesture when `presentationStyle` is `pageSheet or formSheet`. When `allowSwipeDismissal` is enabled this callback will be called after dismissing the modal.

| Type                                    |
| --------------------------------------- |
| functionRequiredAndroidTV***functioniOS |

***

### `onShow`[​](#onshow "Direct link to onshow")

The `onShow` prop allows passing a function that will be called once the modal has been shown.

| Type     |
| -------- |
| function |

***

### `presentationStyle`iOS[​](#presentationstyle-ios "Direct link to presentationstyle-ios")

The `presentationStyle` prop controls how the modal appears (generally on larger devices such as iPad or plus-sized iPhones). See <https://developer.apple.com/reference/uikit/uimodalpresentationstyle> for details.

Possible values:

* `fullScreen` covers the screen completely
* `pageSheet` covers portrait-width view centered (only on larger devices)
* `formSheet` covers narrow-width view centered (only on larger devices)
* `overFullScreen` covers the screen completely, but allows transparency

| Type                                                                   | Default                                                                          |
| ---------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| enum(`'fullScreen'`, `'pageSheet'`, `'formSheet'`, `'overFullScreen'`) | `fullScreen` if `transparent={false}`***`overFullScreen` if `transparent={true}` |

***

### `statusBarTranslucent`Android[​](#statusbartranslucent-android "Direct link to statusbartranslucent-android")

The `statusBarTranslucent` prop determines whether your modal should go under the system statusbar.

| Type | Default |
| ---- | ------- |
| bool | `false` |

***

### `supportedOrientations`iOS[​](#supportedorientations-ios "Direct link to supportedorientations-ios")

The `supportedOrientations` prop allows the modal to be rotated to any of the specified orientations. On iOS, the modal is still restricted by what's specified in your app's Info.plist's UISupportedInterfaceOrientations field.

note

When using `presentationStyle` of `pageSheet` or `formSheet`, this property will be ignored on iOS.

| Type                                                                                                           | Default        |
| -------------------------------------------------------------------------------------------------------------- | -------------- |
| array of enums(`'portrait'`, `'portrait-upside-down'`, `'landscape'`, `'landscape-left'`, `'landscape-right'`) | `['portrait']` |

***

### `transparent`[​](#transparent "Direct link to transparent")

The `transparent` prop determines whether your modal will fill the entire view. Setting this to `true` will render the modal over a transparent background.

| Type | Default |
| ---- | ------- |
| bool | `false` |

***

### `visible`[​](#visible "Direct link to visible")

The `visible` prop determines whether your modal is visible.

| Type | Default |
| ---- | ------- |
| bool | `true`  |
