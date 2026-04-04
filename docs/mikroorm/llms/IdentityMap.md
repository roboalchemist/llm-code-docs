# Source: https://mikro-orm.io/api/core/class/IdentityMap.md

# IdentityMap<!-- -->

## Index[**](#index)

### Constructors

* [**constructor](#constructor)

### Methods

* [**\[iterator\]](#\[iterator])
* [**clear](#clear)
* [**delete](#delete)
* [**get](#get)
* [**getByHash](#getbyhash)
* [**getKeyHash](#getkeyhash)
* [**getStore](#getstore)
* [**keys](#keys)
* [**store](#store)
* [**storeByKey](#storebykey)
* [**values](#values)

## Constructors<!-- -->[**](#constructors)

### [**](#constructor)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/unit-of-work/IdentityMap.ts#L9)constructor

* ****new IdentityMap**(defaultSchema): [IdentityMap](https://mikro-orm.io/api/core/class/IdentityMap.md)

* #### Parameters

  * ##### optionaldefaultSchema: string

  #### Returns [IdentityMap](https://mikro-orm.io/api/core/class/IdentityMap.md)

## Methods<!-- -->[**](#methods)

### [**](#\[iterator])[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/unit-of-work/IdentityMap.ts#L84)\[iterator]

* ****\[iterator]**(): IterableIterator\<Partial\<any>, any, any>

* #### Returns IterableIterator\<Partial\<any>, any, any>

### [**](#clear)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/unit-of-work/IdentityMap.ts#L70)clear

* ****clear**(): void

* #### Returns void

### [**](#delete)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/unit-of-work/IdentityMap.ts#L35)delete

* ****delete**\<T>(item): void

* #### Parameters

  * ##### item: T

  #### Returns void

### [**](#get)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/unit-of-work/IdentityMap.ts#L105)get

* ****get**\<T>(hash): undefined | T

* For back compatibility only.

  ***

  #### Parameters

  * ##### hash: string

  #### Returns undefined | T

### [**](#getbyhash)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/unit-of-work/IdentityMap.ts#L52)getByHash

* ****getByHash**\<T>(meta, hash): undefined | T

* #### Parameters

  * ##### meta: [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<T, [EntityCtor](https://mikro-orm.io/api/core.md#EntityCtor)\<T>>

  * ##### hash: string

  #### Returns undefined | T

### [**](#getkeyhash)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/unit-of-work/IdentityMap.ts#L134)getKeyHash

* ****getKeyHash**(key, value, schema): string

* Creates a hash for an alternate key lookup. Format: `[key]value` or `schema:[key]value`

  ***

  #### Parameters

  * ##### key: string

  * ##### value: string

  * ##### optionalschema: string

  #### Returns string

### [**](#getstore)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/unit-of-work/IdentityMap.ts#L57)getStore

* ****getStore**\<T>(meta): Map\<string, T>

* #### Parameters

  * ##### meta: [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<T, [EntityCtor](https://mikro-orm.io/api/core.md#EntityCtor)\<T>>

  #### Returns Map\<string, T>

### [**](#keys)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/unit-of-work/IdentityMap.ts#L92)keys

* ****keys**(): string\[]

* #### Returns string\[]

### [**](#store)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/unit-of-work/IdentityMap.ts#L13)store

* ****store**\<T>(item): void

* #### Parameters

  * ##### item: T

  #### Returns void

### [**](#storebykey)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/unit-of-work/IdentityMap.ts#L21)storeByKey

* ****storeByKey**\<T>(item, key, value, schema): void

* Stores an entity under an alternate key (non-PK property). This allows looking up entities by unique properties that are not the primary key.

  ***

  #### Parameters

  * ##### item: T

  * ##### key: string

  * ##### value: string

  * ##### optionalschema: string

  #### Returns void

### [**](#values)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/unit-of-work/IdentityMap.ts#L74)values

* ****values**(): Partial\<any>\[]

* #### Returns Partial\<any>\[]
