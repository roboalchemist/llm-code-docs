# Interface: \_ReactivePropertyOptions

Options for creating a reactive property

## Type Parameters[#](#type-parameters)

| Type Parameter |
| --- |
| `T` |

## Properties[#](#properties)

| Property | Type | Description |
| --- | --- | --- |
| `equals?` | [`_EqualsFn`](https://img.ly/docs/cesdk/vue/api/engine/type-aliases/equalsfn/)<`T`\> | Equality comparison function (default: strict equality) |
| `emitOnSubscribe?` | `boolean` | If true, emit the initial value to new subscribers |
| `trackSource?` | (`listener`) => [`_Unsubscribe`](https://img.ly/docs/cesdk/vue/api/engine/type-aliases/unsubscribe/) | Optional source to track (will subscribe and forward updates) |

---



[Source](https:/img.ly/docs/cesdk/vue/api/engine/interfaces/reactiveproperty)