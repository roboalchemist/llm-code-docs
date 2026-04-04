# Function: \_createReactiveProperty

```
function _createReactiveProperty<T>(initialValue, options?): _ReactiveProperty<T>;
```

Creates a reactive property with subscribe, value, and update methods.

This is the main utility for managing state with change notifications. Values are memoized by default (only emit when value changes).

## Type Parameters[#](#type-parameters)

| Type Parameter |
| --- |
| `T` |

## Parameters[#](#parameters)

| Parameter | Type | Description |
| --- | --- | --- |
| `initialValue` | `T` | The initial value of the property |
| `options?` | [`_ReactivePropertyOptions`](https://img.ly/docs/cesdk/vue/api/engine/interfaces/reactivepropertyoptions/)<`T`\> | Configuration options |

## Returns[#](#returns)

[`_ReactiveProperty`](https://img.ly/docs/cesdk/vue/api/engine/interfaces/reactiveproperty/)<`T`\>

A reactive property with subscribe, value, and update methods

## Example[#](#example)

```
// Simple valueconst zoom = createReactiveProperty(1.0);zoom.subscribe((value) => console.log('Zoom:', value));zoom.update(2.0); // Logs: "Zoom: 2.0"
// With custom equality for objectsconst settings = createReactiveProperty(  { width: 800, height: 600 },  { equals: isEqual });
// With initial value emissionconst formats = createReactiveProperty(  defaultFormats,  { emitOnSubscribe: true });
```

---



[Source](https:/img.ly/docs/cesdk/vue/api/engine/functions/createderivedproperty)