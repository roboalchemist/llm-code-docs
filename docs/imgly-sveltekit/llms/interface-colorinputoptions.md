# Interface: ColorInputOptions

Represents options for a color input.

The `ColorInputOptions` interface provides a set of properties that control the behavior and appearance of a color input. These options include settings for the input label, input label position, value, value setter, disabled state, label, and suffix.

## Extends[#](#extends)

*   [`InputOptions`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/interfaces/inputoptions/)<`Color`\>

## Properties[#](#properties)

| Property | Type | Inherited from |
| --- | --- | --- |
| `label?` | `string` | `string`\[\] |
| `inputLabel?` | `string` | `string`\[\] |
| `inputLabelPosition?` | `"top"` | `"left"` |
| `value` | `Color` | [`InputOptions`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/interfaces/inputoptions/).[`value`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/interfaces/inputoptions/) |
| `setValue` | (`value`) => `void` | [`InputOptions`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/interfaces/inputoptions/).[`setValue`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/interfaces/inputoptions/) |
| `isDisabled?` | `boolean` | [`InputOptions`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/interfaces/inputoptions/).[`isDisabled`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/interfaces/inputoptions/) |
| `suffix?` | `Partial` | [`InputOptions`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/interfaces/inputoptions/).[`suffix`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/interfaces/inputoptions/) |

---



[Source](https:/img.ly/docs/cesdk/sveltekit/api/cesdk-js/interfaces/cmykcolor)