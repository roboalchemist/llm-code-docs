# Source: https://reactnative.dev/docs/refreshcontrol.md

# RefreshControl

This component is used inside a ScrollView or ListView to add pull to refresh functionality. When the ScrollView is at `scrollY: 0`, swiping down triggers an `onRefresh` event.

## Example[​](#example "Direct link to Example")

note

`refreshing` is a controlled prop, this is why it needs to be set to `true` in the `onRefresh` function otherwise the refresh indicator will stop immediately.

***

# Reference

## Props[​](#props "Direct link to Props")

### [View Props](/docs/view.md#props)[​](#view-props "Direct link to view-props")

Inherits [View Props](/docs/view.md#props).

***

### Require&#x64;**`refreshing`**[​](#requiredrefreshing "Direct link to requiredrefreshing")

Whether the view should be indicating an active refresh.

| Type    |
| ------- |
| boolean |

***

### `colors`Android[​](#colors-android "Direct link to colors-android")

The colors (at least one) that will be used to draw the refresh indicator.

| Type                               |
| ---------------------------------- |
| array of [colors](/docs/colors.md) |

***

### `enabled`Android[​](#enabled-android "Direct link to enabled-android")

Whether the pull to refresh functionality is enabled.

| Type    | Default |
| ------- | ------- |
| boolean | `true`  |

***

### `onRefresh`[​](#onrefresh "Direct link to onrefresh")

Called when the view starts refreshing.

| Type     |
| -------- |
| function |

***

### `progressBackgroundColor`Android[​](#progressbackgroundcolor-android "Direct link to progressbackgroundcolor-android")

The background color of the refresh indicator.

| Type                     |
| ------------------------ |
| [color](/docs/colors.md) |

***

### `progressViewOffset`[​](#progressviewoffset "Direct link to progressviewoffset")

Progress view top offset.

| Type   | Default |
| ------ | ------- |
| number | `0`     |

***

### `size`Android[​](#size-android "Direct link to size-android")

Size of the refresh indicator.

| Type                         | Default     |
| ---------------------------- | ----------- |
| enum(`'default'`, `'large'`) | `'default'` |

***

### `tintColor`iOS[​](#tintcolor-ios "Direct link to tintcolor-ios")

The color of the refresh indicator.

| Type                     |
| ------------------------ |
| [color](/docs/colors.md) |

***

### `title`iOS[​](#title-ios "Direct link to title-ios")

The title displayed under the refresh indicator.

| Type   |
| ------ |
| string |

***

### `titleColor`iOS[​](#titlecolor-ios "Direct link to titlecolor-ios")

The color of the refresh indicator title.

| Type                     |
| ------------------------ |
| [color](/docs/colors.md) |
