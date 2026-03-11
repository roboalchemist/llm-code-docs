# Source: https://mikro-orm.io/api/core/interface/FlushEventArgs.md

# FlushEventArgs<!-- -->

### Hierarchy

* Omit<[EventArgs](https://mikro-orm.io/api/core/interface/EventArgs.md)\<any>, entity | changeSet | meta>
  * *FlushEventArgs*

## Index[**](#index)

### Properties

* [**em](#em)
* [**uow](#uow)

## Properties<!-- -->[**](#properties)

### [**](#em)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/events/EventSubscriber.ts#L9)inheritedem

**em: [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>

Inherited from Omit.em

### [**](#uow)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/events/EventSubscriber.ts#L15)uow

**uow: [UnitOfWork](https://mikro-orm.io/api/core/class/UnitOfWork.md)
