# Source: https://reactnative.dev/docs/keyboardavoidingview.md

# KeyboardAvoidingView

This component will automatically adjust its height, position, or bottom padding based on the keyboard height to remain visible while the virtual keyboard is displayed.

## Example[​](#example "Direct link to Example")

***

# Reference

## Props[​](#props "Direct link to Props")

### [View Props](/docs/view.md#props)[​](#view-props "Direct link to view-props")

Inherits [View Props](/docs/view.md#props).

***

### `behavior`[​](#behavior "Direct link to behavior")

Specify how to react to the presence of the keyboard.

note

Android and iOS both interact with this prop differently. On both iOS and Android, setting `behavior` is recommended.

| Type                                        |
| ------------------------------------------- |
| enum(`'height'`, `'position'`, `'padding'`) |

***

### `contentContainerStyle`[​](#contentcontainerstyle "Direct link to contentcontainerstyle")

The style of the content container (View) when behavior is `'position'`.

| Type                                    |
| --------------------------------------- |
| [View Style](/docs/view-style-props.md) |

***

### `enabled`[​](#enabled "Direct link to enabled")

Enabled or disabled KeyboardAvoidingView.

| Type    | Default |
| ------- | ------- |
| boolean | `true`  |

***

### `keyboardVerticalOffset`[​](#keyboardverticaloffset "Direct link to keyboardverticaloffset")

This is the distance between the top of the user screen and the react native view, may be non-zero in some use cases.

| Type   | Default |
| ------ | ------- |
| number | `0`     |
