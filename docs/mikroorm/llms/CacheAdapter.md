# Source: https://mikro-orm.io/api/core/interface/CacheAdapter.md

# CacheAdapter<!-- -->

### Hierarchy

* *CacheAdapter*
  * [SyncCacheAdapter](https://mikro-orm.io/api/core/interface/SyncCacheAdapter.md)

### Implemented by

* [GeneratedCacheAdapter](https://mikro-orm.io/api/core/class/GeneratedCacheAdapter.md)
* [MemoryCacheAdapter](https://mikro-orm.io/api/core/class/MemoryCacheAdapter.md)

## Index[**](#index)

### Methods

* [**clear](#clear)
* [**close](#close)
* [**get](#get)
* [**remove](#remove)
* [**set](#set)

## Methods<!-- -->[**](#methods)

### [**](#clear)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/cache/CacheAdapter.ts#L20)clear

* ****clear**(): void | Promise\<void>

* Clears all items stored in the cache.

  ***

  #### Returns void | Promise\<void>

### [**](#close)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/cache/CacheAdapter.ts#L25)optionalclose

* ****close**(): void | Promise\<void>

* Called inside `MikroORM.close()` Allows graceful shutdowns (e.g. for redis).

  ***

  #### Returns void | Promise\<void>

### [**](#get)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/cache/CacheAdapter.ts#L5)get

* ****get**\<T>(name): undefined | T | Promise\<undefined | T>

* Gets the items under `name` key from the cache.

  ***

  #### Parameters

  * ##### name: string

  #### Returns undefined | T | Promise\<undefined | T>

### [**](#remove)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/cache/CacheAdapter.ts#L15)remove

* ****remove**(name): void | Promise\<void>

* Removes the item from cache.

  ***

  #### Parameters

  * ##### name: string

  #### Returns void | Promise\<void>

### [**](#set)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/cache/CacheAdapter.ts#L10)set

* ****set**(name, data, origin, expiration): void | Promise\<void>

* Sets the item to the cache. `origin` is used for cache invalidation and should reflect the change in data.

  ***

  #### Parameters

  * ##### name: string

  * ##### data: any

  * ##### origin: string

  * ##### optionalexpiration: number

  #### Returns void | Promise\<void>
