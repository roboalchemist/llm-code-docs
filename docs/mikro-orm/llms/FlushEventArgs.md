# Source: https://mikro-orm.io/api/core/interface/FlushEventArgs.md

# FlushEventArgs<!-- -->

### Hierarchy

* Omit<[EventArgs](https://mikro-orm.io/api/core/interface/EventArgs.md)\<any>, entity | changeSet | meta>
  * *FlushEventArgs*

## Index[**](#Index)

### Properties

* [**em](#em)
* [**uow](#uow)

## Properties<!-- -->[**](#Properties)

### [**](#em)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/events/EventSubscriber.ts#L8)inheritedem

**em: [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>

Inherited from Omit.em

### [**](#uow)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/events/EventSubscriber.ts#L14)uow

**uow: [UnitOfWork](https://mikro-orm.io/api/core/class/UnitOfWork.md)
