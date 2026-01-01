# Source: https://mikro-orm.io/api/core/class/NullCacheAdapter.md

# NullCacheAdapter<!-- -->

### Implements

* [SyncCacheAdapter](https://mikro-orm.io/api/core/interface/SyncCacheAdapter.md)

## Index[**](#Index)

### Constructors

* [**constructor](#constructor)

### Methods

* [**clear](#clear)
* [**get](#get)
* [**remove](#remove)
* [**set](#set)

## Constructors<!-- -->[**](#Constructors)

### [**](#constructor)constructor

* ****new NullCacheAdapter**(): [NullCacheAdapter](https://mikro-orm.io/api/core/class/NullCacheAdapter.md)

- #### Returns [NullCacheAdapter](https://mikro-orm.io/api/core/class/NullCacheAdapter.md)

## Methods<!-- -->[**](#Methods)

### [**](#clear)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/cache/NullCacheAdapter.ts#L29)clear

* ****clear**(): void

- Implementation of SyncCacheAdapter.clear

  Clears all items stored in the cache.

  ***

  #### Returns void

### [**](#get)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/cache/NullCacheAdapter.ts#L8)get

* ****get**(name): any

- Implementation of SyncCacheAdapter.get

  Gets the items under `name` key from the cache.

  ***

  #### Parameters

  * ##### name: string

  #### Returns any

### [**](#remove)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/cache/NullCacheAdapter.ts#L22)remove

* ****remove**(name): void

- Implementation of SyncCacheAdapter.remove

  Removes the item from cache.

  ***

  #### Parameters

  * ##### name: string

  #### Returns void

### [**](#set)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/cache/NullCacheAdapter.ts#L15)set

* ****set**(name, data, origin): void

- Implementation of SyncCacheAdapter.set

  Sets the item to the cache. `origin` is used for cache invalidation and should reflect the change in data.

  ***

  #### Parameters

  * ##### name: string
  * ##### data: any
  * ##### origin: string

  #### Returns void
