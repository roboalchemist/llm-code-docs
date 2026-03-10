# Function: \_createTrackedProperty

```
function _createTrackedProperty<T, U>(   getter,   setter,   source,options?): _ReactiveProperty<T>;
```

Creates a reactive property that tracks a source and updates based on a getter/setter.

This is useful for wrapping engine properties or complex state logic.

## Type Parameters[#](#type-parameters)

| Type Parameter | Default type |
| --- | --- |
| `T` | \- |
| `U` | `any` |

## Parameters[#](#parameters)

| Parameter | Type | Description |
| --- | --- | --- |
| `getter` | () => `T` | Function to get current value |
| `setter` | (`value`) => `void` | Function to update value |
| `source` | (`listener`) => [`_Unsubscribe`](https://img.ly/docs/cesdk/vue/api/engine/type-aliases/unsubscribe/) | Source to track for updates |
| `options?` | `Pick`<[`_ReactivePropertyOptions`](https://img.ly/docs/cesdk/vue/api/engine/interfaces/reactivepropertyoptions/)<`T`\>, `"equals"`\> | Configuration options |

## Returns[#](#returns)

[`_ReactiveProperty`](https://img.ly/docs/cesdk/vue/api/engine/interfaces/reactiveproperty/)<`T`\>

A reactive property

## Example[#](#example)

```
const settings = createTrackedProperty(  // Getter  () => {    const camera = engine.block.findByType('camera')[0];    return {      width: engine.block.getFloat(camera, 'camera/resolution/width'),      height: engine.block.getFloat(camera, 'camera/resolution/height')    };  },  // Setter  ({ width, height }) => {    const camera = engine.block.findByType('camera')[0];    engine.block.setFloat(camera, 'camera/resolution/width', width);    engine.block.setFloat(camera, 'camera/resolution/height', height);  },  // Source to track  onCameraUpdated,  // Options  { equals: isEqual });
```

---



[Source](https:/img.ly/docs/cesdk/vue/api/engine/functions/createreactiveproperty)