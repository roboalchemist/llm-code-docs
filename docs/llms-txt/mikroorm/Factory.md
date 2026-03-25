# Source: https://mikro-orm.io/api/seeder/class/Factory.md

# abstractFactory<!-- --> \<TEntity, TInput>

## Index[**](#index)

### Constructors

* [**constructor](#constructor)

### Properties

* [**model](#model)

### Methods

* [**create](#create)
* [**createOne](#createone)
* [**each](#each)
* [**make](#make)
* [**makeEntity](#makeentity)
* [**makeOne](#makeone)

## Constructors<!-- -->[**](#constructors)

### [**](#constructor)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/seeder/src/Factory.ts#L7)constructor

* ****new Factory**\<TEntity, TInput>(em): [Factory](https://mikro-orm.io/api/seeder/class/Factory.md)\<TEntity, TInput>

* #### Parameters

  * ##### em: [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>

  #### Returns [Factory](https://mikro-orm.io/api/seeder/class/Factory.md)\<TEntity, TInput>

## Properties<!-- -->[**](#properties)

### [**](#model)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/seeder/src/Factory.ts#L4)abstractreadonlymodel

**model: [Constructor](https://mikro-orm.io/api/core.md#Constructor)\<TEntity>

## Methods<!-- -->[**](#methods)

### [**](#create)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/seeder/src/Factory.ts#L68)create

* ****create**(amount, input): Promise\<TEntity\[]>

* Create (and flush) multiple entities

  ***

  #### Parameters

  * ##### amount: number

    Number of entities that should be generated

  * ##### optionalinput: TInput

    Object specifying what default attributes of the entity factory should be overridden

  #### Returns Promise\<TEntity\[]>

### [**](#createone)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/seeder/src/Factory.ts#L57)createOne

* ****createOne**(input): Promise\<TEntity>

* Create (and flush) a single entity

  ***

  #### Parameters

  * ##### optionalinput: TInput

    Object specifying what default attributes of the entity factory should be overridden

  #### Returns Promise\<TEntity>

### [**](#each)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/seeder/src/Factory.ts#L79)each

* ****each**(eachFunction): this

* Set a function that is applied to each entity before it is returned In case of `createOne` or `create` it is applied before the entity is persisted

  ***

  #### Parameters

  * ##### eachFunction: (entity, index) => void

    The function that is applied on every entity

  #### Returns this

### [**](#make)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/seeder/src/Factory.ts#L45)make

* ****make**(amount, input): TEntity\[]

* Make multiple entities and then persist them (not flush)

  ***

  #### Parameters

  * ##### amount: number

    Number of entities that should be generated

  * ##### optionalinput: TInput

    Object specifying what default attributes of the entity factory should be overridden

  #### Returns TEntity\[]

### [**](#makeentity)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/seeder/src/Factory.ts#L15)makeEntity

* ****makeEntity**(input, index): TEntity

* Make a single entity instance, without persisting it.

  ***

  #### Parameters

  * ##### optionalinput: TInput

    Object specifying what default attributes of the entity factory should be overridden

  * ##### index: number = <!-- -->0

  #### Returns TEntity

### [**](#makeone)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/seeder/src/Factory.ts#L34)makeOne

* ****makeOne**(input): TEntity

* Make a single entity and persist (not flush)

  ***

  #### Parameters

  * ##### optionalinput: TInput

    Object specifying what default attributes of the entity factory should be overridden

  #### Returns TEntity
