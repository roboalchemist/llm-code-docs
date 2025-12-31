# Source: https://reactnative.dev/docs/touchablehighlight.md

# TouchableHighlight

tip

If you're looking for a more extensive and future-proof way to handle touch-based input, check out the [Pressable](/docs/pressable.md) API.

A wrapper for making views respond properly to touches. On press down, the opacity of the wrapped view is decreased, which allows the underlay color to show through, darkening or tinting the view.

The underlay comes from wrapping the child in a new View, which can affect layout, and sometimes cause unwanted visual artifacts if not used correctly, for example if the backgroundColor of the wrapped view isn't explicitly set to an opaque color.

TouchableHighlight must have one child (not zero or more than one). If you wish to have several child components, wrap them in a View.

tsx

```
function MyComponent(props: MyComponentProps) {
  return (
    <View {...props} style={{flex: 1, backgroundColor: '#fff'}}>
      <Text>My Component</Text>
    </View>
  );
}

<TouchableHighlight
  activeOpacity={0.6}
  underlayColor="#DDDDDD"
  onPress={() => alert('Pressed!')}>
  <MyComponent />
</TouchableHighlight>;
```

## Example[​](#example "Direct link to Example")

***

# Reference

## Props[​](#props "Direct link to Props")

### [TouchableWithoutFeedback Props](/docs/touchablewithoutfeedback.md#props)[​](#touchablewithoutfeedback-props "Direct link to touchablewithoutfeedback-props")

Inherits [TouchableWithoutFeedback Props](/docs/touchablewithoutfeedback.md#props).

***

### `activeOpacity`[​](#activeopacity "Direct link to activeopacity")

Determines what the opacity of the wrapped view should be when touch is active. The value should be between 0 and 1. Defaults to 0.85. Requires `underlayColor` to be set.

| Type   |
| ------ |
| number |

***

### `onHideUnderlay`[​](#onhideunderlay "Direct link to onhideunderlay")

Called immediately after the underlay is hidden.

| Type     |
| -------- |
| function |

***

### `onShowUnderlay`[​](#onshowunderlay "Direct link to onshowunderlay")

Called immediately after the underlay is shown.

| Type     |
| -------- |
| function |

***

### `ref`[​](#ref "Direct link to ref")

A ref setter that will be assigned an [element node](/docs/element-nodes.md) when mounted.

***

### `style`[​](#style "Direct link to style")

| Type        |
| ----------- |
| View\.style |

***

### `underlayColor`[​](#underlaycolor "Direct link to underlaycolor")

The color of the underlay that will show through when the touch is active.

| Type                     |
| ------------------------ |
| [color](/docs/colors.md) |

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

### `testOnly_pressed`[​](#testonly_pressed "Direct link to testonly_pressed")

Handy for snapshot tests.

| Type |
| ---- |
| bool |
