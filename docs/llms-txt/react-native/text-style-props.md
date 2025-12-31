# Source: https://reactnative.dev/docs/text-style-props.md

# Text Style Props

### Example[​](#example "Direct link to Example")

<!-- -->

* TypeScript
* JavaScript

# Reference

## Props[​](#props "Direct link to Props")

### `color`[​](#color "Direct link to color")

| Type                     |
| ------------------------ |
| [color](/docs/colors.md) |

***

### `fontFamily`[​](#fontfamily "Direct link to fontfamily")

| Type   |
| ------ |
| string |

The generic font families `system-ui`, `ui-sans-serif`, `ui-serif`, `ui-monospace`, and `ui-rounded` are supported on iOS.

***

### `fontSize`[​](#fontsize "Direct link to fontsize")

| Type   |
| ------ |
| number |

***

### `fontStyle`[​](#fontstyle "Direct link to fontstyle")

| Type                         |
| ---------------------------- |
| enum(`'normal'`, `'italic'`) |

***

### `fontWeight`[​](#fontweight "Direct link to fontweight")

Specifies font weight. The values `'normal'` and `'bold'` are supported for most fonts. Not all fonts have a variant for each of the numeric values, in that case the closest one is chosen.

| Type                                                                                                                  | Default    |
| --------------------------------------------------------------------------------------------------------------------- | ---------- |
| enum(`'normal'`, `'bold'`, `'100'`, `'200'`, `'300'`, `'400'`, `'500'`, `'600'`, `'700'`, `'800'`, `'900'`) or number | `'normal'` |

***

### `includeFontPadding`Android[​](#includefontpadding-android "Direct link to includefontpadding-android")

Set to `false` to remove extra font padding intended to make space for certain ascenders / descenders. With some fonts, this padding can make text look slightly misaligned when centered vertically. For best results also set `textAlignVertical` to `center`.

| Type | Default |
| ---- | ------- |
| bool | `true`  |

***

### `fontVariant`[​](#fontvariant "Direct link to fontvariant")

Allows you to set all the font variants for a font. Can be set by using an array of enums or a space-separated string e.g. `'small-caps common-ligatures'`.

| Type                                                                                                                 | Default |
| -------------------------------------------------------------------------------------------------------------------- | ------- |
| array of enum(`'small-caps'`, `'oldstyle-nums'`, `'lining-nums'`, `'tabular-nums'`, `'proportional-nums'`) or string | `[]`    |

***

### `letterSpacing`[​](#letterspacing "Direct link to letterspacing")

Increase or decrease the spacing between characters. By default there is no extra letter spacing.

| Type   |
| ------ |
| number |

***

### `lineHeight`[​](#lineheight "Direct link to lineheight")

Numeric value that controls the vertical spacing between lines of text within a text element. It specifies the distance between the baselines of consecutive lines of text.

| Type   |
| ------ |
| number |

***

### `textAlign`[​](#textalign "Direct link to textalign")

Specifies text alignment. On Android, the value 'justify' is only supported on Oreo (8.0) or above (API level >= 26). The value will fallback to `left` on lower Android versions.

| Type                                                         | Default  |
| ------------------------------------------------------------ | -------- |
| enum(`'auto'`, `'left'`, `'right'`, `'center'`, `'justify'`) | `'auto'` |

***

### `textAlignVertical`Android[​](#textalignvertical-android "Direct link to textalignvertical-android")

| Type                                            | Default  |
| ----------------------------------------------- | -------- |
| enum(`'auto'`, `'top'`, `'bottom'`, `'center'`) | `'auto'` |

***

### `textDecorationColor`iOS[​](#textdecorationcolor-ios "Direct link to textdecorationcolor-ios")

| Type                     |
| ------------------------ |
| [color](/docs/colors.md) |

***

### `textDecorationLine`[​](#textdecorationline "Direct link to textdecorationline")

| Type                                                                        | Default  |
| --------------------------------------------------------------------------- | -------- |
| enum(`'none'`, `'underline'`, `'line-through'`, `'underline line-through'`) | `'none'` |

***

### `textDecorationStyle`iOS[​](#textdecorationstyle-ios "Direct link to textdecorationstyle-ios")

| Type                                                | Default   |
| --------------------------------------------------- | --------- |
| enum(`'solid'`, `'double'`, `'dotted'`, `'dashed'`) | `'solid'` |

***

### `textShadowColor`[​](#textshadowcolor "Direct link to textshadowcolor")

| Type                     |
| ------------------------ |
| [color](/docs/colors.md) |

***

### `textShadowOffset`[​](#textshadowoffset "Direct link to textshadowoffset")

| Type                                        |
| ------------------------------------------- |
| object: `{width?: number, height?: number}` |

***

### `textShadowRadius`[​](#textshadowradius "Direct link to textshadowradius")

| Type   |
| ------ |
| number |

***

### `textTransform`[​](#texttransform "Direct link to texttransform")

| Type                                                         | Default  |
| ------------------------------------------------------------ | -------- |
| enum(`'none'`, `'uppercase'`, `'lowercase'`, `'capitalize'`) | `'none'` |

***

### `verticalAlign`Android[​](#verticalalign-android "Direct link to verticalalign-android")

| Type                                            | Default  |
| ----------------------------------------------- | -------- |
| enum(`'auto'`, `'top'`, `'bottom'`, `'middle'`) | `'auto'` |

***

### `writingDirection`iOS[​](#writingdirection-ios "Direct link to writingdirection-ios")

| Type                             | Default  |
| -------------------------------- | -------- |
| enum(`'auto'`, `'ltr'`, `'rtl'`) | `'auto'` |

***

### `userSelect`[​](#userselect "Direct link to userselect")

It allows the user to select text and to use the native copy and paste functionality. Has precedence over the `selectable` prop.

| Type                                                     | Default |
| -------------------------------------------------------- | ------- |
| enum(`'auto'`, `'text'`, `'none'`, `'contain'`, `'all'`) | `none`  |
