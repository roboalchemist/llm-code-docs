# Source: https://mikro-orm.io/api/core/interface/EventArgs.md

# EventArgs<!-- --> \<T>

## Index[**](#index)

### Properties

* [**em](#em)
* [**entity](#entity)
* [**changeSet](#changeSet)
* [**meta](#meta)

## Properties<!-- -->[**](#properties)

### [**](#em)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/events/EventSubscriber.ts#L9)em

**em: [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>

### [**](#entity)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/events/EventSubscriber.ts#L8)entity

**entity: T

### [**](#changeSet)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/events/EventSubscriber.ts#L11)optionalchangeSet

**changeSet?

<!-- -->

: [ChangeSet](https://mikro-orm.io/api/core/class/ChangeSet.md)\<T & {}>

### [**](#meta)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/events/EventSubscriber.ts#L10)meta

**meta: [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<T, [EntityCtor](https://mikro-orm.io/api/core.md#EntityCtor)\<T>>
