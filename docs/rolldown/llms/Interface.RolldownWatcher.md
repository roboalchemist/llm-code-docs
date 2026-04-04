# Source: https://rolldown.rs/reference/Interface.RolldownWatcher.md

---
url: /reference/Interface.RolldownWatcher.md
---
# Interface: RolldownWatcher

## Methods

### clear()

* **Type**: (`event`: `E`) => `void`

Unregister all listeners for a specific event defined in [`RolldownWatcherWatcherEventMap`](TypeAlias.RolldownWatcherWatcherEventMap.md).

#### Type Parameters

##### E

`E` *extends* keyof [`RolldownWatcherWatcherEventMap`](TypeAlias.RolldownWatcherWatcherEventMap.md)

#### Parameters

##### event

`E`

#### Returns

`void`

***

### close()

* **Type**: () => `Promise`<`void`>

Close the watcher and stop listening for file changes.

#### Returns

`Promise`<`void`>

***

### off()

* **Type**: (`event`: `E`, `listener`: (...`args`) => `MaybePromise`<`void`>) => `this`

Unregister a listener for events defined in [`RolldownWatcherWatcherEventMap`](TypeAlias.RolldownWatcherWatcherEventMap.md).

#### Type Parameters

##### E

`E` *extends* keyof [`RolldownWatcherWatcherEventMap`](TypeAlias.RolldownWatcherWatcherEventMap.md)

#### Parameters

##### event

`E`

##### listener

(...`args`) => `MaybePromise`<`void`>

#### Returns

`this`

***

### on()

* **Type**: (`event`: `E`, `listener`: (...`args`) => `MaybePromise`<`void`>) => `this`

Register a listener for events defined in [`RolldownWatcherWatcherEventMap`](TypeAlias.RolldownWatcherWatcherEventMap.md).

#### Type Parameters

##### E

`E` *extends* keyof [`RolldownWatcherWatcherEventMap`](TypeAlias.RolldownWatcherWatcherEventMap.md)

#### Parameters

##### event

`E`

##### listener

(...`args`) => `MaybePromise`<`void`>

#### Returns

`this`
