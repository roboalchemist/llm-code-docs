# Interface: TextInputOptions

Represents options for a text input.

The `TextInputOptions` interface provides a set of properties that control the behavior and appearance of a text input. These options include settings for the input label, input label position, value, value setter, disabled state, placeholder, suffix, and requireConfirm.

## Extends[#](#extends)

*   [`InputOptions`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/interfaces/inputoptions/)<`string`\>

## Properties[#](#properties)

| Property | Type | Default value | Description | Inherited from |
| --- | --- | --- | --- | --- |
| `inputLabel?` | `string` | `string`\[\] | `undefined` | \- |
| `inputLabelPosition?` | `"top"` | `"left"` | `undefined` | \- |
| `value` | `string` | `undefined` | \- | [`InputOptions`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/interfaces/inputoptions/).[`value`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/interfaces/inputoptions/) |
| `setValue` | (`value`) => `void` | `undefined` | \- | [`InputOptions`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/interfaces/inputoptions/).[`setValue`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/interfaces/inputoptions/) |
| `isDisabled?` | `boolean` | `undefined` | \- | [`InputOptions`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/interfaces/inputoptions/).[`isDisabled`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/interfaces/inputoptions/) |
| `suffix?` | `Partial` | `undefined` | \- | [`InputOptions`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/interfaces/inputoptions/).[`suffix`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/interfaces/inputoptions/) |
| `requireConfirm?` | `boolean` | `true` | Whether to require explicit confirmation (Enter/Escape/blur) before applying changes. When true, changes are only applied when user presses Enter/ESC or blurs the input. When false, changes are applied immediately on every keystroke. | \- |

---



[Source](https:/img.ly/docs/cesdk/sveltekit/api/cesdk-js/interfaces/textareaoptions)