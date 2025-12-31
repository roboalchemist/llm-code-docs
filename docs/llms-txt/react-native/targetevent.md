# Source: https://reactnative.dev/docs/targetevent.md

# TargetEvent Object Type

`TargetEvent` object is returned in the callback as a result of focus change, for example `onFocus` or `onBlur` in the [TextInput](/docs/textinput.md) component.

## Example[​](#example "Direct link to Example")

```
{
    target: 1127
}
```

## Keys and values[​](#keys-and-values "Direct link to Keys and values")

### `target`[​](#target "Direct link to target")

The node id of the element receiving the TargetEvent.

| Type                        | Optional |
| --------------------------- | -------- |
| number, `null`, `undefined` | No       |

## Used by[​](#used-by "Direct link to Used by")

* [`TextInput`](/docs/textinput.md)
* [`TouchableWithoutFeedback`](/docs/touchablewithoutfeedback.md)
