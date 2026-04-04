# Source: https://mikro-orm.io/api/core/class/IdentityMap.md

# IdentityMap<!-- -->

## Index[**](#Index)

### Constructors

* [**constructor](#constructor)

### Methods

* [**\[iterator\]](#\[iterator])
* [**clear](#clear)
* [**delete](#delete)
* [**get](#get)
* [**getByHash](#getByHash)
* [**getStore](#getStore)
* [**keys](#keys)
* [**store](#store)
* [**values](#values)

## Constructors<!-- -->[**](#Constructors)

### [**](#constructor)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/unit-of-work/IdentityMap.ts#L5)constructor

* ****new IdentityMap**(defaultSchema): [IdentityMap](https://mikro-orm.io/api/core/class/IdentityMap.md)

- #### Parameters

  * ##### optionaldefaultSchema: string

  #### Returns [IdentityMap](https://mikro-orm.io/api/core/class/IdentityMap.md)

## Methods<!-- -->[**](#Methods)

### [**](#\[iterator])[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/unit-of-work/IdentityMap.ts#L49)\[iterator]

* ****\[iterator]**(): IterableIterator\<Partial\<any>, any, any>

- #### Returns IterableIterator\<Partial\<any>, any, any>

### [**](#clear)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/unit-of-work/IdentityMap.ts#L35)clear

* ****clear**(): void

- #### Returns void

### [**](#delete)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/unit-of-work/IdentityMap.ts#L13)delete

* ****delete**\<T>(item): void

- #### Parameters

  * ##### item: T

  #### Returns void

### [**](#get)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/unit-of-work/IdentityMap.ts#L70)get

* ****get**\<T>(hash): undefined | T

- For back compatibility only.

  ***

  #### Parameters

  * ##### hash: string

  #### Returns undefined | T

### [**](#getByHash)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/unit-of-work/IdentityMap.ts#L17)getByHash

* ****getByHash**\<T>(meta, hash): undefined | T

- #### Parameters

  * ##### meta: [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<T>
  * ##### hash: string

  #### Returns undefined | T

### [**](#getStore)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/unit-of-work/IdentityMap.ts#L22)getStore

* ****getStore**\<T>(meta): Map\<string, T>

- #### Parameters

  * ##### meta: [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<T>

  #### Returns Map\<string, T>

### [**](#keys)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/unit-of-work/IdentityMap.ts#L57)keys

* ****keys**(): string\[]

- #### Returns string\[]

### [**](#store)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/unit-of-work/IdentityMap.ts#L9)store

* ****store**\<T>(item): void

- #### Parameters

  * ##### item: T

  #### Returns void

### [**](#values)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/unit-of-work/IdentityMap.ts#L39)values

* ****values**(): Partial\<any>\[]

- #### Returns Partial\<any>\[]
