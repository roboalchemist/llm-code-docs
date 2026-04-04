# Source: https://mikro-orm.io/api/core/class/ScalarReference.md

# ScalarReference<!-- --> \<Value>

## Index[**](#index)

### Constructors

* [**constructor](#constructor)

### Methods

* [**bind](#bind)
* [**isInitialized](#isinitialized)
* [**load](#load)
* [**loadOrFail](#loadorfail)
* [**set](#set)
* [**unwrap](#unwrap)

## Constructors<!-- -->[**](#constructors)

### [**](#constructor)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/Reference.ts#L242)constructor

* ****new ScalarReference**\<Value>(value, initialized): [ScalarReference](https://mikro-orm.io/api/core/class/ScalarReference.md)\<Value>

* #### Parameters

  * ##### optionalvalue: Value

  * ##### initialized: boolean = <!-- -->

  #### Returns [ScalarReference](https://mikro-orm.io/api/core/class/ScalarReference.md)\<Value>

## Methods<!-- -->[**](#methods)

### [**](#bind)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/Reference.ts#L294)bind

* ****bind**\<Entity>(entity, property): void

* #### Parameters

  * ##### entity: Entity

  * ##### property: [EntityKey](https://mikro-orm.io/api/core.md#EntityKey)\<Entity>

  #### Returns void

### [**](#isinitialized)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/Reference.ts#L304)isInitialized

* ****isInitialized**(): boolean

* #### Returns boolean

### [**](#load)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/Reference.ts#L253)load

* ****load**(options): Promise\<undefined | Value>

* Ensures the underlying entity is loaded first (without reloading it if it already is loaded). Returns either the whole entity, or the requested property.

  ***

  #### Parameters

  * ##### optionaloptions: Omit<[LoadReferenceOptions](https://mikro-orm.io/api/core/interface/LoadReferenceOptions.md)\<any, any, \*, never>, fields | exclude | populate>

  #### Returns Promise\<undefined | Value>

### [**](#loadorfail)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/Reference.ts#L274)loadOrFail

* ****loadOrFail**(options): Promise\<Value>

* Ensures the underlying entity is loaded first (without reloading it if it already is loaded). Returns the entity or throws an error just like `em.findOneOrFail()` (and respects the same config options).

  ***

  #### Parameters

  * ##### options: Omit<[LoadReferenceOrFailOptions](https://mikro-orm.io/api/core/interface/LoadReferenceOrFailOptions.md)\<any, any, \*, never>, fields | exclude | populate> = <!-- -->{}

  #### Returns Promise\<Value>

### [**](#set)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/Reference.ts#L289)set

* ****set**(value): void

* #### Parameters

  * ##### value: Value

  #### Returns void

### [**](#unwrap)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/Reference.ts#L300)unwrap

* ****unwrap**(): undefined | Value

* #### Returns undefined | Value
