# Source: https://mikro-orm.io/api/sql/class/EntityRepository.md

# Source: https://mikro-orm.io/api/mongodb/class/EntityRepository.md

# Source: https://mikro-orm.io/api/core/class/EntityRepository.md

# EntityRepository<!-- --> \<Entity>

### Hierarchy

* *EntityRepository*

  * [EntityRepository](https://mikro-orm.io/api/sql/class/EntityRepository.md)
  * [EntityRepository](https://mikro-orm.io/api/mongodb/class/EntityRepository.md)

## Index[**](#index)

### Constructors

* [**constructor](#constructor)

### Methods

* [**assign](#assign)
* [**canPopulate](#canpopulate)
* [**count](#count)
* [**create](#create)
* [**find](#find)
* [**findAll](#findall)
* [**findAndCount](#findandcount)
* [**findByCursor](#findbycursor)
* [**findOne](#findone)
* [**findOneOrFail](#findoneorfail)
* [**getEntityManager](#getentitymanager)
* [**getEntityName](#getentityname)
* [**getReference](#getreference)
* [**insert](#insert)
* [**insertMany](#insertmany)
* [**map](#map)
* [**merge](#merge)
* [**nativeDelete](#nativedelete)
* [**nativeUpdate](#nativeupdate)
* [**populate](#populate)
* [**stream](#stream)
* [**upsert](#upsert)
* [**upsertMany](#upsertmany)

## Constructors<!-- -->[**](#constructors)

### [**](#constructor)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/EntityRepository.ts#L44)constructor

* ****new EntityRepository**\<Entity>(em, entityName): [EntityRepository](https://mikro-orm.io/api/core/class/EntityRepository.md)\<Entity>

* #### Parameters

  * ##### em: [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>

  * ##### entityName: [EntityName](https://mikro-orm.io/api/core.md#EntityName)\<Entity>

  #### Returns [EntityRepository](https://mikro-orm.io/api/core/class/EntityRepository.md)\<Entity>

## Methods<!-- -->[**](#methods)

### [**](#assign)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/EntityRepository.ts#L372)assign

* ****assign**\<Ent, Naked, Convert, Data>(entity, data, options): [MergeSelected](https://mikro-orm.io/api/core.md#MergeSelected)\<Ent, Naked, keyof
  <!-- -->
  Data & string>

* Shortcut for `wrap(entity).assign(data, { em })`

  ***

  #### Parameters

  * ##### entity: Ent | Partial\<Ent>

  * ##### data: Data & [IsSubset](https://mikro-orm.io/api/core.md#IsSubset)<[EntityData](https://mikro-orm.io/api/core.md#EntityData)\<Naked, Convert>, Data>

  * ##### optionaloptions: [AssignOptions](https://mikro-orm.io/api/core/interface/AssignOptions.md)\<Convert>

  #### Returns [MergeSelected](https://mikro-orm.io/api/core.md#MergeSelected)\<Ent, Naked, keyof<!-- --> Data & string>

### [**](#canpopulate)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/EntityRepository.ts#L280)canPopulate

* ****canPopulate**(property): boolean

* Checks whether given property can be populated on the entity.

  ***

  #### Parameters

  * ##### property: string

  #### Returns boolean

### [**](#count)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/EntityRepository.ts#L399)count

* ****count**\<Hint>(where, options): Promise\<number>

* Returns total number of entities matching your `where` query.

  ***

  #### Parameters

  * ##### where: [FilterQuery](https://mikro-orm.io/api/core.md#FilterQuery)\<Entity> = <!-- -->

  * ##### options: [CountOptions](https://mikro-orm.io/api/core/interface/CountOptions.md)\<Entity, Hint> = <!-- -->{}

  #### Returns Promise\<number>

### [**](#create)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/EntityRepository.ts#L322)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/EntityRepository.ts#L342)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/EntityRepository.ts#L362)create

* ****create**\<Convert, Data>(data, options): Entity
* ****create**\<Convert, Data>(data, options): Entity

* Creates new instance of given entity and populates it with given data. The entity constructor will be used unless you provide `{ managed: true }` in the `options` parameter. The constructor will be given parameters based on the defined constructor of the entity. If the constructor parameter matches a property name, its value will be extracted from `data`. If no matching property exists, the whole `data` parameter will be passed. This means we can also define `constructor(data: Partial<T>)` and `em.create()` will pass the data into it (unless we have a property named `data` too).

  The parameters are strictly checked, you need to provide all required properties. You can use `OptionalProps` symbol to omit some properties from this check without making them optional. Alternatively, use `partial: true` in the options to disable the strict checks for required properties. This option has no effect on runtime.

  The newly created entity will be automatically marked for persistence via `em.persist` unless you disable this behavior, either locally via `persist: false` option, or globally via `persistOnCreate` ORM config option.

  ***

  #### Parameters

  * ##### data: Data & [IsSubset](https://mikro-orm.io/api/core.md#IsSubset)<[RequiredEntityData](https://mikro-orm.io/api/core.md#RequiredEntityData)\<Entity, never, Convert>, Data>

  * ##### optionaloptions: [CreateOptions](https://mikro-orm.io/api/core/interface/CreateOptions.md)\<Convert>

  #### Returns Entity

### [**](#find)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/EntityRepository.ts#L139)find

* ****find**\<Hint, Fields, Excludes>(where, options): Promise<[Loaded](https://mikro-orm.io/api/core.md#Loaded)\<Entity, Hint, Fields, Excludes>\[]>

* Finds all entities matching your `where` query. You can pass additional options via the `options` parameter.

  ***

  #### Parameters

  * ##### where: [FilterQuery](https://mikro-orm.io/api/core.md#FilterQuery)\<Entity>

  * ##### optionaloptions: [FindOptions](https://mikro-orm.io/api/core/interface/FindOptions.md)\<Entity, Hint, Fields, Excludes>

  #### Returns Promise<[Loaded](https://mikro-orm.io/api/core.md#Loaded)\<Entity, Hint, Fields, Excludes>\[]>

### [**](#findall)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/EntityRepository.ts#L174)findAll

* ****findAll**\<Hint, Fields, Excludes>(options): Promise<[Loaded](https://mikro-orm.io/api/core.md#Loaded)\<Entity, Hint, Fields, Excludes>\[]>

* Finds all entities of given type. You can pass additional options via the `options` parameter.

  ***

  #### Parameters

  * ##### optionaloptions: [FindAllOptions](https://mikro-orm.io/api/core/interface/FindAllOptions.md)\<Entity, Hint, Fields, Excludes>

  #### Returns Promise<[Loaded](https://mikro-orm.io/api/core.md#Loaded)\<Entity, Hint, Fields, Excludes>\[]>

### [**](#findandcount)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/EntityRepository.ts#L150)findAndCount

* ****findAndCount**\<Hint, Fields, Excludes>(where, options): Promise<\[[Loaded](https://mikro-orm.io/api/core.md#Loaded)\<Entity, Hint, Fields, Excludes>\[], number]>

* Calls `em.find()` and `em.count()` with the same arguments (where applicable) and returns the results as tuple where first element is the array of entities, and the second is the count.

  ***

  #### Parameters

  * ##### where: [FilterQuery](https://mikro-orm.io/api/core.md#FilterQuery)\<Entity>

  * ##### optionaloptions: [FindOptions](https://mikro-orm.io/api/core/interface/FindOptions.md)\<Entity, Hint, Fields, Excludes>

  #### Returns Promise<\[[Loaded](https://mikro-orm.io/api/core.md#Loaded)\<Entity, Hint, Fields, Excludes>\[], number]>

### [**](#findbycursor)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/EntityRepository.ts#L160)findByCursor

* ****findByCursor**\<Hint, Fields, Excludes, IncludeCount>(options): Promise<[Cursor](https://mikro-orm.io/api/core/class/Cursor.md)\<Entity, Hint, Fields, Excludes, IncludeCount>>

* Calls `em.find()` and `em.count()` with the same arguments (where applicable) and returns the results as [Cursor](https://mikro-orm.io/api/core/class/Cursor.md) object. Supports `before`, `after`, `first` and `last` options while disallowing `limit` and `offset`. Explicit `orderBy` option is required.

  Use `first` and `after` for forward pagination, or `last` and `before` for backward pagination.

  * `first` and `last` are numbers and serve as an alternative to `offset`, those options are mutually exclusive, use only one at a time

  * `before` and `after` specify the previous cursor value, it can be one of the:

    * `Cursor` instance
    * opaque string provided by `startCursor/endCursor` properties
    * POJO/entity instance

  ```
  const currentCursor = await em.findByCursor(User, {
    first: 10,
    after: previousCursor, // cursor instance
    orderBy: { id: 'desc' },
  });

  // to fetch next page
  const nextCursor = await em.findByCursor(User, {
    first: 10,
    after: currentCursor.endCursor, // opaque string
    orderBy: { id: 'desc' },
  });

  // to fetch next page
  const nextCursor2 = await em.findByCursor(User, {
    first: 10,
    after: { id: lastSeenId }, // entity-like POJO
    orderBy: { id: 'desc' },
  });
  ```

  The options also support an `includeCount` (true by default) option. If set to false, the `totalCount` is not returned as part of the cursor. This is useful for performance reason, when you don't care about the total number of pages.

  The `Cursor` object provides the following interface:

  ```
  Cursor<User> {
    items: [
      User { ... },
      User { ... },
      User { ... },
    ],
    totalCount: 50, // not included if `includeCount: false`
    startCursor: 'WzRd',
    endCursor: 'WzZd',
    hasPrevPage: true,
    hasNextPage: true,
  }
  ```

  ***

  #### Parameters

  * ##### options: [FindByCursorOptions](https://mikro-orm.io/api/core/interface/FindByCursorOptions.md)\<Entity, Hint, Fields, Excludes, IncludeCount>

  #### Returns Promise<[Cursor](https://mikro-orm.io/api/core/class/Cursor.md)\<Entity, Hint, Fields, Excludes, IncludeCount>>

### [**](#findone)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/EntityRepository.ts#L52)findOne

* ****findOne**\<Hint, Fields, Excludes>(where, options): Promise\<null | [Loaded](https://mikro-orm.io/api/core.md#Loaded)\<Entity, Hint, Fields, Excludes>>

* Finds first entity matching your `where` query.

  ***

  #### Parameters

  * ##### where: [FilterQuery](https://mikro-orm.io/api/core.md#FilterQuery)\<Entity>

  * ##### optionaloptions: [FindOneOptions](https://mikro-orm.io/api/core/interface/FindOneOptions.md)\<Entity, Hint, Fields, Excludes>

  #### Returns Promise\<null | [Loaded](https://mikro-orm.io/api/core.md#Loaded)\<Entity, Hint, Fields, Excludes>>

### [**](#findoneorfail)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/EntityRepository.ts#L64)findOneOrFail

* ****findOneOrFail**\<Hint, Fields, Excludes>(where, options): Promise<[Loaded](https://mikro-orm.io/api/core.md#Loaded)\<Entity, Hint, Fields, Excludes>>

* Finds first entity matching your `where` query. If nothing is found, it will throw an error. You can override the factory for creating this method via `options.failHandler` locally or via `Configuration.findOneOrFailHandler` globally.

  ***

  #### Parameters

  * ##### where: [FilterQuery](https://mikro-orm.io/api/core.md#FilterQuery)\<Entity>

  * ##### optionaloptions: [FindOneOrFailOptions](https://mikro-orm.io/api/core/interface/FindOneOrFailOptions.md)\<Entity, Hint, Fields, Excludes>

  #### Returns Promise<[Loaded](https://mikro-orm.io/api/core.md#Loaded)\<Entity, Hint, Fields, Excludes>>

### [**](#getentitymanager)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/EntityRepository.ts#L413)getEntityManager

* ****getEntityManager**(): [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>

* Returns the underlying EntityManager instance

  ***

  #### Returns [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>

### [**](#getentityname)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/EntityRepository.ts#L406)getEntityName

* ****getEntityName**(): string

* #### Returns string

### [**](#getreference)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/EntityRepository.ts#L238)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/EntityRepository.ts#L247)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/EntityRepository.ts#L255)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/EntityRepository.ts#L263)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/EntityRepository.ts#L268)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/EntityRepository.ts#L273)getReference

* ****getReference**\<K>(id, options): [Ref](https://mikro-orm.io/api/core.md#Ref)\<Entity>
* ****getReference**\<K>(id, options): Entity
* ****getReference**(id, options): [Ref](https://mikro-orm.io/api/core.md#Ref)\<Entity>
* ****getReference**(id): Entity
* ****getReference**(id, options): Entity

* Gets a reference to the entity identified by the given type and alternate key property without actually loading it. The key option specifies which property to use for identity map lookup instead of the primary key.

  ***

  #### Parameters

  * ##### id: Entity\[K]

  * ##### options: Omit<[GetReferenceOptions](https://mikro-orm.io/api/core/interface/GetReferenceOptions.md), key | wrapped> & { key: K; wrapped: true }

  #### Returns [Ref](https://mikro-orm.io/api/core.md#Ref)\<Entity>

### [**](#insert)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/EntityRepository.ts#L192)insert

* ****insert**(data, options): Promise\<Entity extends { \[PrimaryKeyProp]?
  <!-- -->
  : PK } ? PK extends undefined ? Omit\<Entity\<Entity>, typeof [PrimaryKeyProp](https://mikro-orm.io/api/core.md#PrimaryKeyProp)> : PK extends keyof
  <!-- -->
  Entity\<Entity> ? ReadonlyPrimary\<UnwrapPrimary\<Entity\<Entity>\[PK\<PK>]>> : PK extends keyof
  <!-- -->
  Entity\<Entity>\[] ? ReadonlyPrimary\<PrimaryPropToType\<Entity\<Entity>, PK\<PK>>> : PK : Entity extends { \_id?
  <!-- -->
  : PK } ? string | ReadonlyPrimary\<PK> : Entity extends { id?
  <!-- -->
  : PK } ? ReadonlyPrimary\<PK> : Entity extends { uuid?
  <!-- -->
  : PK } ? ReadonlyPrimary\<PK> : Entity>

* Fires native insert query. Calling this has no side effects on the context (identity map).

  ***

  #### Parameters

  * ##### data: Entity | [RequiredEntityData](https://mikro-orm.io/api/core.md#RequiredEntityData)\<Entity>

  * ##### optionaloptions: [NativeInsertUpdateOptions](https://mikro-orm.io/api/core/interface/NativeInsertUpdateOptions.md)\<Entity>

  #### Returns Promise\<Entity extends { \[PrimaryKeyProp]?<!-- -->: PK } ? PK extends undefined ? Omit\<Entity\<Entity>, typeof [PrimaryKeyProp](https://mikro-orm.io/api/core.md#PrimaryKeyProp)> : PK extends keyof<!-- --> Entity\<Entity> ? ReadonlyPrimary\<UnwrapPrimary\<Entity\<Entity>\[PK\<PK>]>> : PK extends keyof<!-- --> Entity\<Entity>\[] ? ReadonlyPrimary\<PrimaryPropToType\<Entity\<Entity>, PK\<PK>>> : PK : Entity extends { \_id?<!-- -->: PK } ? string | ReadonlyPrimary\<PK> : Entity extends { id?<!-- -->: PK } ? ReadonlyPrimary\<PK> : Entity extends { uuid?<!-- -->: PK } ? ReadonlyPrimary\<PK> : Entity>

### [**](#insertmany)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/EntityRepository.ts#L202)insertMany

* ****insertMany**(data, options): Promise<(Entity extends { \[PrimaryKeyProp]?
  <!-- -->
  : PK } ? PK extends undefined ? Omit\<Entity\<Entity>, typeof [PrimaryKeyProp](https://mikro-orm.io/api/core.md#PrimaryKeyProp)> : PK extends keyof
  <!-- -->
  Entity\<Entity> ? ReadonlyPrimary\<UnwrapPrimary\<Entity\<Entity>\[PK\<PK>]>> : PK extends keyof
  <!-- -->
  Entity\<Entity>\[] ? ReadonlyPrimary\<PrimaryPropToType\<Entity\<Entity>, PK\<PK>>> : PK : Entity extends { \_id?
  <!-- -->
  : PK } ? string | ReadonlyPrimary\<PK> : Entity extends { id?
  <!-- -->
  : PK } ? ReadonlyPrimary\<PK> : Entity extends { uuid?
  <!-- -->
  : PK } ? ReadonlyPrimary\<PK> : Entity)\[]>

* Fires native insert query. Calling this has no side effects on the context (identity map).

  ***

  #### Parameters

  * ##### data: Entity\[] | [RequiredEntityData](https://mikro-orm.io/api/core.md#RequiredEntityData)\<Entity>\[]

  * ##### optionaloptions: [NativeInsertUpdateOptions](https://mikro-orm.io/api/core/interface/NativeInsertUpdateOptions.md)\<Entity>

  #### Returns Promise<(Entity extends { \[PrimaryKeyProp]?<!-- -->: PK } ? PK extends undefined ? Omit\<Entity\<Entity>, typeof [PrimaryKeyProp](https://mikro-orm.io/api/core.md#PrimaryKeyProp)> : PK extends keyof<!-- --> Entity\<Entity> ? ReadonlyPrimary\<UnwrapPrimary\<Entity\<Entity>\[PK\<PK>]>> : PK extends keyof<!-- --> Entity\<Entity>\[] ? ReadonlyPrimary\<PrimaryPropToType\<Entity\<Entity>, PK\<PK>>> : PK : Entity extends { \_id?<!-- -->: PK } ? string | ReadonlyPrimary\<PK> : Entity extends { id?<!-- -->: PK } ? ReadonlyPrimary\<PK> : Entity extends { uuid?<!-- -->: PK } ? ReadonlyPrimary\<PK> : Entity)\[]>

### [**](#map)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/EntityRepository.ts#L230)map

* ****map**(result, options): Entity

* Maps raw database result to an entity and merges it to this EntityManager.

  ***

  #### Parameters

  * ##### result: [EntityDictionary](https://mikro-orm.io/api/core.md#EntityDictionary)\<Entity>

  * ##### optionaloptions: { schema?<!-- -->: string }

    * ##### optionalschema: string

  #### Returns Entity

### [**](#merge)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/EntityRepository.ts#L392)merge

* ****merge**(data, options): Entity

* Merges given entity to this EntityManager so it becomes managed. You can force refreshing of existing entities via second parameter. By default it will return already loaded entities without modifying them.

  ***

  #### Parameters

  * ##### data: Entity | [EntityData](https://mikro-orm.io/api/core.md#EntityData)\<Entity>

  * ##### optionaloptions: [MergeOptions](https://mikro-orm.io/api/core/interface/MergeOptions.md)

  #### Returns Entity

### [**](#nativedelete)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/EntityRepository.ts#L223)nativeDelete

* ****nativeDelete**(where, options): Promise\<number>

* Fires native delete query. Calling this has no side effects on the context (identity map).

  ***

  #### Parameters

  * ##### where: [FilterQuery](https://mikro-orm.io/api/core.md#FilterQuery)\<Entity>

  * ##### optionaloptions: [DeleteOptions](https://mikro-orm.io/api/core/interface/DeleteOptions.md)\<Entity>

  #### Returns Promise\<number>

### [**](#nativeupdate)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/EntityRepository.ts#L212)nativeUpdate

* ****nativeUpdate**(where, data, options): Promise\<number>

* Fires native update query. Calling this has no side effects on the context (identity map).

  ***

  #### Parameters

  * ##### where: [FilterQuery](https://mikro-orm.io/api/core.md#FilterQuery)\<Entity>

  * ##### data: [EntityData](https://mikro-orm.io/api/core.md#EntityData)\<Entity>

  * ##### optionaloptions: [UpdateOptions](https://mikro-orm.io/api/core/interface/UpdateOptions.md)\<Entity>

  #### Returns Promise\<number>

### [**](#populate)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/EntityRepository.ts#L287)populate

* ****populate**\<Ent, Hint, Naked, Fields, Excludes>(entities, populate, options): Promise\<Ent extends object\[] ? [MergeLoaded](https://mikro-orm.io/api/core.md#MergeLoaded)\<ArrayElement\<Ent\<Ent>>, Naked, Hint, Fields, Excludes>\[] : [MergeLoaded](https://mikro-orm.io/api/core.md#MergeLoaded)\<Ent, Naked, Hint, Fields, Excludes>>

* Loads specified relations in batch. This will execute one query for each relation, that will populate it on all the specified entities.

  ***

  #### Parameters

  * ##### entities: Ent

  * ##### populate: false | [AutoPath](https://mikro-orm.io/api/core.md#AutoPath)\<Naked, Hint, ALL>\[]

  * ##### optionaloptions: [EntityLoaderOptions](https://mikro-orm.io/api/core/interface/EntityLoaderOptions.md)\<Naked, Fields, Excludes>

  #### Returns Promise\<Ent extends object\[] ? [MergeLoaded](https://mikro-orm.io/api/core.md#MergeLoaded)\<ArrayElement\<Ent\<Ent>>, Naked, Hint, Fields, Excludes>\[] : [MergeLoaded](https://mikro-orm.io/api/core.md#MergeLoaded)\<Ent, Naked, Hint, Fields, Excludes>>

### [**](#stream)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/EntityRepository.ts#L183)stream

* ****stream**\<Hint, Fields, Excludes>(options): AsyncIterableIterator<[Loaded](https://mikro-orm.io/api/core.md#Loaded)\<Entity, Hint, Fields, Excludes>, any, any>

* Finds all entities and returns an async iterable (async generator) that yields results one by one. The results are merged and mapped to entity instances, without adding them to the identity map. You can disable merging by passing the options `{ mergeResults: false }`. With `mergeResults` disabled, to-many collections will contain at most one item, and you will get duplicate root entities when there are multiple items in the populated collection. This is useful for processing large datasets without loading everything into memory at once.

  ```
  const stream = em.stream(Book, { populate: ['author'] });

  for await (const book of stream) {
    // book is an instance of Book entity
    console.log(book.title, book.author.name);
  }
  ```

  ***

  #### Parameters

  * ##### optionaloptions: [StreamOptions](https://mikro-orm.io/api/core/interface/StreamOptions.md)\<Entity, Hint, Fields, Excludes>

  #### Returns AsyncIterableIterator<[Loaded](https://mikro-orm.io/api/core.md#Loaded)\<Entity, Hint, Fields, Excludes>, any, any>

### [**](#upsert)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/EntityRepository.ts#L97)upsert

* ****upsert**\<Fields>(entityOrData, options): Promise\<Entity>

* Creates or updates the entity, based on whether it is already present in the database. This method performs an `insert on conflict merge` query ensuring the database is in sync, returning a managed entity instance. The method accepts either `entityName` together with the entity `data`, or just entity instance.

  ```
  // insert into "author" ("age", "email") values (33, 'foo@bar.com') on conflict ("email") do update set "age" = 41
  const author = await em.getRepository(Author).upsert({ email: 'foo@bar.com', age: 33 });
  ```

  The entity data needs to contain either the primary key, or any other unique property. Let's consider the following example, where `Author.email` is a unique property:

  ```
  // insert into "author" ("age", "email") values (33, 'foo@bar.com') on conflict ("email") do update set "age" = 41
  // select "id" from "author" where "email" = 'foo@bar.com'
  const author = await em.getRepository(Author).upsert({ email: 'foo@bar.com', age: 33 });
  ```

  Depending on the driver support, this will either use a returning query, or a separate select query, to fetch the primary key if it's missing from the `data`.

  If the entity is already present in current context, there won't be any queries - instead, the entity data will be assigned and an explicit `flush` will be required for those changes to be persisted.

  ***

  #### Parameters

  * ##### optionalentityOrData: Entity | [EntityData](https://mikro-orm.io/api/core.md#EntityData)\<Entity>

  * ##### optionaloptions: [UpsertOptions](https://mikro-orm.io/api/core/interface/UpsertOptions.md)\<Entity, Fields>

  #### Returns Promise\<Entity>

### [**](#upsertmany)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/EntityRepository.ts#L129)upsertMany

* ****upsertMany**\<Fields>(entitiesOrData, options): Promise\<Entity\[]>

* Creates or updates the entity, based on whether it is already present in the database. This method performs an `insert on conflict merge` query ensuring the database is in sync, returning a managed entity instance.

  ```
  // insert into "author" ("age", "email") values (33, 'foo@bar.com') on conflict ("email") do update set "age" = 41
  const authors = await em.getRepository(Author).upsertMany([{ email: 'foo@bar.com', age: 33 }, ...]);
  ```

  The entity data needs to contain either the primary key, or any other unique property. Let's consider the following example, where `Author.email` is a unique property:

  ```
  // insert into "author" ("age", "email") values (33, 'foo@bar.com'), (666, 'lol@lol.lol') on conflict ("email") do update set "age" = excluded."age"
  // select "id" from "author" where "email" = 'foo@bar.com'
  const author = await em.getRepository(Author).upsertMany([
    { email: 'foo@bar.com', age: 33 },
    { email: 'lol@lol.lol', age: 666 },
  ]);
  ```

  Depending on the driver support, this will either use a returning query, or a separate select query, to fetch the primary key if it's missing from the `data`.

  If the entity is already present in current context, there won't be any queries - instead, the entity data will be assigned and an explicit `flush` will be required for those changes to be persisted.

  ***

  #### Parameters

  * ##### optionalentitiesOrData: [EntityData](https://mikro-orm.io/api/core.md#EntityData)\<Entity>\[] | Entity\[]

  * ##### optionaloptions: [UpsertManyOptions](https://mikro-orm.io/api/core/interface/UpsertManyOptions.md)\<Entity, Fields>

  #### Returns Promise\<Entity\[]>
