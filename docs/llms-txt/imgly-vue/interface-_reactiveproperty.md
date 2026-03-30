# Interface: \_ReactiveProperty

A reactive property with subscribe, value, and update methods

## Type Parameters[#](#type-parameters)

| Type Parameter |
| --- |
| `T` |

## Properties[#](#properties)

| Property | Type | Description |
| --- | --- | --- |
| `subscribe` | (`listener`) => [`_Unsubscribe`](https://img.ly/docs/cesdk/vue/api/engine/type-aliases/unsubscribe/) | Subscribe to value changes |
| `value` | () => `T` | Get current value |
| `update` | (`newValue`) => `void` | Update the value (will notify listeners if changed) |

---



[Source](https:/img.ly/docs/cesdk/vue/api/engine/interfaces/range)