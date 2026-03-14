# Source: https://mikro-orm.io/api/sql/interface/Column.md

# Column<!-- -->

## Index[**](#index)

### Properties

* [**autoincrement](#autoincrement)
* [**comment](#comment)
* [**default](#default)
* [**defaultConstraint](#defaultConstraint)
* [**enumItems](#enumItems)
* [**extra](#extra)
* [**generated](#generated)
* [**ignoreSchemaChanges](#ignoreSchemaChanges)
* [**length](#length)
* [**mappedType](#mappedtype)
* [**name](#name)
* [**nativeEnumName](#nativeEnumName)
* [**nullable](#nullable)
* [**precision](#precision)
* [**primary](#primary)
* [**scale](#scale)
* [**type](#type)
* [**unique](#unique)
* [**unsigned](#unsigned)

## Properties<!-- -->[**](#properties)

### [**](#autoincrement)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L64)optionalautoincrement

**autoincrement?

<!-- -->

: boolean

### [**](#comment)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L71)optionalcomment

**comment?

<!-- -->

: string

### [**](#default)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L69)optionaldefault

**default?

<!-- -->

: null | string

### [**](#defaultConstraint)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L70)optionaldefaultConstraint

**defaultConstraint?

<!-- -->

: string

### [**](#enumItems)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L74)optionalenumItems

**enumItems?

<!-- -->

: string\[]

### [**](#extra)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L78)optionalextra

**extra?

<!-- -->

: string

mysql only

### [**](#generated)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L72)optionalgenerated

**generated?

<!-- -->

: string

### [**](#ignoreSchemaChanges)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L79)optionalignoreSchemaChanges

**ignoreSchemaChanges?

<!-- -->

: (type | extra | default)\[]

### [**](#length)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L66)optionallength

**length?

<!-- -->

: number

### [**](#mappedtype)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L62)mappedType

**mappedType: [Type](https://mikro-orm.io/api/core/class/Type.md)\<unknown, unknown>

### [**](#name)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L60)name

**name: string

### [**](#nativeEnumName)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L73)optionalnativeEnumName

**nativeEnumName?

<!-- -->

: string

### [**](#nullable)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L65)optionalnullable

**nullable?

<!-- -->

: boolean

### [**](#precision)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L67)optionalprecision

**precision?

<!-- -->

: number

### [**](#primary)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L75)optionalprimary

**primary?

<!-- -->

: boolean

### [**](#scale)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L68)optionalscale

**scale?

<!-- -->

: number

### [**](#type)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L61)type

**type: string

### [**](#unique)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L76)optionalunique

**unique?

<!-- -->

: boolean

### [**](#unsigned)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/typings.ts#L63)optionalunsigned

**unsigned?

<!-- -->

: boolean
