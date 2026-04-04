# Source: https://mikro-orm.io/api/core/interface/NativeInsertUpdateManyOptions.md

# NativeInsertUpdateManyOptions<!-- --> \<T>

### Hierarchy

* [NativeInsertUpdateOptions](https://mikro-orm.io/api/core/interface/NativeInsertUpdateOptions.md)\<T>
  * *NativeInsertUpdateManyOptions*

## Index[**](#Index)

### Properties

* [**convertCustomTypes](#convertCustomTypes)
* [**ctx](#ctx)
* [**loggerContext](#loggerContext)
* [**processCollections](#processCollections)
* [**schema](#schema)
* [**upsert](#upsert)

## Properties<!-- -->[**](#Properties)

### [**](#convertCustomTypes)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L219)optionalinheritedconvertCustomTypes

**convertCustomTypes?

<!-- -->

: boolean

Inherited from NativeInsertUpdateOptions.convertCustomTypes

### [**](#ctx)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L220)optionalinheritedctx

**ctx?

<!-- -->

: any

Inherited from NativeInsertUpdateOptions.ctx

### [**](#loggerContext)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L224)optionalinheritedloggerContext

**loggerContext?

<!-- -->

: [LogContext](https://mikro-orm.io/api/core/interface/LogContext.md)

Inherited from NativeInsertUpdateOptions.loggerContext

### [**](#processCollections)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L228)optionalprocessCollections

**processCollections?

<!-- -->

: boolean

### [**](#schema)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L221)optionalinheritedschema

**schema?

<!-- -->

: string

Inherited from NativeInsertUpdateOptions.schema

### [**](#upsert)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L223)optionalinheritedupsert

**upsert?

<!-- -->

: boolean

Inherited from NativeInsertUpdateOptions.upsert

`nativeUpdate()` only option
