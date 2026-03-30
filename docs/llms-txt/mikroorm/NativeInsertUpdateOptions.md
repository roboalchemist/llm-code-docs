# Source: https://mikro-orm.io/api/core/interface/NativeInsertUpdateOptions.md

# NativeInsertUpdateOptions<!-- --> \<T>

### Hierarchy

* *NativeInsertUpdateOptions*
  * [NativeInsertUpdateManyOptions](https://mikro-orm.io/api/core/interface/NativeInsertUpdateManyOptions.md)

## Index[**](#index)

### Properties

* [**convertCustomTypes](#convertCustomTypes)
* [**ctx](#ctx)
* [**filters](#filters)
* [**loggerContext](#loggerContext)
* [**schema](#schema)
* [**unionWhere](#unionWhere)
* [**unionWhereStrategy](#unionWhereStrategy)
* [**upsert](#upsert)

## Properties<!-- -->[**](#properties)

### [**](#convertCustomTypes)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L379)optionalconvertCustomTypes

**convertCustomTypes?

<!-- -->

: boolean

### [**](#ctx)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L380)optionalctx

**ctx?

<!-- -->

: any

### [**](#filters)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L389)optionalfilters

**filters?

<!-- -->

: [FilterOptions](https://mikro-orm.io/api/core.md#FilterOptions)

### [**](#loggerContext)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L384)optionalloggerContext

**loggerContext?

<!-- -->

: [LogContext](https://mikro-orm.io/api/core/interface/LogContext.md)

### [**](#schema)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L381)optionalschema

**schema?

<!-- -->

: string

### [**](#unionWhere)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L386)optionalunionWhere

**unionWhere?

<!-- -->

: [ObjectQuery](https://mikro-orm.io/api/core.md#ObjectQuery)\<T>\[]

sql only

### [**](#unionWhereStrategy)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L388)optionalunionWhereStrategy

**unionWhereStrategy?

<!-- -->

: union-all | union

sql only

### [**](#upsert)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L383)optionalupsert

**upsert?

<!-- -->

: boolean

`nativeUpdate()` only option
