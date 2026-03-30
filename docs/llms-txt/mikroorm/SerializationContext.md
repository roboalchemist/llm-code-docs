# Source: https://mikro-orm.io/api/core/class/SerializationContext.md

# SerializationContext<!-- --> \<T>

Helper that allows to keep track of where we are currently at when serializing complex entity graph with cycles. Before we process a property, we call `visit` that checks if it is not a cycle path (but allows to pass cycles that are defined in populate hint). If not, we proceed and call `leave` afterwards.

## Index[**](#index)

### Constructors

* [**constructor](#constructor)

### Properties

* [**path](#path)
* [**visited](#visited)

### Methods

* [**close](#close)
* [**isExcluded](#isexcluded)
* [**isMarkedAsPopulated](#ismarkedaspopulated)
* [**isPartiallyLoaded](#ispartiallyloaded)
* [**leave](#leave)
* [**visit](#visit)
* [**propagate](#propagate)

## Constructors<!-- -->[**](#constructors)

### [**](#constructor)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/serialization/SerializationContext.ts#L18)constructor

* ****new SerializationContext**\<T>(populate, fields, exclude): [SerializationContext](https://mikro-orm.io/api/core/class/SerializationContext.md)\<T>

* #### Parameters

  * ##### populate: [PopulateOptions](https://mikro-orm.io/api/core.md#PopulateOptions)\<T>\[] = <!-- -->\[]

  * ##### optionalfields: Set\<string>

  * ##### optionalexclude: readonly<!-- --> string\[]

  #### Returns [SerializationContext](https://mikro-orm.io/api/core/class/SerializationContext.md)\<T>

## Properties<!-- -->[**](#properties)

### [**](#path)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/serialization/SerializationContext.ts#L11)readonlypath

**path: \[[EntityName](https://mikro-orm.io/api/core.md#EntityName), string]\[] =

<!-- -->

\[]

### [**](#visited)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/serialization/SerializationContext.ts#L12)readonlyvisited

**visited: Set\<Partial\<any>> =

<!-- -->

...

## Methods<!-- -->[**](#methods)

### [**](#close)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/serialization/SerializationContext.ts#L51)close

* ****close**(): void

* #### Returns void

### [**](#isexcluded)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/serialization/SerializationContext.ts#L120)isExcluded

* ****isExcluded**(entityName, prop): boolean

* #### Parameters

  * ##### entityName: [EntityName](https://mikro-orm.io/api/core.md#EntityName)

  * ##### prop: string

  #### Returns boolean

### [**](#ismarkedaspopulated)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/serialization/SerializationContext.ts#L93)isMarkedAsPopulated

* ****isMarkedAsPopulated**(entityName, prop): boolean

* #### Parameters

  * ##### entityName: [EntityName](https://mikro-orm.io/api/core.md#EntityName)

  * ##### prop: string

  #### Returns boolean

### [**](#ispartiallyloaded)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/serialization/SerializationContext.ts#L130)isPartiallyLoaded

* ****isPartiallyLoaded**(entityName, prop): boolean

* #### Parameters

  * ##### entityName: [EntityName](https://mikro-orm.io/api/core.md#EntityName)

  * ##### prop: string

  #### Returns boolean

### [**](#leave)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/serialization/SerializationContext.ts#L42)leave

* ****leave**(entityName, prop): void

* #### Parameters

  * ##### entityName: [EntityName](https://mikro-orm.io/api/core.md#EntityName)

  * ##### prop: string

  #### Returns void

### [**](#visit)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/serialization/SerializationContext.ts#L27)visit

* ****visit**(entityName, prop): boolean

* Returns true when there is a cycle detected.

  ***

  #### Parameters

  * ##### entityName: [EntityName](https://mikro-orm.io/api/core.md#EntityName)

  * ##### prop: string

  #### Returns boolean

### [**](#propagate)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/serialization/SerializationContext.ts#L60)staticpropagate

* ****propagate**(root, entity, isVisible): void

* When initializing new context, we need to propagate it to the whole entity graph recursively.

  ***

  #### Parameters

  * ##### root: [SerializationContext](https://mikro-orm.io/api/core/class/SerializationContext.md)\<any>

  * ##### entity: Partial\<any>

  * ##### isVisible: (meta, prop) => boolean

  #### Returns void
