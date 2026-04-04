# Interface: \_FindAssetsQuery

Represents a query for finding assets.

The `FindAssetsQuery` interface provides a set of properties that describe a query for finding assets, including the number of assets per page, the page number, the query string, the tags, the groups, the excluded groups, the locale, the sorting order, the sort key, and whether to sort active assets first.

Methods for working with queries for finding assets.

## Properties[#](#properties)

| Property | Type |
| --- | --- |
| `perPage` | `number` |
| `page` | `number` |
| `query` | `string` |
| `tags` | `string`\[\] |
| `groups` | `string`\[\] |
| `excludeGroups` | `string`\[\] |
| `locale` | `string` |
| `sortingOrder` | [`SortingOrder`](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/sortingorder/) |
| `sortKey` | `string` |
| `sortActiveFirst` | `boolean` |

---



[Source](https:/img.ly/docs/cesdk/sveltekit/api/engine/interfaces/engineplugin)