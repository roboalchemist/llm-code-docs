# Source: https://mikro-orm.io/api/core/class/ChangeSetPersister.md

# ChangeSetPersister<!-- -->

## Index[**](#index)

### Constructors

* [**constructor](#constructor)

### Methods

* [**executeDeletes](#executedeletes)
* [**executeInserts](#executeinserts)
* [**executeUpdates](#executeupdates)
* [**mapReturnedValues](#mapreturnedvalues)

## Constructors<!-- -->[**](#constructors)

### [**](#constructor)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/unit-of-work/ChangeSetPersister.ts#L43)constructor

* ****new ChangeSetPersister**(em): [ChangeSetPersister](https://mikro-orm.io/api/core/class/ChangeSetPersister.md)

* #### Parameters

  * ##### em: [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>

  #### Returns [ChangeSetPersister](https://mikro-orm.io/api/core/class/ChangeSetPersister.md)

## Methods<!-- -->[**](#methods)

### [**](#executedeletes)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/unit-of-work/ChangeSetPersister.ts#L107)executeDeletes

* ****executeDeletes**\<T>(changeSets, options, withSchema): Promise\<void>

* #### Parameters

  * ##### changeSets: [ChangeSet](https://mikro-orm.io/api/core/class/ChangeSet.md)\<T>\[]

  * ##### optionaloptions: [DriverMethodOptions](https://mikro-orm.io/api/core/interface/DriverMethodOptions.md)

  * ##### optionalwithSchema: boolean

  #### Returns Promise\<void>

### [**](#executeinserts)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/unit-of-work/ChangeSetPersister.ts#L55)executeInserts

* ****executeInserts**\<T>(changeSets, options, withSchema): Promise\<void>

* #### Parameters

  * ##### changeSets: [ChangeSet](https://mikro-orm.io/api/core/class/ChangeSet.md)\<T>\[]

  * ##### optionaloptions: [DriverMethodOptions](https://mikro-orm.io/api/core/interface/DriverMethodOptions.md)

  * ##### optionalwithSchema: boolean

  #### Returns Promise\<void>

### [**](#executeupdates)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/unit-of-work/ChangeSetPersister.ts#L76)executeUpdates

* ****executeUpdates**\<T>(changeSets, batched, options, withSchema): Promise\<void>

* #### Parameters

  * ##### changeSets: [ChangeSet](https://mikro-orm.io/api/core/class/ChangeSet.md)\<T>\[]

  * ##### batched: boolean

  * ##### optionaloptions: [DriverMethodOptions](https://mikro-orm.io/api/core/interface/DriverMethodOptions.md)

  * ##### optionalwithSchema: boolean

  #### Returns Promise\<void>

### [**](#mapreturnedvalues)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/unit-of-work/ChangeSetPersister.ts#L641)mapReturnedValues

* ****mapReturnedValues**\<T>(entity, payload, row, meta, upsert): void

* Maps values returned via `returning` statement (postgres) or the inserted id (other sql drivers). No need to handle composite keys here as they need to be set upfront. We do need to map to the change set payload too, as it will be used in the originalEntityData for new entities.

  ***

  #### Parameters

  * ##### entity: undefined | null | T

  * ##### payload: [EntityDictionary](https://mikro-orm.io/api/core.md#EntityDictionary)\<T>

  * ##### row: undefined | [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)

  * ##### meta: [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<T, [EntityCtor](https://mikro-orm.io/api/core.md#EntityCtor)\<T>>

  * ##### upsert: boolean = <!-- -->false

  #### Returns void
