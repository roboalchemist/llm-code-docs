# Source: https://mikro-orm.io/api/core/class/RequestContext.md

# RequestContext<!-- -->

Uses `AsyncLocalStorage` to create async context that holds the current EM fork.

## Index[**](#index)

### Constructors

* [**constructor](#constructor)

### Properties

* [**id](#id)
* [**map](#map)

### Accessors

* [**em](#em)

### Methods

* [**create](#create)
* [**currentRequestContext](#currentRequestContext)
* [**enter](#enter)
* [**getEntityManager](#getEntityManager)

## Constructors<!-- -->[**](#constructors)

### [**](#constructor)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/RequestContext.ts#L13)constructor

* ****new RequestContext**(map): [RequestContext](https://mikro-orm.io/api/core/class/RequestContext.md)

* #### Parameters

  * ##### map: Map\<string, [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>>

  #### Returns [RequestContext](https://mikro-orm.io/api/core/class/RequestContext.md)

## Properties<!-- -->[**](#properties)

### [**](#id)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/RequestContext.ts#L11)readonlyid

**id: number =

<!-- -->

...

### [**](#map)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/RequestContext.ts#L13)readonlymap

**map: Map\<string, [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>>

## Accessors<!-- -->[**](#accessors)

### [**](#em)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/RequestContext.ts#L18)em

* **get em(): undefined | [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>

* Returns default EntityManager.

  ***

  #### Returns undefined | [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>

## Methods<!-- -->[**](#methods)

### [**](#create)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/RequestContext.ts#L27)staticcreate

* ****create**\<T>(em, next, options): T

* Creates new RequestContext instance and runs the code inside its domain. If the handler is async, the return value needs to be awaited. Uses `AsyncLocalStorage.run()`, suitable for regular express style middlewares with a `next` callback.

  ***

  #### Parameters

  * ##### em: [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>> | [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>\[]

  * ##### next: (...args) => T

  *

    ##### options: [CreateContextOptions](https://mikro-orm.io/api/core/interface/CreateContextOptions.md) = <!-- -->{}

  #### Returns T

### [**](#currentRequestContext)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/RequestContext.ts#L49)staticcurrentRequestContext

* ****currentRequestContext**(): undefined | [RequestContext](https://mikro-orm.io/api/core/class/RequestContext.md)

* Returns current RequestContext (if available).

  ***

  #### Returns undefined | [RequestContext](https://mikro-orm.io/api/core/class/RequestContext.md)

### [**](#enter)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/RequestContext.ts#L41)staticenter

* ****enter**(em, options): void

* Creates new RequestContext instance and runs the code inside its domain. If the handler is async, the return value needs to be awaited. Uses `AsyncLocalStorage.enterWith()`, suitable for elysia style middlewares without a `next` callback.

  ***

  #### Parameters

  * ##### em: [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>> | [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>\[]

  * ##### options: [CreateContextOptions](https://mikro-orm.io/api/core/interface/CreateContextOptions.md) = <!-- -->{}

  #### Returns void

### [**](#getEntityManager)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/RequestContext.ts#L56)staticgetEntityManager

* ****getEntityManager**(name): undefined | [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>

* Returns current EntityManager (if available).

  ***

  #### Parameters

  * ##### name: string = <!-- -->'default'

  #### Returns undefined | [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>
