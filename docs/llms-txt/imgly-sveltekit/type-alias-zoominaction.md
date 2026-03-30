# Type Alias: ZoomInAction

```
type ZoomInAction = (options?) => void | Promise<void>;
```

Action function for zooming in by one step

## Parameters[#](#parameters)

| Parameter | Type | Description |
| --- | --- | --- |
| `options?` | { `stepSize?`: `number`; `animate?`: | `boolean` |
| `options.stepSize?` | `number` | Custom step size for zoom in (default uses predefined steps) |
| `options.animate?` |  | `boolean` |
| `options.maxZoom?` | `number` | Maximum allowed zoom level (default: 32) |

## Returns[#](#returns)

`void` | `Promise`<`void`\>

---



[Source](https:/img.ly/docs/cesdk/sveltekit/api/cesdk-js/type-aliases/zoomautofitaxis)