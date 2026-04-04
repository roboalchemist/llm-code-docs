# Type Alias: PanelOptions

```
type PanelOptions<T> = object;
```

Represents the options for a panel in the Creative Editor SDK. This interface defines the options for a panel, including whether it is closable by the user, its position, whether it is floating, and its payload.

## Type Parameters[#](#type-parameters)

| Type Parameter |
| --- |
| `T` _extends_ [`PanelId`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/panelid/) |

## Properties[#](#properties)

| Property | Type |
| --- | --- |
| `closableByUser?` | `boolean` |
| `position?` | [`PanelPosition`](https://img.ly/docs/cesdk/vue/api/cesdk-js/enumerations/panelposition/) |
| `floating?` | `boolean` |
| `payload?` | [`PanelPayload`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/panelpayload/)<`T`\> |

---



[Source](https:/img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/panelid)