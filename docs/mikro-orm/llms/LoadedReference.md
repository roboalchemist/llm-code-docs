# Source: https://mikro-orm.io/api/core/interface/LoadedReference.md

# LoadedReference<!-- --> \<T>

### Hierarchy

* [Reference](https://mikro-orm.io/api/core/class/Reference.md)\<NonNullable\<T>>
  * *LoadedReference*

## Index[**](#Index)

### Properties

* [**$](#$)

### Methods

* [**get](#get)
* [**getEntity](#getEntity)
* [**getProperty](#getProperty)
* [**isInitialized](#isInitialized)
* [**load](#load)
* [**loadOrFail](#loadOrFail)
* [**loadProperty](#loadProperty)
* [**populated](#populated)
* [**toJSON](#toJSON)
* [**unwrap](#unwrap)

## Properties<!-- -->[**](#Properties)

### [**](#$)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L1264)$

**$: NonNullable\<T>

## Methods<!-- -->[**](#Methods)

### [**](#get)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/typings.ts#L1265)get

* ****get**(): NonNullable\<T>

- #### Returns NonNullable\<T>

### [**](#getEntity)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/Reference.ts#L169)inheritedgetEntity

* ****getEntity**(): NonNullable\<T>

- Inherited from Reference.getEntity

  #### Returns NonNullable\<T>

### [**](#getProperty)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/Reference.ts#L177)inheritedgetProperty

* ****getProperty**\<K>(prop): NonNullable\<T>\[K]

- Inherited from Reference.getProperty

  #### Parameters

  * ##### prop: K

  #### Returns NonNullable\<T>\[K]

### [**](#isInitialized)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/Reference.ts#L186)inheritedisInitialized

* ****isInitialized**(): boolean

- Inherited from Reference.isInitialized

  #### Returns boolean

### [**](#load)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/Reference.ts#L117)inheritedload

* ****load**\<TT, P, F, E>(options): Promise\<null | [Loaded](https://mikro-orm.io/api/core.md#Loaded)\<TT, P, F, E>>

- Inherited from Reference.load

  Ensures the underlying entity is loaded first (without reloading it if it already is loaded). Returns the entity. If the entity is not found in the database (e.g. it was deleted in the meantime, or currently active filters disallow loading of it) the method returns `null`. Use `loadOrFail()` if you want an error to be thrown in such a case.

  ***

  #### Parameters

  * ##### options: [LoadReferenceOptions](https://mikro-orm.io/api/core/interface/LoadReferenceOptions.md)\<TT, P, F, E> = <!-- -->{}

  #### Returns Promise\<null | [Loaded](https://mikro-orm.io/api/core.md#Loaded)\<TT, P, F, E>>

### [**](#loadOrFail)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/Reference.ts#L146)inheritedloadOrFail

* ****loadOrFail**\<TT, P, F, E>(options): Promise<[Loaded](https://mikro-orm.io/api/core.md#Loaded)\<TT, P, F, E>>

- Inherited from Reference.loadOrFail

  Ensures the underlying entity is loaded first (without reloading it if it already is loaded). Returns the entity or throws an error just like `em.findOneOrFail()` (and respects the same config options).

  ***

  #### Parameters

  * ##### options: [LoadReferenceOrFailOptions](https://mikro-orm.io/api/core/interface/LoadReferenceOrFailOptions.md)\<TT, P, F, E> = <!-- -->{}

  #### Returns Promise<[Loaded](https://mikro-orm.io/api/core.md#Loaded)\<TT, P, F, E>>

### [**](#loadProperty)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/Reference.ts#L181)inheritedloadProperty

* ****loadProperty**\<TT, P, K>(prop, options): Promise<[Loaded](https://mikro-orm.io/api/core.md#Loaded)\<TT, P>\[K]>

- Inherited from Reference.loadProperty

  #### Parameters

  * ##### prop: K
  * ##### optionaloptions: [LoadReferenceOrFailOptions](https://mikro-orm.io/api/core/interface/LoadReferenceOrFailOptions.md)\<TT, P, \*, never>

  #### Returns Promise<[Loaded](https://mikro-orm.io/api/core.md#Loaded)\<TT, P>\[K]>

### [**](#populated)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/Reference.ts#L190)inheritedpopulated

* ****populated**(populated): void

- Inherited from Reference.populated

  #### Parameters

  * ##### optionalpopulated: boolean

  #### Returns void

### [**](#toJSON)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/Reference.ts#L194)inheritedtoJSON

* ****toJSON**(...args): [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)

- Inherited from Reference.toJSON

  #### Parameters

  * ##### rest...args: any\[]

  #### Returns [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)

### [**](#unwrap)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/entity/Reference.ts#L165)inheritedunwrap

* ****unwrap**(): NonNullable\<T>

- Inherited from Reference.unwrap

  #### Returns NonNullable\<T>
