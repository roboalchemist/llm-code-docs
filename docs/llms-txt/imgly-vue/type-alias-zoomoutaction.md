# Type Alias: ZoomOutAction

```
type ZoomOutAction = (options?) => void | Promise<void>;
```

Action function for zooming out by one step

## Parameters[#](#parameters)

| Parameter | Type | Description |
| --- | --- | --- |
| `options?` | { `stepSize?`: `number`; `animate?`: | `boolean` |
| `options.stepSize?` | `number` | Custom step size for zoom out (default uses predefined steps) |
| `options.animate?` |  | `boolean` |
| `options.minZoom?` | `number` | Minimum allowed zoom level (default: 0.125) |

## Returns[#](#returns)

`void` | `Promise`<`void`\>

---



[Source](https:/img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/zoominaction)