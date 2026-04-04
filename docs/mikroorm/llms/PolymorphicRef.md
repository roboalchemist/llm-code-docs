# Source: https://mikro-orm.io/api/core/class/PolymorphicRef.md

# PolymorphicRef<!-- -->

Wrapper class for polymorphic relation reference data. Holds the discriminator value (type identifier) and the primary key value(s). Used internally to track polymorphic FK values before hydration.

## Index[**](#index)

### Constructors

* [**constructor](#constructor)

### Properties

* [**discriminator](#discriminator)
* [**id](#id)

### Methods

* [**toTuple](#totuple)

## Constructors<!-- -->[**](#constructors)

### [**](#constructor)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/PolymorphicRef.ts#L9)constructor

* ****new PolymorphicRef**(discriminator, id): [PolymorphicRef](https://mikro-orm.io/api/core/class/PolymorphicRef.md)

* #### Parameters

  * ##### discriminator: string

  * ##### id: unknown

  #### Returns [PolymorphicRef](https://mikro-orm.io/api/core/class/PolymorphicRef.md)

## Properties<!-- -->[**](#properties)

### [**](#discriminator)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/PolymorphicRef.ts#L10)publicreadonlydiscriminator

**discriminator: string

### [**](#id)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/PolymorphicRef.ts#L11)publicid

**id: unknown

## Methods<!-- -->[**](#methods)

### [**](#totuple)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/PolymorphicRef.ts#L15)toTuple

* ****toTuple**(): unknown\[]

* Returns `[discriminator, ...idValues]` tuple suitable for column-level expansion.

  ***

  #### Returns unknown\[]
