# Source: https://reactnative.dev/docs/shadow-props.md

# Shadow Props

* TypeScript
* JavaScript

***

# Reference

There are 3 sets of shadow APIs in React Native:

* `boxShadow`: A View style prop and a spec-compliant implementation of the [web style prop of the same name](https://developer.mozilla.org/en-US/docs/Web/CSS/box-shadow).
* `dropShadow`: A specific filter function available as part of the [`filter`](/docs/view-style-props.md#filter) View style prop.
* Various `shadow` props (`shadowColor`, `shadowOffset`, `shadowOpacity`, `shadowRadius`): These map directly to their native counterparts exposed by the platform-level APIs.

The difference between `dropShadow` and `boxShadow` are as follows:

* `dropShadow` exists as part of `filter`, whereas `boxShadow` is a standalone style prop.
* `dropShadow` is an alpha mask, so only pixels with a positive alpha value will "cast" a shadow. `boxShadow` will cast around the border box of the element no matter it's contents (unless it is inset).
* `dropShadow` is only available on Android, `boxShadow` is available on iOS and Android.
* `dropShadow` cannot be inset like `boxShadow`.
* `dropShadow` does not have the `spreadDistance` argument like `boxShadow`.

Both `boxShadow` and `dropShadow` are generally more capable than the `shadow` props. The `shadow` props, however, map to native platform-level APIs, so if you only need a straightforward shadow these props are recommended. Note that only `shadowColor` works on both Android and iOS, all other `shadow` props only work on iOS.

## Props[​](#props "Direct link to Props")

### `boxShadow`[​](#boxshadow "Direct link to boxshadow")

See [View Style Props](/docs/view-style-props.md#boxshadow) for documentation.

### `dropShadow`Android[​](#dropshadow-android "Direct link to dropshadow-android")

See [View Style Props](/docs/view-style-props.md#filter) for documentation.

### `shadowColor`[​](#shadowcolor "Direct link to shadowcolor")

Sets the drop shadow color.

This property will only work on Android API 28 and above. For similar functionality on lower Android APIs, use the [`elevation` property](/docs/view-style-props.md#elevation-android).

| Type                     |
| ------------------------ |
| [color](/docs/colors.md) |

***

### `shadowOffset`iOS[​](#shadowoffset-ios "Direct link to shadowoffset-ios")

Sets the drop shadow offset.

| Type                                     |
| ---------------------------------------- |
| object: `{width: number,height: number}` |

***

### `shadowOpacity`iOS[​](#shadowopacity-ios "Direct link to shadowopacity-ios")

Sets the drop shadow opacity (multiplied by the color's alpha component).

| Type   |
| ------ |
| number |

***

### `shadowRadius`iOS[​](#shadowradius-ios "Direct link to shadowradius-ios")

Sets the drop shadow blur radius.

| Type   |
| ------ |
| number |
