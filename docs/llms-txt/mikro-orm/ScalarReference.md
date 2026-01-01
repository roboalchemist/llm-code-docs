# Source: https://mikro-orm.io/api/core/class/ScalarReference.md

# ScalarReference<!-- --> \<Value>

## Index[**](#Index)

### Constructors

* [**constructor](#constructor)

### Methods

* [**bind](#bind)
* [**isInitialized](#isInitialized)
* [**load](#load)
* [**loadOrFail](#loadOrFail)
* [**set](#set)
* [**unwrap](#unwrap)

## Constructors<!-- -->[**](#Constructors)

### [**](#constructor)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/Reference.ts#L220)constructor

* ****new ScalarReference**\<Value>(value, initialized): [ScalarReference](https://mikro-orm.io/api/core/class/ScalarReference.md)\<Value>

- #### Parameters

  * ##### optionalvalue: Value
  * ##### initialized: boolean = <!-- -->...

  #### Returns [ScalarReference](https://mikro-orm.io/api/core/class/ScalarReference.md)\<Value>

## Methods<!-- -->[**](#Methods)

### [**](#bind)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/Reference.ts#L264)bind

* ****bind**\<Entity>(entity, property): void

- #### Parameters

  * ##### entity: Entity
  * ##### property: [EntityKey](https://mikro-orm.io/api/core.md#EntityKey)\<Entity>

  #### Returns void

### [**](#isInitialized)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/Reference.ts#L274)isInitialized

* ****isInitialized**(): boolean

- #### Returns boolean

### [**](#load)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/Reference.ts#L226)load

* ****load**(options): Promise\<undefined | Value>

- Ensures the underlying entity is loaded first (without reloading it if it already is loaded). Returns either the whole entity, or the requested property.

  ***

  #### Parameters

  * ##### optionaloptions: Omit<[LoadReferenceOptions](https://mikro-orm.io/api/core/interface/LoadReferenceOptions.md)\<any, any, \*, never>, populate | fields | exclude>

  #### Returns Promise\<undefined | Value>

### [**](#loadOrFail)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/Reference.ts#L244)loadOrFail

* ****loadOrFail**(options): Promise\<Value>

- Ensures the underlying entity is loaded first (without reloading it if it already is loaded). Returns the entity or throws an error just like `em.findOneOrFail()` (and respects the same config options).

  ***

  #### Parameters

  * ##### options: Omit<[LoadReferenceOrFailOptions](https://mikro-orm.io/api/core/interface/LoadReferenceOrFailOptions.md)\<any, any, \*, never>, populate | fields | exclude> = <!-- -->{}

  #### Returns Promise\<Value>

### [**](#set)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/Reference.ts#L259)set

* ****set**(value): void

- #### Parameters

  * ##### value: Value

  #### Returns void

### [**](#unwrap)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/Reference.ts#L270)unwrap

* ****unwrap**(): undefined | Value

- #### Returns undefined | Value
