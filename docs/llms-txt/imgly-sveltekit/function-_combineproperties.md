# Function: \_combineProperties

```
function _combineProperties<T>(properties, options?): _ReadonlyReactiveProperty<T>;
```

Combines multiple reactive properties into a single reactive property.

Similar to `combineLatest` from RxJS but simpler. Emits whenever any source emits.

## Type Parameters[#](#type-parameters)

| Type Parameter |
| --- |
| `T` _extends_ `any`\[\] |

## Parameters[#](#parameters)

| Parameter | Type | Description |
| --- | --- | --- |
| `properties` | { \[K in string | number |
| `options?` | `Pick`<[`_ReactivePropertyOptions`](https://img.ly/docs/cesdk/sveltekit/api/engine/interfaces/reactivepropertyoptions/)<`T`\>, `"equals"`\> | Configuration options |

## Returns[#](#returns)

[`_ReadonlyReactiveProperty`](https://img.ly/docs/cesdk/sveltekit/api/engine/interfaces/readonlyreactiveproperty/)<`T`\>

A reactive property containing an array of values

## Example[#](#example)

```
const x = createReactiveProperty(0);const y = createReactiveProperty(0);
const position = combineProperties([x, y]);
position.subscribe(([xVal, yVal]) => {  console.log(`Position: (${xVal}, ${yVal})`);});
```

---



[Source](https:/img.ly/docs/cesdk/sveltekit/api/engine/functions/checkvideosupport)