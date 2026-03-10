# Type Alias: ExportSceneAction

```
type ExportSceneAction = (options) => void | Promise<void>;
```

Action function for handling scene export operations.

## Parameters[#](#parameters)

| Parameter | Type | Description |
| --- | --- | --- |
| `options` | { `format`: `"scene"` | `"archive"`; } |
| `options.format` | `"scene"` | `"archive"` |

## Returns[#](#returns)

`void` | `Promise`<`void`\>

A promise that resolves when the export operation is complete, or void for synchronous operations

---



[Source](https:/img.ly/docs/cesdk/sveltekit/api/cesdk-js/type-aliases/featureid)