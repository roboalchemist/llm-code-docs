# Source: https://mikro-orm.io/api/core/class/Collection.md

# Collection<!-- --> \<T, O>

### Hierarchy

* [ArrayCollection](https://mikro-orm.io/api/core/class/ArrayCollection.md)\<T, O>
  * *Collection*
    * [LoadedCollection](https://mikro-orm.io/api/core/interface/LoadedCollection.md)

## Index[**](#Index)

### Constructors

* [**constructor](#constructor)

### Properties

* [**owner](#owner)

### Accessors

* [**length](#length)

### Methods

* [**\[iterator\]](#\[iterator])
* [**add](#add)
* [**contains](#contains)
* [**count](#count)
* [**exists](#exists)
* [**filter](#filter)
* [**find](#find)
* [**getIdentifiers](#getIdentifiers)
* [**getItems](#getItems)
* [**indexBy](#indexBy)
* [**init](#init)
* [**isDirty](#isDirty)
* [**isEmpty](#isEmpty)
* [**isInitialized](#isInitialized)
* [**isPartial](#isPartial)
* [**load](#load)
* [**loadCount](#loadCount)
* [**loadItems](#loadItems)
* [**map](#map)
* [**matching](#matching)
* [**populated](#populated)
* [**reduce](#reduce)
* [**remove](#remove)
* [**removeAll](#removeAll)
* [**set](#set)
* [**setDirty](#setDirty)
* [**shouldPopulate](#shouldPopulate)
* [**slice](#slice)
* [**toArray](#toArray)
* [**toJSON](#toJSON)
* [**create](#create)

## Constructors<!-- -->[**](#Constructors)

### [**](#constructor)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/Collection.ts#L38)constructor

* ****new Collection**\<T, O>(owner, items, initialized): [Collection](https://mikro-orm.io/api/core/class/Collection.md)\<T, O>

- Overrides ArrayCollection.constructor

  #### Parameters

  * ##### owner: O
  * ##### optionalitems: T\[]
  * ##### initialized: boolean = <!-- -->true

  #### Returns [Collection](https://mikro-orm.io/api/core/class/Collection.md)\<T, O>

## Properties<!-- -->[**](#Properties)

### [**](#owner)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/ArrayCollection.ts#L19)readonlyinheritedowner

**owner: O

Inherited from ArrayCollection.owner

## Accessors<!-- -->[**](#Accessors)

### [**](#length)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/ArrayCollection.ts#L367)inheritedlength

* **get length(): number

- Inherited from ArrayCollection.length

  #### Returns number

## Methods<!-- -->[**](#Methods)

### [**](#\[iterator])[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/ArrayCollection.ts#L371)inherited\[iterator]

* ****\[iterator]**(): IterableIterator\<T, any, any>

- Inherited from ArrayCollection.\[iterator]

  #### Returns IterableIterator\<T, any, any>

### [**](#add)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/Collection.ts#L162)add

* ****add**\<TT>(entity, ...entities): void

- Overrides ArrayCollection.add

  #### Parameters

  * ##### entity: TT | [Reference](https://mikro-orm.io/api/core/class/Reference.md)\<TT> | Iterable\<TT | [Reference](https://mikro-orm.io/api/core/class/Reference.md)\<TT>, any, any>
  * ##### rest...entities: (TT | [Reference](https://mikro-orm.io/api/core/class/Reference.md)\<TT>)\[]

  #### Returns void

### [**](#contains)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/Collection.ts#L196)contains

* ****contains**\<TT>(item, check): boolean

- Overrides ArrayCollection.contains

  #### Parameters

  * ##### item: TT | [Reference](https://mikro-orm.io/api/core/class/Reference.md)\<TT>
  * ##### check: boolean = <!-- -->true

  #### Returns boolean

### [**](#count)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/Collection.ts#L204)count

* ****count**(): number

- Overrides ArrayCollection.count

  #### Returns number

### [**](#exists)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/Collection.ts#L225)exists

* ****exists**(cb): boolean

- Overrides ArrayCollection.exists

  Tests for the existence of an element that satisfies the given predicate.

  ***

  #### Parameters

  * ##### cb: (item) => boolean


  #### Returns boolean

### [**](#filter)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/Collection.ts#L241)filter

* ****filter**(cb): T\[]

- Overrides ArrayCollection.filter

  Extracts a subset of the collection items.

  ***

  #### Parameters

  * ##### cb: (item, index) => boolean


  #### Returns T\[]

### [**](#find)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/Collection.ts#L233)find

* ****find**(cb): undefined | T

- Overrides ArrayCollection.find

  Returns the first element of this collection that satisfies the predicate.

  ***

  #### Parameters

  * ##### cb: (item, index) => boolean


  #### Returns undefined | T

### [**](#getIdentifiers)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/ArrayCollection.ts#L51)inheritedgetIdentifiers

* ****getIdentifiers**\<U>(field): U\[]

- Inherited from ArrayCollection.getIdentifiers

  #### Parameters

  * ##### optionalfield: string | string\[]

  #### Returns U\[]

### [**](#getItems)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/Collection.ts#L146)getItems

* ****getItems**(check): T\[]

- Overrides ArrayCollection.getItems

  Returns the items (the collection must be initialized)

  ***

  #### Parameters

  * ##### check: boolean = <!-- -->true

  #### Returns T\[]

### [**](#indexBy)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/Collection.ts#L258)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/Collection.ts#L263)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/Collection.ts#L268)indexBy

* ****indexBy**\<K1, K2>(key): Record\<T\[K1] & PropertyKey, T>
* ****indexBy**\<K1, K2>(key, valueKey): Record\<T\[K1] & PropertyKey, T\[K2]>

- Overrides ArrayCollection.indexBy

  Maps the collection items to a dictionary, indexed by the key you specify. If there are more items with the same key, only the first one will be present.

  ***

  #### Parameters

  * ##### key: K1

  #### Returns Record\<T\[K1] & PropertyKey, T>

### [**](#init)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/Collection.ts#L289)init

* ****init**\<TT, P>(options): Promise<[LoadedCollection](https://mikro-orm.io/api/core/interface/LoadedCollection.md)<[Loaded](https://mikro-orm.io/api/core.md#Loaded)\<TT, P>>>

- #### Parameters

  * ##### options: [InitCollectionOptions](https://mikro-orm.io/api/core/interface/InitCollectionOptions.md)\<TT, P, \*, never> = <!-- -->{}

  #### Returns Promise<[LoadedCollection](https://mikro-orm.io/api/core/interface/LoadedCollection.md)<[Loaded](https://mikro-orm.io/api/core.md#Loaded)\<TT, P>>>

### [**](#isDirty)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/ArrayCollection.ts#L351)inheritedisDirty

* ****isDirty**(): boolean

- Inherited from ArrayCollection.isDirty

  #### Returns boolean

### [**](#isEmpty)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/Collection.ts#L209)isEmpty

* ****isEmpty**(): boolean

- Overrides ArrayCollection.isEmpty

  #### Returns boolean

### [**](#isInitialized)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/ArrayCollection.ts#L337)inheritedisInitialized

* ****isInitialized**(fully): boolean

- Inherited from ArrayCollection.isInitialized

  #### Parameters

  * ##### fully: boolean = <!-- -->false

  #### Returns boolean

### [**](#isPartial)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/ArrayCollection.ts#L355)inheritedisPartial

* ****isPartial**(): boolean

- Inherited from ArrayCollection.isPartial

  #### Returns boolean

### [**](#load)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/Collection.ts#L62)load

* ****load**\<TT, P>(options): Promise<[LoadedCollection](https://mikro-orm.io/api/core/interface/LoadedCollection.md)<[Loaded](https://mikro-orm.io/api/core.md#Loaded)\<TT, P>>>

- Ensures the collection is loaded first (without reloading it if it already is loaded). Returns the Collection instance (itself), works the same as `Reference.load()`.

  ***

  #### Parameters

  * ##### options: [InitCollectionOptions](https://mikro-orm.io/api/core/interface/InitCollectionOptions.md)\<TT, P, \*, never> = <!-- -->{}

  #### Returns Promise<[LoadedCollection](https://mikro-orm.io/api/core/interface/LoadedCollection.md)<[Loaded](https://mikro-orm.io/api/core.md#Loaded)\<TT, P>>>

### [**](#loadCount)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/Collection.ts#L95)loadCount

* ****loadCount**(options): Promise\<number>

- Overrides ArrayCollection.loadCount

  Gets the count of collection items from database instead of counting loaded items. The value is cached (unless you use the `where` option), use `refresh: true` to force reload it.

  ***

  #### Parameters

  * ##### options: boolean | [LoadCountOptions](https://mikro-orm.io/api/core/interface/LoadCountOptions.md)\<T> = <!-- -->{}

  #### Returns Promise\<number>

### [**](#loadItems)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/Collection.ts#L86)loadItems

* ****loadItems**\<TT, P>(options): Promise<[Loaded](https://mikro-orm.io/api/core.md#Loaded)\<TT, P>\[]>

- Initializes the collection and returns the items

  ***

  #### Parameters

  * ##### optionaloptions: [InitCollectionOptions](https://mikro-orm.io/api/core/interface/InitCollectionOptions.md)\<TT, P, \*, never>

  #### Returns Promise<[Loaded](https://mikro-orm.io/api/core.md#Loaded)\<TT, P>\[]>

### [**](#map)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/Collection.ts#L249)map

* ****map**\<R>(mapper): R\[]

- Overrides ArrayCollection.map

  Maps the collection items based on your provided mapper function.

  ***

  #### Parameters

  * ##### mapper: (item, index) => R


  #### Returns R\[]

### [**](#matching)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/Collection.ts#L119)matching

* ****matching**\<TT, P>(options): Promise<[Loaded](https://mikro-orm.io/api/core.md#Loaded)\<TT, P>\[]>

- #### Parameters

  * ##### options: [MatchingOptions](https://mikro-orm.io/api/core/interface/MatchingOptions.md)\<T, P>

  #### Returns Promise<[Loaded](https://mikro-orm.io/api/core.md#Loaded)\<TT, P>\[]>

### [**](#populated)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/Collection.ts#L285)populated

* ****populated**(populated): void

- #### Parameters

  * ##### populated: undefined | boolean = <!-- -->true

  #### Returns void

### [**](#reduce)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/ArrayCollection.ts#L300)inheritedreduce

* ****reduce**\<R>(cb, initial): R

- Inherited from ArrayCollection.reduce

  Maps the collection items based on your provided mapper function to a single object.

  ***

  #### Parameters

  * ##### cb: (obj, item, index) => R
  *
    ##### initial: R = <!-- -->...

  #### Returns R

### [**](#remove)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/Collection.ts#L173)remove

* ****remove**\<TT>(entity, ...entities): void

- Overrides ArrayCollection.remove

  Remove specified item(s) from the collection. Note that removing item from collection does not necessarily imply deleting the target entity, it means we are disconnecting the relation - removing items from collection, not removing entities from database - `Collection.remove()` is not the same as `em.remove()`. If we want to delete the entity by removing it from collection, we need to enable `orphanRemoval: true`, which tells the ORM we don't want orphaned entities to exist, so we know those should be removed.

  ***

  #### Parameters

  * ##### entity: TT | [Reference](https://mikro-orm.io/api/core/class/Reference.md)\<TT> | Iterable\<TT | [Reference](https://mikro-orm.io/api/core/class/Reference.md)\<TT>, any, any> | (item) => boolean
  *
    ##### rest...entities: (TT | [Reference](https://mikro-orm.io/api/core/class/Reference.md)\<TT>)\[]

  #### Returns void

### [**](#removeAll)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/ArrayCollection.ts#L187)inheritedremoveAll

* ****removeAll**(): void

- Inherited from ArrayCollection.removeAll

  Remove all items from the collection. Note that removing items from collection does not necessarily imply deleting the target entity, it means we are disconnecting the relation - removing items from collection, not removing entities from database - `Collection.remove()` is not the same as `em.remove()`. If we want to delete the entity by removing it from collection, we need to enable `orphanRemoval: true`, which tells the ORM we don't want orphaned entities to exist, so we know those should be removed.

  ***

  #### Returns void

### [**](#set)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/ArrayCollection.ts#L105)inheritedset

* ****set**(items): void

- Inherited from ArrayCollection.set

  #### Parameters

  * ##### items: Iterable\<T | [Reference](https://mikro-orm.io/api/core/class/Reference.md)\<T>, any, any>

  #### Returns void

### [**](#setDirty)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/ArrayCollection.ts#L363)inheritedsetDirty

* ****setDirty**(dirty): void

- Inherited from ArrayCollection.setDirty

  #### Parameters

  * ##### dirty: boolean = <!-- -->true

  #### Returns void

### [**](#shouldPopulate)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/Collection.ts#L273)shouldPopulate

* ****shouldPopulate**(populated): boolean

- #### Parameters

  * ##### optionalpopulated: boolean

  #### Returns boolean

### [**](#slice)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/Collection.ts#L217)slice

* ****slice**(start, end): T\[]

- Overrides ArrayCollection.slice

  Extracts a slice of the collection items starting at position start to end (exclusive) of the collection. If end is null it returns all elements from start to the end of the collection.

  ***

  #### Parameters

  * ##### optionalstart: number
  * ##### optionalend: number

  #### Returns T\[]

### [**](#toArray)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/ArrayCollection.ts#L36)inheritedtoArray

* ****toArray**\<TT>(): [EntityDTO](https://mikro-orm.io/api/core.md#EntityDTO)\<TT>\[]

- Inherited from ArrayCollection.toArray

  #### Returns [EntityDTO](https://mikro-orm.io/api/core.md#EntityDTO)\<TT>\[]

### [**](#toJSON)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/Collection.ts#L154)toJSON

* ****toJSON**\<TT>(): [EntityDTO](https://mikro-orm.io/api/core.md#EntityDTO)\<TT>\[]

- Overrides ArrayCollection.toJSON

  #### Returns [EntityDTO](https://mikro-orm.io/api/core.md#EntityDTO)\<TT>\[]

### [**](#create)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/Collection.ts#L46)staticcreate

* ****create**\<T, O>(owner, prop, items, initialized): [Collection](https://mikro-orm.io/api/core/class/Collection.md)\<T, O>

- Creates new Collection instance, assigns it to the owning entity and sets the items to it (propagating them to their inverse sides)

  ***

  #### Parameters

  * ##### owner: O
  * ##### prop: [EntityKey](https://mikro-orm.io/api/core.md#EntityKey)\<O>
  * ##### items: undefined | T\[]
  * ##### initialized: boolean

  #### Returns [Collection](https://mikro-orm.io/api/core/class/Collection.md)\<T, O>
