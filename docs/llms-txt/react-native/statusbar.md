# Source: https://reactnative.dev/docs/statusbar.md

# StatusBar

Component to control the app's status bar. The status bar is the zone, typically at the top of the screen, that displays the current time, Wi-Fi and cellular network information, battery level and/or other status icons.

### Usage with Navigator[​](#usage-with-navigator "Direct link to Usage with Navigator")

It is possible to have multiple `StatusBar` components mounted at the same time. The props will be merged in the order the `StatusBar` components were mounted.

* TypeScript
* JavaScript

### Imperative API[​](#imperative-api "Direct link to Imperative API")

For cases where using a component is not ideal, there is also an imperative API exposed as static functions on the component. It is however not recommended to use the static API and the component for the same prop because any value set by the static API will get overridden by the one set by the component in the next render.

***

# Reference

## Constants[​](#constants "Direct link to Constants")

### `currentHeight`Android[​](#currentheight-android "Direct link to currentheight-android")

The height of the status bar, which includes the notch height, if present.

***

## Props[​](#props "Direct link to Props")

### `animated`[​](#animated "Direct link to animated")

If the transition between status bar property changes should be animated. Supported for `backgroundColor`, `barStyle` and `hidden` properties.

| Type    | Required | Default |
| ------- | -------- | ------- |
| boolean | No       | `false` |

***

### `backgroundColor`Android[​](#backgroundcolor-android "Direct link to backgroundcolor-android")

The background color of the status bar.

warning

