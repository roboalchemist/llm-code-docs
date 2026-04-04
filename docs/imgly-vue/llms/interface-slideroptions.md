# Interface: SliderOptions

Represents options for a slider.

The `SliderOptions` interface provides a set of properties that control the behavior and appearance of a slider. These options include settings for the input label, input label position, value, value setter, disabled state, minimum value, maximum value, step value, centered state, and suffix.

## Extends[#](#extends)

*   [`InputOptions`](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/inputoptions/)<`number`\>

## Properties[#](#properties)

| Property | Type | Inherited from |
| --- | --- | --- |
| `inputLabel?` | `string` | `string`\[\] |
| `inputLabelPosition?` | `"top"` | `"left"` |
| `value` | `number` | [`InputOptions`](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/inputoptions/).[`value`](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/inputoptions/) |
| `setValue` | (`value`) => `void` | [`InputOptions`](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/inputoptions/).[`setValue`](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/inputoptions/) |
| `isDisabled?` | `boolean` | [`InputOptions`](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/inputoptions/).[`isDisabled`](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/inputoptions/) |
| `suffix?` | `Partial` | [`InputOptions`](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/inputoptions/).[`suffix`](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/inputoptions/) |
| `min` | `number` | \- |
| `max` | `number` | \- |
| `step?` | `number` | \- |
| `centered?` | `boolean` | \- |

---



[Source](https:/img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/selectvalue)