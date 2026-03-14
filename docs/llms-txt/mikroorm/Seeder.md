# Source: https://mikro-orm.io/api/seeder/class/Seeder.md

# abstractSeeder<!-- --> \<T>

## Index[**](#index)

### Constructors

* [**constructor](#constructor)

### Methods

* [**run](#run)

## Constructors<!-- -->[**](#constructors)

### [**](#constructor)constructor

* ****new Seeder**\<T>(): [Seeder](https://mikro-orm.io/api/seeder/class/Seeder.md)\<T>

* #### Returns [Seeder](https://mikro-orm.io/api/seeder/class/Seeder.md)\<T>

## Methods<!-- -->[**](#methods)

### [**](#run)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/seeder/src/Seeder.ts#L4)abstractrun

* ****run**(em, context): void | Promise\<void>

* #### Parameters

  * ##### em: [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>

  * ##### optionalcontext: T

  #### Returns void | Promise\<void>
