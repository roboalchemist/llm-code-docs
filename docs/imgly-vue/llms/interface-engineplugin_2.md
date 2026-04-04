# Interface: EnginePlugin

Represents an engine plugin.

Defines the structure of an engine plugin, including its name, version, and initialization function.

*   ‘name’: The name of the plugin.
*   ‘version’: The version of the plugin.
*   ‘initialize’: The function to initialize the plugin with the provided context. Can be synchronous or asynchronous.

## Properties[#](#properties)

| Property | Type |
| --- | --- |
| `name` | `string` |
| `version` | `string` |
| `initialize` | (`context`) => `void` |

---



[Source](https:/img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/engineconfiguration)