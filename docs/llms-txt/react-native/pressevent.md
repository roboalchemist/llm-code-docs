# Source: https://reactnative.dev/docs/pressevent.md

# PressEvent Object Type

`PressEvent` object is returned in the callback as a result of user press interaction, for example `onPress` in [Button](/docs/button.md) component.

## Example[​](#example "Direct link to Example")

js

```
{
    changedTouches: [PressEvent],
    identifier: 1,
    locationX: 8,
    locationY: 4.5,
    pageX: 24,
    pageY: 49.5,
    target: 1127,
    timestamp: 85131876.58868201,
    touches: []
}
```

## Keys and values[​](#keys-and-values "Direct link to Keys and values")

### `changedTouches`[​](#changedtouches "Direct link to changedtouches")

Array of all PressEvents that have changed since the last event.

| Type                 | Optional |
| -------------------- | -------- |
| array of PressEvents | No       |

### `force`iOS[​](#force-ios "Direct link to force-ios")

Amount of force used during the 3D Touch press. Returns the float value in range from `0.0` to `1.0`.

| Type   | Optional |
| ------ | -------- |
| number | Yes      |

### `identifier`[​](#identifier "Direct link to identifier")

Unique numeric identifier assigned to the event.

| Type   | Optional |
| ------ | -------- |
| number | No       |

### `locationX`[​](#locationx "Direct link to locationx")

Touch origin X coordinate inside touchable area (relative to the element).

| Type   | Optional |
| ------ | -------- |
| number | No       |

### `locationY`[​](#locationy "Direct link to locationy")

Touch origin Y coordinate inside touchable area (relative to the element).

| Type   | Optional |
| ------ | -------- |
| number | No       |

### `pageX`[​](#pagex "Direct link to pagex")

Touch origin X coordinate on the screen (relative to the root view).

| Type   | Optional |
| ------ | -------- |
| number | No       |

### `pageY`[​](#pagey "Direct link to pagey")

Touch origin Y coordinate on the screen (relative to the root view).

| Type   | Optional |
| ------ | -------- |
| number | No       |

### `target`[​](#target "Direct link to target")

The node id of the element receiving the PressEvent.

| Type                        | Optional |
| --------------------------- | -------- |
| number, `null`, `undefined` | No       |

### `timestamp`[​](#timestamp "Direct link to timestamp")

Timestamp value when a PressEvent occurred. Value is represented in milliseconds.

| Type   | Optional |
| ------ | -------- |
| number | No       |

### `touches`[​](#touches "Direct link to touches")

Array of all current PressEvents on the screen.

| Type                 | Optional |
| -------------------- | -------- |
| array of PressEvents | No       |

## Used by[​](#used-by "Direct link to Used by")

* [`Button`](/docs/button.md)
* [`PanResponder`](/docs/panresponder.md)
* [`Pressable`](/docs/pressable.md)
* [`ScrollView`](/docs/scrollview.md)
* [`Text`](/docs/text.md)
* [`TextInput`](/docs/textinput.md)
* [`TouchableHighlight`](/docs/touchablenativefeedback.md)
* [`TouchableOpacity`](/docs/touchablewithoutfeedback.md)
* [`TouchableNativeFeedback`](/docs/touchablenativefeedback.md)
* [`TouchableWithoutFeedback`](/docs/touchablewithoutfeedback.md)
* [`View`](/docs/view.md)
