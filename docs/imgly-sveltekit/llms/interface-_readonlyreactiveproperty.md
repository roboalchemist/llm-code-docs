# Interface: \_ReadonlyReactiveProperty

A read-only reactive property with subscribe and value methods

## Type Parameters[#](#type-parameters)

| Type Parameter |
| --- |
| `T` |

## Properties[#](#properties)

| Property | Type | Description |
| --- | --- | --- |
| `subscribe` | (`listener`) => [`_Unsubscribe`](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/unsubscribe/) | Subscribe to value changes |
| `value` | () => `T` | Get current value |

---



[Source](https:/img.ly/docs/cesdk/sveltekit/api/engine/interfaces/reactor)