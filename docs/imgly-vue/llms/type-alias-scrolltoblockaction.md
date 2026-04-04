# Type Alias: ScrollToBlockAction

```
type ScrollToBlockAction = (blockId, options?) => Promise<void>;
```

Action function for scrolling to a specific block

## Parameters[#](#parameters)

| Parameter | Type | Description |
| --- | --- | --- |
| `blockId` | `number` | \- |
| `options?` | { `animate?`: `boolean`; } | \- |
| `options.animate?` | `boolean` | Whether to animate the scroll (default: false) |

## Returns[#](#returns)

`Promise`<`void`\>

---



[Source](https:/img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/scenelayout)