# Source: https://mikro-orm.io/api/seeder/class/SeedManager.md

# SeedManager<!-- -->

### Implements

* [ISeedManager](https://mikro-orm.io/api/core/interface/ISeedManager.md)

## Index[**](#Index)

### Constructors

* [**constructor](#constructor)

### Methods

* [**createSeeder](#createSeeder)
* [**seed](#seed)
* [**register](#register)

## Constructors<!-- -->[**](#Constructors)

### [**](#constructor)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/seeder/src/SeedManager.ts#L20)constructor

* ****new SeedManager**(em): [SeedManager](https://mikro-orm.io/api/seeder/class/SeedManager.md)

- #### Parameters

  * ##### em: [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>

  #### Returns [SeedManager](https://mikro-orm.io/api/seeder/class/SeedManager.md)

## Methods<!-- -->[**](#Methods)

### [**](#createSeeder)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/seeder/src/SeedManager.ts#L70)createSeeder

* ****createSeeder**(className): Promise\<string>

- Implementation of ISeedManager.createSeeder

  #### Parameters

  * ##### className: string

  #### Returns Promise\<string>

### [**](#seed)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/seeder/src/SeedManager.ts#L34)seed

* ****seed**(...classNames): Promise\<void>

- Implementation of ISeedManager.seed

  #### Parameters

  * ##### rest...classNames: [Constructor](https://mikro-orm.io/api/core.md#Constructor)<[Seeder](https://mikro-orm.io/api/seeder/class/Seeder.md)<[Dictionary](https://mikro-orm.io/api/core.md#Dictionary)>>\[]

  #### Returns Promise\<void>

### [**](#register)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/seeder/src/SeedManager.ts#L30)staticregister

* ****register**(orm): void

- #### Parameters

  * ##### orm: [MikroORM](https://mikro-orm.io/api/core/class/MikroORM.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>, [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>>

  #### Returns void
