# Source: https://mikro-orm.io/api/core/class/UnitOfWork.md

# UnitOfWork<!-- -->

## Index[**](#index)

### Constructors

* [**constructor](#constructor)

### Methods

* [**cancelOrphanRemoval](#cancelorphanremoval)
* [**clear](#clear)
* [**clearActionsQueue](#clearactionsqueue)
* [**commit](#commit)
* [**computeChangeSet](#computechangeset)
* [**computeChangeSets](#computechangesets)
* [**getById](#getbyid)
* [**getByKey](#getbykey)
* [**getCollectionUpdates](#getcollectionupdates)
* [**getExtraUpdates](#getextraupdates)
* [**getChangeSetPersister](#getchangesetpersister)
* [**getChangeSets](#getchangesets)
* [**getIdentityMap](#getidentitymap)
* [**getOriginalEntityData](#getoriginalentitydata)
* [**getOrphanRemoveStack](#getorphanremovestack)
* [**getPersistStack](#getpersiststack)
* [**getRemoveStack](#getremovestack)
* [**lock](#lock)
* [**merge](#merge)
* [**persist](#persist)
* [**recomputeSingleChangeSet](#recomputesinglechangeset)
* [**remove](#remove)
* [**shouldAutoFlush](#shouldautoflush)
* [**scheduleExtraUpdate](#scheduleextraupdate)
* [**scheduleOrphanRemoval](#scheduleorphanremoval)
* [**storeByKey](#storebykey)
* [**tryGetById](#trygetbyid)
* [**unsetIdentity](#unsetidentity)

## Constructors<!-- -->[**](#constructors)

### [**](#constructor)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/unit-of-work/UnitOfWork.ts#L73)constructor

* ****new UnitOfWork**(em): [UnitOfWork](https://mikro-orm.io/api/core/class/UnitOfWork.md)

* #### Parameters

  * ##### em: [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>

  #### Returns [UnitOfWork](https://mikro-orm.io/api/core/class/UnitOfWork.md)

## Methods<!-- -->[**](#methods)

### [**](#cancelorphanremoval)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/unit-of-work/UnitOfWork.ts#L747)cancelOrphanRemoval

* ****cancelOrphanRemoval**(entity, visited): void

* #### Parameters

  * ##### entity: Partial\<any>

  * ##### optionalvisited: Set\<Partial\<any>>

  #### Returns void

### [**](#clear)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/unit-of-work/UnitOfWork.ts#L583)clear

* ****clear**(): void

* #### Returns void

### [**](#clearactionsqueue)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/unit-of-work/UnitOfWork.ts#L386)clearActionsQueue

* ****clearActionsQueue**(): void

* #### Returns void

### [**](#commit)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/unit-of-work/UnitOfWork.ts#L491)commit

* ****commit**(): Promise\<void>

* #### Returns Promise\<void>

### [**](#computechangeset)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/unit-of-work/UnitOfWork.ts#L390)computeChangeSet

* ****computeChangeSet**\<T>(entity, type): void

* #### Parameters

  * ##### entity: T

  * ##### optionaltype: [ChangeSetType](https://mikro-orm.io/api/core/enum/ChangeSetType.md)

  #### Returns void

### [**](#computechangesets)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/unit-of-work/UnitOfWork.ts#L621)computeChangeSets

* ****computeChangeSets**(): void

* #### Returns void

### [**](#getbyid)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/unit-of-work/UnitOfWork.ts#L221)getById

* ****getById**\<T>(entityName, id, schema, convertCustomTypes): undefined | T

* Returns entity from the identity map. For composite keys, you need to pass an array of PKs in the same order as they are defined in `meta.primaryKeys`.

  ***

  #### Parameters

  * ##### entityName: [EntityName](https://mikro-orm.io/api/core.md#EntityName)\<T>

  * ##### id: (T extends { \[PrimaryKeyProp]?<!-- -->: PK } ? PK extends undefined ? Omit\<T\<T>, typeof [PrimaryKeyProp](https://mikro-orm.io/api/core.md#PrimaryKeyProp)> : PK extends keyof<!-- --> T\<T> ? ReadonlyPrimary\<UnwrapPrimary\<T\<T>\[PK\<PK>]>> : PK extends keyof<!-- --> T\<T>\[] ? ReadonlyPrimary\<PrimaryPropToType\<T\<T>, PK\<PK>>> : PK : T extends { \_id?<!-- -->: PK } ? string | ReadonlyPrimary\<PK> : T extends { id?<!-- -->: PK } ? ReadonlyPrimary\<PK> : T extends { uuid?<!-- -->: PK } ? ReadonlyPrimary\<PK> : T) | (T extends { \[PrimaryKeyProp]?<!-- -->: PK } ? PK extends undefined ? Omit\<T\<T>, typeof [PrimaryKeyProp](https://mikro-orm.io/api/core.md#PrimaryKeyProp)> : PK extends keyof<!-- --> T\<T> ? ReadonlyPrimary\<UnwrapPrimary\<T\<T>\[PK\<PK>]>> : PK extends keyof<!-- --> T\<T>\[] ? ReadonlyPrimary\<PrimaryPropToType\<T\<T>, PK\<PK>>> : PK : T extends { \_id?<!-- -->: PK } ? string | ReadonlyPrimary\<PK> : T extends { id?<!-- -->: PK } ? ReadonlyPrimary\<PK> : T extends { uuid?<!-- -->: PK } ? ReadonlyPrimary\<PK> : T)\[]

  * ##### optionalschema: string

  * ##### optionalconvertCustomTypes: boolean

  #### Returns undefined | T

### [**](#getbykey)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/unit-of-work/UnitOfWork.ts#L265)getByKey

* ****getByKey**\<T>(entityName, key, value, schema, convertCustomTypes): undefined | T

* Returns entity from the identity map by an alternate key (non-PK property).

  ***

  #### Parameters

  * ##### entityName: [EntityName](https://mikro-orm.io/api/core.md#EntityName)\<T>

  * ##### key: string

  * ##### value: unknown

  * ##### optionalschema: string

  * ##### optionalconvertCustomTypes: boolean

    If true, the value is in database format and will be converted to JS format for lookup. If false (default), the value is assumed to be in JS format already.

  #### Returns undefined | T

### [**](#getcollectionupdates)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/unit-of-work/UnitOfWork.ts#L354)getCollectionUpdates

* ****getCollectionUpdates**(): [Collection](https://mikro-orm.io/api/core/class/Collection.md)\<Partial\<any>, object>\[]

* #### Returns [Collection](https://mikro-orm.io/api/core/class/Collection.md)\<Partial\<any>, object>\[]

### [**](#getextraupdates)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/unit-of-work/UnitOfWork.ts#L358)getExtraUpdates

* ****getExtraUpdates**(): Set<\[Partial\<any>, string | string\[], Partial\<any> | [Collection](https://mikro-orm.io/api/core/class/Collection.md)\<any, object> | Partial\<any>\[] | [Reference](https://mikro-orm.io/api/core/class/Reference.md)\<any>, undefined | [ChangeSet](https://mikro-orm.io/api/core/class/ChangeSet.md)\<any>, [ChangeSetType](https://mikro-orm.io/api/core/enum/ChangeSetType.md)]>

* #### Returns Set<\[Partial\<any>, string | string\[], Partial\<any> | [Collection](https://mikro-orm.io/api/core/class/Collection.md)\<any, object> | Partial\<any>\[] | [Reference](https://mikro-orm.io/api/core/class/Reference.md)\<any>, undefined | [ChangeSet](https://mikro-orm.io/api/core/class/ChangeSet.md)\<any>, [ChangeSetType](https://mikro-orm.io/api/core/enum/ChangeSetType.md)]>

### [**](#getchangesetpersister)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/unit-of-work/UnitOfWork.ts#L756)getChangeSetPersister

* ****getChangeSetPersister**(): [ChangeSetPersister](https://mikro-orm.io/api/core/class/ChangeSetPersister.md)

* #### Returns [ChangeSetPersister](https://mikro-orm.io/api/core/class/ChangeSetPersister.md)

### [**](#getchangesets)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/unit-of-work/UnitOfWork.ts#L350)getChangeSets

* ****getChangeSets**(): [ChangeSet](https://mikro-orm.io/api/core/class/ChangeSet.md)\<Partial\<any>>\[]

* #### Returns [ChangeSet](https://mikro-orm.io/api/core/class/ChangeSet.md)\<Partial\<any>>\[]

### [**](#getidentitymap)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/unit-of-work/UnitOfWork.ts#L331)getIdentityMap

* ****getIdentityMap**(): [IdentityMap](https://mikro-orm.io/api/core/class/IdentityMap.md)

* Returns map of all managed entities.

  ***

  #### Returns [IdentityMap](https://mikro-orm.io/api/core/class/IdentityMap.md)

### [**](#getoriginalentitydata)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/unit-of-work/UnitOfWork.ts#L338)getOriginalEntityData

* ****getOriginalEntityData**\<T>(entity): undefined | [EntityData](https://mikro-orm.io/api/core.md#EntityData)\<T>

* Returns stored snapshot of entity state that is used for change set computation.

  ***

  #### Parameters

  * ##### entity: T

  #### Returns undefined | [EntityData](https://mikro-orm.io/api/core.md#EntityData)\<T>

### [**](#getorphanremovestack)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/unit-of-work/UnitOfWork.ts#L752)getOrphanRemoveStack

* ****getOrphanRemoveStack**(): Set\<Partial\<any>>

* #### Returns Set\<Partial\<any>>

### [**](#getpersiststack)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/unit-of-work/UnitOfWork.ts#L342)getPersistStack

* ****getPersistStack**(): Set\<Partial\<any>>

* #### Returns Set\<Partial\<any>>

### [**](#getremovestack)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/unit-of-work/UnitOfWork.ts#L346)getRemoveStack

* ****getRemoveStack**(): Set\<Partial\<any>>

* #### Returns Set\<Partial\<any>>

### [**](#lock)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/unit-of-work/UnitOfWork.ts#L569)lock

* ****lock**\<T>(entity, options): Promise\<void>

* #### Parameters

  * ##### entity: T

  * ##### options: [LockOptions](https://mikro-orm.io/api/core/interface/LockOptions.md)

  #### Returns Promise\<void>

### [**](#merge)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/unit-of-work/UnitOfWork.ts#L84)merge

* ****merge**\<T>(entity, visited): void

* #### Parameters

  * ##### entity: T

  * ##### optionalvisited: Set\<Partial\<any>>

  #### Returns void

### [**](#persist)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/unit-of-work/UnitOfWork.ts#L430)persist

* ****persist**\<T>(entity, visited, options): void

* #### Parameters

  * ##### entity: T

  * ##### optionalvisited: Set\<Partial\<any>>

  * ##### options: { cascade?<!-- -->: boolean; checkRemoveStack?<!-- -->: boolean } = <!-- -->{}

    * ##### optionalcascade: boolean

    * ##### optionalcheckRemoveStack: boolean

  #### Returns void

### [**](#recomputesinglechangeset)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/unit-of-work/UnitOfWork.ts#L415)recomputeSingleChangeSet

* ****recomputeSingleChangeSet**\<T>(entity): void

* #### Parameters

  * ##### entity: T

  #### Returns void

### [**](#remove)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/unit-of-work/UnitOfWork.ts#L455)remove

* ****remove**\<T>(entity, visited, options): void

* #### Parameters

  * ##### entity: T

  * ##### optionalvisited: Set\<Partial\<any>>

  * ##### options: { cascade?<!-- -->: boolean } = <!-- -->{}

    * ##### optionalcascade: boolean

  #### Returns void

### [**](#shouldautoflush)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/unit-of-work/UnitOfWork.ts#L370)shouldAutoFlush

* ****shouldAutoFlush**\<T>(meta): boolean

* #### Parameters

  * ##### meta: [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<T, [EntityCtor](https://mikro-orm.io/api/core.md#EntityCtor)\<T>>

  #### Returns boolean

### [**](#scheduleextraupdate)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/unit-of-work/UnitOfWork.ts#L695)scheduleExtraUpdate

* ****scheduleExtraUpdate**\<T>(changeSet, props): void

* #### Parameters

  * ##### changeSet: [ChangeSet](https://mikro-orm.io/api/core/class/ChangeSet.md)\<T>

  * ##### props: [EntityProperty](https://mikro-orm.io/api/core/interface/EntityProperty.md)\<T, any>\[]

  #### Returns void

### [**](#scheduleorphanremoval)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/unit-of-work/UnitOfWork.ts#L737)scheduleOrphanRemoval

* ****scheduleOrphanRemoval**(entity, visited): void

* #### Parameters

  * ##### optionalentity: Partial\<any>

  * ##### optionalvisited: Set\<Partial\<any>>

  #### Returns void

### [**](#storebykey)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/unit-of-work/UnitOfWork.ts#L291)storeByKey

* ****storeByKey**\<T>(entity, key, value, schema, convertCustomTypes): void

* Stores an entity in the identity map under an alternate key (non-PK property). Also sets the property value on the entity.

  ***

  #### Parameters

  * ##### entity: T

  * ##### key: string

  * ##### value: unknown

  * ##### optionalschema: string

  * ##### optionalconvertCustomTypes: boolean

    If true, the value is in database format and will be converted to JS format. If false (default), the value is assumed to be in JS format already.

  #### Returns void

### [**](#trygetbyid)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/unit-of-work/UnitOfWork.ts#L313)tryGetById

* ****tryGetById**\<T>(entityName, where, schema, strict): null | T

* #### Parameters

  * ##### entityName: [EntityName](https://mikro-orm.io/api/core.md#EntityName)\<T>

  * ##### where: [FilterQuery](https://mikro-orm.io/api/core.md#FilterQuery)\<T>

  * ##### optionalschema: string

  * ##### strict: boolean = <!-- -->true

  #### Returns null | T

### [**](#unsetidentity)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/unit-of-work/UnitOfWork.ts#L589)unsetIdentity

* ****unsetIdentity**(entity): void

* #### Parameters

  * ##### entity: Partial\<any>

  #### Returns void
