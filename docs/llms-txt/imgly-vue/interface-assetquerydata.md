# Interface: AssetQueryData

Defines a request for querying assets

## Properties[#](#properties)

| Property | Type | Description |
| --- | --- | --- |
| `query?` | `string` | A query string used for (fuzzy) searching of labels and tags |
| `page` | `number` | The current page queried for paginated views. |
| `tags?` | `string` | `string`\[\] |
| `groups?` | [`AssetGroups`](https://img.ly/docs/cesdk/vue/api/engine/type-aliases/assetgroups/) | Query only these groups |
| `excludeGroups?` | [`AssetGroups`](https://img.ly/docs/cesdk/vue/api/engine/type-aliases/assetgroups/) | Filter out assets with this groups |
| `locale?` | `string` | Choose the locale of the labels and tags for localized search and filtering |
| `perPage` | `number` | The number of results queried. How many assets shall be returned regardless of the total number of assets available. Together with `page` this can be used for pagination. |
| `sortingOrder?` | [`SortingOrder`](https://img.ly/docs/cesdk/vue/api/engine/type-aliases/sortingorder/) | The order to sort by if the asset source supports sorting. If set to None, the order is the same as the assets were added to the source. |
| `sortKey?` | `string` | The key that identifies the meta data value to sort by or ‘id’ to sort by the asset ID. If empty, the assets are sorted by the index. |
| `sortActiveFirst?` | `boolean` | Sort assets that are marked as active first. |

---



[Source](https:/img.ly/docs/cesdk/vue/api/engine/interfaces/assetpayload)