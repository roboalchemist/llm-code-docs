# Type Alias: ZoomToBlockAction

```
type ZoomToBlockAction = (blockId, options?) => Promise<void>;
```

Action function for zooming to a specific block

## Parameters[#](#parameters)

| Parameter | Type | Description |
| --- | --- | --- |
| `blockId` | `number` | \- |
| `options?` | { `padding?`: | `number` |
| `options.padding?` |  | `number` |
| `options.animate?` |  | `boolean` |
| `options.autoFit?` | `boolean` | Whether to enable auto-fit mode after zooming (default: false) |

## Returns[#](#returns)

`Promise`<`void`\>

---



[Source](https:/img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/zoomoptions)