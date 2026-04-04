# Source: https://mikro-orm.io/api/core/class/GeneratedCacheAdapter.md

# GeneratedCacheAdapter<!-- -->

### Implements

* [CacheAdapter](https://mikro-orm.io/api/core/interface/CacheAdapter.md)

## Index[**](#Index)

### Constructors

* [**constructor](#constructor)

### Methods

* [**clear](#clear)
* [**get](#get)
* [**remove](#remove)
* [**set](#set)

## Constructors<!-- -->[**](#Constructors)

### [**](#constructor)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/cache/GeneratedCacheAdapter.ts#L8)constructor

* ****new GeneratedCacheAdapter**(options): [GeneratedCacheAdapter](https://mikro-orm.io/api/core/class/GeneratedCacheAdapter.md)

- #### Parameters

  * ##### options: { data: [Dictionary](https://mikro-orm.io/api/core.md#Dictionary) }
    * ##### data: [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)

  #### Returns [GeneratedCacheAdapter](https://mikro-orm.io/api/core/class/GeneratedCacheAdapter.md)

## Methods<!-- -->[**](#Methods)

### [**](#clear)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/cache/GeneratedCacheAdapter.ts#L39)clear

* ****clear**(): void

- Implementation of CacheAdapter.clear

  Clears all items stored in the cache.

  ***

  #### Returns void

### [**](#get)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/cache/GeneratedCacheAdapter.ts#L15)get

* ****get**\<T>(name): undefined | T

- Implementation of CacheAdapter.get

  Gets the items under `name` key from the cache.

  ***

  #### Parameters

  * ##### name: string

  #### Returns undefined | T

### [**](#remove)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/cache/GeneratedCacheAdapter.ts#L32)remove

* ****remove**(name): void

- Implementation of CacheAdapter.remove

  Removes the item from cache.

  ***

  #### Parameters

  * ##### name: string

  #### Returns void

### [**](#set)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/cache/GeneratedCacheAdapter.ts#L25)set

* ****set**(name, data, origin): void

- Implementation of CacheAdapter.set

  Sets the item to the cache. `origin` is used for cache invalidation and should reflect the change in data.

  ***

  #### Parameters

  * ##### name: string
  * ##### data: any
  * ##### origin: string

  #### Returns void
