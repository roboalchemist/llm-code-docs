# Type Alias: ImportSceneAction

```
type ImportSceneAction = (options) => void | Promise<void>;
```

Action function for handling scene import operations.

## Parameters[#](#parameters)

| Parameter | Type | Description |
| --- | --- | --- |
| `options` | { `format?`: `"scene"` | `"archive"`; } |
| `options.format?` | `"scene"` | `"archive"` |

## Returns[#](#returns)

`void` | `Promise`<`void`\>

A promise that resolves with the imported scene data as a string, or the scene data directly

---



[Source](https:/img.ly/docs/cesdk/sveltekit/api/cesdk-js/type-aliases/horizontalblockalignment)