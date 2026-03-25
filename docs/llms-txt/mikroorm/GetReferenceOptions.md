# Source: https://mikro-orm.io/api/core/interface/GetReferenceOptions.md

# GetReferenceOptions<!-- -->

## Index[**](#index)

### Properties

* [**convertCustomTypes](#convertCustomTypes)
* [**key](#key)
* [**schema](#schema)
* [**wrapped](#wrapped)

## Properties<!-- -->[**](#properties)

### [**](#convertCustomTypes)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L502)optionalconvertCustomTypes

**convertCustomTypes?

<!-- -->

: boolean

### [**](#key)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L508)optionalkey

**key?

<!-- -->

: string

Property name to use for identity map lookup instead of the primary key. This is useful for creating references by unique non-PK properties.

### [**](#schema)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L503)optionalschema

**schema?

<!-- -->

: string

### [**](#wrapped)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L501)optionalwrapped

**wrapped?

<!-- -->

: boolean
