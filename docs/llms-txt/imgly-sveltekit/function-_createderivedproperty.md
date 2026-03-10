# Function: \_createDerivedProperty

```
function _createDerivedProperty<T, S>(   sources,   derive,options?): _ReadonlyReactiveProperty<T>;
```

Creates a derived reactive property from one or more sources.

The value is computed from source values using a derivation function. Updates are memoized (only emit when derived value changes).

## Type Parameters[#](#type-parameters)

| Type Parameter |
| --- |
| `T` |
| `S` _extends_ `any`\[\] |

## Parameters[#](#parameters)

| Parameter | Type | Description |
| --- | --- | --- |
| `sources` | { \[K in string | number |
| `derive` | (…`values`) => `T` | Function that computes the derived value from source values |
| `options?` | `Pick`<[`_ReactivePropertyOptions`](https://img.ly/docs/cesdk/sveltekit/api/engine/interfaces/reactivepropertyoptions/)<`T`\>, `"equals"`\> | Configuration options |

## Returns[#](#returns)

[`_ReadonlyReactiveProperty`](https://img.ly/docs/cesdk/sveltekit/api/engine/interfaces/readonlyreactiveproperty/)<`T`\>

A read-only reactive property

## Example[#](#example)

```
const width = createReactiveProperty(800);const height = createReactiveProperty(600);
const area = createDerivedProperty(  [width, height],  (w, h) => w * h);
area.subscribe((value) => console.log('Area:', value));width.update(1000); // Logs: "Area: 600000"
```

---



[Source](https:/img.ly/docs/cesdk/sveltekit/api/engine/functions/combineproperties)