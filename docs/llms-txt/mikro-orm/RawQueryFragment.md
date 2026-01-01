# Source: https://mikro-orm.io/api/core/class/RawQueryFragment.md

# RawQueryFragment<!-- -->

## Index[**](#Index)

### Constructors

* [**constructor](#constructor)

### Properties

* [**params](#params)
* [**sql](#sql)
* [**cloneRegistry](#cloneRegistry)

### Methods

* [**as](#as)
* [**clone](#clone)
* [**toJSON](#toJSON)
* [**toString](#toString)
* [**valueOf](#valueOf)
* [**getKnownFragment](#getKnownFragment)
* [**isKnownFragment](#isKnownFragment)
* [**remove](#remove)
* [**run](#run)

## Constructors<!-- -->[**](#Constructors)

### [**](#constructor)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/RawQueryFragment.ts#L17)constructor

* ****new RawQueryFragment**(sql, params): [RawQueryFragment](https://mikro-orm.io/api/core/class/RawQueryFragment.md)

- #### Parameters

  * ##### sql: string
  * ##### params: unknown\[] = <!-- -->\[]

  #### Returns [RawQueryFragment](https://mikro-orm.io/api/core/class/RawQueryFragment.md)

## Properties<!-- -->[**](#Properties)

### [**](#params)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/RawQueryFragment.ts#L19)readonlyparams

**params: unknown\[] =

<!-- -->

\[]

### [**](#sql)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/RawQueryFragment.ts#L18)readonlysql

**sql: string

### [**](#cloneRegistry)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/RawQueryFragment.ts#L11)staticoptionalcloneRegistry

**cloneRegistry?

<!-- -->

: Set\<string>

## Methods<!-- -->[**](#Methods)

### [**](#as)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/RawQueryFragment.ts#L24)as

* ****as**(alias): [RawQueryFragment](https://mikro-orm.io/api/core/class/RawQueryFragment.md)

- #### Parameters

  * ##### alias: string

  #### Returns [RawQueryFragment](https://mikro-orm.io/api/core/class/RawQueryFragment.md)

### [**](#clone)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/RawQueryFragment.ts#L57)clone

* ****clone**(): [RawQueryFragment](https://mikro-orm.io/api/core/class/RawQueryFragment.md)

- #### Returns [RawQueryFragment](https://mikro-orm.io/api/core/class/RawQueryFragment.md)

### [**](#toJSON)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/RawQueryFragment.ts#L38)toJSON

* ****toJSON**(): string

- #### Returns string

### [**](#toString)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/RawQueryFragment.ts#L42)toString

* ****toString**(): string

- #### Returns string

### [**](#valueOf)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/RawQueryFragment.ts#L34)valueOf

* ****valueOf**(): string

- #### Returns string

### [**](#getKnownFragment)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/RawQueryFragment.ts#L86)staticgetKnownFragment

* ****getKnownFragment**(key, cleanup): undefined | [RawQueryFragment](https://mikro-orm.io/api/core/class/RawQueryFragment.md)

- #### Parameters

  * ##### key: string | [RawQueryFragment](https://mikro-orm.io/api/core/class/RawQueryFragment.md)
  * ##### cleanup: boolean = <!-- -->true

  #### Returns undefined | [RawQueryFragment](https://mikro-orm.io/api/core/class/RawQueryFragment.md)

### [**](#isKnownFragment)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/RawQueryFragment.ts#L78)staticisKnownFragment

* ****isKnownFragment**(key): boolean

- #### Parameters

  * ##### key: string | [RawQueryFragment](https://mikro-orm.io/api/core/class/RawQueryFragment.md)

  #### Returns boolean

### [**](#remove)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/RawQueryFragment.ts#L100)staticremove

* ****remove**(key): void

- #### Parameters

  * ##### key: string

  #### Returns void

### [**](#run)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/utils/RawQueryFragment.ts#L62)staticrun

* ****run**\<T>(cb): Promise\<T>

- #### Parameters

  * ##### cb: (...args) => Promise\<T>


  #### Returns Promise\<T>
