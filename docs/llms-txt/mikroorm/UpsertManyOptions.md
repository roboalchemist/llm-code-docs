# Source: https://mikro-orm.io/api/core/interface/UpsertManyOptions.md

# UpsertManyOptions<!-- --> \<Entity, Fields>

### Hierarchy

* [UpsertOptions](https://mikro-orm.io/api/core/interface/UpsertOptions.md)\<Entity, Fields>
  * *UpsertManyOptions*

## Index[**](#index)

### Properties

* [**batchSize](#batchSize)
* [**convertCustomTypes](#convertCustomTypes)
* [**ctx](#ctx)
* [**disableIdentityMap](#disableIdentityMap)
* [**filters](#filters)
* [**loggerContext](#loggerContext)
* [**onConflictAction](#onConflictAction)
* [**onConflictExcludeFields](#onConflictExcludeFields)
* [**onConflictFields](#onConflictFields)
* [**onConflictMergeFields](#onConflictMergeFields)
* [**onConflictWhere](#onConflictWhere)
* [**schema](#schema)
* [**unionWhere](#unionWhere)
* [**unionWhereStrategy](#unionWhereStrategy)

## Properties<!-- -->[**](#properties)

### [**](#batchSize)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L411)optionalbatchSize

**batchSize?

<!-- -->

: number

### [**](#convertCustomTypes)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L379)optionalinheritedconvertCustomTypes

**convertCustomTypes?

<!-- -->

: boolean

Inherited from UpsertOptions.convertCustomTypes

### [**](#ctx)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L380)optionalinheritedctx

**ctx?

<!-- -->

: any

Inherited from UpsertOptions.ctx

### [**](#disableIdentityMap)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L407)optionalinheriteddisableIdentityMap

**disableIdentityMap?

<!-- -->

: boolean

Inherited from UpsertOptions.disableIdentityMap

### [**](#filters)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L389)optionalinheritedfilters

**filters?

<!-- -->

: [FilterOptions](https://mikro-orm.io/api/core.md#FilterOptions)

Inherited from UpsertOptions.filters

### [**](#loggerContext)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L384)optionalinheritedloggerContext

**loggerContext?

<!-- -->

: [LogContext](https://mikro-orm.io/api/core/interface/LogContext.md)

Inherited from UpsertOptions.loggerContext

### [**](#onConflictAction)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L403)optionalinheritedonConflictAction

**onConflictAction?

<!-- -->

: merge | ignore

Inherited from UpsertOptions.onConflictAction

### [**](#onConflictExcludeFields)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L405)optionalinheritedonConflictExcludeFields

**onConflictExcludeFields?

<!-- -->

: [AutoPath](https://mikro-orm.io/api/core.md#AutoPath)\<Entity, Fields, \*, 9>\[]

Inherited from UpsertOptions.onConflictExcludeFields

### [**](#onConflictFields)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L402)optionalinheritedonConflictFields

**onConflictFields?

<!-- -->

: [RawQueryFragment](https://mikro-orm.io/api/core/class/RawQueryFragment.md)\<string> | keyof

<!-- -->

Entity\[]

Inherited from UpsertOptions.onConflictFields

### [**](#onConflictMergeFields)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L404)optionalinheritedonConflictMergeFields

**onConflictMergeFields?

<!-- -->

: [AutoPath](https://mikro-orm.io/api/core.md#AutoPath)\<Entity, Fields, \*, 9>\[]

Inherited from UpsertOptions.onConflictMergeFields

### [**](#onConflictWhere)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L406)optionalinheritedonConflictWhere

**onConflictWhere?

<!-- -->

: [FilterQuery](https://mikro-orm.io/api/core.md#FilterQuery)\<Entity>

Inherited from UpsertOptions.onConflictWhere

### [**](#schema)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L381)optionalinheritedschema

**schema?

<!-- -->

: string

Inherited from UpsertOptions.schema

### [**](#unionWhere)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L386)optionalinheritedunionWhere

**unionWhere?

<!-- -->

: [ObjectQuery](https://mikro-orm.io/api/core.md#ObjectQuery)\<Entity>\[]

Inherited from UpsertOptions.unionWhere

sql only

### [**](#unionWhereStrategy)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/drivers/IDatabaseDriver.ts#L388)optionalinheritedunionWhereStrategy

**unionWhereStrategy?

<!-- -->

: union-all | union

Inherited from UpsertOptions.unionWhereStrategy

sql only
