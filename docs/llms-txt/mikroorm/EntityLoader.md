# Source: https://mikro-orm.io/api/core/class/EntityLoader.md

# EntityLoader<!-- -->

## Index[**](#index)

### Constructors

* [**constructor](#constructor)

### Methods

* [**normalizePopulate](#normalizepopulate)
* [**populate](#populate)

## Constructors<!-- -->[**](#constructors)

### [**](#constructor)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/EntityLoader.ts#L66)constructor

* ****new EntityLoader**(em): [EntityLoader](https://mikro-orm.io/api/core/class/EntityLoader.md)

* #### Parameters

  * ##### em: [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>

  #### Returns [EntityLoader](https://mikro-orm.io/api/core/class/EntityLoader.md)

## Methods<!-- -->[**](#methods)

### [**](#normalizepopulate)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/EntityLoader.ts#L135)normalizePopulate

* ****normalizePopulate**\<Entity>(entityName, populate, strategy, lookup, exclude): [PopulateOptions](https://mikro-orm.io/api/core.md#PopulateOptions)\<Entity>\[]

* #### Parameters

  * ##### entityName: [EntityName](https://mikro-orm.io/api/core.md#EntityName)\<Entity>

  * ##### populate: boolean | [PopulateOptions](https://mikro-orm.io/api/core.md#PopulateOptions)\<Entity> | (boolean | [PopulateOptions](https://mikro-orm.io/api/core.md#PopulateOptions)\<Entity>)\[]

  * ##### optionalstrategy: [LoadStrategy](https://mikro-orm.io/api/core/enum/LoadStrategy.md)

  * ##### lookup: boolean = <!-- -->true

  * ##### optionalexclude: string\[]

  #### Returns [PopulateOptions](https://mikro-orm.io/api/core.md#PopulateOptions)\<Entity>\[]

### [**](#populate)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/EntityLoader.ts#L76)populate

* ****populate**\<Entity, Fields>(entityName, entities, populate, options): Promise\<void>

* Loads specified relations in batch. This will execute one query for each relation, that will populate it on all the specified entities.

  ***

  #### Parameters

  * ##### entityName: [EntityName](https://mikro-orm.io/api/core.md#EntityName)\<Entity>

  * ##### entities: Entity\[]

  * ##### populate: boolean | [PopulateOptions](https://mikro-orm.io/api/core.md#PopulateOptions)\<Entity>\[]

  * ##### options: [EntityLoaderOptions](https://mikro-orm.io/api/core/interface/EntityLoaderOptions.md)\<Entity, Fields, never>

  #### Returns Promise\<void>