Due to edge-to-edge enforcement introduced in Android 15, setting background color of the status bar is deprecated in API level 35 and setting it will have no effect. You can read more about our [edge-to-edge recommendations here](https://github.com/react-native-community/discussions-and-proposals/discussions/827).

| Type                     | Required | Default                                                                |
| ------------------------ | -------- | ---------------------------------------------------------------------- |
| [color](/docs/colors.md) | No       | default system StatusBar background color, or `'black'` if not defined |

***

### `barStyle`[​](#barstyle "Direct link to barstyle")

Sets the color of the status bar text.

On Android, this will only have an impact on API versions 23 and above.

| Type                                                | Required | Default     |
| --------------------------------------------------- | -------- | ----------- |
| [StatusBarStyle](/docs/statusbar.md#statusbarstyle) | No       | `'default'` |

***

### `hidden`[​](#hidden "Direct link to hidden")

If the status bar is hidden.

| Type    | Required | Default |
| ------- | -------- | ------- |
| boolean | No       | `false` |

***

### `networkActivityIndicatorVisible`iOS[​](#networkactivityindicatorvisible-ios "Direct link to networkactivityindicatorvisible-ios")

If the network activity indicator should be visible.

| Type    | Default |
| ------- | ------- |
| boolean | `false` |

***

### `showHideTransition`iOS[​](#showhidetransition-ios "Direct link to showhidetransition-ios")

The transition effect when showing and hiding the status bar using the `hidden` prop.

| Type                                                        | Default  |
| ----------------------------------------------------------- | -------- |
| [StatusBarAnimation](/docs/statusbar.md#statusbaranimation) | `'fade'` |

***

### `translucent`Android[​](#translucent-android "Direct link to translucent-android")

If the status bar is translucent. When translucent is set to `true`, the app will draw under the status bar. This is useful when using a semi transparent status bar color.

warning

Due to edge-to-edge enforcement introduced in Android 15, setting the status bar as translucent is deprecated in API level 35 and setting it will have no effect. You can read more about our [edge-to-edge recommendations here](https://github.com/react-native-community/discussions-and-proposals/discussions/827).

| Type    | Default |
| ------- | ------- |
| boolean | `false` |

## Methods[​](#methods "Direct link to Methods")

### `popStackEntry()`[​](#popstackentry "Direct link to popstackentry")

tsx

```
static popStackEntry(entry: StatusBarProps);
```

Get and remove the last StatusBar entry from the stack.

**Parameters:**

| Name          | Type | Description                           |
| ------------- | ---- | ------------------------------------- |
| entryRequired | any  | Entry returned from `pushStackEntry`. |

***

### `pushStackEntry()`[​](#pushstackentry "Direct link to pushstackentry")

tsx

```
static pushStackEntry(props: StatusBarProps): StatusBarProps;
```

Push a StatusBar entry onto the stack. The return value should be passed to `popStackEntry` when complete.

**Parameters:**

| Name          | Type | Description                                                      |
| ------------- | ---- | ---------------------------------------------------------------- |
| propsRequired | any  | Object containing the StatusBar props to use in the stack entry. |

***

### `replaceStackEntry()`[​](#replacestackentry "Direct link to replacestackentry")

tsx

```
static replaceStackEntry(
  entry: StatusBarProps,
  props: StatusBarProps
): StatusBarProps;
```

Replace an existing StatusBar stack entry with new props.

**Parameters:**

| Name          | Type | Description                                                                  |
| ------------- | ---- | ---------------------------------------------------------------------------- |
| entryRequired | any  | Entry returned from `pushStackEntry` to replace.                             |
| propsRequired | any  | Object containing the StatusBar props to use in the replacement stack entry. |

***

### `setBackgroundColor()`Android[​](#setbackgroundcolor-android "Direct link to setbackgroundcolor-android")

tsx

```
static setBackgroundColor(color: ColorValue, animated?: boolean);
```

Set the background color for the status bar.

warning

Due to edge-to-edge enforcement introduced in Android 15, setting background color of the status bar is deprecated in API level 35 and setting it will have no effect. You can read more about our [edge-to-edge recommendations here](https://github.com/react-native-community/discussions-and-proposals/discussions/827).

**Parameters:**

| Name          | Type    | Description               |
| ------------- | ------- | ------------------------- |
| colorRequired | string  | Background color.         |
| animated      | boolean | Animate the style change. |

***

### `setBarStyle()`[​](#setbarstyle "Direct link to setbarstyle")

tsx

```
static setBarStyle(style: StatusBarStyle, animated?: boolean);
```

Set the status bar style.

**Parameters:**

| Name          | Type                                                | Description               |
| ------------- | --------------------------------------------------- | ------------------------- |
| styleRequired | [StatusBarStyle](/docs/statusbar.md#statusbarstyle) | Status bar style to set.  |
| animated      | boolean                                             | Animate the style change. |

***

### `setHidden()`[​](#sethidden "Direct link to sethidden")

tsx

```
static setHidden(hidden: boolean, animation?: StatusBarAnimation);
```

Show or hide the status bar.

**Parameters:**

| Name           | Type                                                        | Description                                             |
| -------------- | ----------------------------------------------------------- | ------------------------------------------------------- |
| hiddenRequired | boolean                                                     | Hide the status bar.                                    |
| animationiOS   | [StatusBarAnimation](/docs/statusbar.md#statusbaranimation) | Animation when changing the status bar hidden property. |

***

### `setNetworkActivityIndicatorVisible()`iOS[​](#setnetworkactivityindicatorvisible-ios "Direct link to setnetworkactivityindicatorvisible-ios")

tsx

```
static setNetworkActivityIndicatorVisible(visible: boolean);
```

Control the visibility of the network activity indicator.

**Parameters:**

| Name            | Type    | Description         |
| --------------- | ------- | ------------------- |
| visibleRequired | boolean | Show the indicator. |

***

### `setTranslucent()`Android[​](#settranslucent-android "Direct link to settranslucent-android")

tsx

```
static setTranslucent(translucent: boolean);
```

Control the translucency of the status bar.

warning

Due to edge-to-edge enforcement introduced in Android 15, setting the status bar as translucent is deprecated in API level 35 and setting it will have no effect. You can read more about our [edge-to-edge recommendations here](https://github.com/react-native-community/discussions-and-proposals/discussions/827).

**Parameters:**

| Name                | Type    | Description         |
| ------------------- | ------- | ------------------- |
| translucentRequired | boolean | Set as translucent. |

## Type Definitions[​](#type-definitions "Direct link to Type Definitions")

### StatusBarAnimation[​](#statusbaranimation "Direct link to StatusBarAnimation")

Status bar animation type for transitions on the iOS.

| Type |
| ---- |
| enum |

**Constants:**

| Value     | Type   | Description     |
| --------- | ------ | --------------- |
| `'fade'`  | string | Fade animation  |
| `'slide'` | string | Slide animation |
| `'none'`  | string | No animation    |

***

### StatusBarStyle[​](#statusbarstyle "Direct link to StatusBarStyle")

Status bar style type.

| Type |
| ---- |
| enum |

**Constants:**

| Value             | Type   | Description                                                |
| ----------------- | ------ | ---------------------------------------------------------- |
| `'default'`       | string | Default status bar style (dark for iOS, light for Android) |
| `'light-content'` | string | White texts and icons                                      |
| `'dark-content'`  | string | Dark texts and icons (requires API>=23 on Android)         |
