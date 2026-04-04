# Interface: AssetLibraryEntry

Represents an entry in the asset library, combining data and view configurations.

## Extends[#](#extends)

*   [`AssetLibraryEntryData`](https://img.ly/docs/cesdk/vue/api/cesdk-js/documentation/namespaces/userinterfaceelements/interfaces/assetlibraryentrydata/).[`AssetLibraryEntryView`](https://img.ly/docs/cesdk/vue/api/cesdk-js/documentation/namespaces/userinterfaceelements/interfaces/assetlibraryentryview/)

## Properties[#](#properties)

| Property | Type | Description | Inherited from |
| --- | --- | --- | --- |
| `id` | `string` | \- | [`AssetLibraryEntryData`](https://img.ly/docs/cesdk/vue/api/cesdk-js/documentation/namespaces/userinterfaceelements/interfaces/assetlibraryentrydata/).[`id`](https://img.ly/docs/cesdk/vue/api/cesdk-js/documentation/namespaces/userinterfaceelements/interfaces/assetlibraryentrydata/) |
| `sourceIds` | `string`\[\] | (`context`) => `string`\[\] | \- |
| `sceneMode?` |  | `"Design"` | `"Video"` |
| `excludeGroups?` | `string`\[\] | \- | [`AssetLibraryEntryData`](https://img.ly/docs/cesdk/vue/api/cesdk-js/documentation/namespaces/userinterfaceelements/interfaces/assetlibraryentrydata/).[`excludeGroups`](https://img.ly/docs/cesdk/vue/api/cesdk-js/documentation/namespaces/userinterfaceelements/interfaces/assetlibraryentrydata/) |
| `includeGroups?` | `string`\[\] | \- | [`AssetLibraryEntryData`](https://img.ly/docs/cesdk/vue/api/cesdk-js/documentation/namespaces/userinterfaceelements/interfaces/assetlibraryentrydata/).[`includeGroups`](https://img.ly/docs/cesdk/vue/api/cesdk-js/documentation/namespaces/userinterfaceelements/interfaces/assetlibraryentrydata/) |
| `title?` | `string` | (`options`) => `string` | \- |
| `canAdd?` | `boolean` | (`sourceId`) => `boolean` | If `true` an upload button will be shown and the uploaded file will be added to the source. If a function is used it will be called with the current asset source id. The asset source needs to support `addAsset`. |
| `canRemove?` | `boolean` | (`sourceId`) => `boolean` | If `true` the asset can be removed from the asset source. If a function is used it will be called with the current asset source id. The asset source needs to support `removeAsset`. |
| `showGroupOverview?` | `boolean` | \- | [`AssetLibraryEntryView`](https://img.ly/docs/cesdk/vue/api/cesdk-js/documentation/namespaces/userinterfaceelements/interfaces/assetlibraryentryview/).[`showGroupOverview`](https://img.ly/docs/cesdk/vue/api/cesdk-js/documentation/namespaces/userinterfaceelements/interfaces/assetlibraryentryview/) |
| `isSearchable?` | `boolean` | Indicates whether this asset library entry supports searching. When set to false, this entry’s assets cannot be searched. The search field in the panel will only be shown if at least one visible entry is searchable. Defaults to true (entry is searchable). | [`AssetLibraryEntryView`](https://img.ly/docs/cesdk/vue/api/cesdk-js/documentation/namespaces/userinterfaceelements/interfaces/assetlibraryentryview/).[`isSearchable`](https://img.ly/docs/cesdk/vue/api/cesdk-js/documentation/namespaces/userinterfaceelements/interfaces/assetlibraryentryview/) |
| `promptBeforeApply?` |  | `boolean` | { `show`: `boolean`; `sourceIds?`: `string`\[\]; } |
| `icon?` | [`CustomIcon`](https://img.ly/docs/cesdk/vue/api/cesdk-js/documentation/namespaces/userinterfaceelements/type-aliases/customicon/) | \- | [`AssetLibraryEntryView`](https://img.ly/docs/cesdk/vue/api/cesdk-js/documentation/namespaces/userinterfaceelements/interfaces/assetlibraryentryview/).[`icon`](https://img.ly/docs/cesdk/vue/api/cesdk-js/documentation/namespaces/userinterfaceelements/interfaces/assetlibraryentryview/) |
| `previewLength?` | `number` | Determines how many asset results will be show in an overview or section overview. | [`AssetLibraryEntryView`](https://img.ly/docs/cesdk/vue/api/cesdk-js/documentation/namespaces/userinterfaceelements/interfaces/assetlibraryentryview/).[`previewLength`](https://img.ly/docs/cesdk/vue/api/cesdk-js/documentation/namespaces/userinterfaceelements/interfaces/assetlibraryentryview/) |
| `previewBackgroundType?` | `"cover"` | `"contain"` | Determines if the thumbUri is set as a background that will be contained or covered by the card in an overview or section overview. |
| `gridBackgroundType?` | `"cover"` | `"contain"` | Determines if the thumbUri is set as a background that will be contained or covered by the card in the grid view |
| `gridColumns?` | `number` | Number of columns in the grid view | [`AssetLibraryEntryView`](https://img.ly/docs/cesdk/vue/api/cesdk-js/documentation/namespaces/userinterfaceelements/interfaces/assetlibraryentryview/).[`gridColumns`](https://img.ly/docs/cesdk/vue/api/cesdk-js/documentation/namespaces/userinterfaceelements/interfaces/assetlibraryentryview/) |
| `gridItemHeight?` | `"auto"` | `"square"` | Determines the height of an item in the grid view. - `auto` automatically determine height yielding a masonry-like grid view - `square` every card will have the same square size |
| `cardBackgroundPreferences?` |  | [`CardBackground`](https://img.ly/docs/cesdk/vue/api/cesdk-js/documentation/namespaces/userinterfaceelements/type-aliases/cardbackground/)\[\] | (`asset`) => [`CustomCardBackground`](https://img.ly/docs/cesdk/vue/api/cesdk-js/documentation/namespaces/userinterfaceelements/type-aliases/customcardbackground/) |
| `cardBorder?` | `boolean` | Draws a border around the card if set to true | [`AssetLibraryEntryView`](https://img.ly/docs/cesdk/vue/api/cesdk-js/documentation/namespaces/userinterfaceelements/interfaces/assetlibraryentryview/).[`cardBorder`](https://img.ly/docs/cesdk/vue/api/cesdk-js/documentation/namespaces/userinterfaceelements/interfaces/assetlibraryentryview/) |
| `cardLabel?` | (`assetResult`) => `string` | Overwrite the label of a card for a specific asset result | [`AssetLibraryEntryView`](https://img.ly/docs/cesdk/vue/api/cesdk-js/documentation/namespaces/userinterfaceelements/interfaces/assetlibraryentryview/).[`cardLabel`](https://img.ly/docs/cesdk/vue/api/cesdk-js/documentation/namespaces/userinterfaceelements/interfaces/assetlibraryentryview/) |
| `cardStyle?` | (`assetResult`) => `Record`<`string`, `string`\> | Add custom styles to a card for a specific asset result | [`AssetLibraryEntryView`](https://img.ly/docs/cesdk/vue/api/cesdk-js/documentation/namespaces/userinterfaceelements/interfaces/assetlibraryentryview/).[`cardStyle`](https://img.ly/docs/cesdk/vue/api/cesdk-js/documentation/namespaces/userinterfaceelements/interfaces/assetlibraryentryview/) |
| `cardLabelStyle?` | (`assetResult`) => `Record`<`string`, `string`\> | Add custom styles to a label for a specific asset result | [`AssetLibraryEntryView`](https://img.ly/docs/cesdk/vue/api/cesdk-js/documentation/namespaces/userinterfaceelements/interfaces/assetlibraryentryview/).[`cardLabelStyle`](https://img.ly/docs/cesdk/vue/api/cesdk-js/documentation/namespaces/userinterfaceelements/interfaces/assetlibraryentryview/) |
| `cardLabelPosition?` | (`assetResult`) => `"inside"` | `"below"` | Position the label inside or below the card. Defaults to ‘inside’. |
| `cardLabelTruncateLines?` | (`assetResult`) => `"single"` | `"multi"` | Control label truncation to occur at end of first line (‘single’), or at end of second line (‘multi’). Defaults to ‘multi’. |
| `disableTooltips?` | `boolean` | Control whether tooltips should be disabled for asset library cards. When set to true, tooltips will not be shown on cards. Defaults to false (tooltips are shown). | [`AssetLibraryEntryView`](https://img.ly/docs/cesdk/vue/api/cesdk-js/documentation/namespaces/userinterfaceelements/interfaces/assetlibraryentryview/).[`disableTooltips`](https://img.ly/docs/cesdk/vue/api/cesdk-js/documentation/namespaces/userinterfaceelements/interfaces/assetlibraryentryview/) |
| `sortBy?` |  | [`SortingOrder`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/sortingorder/) | { `sortKey?`: `string`; `sortingOrder?`: [`SortingOrder`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/sortingorder/); } |

---



[Source](https:/img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/assetfixedsize)