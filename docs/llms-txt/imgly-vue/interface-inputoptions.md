# Interface: InputOptions

Represents options for an input.

The `InputOptions` interface provides a set of properties that control the behavior and appearance of an input. These options include settings for the input label, input label position, value, value setter, disabled state, and suffix.

## Extended by[#](#extended-by)

*   [`CheckboxOptions`](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/checkboxoptions/)
*   [`ColorInputOptions`](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/colorinputoptions/)
*   [`NumberInputOptions`](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/numberinputoptions/)
*   [`SelectOptions`](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/selectoptions/)
*   [`SliderOptions`](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/slideroptions/)
*   [`TextAreaOptions`](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/textareaoptions/)
*   [`TextInputOptions`](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/textinputoptions/)

## Type Parameters[#](#type-parameters)

| Type Parameter | Default type |
| --- | --- |
| `T` | \- |
| `P` | `"top"` |

## Properties[#](#properties)

| Property | Type |
| --- | --- |
| `inputLabel?` | `string` |
| `inputLabelPosition?` | `P` |
| `value` | `T` |
| `setValue` | (`value`) => `void` |
| `isDisabled?` | `boolean` |
| `suffix?` | `Partial` |

---



[Source](https:/img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/htmlcreativeenginecanvaselement)