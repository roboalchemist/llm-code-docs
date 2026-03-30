# Interface: Reaction

Reactions track read calls and provide a way to react if they change.

*   Read calls are tracked by passing a function to `track`. That function will be executed, and any read calls made during that execution will be tracked and associated with this reaction.
*   Reactions can be subscribed to by passing a callback to `subscribe`. That callback will be executed whenever any of the read calls associated with this reaction change.

## Methods[#](#methods)

### track()[#](#track)

```
track<T>(cb): T;
```

Execute the callback and track all engine read calls that happen during the execution. These read calls are associated with this reaction.

#### Type Parameters[#](#type-parameters)

| Type Parameter |
| --- |
| `T` |

#### Parameters[#](#parameters)

| Parameter | Type |
| --- | --- |
| `cb` | () => `T` |

#### Returns[#](#returns)

`T`

* * *

### subscribe()[#](#subscribe)

```
subscribe(cb): () => void;
```

When the Reactor detects that the engine read calls associated with this reaction might have changed, it will invoke the subscription handler.

#### Parameters[#](#parameters-1)

| Parameter | Type |
| --- | --- |
| `cb` | () => `void` |

#### Returns[#](#returns-1)

A function that can be called to unsubscribe the handler.

```
(): void;
```

##### Returns[#](#returns-2)

`void`

* * *

### dispose()[#](#dispose)

```
dispose(): void;
```

Unsubscribe all handlers, nullify the reference to the Reactor and dispose the reaction.

#### Returns[#](#returns-3)

`void`

---



[Source](https:/img.ly/docs/cesdk/vue/api/engine/interfaces/reactivepropertyoptions)