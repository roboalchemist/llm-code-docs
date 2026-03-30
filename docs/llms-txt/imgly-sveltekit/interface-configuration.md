# Interface: Configuration

Specifies the configuration for the Creative Editor SDK.

The `Configuration` interface provides a set of properties that control the behavior and settings of the editor. These options include settings for the base URL, license, user ID, core settings, logger, feature flags, presets, force WebGL1, audio output, and role.

## Properties[#](#properties)

| Property | Type | Description |
| --- | --- | --- |
| `baseURL` | `string` | \- |
| `license?` | `string` | \- |
| `userId?` | `string` | \- |
| `core` | `object` | \- |
| `core.baseURL` | `string` | \- |
| `logger` | [`Logger`](https://img.ly/docs/cesdk/sveltekit/api/engine/interfaces/logger/) | \- |
| `featureFlags?` | `object` | \- |
| ~`presets`~ | `object` | **Deprecated** This config key is not used anymore and will be removed. |
| `presets.typefaces?` | `object` | **Deprecated** The configuration option `presets.typefaces` does not exist anymore. Custom typefaces should be defined as asset sources using the `cesdk.engine.asset.addSource` or `cesdk.engine.asset.addLocalSource` instead. |
| `forceWebGL1?` | `boolean` | By default the engine tries to create a webgl2 context. If this fails it falls back to trying to create a webgl1 context. If this configuration option is set to true, it will no longer try to create a webgl2 context and always create a webgl1 context. |
| `audioOutput?` | `"auto"` | `"none"` |
| `role?` | [`RoleString`](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/rolestring/) | \- |

---



[Source](https:/img.ly/docs/cesdk/sveltekit/api/engine/interfaces/cursorevent)