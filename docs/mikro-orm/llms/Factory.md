# Source: https://mikro-orm.io/api/seeder/class/Factory.md

# abstractFactory<!-- --> \<TEntity, TInput>

## Index[**](#Index)

### Constructors

* [**constructor](#constructor)

### Properties

* [**model](#model)

### Methods

* [**create](#create)
* [**createOne](#createOne)
* [**each](#each)
* [**make](#make)
* [**makeEntity](#makeEntity)
* [**makeOne](#makeOne)

## Constructors<!-- -->[**](#Constructors)

### [**](#constructor)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/seeder/src/Factory.ts#L13)constructor

* ****new Factory**\<TEntity, TInput>(em): [Factory](https://mikro-orm.io/api/seeder/class/Factory.md)\<TEntity, TInput>

- #### Parameters

  * ##### em: [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>

  #### Returns [Factory](https://mikro-orm.io/api/seeder/class/Factory.md)\<TEntity, TInput>

## Properties<!-- -->[**](#Properties)

### [**](#model)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/seeder/src/Factory.ts#L10)abstractreadonlymodel

**model: [Constructor](https://mikro-orm.io/api/core.md#Constructor)\<TEntity>

## Methods<!-- -->[**](#Methods)

### [**](#create)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/seeder/src/Factory.ts#L78)create

* ****create**(amount, input): Promise\<TEntity\[]>

- Create (and flush) multiple entities

  ***

  #### Parameters

  * ##### amount: number

    Number of entities that should be generated

  * ##### optionalinput: TInput

    Object specifying what default attributes of the entity factory should be overridden

  #### Returns Promise\<TEntity\[]>

### [**](#createOne)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/seeder/src/Factory.ts#L67)createOne

* ****createOne**(input): Promise\<TEntity>

- Create (and flush) a single entity

  ***

  #### Parameters

  * ##### optionalinput: TInput

    Object specifying what default attributes of the entity factory should be overridden

  #### Returns Promise\<TEntity>

### [**](#each)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/seeder/src/Factory.ts#L89)each

* ****each**(eachFunction): [Factory](https://mikro-orm.io/api/seeder/class/Factory.md)\<TEntity, TInput>

- Set a function that is applied to each entity before it is returned In case of `createOne` or `create` it is applied before the entity is persisted

  ***

  #### Parameters

  * ##### eachFunction: (entity, index) => void

    The function that is applied on every entity



  #### Returns [Factory](https://mikro-orm.io/api/seeder/class/Factory.md)\<TEntity, TInput>

### [**](#make)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/seeder/src/Factory.ts#L55)make

* ****make**(amount, input): TEntity\[]

- Make multiple entities and then persist them (not flush)

  ***

  #### Parameters

  * ##### amount: number

    Number of entities that should be generated

  * ##### optionalinput: TInput

    Object specifying what default attributes of the entity factory should be overridden

  #### Returns TEntity\[]

### [**](#makeEntity)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/seeder/src/Factory.ts#L21)makeEntity

* ****makeEntity**(input, index): TEntity

- Make a single entity instance, without persisting it.

  ***

  #### Parameters

  * ##### optionalinput: TInput

    Object specifying what default attributes of the entity factory should be overridden

  * ##### index: number = <!-- -->0

  #### Returns TEntity

### [**](#makeOne)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/seeder/src/Factory.ts#L44)makeOne

* ****makeOne**(input): TEntity

- Make a single entity and persist (not flush)

  ***

  #### Parameters

  * ##### optionalinput: TInput

    Object specifying what default attributes of the entity factory should be overridden

  #### Returns TEntity
