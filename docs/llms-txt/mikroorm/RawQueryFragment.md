# Source: https://mikro-orm.io/api/core/class/RawQueryFragment.md

# RawQueryFragment<!-- --> \<Alias>

## Index[**](#index)

### Constructors

* [**constructor](#constructor)

### Properties

* [**params](#params)
* [**sql](#sql)

### Accessors

* [**\[toStringTag\]](#\[toStringTag])
* [**key](#key)

### Methods

* [**\[toPrimitive\]](#\[toPrimitive])
* [**as](#as)
* [**clone](#clone)
* [**toJSON](#tojson)
* [**getKnownFragment](#getKnownFragment)
* [**hasObjectFragments](#hasObjectFragments)
* [**isKnownFragment](#isKnownFragment)
* [**isKnownFragmentSymbol](#isKnownFragmentSymbol)

## Constructors<!-- -->[**](#constructors)

### [**](#constructor)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/RawQueryFragment.ts#L16)constructor

* ****new RawQueryFragment**\<Alias>(sql, params): [RawQueryFragment](https://mikro-orm.io/api/core/class/RawQueryFragment.md)\<Alias>

* #### Parameters

  * ##### sql: string

  * ##### params: unknown\[] = <!-- -->\[]

  #### Returns [RawQueryFragment](https://mikro-orm.io/api/core/class/RawQueryFragment.md)\<Alias>

## Properties<!-- -->[**](#properties)

### [**](#params)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/RawQueryFragment.ts#L18)readonlyparams

**params: unknown\[] =

<!-- -->

\[]

### [**](#sql)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/RawQueryFragment.ts#L17)readonlysql

**sql: string

## Accessors<!-- -->[**](#accessors)

### [**](#\[toStringTag])[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/RawQueryFragment.ts#L45)\[toStringTag]

* **get \[toStringTag]\(): string

* #### Returns string

### [**](#key)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/RawQueryFragment.ts#L21)key

* **get key(): [RawQueryFragmentSymbol](https://mikro-orm.io/api/core.md#RawQueryFragmentSymbol)

* #### Returns [RawQueryFragmentSymbol](https://mikro-orm.io/api/core.md#RawQueryFragmentSymbol)

## Methods<!-- -->[**](#methods)

### [**](#\[toPrimitive])[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/RawQueryFragment.ts#L34)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/RawQueryFragment.ts#L35)\[toPrimitive]

* ****\[toPrimitive]**(hint): [RawQueryFragmentSymbol](https://mikro-orm.io/api/core.md#RawQueryFragmentSymbol)

* #### Parameters

  * ##### hint: string

  #### Returns [RawQueryFragmentSymbol](https://mikro-orm.io/api/core.md#RawQueryFragmentSymbol)

### [**](#as)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/RawQueryFragment.ts#L30)as

* ****as**\<A>(alias): [RawQueryFragment](https://mikro-orm.io/api/core/class/RawQueryFragment.md)\<A>

* #### Parameters

  * ##### alias: A

  #### Returns [RawQueryFragment](https://mikro-orm.io/api/core/class/RawQueryFragment.md)\<A>

### [**](#clone)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/RawQueryFragment.ts#L53)clone

* ****clone**(): this

* #### Returns this

### [**](#tojson)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/RawQueryFragment.ts#L49)toJSON

* ****toJSON**(): string

* #### Returns string

### [**](#getKnownFragment)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/RawQueryFragment.ts#L76)staticgetKnownFragment

* ****getKnownFragment**(key): undefined | [RawQueryFragment](https://mikro-orm.io/api/core/class/RawQueryFragment.md)\<string>

* #### Parameters

  * ##### key: unknown

  #### Returns undefined | [RawQueryFragment](https://mikro-orm.io/api/core/class/RawQueryFragment.md)\<string>

### [**](#hasObjectFragments)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/RawQueryFragment.ts#L61)statichasObjectFragments

* ****hasObjectFragments**(object): boolean

* #### Parameters

  * ##### object: unknown

  #### Returns boolean

### [**](#isKnownFragment)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/RawQueryFragment.ts#L68)staticisKnownFragment

* ****isKnownFragment**(key): key is symbol | [RawQueryFragment](https://mikro-orm.io/api/core/class/RawQueryFragment.md)\<string>

* #### Parameters

  * ##### key: unknown

  #### Returns key is symbol | [RawQueryFragment](https://mikro-orm.io/api/core/class/RawQueryFragment.md)\<string>

### [**](#isKnownFragmentSymbol)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/utils/RawQueryFragment.ts#L57)staticisKnownFragmentSymbol

* ****isKnownFragmentSymbol**(key): key is [RawQueryFragmentSymbol](https://mikro-orm.io/api/core.md#RawQueryFragmentSymbol)

* #### Parameters

  * ##### key: unknown

  #### Returns key is [RawQueryFragmentSymbol](https://mikro-orm.io/api/core.md#RawQueryFragmentSymbol)
