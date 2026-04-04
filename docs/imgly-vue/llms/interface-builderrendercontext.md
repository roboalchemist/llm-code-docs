# Interface: BuilderRenderContext

## Properties[#](#properties)

| Property | Type | Description |
| --- | --- | --- |
| `builder` | [`Builder`](https://img.ly/docs/cesdk/vue/api/cesdk-js/documentation/namespaces/experimentalbuilder/interfaces/builder/) | \- |
| `global` | { <`T`\> (`id`, `defaultValue`): `object`; <`T`\> (`id`): `object`; } | Global state object that can be used to store and retrieve values. It will take a unique identifier for this state that can be used to access this store later. `const { value, setValue } = global('unique-id', 'default-value');` If no default value is set, the `value` property may be undefined if no value was set before: `const { value, setValue } = global('unique-id', 'default-value');` **Param** The unique identifier for the state. **Param** The default value for the state. |

---



[Source](https:/img.ly/docs/cesdk/vue/api/cesdk-js/documentation/namespaces/experimentalbuilder/interfaces/builder)