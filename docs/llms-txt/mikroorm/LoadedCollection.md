# Source: https://mikro-orm.io/api/core/interface/LoadedCollection.md

# LoadedCollection<!-- --> \<T>

### Hierarchy

* [Collection](https://mikro-orm.io/api/core/class/Collection.md)\<T>
  * *LoadedCollection*

## Index[**](#index)

### Properties

* [**$](#$)
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
* [**get](#get)
* [**getIdentifiers](#getIdentifiers)
* [**getItems](#getitems)
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

## Properties<!-- -->[**](#properties)

### [**](#$)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1799)$

**$: [Collection](https://mikro-orm.io/api/core/class/Collection.md)\<T, object>

### [**](#owner)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/Collection.ts#L48)readonlyinheritedowner

**owner: object

Inherited from Collection.owner

## Accessors<!-- -->[**](#accessors)

### [**](#length)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/Collection.ts#L822)inheritedlength

* **get length(): number

* Inherited from Collection.length

  #### Returns number

## Methods<!-- -->[**](#methods)

### [**](#\[iterator])[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/Collection.ts#L826)inherited\[iterator]

* ****\[iterator]**(): IterableIterator\<T, any, any>

* Inherited from Collection.\[iterator]

  #### Returns IterableIterator\<T, any, any>

### [**](#add)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/Collection.ts#L208)inheritedadd

* ****add**\<TT>(entity, ...entities): number

* Inherited from Collection.add

  #### Parameters

  * ##### entity: TT | [Reference](https://mikro-orm.io/api/core/class/Reference.md)\<TT> | Iterable\<TT | [Reference](https://mikro-orm.io/api/core/class/Reference.md)\<TT>, any, any>

  * ##### rest...entities: (TT | [Reference](https://mikro-orm.io/api/core/class/Reference.md)\<TT>)\[]

  #### Returns number

### [**](#contains)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/Collection.ts#L300)inheritedcontains

* ****contains**\<TT>(item, check): boolean

* Inherited from Collection.contains

  #### Parameters

  * ##### item: TT | [Reference](https://mikro-orm.io/api/core/class/Reference.md)\<TT>

  * ##### check: boolean = <!-- -->true

  #### Returns boolean

### [**](#count)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/Collection.ts#L309)inheritedcount

* ****count**(): number

* Inherited from Collection.count

  #### Returns number

### [**](#exists)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/Collection.ts#L676)inheritedexists

* ****exists**(cb): boolean

* Inherited from Collection.exists

  Tests for the existence of an element that satisfies the given predicate.

  ***

  #### Parameters

  * ##### cb: (item) => boolean

  #### Returns boolean

### [**](#filter)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/Collection.ts#L717)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/Collection.ts#L722)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/Collection.ts#L727)inheritedfilter

* ****filter**\<S>(cb): S\[]
* ****filter**(cb): T\[]

* Inherited from Collection.filter

  Extracts a subset of the collection items.

  ***

  #### Parameters

  * ##### cb: (item, index) => item is S

  #### Returns S\[]

### [**](#find)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/Collection.ts#L691)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/Collection.ts#L696)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/Collection.ts#L701)inheritedfind

* ****find**\<S>(cb): undefined | S
* ****find**(cb): undefined | T

* Inherited from Collection.find

  Returns the first element of this collection that satisfies the predicate.

  ***

  #### Parameters

  * ##### cb: (item, index) => item is S

  #### Returns undefined | S

### [**](#get)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1800)get

* ****get**(): [Collection](https://mikro-orm.io/api/core/class/Collection.md)\<T, object>

* #### Returns [Collection](https://mikro-orm.io/api/core/class/Collection.md)\<T, object>

### [**](#getIdentifiers)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/Collection.ts#L531)inheritedgetIdentifiers

* ****getIdentifiers**\<U>(field): U\[]

* Inherited from Collection.getIdentifiers

  #### Parameters

  * ##### optionalfield: string | string\[]

  #### Returns U\[]

### [**](#getitems)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/typings.ts#L1801)getItems

* ****getItems**(check): T\[]

* Overrides Collection.getItems

  Returns the items (the collection must be initialized)

  ***

  #### Parameters

  * ##### optionalcheck: boolean

  #### Returns T\[]

### [**](#indexBy)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/Collection.ts#L774)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/Collection.ts#L780)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/Collection.ts#L786)inheritedindexBy

* ****indexBy**\<K1, K2>(key): Record\<T\[K1] & PropertyKey, T>
* ****indexBy**\<K1, K2>(key, valueKey): Record\<T\[K1] & PropertyKey, T\[K2]>

* Inherited from Collection.indexBy

  Maps the collection items to a dictionary, indexed by the key you specify. If there are more items with the same key, only the first one will be present.

  ***

  #### Parameters

  * ##### key: K1

  #### Returns Record\<T\[K1] & PropertyKey, T>

### [**](#init)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/Collection.ts#L335)inheritedinit

* ****init**\<TT, P>(options): Promise<[LoadedCollection](https://mikro-orm.io/api/core/interface/LoadedCollection.md)<[Loaded](https://mikro-orm.io/api/core.md#Loaded)\<TT, P>>>

* Inherited from Collection.init

  #### Parameters

  * ##### options: [InitCollectionOptions](https://mikro-orm.io/api/core/interface/InitCollectionOptions.md)\<TT, P, \*, never> = <!-- -->{}

  #### Returns Promise<[LoadedCollection](https://mikro-orm.io/api/core/interface/LoadedCollection.md)<[Loaded](https://mikro-orm.io/api/core.md#Loaded)\<TT, P>>>

### [**](#isDirty)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/Collection.ts#L810)inheritedisDirty

* ****isDirty**(): boolean

* Inherited from Collection.isDirty

  #### Returns boolean

### [**](#isEmpty)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/Collection.ts#L314)inheritedisEmpty

* ****isEmpty**(): boolean

* Inherited from Collection.isEmpty

  #### Returns boolean

### [**](#isInitialized)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/Collection.ts#L796)inheritedisInitialized

* ****isInitialized**(fully): boolean

* Inherited from Collection.isInitialized

  #### Parameters

  * ##### fully: boolean = <!-- -->false

  #### Returns boolean

### [**](#isPartial)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/Collection.ts#L814)inheritedisPartial

* ****isPartial**(): boolean

* Inherited from Collection.isPartial

  #### Returns boolean

### [**](#load)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/Collection.ts#L86)inheritedload

* ****load**\<TT, P>(options): Promise<[LoadedCollection](https://mikro-orm.io/api/core/interface/LoadedCollection.md)<[Loaded](https://mikro-orm.io/api/core.md#Loaded)\<TT, P>>>

* Inherited from Collection.load

  Ensures the collection is loaded first (without reloading it if it already is loaded). Returns the Collection instance (itself), works the same as `Reference.load()`.

  ***

  #### Parameters

  * ##### options: [InitCollectionOptions](https://mikro-orm.io/api/core/interface/InitCollectionOptions.md)\<TT, P, \*, never> = <!-- -->{}

  #### Returns Promise<[LoadedCollection](https://mikro-orm.io/api/core/interface/LoadedCollection.md)<[Loaded](https://mikro-orm.io/api/core.md#Loaded)\<TT, P>>>

### [**](#loadCount)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/Collection.ts#L123)inheritedloadCount

* ****loadCount**(options): Promise\<number>

* Inherited from Collection.loadCount

  Gets the count of collection items from database instead of counting loaded items. The value is cached (unless you use the `where` option), use `refresh: true` to force reload it.

  ***

  #### Parameters

  * ##### options: boolean | [LoadCountOptions](https://mikro-orm.io/api/core/interface/LoadCountOptions.md)\<T> = <!-- -->{}

  #### Returns Promise\<number>

### [**](#loadItems)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/Collection.ts#L112)inheritedloadItems

* ****loadItems**\<TT, P>(options): Promise<[Loaded](https://mikro-orm.io/api/core.md#Loaded)\<TT, P>\[]>

* Inherited from Collection.loadItems

  Initializes the collection and returns the items

  ***

  #### Parameters

  * ##### optionaloptions: [InitCollectionOptions](https://mikro-orm.io/api/core/interface/InitCollectionOptions.md)\<TT, P, \*, never>

  #### Returns Promise<[Loaded](https://mikro-orm.io/api/core.md#Loaded)\<TT, P>\[]>

### [**](#map)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/Collection.ts#L744)inheritedmap

* ****map**\<R>(mapper): R\[]

* Inherited from Collection.map

  Maps the collection items based on your provided mapper function.

  ***

  #### Parameters

  * ##### mapper: (item, index) => R

  #### Returns R\[]

### [**](#matching)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/Collection.ts#L151)inheritedmatching

* ****matching**\<TT, P>(options): Promise<[Loaded](https://mikro-orm.io/api/core.md#Loaded)\<TT, P>\[]>

* Inherited from Collection.matching

  #### Parameters

  * ##### options: [MatchingOptions](https://mikro-orm.io/api/core/interface/MatchingOptions.md)\<T, P>

  #### Returns Promise<[Loaded](https://mikro-orm.io/api/core.md#Loaded)\<TT, P>\[]>

### [**](#populated)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/Collection.ts#L331)inheritedpopulated

* ****populated**(populated): void

* Inherited from Collection.populated

  #### Parameters

  * ##### populated: undefined | boolean = <!-- -->true

  #### Returns void

### [**](#reduce)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/Collection.ts#L759)inheritedreduce

* ****reduce**\<R>(cb, initial): R

* Inherited from Collection.reduce

  Maps the collection items based on your provided mapper function to a single object.

  ***

  #### Parameters

  * ##### cb: (obj, item, index) => R

  *

    ##### initial: R = <!-- -->

  #### Returns R

### [**](#remove)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/Collection.ts#L246)inheritedremove

* ****remove**\<TT>(entity, ...entities): number

* Inherited from Collection.remove

  Remove specified item(s) from the collection. Note that removing item from collection does not necessarily imply deleting the target entity, it means we are disconnecting the relation - removing items from collection, not removing entities from database - `Collection.remove()` is not the same as `em.remove()`. If we want to delete the entity by removing it from collection, we need to enable `orphanRemoval: true`, which tells the ORM we don't want orphaned entities to exist, so we know those should be removed.

  ***

  #### Parameters

  * ##### entity: TT | [Reference](https://mikro-orm.io/api/core/class/Reference.md)\<TT> | Iterable\<TT | [Reference](https://mikro-orm.io/api/core/class/Reference.md)\<TT>, any, any> | (item) => boolean

  *

    ##### rest...entities: (TT | [Reference](https://mikro-orm.io/api/core/class/Reference.md)\<TT>)\[]

  #### Returns number

### [**](#removeAll)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/Collection.ts#L624)inheritedremoveAll

* ****removeAll**(): void

* Inherited from Collection.removeAll

  Remove all items from the collection. Note that removing items from collection does not necessarily imply deleting the target entity, it means we are disconnecting the relation - removing items from collection, not removing entities from database - `Collection.remove()` is not the same as `em.remove()`. If we want to delete the entity by removing it from collection, we need to enable `orphanRemoval: true`, which tells the ORM we don't want orphaned entities to exist, so we know those should be removed.

  ***

  #### Returns void

### [**](#set)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/Collection.ts#L572)inheritedset

* ****set**(items): void

* Inherited from Collection.set

  #### Parameters

  * ##### items: Iterable\<T | [Reference](https://mikro-orm.io/api/core/class/Reference.md)\<T>, any, any>

  #### Returns void

### [**](#setDirty)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/Collection.ts#L818)inheritedsetDirty

* ****setDirty**(dirty): void

* Inherited from Collection.setDirty

  #### Parameters

  * ##### dirty: boolean = <!-- -->true

  #### Returns void

### [**](#shouldPopulate)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/Collection.ts#L319)inheritedshouldPopulate

* ****shouldPopulate**(populated): boolean

* Inherited from Collection.shouldPopulate

  #### Parameters

  * ##### optionalpopulated: boolean

  #### Returns boolean

### [**](#slice)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/Collection.ts#L652)inheritedslice

* ****slice**(start, end): T\[]

* Inherited from Collection.slice

  Extracts a slice of the collection items starting at position start to end (exclusive) of the collection. If end is null it returns all elements from start to the end of the collection.

  ***

  #### Parameters

  * ##### start: number = <!-- -->0

  * ##### optionalend: number

  #### Returns T\[]

### [**](#toArray)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/Collection.ts#L523)inheritedtoArray

* ****toArray**\<TT>(): [EntityDTO](https://mikro-orm.io/api/core.md#EntityDTO)\<TT>\[]

* Inherited from Collection.toArray

  #### Returns [EntityDTO](https://mikro-orm.io/api/core.md#EntityDTO)\<TT>\[]

### [**](#toJSON)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/Collection.ts#L200)inheritedtoJSON

* ****toJSON**\<TT>(): [EntityDTO](https://mikro-orm.io/api/core.md#EntityDTO)\<TT>\[]

* Inherited from Collection.toJSON

  #### Returns [EntityDTO](https://mikro-orm.io/api/core.md#EntityDTO)\<TT>\[]
