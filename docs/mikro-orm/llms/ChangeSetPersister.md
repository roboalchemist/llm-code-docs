# Source: https://mikro-orm.io/api/core/class/ChangeSetPersister.md

# ChangeSetPersister<!-- -->

## Index[**](#Index)

### Constructors

* [**constructor](#constructor)

### Methods

* [**executeDeletes](#executeDeletes)
* [**executeInserts](#executeInserts)
* [**executeUpdates](#executeUpdates)
* [**mapReturnedValues](#mapReturnedValues)

## Constructors<!-- -->[**](#Constructors)

### [**](#constructor)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/unit-of-work/ChangeSetPersister.ts#L19)constructor

* ****new ChangeSetPersister**(driver, metadata, hydrator, factory, validator, config, em): [ChangeSetPersister](https://mikro-orm.io/api/core/class/ChangeSetPersister.md)

- #### Parameters

  * ##### driver: [IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>
  * ##### metadata: [MetadataStorage](https://mikro-orm.io/api/core/class/MetadataStorage.md)
  * ##### hydrator: IHydrator
  * ##### factory: [EntityFactory](https://mikro-orm.io/api/core/class/EntityFactory.md)
  * ##### validator: [EntityValidator](https://mikro-orm.io/api/core/class/EntityValidator.md)
  * ##### config: [Configuration](https://mikro-orm.io/api/core/class/Configuration.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>, [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>>
  * ##### em: [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>

  #### Returns [ChangeSetPersister](https://mikro-orm.io/api/core/class/ChangeSetPersister.md)

## Methods<!-- -->[**](#Methods)

### [**](#executeDeletes)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/unit-of-work/ChangeSetPersister.ts#L65)executeDeletes

* ****executeDeletes**\<T>(changeSets, options, withSchema): Promise\<void>

- #### Parameters

  * ##### changeSets: [ChangeSet](https://mikro-orm.io/api/core/class/ChangeSet.md)\<T>\[]
  * ##### optionaloptions: [DriverMethodOptions](https://mikro-orm.io/api/core/interface/DriverMethodOptions.md)
  * ##### optionalwithSchema: boolean

  #### Returns Promise\<void>

### [**](#executeInserts)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/unit-of-work/ChangeSetPersister.ts#L31)executeInserts

* ****executeInserts**\<T>(changeSets, options, withSchema): Promise\<void>

- #### Parameters

  * ##### changeSets: [ChangeSet](https://mikro-orm.io/api/core/class/ChangeSet.md)\<T>\[]
  * ##### optionaloptions: [DriverMethodOptions](https://mikro-orm.io/api/core/interface/DriverMethodOptions.md)
  * ##### optionalwithSchema: boolean

  #### Returns Promise\<void>

### [**](#executeUpdates)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/unit-of-work/ChangeSetPersister.ts#L48)executeUpdates

* ****executeUpdates**\<T>(changeSets, batched, options, withSchema): Promise\<void>

- #### Parameters

  * ##### changeSets: [ChangeSet](https://mikro-orm.io/api/core/class/ChangeSet.md)\<T>\[]
  * ##### batched: boolean
  * ##### optionaloptions: [DriverMethodOptions](https://mikro-orm.io/api/core/interface/DriverMethodOptions.md)
  * ##### optionalwithSchema: boolean

  #### Returns Promise\<void>

### [**](#mapReturnedValues)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/unit-of-work/ChangeSetPersister.ts#L455)mapReturnedValues

* ****mapReturnedValues**\<T>(entity, payload, row, meta, upsert): void

- Maps values returned via `returning` statement (postgres) or the inserted id (other sql drivers). No need to handle composite keys here as they need to be set upfront. We do need to map to the change set payload too, as it will be used in the originalEntityData for new entities.

  ***

  #### Parameters

  * ##### entity: undefined | null | T
  * ##### payload: [EntityDictionary](https://mikro-orm.io/api/core.md#EntityDictionary)\<T>
  * ##### row: undefined | [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)
  * ##### meta: [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<T>
  * ##### upsert: boolean = <!-- -->false

  #### Returns void
