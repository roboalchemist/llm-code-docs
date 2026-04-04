# Source: https://mikro-orm.io/api/core/class/SerializationContext.md

# SerializationContext<!-- --> \<T>

Helper that allows to keep track of where we are currently at when serializing complex entity graph with cycles. Before we process a property, we call `visit` that checks if it is not a cycle path (but allows to pass cycles that are defined in populate hint). If not, we proceed and call `leave` afterwards.

## Index[**](#Index)

### Constructors

* [**constructor](#constructor)

### Properties

* [**path](#path)
* [**visited](#visited)

### Methods

* [**close](#close)
* [**isMarkedAsPopulated](#isMarkedAsPopulated)
* [**isPartiallyLoaded](#isPartiallyLoaded)
* [**leave](#leave)
* [**visit](#visit)
* [**propagate](#propagate)

## Constructors<!-- -->[**](#Constructors)

### [**](#constructor)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/serialization/SerializationContext.ts#L17)constructor

* ****new SerializationContext**\<T>(config, populate, fields, exclude): [SerializationContext](https://mikro-orm.io/api/core/class/SerializationContext.md)\<T>

- #### Parameters

  * ##### config: [Configuration](https://mikro-orm.io/api/core/class/Configuration.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>, [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>>
  * ##### populate: [PopulateOptions](https://mikro-orm.io/api/core.md#PopulateOptions)\<T>\[] = <!-- -->\[]
  * ##### optionalfields: Set\<string>
  * ##### optionalexclude: string\[]

  #### Returns [SerializationContext](https://mikro-orm.io/api/core/class/SerializationContext.md)\<T>

## Properties<!-- -->[**](#Properties)

### [**](#path)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/serialization/SerializationContext.ts#L13)readonlypath

**path: \[string, string]\[] =

<!-- -->

\[]

### [**](#visited)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/serialization/SerializationContext.ts#L14)readonlyvisited

**visited: Set\<Partial\<any>> =

<!-- -->

...

## Methods<!-- -->[**](#Methods)

### [**](#close)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/serialization/SerializationContext.ts#L49)close

* ****close**(): void

- #### Returns void

### [**](#isMarkedAsPopulated)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/serialization/SerializationContext.ts#L87)isMarkedAsPopulated

* ****isMarkedAsPopulated**(entityName, prop): boolean

- #### Parameters

  * ##### entityName: string
  * ##### prop: string

  #### Returns boolean

### [**](#isPartiallyLoaded)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/serialization/SerializationContext.ts#L114)isPartiallyLoaded

* ****isPartiallyLoaded**(entityName, prop): boolean

- #### Parameters

  * ##### entityName: string
  * ##### prop: string

  #### Returns boolean

### [**](#leave)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/serialization/SerializationContext.ts#L40)leave

* ****leave**\<U>(entityName, prop): void

- #### Parameters

  * ##### entityName: string
  * ##### prop: string

  #### Returns void

### [**](#visit)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/serialization/SerializationContext.ts#L25)visit

* ****visit**(entityName, prop): boolean

- Returns true when there is a cycle detected.

  ***

  #### Parameters

  * ##### entityName: string
  * ##### prop: string

  #### Returns boolean

### [**](#propagate)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/serialization/SerializationContext.ts#L58)staticpropagate

* ****propagate**(root, entity, isVisible): void

- When initializing new context, we need to propagate it to the whole entity graph recursively.

  ***

  #### Parameters

  * ##### root: [SerializationContext](https://mikro-orm.io/api/core/class/SerializationContext.md)\<any>
  * ##### entity: Partial\<any>
  * ##### isVisible: (meta, prop) => boolean


  #### Returns void
