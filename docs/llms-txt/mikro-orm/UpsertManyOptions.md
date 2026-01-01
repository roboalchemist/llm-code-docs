# Source: https://mikro-orm.io/api/core/interface/UpsertManyOptions.md

# UpsertManyOptions<!-- --> \<Entity, Fields>

### Hierarchy

* [UpsertOptions](https://mikro-orm.io/api/core/interface/UpsertOptions.md)\<Entity, Fields>
  * *UpsertManyOptions*

## Index[**](#Index)

### Properties

* [**batchSize](#batchSize)
* [**convertCustomTypes](#convertCustomTypes)
* [**ctx](#ctx)
* [**disableIdentityMap](#disableIdentityMap)
* [**loggerContext](#loggerContext)
* [**onConflictAction](#onConflictAction)
* [**onConflictExcludeFields](#onConflictExcludeFields)
* [**onConflictFields](#onConflictFields)
* [**onConflictMergeFields](#onConflictMergeFields)
* [**schema](#schema)

## Properties<!-- -->[**](#Properties)

### [**](#batchSize)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L240)optionalbatchSize

**batchSize?

<!-- -->

: number

### [**](#convertCustomTypes)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L219)optionalinheritedconvertCustomTypes

**convertCustomTypes?

<!-- -->

: boolean

Inherited from UpsertOptions.convertCustomTypes

### [**](#ctx)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L220)optionalinheritedctx

**ctx?

<!-- -->

: any

Inherited from UpsertOptions.ctx

### [**](#disableIdentityMap)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L236)optionalinheriteddisableIdentityMap

**disableIdentityMap?

<!-- -->

: boolean

Inherited from UpsertOptions.disableIdentityMap

### [**](#loggerContext)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L224)optionalinheritedloggerContext

**loggerContext?

<!-- -->

: [LogContext](https://mikro-orm.io/api/core/interface/LogContext.md)

Inherited from UpsertOptions.loggerContext

### [**](#onConflictAction)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L233)optionalinheritedonConflictAction

**onConflictAction?

<!-- -->

: merge | ignore

Inherited from UpsertOptions.onConflictAction

### [**](#onConflictExcludeFields)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L235)optionalinheritedonConflictExcludeFields

**onConflictExcludeFields?

<!-- -->

: [AutoPath](https://mikro-orm.io/api/core.md#AutoPath)\<Entity, Fields, \*, 9>\[]

Inherited from UpsertOptions.onConflictExcludeFields

### [**](#onConflictFields)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L232)optionalinheritedonConflictFields

**onConflictFields?

<!-- -->

: [RawQueryFragment](https://mikro-orm.io/api/core/class/RawQueryFragment.md) | keyof

<!-- -->

Entity\[]

Inherited from UpsertOptions.onConflictFields

### [**](#onConflictMergeFields)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L234)optionalinheritedonConflictMergeFields

**onConflictMergeFields?

<!-- -->

: [AutoPath](https://mikro-orm.io/api/core.md#AutoPath)\<Entity, Fields, \*, 9>\[]

Inherited from UpsertOptions.onConflictMergeFields

### [**](#schema)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/drivers/IDatabaseDriver.ts#L221)optionalinheritedschema

**schema?

<!-- -->

: string

Inherited from UpsertOptions.schema
ema

**schema?

<!-- -->

: string

Inherited from UpsertOptions.schema
