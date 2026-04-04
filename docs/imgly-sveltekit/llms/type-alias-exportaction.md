# Type Alias: ExportAction

```
type ExportAction = (options?) => void | Promise<void>;
```

Action function for handling export operations. Can be called with or without options to customize the export behavior. Supports both standard and video export workflows through a generic type parameter. The return type is automatically inferred based on the input options type.

## Parameters[#](#parameters)

| Parameter | Type | Description |
| --- | --- | --- |
| `options?` |  | [`EngineExportOptions`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/type-aliases/engineexportoptions/) |

## Returns[#](#returns)

`void` | `Promise`<`void`\>

A promise that resolves when the export operation is complete, or void for synchronous operations

---



[Source](https:/img.ly/docs/cesdk/sveltekit/api/cesdk-js/type-aliases/engineplugincontext)