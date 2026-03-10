# Type Alias: PanelPayload

```
type PanelPayload<T> = T extends "//ly.img.panel/assetLibrary" ? AssetLibraryPanelPayload : UnknownPanelPayload;
```

Represents the payload for a panel in the Creative Editor SDK. This type defines the payload based on the panel ID.

## Type Parameters[#](#type-parameters)

| Type Parameter |
| --- |
| `T` _extends_ [`PanelId`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/type-aliases/panelid/) |

---



[Source](https:/img.ly/docs/cesdk/sveltekit/api/cesdk-js/type-aliases/objecttypeshorthand)