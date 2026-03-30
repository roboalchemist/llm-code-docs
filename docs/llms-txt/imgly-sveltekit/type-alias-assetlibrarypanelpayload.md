# Type Alias: AssetLibraryPanelPayload

```
type AssetLibraryPanelPayload = object;
```

Represents the payload for the asset library panel in the Creative Editor SDK. This interface defines the title, entries, and placement options for the asset library panel.

## Properties[#](#properties)

| Property | Type | Description |
| --- | --- | --- |
| `title?` | `string` | `string`\[\] |
| `entries?` | `string`\[\] | \- |
| `applyAssetContext?` | [`ApplyAssetOptions`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/interfaces/applyassetoptions/) | Context for asset application. Passed directly to engine.asset.apply() when an asset is selected. |

---



[Source](https:/img.ly/docs/cesdk/sveltekit/api/cesdk-js/type-aliases/assetmetadata)