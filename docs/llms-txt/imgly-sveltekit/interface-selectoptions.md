# Interface: SelectOptions

Represents options for a select input.

The `SelectOptions` interface provides a set of properties that control the behavior and appearance of a select input. These options include settings for the input label, input label position, value, value setter, disabled state, icon, tooltip, loading state, loading progress, suffix, and values.

## Extends[#](#extends)

*   [`InputOptions`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/interfaces/inputoptions/)<[`SelectValue`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/interfaces/selectvalue/)\>

## Properties[#](#properties)

| Property | Type | Overrides | Inherited from |
| --- | --- | --- | --- |
| `inputLabelPosition?` | `"top"` | `"left"` | \- |
| `value` | [`SelectValue`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/interfaces/selectvalue/) | \- | [`InputOptions`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/interfaces/inputoptions/).[`value`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/interfaces/inputoptions/) |
| `setValue` | (`value`) => `void` | \- | [`InputOptions`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/interfaces/inputoptions/).[`setValue`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/interfaces/inputoptions/) |
| `icon?` | [`CustomIcon`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/documentation/namespaces/userinterfaceelements/type-aliases/customicon/) | \- | \- |
| `inputLabel?` | `string` | `string`\[\] | [`InputOptions`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/interfaces/inputoptions/).[`inputLabel`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/interfaces/inputoptions/) |
| `tooltip?` | `string` | `string`\[\] | \- |
| `isDisabled?` | `boolean` | [`InputOptions`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/interfaces/inputoptions/).[`isDisabled`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/interfaces/inputoptions/) | \- |
| `isLoading?` | `boolean` | \- | \- |
| `loadingProgress?` | `number` | \- | \- |
| `suffix?` | `Partial` | [`InputOptions`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/interfaces/inputoptions/).[`suffix`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/interfaces/inputoptions/) | \- |
| `values` | [`SelectValue`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/interfaces/selectvalue/)\[\] | \- | \- |

---



[Source](https:/img.ly/docs/cesdk/sveltekit/api/cesdk-js/interfaces/rgbcolor)