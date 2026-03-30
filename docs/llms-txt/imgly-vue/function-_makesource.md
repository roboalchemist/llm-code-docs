# Function: \_makeSource

```
function _makeSource<T>(): _Source<T>;
```

Creates a simple event source that can emit values to subscribed listeners.

This is the most basic building block - a pub/sub pattern without state management.

## Type Parameters[#](#type-parameters)

| Type Parameter |
| --- |
| `T` |

## Returns[#](#returns)

[`_Source`](https://img.ly/docs/cesdk/vue/api/engine/interfaces/source-1/)<`T`\>

A source function with an emit method

## Example[#](#example)

```
const onResize = makeSource<{ width: number; height: number }>();
// Subscribeconst unsubscribe = onResize((size) => {  console.log('New size:', size);});
// EmitonResize.emit({ width: 800, height: 600 });
// Cleanupunsubscribe();
```

---



[Source](https:/img.ly/docs/cesdk/vue/api/engine/functions/isrgbacolor)