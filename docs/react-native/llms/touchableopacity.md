# Source: https://reactnative.dev/docs/touchableopacity.md

# TouchableOpacity

tip

If you're looking for a more extensive and future-proof way to handle touch-based input, check out the [Pressable](/docs/pressable.md) API.

A wrapper for making views respond properly to touches. On press down, the opacity of the wrapped view is decreased, dimming it.

Opacity is controlled by wrapping the children in an `Animated.View`, which is added to the view hierarchy. Be aware that this can affect layout.

## Example[​](#example "Direct link to Example")

***

# Reference

## Props[​](#props "Direct link to Props")

### [TouchableWithoutFeedback Props](/docs/touchablewithoutfeedback.md#props)[​](#touchablewithoutfeedback-props "Direct link to touchablewithoutfeedback-props")

Inherits [TouchableWithoutFeedback Props](/docs/touchablewithoutfeedback.md#props).

***

### `style`[​](#style "Direct link to style")

| Type                                    |
| --------------------------------------- |
| [View.style](/docs/view-style-props.md) |

***

### `activeOpacity`[​](#activeopacity "Direct link to activeopacity")

Determines what the opacity of the wrapped view should be when touch is active. Defaults to `0.2`.

| Type   |
| ------ |
| number |

***

### `hasTVPreferredFocus`iOS[​](#hastvpreferredfocus-ios "Direct link to hastvpreferredfocus-ios")

*(Apple TV only)* TV preferred focus (see documentation for the View component).

| Type |
| ---- |
| bool |

***

### `nextFocusDown`Android[​](#nextfocusdown-android "Direct link to nextfocusdown-android")

TV next focus down (see documentation for the View component).

| Type   |
| ------ |
| number |

***

### `nextFocusForward`Android[​](#nextfocusforward-android "Direct link to nextfocusforward-android")

TV next focus forward (see documentation for the View component).

| Type   |
| ------ |
| number |

***

### `nextFocusLeft`Android[​](#nextfocusleft-android "Direct link to nextfocusleft-android")

TV next focus left (see documentation for the View component).

| Type   |
| ------ |
| number |

***

### `nextFocusRight`Android[​](#nextfocusright-android "Direct link to nextfocusright-android")

TV next focus right (see documentation for the View component).

| Type   |
| ------ |
| number |

***

### `nextFocusUp`Android[​](#nextfocusup-android "Direct link to nextfocusup-android")

TV next focus up (see documentation for the View component).

| Type   |
| ------ |
| number |

***

### `ref`[​](#ref "Direct link to ref")

A ref setter that will be assigned an [element node](/docs/element-nodes.md) when mounted.
