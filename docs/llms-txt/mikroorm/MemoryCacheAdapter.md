# Source: https://mikro-orm.io/api/core/class/MemoryCacheAdapter.md

# MemoryCacheAdapter<!-- -->

### Implements

* [CacheAdapter](https://mikro-orm.io/api/core/interface/CacheAdapter.md)

## Index[**](#index)

### Constructors

* [**constructor](#constructor)

### Methods

* [**clear](#clear)
* [**get](#get)
* [**remove](#remove)
* [**set](#set)

## Constructors<!-- -->[**](#constructors)

### [**](#constructor)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/cache/MemoryCacheAdapter.ts#L7)constructor

* ****new MemoryCacheAdapter**(options): [MemoryCacheAdapter](https://mikro-orm.io/api/core/class/MemoryCacheAdapter.md)

* #### Parameters

  * ##### options: { expiration: number }

    * ##### expiration: number

  #### Returns [MemoryCacheAdapter](https://mikro-orm.io/api/core/class/MemoryCacheAdapter.md)

## Methods<!-- -->[**](#methods)

### [**](#clear)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/cache/MemoryCacheAdapter.ts#L45)clear

* ****clear**(): void

* Implementation of CacheAdapter.clear

  Clears all items stored in the cache.

  ***

  #### Returns void

### [**](#get)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/cache/MemoryCacheAdapter.ts#L14)get

* ****get**\<T>(name): undefined | T

* Implementation of CacheAdapter.get

  Gets the items under `name` key from the cache.

  ***

  #### Parameters

  * ##### name: string

  #### Returns undefined | T

### [**](#remove)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/cache/MemoryCacheAdapter.ts#L38)remove

* ****remove**(name): void

* Implementation of CacheAdapter.remove

  Removes the item from cache.

  ***

  #### Parameters

  * ##### name: string

  #### Returns void

### [**](#set)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/cache/MemoryCacheAdapter.ts#L31)set

* ****set**(name, data, origin, expiration): void

* Implementation of CacheAdapter.set

  Sets the item to the cache. `origin` is used for cache invalidation and should reflect the change in data.

  ***

  #### Parameters

  * ##### name: string

  * ##### data: any

  * ##### origin: string

  * ##### optionalexpiration: number

  #### Returns void
