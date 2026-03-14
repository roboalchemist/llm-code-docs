# Source: https://mikro-orm.io/api/core/class/ChangeSetComputer.md

# ChangeSetComputer<!-- -->

## Index[**](#index)

### Constructors

* [**constructor](#constructor)

### Methods

* [**computeChangeSet](#computechangeset)

## Constructors<!-- -->[**](#constructors)

### [**](#constructor)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/unit-of-work/ChangeSetComputer.ts#L26)constructor

* ****new ChangeSetComputer**(em, collectionUpdates): [ChangeSetComputer](https://mikro-orm.io/api/core/class/ChangeSetComputer.md)

* #### Parameters

  * ##### em: [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>

  * ##### collectionUpdates: Set<[Collection](https://mikro-orm.io/api/core/class/Collection.md)\<Partial\<any>, object>>

  #### Returns [ChangeSetComputer](https://mikro-orm.io/api/core/class/ChangeSetComputer.md)

## Methods<!-- -->[**](#methods)

### [**](#computechangeset)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/unit-of-work/ChangeSetComputer.ts#L35)computeChangeSet

* ****computeChangeSet**\<T>(entity): null | [ChangeSet](https://mikro-orm.io/api/core/class/ChangeSet.md)\<T>

* #### Parameters

  * ##### entity: T

  #### Returns null | [ChangeSet](https://mikro-orm.io/api/core/class/ChangeSet.md)\<T>
