# Interface: AssetResult

Single asset result of a query from the engine.

## Extends[#](#extends)

*   [`Asset`](https://img.ly/docs/cesdk/vue/api/engine/interfaces/asset/)

## Extended by[#](#extended-by)

*   [`CompleteAssetResult`](https://img.ly/docs/cesdk/vue/api/engine/interfaces/completeassetresult/)

## Properties[#](#properties)

| Property | Type | Description | Inherited from |
| --- | --- | --- | --- |
| `id` | `string` | The unique id of this asset. | [`Asset`](https://img.ly/docs/cesdk/vue/api/engine/interfaces/asset/).[`id`](https://img.ly/docs/cesdk/vue/api/engine/interfaces/asset/) |
| `groups?` | [`AssetGroups`](https://img.ly/docs/cesdk/vue/api/engine/type-aliases/assetgroups/) | Groups of the asset. | [`Asset`](https://img.ly/docs/cesdk/vue/api/engine/interfaces/asset/).[`groups`](https://img.ly/docs/cesdk/vue/api/engine/interfaces/asset/) |
| `meta?` | [`AssetMetaData`](https://img.ly/docs/cesdk/vue/api/engine/type-aliases/assetmetadata/) | Asset-specific and custom meta information | [`Asset`](https://img.ly/docs/cesdk/vue/api/engine/interfaces/asset/).[`meta`](https://img.ly/docs/cesdk/vue/api/engine/interfaces/asset/) |
| `payload?` | [`AssetPayload`](https://img.ly/docs/cesdk/vue/api/engine/interfaces/assetpayload/) | Structured asset-specific data | [`Asset`](https://img.ly/docs/cesdk/vue/api/engine/interfaces/asset/).[`payload`](https://img.ly/docs/cesdk/vue/api/engine/interfaces/asset/) |
| `locale?` | `string` | The locale of the label and tags | \- |
| `label?` | `string` | The label of the result. Used for description and tooltips. | \- |
| `tags?` | `string`\[\] | The tags of this asset. Used for filtering and free-text searching. | \- |
| `active?` | `boolean` | If the asset is marked as active, i.e., used in a currently selected element. | \- |
| `credits?` | `object` | Credits for the artist of the asset | \- |
| `credits.name` | `string` | \- | \- |
| `credits.url?` | `string` | \- | \- |
| `license?` | `object` | License for this asset. Overwrites the source license if present | \- |
| `license.name` | `string` | \- | \- |
| `license.url?` | `string` | \- | \- |
| `utm?` | `object` | UTM parameters for the links inside the credits | \- |
| `utm.source?` | `string` | \- | \- |
| `utm.medium?` | `string` | \- | \- |

---



[Source](https:/img.ly/docs/cesdk/vue/api/engine/interfaces/assetquerydata)