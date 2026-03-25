# Source: https://mikro-orm.io/api/core/class/EntitySchema.md

# EntitySchema<!-- --> \<Entity, Base, Class>

### Hierarchy

* *EntitySchema*
  * [EntitySchemaWithMeta](https://mikro-orm.io/api/core/interface/EntitySchemaWithMeta.md)

## Index[**](#index)

### Constructors

* [**constructor](#constructor)

### Properties

* [**REGISTRY](#REGISTRY)

### Accessors

* [**class](#class)
* [**meta](#meta)
* [**name](#name)
* [**properties](#properties)
* [**tableName](#tablename)

### Methods

* [**addEmbedded](#addembedded)
* [**addEnum](#addenum)
* [**addHook](#addhook)
* [**addIndex](#addindex)
* [**addManyToMany](#addmanytomany)
* [**addManyToOne](#addmanytoone)
* [**addOneToMany](#addonetomany)
* [**addOneToOne](#addonetoone)
* [**addPrimaryKey](#addprimarykey)
* [**addProperty](#addproperty)
* [**addSerializedPrimaryKey](#addserializedprimarykey)
* [**addUnique](#addunique)
* [**addVersion](#addversion)
* [**new](#new)
* [**setClass](#setclass)
* [**setCustomRepository](#setcustomrepository)
* [**setExtends](#setextends)
* [**fromMetadata](#fromMetadata)

## Constructors<!-- -->[**](#constructors)

### [**](#constructor)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/EntitySchema.ts#L85)constructor

* ****new EntitySchema**\<Entity, Base, Class>(meta): [EntitySchema](https://mikro-orm.io/api/core/class/EntitySchema.md)\<Entity, Base, Class>

* #### Parameters

  * ##### meta: [EntitySchemaMetadata](https://mikro-orm.io/api/core.md#EntitySchemaMetadata)\<Entity, Base, Class>

  #### Returns [EntitySchema](https://mikro-orm.io/api/core/class/EntitySchema.md)\<Entity, Base, Class>

## Properties<!-- -->[**](#properties)

### [**](#REGISTRY)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/EntitySchema.ts#L76)staticREGISTRY

**REGISTRY: Map\<Partial\<any>, [EntitySchema](https://mikro-orm.io/api/core/class/EntitySchema.md)\<any, never, [EntityCtor](https://mikro-orm.io/api/core.md#EntityCtor)\<any>>> =

<!-- -->

...

When schema links the entity class via `class` option, this registry allows the lookup from opposite side, so we can use the class in `entities` option just like the EntitySchema instance.

## Accessors<!-- -->[**](#accessors)

### [**](#class)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/EntitySchema.ts#L340)class

* **get class(): Class

* #### Returns Class

### [**](#meta)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/EntitySchema.ts#L328)meta

* **get meta(): [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<Entity, Class>

* #### Returns [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<Entity, Class>

### [**](#name)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/EntitySchema.ts#L332)name

* **get name(): string | [EntityName](https://mikro-orm.io/api/core.md#EntityName)\<Entity>

* #### Returns string | [EntityName](https://mikro-orm.io/api/core.md#EntityName)\<Entity>

### [**](#properties)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/EntitySchema.ts#L344)properties

* **get properties(): Record\<string, any>

* #### Returns Record\<string, any>

### [**](#tablename)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/EntitySchema.ts#L336)tableName

* **get tableName(): string

* #### Returns string

## Methods<!-- -->[**](#methods)

### [**](#addembedded)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/EntitySchema.ts#L183)addEmbedded

* ****addEmbedded**\<Target>(name, options): void

* #### Parameters

  * ##### name: [EntityKey](https://mikro-orm.io/api/core.md#EntityKey)\<Entity>

  * ##### options: [EmbeddedOptions](https://mikro-orm.io/api/core/interface/EmbeddedOptions.md)\<Entity, Target>

  #### Returns void

### [**](#addenum)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/EntitySchema.ts#L141)addEnum

* ****addEnum**(name, type, options): void

* #### Parameters

  * ##### name: [EntityKey](https://mikro-orm.io/api/core.md#EntityKey)\<Entity>

  * ##### optionaltype: TypeType

  * ##### options: [EnumOptions](https://mikro-orm.io/api/core/interface/EnumOptions.md)\<Entity> = <!-- -->{}

  #### Returns void

### [**](#addhook)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/EntitySchema.ts#L557)addHook

* ****addHook**\<T>(event, handler): this

* Adds a lifecycle hook handler to the entity schema. This method allows registering hooks after the entity is defined, which can be useful for avoiding circular type references.

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

### [**](#addindex)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/EntitySchema.ts#L281)addIndex

* ****addIndex**\<Key>(options): void

* #### Parameters

  * ##### options: [IndexOptions](https://mikro-orm.io/api/core/interface/IndexOptions.md)\<Entity, Key>

  #### Returns void

### [**](#addmanytomany)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/EntitySchema.ts#L221)addManyToMany

* ****addManyToMany**\<Target>(name, type, options): void

* #### Parameters

  * ##### name: [EntityKey](https://mikro-orm.io/api/core.md#EntityKey)\<Entity>

  * ##### type: TypeType

  * ##### options: [ManyToManyOptions](https://mikro-orm.io/api/core/interface/ManyToManyOptions.md)\<Entity, Target>

  #### Returns void

### [**](#addmanytoone)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/EntitySchema.ts#L199)addManyToOne

* ****addManyToOne**\<Target>(name, type, options): void

* #### Parameters

  * ##### name: [EntityKey](https://mikro-orm.io/api/core.md#EntityKey)\<Entity>

  * ##### type: TypeType

  * ##### options: [ManyToOneOptions](https://mikro-orm.io/api/core/interface/ManyToOneOptions.md)\<Entity, Target>

  #### Returns void

### [**](#addonetomany)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/EntitySchema.ts#L243)addOneToMany

* ****addOneToMany**\<Target>(name, type, options): void

* #### Parameters

  * ##### name: [EntityKey](https://mikro-orm.io/api/core.md#EntityKey)\<Entity>

  * ##### type: TypeType

  * ##### options: [OneToManyOptions](https://mikro-orm.io/api/core/interface/OneToManyOptions.md)\<Entity, Target>

  #### Returns void

### [**](#addonetoone)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/EntitySchema.ts#L252)addOneToOne

* ****addOneToOne**\<Target>(name, type, options): void

* #### Parameters

  * ##### name: [EntityKey](https://mikro-orm.io/api/core.md#EntityKey)\<Entity>

  * ##### type: TypeType

  * ##### options: [OneToOneOptions](https://mikro-orm.io/api/core/interface/OneToOneOptions.md)\<Entity, Target>

  #### Returns void

### [**](#addprimarykey)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/EntitySchema.ts#L170)addPrimaryKey

* ****addPrimaryKey**(name, type, options): void

* #### Parameters

  * ##### name: [EntityKey](https://mikro-orm.io/api/core.md#EntityKey)\<Entity>

  * ##### type: TypeType

  * ##### options: [PrimaryKeyOptions](https://mikro-orm.io/api/core/interface/PrimaryKeyOptions.md)\<Entity> = <!-- -->{}

  #### Returns void

### [**](#addproperty)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/EntitySchema.ts#L112)addProperty

* ****addProperty**(name, type, options): void

* #### Parameters

  * ##### name: [EntityKey](https://mikro-orm.io/api/core.md#EntityKey)\<Entity>

  * ##### optionaltype: TypeType

  * ##### options: [PropertyOptions](https://mikro-orm.io/api/core/interface/PropertyOptions.md)\<Entity> | [EntityProperty](https://mikro-orm.io/api/core/interface/EntityProperty.md)\<Entity, any> = <!-- -->{}

  #### Returns void

### [**](#addserializedprimarykey)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/EntitySchema.ts#L174)addSerializedPrimaryKey

* ****addSerializedPrimaryKey**(name, type, options): void

* #### Parameters

  * ##### name: [EntityKey](https://mikro-orm.io/api/core.md#EntityKey)\<Entity>

  * ##### type: TypeType

  * ##### options: [SerializedPrimaryKeyOptions](https://mikro-orm.io/api/core/interface/SerializedPrimaryKeyOptions.md)\<Entity> = <!-- -->{}

  #### Returns void

### [**](#addunique)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/EntitySchema.ts#L285)addUnique

* ****addUnique**\<Key>(options): void

* #### Parameters

  * ##### options: [UniqueOptions](https://mikro-orm.io/api/core/interface/UniqueOptions.md)\<Entity, Key>

  #### Returns void

### [**](#addversion)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/EntitySchema.ts#L166)addVersion

* ****addVersion**(name, type, options): void

* #### Parameters

  * ##### name: [EntityKey](https://mikro-orm.io/api/core.md#EntityKey)\<Entity>

  * ##### type: TypeType

  * ##### options: [PropertyOptions](https://mikro-orm.io/api/core/interface/PropertyOptions.md)\<Entity> = <!-- -->{}

  #### Returns void

### [**](#new)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/EntitySchema.ts#L348)new

* ****new**(...params): Entity

* #### Parameters

  * ##### rest...params: ConstructorParameters\<Class>

  #### Returns Entity

### [**](#setclass)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/EntitySchema.ts#L297)setClass

* ****setClass**(cls): void

* #### Parameters

  * ##### cls: Class

  #### Returns void

### [**](#setcustomrepository)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/EntitySchema.ts#L289)setCustomRepository

* ****setCustomRepository**(repository): void

* #### Parameters

  * ##### repository: () => [Constructor](https://mikro-orm.io/api/core.md#Constructor)

  #### Returns void

### [**](#setextends)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/EntitySchema.ts#L293)setExtends

* ****setExtends**(base): void

* #### Parameters

  * ##### base: [EntityName](https://mikro-orm.io/api/core.md#EntityName)

  #### Returns void

### [**](#fromMetadata)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/metadata/EntitySchema.ts#L103)staticfromMetadata

* ****fromMetadata**\<T, U>(meta): [EntitySchema](https://mikro-orm.io/api/core/class/EntitySchema.md)\<T, U, [EntityCtor](https://mikro-orm.io/api/core.md#EntityCtor)\<T>>

* #### Parameters

  * ##### meta: [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<T, [EntityCtor](https://mikro-orm.io/api/core.md#EntityCtor)\<T>> | [DeepPartial](https://mikro-orm.io/api/core.md#DeepPartial)<[EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<T, [EntityCtor](https://mikro-orm.io/api/core.md#EntityCtor)\<T>>>

  #### Returns [EntitySchema](https://mikro-orm.io/api/core/class/EntitySchema.md)\<T, U, [EntityCtor](https://mikro-orm.io/api/core.md#EntityCtor)\<T>>
