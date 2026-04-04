# Source: https://mikro-orm.io/api/core/class/Cursor.md

# Cursor<!-- --> \<Entity, Hint, Fields, Excludes, IncludeCount>

As an alternative to the offset-based pagination with `limit` and `offset`, we can paginate based on a cursor. A cursor is an opaque string that defines a specific place in ordered entity graph. You can use `em.findByCursor()` to access those options. Under the hood, it will call `em.find()` and `em.count()` just like the `em.findAndCount()` method, but will use the cursor options instead.

Supports `before`, `after`, `first` and `last` options while disallowing `limit` and `offset`. Explicit `orderBy` option is required.

Use `first` and `after` for forward pagination, or `last` and `before` for backward pagination.

* `first` and `last` are numbers and serve as an alternative to `offset`, those options are mutually exclusive, use only one at a time
* `before` and `after` specify the previous cursor value

```
const currentCursor = await em.findByCursor(User, {}, {
  first: 10,
  after: previousCursor, // can be either string or `Cursor` instance
  orderBy: { id: 'desc' },
});

// to fetch next page
const nextCursor = await em.findByCursor(User, {}, {
  first: 10,
  after: currentCursor.endCursor, // or currentCursor.endCursor
  orderBy: { id: 'desc' },
});
```

The `Cursor` object provides the following interface:

```
Cursor<User> {
  items: [
    User { ... },
    User { ... },
    User { ... },
    ...
  ],
  totalCount: 50,
  length: 10,
  startCursor: 'WzRd',
  endCursor: 'WzZd',
  hasPrevPage: true,
  hasNextPage: true,
}
```

## Index[**](#Index)

### Constructors

* [**constructor](#constructor)

### Properties

* [**hasNextPage](#hasNextPage)
* [**hasPrevPage](#hasPrevPage)
* [**items](#items)
* [**totalCount](#totalCount)

### Accessors

* [**endCursor](#endCursor)
* [**length](#length)
* [**startCursor](#startCursor)

### Methods

* [**\[iterator\]](#\[iterator])
* [**from](#from)
* [**decode](#decode)
* [**encode](#encode)
* [**for](#for)
* [**getDefinition](#getDefinition)

## Constructors<!-- -->[**](#Constructors)

### [**](#constructor)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Cursor.ts#L71)constructor

* ****new Cursor**\<Entity, Hint, Fields, Excludes, IncludeCount>(items, totalCount, options, meta): [Cursor](https://mikro-orm.io/api/core/class/Cursor.md)\<Entity, Hint, Fields, Excludes, IncludeCount>

- #### Parameters

  * ##### items: [Loaded](https://mikro-orm.io/api/core.md#Loaded)\<Entity, Hint, Fields, Excludes>\[]
  * ##### totalCount: IncludeCount extends true ? number : undefined
  * ##### options: [FindByCursorOptions](https://mikro-orm.io/api/core/interface/FindByCursorOptions.md)\<Entity, Hint, Fields, Excludes, IncludeCount>
  * ##### meta: [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<Entity>

  #### Returns [Cursor](https://mikro-orm.io/api/core/class/Cursor.md)\<Entity, Hint, Fields, Excludes, IncludeCount>

## Properties<!-- -->[**](#Properties)

### [**](#hasNextPage)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Cursor.ts#L67)readonlyhasNextPage

**hasNextPage: boolean

### [**](#hasPrevPage)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Cursor.ts#L66)readonlyhasPrevPage

**hasPrevPage: boolean

### [**](#items)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Cursor.ts#L72)readonlyitems

**items: [Loaded](https://mikro-orm.io/api/core.md#Loaded)\<Entity, Hint, Fields, Excludes>\[]

### [**](#totalCount)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Cursor.ts#L73)readonlytotalCount

**totalCount: IncludeCount extends true ? number : undefined

## Accessors<!-- -->[**](#Accessors)

### [**](#endCursor)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Cursor.ts#L103)endCursor

* **get endCursor(): null | string

- #### Returns null | string

### [**](#length)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Cursor.ts#L153)length

* **get length(): number

- #### Returns number

### [**](#startCursor)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Cursor.ts#L95)startCursor

* **get startCursor(): null | string

- #### Returns null | string

## Methods<!-- -->[**](#Methods)

### [**](#\[iterator])[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Cursor.ts#L147)\[iterator]

* ****\[iterator]**(): IterableIterator<[Loaded](https://mikro-orm.io/api/core.md#Loaded)\<Entity, Hint, Fields, Excludes>, any, any>

- #### Returns IterableIterator<[Loaded](https://mikro-orm.io/api/core.md#Loaded)\<Entity, Hint, Fields, Excludes>, any, any>

### [**](#from)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Cursor.ts#L114)from

* ****from**(entity): string

- Computes the cursor value for a given entity.

  ***

  #### Parameters

  * ##### entity: Entity | [Loaded](https://mikro-orm.io/api/core.md#Loaded)\<Entity, Hint, Fields, Excludes>

  #### Returns string

### [**](#decode)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Cursor.ts#L169)staticdecode

* ****decode**(value): unknown\[]

- #### Parameters

  * ##### value: string

  #### Returns unknown\[]

### [**](#encode)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Cursor.ts#L165)staticencode

* ****encode**(value): string

- #### Parameters

  * ##### value: unknown\[]

  #### Returns string

### [**](#for)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Cursor.ts#L160)staticfor

* ****for**\<Entity>(meta, entity, orderBy): string

- Computes the cursor value for given entity and order definition.

  ***

  #### Parameters

  * ##### meta: [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<Entity>
  * ##### entity: [FilterObject](https://mikro-orm.io/api/core.md#FilterObject)\<Entity>
  * ##### orderBy: [OrderDefinition](https://mikro-orm.io/api/core.md#OrderDefinition)\<Entity>

  #### Returns string

### [**](#getDefinition)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/Cursor.ts#L179)staticgetDefinition

* ****getDefinition**\<Entity>(meta, orderBy): \[never, [QueryOrder](https://mikro-orm.io/api/core/enum/QueryOrder.md)]\[]

- #### Parameters

  * ##### meta: [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<Entity>
  * ##### orderBy: [OrderDefinition](https://mikro-orm.io/api/core.md#OrderDefinition)\<Entity>

  #### Returns \[never, [QueryOrder](https://mikro-orm.io/api/core/enum/QueryOrder.md)]\[]
