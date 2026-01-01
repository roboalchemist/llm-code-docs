# Source: https://mikro-orm.io/api/core/class/EntityLoader.md

# EntityLoader<!-- -->

## Index[**](#Index)

### Constructors

* [**constructor](#constructor)

### Methods

* [**normalizePopulate](#normalizePopulate)
* [**populate](#populate)

## Constructors<!-- -->[**](#Constructors)

### [**](#constructor)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/EntityLoader.ts#L60)constructor

* ****new EntityLoader**(em): [EntityLoader](https://mikro-orm.io/api/core/class/EntityLoader.md)

- #### Parameters

  * ##### em: [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>

  #### Returns [EntityLoader](https://mikro-orm.io/api/core/class/EntityLoader.md)

## Methods<!-- -->[**](#Methods)

### [**](#normalizePopulate)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/EntityLoader.ts#L117)normalizePopulate

* ****normalizePopulate**\<Entity>(entityName, populate, strategy, lookup): [PopulateOptions](https://mikro-orm.io/api/core.md#PopulateOptions)\<Entity>\[]

- #### Parameters

  * ##### entityName: string
  * ##### populate: boolean | [PopulateOptions](https://mikro-orm.io/api/core.md#PopulateOptions)\<Entity> | (boolean | [PopulateOptions](https://mikro-orm.io/api/core.md#PopulateOptions)\<Entity>)\[]
  * ##### optionalstrategy: [LoadStrategy](https://mikro-orm.io/api/core/enum/LoadStrategy.md)
  * ##### lookup: boolean = <!-- -->true

  #### Returns [PopulateOptions](https://mikro-orm.io/api/core.md#PopulateOptions)\<Entity>\[]

### [**](#populate)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/EntityLoader.ts#L69)populate

* ****populate**\<Entity, Fields>(entityName, entities, populate, options): Promise\<void>

- Loads specified relations in batch. This will execute one query for each relation, that will populate it on all the specified entities.

  ***

  #### Parameters

  * ##### entityName: string
  * ##### entities: Entity\[]
  * ##### populate: boolean | [PopulateOptions](https://mikro-orm.io/api/core.md#PopulateOptions)\<Entity>\[]
  * ##### options: [EntityLoaderOptions](https://mikro-orm.io/api/core.md#EntityLoaderOptions)\<Entity, Fields, never>

  #### Returns Promise\<void>
