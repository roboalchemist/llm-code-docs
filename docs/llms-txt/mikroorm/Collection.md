# Source: https://mikro-orm.io/api/core/class/Collection.md

# Collection<!-- --> \<T, O>

### Hierarchy

* *Collection*
  * [LoadedCollection](https://mikro-orm.io/api/core/interface/LoadedCollection.md)

## Index[**](#index)

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
* [**getIdentifiers](#getidentifiers)
* [**getItems](#getitems)
* [**indexBy](#indexby)
* [**init](#init)
* [**isDirty](#isdirty)
* [**isEmpty](#isempty)
* [**isInitialized](#isinitialized)
* [**isPartial](#ispartial)
* [**load](#load)
* [**loadCount](#loadcount)
* [**loadItems](#loaditems)
* [**map](#map)
* [**matching](#matching)
* [**populated](#populated)
* [**reduce](#reduce)
* [**remove](#remove)
* [**removeAll](#removeall)
* [**set](#set)
* [**setDirty](#setdirty)
* [**shouldPopulate](#shouldpopulate)
* [**slice](#slice)
* [**toArray](#toarray)
* [**toJSON](#tojson)
* [**create](#create)

## Constructors<!-- -->[**](#constructors)

### [**](#constructor)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/Collection.ts#L47)constructor

* ****new Collection**\<T, O>(owner, items, initialized): [Collection](https://mikro-orm.io/api/core/class/Collection.md)\<T, O>

* #### Parameters

  * ##### owner: O

  * ##### optionalitems: T\[]

  * ##### initialized: boolean = <!-- -->true

  #### Returns [Collection](https://mikro-orm.io/api/core/class/Collection.md)\<T, O>

## Properties<!-- -->[**](#properties)

### [**](#owner)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/Collection.ts#L48)readonlyowner

**owner: O

## Accessors<!-- -->[**](#accessors)

### [**](#length)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/Collection.ts#L822)length

* **get length(): number

* #### Returns number

## Methods<!-- -->[**](#methods)

### [**](#\[iterator])[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/Collection.ts#L826)\[iterator]

* ****\[iterator]**(): IterableIterator\<T, any, any>

* #### Returns IterableIterator\<T, any, any>

### [**](#add)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/Collection.ts#L208)add

* ****add**\<TT>(entity, ...entities): number

* #### Parameters

  * ##### entity: TT | [Reference](https://mikro-orm.io/api/core/class/Reference.md)\<TT> | Iterable\<TT | [Reference](https://mikro-orm.io/api/core/class/Reference.md)\<TT>, any, any>

  * ##### rest...entities: (TT | [Reference](https://mikro-orm.io/api/core/class/Reference.md)\<TT>)\[]

  #### Returns number

### [**](#contains)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/Collection.ts#L300)contains

* ****contains**\<TT>(item, check): boolean

* #### Parameters

  * ##### item: TT | [Reference](https://mikro-orm.io/api/core/class/Reference.md)\<TT>

  * ##### check: boolean = <!-- -->true

  #### Returns boolean

### [**](#count)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/Collection.ts#L309)count

* ****count**(): number

* #### Returns number

### [**](#exists)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/Collection.ts#L676)exists

* ****exists**(cb): boolean

* Tests for the existence of an element that satisfies the given predicate.

  ***

  #### Parameters

  * ##### cb: (item) => boolean

  #### Returns boolean

### [**](#filter)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/Collection.ts#L717)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/Collection.ts#L722)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/Collection.ts#L727)filter

* ****filter**\<S>(cb): S\[]
* ****filter**(cb): T\[]

* Extracts a subset of the collection items.

  ***

  #### Parameters

  * ##### cb: (item, index) => item is S

  #### Returns S\[]

### [**](#find)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/Collection.ts#L691)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/Collection.ts#L696)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/Collection.ts#L701)find

* ****find**\<S>(cb): undefined | S
* ****find**(cb): undefined | T

* Returns the first element of this collection that satisfies the predicate.

  ***

  #### Parameters

  * ##### cb: (item, index) => item is S

  #### Returns undefined | S

### [**](#getidentifiers)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/Collection.ts#L531)getIdentifiers

* ****getIdentifiers**\<U>(field): U\[]

* #### Parameters

  * ##### optionalfield: string | string\[]

  #### Returns U\[]

### [**](#getitems)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/Collection.ts#L192)getItems

* ****getItems**(check): T\[]

* Returns the items (the collection must be initialized)

  ***

  #### Parameters

  * ##### check: boolean = <!-- -->true

  #### Returns T\[]

### [**](#indexby)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/Collection.ts#L774)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/Collection.ts#L780)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/Collection.ts#L786)indexBy

* ****indexBy**\<K1, K2>(key): Record\<T\[K1] & PropertyKey, T>
* ****indexBy**\<K1, K2>(key, valueKey): Record\<T\[K1] & PropertyKey, T\[K2]>

* Maps the collection items to a dictionary, indexed by the key you specify. If there are more items with the same key, only the first one will be present.

  ***

  #### Parameters

  * ##### key: K1

  #### Returns Record\<T\[K1] & PropertyKey, T>

### [**](#init)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/Collection.ts#L335)init

* ****init**\<TT, P>(options): Promise<[LoadedCollection](https://mikro-orm.io/api/core/interface/LoadedCollection.md)<[Loaded](https://mikro-orm.io/api/core.md#Loaded)\<TT, P>>>

* #### Parameters

  * ##### options: [InitCollectionOptions](https://mikro-orm.io/api/core/interface/InitCollectionOptions.md)\<TT, P, \*, never> = <!-- -->{}

  #### Returns Promise<[LoadedCollection](https://mikro-orm.io/api/core/interface/LoadedCollection.md)<[Loaded](https://mikro-orm.io/api/core.md#Loaded)\<TT, P>>>

### [**](#isdirty)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/Collection.ts#L810)isDirty

* ****isDirty**(): boolean

* #### Returns boolean

### [**](#isempty)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/Collection.ts#L314)isEmpty

* ****isEmpty**(): boolean

* #### Returns boolean

### [**](#isinitialized)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/Collection.ts#L796)isInitialized

* ****isInitialized**(fully): boolean

* #### Parameters

  * ##### fully: boolean = <!-- -->false

  #### Returns boolean

### [**](#ispartial)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/Collection.ts#L814)isPartial

* ****isPartial**(): boolean

* #### Returns boolean

### [**](#load)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/Collection.ts#L86)load

* ****load**\<TT, P>(options): Promise<[LoadedCollection](https://mikro-orm.io/api/core/interface/LoadedCollection.md)<[Loaded](https://mikro-orm.io/api/core.md#Loaded)\<TT, P>>>

* Ensures the collection is loaded first (without reloading it if it already is loaded). Returns the Collection instance (itself), works the same as `Reference.load()`.

  ***

  #### Parameters

  * ##### options: [InitCollectionOptions](https://mikro-orm.io/api/core/interface/InitCollectionOptions.md)\<TT, P, \*, never> = <!-- -->{}

  #### Returns Promise<[LoadedCollection](https://mikro-orm.io/api/core/interface/LoadedCollection.md)<[Loaded](https://mikro-orm.io/api/core.md#Loaded)\<TT, P>>>

### [**](#loadcount)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/Collection.ts#L123)loadCount

* ****loadCount**(options): Promise\<number>

* Gets the count of collection items from database instead of counting loaded items. The value is cached (unless you use the `where` option), use `refresh: true` to force reload it.

  ***

  #### Parameters

  * ##### options: boolean | [LoadCountOptions](https://mikro-orm.io/api/core/interface/LoadCountOptions.md)\<T> = <!-- -->{}

  #### Returns Promise\<number>

### [**](#loaditems)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/Collection.ts#L112)loadItems

* ****loadItems**\<TT, P>(options): Promise<[Loaded](https://mikro-orm.io/api/core.md#Loaded)\<TT, P>\[]>

* Initializes the collection and returns the items

  ***

  #### Parameters

  * ##### optionaloptions: [InitCollectionOptions](https://mikro-orm.io/api/core/interface/InitCollectionOptions.md)\<TT, P, \*, never>

  #### Returns Promise<[Loaded](https://mikro-orm.io/api/core.md#Loaded)\<TT, P>\[]>

### [**](#map)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/Collection.ts#L744)map

* ****map**\<R>(mapper): R\[]

* Maps the collection items based on your provided mapper function.

  ***

  #### Parameters

  * ##### mapper: (item, index) => R

  #### Returns R\[]

### [**](#matching)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/Collection.ts#L151)matching

* ****matching**\<TT, P>(options): Promise<[Loaded](https://mikro-orm.io/api/core.md#Loaded)\<TT, P>\[]>

* #### Parameters

  * ##### options: [MatchingOptions](https://mikro-orm.io/api/core/interface/MatchingOptions.md)\<T, P>

  #### Returns Promise<[Loaded](https://mikro-orm.io/api/core.md#Loaded)\<TT, P>\[]>

### [**](#populated)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/Collection.ts#L331)populated

* ****populated**(populated): void

* #### Parameters

  * ##### populated: undefined | boolean = <!-- -->true

  #### Returns void

### [**](#reduce)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/Collection.ts#L759)reduce

* ****reduce**\<R>(cb, initial): R

* Maps the collection items based on your provided mapper function to a single object.

  ***

  #### Parameters

  * ##### cb: (obj, item, index) => R

  *

    ##### initial: R = <!-- -->

  #### Returns R

### [**](#remove)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/Collection.ts#L246)remove

* ****remove**\<TT>(entity, ...entities): number

* Remove specified item(s) from the collection. Note that removing item from collection does not necessarily imply deleting the target entity, it means we are disconnecting the relation - removing items from collection, not removing entities from database - `Collection.remove()` is not the same as `em.remove()`. If we want to delete the entity by removing it from collection, we need to enable `orphanRemoval: true`, which tells the ORM we don't want orphaned entities to exist, so we know those should be removed.

  ***

  #### Parameters

  * ##### entity: TT | [Reference](https://mikro-orm.io/api/core/class/Reference.md)\<TT> | Iterable\<TT | [Reference](https://mikro-orm.io/api/core/class/Reference.md)\<TT>, any, any> | (item) => boolean

  *

    ##### rest...entities: (TT | [Reference](https://mikro-orm.io/api/core/class/Reference.md)\<TT>)\[]

  #### Returns number

### [**](#removeall)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/Collection.ts#L624)removeAll

* ****removeAll**(): void

* Remove all items from the collection. Note that removing items from collection does not necessarily imply deleting the target entity, it means we are disconnecting the relation - removing items from collection, not removing entities from database - `Collection.remove()` is not the same as `em.remove()`. If we want to delete the entity by removing it from collection, we need to enable `orphanRemoval: true`, which tells the ORM we don't want orphaned entities to exist, so we know those should be removed.

  ***

  #### Returns void

### [**](#set)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/Collection.ts#L572)set

* ****set**(items): void

* #### Parameters

  * ##### items: Iterable\<T | [Reference](https://mikro-orm.io/api/core/class/Reference.md)\<T>, any, any>

  #### Returns void

### [**](#setdirty)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/Collection.ts#L818)setDirty

* ****setDirty**(dirty): void

* #### Parameters

  * ##### dirty: boolean = <!-- -->true

  #### Returns void

### [**](#shouldpopulate)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/Collection.ts#L319)shouldPopulate

* ****shouldPopulate**(populated): boolean

* #### Parameters

  * ##### optionalpopulated: boolean

  #### Returns boolean

### [**](#slice)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/Collection.ts#L652)slice

* ****slice**(start, end): T\[]

* Extracts a slice of the collection items starting at position start to end (exclusive) of the collection. If end is null it returns all elements from start to the end of the collection.

  ***

  #### Parameters

  * ##### start: number = <!-- -->0

  * ##### optionalend: number

  #### Returns T\[]

### [**](#toarray)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/Collection.ts#L523)toArray

* ****toArray**\<TT>(): [EntityDTO](https://mikro-orm.io/api/core.md#EntityDTO)\<TT>\[]

* #### Returns [EntityDTO](https://mikro-orm.io/api/core.md#EntityDTO)\<TT>\[]

### [**](#tojson)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/Collection.ts#L200)toJSON

* ****toJSON**\<TT>(): [EntityDTO](https://mikro-orm.io/api/core.md#EntityDTO)\<TT>\[]

* #### Returns [EntityDTO](https://mikro-orm.io/api/core.md#EntityDTO)\<TT>\[]

### [**](#create)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/Collection.ts#L65)staticcreate

* ****create**\<T, O>(owner, prop, items, initialized): [Collection](https://mikro-orm.io/api/core/class/Collection.md)\<T, O>

* Creates new Collection instance, assigns it to the owning entity and sets the items to it (propagating them to their inverse sides)

  ***

  #### Parameters

  * ##### owner: O

  * ##### prop: [EntityKey](https://mikro-orm.io/api/core.md#EntityKey)\<O>

  * ##### items: undefined | T\[]

  * ##### initialized: boolean

  #### Returns [Collection](https://mikro-orm.io/api/core/class/Collection.md)\<T, O>
