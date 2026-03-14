# Source: https://mikro-orm.io/api/core/class/MetadataProvider.md

# MetadataProvider<!-- -->

### Hierarchy

* *MetadataProvider*
  * [TsMorphMetadataProvider](https://mikro-orm.io/api/reflection/class/TsMorphMetadataProvider.md)

## Index[**](#index)

### Constructors

* [**constructor](#constructor)

### Methods

* [**combineCache](#combinecache)
* [**getCachedMetadata](#getcachedmetadata)
* [**getCacheKey](#getcachekey)
* [**loadEntityMetadata](#loadentitymetadata)
* [**loadFromCache](#loadfromcache)
* [**saveToCache](#savetocache)
* [**useCache](#usecache)
* [**useCache](#usecache)

## Constructors<!-- -->[**](#constructors)

### [**](#constructor)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/MetadataProvider.ts#L17)constructor

* ****new MetadataProvider**(config): [MetadataProvider](https://mikro-orm.io/api/core/class/MetadataProvider.md)

* #### Parameters

  * ##### config: [IConfiguration](https://mikro-orm.io/api/core/interface/IConfiguration.md)

  #### Returns [MetadataProvider](https://mikro-orm.io/api/core/class/MetadataProvider.md)

## Methods<!-- -->[**](#methods)

### [**](#combinecache)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/MetadataProvider.ts#L106)combineCache

* ****combineCache**(): void

* #### Returns void

### [**](#getcachedmetadata)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/MetadataProvider.ts#L88)getCachedMetadata

* ****getCachedMetadata**\<T>(meta, root): undefined | [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<T, [EntityCtor](https://mikro-orm.io/api/core.md#EntityCtor)\<T>>

* #### Parameters

  * ##### meta: Pick<[EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<T, [EntityCtor](https://mikro-orm.io/api/core.md#EntityCtor)\<T>>, className | path | root>

  * ##### root: [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<T, [EntityCtor](https://mikro-orm.io/api/core.md#EntityCtor)\<T>>

  #### Returns undefined | [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<T, [EntityCtor](https://mikro-orm.io/api/core.md#EntityCtor)\<T>>

### [**](#getcachekey)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/MetadataProvider.ts#L115)getCacheKey

* ****getCacheKey**(meta): string

* #### Parameters

  * ##### meta: Pick<[EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<any, [EntityCtor](https://mikro-orm.io/api/core.md#EntityCtor)\<any>>, className | path>

  #### Returns string

### [**](#loadentitymetadata)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/MetadataProvider.ts#L19)loadEntityMetadata

* ****loadEntityMetadata**(meta): void

* #### Parameters

  * ##### meta: [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<any, [EntityCtor](https://mikro-orm.io/api/core.md#EntityCtor)\<any>>

  #### Returns void

### [**](#loadfromcache)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/MetadataProvider.ts#L39)loadFromCache

* ****loadFromCache**(meta, cache): void

* #### Parameters

  * ##### meta: [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<any, [EntityCtor](https://mikro-orm.io/api/core.md#EntityCtor)\<any>>

  * ##### cache: [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<any, [EntityCtor](https://mikro-orm.io/api/core.md#EntityCtor)\<any>>

  #### Returns void

### [**](#savetocache)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/MetadataProvider.ts#L84)saveToCache

* ****saveToCache**(meta): void

* #### Parameters

  * ##### meta: [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<any, [EntityCtor](https://mikro-orm.io/api/core.md#EntityCtor)\<any>>

  #### Returns void

### [**](#usecache)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/MetadataProvider.ts#L80)useCache

* ****useCache**(): boolean

* #### Returns boolean

### [**](#usecache)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/MetadataProvider.ts#L76)staticuseCache

* ****useCache**(): boolean

* #### Returns boolean
