# Source: https://reactnative.dev/docs/dropshadowvalue.md

# DropShadowValue Object Type

The `DropShadowValue` object is taken by the [`filter`](/docs/view-style-props.md#filter) style prop for the `dropShadow` function. It is comprised of 2 or 3 lengths and an optional color. These values collectively define the drop shadow's color, position, and blurriness.

## Example[​](#example "Direct link to Example")

js

```
{
  offsetX: 10,
  offsetY: -3,
  standardDeviation: '15px',
  color: 'blue',
}
```

## Keys and values[​](#keys-and-values "Direct link to Keys and values")

### `offsetX`[​](#offsetx "Direct link to offsetx")

The offset on the x-axis. This can be positive or negative. A positive value indicates right and negative indicates left.

| Type             | Optional |
| ---------------- | -------- |
| number \| string | No       |

### `offsetY`[​](#offsety "Direct link to offsety")

The offset on the y-axis. This can be positive or negative. A positive value indicates up and negative indicates down.

| Type             | Optional |
| ---------------- | -------- |
| number \| string | No       |

### `standardDeviation`[​](#standarddeviation "Direct link to standarddeviation")

Represents the standard deviation used in the [Gaussian blur](https://en.wikipedia.org/wiki/Gaussian_blur) algorithm. The larger the value the blurrier the shadow is. Only non-negative values are valid. The default is 0.

| Type             | Optional |
| ---------------- | -------- |
| number \| string | Yes      |

### `color`[​](#color "Direct link to color")

The color of the shadow. The default is `black`.

| Type                     | Optional |
| ------------------------ | -------- |
| [color](/docs/colors.md) | Yes      |

## Used by[​](#used-by "Direct link to Used by")

* [`filter`](/docs/view-style-props.md#filter)
