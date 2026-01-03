# Source: https://mikro-orm.io/api/core/class/UnitOfWork.md

# UnitOfWork<!-- -->

## Index[**](#Index)

### Constructors

* [**constructor](#constructor)

### Methods

* [**cancelOrphanRemoval](#cancelOrphanRemoval)
* [**clear](#clear)
* [**clearActionsQueue](#clearActionsQueue)
* [**commit](#commit)
* [**computeChangeSet](#computeChangeSet)
* [**computeChangeSets](#computeChangeSets)
* [**getById](#getById)
* [**getChangeSetPersister](#getChangeSetPersister)
* [**getChangeSets](#getChangeSets)
* [**getCollectionUpdates](#getCollectionUpdates)
* [**getExtraUpdates](#getExtraUpdates)
* [**getIdentityMap](#getIdentityMap)
* [**getOriginalEntityData](#getOriginalEntityData)
* [**getOrphanRemoveStack](#getOrphanRemoveStack)
* [**getPersistStack](#getPersistStack)
* [**getRemoveStack](#getRemoveStack)
* [**lock](#lock)
* [**merge](#merge)
* [**persist](#persist)
* [**recomputeSingleChangeSet](#recomputeSingleChangeSet)
* [**remove](#remove)
* [**scheduleExtraUpdate](#scheduleExtraUpdate)
* [**scheduleOrphanRemoval](#scheduleOrphanRemoval)
* [**shouldAutoFlush](#shouldAutoFlush)
* [**tryGetById](#tryGetById)
* [**unsetIdentity](#unsetIdentity)

## Constructors<!-- -->[**](#Constructors)

### [**](#constructor)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/unit-of-work/UnitOfWork.ts#L54)constructor

* ****new UnitOfWork**(em): [UnitOfWork](https://mikro-orm.io/api/core/class/UnitOfWork.md)

- #### Parameters

  * ##### em: [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>

  #### Returns [UnitOfWork](https://mikro-orm.io/api/core/class/UnitOfWork.md)

## Methods<!-- -->[**](#Methods)

### [**](#cancelOrphanRemoval)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/unit-of-work/UnitOfWork.ts#L623)cancelOrphanRemoval

* ****cancelOrphanRemoval**(entity, visited): void

- #### Parameters

  * ##### entity: Partial\<any>
  * ##### optionalvisited: Set\<Partial\<any>>

  #### Returns void

### [**](#clear)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/unit-of-work/UnitOfWork.ts#L475)clear

* ****clear**(): void

- #### Returns void

### [**](#clearActionsQueue)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/unit-of-work/UnitOfWork.ts#L286)clearActionsQueue

* ****clearActionsQueue**(): void

- #### Returns void

### [**](#commit)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/unit-of-work/UnitOfWork.ts#L385)commit

* ****commit**(): Promise\<void>

- #### Returns Promise\<void>

### [**](#computeChangeSet)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/unit-of-work/UnitOfWork.ts#L290)computeChangeSet

* ****computeChangeSet**\<T>(entity, type): void

- #### Parameters

  * ##### entity: T
  * ##### optionaltype: [ChangeSetType](https://mikro-orm.io/api/core/enum/ChangeSetType.md)

  #### Returns void

### [**](#computeChangeSets)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/unit-of-work/UnitOfWork.ts#L509)computeChangeSets

* ****computeChangeSets**(): void

- #### Returns void

### [**](#getById)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/unit-of-work/UnitOfWork.ts#L186)getById

* ****getById**\<T>(entityName, id, schema, convertCustomTypes): undefined | T

- Returns entity from the identity map. For composite keys, you need to pass an array of PKs in the same order as they are defined in `meta.primaryKeys`.

  ***

  #### Parameters

  * ##### entityName: string
  * ##### id: (T extends { \[PrimaryKeyProp]?<!-- -->: PK } ? PK extends undefined ? Omit\<T\<T>, typeof [PrimaryKeyProp](https://mikro-orm.io/api/core.md#PrimaryKeyProp)> : PK extends keyof<!-- --> T\<T> ? ReadonlyPrimary\<UnwrapPrimary\<T\<T>\[PK\<PK>]>> : PK extends keyof<!-- --> T\<T>\[] ? ReadonlyPrimary\<PrimaryPropToType\<T\<T>, PK\<PK>>> : PK : T extends { \_id?<!-- -->: PK } ? string | ReadonlyPrimary\<PK> : T extends { id?<!-- -->: PK } ? ReadonlyPrimary\<PK> : T extends { uuid?<!-- -->: PK } ? ReadonlyPrimary\<PK> : T) | (T extends { \[PrimaryKeyProp]?<!-- -->: PK } ? PK extends undefined ? Omit\<T\<T>, typeof [PrimaryKeyProp](https://mikro-orm.io/api/core.md#PrimaryKeyProp)> : PK extends keyof<!-- --> T\<T> ? ReadonlyPrimary\<UnwrapPrimary\<T\<T>\[PK\<PK>]>> : PK extends keyof<!-- --> T\<T>\[] ? ReadonlyPrimary\<PrimaryPropToType\<T\<T>, PK\<PK>>> : PK : T extends { \_id?<!-- -->: PK } ? string | ReadonlyPrimary\<PK> : T extends { id?<!-- -->: PK } ? ReadonlyPrimary\<PK> : T extends { uuid?<!-- -->: PK } ? ReadonlyPrimary\<PK> : T)\[]
  * ##### optionalschema: string
  * ##### optionalconvertCustomTypes: boolean

  #### Returns undefined | T

### [**](#getChangeSetPersister)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/unit-of-work/UnitOfWork.ts#L632)getChangeSetPersister

* ****getChangeSetPersister**(): [ChangeSetPersister](https://mikro-orm.io/api/core/class/ChangeSetPersister.md)

- #### Returns [ChangeSetPersister](https://mikro-orm.io/api/core/class/ChangeSetPersister.md)

### [**](#getChangeSets)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/unit-of-work/UnitOfWork.ts#L252)getChangeSets

* ****getChangeSets**(): [ChangeSet](https://mikro-orm.io/api/core/class/ChangeSet.md)\<Partial\<any>>\[]

- #### Returns [ChangeSet](https://mikro-orm.io/api/core/class/ChangeSet.md)\<Partial\<any>>\[]

### [**](#getCollectionUpdates)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/unit-of-work/UnitOfWork.ts#L256)getCollectionUpdates

* ****getCollectionUpdates**(): [Collection](https://mikro-orm.io/api/core/class/Collection.md)\<Partial\<any>, object>\[]

- #### Returns [Collection](https://mikro-orm.io/api/core/class/Collection.md)\<Partial\<any>, object>\[]

### [**](#getExtraUpdates)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/unit-of-work/UnitOfWork.ts#L260)getExtraUpdates

* ****getExtraUpdates**(): Set<\[Partial\<any>, string | string\[], [Reference](https://mikro-orm.io/api/core/class/Reference.md)\<any> | Partial\<any> | [Collection](https://mikro-orm.io/api/core/class/Collection.md)\<any, object> | Partial\<any>\[], undefined | [ChangeSet](https://mikro-orm.io/api/core/class/ChangeSet.md)\<any>, [ChangeSetType](https://mikro-orm.io/api/core/enum/ChangeSetType.md)]>

- #### Returns Set<\[Partial\<any>, string | string\[], [Reference](https://mikro-orm.io/api/core/class/Reference.md)\<any> | Partial\<any> | [Collection](https://mikro-orm.io/api/core/class/Collection.md)\<any, object> | Partial\<any>\[], undefined | [ChangeSet](https://mikro-orm.io/api/core/class/ChangeSet.md)\<any>, [ChangeSetType](https://mikro-orm.io/api/core/enum/ChangeSetType.md)]>

### [**](#getIdentityMap)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/unit-of-work/UnitOfWork.ts#L233)getIdentityMap

* ****getIdentityMap**(): [IdentityMap](https://mikro-orm.io/api/core/class/IdentityMap.md)

- Returns map of all managed entities.

  ***

  #### Returns [IdentityMap](https://mikro-orm.io/api/core/class/IdentityMap.md)

### [**](#getOriginalEntityData)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/unit-of-work/UnitOfWork.ts#L240)getOriginalEntityData

* ****getOriginalEntityData**\<T>(entity): undefined | [EntityData](https://mikro-orm.io/api/core.md#EntityData)\<T>

- Returns stored snapshot of entity state that is used for change set computation.

  ***

  #### Parameters

  * ##### entity: T

  #### Returns undefined | [EntityData](https://mikro-orm.io/api/core.md#EntityData)\<T>

### [**](#getOrphanRemoveStack)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/unit-of-work/UnitOfWork.ts#L628)getOrphanRemoveStack

* ****getOrphanRemoveStack**(): Set\<Partial\<any>>

- #### Returns Set\<Partial\<any>>

### [**](#getPersistStack)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/unit-of-work/UnitOfWork.ts#L244)getPersistStack

* ****getPersistStack**(): Set\<Partial\<any>>

- #### Returns Set\<Partial\<any>>

### [**](#getRemoveStack)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/unit-of-work/UnitOfWork.ts#L248)getRemoveStack

* ****getRemoveStack**(): Set\<Partial\<any>>

- #### Returns Set\<Partial\<any>>

### [**](#lock)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/unit-of-work/UnitOfWork.ts#L461)lock

* ****lock**\<T>(entity, options): Promise\<void>

- #### Parameters

  * ##### entity: T
  * ##### options: [LockOptions](https://mikro-orm.io/api/core/interface/LockOptions.md)

  #### Returns Promise\<void>

### [**](#merge)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/unit-of-work/UnitOfWork.ts#L64)merge

* ****merge**\<T>(entity, visited): void

- #### Parameters

  * ##### entity: T
  * ##### optionalvisited: Set\<Partial\<any>>

  #### Returns void

### [**](#persist)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/unit-of-work/UnitOfWork.ts#L328)persist

* ****persist**\<T>(entity, visited, options): void

- #### Parameters

  * ##### entity: T
  * ##### optionalvisited: Set\<Partial\<any>>
  * ##### options: { cascade?<!-- -->: boolean; checkRemoveStack?<!-- -->: boolean } = <!-- -->{}
    * ##### optionalcascade: boolean
    * ##### optionalcheckRemoveStack: boolean

  #### Returns void

### [**](#recomputeSingleChangeSet)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/unit-of-work/UnitOfWork.ts#L311)recomputeSingleChangeSet

* ****recomputeSingleChangeSet**\<T>(entity): void

- #### Parameters

  * ##### entity: T

  #### Returns void

### [**](#remove)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/unit-of-work/UnitOfWork.ts#L349)remove

* ****remove**\<T>(entity, visited, options): void

- #### Parameters

  * ##### entity: T
  * ##### optionalvisited: Set\<Partial\<any>>
  * ##### options: { cascade?<!-- -->: boolean } = <!-- -->{}
    * ##### optionalcascade: boolean

  #### Returns void

### [**](#scheduleExtraUpdate)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/unit-of-work/UnitOfWork.ts#L578)scheduleExtraUpdate

* ****scheduleExtraUpdate**\<T>(changeSet, props): void

- #### Parameters

  * ##### changeSet: [ChangeSet](https://mikro-orm.io/api/core/class/ChangeSet.md)\<T>
  * ##### props: [EntityProperty](https://mikro-orm.io/api/core/interface/EntityProperty.md)\<T, any>\[]

  #### Returns void

### [**](#scheduleOrphanRemoval)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/unit-of-work/UnitOfWork.ts#L614)scheduleOrphanRemoval

* ****scheduleOrphanRemoval**(entity, visited): void

- #### Parameters

  * ##### optionalentity: Partial\<any>
  * ##### optionalvisited: Set\<Partial\<any>>

  #### Returns void

### [**](#shouldAutoFlush)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/unit-of-work/UnitOfWork.ts#L264)shouldAutoFlush

* ****shouldAutoFlush**\<T>(meta): boolean

- #### Parameters

  * ##### meta: [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<T>

  #### Returns boolean

### [**](#tryGetById)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/unit-of-work/UnitOfWork.ts#L220)tryGetById

* ****tryGetById**\<T>(entityName, where, schema, strict): null | T

- #### Parameters

  * ##### entityName: string
  * ##### where: [FilterQuery](https://mikro-orm.io/api/core.md#FilterQuery)\<T>
  * ##### optionalschema: string
  * ##### strict: boolean = <!-- -->true

  #### Returns null | T

### [**](#unsetIdentity)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/unit-of-work/UnitOfWork.ts#L481)unsetIdentity

* ****unsetIdentity**(entity): void

- #### Parameters

  * ##### entity: Partial\<any>

  #### Returns void
