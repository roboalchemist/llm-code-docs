# Source: https://mikro-orm.io/api/core/class/ReflectMetadataProvider.md

# ReflectMetadataProvider<!-- -->

### Hierarchy

* [MetadataProvider](https://mikro-orm.io/api/core/class/MetadataProvider.md)
  * *ReflectMetadataProvider*

## Index[**](#Index)

### Constructors

* [**constructor](#constructor)

### Methods

* [**loadEntityMetadata](#loadEntityMetadata)
* [**loadFromCache](#loadFromCache)
* [**useCache](#useCache)

## Constructors<!-- -->[**](#Constructors)

### [**](#constructor)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/metadata/MetadataProvider.ts#L13)constructor

* ****new ReflectMetadataProvider**(config): [ReflectMetadataProvider](https://mikro-orm.io/api/core/class/ReflectMetadataProvider.md)

- Inherited from MetadataProvider.constructor

  #### Parameters

  * ##### config: [IConfiguration](https://mikro-orm.io/api/core/interface/IConfiguration.md)

  #### Returns [ReflectMetadataProvider](https://mikro-orm.io/api/core/class/ReflectMetadataProvider.md)

## Methods<!-- -->[**](#Methods)

### [**](#loadEntityMetadata)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/metadata/ReflectMetadataProvider.ts#L9)loadEntityMetadata

* ****loadEntityMetadata**(meta, name): void

- Overrides MetadataProvider.loadEntityMetadata

  #### Parameters

  * ##### meta: [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<any>
  * ##### name: string

  #### Returns void

### [**](#loadFromCache)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/metadata/MetadataProvider.ts#L17)inheritedloadFromCache

* ****loadFromCache**(meta, cache): void

- Inherited from MetadataProvider.loadFromCache

  #### Parameters

  * ##### meta: [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<any>
  * ##### cache: [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<any>

  #### Returns void

### [**](#useCache)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/metadata/MetadataProvider.ts#L29)inheriteduseCache

* ****useCache**(): boolean

- Inherited from MetadataProvider.useCache

  #### Returns boolean
