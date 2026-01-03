# Source: https://mikro-orm.io/api/core/interface/EventArgs.md

# EventArgs<!-- --> \<T>

## Index[**](#Index)

### Properties

* [**changeSet](#changeSet)
* [**em](#em)
* [**entity](#entity)
* [**meta](#meta)

## Properties<!-- -->[**](#Properties)

### [**](#changeSet)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/events/EventSubscriber.ts#L10)optionalchangeSet

**changeSet?

<!-- -->

: [ChangeSet](https://mikro-orm.io/api/core/class/ChangeSet.md)\<T & {}>

### [**](#em)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/events/EventSubscriber.ts#L8)em

**em: [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>

### [**](#entity)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/events/EventSubscriber.ts#L7)entity

**entity: T

### [**](#meta)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/events/EventSubscriber.ts#L9)meta

**meta: [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<T>
