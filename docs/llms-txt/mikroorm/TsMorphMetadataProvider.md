# Source: https://mikro-orm.io/api/reflection/class/TsMorphMetadataProvider.md

# TsMorphMetadataProvider<!-- -->

### Hierarchy

* [MetadataProvider](https://mikro-orm.io/api/core/class/MetadataProvider.md)
  * *TsMorphMetadataProvider*

## Index[**](#index)

### Constructors

* [**constructor](#constructor)

### Methods

* [**combineCache](#combineCache)
* [**getCachedMetadata](#getCachedMetadata)
* [**getCacheKey](#getcachekey)
* [**getExistingSourceFile](#getexistingsourcefile)
* [**loadEntityMetadata](#loadentitymetadata)
* [**loadFromCache](#loadFromCache)
* [**saveToCache](#savetocache)
* [**useCache](#usecache)
* [**useCache](#usecache)

## Constructors<!-- -->[**](#constructors)

### [**](#constructor)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/MetadataProvider.ts#L17)constructor

* ****new TsMorphMetadataProvider**(config): [TsMorphMetadataProvider](https://mikro-orm.io/api/reflection/class/TsMorphMetadataProvider.md)

* Inherited from MetadataProvider.constructor

  #### Parameters

  * ##### config: [IConfiguration](https://mikro-orm.io/api/core/interface/IConfiguration.md)

  #### Returns [TsMorphMetadataProvider](https://mikro-orm.io/api/reflection/class/TsMorphMetadataProvider.md)

## Methods<!-- -->[**](#methods)

### [**](#combineCache)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/MetadataProvider.ts#L106)inheritedcombineCache

* ****combineCache**(): void

* Inherited from MetadataProvider.combineCache

  #### Returns void

### [**](#getCachedMetadata)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/MetadataProvider.ts#L88)inheritedgetCachedMetadata

* ****getCachedMetadata**\<T>(meta, root): undefined | [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<T, [EntityCtor](https://mikro-orm.io/api/core.md#EntityCtor)\<T>>

* Inherited from MetadataProvider.getCachedMetadata

  #### Parameters

  * ##### meta: Pick<[EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<T, [EntityCtor](https://mikro-orm.io/api/core.md#EntityCtor)\<T>>, className | path | root>

  * ##### root: [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<T, [EntityCtor](https://mikro-orm.io/api/core.md#EntityCtor)\<T>>

  #### Returns undefined | [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<T, [EntityCtor](https://mikro-orm.io/api/core.md#EntityCtor)\<T>>

### [**](#getcachekey)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/reflection/src/TsMorphMetadataProvider.ts#L343)getCacheKey

* ****getCacheKey**(meta): string

* Overrides MetadataProvider.getCacheKey

  #### Parameters

  * ##### meta: Pick<[EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<any, [EntityCtor](https://mikro-orm.io/api/core.md#EntityCtor)\<any>>, className | path>

  #### Returns string

### [**](#getexistingsourcefile)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/reflection/src/TsMorphMetadataProvider.ts#L46)getExistingSourceFile

* ****getExistingSourceFile**(path, ext, validate): SourceFile

* #### Parameters

  * ##### path: string

  * ##### optionalext: string

  * ##### validate: boolean = <!-- -->true

  #### Returns SourceFile

### [**](#loadentitymetadata)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/reflection/src/TsMorphMetadataProvider.ts#L38)loadEntityMetadata

* ****loadEntityMetadata**(meta): void

* Overrides MetadataProvider.loadEntityMetadata

  #### Parameters

  * ##### meta: [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<any, [EntityCtor](https://mikro-orm.io/api/core.md#EntityCtor)\<any>>

  #### Returns void

### [**](#loadFromCache)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/MetadataProvider.ts#L39)inheritedloadFromCache

* ****loadFromCache**(meta, cache): void

* Inherited from MetadataProvider.loadFromCache

  #### Parameters

  * ##### meta: [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<any, [EntityCtor](https://mikro-orm.io/api/core.md#EntityCtor)\<any>>

  * ##### cache: [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<any, [EntityCtor](https://mikro-orm.io/api/core.md#EntityCtor)\<any>>

  #### Returns void

### [**](#savetocache)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/reflection/src/TsMorphMetadataProvider.ts#L298)saveToCache

* ****saveToCache**(meta): void

* Overrides MetadataProvider.saveToCache

  #### Parameters

  * ##### meta: [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<any, [EntityCtor](https://mikro-orm.io/api/core.md#EntityCtor)\<any>>

  #### Returns void

### [**](#usecache)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/reflection/src/TsMorphMetadataProvider.ts#L34)useCache

* ****useCache**(): boolean

* Overrides MetadataProvider.useCache

  #### Returns boolean

### [**](#usecache)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/reflection/src/TsMorphMetadataProvider.ts#L30)staticuseCache

* ****useCache**(): boolean

* Overrides MetadataProvider.useCache

  #### Returns boolean
