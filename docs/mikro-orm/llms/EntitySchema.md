# Source: https://mikro-orm.io/api/core/class/EntitySchema.md

# EntitySchema<!-- --> \<Entity, Base>

## Index[**](#Index)

### Constructors

* [**constructor](#constructor)

### Properties

* [**REGISTRY](#REGISTRY)

### Accessors

* [**meta](#meta)
* [**name](#name)

### Methods

* [**addEmbedded](#addEmbedded)
* [**addEnum](#addEnum)
* [**addIndex](#addIndex)
* [**addManyToMany](#addManyToMany)
* [**addManyToOne](#addManyToOne)
* [**addOneToMany](#addOneToMany)
* [**addOneToOne](#addOneToOne)
* [**addPrimaryKey](#addPrimaryKey)
* [**addProperty](#addProperty)
* [**addSerializedPrimaryKey](#addSerializedPrimaryKey)
* [**addUnique](#addUnique)
* [**addVersion](#addVersion)
* [**setClass](#setClass)
* [**setCustomRepository](#setCustomRepository)
* [**setExtends](#setExtends)
* [**fromMetadata](#fromMetadata)

## Constructors<!-- -->[**](#Constructors)

### [**](#constructor)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/metadata/EntitySchema.ts#L65)constructor

* ****new EntitySchema**\<Entity, Base>(meta): [EntitySchema](https://mikro-orm.io/api/core/class/EntitySchema.md)\<Entity, Base>

- #### Parameters

  * ##### meta: [EntitySchemaMetadata](https://mikro-orm.io/api/core.md#EntitySchemaMetadata)\<Entity, Base>

  #### Returns [EntitySchema](https://mikro-orm.io/api/core/class/EntitySchema.md)\<Entity, Base>

## Properties<!-- -->[**](#Properties)

### [**](#REGISTRY)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/metadata/EntitySchema.ts#L59)staticREGISTRY

**REGISTRY: Map\<Partial\<any>, [EntitySchema](https://mikro-orm.io/api/core/class/EntitySchema.md)\<any, never>> =

<!-- -->

...

When schema links the entity class via `class` option, this registry allows the lookup from opposite side, so we can use the class in `entities` option just like the EntitySchema instance.

## Accessors<!-- -->[**](#Accessors)

### [**](#meta)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/metadata/EntitySchema.ts#L269)meta

* **get meta(): [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<Entity>

- #### Returns [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<Entity>

### [**](#name)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/metadata/EntitySchema.ts#L273)name

* **get name(): [EntityName](https://mikro-orm.io/api/core.md#EntityName)\<Entity>

- #### Returns [EntityName](https://mikro-orm.io/api/core.md#EntityName)\<Entity>

## Methods<!-- -->[**](#Methods)

### [**](#addEmbedded)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/metadata/EntitySchema.ts#L150)addEmbedded

* ****addEmbedded**\<Target>(name, options): void

- #### Parameters

  * ##### name: [EntityKey](https://mikro-orm.io/api/core.md#EntityKey)\<Entity>
  * ##### options: [EmbeddedOptions](https://mikro-orm.io/api/core/interface/EmbeddedOptions.md)\<Entity, Target>

  #### Returns void

### [**](#addEnum)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/metadata/EntitySchema.ts#L112)addEnum

* ****addEnum**(name, type, options): void

- #### Parameters

  * ##### name: [EntityKey](https://mikro-orm.io/api/core.md#EntityKey)\<Entity>
  * ##### optionaltype: TypeType
  * ##### options: [EnumOptions](https://mikro-orm.io/api/core/interface/EnumOptions.md)\<Entity> = <!-- -->{}

  #### Returns void

### [**](#addIndex)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/metadata/EntitySchema.ts#L232)addIndex

* ****addIndex**\<Key>(options): void

- #### Parameters

  * ##### options: [IndexOptions](https://mikro-orm.io/api/core/interface/IndexOptions.md)\<Entity, Key>

  #### Returns void

### [**](#addManyToMany)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/metadata/EntitySchema.ts#L184)addManyToMany

* ****addManyToMany**\<Target>(name, type, options): void

- #### Parameters

  * ##### name: [EntityKey](https://mikro-orm.io/api/core.md#EntityKey)\<Entity>
  * ##### type: TypeType
  * ##### options: [ManyToManyOptions](https://mikro-orm.io/api/core/interface/ManyToManyOptions.md)\<Entity, Target>

  #### Returns void

### [**](#addManyToOne)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/metadata/EntitySchema.ts#L166)addManyToOne

* ****addManyToOne**\<Target>(name, type, options): void

- #### Parameters

  * ##### name: [EntityKey](https://mikro-orm.io/api/core.md#EntityKey)\<Entity>
  * ##### type: TypeType
  * ##### options: [ManyToOneOptions](https://mikro-orm.io/api/core/interface/ManyToOneOptions.md)\<Entity, Target>

  #### Returns void

### [**](#addOneToMany)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/metadata/EntitySchema.ts#L202)addOneToMany

* ****addOneToMany**\<Target>(name, type, options): void

- #### Parameters

  * ##### name: [EntityKey](https://mikro-orm.io/api/core.md#EntityKey)\<Entity>
  * ##### type: TypeType
  * ##### options: [OneToManyOptions](https://mikro-orm.io/api/core/interface/OneToManyOptions.md)\<Entity, Target>

  #### Returns void

### [**](#addOneToOne)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/metadata/EntitySchema.ts#L207)addOneToOne

* ****addOneToOne**\<Target>(name, type, options): void

- #### Parameters

  * ##### name: [EntityKey](https://mikro-orm.io/api/core.md#EntityKey)\<Entity>
  * ##### type: TypeType
  * ##### options: [OneToOneOptions](https://mikro-orm.io/api/core/interface/OneToOneOptions.md)\<Entity, Target>

  #### Returns void

### [**](#addPrimaryKey)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/metadata/EntitySchema.ts#L141)addPrimaryKey

* ****addPrimaryKey**(name, type, options): void

- #### Parameters

  * ##### name: [EntityKey](https://mikro-orm.io/api/core.md#EntityKey)\<Entity>
  * ##### type: TypeType
  * ##### options: [PrimaryKeyOptions](https://mikro-orm.io/api/core/interface/PrimaryKeyOptions.md)\<Entity> = <!-- -->{}

  #### Returns void

### [**](#addProperty)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/metadata/EntitySchema.ts#L92)addProperty

* ****addProperty**(name, type, options): void

- #### Parameters

  * ##### name: [EntityKey](https://mikro-orm.io/api/core.md#EntityKey)\<Entity>
  * ##### optionaltype: TypeType
  * ##### options: [PropertyOptions](https://mikro-orm.io/api/core/interface/PropertyOptions.md)\<Entity> | [EntityProperty](https://mikro-orm.io/api/core/interface/EntityProperty.md)\<Entity, any> = <!-- -->{}

  #### Returns void

### [**](#addSerializedPrimaryKey)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/metadata/EntitySchema.ts#L145)addSerializedPrimaryKey

* ****addSerializedPrimaryKey**(name, type, options): void

- #### Parameters

  * ##### name: [EntityKey](https://mikro-orm.io/api/core.md#EntityKey)\<Entity>
  * ##### type: TypeType
  * ##### options: [SerializedPrimaryKeyOptions](https://mikro-orm.io/api/core/interface/SerializedPrimaryKeyOptions.md)\<Entity> = <!-- -->{}

  #### Returns void

### [**](#addUnique)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/metadata/EntitySchema.ts#L236)addUnique

* ****addUnique**\<Key>(options): void

- #### Parameters

  * ##### options: [UniqueOptions](https://mikro-orm.io/api/core/interface/UniqueOptions.md)\<Entity, Key>

  #### Returns void

### [**](#addVersion)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/metadata/EntitySchema.ts#L137)addVersion

* ****addVersion**(name, type, options): void

- #### Parameters

  * ##### name: [EntityKey](https://mikro-orm.io/api/core.md#EntityKey)\<Entity>
  * ##### type: TypeType
  * ##### options: [PropertyOptions](https://mikro-orm.io/api/core/interface/PropertyOptions.md)\<Entity> = <!-- -->{}

  #### Returns void

### [**](#setClass)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/metadata/EntitySchema.ts#L248)setClass

* ****setClass**(proto): void

- #### Parameters

  * ##### proto: [EntityClass](https://mikro-orm.io/api/core.md#EntityClass)\<Entity>

  #### Returns void

### [**](#setCustomRepository)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/metadata/EntitySchema.ts#L240)setCustomRepository

* ****setCustomRepository**(repository): void

- #### Parameters

  * ##### repository: () => [Constructor](https://mikro-orm.io/api/core.md#Constructor)


  #### Returns void

### [**](#setExtends)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/metadata/EntitySchema.ts#L244)setExtends

* ****setExtends**(base): void

- #### Parameters

  * ##### base: [EntityName](https://mikro-orm.io/api/core.md#EntityName)\<any>

  #### Returns void

### [**](#fromMetadata)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/metadata/EntitySchema.ts#L85)staticfromMetadata

* ****fromMetadata**\<T, U>(meta): [EntitySchema](https://mikro-orm.io/api/core/class/EntitySchema.md)\<T, U>

- #### Parameters

  * ##### meta: [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<T> | [DeepPartial](https://mikro-orm.io/api/core.md#DeepPartial)<[EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<T>>

  #### Returns [EntitySchema](https://mikro-orm.io/api/core/class/EntitySchema.md)\<T, U>
