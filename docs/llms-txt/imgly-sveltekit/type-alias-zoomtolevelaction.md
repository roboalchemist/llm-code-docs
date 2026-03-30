# Type Alias: ZoomToLevelAction

```
type ZoomToLevelAction = (level, options?) => void | Promise<void>;
```

Action function for setting zoom to a specific level

## Parameters[#](#parameters)

| Parameter | Type | Description |
| --- | --- | --- |
| `level` | `number` | \- |
| `options?` | { `animate?`: | `boolean` |
| `options.animate?` |  | `boolean` |
| `options.minZoom?` | `number` | Minimum allowed zoom level (default: 0.125) |
| `options.maxZoom?` | `number` | Maximum allowed zoom level (default: 32) |

## Returns[#](#returns)

`void` | `Promise`<`void`\>

---



[Source](https:/img.ly/docs/cesdk/sveltekit/api/cesdk-js/type-aliases/zoomoutaction)