# Source: https://mikro-orm.io/api/seeder/class/SeedManager.md

# SeedManager<!-- -->

### Implements

* [ISeedManager](https://mikro-orm.io/api/core/interface/ISeedManager.md)

## Index[**](#index)

### Constructors

* [**constructor](#constructor)

### Methods

* [**create](#create)
* [**seed](#seed)
* [**register](#register)

## Constructors<!-- -->[**](#constructors)

### [**](#constructor)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/seeder/src/SeedManager.ts#L19)constructor

* ****new SeedManager**(em): [SeedManager](https://mikro-orm.io/api/seeder/class/SeedManager.md)

* #### Parameters

  * ##### em: [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>

  #### Returns [SeedManager](https://mikro-orm.io/api/seeder/class/SeedManager.md)

## Methods<!-- -->[**](#methods)

### [**](#create)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/seeder/src/SeedManager.ts#L140)create

* ****create**(className): Promise\<string>

* Implementation of ISeedManager.create

  #### Parameters

  * ##### className: string

  #### Returns Promise\<string>

### [**](#seed)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/seeder/src/SeedManager.ts#L78)seed

* ****seed**(...classNames): Promise\<void>

* Implementation of ISeedManager.seed

  #### Parameters

  * ##### rest...classNames: [Constructor](https://mikro-orm.io/api/core.md#Constructor)<[Seeder](https://mikro-orm.io/api/seeder/class/Seeder.md)<[Dictionary](https://mikro-orm.io/api/core.md#Dictionary)>>\[]

  #### Returns Promise\<void>

### [**](#register)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/seeder/src/SeedManager.ts#L44)staticregister

* ****register**(orm): void

* #### Parameters

  * ##### orm: [MikroORM](https://mikro-orm.io/api/core/class/MikroORM.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>, [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>, (string | [EntitySchema](https://mikro-orm.io/api/core/class/EntitySchema.md)\<any, never, [EntityCtor](https://mikro-orm.io/api/core.md#EntityCtor)\<any>> | [EntityClass](https://mikro-orm.io/api/core.md#EntityClass)\<Partial\<any>>)\[]>

  #### Returns void
