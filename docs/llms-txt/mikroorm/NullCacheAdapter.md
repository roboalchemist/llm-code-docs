# Source: https://mikro-orm.io/api/core/class/NullCacheAdapter.md

# NullCacheAdapter<!-- -->

### Implements

* [SyncCacheAdapter](https://mikro-orm.io/api/core/interface/SyncCacheAdapter.md)

## Index[**](#index)

### Constructors

* [**constructor](#constructor)

### Methods

* [**clear](#clear)
* [**get](#get)
* [**remove](#remove)
* [**set](#set)

## Constructors<!-- -->[**](#constructors)

### [**](#constructor)constructor

* ****new NullCacheAdapter**(): [NullCacheAdapter](https://mikro-orm.io/api/core/class/NullCacheAdapter.md)

* #### Returns [NullCacheAdapter](https://mikro-orm.io/api/core/class/NullCacheAdapter.md)

## Methods<!-- -->[**](#methods)

### [**](#clear)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/cache/NullCacheAdapter.ts#L28)clear

* ****clear**(): void

* Implementation of SyncCacheAdapter.clear

  Clears all items stored in the cache.

  ***

  #### Returns void

### [**](#get)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/cache/NullCacheAdapter.ts#L7)get

* ****get**(name): any

* Implementation of SyncCacheAdapter.get

  Gets the items under `name` key from the cache.

  ***

  #### Parameters

  * ##### name: string

  #### Returns any

### [**](#remove)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/cache/NullCacheAdapter.ts#L21)remove

* ****remove**(name): void

* Implementation of SyncCacheAdapter.remove

  Removes the item from cache.

  ***

  #### Parameters

  * ##### name: string

  #### Returns void

### [**](#set)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/cache/NullCacheAdapter.ts#L14)set

* ****set**(name, data, origin): void

* Implementation of SyncCacheAdapter.set

  Sets the item to the cache. `origin` is used for cache invalidation and should reflect the change in data.

  ***

  #### Parameters

  * ##### name: string

  * ##### data: any

  * ##### origin: string

  #### Returns void
