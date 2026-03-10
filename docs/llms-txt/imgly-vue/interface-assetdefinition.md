# Interface: AssetDefinition

Definition of an asset used if an asset is added to an asset source.

## Extends[#](#extends)

*   [`Asset`](https://img.ly/docs/cesdk/vue/api/engine/interfaces/asset/)

## Properties[#](#properties)

| Property | Type | Description | Inherited from |
| --- | --- | --- | --- |
| `id` | `string` | The unique id of this asset. | [`Asset`](https://img.ly/docs/cesdk/vue/api/engine/interfaces/asset/).[`id`](https://img.ly/docs/cesdk/vue/api/engine/interfaces/asset/) |
| `groups?` | [`AssetGroups`](https://img.ly/docs/cesdk/vue/api/engine/type-aliases/assetgroups/) | Groups of the asset. | [`Asset`](https://img.ly/docs/cesdk/vue/api/engine/interfaces/asset/).[`groups`](https://img.ly/docs/cesdk/vue/api/engine/interfaces/asset/) |
| `meta?` | [`AssetMetaData`](https://img.ly/docs/cesdk/vue/api/engine/type-aliases/assetmetadata/) | Asset-specific and custom meta information | [`Asset`](https://img.ly/docs/cesdk/vue/api/engine/interfaces/asset/).[`meta`](https://img.ly/docs/cesdk/vue/api/engine/interfaces/asset/) |
| `payload?` | [`AssetPayload`](https://img.ly/docs/cesdk/vue/api/engine/interfaces/assetpayload/) | Structured asset-specific data | [`Asset`](https://img.ly/docs/cesdk/vue/api/engine/interfaces/asset/).[`payload`](https://img.ly/docs/cesdk/vue/api/engine/interfaces/asset/) |
| `label?` | `Record`<`string`, `string`\> | Label used to display in aria-label and as a tooltip. Will be also searched in a query and should be localized | \- |
| `tags?` | `Record`<`string`, `string`\[\]> | Tags for this asset. Can be used for filtering, but is also useful for free-text search. Since the label is searched as well as used for tooltips you do not want to overdo it, but still add things which are searched. Thus, it should be localized similar to the `label`. | \- |

---



[Source](https:/img.ly/docs/cesdk/vue/api/engine/interfaces/assetcolorproperty)