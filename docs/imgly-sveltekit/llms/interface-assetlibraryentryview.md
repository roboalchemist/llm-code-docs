# Interface: AssetLibraryEntryView

Interface representing the view configuration for an asset library entry.

*   `showGroupOverview`: Optional boolean indicating whether to show the group overview.
*   `promptBeforeApply`: Optional configuration for showing a confirmation dialog before applying an asset.
*   `icon`: Optional custom icon for the asset.
*   `previewLength`: Optional number determining how many asset results will be shown in an overview or section overview.
*   `previewBackgroundType`: Optional type determining if the thumbUri is set as a background that will be contained or covered by the card in an overview or section overview.
*   `gridBackgroundType`: Optional type determining if the thumbUri is set as a background that will be contained or covered by the card in the grid view.
*   `gridColumns`: Optional number of columns in the grid view.
*   `gridItemHeight`: Optional height of an item in the grid view, either ‘auto’ or ‘square’.
*   `cardBackgroundPreferences`: Optional configuration for determining what will be used as the card background from the asset and in which priorities.
*   `cardBorder`: Optional boolean indicating whether to draw a border around the card.
*   `cardLabel`: Optional function to overwrite the label of a card for a specific asset result.
*   `cardStyle`: Optional function to add custom styles to a card for a specific asset result.
*   `cardLabelStyle`: Optional function to add custom styles to a label for a specific asset result.
*   `cardLabelPosition`: Optional function to position the label inside or below the card.
*   `cardLabelTruncateLines`: Optional function to control label truncation to occur at end of first line (‘single’) or at end of second line (‘multi’).
*   `sortBy`: Optional configuration for sorting the asset results.

## Extended by[#](#extended-by)

*   [`AssetLibraryEntry`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/interfaces/assetlibraryentry/)

## Properties[#](#properties)

| Property | Type | Description |
| --- | --- | --- |
| `showGroupOverview?` | `boolean` | \- |
| `isSearchable?` | `boolean` | Indicates whether this asset library entry supports searching. When set to false, this entry’s assets cannot be searched. The search field in the panel will only be shown if at least one visible entry is searchable. Defaults to true (entry is searchable). |
| `promptBeforeApply?` |  | `boolean` |
| `icon?` | [`CustomIcon`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/documentation/namespaces/userinterfaceelements/type-aliases/customicon/) | \- |
| `previewLength?` | `number` | Determines how many asset results will be show in an overview or section overview. |
| `previewBackgroundType?` | `"cover"` | `"contain"` |
| `gridBackgroundType?` | `"cover"` | `"contain"` |
| `gridColumns?` | `number` | Number of columns in the grid view |
| `gridItemHeight?` | `"auto"` | `"square"` |
| `cardBackgroundPreferences?` |  | [`CardBackground`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/documentation/namespaces/userinterfaceelements/type-aliases/cardbackground/)\[\] |
| `cardBorder?` | `boolean` | Draws a border around the card if set to true |
| `cardLabel?` | (`assetResult`) => `string` | Overwrite the label of a card for a specific asset result |
| `cardStyle?` | (`assetResult`) => `Record`<`string`, `string`\> | Add custom styles to a card for a specific asset result |
| `cardLabelStyle?` | (`assetResult`) => `Record`<`string`, `string`\> | Add custom styles to a label for a specific asset result |
| `cardLabelPosition?` | (`assetResult`) => `"inside"` | `"below"` |
| `cardLabelTruncateLines?` | (`assetResult`) => `"single"` | `"multi"` |
| `disableTooltips?` | `boolean` | Control whether tooltips should be disabled for asset library cards. When set to true, tooltips will not be shown on cards. Defaults to false (tooltips are shown). |
| `sortBy?` |  | [`SortingOrder`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/type-aliases/sortingorder/) |

---



[Source](https:/img.ly/docs/cesdk/sveltekit/api/cesdk-js/documentation/namespaces/userinterfaceelements/interfaces/assetlibraryentrydata)