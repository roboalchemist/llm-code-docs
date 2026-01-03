# Source: https://mikro-orm.io/api/core/class/ChangeSetComputer.md

# ChangeSetComputer<!-- -->

## Index[**](#Index)

### Constructors

* [**constructor](#constructor)

### Methods

* [**computeChangeSet](#computeChangeSet)

## Constructors<!-- -->[**](#Constructors)

### [**](#constructor)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/unit-of-work/ChangeSetComputer.ts#L14)constructor

* ****new ChangeSetComputer**(validator, collectionUpdates, metadata, platform, config, em): [ChangeSetComputer](https://mikro-orm.io/api/core/class/ChangeSetComputer.md)

- #### Parameters

  * ##### validator: [EntityValidator](https://mikro-orm.io/api/core/class/EntityValidator.md)
  * ##### collectionUpdates: Set<[Collection](https://mikro-orm.io/api/core/class/Collection.md)\<Partial\<any>, object>>
  * ##### metadata: [MetadataStorage](https://mikro-orm.io/api/core/class/MetadataStorage.md)
  * ##### platform: [Platform](https://mikro-orm.io/api/core/class/Platform.md)
  * ##### config: [Configuration](https://mikro-orm.io/api/core/class/Configuration.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>, [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>>
  * ##### em: [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>

  #### Returns [ChangeSetComputer](https://mikro-orm.io/api/core/class/ChangeSetComputer.md)

## Methods<!-- -->[**](#Methods)

### [**](#computeChangeSet)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/unit-of-work/ChangeSetComputer.ts#L23)computeChangeSet

* ****computeChangeSet**\<T>(entity): null | [ChangeSet](https://mikro-orm.io/api/core/class/ChangeSet.md)\<T>

- #### Parameters

  * ##### entity: T

  #### Returns null | [ChangeSet](https://mikro-orm.io/api/core/class/ChangeSet.md)\<T>
