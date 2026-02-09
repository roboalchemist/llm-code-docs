# Source: https://mikro-orm.io/api/knex/interface/MySqlTableBuilder.md

# MySqlTableBuilder<!-- -->

### Hierarchy

* TableBuilder
  * *MySqlTableBuilder*

## Index[**](#Index)

### Methods

* [**bigIncrements](#bigIncrements)
* [**bigint](#bigint)
* [**bigInteger](#bigInteger)
* [**binary](#binary)
* [**boolean](#boolean)
* [**check](#check)
* [**comment](#comment)
* [**date](#date)
* [**datetime](#datetime)
* [**dateTime](#dateTime)
* [**decimal](#decimal)
* [**double](#double)
* [**dropChecks](#dropChecks)
* [**dropColumn](#dropColumn)
* [**dropColumns](#dropColumns)
* [**dropForeign](#dropForeign)
* [**dropIndex](#dropIndex)
* [**dropNullable](#dropNullable)
* [**dropPrimary](#dropPrimary)
* [**dropTimestamps](#dropTimestamps)
* [**dropUnique](#dropUnique)
* [**enu](#enu)
* [**enum](#enum)
* [**float](#float)
* [**foreign](#foreign)
* [**geography](#geography)
* [**geometry](#geometry)
* [**increments](#increments)
* [**index](#index)
* [**integer](#integer)
* [**json](#json)
* [**jsonb](#jsonb)
* [**mediumint](#mediumint)
* [**point](#point)
* [**primary](#primary)
* [**queryContext](#queryContext)
* [**renameColumn](#renameColumn)
* [**setNullable](#setNullable)
* [**smallint](#smallint)
* [**specificType](#specificType)
* [**string](#string)
* [**text](#text)
* [**time](#time)
* [**timestamp](#timestamp)
* [**timestamps](#timestamps)
* [**tinyint](#tinyint)
* [**unique](#unique)
* [**uuid](#uuid)

## Methods<!-- -->[**](#Methods)

### [**](#bigIncrements)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/typings.ts#L217)bigIncrements

* ****bigIncrements**(columnName, options): ColumnBuilder

- Overrides Knex.TableBuilder.bigIncrements

  #### Parameters

  * ##### optionalcolumnName: string
  * ##### optionaloptions: [MySqlIncrementOptions](https://mikro-orm.io/api/knex.md#MySqlIncrementOptions)

  #### Returns ColumnBuilder

### [**](#bigint)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L2436)inheritedbigint

* ****bigint**(columnName): ColumnBuilder

- Inherited from Knex.TableBuilder.bigint

  #### Parameters

  * ##### columnName: string

  #### Returns ColumnBuilder

### [**](#bigInteger)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L2437)inheritedbigInteger

* ****bigInteger**(columnName): ColumnBuilder

- Inherited from Knex.TableBuilder.bigInteger

  #### Parameters

  * ##### columnName: string

  #### Returns ColumnBuilder

### [**](#binary)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L2491)inheritedbinary

* ****binary**(columnName, length): ColumnBuilder

- Inherited from Knex.TableBuilder.binary

  #### Parameters

  * ##### columnName: string
  * ##### optionallength: number

  #### Returns ColumnBuilder

### [**](#boolean)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L2455)inheritedboolean

* ****boolean**(columnName): ColumnBuilder

- Inherited from Knex.TableBuilder.boolean

  #### Parameters

  * ##### columnName: string

  #### Returns ColumnBuilder

### [**](#check)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L2558)inheritedcheck

* ****check**(checkPredicate, bindings, constraintName): TableBuilder

- Inherited from Knex.TableBuilder.check

  #### Parameters

  * ##### checkPredicate: string
  * ##### optionalbindings: Record\<string, any>
  * ##### optionalconstraintName: string

  #### Returns TableBuilder

### [**](#comment)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L2508)inheritedcomment

* ****comment**(val): void

- Inherited from Knex.TableBuilder.comment

  #### Parameters

  * ##### val: string

  #### Returns void

### [**](#date)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L2456)inheriteddate

* ****date**(columnName): ColumnBuilder

- Inherited from Knex.TableBuilder.date

  #### Parameters

  * ##### columnName: string

  #### Returns ColumnBuilder

### [**](#datetime)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L2461)inheriteddatetime

* ****datetime**(columnName, options): ColumnBuilder

- Inherited from Knex.TableBuilder.datetime

  #### Parameters

  * ##### columnName: string
  * ##### optionaloptions: Readonly<{ precision?<!-- -->: number; useTz?<!-- -->: boolean }>

  #### Returns ColumnBuilder

### [**](#dateTime)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L2457)inheriteddateTime

* ****dateTime**(columnName, options): ColumnBuilder

- Inherited from Knex.TableBuilder.dateTime

  #### Parameters

  * ##### columnName: string
  * ##### optionaloptions: Readonly<{ precision?<!-- -->: number; useTz?<!-- -->: boolean }>

  #### Returns ColumnBuilder

### [**](#decimal)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L2450)inheriteddecimal

* ****decimal**(columnName, precision, scale): ColumnBuilder

- Inherited from Knex.TableBuilder.decimal

  #### Parameters

  * ##### columnName: string
  * ##### optionalprecision: null | number
  * ##### optionalscale: number

  #### Returns ColumnBuilder

### [**](#double)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L2445)inheriteddouble

* ****double**(columnName, precision, scale): ColumnBuilder

- Inherited from Knex.TableBuilder.double

  #### Parameters

  * ##### columnName: string
  * ##### optionalprecision: number
  * ##### optionalscale: number

  #### Returns ColumnBuilder

### [**](#dropChecks)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L2577)inheriteddropChecks

* ****dropChecks**(checkConstraintNames): TableBuilder

- Inherited from Knex.TableBuilder.dropChecks

  #### Parameters

  * ##### checkConstraintNames: string | string\[]

  #### Returns TableBuilder

### [**](#dropColumn)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L2429)inheriteddropColumn

* ****dropColumn**(columnName): TableBuilder

- Inherited from Knex.TableBuilder.dropColumn

  #### Parameters

  * ##### columnName: string

  #### Returns TableBuilder

### [**](#dropColumns)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L2430)inheriteddropColumns

* ****dropColumns**(...columnNames): TableBuilder

- Inherited from Knex.TableBuilder.dropColumns

  #### Parameters

  * ##### rest...columnNames: string\[]

  #### Returns TableBuilder

### [**](#dropForeign)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L2563)inheriteddropForeign

* ****dropForeign**(columnNames, foreignKeyName): TableBuilder

- Inherited from Knex.TableBuilder.dropForeign

  #### Parameters

  * ##### columnNames: string | readonly<!-- --> string\[]
  * ##### optionalforeignKeyName: string

  #### Returns TableBuilder

### [**](#dropIndex)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L2572)inheriteddropIndex

* ****dropIndex**(columnNames, indexName): TableBuilder

- Inherited from Knex.TableBuilder.dropIndex

  #### Parameters

  * ##### columnNames: string | readonly<!-- --> (string | Raw\<any>)\[]
  * ##### optionalindexName: string

  #### Returns TableBuilder

### [**](#dropNullable)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L2537)inheriteddropNullable

* ****dropNullable**(column): TableBuilder

- Inherited from Knex.TableBuilder.dropNullable

  #### Parameters

  * ##### column: string

  #### Returns TableBuilder

### [**](#dropPrimary)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L2571)inheriteddropPrimary

* ****dropPrimary**(constraintName): TableBuilder

- Inherited from Knex.TableBuilder.dropPrimary

  #### Parameters

  * ##### optionalconstraintName: string

  #### Returns TableBuilder

### [**](#dropTimestamps)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L2576)inheriteddropTimestamps

* ****dropTimestamps**(useCamelCase): TableBuilder

- Inherited from Knex.TableBuilder.dropTimestamps

  #### Parameters

  * ##### optionaluseCamelCase: boolean

  #### Returns TableBuilder

### [**](#dropUnique)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L2567)inheriteddropUnique

* ****dropUnique**(columnNames, indexName): TableBuilder

- Inherited from Knex.TableBuilder.dropUnique

  #### Parameters

  * ##### columnNames: readonly<!-- --> (string | Raw\<any>)\[]
  * ##### optionalindexName: string

  #### Returns TableBuilder

### [**](#enu)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L2497)inheritedenu

* ****enu**(columnName, values, options): ColumnBuilder

- Inherited from Knex.TableBuilder.enu

  #### Parameters

  * ##### columnName: string
  * ##### values: null | readonly<!-- --> Value\[]
  * ##### optionaloptions: EnumOptions

  #### Returns ColumnBuilder

### [**](#enum)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L2492)inheritedenum

* ****enum**(columnName, values, options): ColumnBuilder

- Inherited from Knex.TableBuilder.enum

  #### Parameters

  * ##### columnName: string
  * ##### values: null | readonly<!-- --> Value\[]
  * ##### optionaloptions: EnumOptions

  #### Returns ColumnBuilder

### [**](#float)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L2440)inheritedfloat

* ****float**(columnName, precision, scale): ColumnBuilder

- Inherited from Knex.TableBuilder.float

  #### Parameters

  * ##### columnName: string
  * ##### optionalprecision: number
  * ##### optionalscale: number

  #### Returns ColumnBuilder

### [**](#foreign)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L2553)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L2554)inheritedforeign

* ****foreign**(column, foreignKeyName): ForeignConstraintBuilder
* ****foreign**(columns, foreignKeyName): MultikeyForeignConstraintBuilder

- Inherited from Knex.TableBuilder.foreign

  #### Parameters

  * ##### column: string
  * ##### optionalforeignKeyName: string

  #### Returns ForeignConstraintBuilder

### [**](#geography)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L2489)inheritedgeography

* ****geography**(columnName): ColumnBuilder

- Inherited from Knex.TableBuilder.geography

  #### Parameters

  * ##### columnName: string

  #### Returns ColumnBuilder

### [**](#geometry)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L2488)inheritedgeometry

* ****geometry**(columnName): ColumnBuilder

- Inherited from Knex.TableBuilder.geometry

  #### Parameters

  * ##### columnName: string

  #### Returns ColumnBuilder

### [**](#increments)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/typings.ts#L216)increments

* ****increments**(columnName, options): ColumnBuilder

- Overrides Knex.TableBuilder.increments

  #### Parameters

  * ##### optionalcolumnName: string
  * ##### optionaloptions: [MySqlIncrementOptions](https://mikro-orm.io/api/knex.md#MySqlIncrementOptions)

  #### Returns ColumnBuilder

### [**](#index)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L2522)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L2527)inheritedindex

* ****index**(columnNames, indexName, indexType): TableBuilder
* ****index**(columnNames, indexName, options): TableBuilder

- Inherited from Knex.TableBuilder.index

  #### Parameters

  * ##### columnNames: string | readonly<!-- --> (string | Raw\<any>)\[]
  * ##### optionalindexName: string
  * ##### optionalindexType: string

  #### Returns TableBuilder

### [**](#integer)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L2432)inheritedinteger

* ****integer**(columnName, length): ColumnBuilder

- Inherited from Knex.TableBuilder.integer

  #### Parameters

  * ##### columnName: string
  * ##### optionallength: number

  #### Returns ColumnBuilder

### [**](#json)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L2502)inheritedjson

* ****json**(columnName): ColumnBuilder

- Inherited from Knex.TableBuilder.json

  #### Parameters

  * ##### columnName: string

  #### Returns ColumnBuilder

### [**](#jsonb)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L2503)inheritedjsonb

* ****jsonb**(columnName): ColumnBuilder

- Inherited from Knex.TableBuilder.jsonb

  #### Parameters

  * ##### columnName: string

  #### Returns ColumnBuilder

### [**](#mediumint)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L2435)inheritedmediumint

* ****mediumint**(columnName): ColumnBuilder

- Inherited from Knex.TableBuilder.mediumint

  #### Parameters

  * ##### columnName: string

  #### Returns ColumnBuilder

### [**](#point)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L2490)inheritedpoint

* ****point**(columnName): ColumnBuilder

- Inherited from Knex.TableBuilder.point

  #### Parameters

  * ##### columnName: string

  #### Returns ColumnBuilder

### [**](#primary)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L2510)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L2518)inheritedprimary

* ****primary**(columnNames, options): TableBuilder
* ****primary**(columnNames, constraintName): TableBuilder

- Inherited from Knex.TableBuilder.primary

  #### Parameters

  * ##### columnNames: readonly<!-- --> string\[]
  * ##### optionaloptions: Readonly<{ constraintName?<!-- -->: string; deferrable?<!-- -->: deferrableType }>

  #### Returns TableBuilder

### [**](#queryContext)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L2578)inheritedqueryContext

* ****queryContext**(context): TableBuilder

- Inherited from Knex.TableBuilder.queryContext

  #### Parameters

  * ##### context: any

  #### Returns TableBuilder

### [**](#renameColumn)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L2431)inheritedrenameColumn

* ****renameColumn**(from, to): TableBuilder

- Inherited from Knex.TableBuilder.renameColumn

  #### Parameters

  * ##### from: string
  * ##### to: string

  #### Returns TableBuilder

### [**](#setNullable)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L2536)inheritedsetNullable

* ****setNullable**(column): TableBuilder

- Inherited from Knex.TableBuilder.setNullable

  #### Parameters

  * ##### column: string

  #### Returns TableBuilder

### [**](#smallint)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L2434)inheritedsmallint

* ****smallint**(columnName): ColumnBuilder

- Inherited from Knex.TableBuilder.smallint

  #### Parameters

  * ##### columnName: string

  #### Returns ColumnBuilder

### [**](#specificType)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L2509)inheritedspecificType

* ****specificType**(columnName, type): ColumnBuilder

- Inherited from Knex.TableBuilder.specificType

  #### Parameters

  * ##### columnName: string
  * ##### type: string

  #### Returns ColumnBuilder

### [**](#string)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L2439)inheritedstring

* ****string**(columnName, length): ColumnBuilder

- Inherited from Knex.TableBuilder.string

  #### Parameters

  * ##### columnName: string
  * ##### optionallength: number

  #### Returns ColumnBuilder

### [**](#text)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L2438)inheritedtext

* ****text**(columnName, textType): ColumnBuilder

- Inherited from Knex.TableBuilder.text

  #### Parameters

  * ##### columnName: string
  * ##### optionaltextType: string

  #### Returns ColumnBuilder

### [**](#time)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L2465)inheritedtime

* ****time**(columnName): ColumnBuilder

- Inherited from Knex.TableBuilder.time

  #### Parameters

  * ##### columnName: string

  #### Returns ColumnBuilder

### [**](#timestamp)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L2466)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L2471)inheritedtimestamp

* ****timestamp**(columnName, options): ColumnBuilder
* ****timestamp**(columnName, withoutTz, precision): ColumnBuilder

- Inherited from Knex.TableBuilder.timestamp

  #### Parameters

  * ##### columnName: string
  * ##### optionaloptions: Readonly<{ precision?<!-- -->: number; useTz?<!-- -->: boolean }>

  #### Returns ColumnBuilder

### [**](#timestamps)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L2476)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L2481)inheritedtimestamps

* ****timestamps**(useTimestamps, defaultToNow, useCamelCase): ColumnBuilder
* ****timestamps**(options): void

- Inherited from Knex.TableBuilder.timestamps

  #### Parameters

  * ##### optionaluseTimestamps: boolean
  * ##### optionaldefaultToNow: boolean
  * ##### optionaluseCamelCase: boolean

  #### Returns ColumnBuilder

### [**](#tinyint)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L2433)inheritedtinyint

* ****tinyint**(columnName, length): ColumnBuilder

- Inherited from Knex.TableBuilder.tinyint

  #### Parameters

  * ##### columnName: string
  * ##### optionallength: number

  #### Returns ColumnBuilder

### [**](#unique)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L2538)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L2549)inheritedunique

* ****unique**(columnNames, options): TableBuilder
* ****unique**(columnNames, indexName): TableBuilder

- Inherited from Knex.TableBuilder.unique

  #### Parameters

  * ##### columnNames: string | readonly<!-- --> (string | Raw\<any>)\[]
  * ##### optionaloptions: Readonly<{ deferrable?<!-- -->: deferrableType; indexName?<!-- -->: string; predicate?<!-- -->: QueryBuilder\<any, any>; storageEngineIndexType?<!-- -->: string; useConstraint?<!-- -->: boolean }>

  #### Returns TableBuilder

### [**](#uuid)[**](https://undefined/mikro-orm/mikro-orm/blob/master/node_modules/knex/types/index.d.ts#L2504)inheriteduuid

* ****uuid**(columnName, options): ColumnBuilder

- Inherited from Knex.TableBuilder.uuid

  #### Parameters

  * ##### columnName: string
  * ##### optionaloptions: Readonly<{ primaryKey?<!-- -->: boolean; useBinaryUuid?<!-- -->: boolean }>

  #### Returns ColumnBuilder
