# Interface: AssetsQueryResult

Return type of a `findAssets` query.

## Type Parameters[#](#type-parameters)

| Type Parameter | Default type |
| --- | --- |
| `T` _extends_ [`AssetResult`](https://img.ly/docs/cesdk/vue/api/engine/interfaces/assetresult/) | [`AssetResult`](https://img.ly/docs/cesdk/vue/api/engine/interfaces/assetresult/) |

## Properties[#](#properties)

| Property | Type | Description |
| --- | --- | --- |
| `assets` | `T`\[\] | The assets in the requested page |
| `currentPage` | `number` | The current, requested page |
| `nextPage?` | `number` | The next page to query if it exists |
| `total` | `number` | How many assets are there in total for the current query regardless of the page |

---



[Source](https:/img.ly/docs/cesdk/vue/api/engine/interfaces/assetspotcolor)