# Interface: AssetLibraryEntryData

Interface representing the data configuration for an asset library entry.

*   `id`: The unique identifier for the asset library entry.
*   `sourceIds`: An array of source IDs associated with the asset library entry, or a function that returns an array of source IDs.
*   `sceneMode`: Optional configuration for the scene mode, which can be a `SceneMode`, ‘All’, or a function returning a `SceneMode` or ‘All’.
*   `excludeGroups`: Optional array of group IDs to exclude from the asset library entry.
*   `includeGroups`: Optional array of group IDs to include in the asset library entry.
*   `title`: Optional title for the asset library entry, which can be a string or a function returning a string or undefined.
*   `canAdd`: Optional boolean or function indicating whether the asset can be added to the source.
*   `canRemove`: Optional boolean or function indicating whether the asset can be removed from the source.

## Extended by[#](#extended-by)

*   [`AssetLibraryEntry`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/interfaces/assetlibraryentry/)

## Properties[#](#properties)

| Property | Type | Description |
| --- | --- | --- |
| `id` | `string` | \- |
| `sourceIds` | `string`\[\] | (`context`) => `string`\[\] |
| `sceneMode?` |  | `"Design"` |
| `excludeGroups?` | `string`\[\] | \- |
| `includeGroups?` | `string`\[\] | \- |
| `title?` | `string` | (`options`) => `string` |
| `canAdd?` | `boolean` | (`sourceId`) => `boolean` |
| `canRemove?` | `boolean` | (`sourceId`) => `boolean` |

---



[Source](https:/img.ly/docs/cesdk/sveltekit/api/cesdk-js/documentation/namespaces/userinterfaceelements/interfaces/assetentrysourceidscontext)