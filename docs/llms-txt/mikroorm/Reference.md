# Source: https://mikro-orm.io/api/core/class/Reference.md

# Reference<!-- --> \<T>

### Hierarchy

* *Reference*
  * [LoadedReference](https://mikro-orm.io/api/core/interface/LoadedReference.md)

## Index[**](#index)

### Constructors

* [**constructor](#constructor)

### Methods

* [**getEntity](#getentity)
* [**getProperty](#getproperty)
* [**isInitialized](#isinitialized)
* [**load](#load)
* [**loadOrFail](#loadorfail)
* [**loadProperty](#loadproperty)
* [**populated](#populated)
* [**toJSON](#tojson)
* [**unwrap](#unwrap)
* [**create](#create)
* [**createFromPK](#createFromPK)
* [**createNakedFromPK](#createNakedFromPK)
* [**isReference](#isReference)
* [**unwrapReference](#unwrapReference)
* [**wrapReference](#wrapReference)

## Constructors<!-- -->[**](#constructors)

### [**](#constructor)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/Reference.ts#L25)constructor

* ****new Reference**\<T>(entity): [Reference](https://mikro-orm.io/api/core/class/Reference.md)\<T>

* #### Parameters

  * ##### entity: T

  #### Returns [Reference](https://mikro-orm.io/api/core/class/Reference.md)\<T>

## Methods<!-- -->[**](#methods)

### [**](#getentity)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/Reference.ts#L187)getEntity

* ****getEntity**(): T

* #### Returns T

### [**](#getproperty)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/Reference.ts#L197)getProperty

* ****getProperty**\<K>(prop): T\[K]

* #### Parameters

  * ##### prop: K

  #### Returns T\[K]

### [**](#isinitialized)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/Reference.ts#L209)isInitialized

* ****isInitialized**(): boolean

* #### Returns boolean

### [**](#load)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/Reference.ts#L128)load

* ****load**\<TT, P, F, E>(options): Promise\<null | [Loaded](https://mikro-orm.io/api/core.md#Loaded)\<TT, P, F, E>>

* Ensures the underlying entity is loaded first (without reloading it if it already is loaded). Returns the entity. If the entity is not found in the database (e.g. it was deleted in the meantime, or currently active filters disallow loading of it) the method returns `null`. Use `loadOrFail()` if you want an error to be thrown in such a case.

  ***

  #### Parameters

  * ##### options: [LoadReferenceOptions](https://mikro-orm.io/api/core/interface/LoadReferenceOptions.md)\<TT, P, F, E> = <!-- -->{}

  #### Returns Promise\<null | [Loaded](https://mikro-orm.io/api/core.md#Loaded)\<TT, P, F, E>>

### [**](#loadorfail)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/Reference.ts#L162)loadOrFail

* ****loadOrFail**\<TT, P, F, E>(options): Promise<[Loaded](https://mikro-orm.io/api/core.md#Loaded)\<TT, P, F, E>>

* Ensures the underlying entity is loaded first (without reloading it if it already is loaded). Returns the entity or throws an error just like `em.findOneOrFail()` (and respects the same config options).

  ***

  #### Parameters

  * ##### options: [LoadReferenceOrFailOptions](https://mikro-orm.io/api/core/interface/LoadReferenceOrFailOptions.md)\<TT, P, F, E> = <!-- -->{}

  #### Returns Promise<[Loaded](https://mikro-orm.io/api/core.md#Loaded)\<TT, P, F, E>>

### [**](#loadproperty)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/Reference.ts#L201)loadProperty

* ****loadProperty**\<TT, P, K>(prop, options): Promise<[Loaded](https://mikro-orm.io/api/core.md#Loaded)\<TT, P>\[K]>

* #### Parameters

  * ##### prop: K

  * ##### optionaloptions: [LoadReferenceOrFailOptions](https://mikro-orm.io/api/core/interface/LoadReferenceOrFailOptions.md)\<TT, P, \*, never>

  #### Returns Promise<[Loaded](https://mikro-orm.io/api/core.md#Loaded)\<TT, P>\[K]>

### [**](#populated)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/Reference.ts#L213)populated

* ****populated**(populated): void

* #### Parameters

  * ##### optionalpopulated: boolean

  #### Returns void

### [**](#tojson)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/Reference.ts#L217)toJSON

* ****toJSON**(...args): [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)

* #### Parameters

  * ##### rest...args: any\[]

  #### Returns [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)

### [**](#unwrap)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/Reference.ts#L183)unwrap

* ****unwrap**(): T

* #### Returns T

### [**](#create)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/Reference.ts#L46)staticcreate

* ****create**\<T>(entity): [Ref](https://mikro-orm.io/api/core.md#Ref)\<T>

* #### Parameters

  * ##### entity: T | [Ref](https://mikro-orm.io/api/core.md#Ref)\<T>

  #### Returns [Ref](https://mikro-orm.io/api/core.md#Ref)\<T>

### [**](#createFromPK)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/Reference.ts#L57)staticcreateFromPK

* ****createFromPK**\<T>(entityType, pk, options): [Ref](https://mikro-orm.io/api/core.md#Ref)\<T>

* #### Parameters

  * ##### entityType: [EntityClass](https://mikro-orm.io/api/core.md#EntityClass)\<T>

  * ##### pk: T extends { \[PrimaryKeyProp]?<!-- -->: PK } ? PK extends undefined ? Omit\<T\<T>, typeof [PrimaryKeyProp](https://mikro-orm.io/api/core.md#PrimaryKeyProp)> : PK extends keyof<!-- --> T\<T> ? ReadonlyPrimary\<UnwrapPrimary\<T\<T>\[PK\<PK>]>> : PK extends keyof<!-- --> T\<T>\[] ? ReadonlyPrimary\<PrimaryPropToType\<T\<T>, PK\<PK>>> : PK : T extends { \_id?<!-- -->: PK } ? string | ReadonlyPrimary\<PK> : T extends { id?<!-- -->: PK } ? ReadonlyPrimary\<PK> : T extends { uuid?<!-- -->: PK } ? ReadonlyPrimary\<PK> : T

  * ##### optionaloptions: { schema?<!-- -->: string }

    * ##### optionalschema: string

  #### Returns [Ref](https://mikro-orm.io/api/core.md#Ref)\<T>

### [**](#createNakedFromPK)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/Reference.ts#L66)staticcreateNakedFromPK

* ****createNakedFromPK**\<T>(entityType, pk, options): T

* #### Parameters

  * ##### entityType: [EntityClass](https://mikro-orm.io/api/core.md#EntityClass)\<T>

  * ##### pk: T extends { \[PrimaryKeyProp]?<!-- -->: PK } ? PK extends undefined ? Omit\<T\<T>, typeof [PrimaryKeyProp](https://mikro-orm.io/api/core.md#PrimaryKeyProp)> : PK extends keyof<!-- --> T\<T> ? ReadonlyPrimary\<UnwrapPrimary\<T\<T>\[PK\<PK>]>> : PK extends keyof<!-- --> T\<T>\[] ? ReadonlyPrimary\<PrimaryPropToType\<T\<T>, PK\<PK>>> : PK : T extends { \_id?<!-- -->: PK } ? string | ReadonlyPrimary\<PK> : T extends { id?<!-- -->: PK } ? ReadonlyPrimary\<PK> : T extends { uuid?<!-- -->: PK } ? ReadonlyPrimary\<PK> : T

  * ##### optionaloptions: { schema?<!-- -->: string }

    * ##### optionalschema: string

  #### Returns T

### [**](#isReference)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/Reference.ts#L95)staticisReference

* ****isReference**\<T>(data): data is [Reference](https://mikro-orm.io/api/core/class/Reference.md)\<T>

* Checks whether the argument is instance of `Reference` wrapper.

  ***

  #### Parameters

  * ##### data: any

  #### Returns data is [Reference](https://mikro-orm.io/api/core/class/Reference.md)\<T>

### [**](#unwrapReference)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/Reference.ts#L119)staticunwrapReference

* ****unwrapReference**\<T>(ref): T

* Returns wrapped entity.

  ***

  #### Parameters

  * ##### ref: T | [Reference](https://mikro-orm.io/api/core/class/Reference.md)\<T> | [ScalarReference](https://mikro-orm.io/api/core/class/ScalarReference.md)\<T> | [Ref](https://mikro-orm.io/api/core.md#Ref)\<T>

  #### Returns T

### [**](#wrapReference)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/entity/Reference.ts#L102)staticwrapReference

* ****wrapReference**\<T, O>(entity, prop): T | [Reference](https://mikro-orm.io/api/core/class/Reference.md)\<T>

* Wraps the entity in a `Reference` wrapper if the property is defined as `ref`.

  ***

  #### Parameters

  * ##### entity: T | [Reference](https://mikro-orm.io/api/core/class/Reference.md)\<T>

  * ##### prop: [EntityProperty](https://mikro-orm.io/api/core/interface/EntityProperty.md)\<O, T>

  #### Returns T | [Reference](https://mikro-orm.io/api/core/class/Reference.md)\<T>
