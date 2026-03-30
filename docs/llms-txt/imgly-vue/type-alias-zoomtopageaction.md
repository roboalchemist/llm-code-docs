# Type Alias: ZoomToPageAction

```
type ZoomToPageAction = (options?) => Promise<void>;
```

Action function for zooming to a page with optional padding

## Parameters[#](#parameters)

| Parameter | Type | Description |
| --- | --- | --- |
| `options?` | { `page?`: `"current"` | `"first"` |
| `options.page?` | `"current"` | `"first"` |
| `options.padding?` |  | `number` |
| `options.animate?` |  | `boolean` |
| `options.autoFit?` | `boolean` | Whether to enable auto-fit mode after zooming (default: false) |

## Returns[#](#returns)

`Promise`<`void`\>

---



[Source](https:/img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/zoomtoselectionaction)