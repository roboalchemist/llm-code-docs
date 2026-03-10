# Interface: BuilderRenderFunctionContext

Represents the context for rendering a builder function.

The `BuilderRenderFunctionContext` interface provides a set of properties that describe the context for rendering a builder function. These options include settings for the builder, engine, state, payload, render optimized small viewport, and experimental APIs.

## Type Parameters[#](#type-parameters)

| Type Parameter |
| --- |
| `P` |

## Properties[#](#properties)

| Property | Modifier | Type | Description |
| --- | --- | --- | --- |
| `builder` | `public` | [`Builder`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/interfaces/builder/) | \- |
| `cesdk` | `public` | [`CreativeEditorSDK`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/classes/creativeeditorsdk/) | \- |
| `engine` | `public` | [`CreativeEngine`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/classes/creativeengine/) | \- |
| `state` | `public` | { <`T`\> (`id`, `defaultValue`): `object`; <`T`\> (`id`): `object`; } | State object that can be used to store and retrieve local values. It will take a unique identifier for this state that can be used to access this store later. `const { value, setValue } = state('unique-id', 'default-value');` If no default value is set, the `value` property may be undefined if no value was set before: `const { value, setValue } = state('unique-id', 'default-value');` **Param** The unique identifier for the state. **Param** The default value for the state. |
| `payload?` | `public` | `P` | \- |
| `renderOptimizedSmallViewport` | `public` | `boolean` | \- |
| `experimental` | `public` | [`BuilderRenderContext`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/documentation/namespaces/experimentalbuilder/interfaces/builderrendercontext/) | PLEASE NOTE: This contains experimental APIs. Use them with caution since they might change without warning and might be replaced with a completely different concept or maybe not at all. |

---



[Source](https:/img.ly/docs/cesdk/sveltekit/api/cesdk-js/interfaces/builtintranslations)