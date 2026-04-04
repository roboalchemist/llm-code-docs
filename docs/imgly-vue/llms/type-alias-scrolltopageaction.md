# Type Alias: ScrollToPageAction

```
type ScrollToPageAction = (options?) => Promise<void>;
```

Action function for scrolling to a specific page

## Parameters[#](#parameters)

| Parameter | Type | Description |
| --- | --- | --- |
| `options?` | { `pageId?`: `number`; `animate?`: `boolean`; } | \- |
| `options.pageId?` | `number` | The page ID to scroll to (defaults to current page) |
| `options.animate?` | `boolean` | Whether to animate the scroll (default: false) |

## Returns[#](#returns)

`Promise`<`void`\>

---



[Source](https:/img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/scope)