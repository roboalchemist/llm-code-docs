# Interface: UserInterfaceElements

Defines the configuration for user interface elements, including panels, dock, libraries, blocks, navigation, and inspector bar.

## Properties[#](#properties)

| Property | Type | Description |
| --- | --- | --- |
| ~`view?`~ | `"advanced"` | `"default"` |
| `panels?` | `object` | \- |
| `panels.inspector?` |  | `boolean` |
| `panels.settings?` |  | `boolean` |
| `panels.assetLibrary?` |  | `boolean` |
| `dock?` | `object` | \- |
| `dock.show?` | `boolean` | **Deprecated** Please use `cesdk.feature.enable('ly.img.dock')` instead. |
| `dock.iconSize?` | `"normal"` | `"large"` |
| `dock.hideLabels?` | `boolean` | \- |
| `dock.defaultGroupId?` | `string` | If groups are used this group will contain all entries that are not included in other groups. **Deprecated** Please use the AssetLibraryEntry & Dock API to control what is shown in the Dock. |
| `dock.groups?` |  | [`DockGroup`](https://img.ly/docs/cesdk/vue/api/cesdk-js/documentation/namespaces/userinterfaceelements/interfaces/dockgroup/)\[\] |
| `libraries?` | `object` | \- |
| `libraries.insert?` | `object` | \- |
| `libraries.insert.entries?` | [`AssetLibraryEntries`](https://img.ly/docs/cesdk/vue/api/cesdk-js/documentation/namespaces/userinterfaceelements/type-aliases/assetlibraryentries/) | **Deprecated** Please use the AssetLibraryEntry & Dock API to control what is shown in the Dock. |
| `libraries.insert.autoClose?` | `boolean` | () => `boolean` |
| `libraries.insert.floating?` | `boolean` | **Deprecated** Please use `cesdk.ui.setPanelFloating('//ly.img.panel/assetLibrary')` instead. |
| `libraries.insert.backgroundTrackLibraryEntries?` | `string`\[\] | (`entries`) => `string`\[\] |
| `libraries.replace?` | `object` | \- |
| `libraries.replace.entries?` | [`AssetLibraryEntries`](https://img.ly/docs/cesdk/vue/api/cesdk-js/documentation/namespaces/userinterfaceelements/type-aliases/assetlibraryentries/) | **Deprecated** Please use the AssetLibraryEntry & Dock API to control what is shown in the Dock. |
| `libraries.replace.autoClose?` | `boolean` | () => `boolean` |
| `libraries.replace.floating?` | `boolean` | **Deprecated** Please use `cesdk.ui.setPanelFloating('//ly.img.panel/replaceAssetLibrary')` instead. |
| ~`blocks?`~ | [`UserInterfaceInspectorBlocks`](https://img.ly/docs/cesdk/vue/api/cesdk-js/documentation/namespaces/userinterfaceelements/interfaces/userinterfaceinspectorblocks/) | **Deprecated** Use `cesdk.feature.enable()` instead. |
| `navigation?` | [`UserInterfaceNavigation`](https://img.ly/docs/cesdk/vue/api/cesdk-js/documentation/namespaces/userinterfaceelements/interfaces/userinterfacenavigation/) | \- |
| `inspectorBar?` |  | `boolean` |

---



[Source](https:/img.ly/docs/cesdk/vue/api/cesdk-js/documentation/namespaces/userinterfaceelements/interfaces/userinterfaceelement)