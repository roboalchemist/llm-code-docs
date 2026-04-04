# Source: https://mikro-orm.io/api/core/class/ArrayCollection.md

# ArrayCollection<!-- --> \<T, O>

### Hierarchy

* *ArrayCollection*
  * [Collection](https://mikro-orm.io/api/core/class/Collection.md)

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
* [**isDirty](#isDirty)
* [**isEmpty](#isEmpty)
* [**isInitialized](#isInitialized)
* [**isPartial](#isPartial)
* [**loadCount](#loadCount)
* [**map](#map)
* [**reduce](#reduce)
* [**remove](#remove)
* [**removeAll](#removeAll)
* [**set](#set)
* [**setDirty](#setDirty)
* [**slice](#slice)
* [**toArray](#toArray)
* [**toJSON](#toJSON)

## Constructors<!-- -->[**](#Constructors)

### [**](#constructor)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/ArrayCollection.ts#L19)constructor

* ****new ArrayCollection**\<T, O>(owner, items): [ArrayCollection](https://mikro-orm.io/api/core/class/ArrayCollection.md)\<T, O>

- #### Parameters

  * ##### owner: O
  * ##### optionalitems: T\[]

  #### Returns [ArrayCollection](https://mikro-orm.io/api/core/class/ArrayCollection.md)\<T, O>

## Properties<!-- -->[**](#Properties)

### [**](#owner)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/ArrayCollection.ts#L19)readonlyowner

**owner: O

## Accessors<!-- -->[**](#Accessors)

### [**](#length)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/ArrayCollection.ts#L367)length

* **get length(): number

- #### Returns number

## Methods<!-- -->[**](#Methods)

### [**](#\[iterator])[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/ArrayCollection.ts#L371)\[iterator]

* ****\[iterator]**(): IterableIterator\<T, any, any>

- #### Returns IterableIterator\<T, any, any>

### [**](#add)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/ArrayCollection.ts#L78)add

* ****add**(entity, ...entities): void

- #### Parameters

  * ##### entity: T | [Reference](https://mikro-orm.io/api/core/class/Reference.md)\<T> | Iterable\<T | [Reference](https://mikro-orm.io/api/core/class/Reference.md)\<T>, any, any>
  * ##### rest...entities: (T | [Reference](https://mikro-orm.io/api/core/class/Reference.md)\<T>)\[]

  #### Returns void

### [**](#contains)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/ArrayCollection.ts#L210)contains

* ****contains**(item, check): boolean

- #### Parameters

  * ##### item: T | [Reference](https://mikro-orm.io/api/core/class/Reference.md)\<T>
  * ##### optionalcheck: boolean

  #### Returns boolean

### [**](#count)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/ArrayCollection.ts#L333)count

* ****count**(): number

- #### Returns number

### [**](#exists)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/ArrayCollection.ts#L242)exists

* ****exists**(cb): boolean

- Tests for the existence of an element that satisfies the given predicate.

  ***

  #### Parameters

  * ##### cb: (item) => boolean


  #### Returns boolean

### [**](#filter)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/ArrayCollection.ts#L270)filter

* ****filter**(cb): T\[]

- Extracts a subset of the collection items.

  ***

  #### Parameters

  * ##### cb: (item, index) => boolean


  #### Returns T\[]

### [**](#find)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/ArrayCollection.ts#L255)find

* ****find**(cb): undefined | T

- Returns the first element of this collection that satisfies the predicate.

  ***

  #### Parameters

  * ##### cb: (item, index) => boolean


  #### Returns undefined | T

### [**](#getIdentifiers)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/ArrayCollection.ts#L51)getIdentifiers

* ****getIdentifiers**\<U>(field): U\[]

- #### Parameters

  * ##### optionalfield: string | string\[]

  #### Returns U\[]

### [**](#getItems)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/ArrayCollection.ts#L32)getItems

* ****getItems**(): T\[]

- #### Returns T\[]

### [**](#indexBy)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/ArrayCollection.ts#L314)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/ArrayCollection.ts#L320)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/ArrayCollection.ts#L326)indexBy

* ****indexBy**\<K1, K2>(key): Record\<T\[K1] & PropertyKey, T>
* ****indexBy**\<K1, K2>(key, valueKey): Record\<T\[K1] & PropertyKey, T\[K2]>

- Maps the collection items to a dictionary, indexed by the key you specify. If there are more items with the same key, only the first one will be present.

  ***

  #### Parameters

  * ##### key: K1

  #### Returns Record\<T\[K1] & PropertyKey, T>

### [**](#isDirty)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/ArrayCollection.ts#L351)isDirty

* ****isDirty**(): boolean

- #### Returns boolean

### [**](#isEmpty)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/ArrayCollection.ts#L359)isEmpty

* ****isEmpty**(): boolean

- #### Returns boolean

### [**](#isInitialized)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/ArrayCollection.ts#L337)isInitialized

* ****isInitialized**(fully): boolean

- #### Parameters

  * ##### fully: boolean = <!-- -->false

  #### Returns boolean

### [**](#isPartial)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/ArrayCollection.ts#L355)isPartial

* ****isPartial**(): boolean

- #### Returns boolean

### [**](#loadCount)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/ArrayCollection.ts#L28)loadCount

* ****loadCount**(): Promise\<number>

- #### Returns Promise\<number>

### [**](#map)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/ArrayCollection.ts#L286)map

* ****map**\<R>(mapper): R\[]

- Maps the collection items based on your provided mapper function.

  ***

  #### Parameters

  * ##### mapper: (item, index) => R


  #### Returns R\[]

### [**](#reduce)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/ArrayCollection.ts#L300)reduce

* ****reduce**\<R>(cb, initial): R

- Maps the collection items based on your provided mapper function to a single object.

  ***

  #### Parameters

  * ##### cb: (obj, item, index) => R
  *
    ##### initial: R = <!-- -->...

  #### Returns R

### [**](#remove)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/ArrayCollection.ts#L157)remove

* ****remove**(entity, ...entities): void

- Remove specified item(s) from the collection. Note that removing item from collection does not necessarily imply deleting the target entity, it means we are disconnecting the relation - removing items from collection, not removing entities from database - `Collection.remove()` is not the same as `em.remove()`. If we want to delete the entity by removing it from collection, we need to enable `orphanRemoval: true`, which tells the ORM we don't want orphaned entities to exist, so we know those should be removed.

  ***

  #### Parameters

  * ##### entity: T | [Reference](https://mikro-orm.io/api/core/class/Reference.md)\<T> | Iterable\<T | [Reference](https://mikro-orm.io/api/core/class/Reference.md)\<T>, any, any>
  * ##### rest...entities: (T | [Reference](https://mikro-orm.io/api/core/class/Reference.md)\<T>)\[]

  #### Returns void

### [**](#removeAll)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/ArrayCollection.ts#L187)removeAll

* ****removeAll**(): void

- Remove all items from the collection. Note that removing items from collection does not necessarily imply deleting the target entity, it means we are disconnecting the relation - removing items from collection, not removing entities from database - `Collection.remove()` is not the same as `em.remove()`. If we want to delete the entity by removing it from collection, we need to enable `orphanRemoval: true`, which tells the ORM we don't want orphaned entities to exist, so we know those should be removed.

  ***

  #### Returns void

### [**](#set)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/ArrayCollection.ts#L105)set

* ****set**(items): void

- #### Parameters

  * ##### items: Iterable\<T | [Reference](https://mikro-orm.io/api/core/class/Reference.md)\<T>, any, any>

  #### Returns void

### [**](#setDirty)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/ArrayCollection.ts#L363)setDirty

* ****setDirty**(dirty): void

- #### Parameters

  * ##### dirty: boolean = <!-- -->true

  #### Returns void

### [**](#slice)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/ArrayCollection.ts#L219)slice

* ****slice**(start, end): T\[]

- Extracts a slice of the collection items starting at position start to end (exclusive) of the collection. If end is null it returns all elements from start to the end of the collection.

  ***

  #### Parameters

  * ##### start: number = <!-- -->0
  * ##### optionalend: number

  #### Returns T\[]

### [**](#toArray)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/ArrayCollection.ts#L36)toArray

* ****toArray**\<TT>(): [EntityDTO](https://mikro-orm.io/api/core.md#EntityDTO)\<TT>\[]

- #### Returns [EntityDTO](https://mikro-orm.io/api/core.md#EntityDTO)\<TT>\[]

### [**](#toJSON)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/ArrayCollection.ts#L47)toJSON

* ****toJSON**(): [EntityDTO](https://mikro-orm.io/api/core.md#EntityDTO)\<T>\[]

- #### Returns [EntityDTO](https://mikro-orm.io/api/core.md#EntityDTO)\<T>\[]
