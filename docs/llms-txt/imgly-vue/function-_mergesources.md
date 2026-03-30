# Function: \_mergeSources

```
function _mergeSources(...sources): (listener) => _Unsubscribe;
```

Merges multiple event sources into a single source that emits when any source emits.

This is useful for tracking properties that depend on multiple independent events.

## Parameters[#](#parameters)

| Parameter | Type | Description |
| --- | --- | --- |
| …`sources` | (`listener`) => [`_Unsubscribe`](https://img.ly/docs/cesdk/vue/api/engine/type-aliases/unsubscribe/)\[\] | Event source functions to merge |

## Returns[#](#returns)

A merged source that emits when any source emits

```
(listener): _Unsubscribe;
```

### Parameters[#](#parameters-1)

| Parameter | Type |
| --- | --- |
| `listener` | [`_Listener`](https://img.ly/docs/cesdk/vue/api/engine/type-aliases/listener/)<`void`\> |

### Returns[#](#returns-1)

[`_Unsubscribe`](https://img.ly/docs/cesdk/vue/api/engine/type-aliases/unsubscribe/)

## Example[#](#example)

```
const zoomChanged = engine.scene.onZoomLevelChanged;const dpiChanged = engine.scene.onDpiChanged;
const zoomOrDpiChanged = mergeSources(zoomChanged, dpiChanged);
// Now use with createTrackedPropertyconst normalizedZoom = createTrackedProperty(  () => engine.scene.getZoomLevel() / getDpi(),  (value) => engine.scene.setZoomLevel(value * getDpi()),  zoomOrDpiChanged);
```

---



[Source](https:/img.ly/docs/cesdk/vue/api/engine/functions/isspotcolor)