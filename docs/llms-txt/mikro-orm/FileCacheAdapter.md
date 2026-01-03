# Source: https://mikro-orm.io/api/core/class/FileCacheAdapter.md

# FileCacheAdapter<!-- -->

### Implements

* [SyncCacheAdapter](https://mikro-orm.io/api/core/interface/SyncCacheAdapter.md)

## Index[**](#Index)

### Constructors

* [**constructor](#constructor)

### Methods

* [**clear](#clear)
* [**combine](#combine)
* [**get](#get)
* [**remove](#remove)
* [**set](#set)

## Constructors<!-- -->[**](#Constructors)

### [**](#constructor)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/cache/FileCacheAdapter.ts#L13)constructor

* ****new FileCacheAdapter**(options, baseDir, pretty, hashAlgorithm): [FileCacheAdapter](https://mikro-orm.io/api/core/class/FileCacheAdapter.md)

- #### Parameters

  * ##### options: { cacheDir: string; combined?<!-- -->: string | boolean }
  * * ##### cacheDir: string
    * ##### optionalcombined: string | boolean
    ##### baseDir: string
  * ##### pretty: boolean = <!-- -->false
  * ##### hashAlgorithm: md5 | sha256 = <!-- -->'md5'

  #### Returns [FileCacheAdapter](https://mikro-orm.io/api/core/class/FileCacheAdapter.md)

## Methods<!-- -->[**](#Methods)

### [**](#clear)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/cache/FileCacheAdapter.ts#L64)clear

* ****clear**(): void

- Implementation of SyncCacheAdapter.clear

  Clears all items stored in the cache.

  ***

  #### Returns void

### [**](#combine)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/cache/FileCacheAdapter.ts#L71)combine

* ****combine**(): string | void

- Implementation of SyncCacheAdapter.combine

  Generates a combined cache from all existing entries.

  ***

  #### Returns string | void

### [**](#get)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/cache/FileCacheAdapter.ts#L21)get

* ****get**(name): any

- Implementation of SyncCacheAdapter.get

  Gets the items under `name` key from the cache.

  ***

  #### Parameters

  * ##### name: string

  #### Returns any

### [**](#remove)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/cache/FileCacheAdapter.ts#L56)remove

* ****remove**(name): void

- Implementation of SyncCacheAdapter.remove

  Removes the item from cache.

  ***

  #### Parameters

  * ##### name: string

  #### Returns void

### [**](#set)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/cache/FileCacheAdapter.ts#L41)set

* ****set**(name, data, origin): void

- Implementation of SyncCacheAdapter.set

  Sets the item to the cache. `origin` is used for cache invalidation and should reflect the change in data.

  ***

  #### Parameters

  * ##### name: string
  * ##### data: any
  * ##### origin: string

  #### Returns void
