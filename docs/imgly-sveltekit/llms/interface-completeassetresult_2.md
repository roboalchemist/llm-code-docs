# Interface: CompleteAssetResult

Asset results that are returned from the engine.

They contain additional information about the context of the asset.

## Extends[#](#extends)

*   [`AssetResult`](https://img.ly/docs/cesdk/sveltekit/api/engine/interfaces/assetresult/)

## Properties[#](#properties)

| Property | Type | Description | Overrides | Inherited from |
| --- | --- | --- | --- | --- |
| `id` | `string` | The unique id of this asset. | \- | [`AssetResult`](https://img.ly/docs/cesdk/sveltekit/api/engine/interfaces/assetresult/).[`id`](https://img.ly/docs/cesdk/sveltekit/api/engine/interfaces/assetresult/) |
| `groups?` | [`AssetGroups`](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/assetgroups/) | Groups of the asset. | \- | [`AssetResult`](https://img.ly/docs/cesdk/sveltekit/api/engine/interfaces/assetresult/).[`groups`](https://img.ly/docs/cesdk/sveltekit/api/engine/interfaces/assetresult/) |
| `meta?` | [`AssetMetaData`](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/assetmetadata/) | Asset-specific and custom meta information | \- | [`AssetResult`](https://img.ly/docs/cesdk/sveltekit/api/engine/interfaces/assetresult/).[`meta`](https://img.ly/docs/cesdk/sveltekit/api/engine/interfaces/assetresult/) |
| `payload?` | [`AssetPayload`](https://img.ly/docs/cesdk/sveltekit/api/engine/interfaces/assetpayload/) | Structured asset-specific data | \- | [`AssetResult`](https://img.ly/docs/cesdk/sveltekit/api/engine/interfaces/assetresult/).[`payload`](https://img.ly/docs/cesdk/sveltekit/api/engine/interfaces/assetresult/) |
| `locale?` | `string` | The locale of the label and tags | \- | [`AssetResult`](https://img.ly/docs/cesdk/sveltekit/api/engine/interfaces/assetresult/).[`locale`](https://img.ly/docs/cesdk/sveltekit/api/engine/interfaces/assetresult/) |
| `label?` | `string` | The label of the result. Used for description and tooltips. | \- | [`AssetResult`](https://img.ly/docs/cesdk/sveltekit/api/engine/interfaces/assetresult/).[`label`](https://img.ly/docs/cesdk/sveltekit/api/engine/interfaces/assetresult/) |
| `tags?` | `string`\[\] | The tags of this asset. Used for filtering and free-text searching. | \- | [`AssetResult`](https://img.ly/docs/cesdk/sveltekit/api/engine/interfaces/assetresult/).[`tags`](https://img.ly/docs/cesdk/sveltekit/api/engine/interfaces/assetresult/) |
| `credits?` | `object` | Credits for the artist of the asset | \- | [`AssetResult`](https://img.ly/docs/cesdk/sveltekit/api/engine/interfaces/assetresult/).[`credits`](https://img.ly/docs/cesdk/sveltekit/api/engine/interfaces/assetresult/) |
| `credits.name` | `string` | \- | \- | \- |
| `credits.url?` | `string` | \- | \- | \- |
| `license?` | `object` | License for this asset. Overwrites the source license if present | \- | [`AssetResult`](https://img.ly/docs/cesdk/sveltekit/api/engine/interfaces/assetresult/).[`license`](https://img.ly/docs/cesdk/sveltekit/api/engine/interfaces/assetresult/) |
| `license.name` | `string` | \- | \- | \- |
| `license.url?` | `string` | \- | \- | \- |
| `utm?` | `object` | UTM parameters for the links inside the credits | \- | [`AssetResult`](https://img.ly/docs/cesdk/sveltekit/api/engine/interfaces/assetresult/).[`utm`](https://img.ly/docs/cesdk/sveltekit/api/engine/interfaces/assetresult/) |
| `utm.source?` | `string` | \- | \- | \- |
| `utm.medium?` | `string` | \- | \- | \- |
| `context` | `object` | Context how an asset was added or shall be used in the future. This is added to all assets coming from the engine. | \- | \- |
| `context.sourceId` | `string` | \- | \- | \- |
| `active` | `boolean` | This is optional in `AssetResult` but always present here | [`AssetResult`](https://img.ly/docs/cesdk/sveltekit/api/engine/interfaces/assetresult/).[`active`](https://img.ly/docs/cesdk/sveltekit/api/engine/interfaces/assetresult/) | \- |

---



[Source](https:/img.ly/docs/cesdk/sveltekit/api/engine/interfaces/cmykcolor)