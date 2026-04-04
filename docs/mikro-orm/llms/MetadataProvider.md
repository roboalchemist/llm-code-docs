# Source: https://mikro-orm.io/api/core/class/MetadataProvider.md

# abstractMetadataProvider<!-- -->

### Hierarchy

* *MetadataProvider*

  * [ReflectMetadataProvider](https://mikro-orm.io/api/core/class/ReflectMetadataProvider.md)
  * [TsMorphMetadataProvider](https://mikro-orm.io/api/reflection/class/TsMorphMetadataProvider.md)

## Index[**](#Index)

### Constructors

* [**constructor](#constructor)

### Methods

* [**loadEntityMetadata](#loadEntityMetadata)
* [**loadFromCache](#loadFromCache)
* [**useCache](#useCache)

## Constructors<!-- -->[**](#Constructors)

### [**](#constructor)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/metadata/MetadataProvider.ts#L13)constructor

* ****new MetadataProvider**(config): [MetadataProvider](https://mikro-orm.io/api/core/class/MetadataProvider.md)

- #### Parameters

  * ##### config: [IConfiguration](https://mikro-orm.io/api/core/interface/IConfiguration.md)

  #### Returns [MetadataProvider](https://mikro-orm.io/api/core/class/MetadataProvider.md)

## Methods<!-- -->[**](#Methods)

### [**](#loadEntityMetadata)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/metadata/MetadataProvider.ts#L15)abstractloadEntityMetadata

* ****loadEntityMetadata**(meta, name): void

- #### Parameters

  * ##### meta: [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<any>
  * ##### name: string

  #### Returns void

### [**](#loadFromCache)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/metadata/MetadataProvider.ts#L17)loadFromCache

* ****loadFromCache**(meta, cache): void

- #### Parameters

  * ##### meta: [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<any>
  * ##### cache: [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<any>

  #### Returns void

### [**](#useCache)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/metadata/MetadataProvider.ts#L29)useCache

* ****useCache**(): boolean

- #### Returns boolean
