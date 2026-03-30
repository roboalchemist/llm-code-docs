# Source: https://mikro-orm.io/api/core/interface/EntitySchemaWithMeta.md

# EntitySchemaWithMeta<!-- --> \<TName, TTableName, TEntity, TBase, TProperties, TClass>

### Hierarchy

* [EntitySchema](https://mikro-orm.io/api/core/class/EntitySchema.md)\<TEntity, TBase, TClass>
  * *EntitySchemaWithMeta*

## Index[**](#index)

### Properties

* [**name](#name)
* [**properties](#properties)
* [**tableName](#tableName)

### Accessors

* [**class](#class)
* [**meta](#meta)

### Methods

* [**addEmbedded](#addEmbedded)
* [**addEnum](#addEnum)
* [**addHook](#addHook)
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
* [**new](#new)
* [**setClass](#setClass)
* [**setCustomRepository](#setCustomRepository)
* [**setExtends](#setExtends)

## Properties<!-- -->[**](#properties)

### [**](#name)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1888)readonlyname

**name: TName

Overrides EntitySchema.name

### [**](#properties)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1889)readonlyproperties

**properties: TProperties

Overrides EntitySchema.properties

### [**](#tableName)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1890)readonlytableName

**tableName: TTableName

Overrides EntitySchema.tableName

## Accessors<!-- -->[**](#accessors)

### [**](#class)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/EntitySchema.ts#L340)inheritedclass

* **get class(): Class

* Inherited from EntitySchema.class

  #### Returns Class

### [**](#meta)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/EntitySchema.ts#L328)inheritedmeta

* **get meta(): [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<Entity, Class>

* Inherited from EntitySchema.meta

  #### Returns [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<Entity, Class>

## Methods<!-- -->[**](#methods)

### [**](#addEmbedded)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/EntitySchema.ts#L183)inheritedaddEmbedded

* ****addEmbedded**\<Target>(name, options): void

* Inherited from EntitySchema.addEmbedded

  #### Parameters

  * ##### name: [EntityKey](https://mikro-orm.io/api/core.md#EntityKey)\<TEntity>

  * ##### options: [EmbeddedOptions](https://mikro-orm.io/api/core/interface/EmbeddedOptions.md)\<TEntity, Target>

  #### Returns void

### [**](#addEnum)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/EntitySchema.ts#L141)inheritedaddEnum

* ****addEnum**(name, type, options): void

* Inherited from EntitySchema.addEnum

  #### Parameters

  * ##### name: [EntityKey](https://mikro-orm.io/api/core.md#EntityKey)\<TEntity>

  * ##### optionaltype: TypeType

  * ##### options: [EnumOptions](https://mikro-orm.io/api/core/interface/EnumOptions.md)\<TEntity> = <!-- -->{}

  #### Returns void

### [**](#addHook)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/EntitySchema.ts#L557)inheritedaddHook

* ****addHook**\<T>(event, handler): this

* Inherited from EntitySchema.addHook

  Adds a lifecycle hook handler to the entity schema. This method allows registering hooks after the entity is defined, which can be useful for avoiding circular type references.

  * **@example**

    ```
    export const Article = defineEntity({
      name: 'Article',
      properties: { ... },
    });

    Article.addHook('beforeCreate', async args => {
      args.entity.slug = args.entity.title.toLowerCase();
    });
    ```

  ***

  #### Parameters

  * ##### event: [EventType](https://mikro-orm.io/api/core/enum/EventType.md) | onInit | onLoad | beforeCreate | afterCreate | beforeUpdate | afterUpdate | beforeUpsert | afterUpsert | beforeDelete | afterDelete | beforeFlush | onFlush | afterFlush | beforeTransactionStart | afterTransactionStart | beforeTransactionCommit | afterTransactionCommit | beforeTransactionRollback | afterTransactionRollback

  * ##### handler: (args) => void | Promise\<void>

  #### Returns this

### [**](#addIndex)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/EntitySchema.ts#L281)inheritedaddIndex

* ****addIndex**\<Key>(options): void

* Inherited from EntitySchema.addIndex

  #### Parameters

  * ##### options: [IndexOptions](https://mikro-orm.io/api/core/interface/IndexOptions.md)\<TEntity, Key>

  #### Returns void

### [**](#addManyToMany)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/EntitySchema.ts#L221)inheritedaddManyToMany

* ****addManyToMany**\<Target>(name, type, options): void

* Inherited from EntitySchema.addManyToMany

  #### Parameters

  * ##### name: [EntityKey](https://mikro-orm.io/api/core.md#EntityKey)\<TEntity>

  * ##### type: TypeType

  * ##### options: [ManyToManyOptions](https://mikro-orm.io/api/core/interface/ManyToManyOptions.md)\<TEntity, Target>

  #### Returns void

### [**](#addManyToOne)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/EntitySchema.ts#L199)inheritedaddManyToOne

* ****addManyToOne**\<Target>(name, type, options): void

* Inherited from EntitySchema.addManyToOne

  #### Parameters

  * ##### name: [EntityKey](https://mikro-orm.io/api/core.md#EntityKey)\<TEntity>

  * ##### type: TypeType

  * ##### options: [ManyToOneOptions](https://mikro-orm.io/api/core/interface/ManyToOneOptions.md)\<TEntity, Target>

  #### Returns void

### [**](#addOneToMany)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/EntitySchema.ts#L243)inheritedaddOneToMany

* ****addOneToMany**\<Target>(name, type, options): void

* Inherited from EntitySchema.addOneToMany

  #### Parameters

  * ##### name: [EntityKey](https://mikro-orm.io/api/core.md#EntityKey)\<TEntity>

  * ##### type: TypeType

  * ##### options: [OneToManyOptions](https://mikro-orm.io/api/core/interface/OneToManyOptions.md)\<TEntity, Target>

  #### Returns void

### [**](#addOneToOne)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/EntitySchema.ts#L252)inheritedaddOneToOne

* ****addOneToOne**\<Target>(name, type, options): void

* Inherited from EntitySchema.addOneToOne

  #### Parameters

  * ##### name: [EntityKey](https://mikro-orm.io/api/core.md#EntityKey)\<TEntity>

  * ##### type: TypeType

  * ##### options: [OneToOneOptions](https://mikro-orm.io/api/core/interface/OneToOneOptions.md)\<TEntity, Target>

  #### Returns void

### [**](#addPrimaryKey)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/EntitySchema.ts#L170)inheritedaddPrimaryKey

* ****addPrimaryKey**(name, type, options): void

* Inherited from EntitySchema.addPrimaryKey

  #### Parameters

  * ##### name: [EntityKey](https://mikro-orm.io/api/core.md#EntityKey)\<TEntity>

  * ##### type: TypeType

  * ##### options: [PrimaryKeyOptions](https://mikro-orm.io/api/core/interface/PrimaryKeyOptions.md)\<TEntity> = <!-- -->{}

  #### Returns void

### [**](#addProperty)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/EntitySchema.ts#L112)inheritedaddProperty

* ****addProperty**(name, type, options): void

* Inherited from EntitySchema.addProperty

  #### Parameters

  * ##### name: [EntityKey](https://mikro-orm.io/api/core.md#EntityKey)\<TEntity>

  * ##### optionaltype: TypeType

  * ##### options: [PropertyOptions](https://mikro-orm.io/api/core/interface/PropertyOptions.md)\<TEntity> | [EntityProperty](https://mikro-orm.io/api/core/interface/EntityProperty.md)\<TEntity, any> = <!-- -->{}

  #### Returns void

### [**](#addSerializedPrimaryKey)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/EntitySchema.ts#L174)inheritedaddSerializedPrimaryKey

* ****addSerializedPrimaryKey**(name, type, options): void

* Inherited from EntitySchema.addSerializedPrimaryKey

  #### Parameters

  * ##### name: [EntityKey](https://mikro-orm.io/api/core.md#EntityKey)\<TEntity>

  * ##### type: TypeType

  * ##### options: [SerializedPrimaryKeyOptions](https://mikro-orm.io/api/core/interface/SerializedPrimaryKeyOptions.md)\<TEntity> = <!-- -->{}

  #### Returns void

### [**](#addUnique)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/EntitySchema.ts#L285)inheritedaddUnique

* ****addUnique**\<Key>(options): void

* Inherited from EntitySchema.addUnique

  #### Parameters

  * ##### options: [UniqueOptions](https://mikro-orm.io/api/core/interface/UniqueOptions.md)\<TEntity, Key>

  #### Returns void

### [**](#addVersion)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/EntitySchema.ts#L166)inheritedaddVersion

* ****addVersion**(name, type, options): void

* Inherited from EntitySchema.addVersion

  #### Parameters

  * ##### name: [EntityKey](https://mikro-orm.io/api/core.md#EntityKey)\<TEntity>

  * ##### type: TypeType

  * ##### options: [PropertyOptions](https://mikro-orm.io/api/core/interface/PropertyOptions.md)\<TEntity> = <!-- -->{}

  #### Returns void

### [**](#new)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/EntitySchema.ts#L348)inheritednew

* ****new**(...params): TEntity

* Inherited from EntitySchema.new

  #### Parameters

  * ##### rest...params: ConstructorParameters\<TClass>

  #### Returns TEntity

### [**](#setClass)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/EntitySchema.ts#L297)inheritedsetClass

* ****setClass**(cls): void

* Inherited from EntitySchema.setClass

  #### Parameters

  * ##### cls: TClass

  #### Returns void

### [**](#setCustomRepository)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/EntitySchema.ts#L289)inheritedsetCustomRepository

* ****setCustomRepository**(repository): void

* Inherited from EntitySchema.setCustomRepository

  #### Parameters

  * ##### repository: () => [Constructor](https://mikro-orm.io/api/core.md#Constructor)

  #### Returns void

### [**](#setExtends)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/EntitySchema.ts#L293)inheritedsetExtends

* ****setExtends**(base): void

* Inherited from EntitySchema.setExtends

  #### Parameters

  * ##### base: [EntityName](https://mikro-orm.io/api/core.md#EntityName)

  #### Returns void
