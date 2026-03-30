# Interface: CheckboxOptions

Represents options for a checkbox.

The `CheckboxOptions` interface provides a set of properties that control the behavior and appearance of a checkbox. These options include settings for the input label, input label position, value, value setter, disabled state, icon, and suffix.

## Extends[#](#extends)

*   [`InputOptions`](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/inputoptions/)<`boolean`, `"left"` | `"right"`\>

## Properties[#](#properties)

| Property | Type | Inherited from |
| --- | --- | --- |
| `icon?` | [`CustomIcon`](https://img.ly/docs/cesdk/vue/api/cesdk-js/documentation/namespaces/userinterfaceelements/type-aliases/customicon/) | \- |
| `inputLabel?` | `string` | `string`\[\] |
| `inputLabelPosition?` | `"left"` | `"right"` |
| `value` | `boolean` | [`InputOptions`](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/inputoptions/).[`value`](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/inputoptions/) |
| `setValue` | (`value`) => `void` | [`InputOptions`](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/inputoptions/).[`setValue`](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/inputoptions/) |
| `isDisabled?` | `boolean` | [`InputOptions`](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/inputoptions/).[`isDisabled`](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/inputoptions/) |
| `suffix?` | `Partial` | [`InputOptions`](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/inputoptions/).[`suffix`](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/inputoptions/) |

---



[Source](https:/img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/cesdkconfiguration)