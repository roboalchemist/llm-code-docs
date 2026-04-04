# Source: https://reactnative.dev/docs/layoutevent.md

# LayoutEvent Object Type

`LayoutEvent` object is returned in the callback as a result of component layout change, for example `onLayout` in [View](/docs/view.md) component.

## Example[​](#example "Direct link to Example")

js

```
{
    layout: {
        width: 520,
        height: 70.5,
        x: 0,
        y: 42.5
    },
    target: 1127
}
```

## Keys and values[​](#keys-and-values "Direct link to Keys and values")

### `height`[​](#height "Direct link to height")

Height of the component after the layout changes.

| Type   | Optional |
| ------ | -------- |
| number | No       |

### `width`[​](#width "Direct link to width")

Width of the component after the layout changes.

| Type   | Optional |
| ------ | -------- |
| number | No       |

### `x`[​](#x "Direct link to x")

Component X coordinate inside the parent component.

| Type   | Optional |
| ------ | -------- |
| number | No       |

### `y`[​](#y "Direct link to y")

Component Y coordinate inside the parent component.

| Type   | Optional |
| ------ | -------- |
| number | No       |

### `target`[​](#target "Direct link to target")

The node id of the element receiving the LayoutEvent.

| Type                        | Optional |
| --------------------------- | -------- |
| number, `null`, `undefined` | No       |

## Used by[​](#used-by "Direct link to Used by")

* [`Image`](/docs/image.md)
* [`Pressable`](/docs/pressable.md)
* [`ScrollView`](/docs/scrollview.md)
* [`Text`](/docs/text.md)
* [`TextInput`](/docs/textinput.md)
* [`TouchableWithoutFeedback`](/docs/touchablewithoutfeedback.md)
* [`View`](/docs/view.md)
