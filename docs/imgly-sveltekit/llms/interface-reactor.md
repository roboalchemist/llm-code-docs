# Interface: Reactor

The reactor coordinates the update of registered _Reactions_.

*   Reactions are created with `createReaction()`
*   `reaction.track(effect)` will run the effect and associate any engine read calls during the execution with the Reaction.
*   `reaction.subscribe(handler)` will invoke the handler whenever the engine read calls in the reaction might have changed after an update.

## Methods[#](#methods)

### createReaction()[#](#createreaction)

```
createReaction(debugName?): Reaction;
```

Create and return a new Reaction that is associated with this Reactor.

#### Parameters[#](#parameters)

| Parameter | Type |
| --- | --- |
| `debugName?` | `string` |

#### Returns[#](#returns)

[`Reaction`](https://img.ly/docs/cesdk/sveltekit/api/engine/interfaces/reaction/)

* * *

### dispose()[#](#dispose)

```
dispose(): void;
```

Dispose the reactor and all reactions. After this call, the reactor is no longer usable.

#### Returns[#](#returns-1)

`void`

## Properties[#](#properties)

| Property | Type | Description |
| --- | --- | --- |
| `nextReaction` | `Promise`<`void`\> | A promise that will resolve after the next update of the Reactor. This can be used to wait for the next update of the Reactor in an async function. `await reactor.nextReaction;` This is useful in situations where you want to make sure that the effects of a reactor update have propagated to any dependent code before continuing. Particularly, this can be used to ensure that the UI has updated before continuing with other operations. |

---



[Source](https:/img.ly/docs/cesdk/sveltekit/api/engine/interfaces/reactivepropertyoptions)