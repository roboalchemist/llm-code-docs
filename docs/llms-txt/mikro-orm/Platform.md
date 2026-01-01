# Source: https://mikro-orm.io/api/core/class/Platform.md

# abstractPlatform<!-- -->

### Hierarchy

* *Platform*

  * [AbstractSqlPlatform](https://mikro-orm.io/api/knex/class/AbstractSqlPlatform.md)
  * [MongoPlatform](https://mikro-orm.io/api/mongodb/class/MongoPlatform.md)

## Index[**](#Index)

### Constructors

* [**constructor](#constructor)

### Methods

* [**allowsComparingTuples](#allowsComparingTuples)
* [**allowsMultiInsert](#allowsMultiInsert)
* [**cloneEmbeddable](#cloneEmbeddable)
* [**convertDateToJSValue](#convertDateToJSValue)
* [**convertIntervalToDatabaseValue](#convertIntervalToDatabaseValue)
* [**convertIntervalToJSValue](#convertIntervalToJSValue)
* [**convertJsonToDatabaseValue](#convertJsonToDatabaseValue)
* [**convertJsonToJSValue](#convertJsonToJSValue)
* [**convertsJsonAutomatically](#convertsJsonAutomatically)
* [**denormalizePrimaryKey](#denormalizePrimaryKey)
* [**escape](#escape)
* [**extractSimpleType](#extractSimpleType)
* [**formatQuery](#formatQuery)
* [**generateCustomOrder](#generateCustomOrder)
* [**getArrayDeclarationSQL](#getArrayDeclarationSQL)
* [**getBigIntTypeDeclarationSQL](#getBigIntTypeDeclarationSQL)
* [**getBlobDeclarationSQL](#getBlobDeclarationSQL)
* [**getBooleanTypeDeclarationSQL](#getBooleanTypeDeclarationSQL)
* [**getCharTypeDeclarationSQL](#getCharTypeDeclarationSQL)
* [**getConfig](#getConfig)
* [**getCurrentTimestampSQL](#getCurrentTimestampSQL)
* [**getDateTimeTypeDeclarationSQL](#getDateTimeTypeDeclarationSQL)
* [**getDateTypeDeclarationSQL](#getDateTypeDeclarationSQL)
* [**getDecimalTypeDeclarationSQL](#getDecimalTypeDeclarationSQL)
* [**getDefaultCharLength](#getDefaultCharLength)
* [**getDefaultCharset](#getDefaultCharset)
* [**getDefaultDateTimeLength](#getDefaultDateTimeLength)
* [**getDefaultMappedType](#getDefaultMappedType)
* [**getDefaultPrimaryName](#getDefaultPrimaryName)
* [**getDefaultSchemaName](#getDefaultSchemaName)
* [**getDefaultVarcharLength](#getDefaultVarcharLength)
* [**getDefaultVersionLength](#getDefaultVersionLength)
* [**getDoubleDeclarationSQL](#getDoubleDeclarationSQL)
* [**getEnumTypeDeclarationSQL](#getEnumTypeDeclarationSQL)
* [**getExceptionConverter](#getExceptionConverter)
* [**getExtension](#getExtension)
* [**getFloatDeclarationSQL](#getFloatDeclarationSQL)
* [**getFullTextIndexExpression](#getFullTextIndexExpression)
* [**getFullTextWhereClause](#getFullTextWhereClause)
* [**getIndexName](#getIndexName)
* [**getIntegerTypeDeclarationSQL](#getIntegerTypeDeclarationSQL)
* [**getIntervalTypeDeclarationSQL](#getIntervalTypeDeclarationSQL)
* [**getJsonDeclarationSQL](#getJsonDeclarationSQL)
* [**getJsonIndexDefinition](#getJsonIndexDefinition)
* [**getMappedType](#getMappedType)
* [**getMediumIntTypeDeclarationSQL](#getMediumIntTypeDeclarationSQL)
* [**getNamingStrategy](#getNamingStrategy)
* [**getRegExpOperator](#getRegExpOperator)
* [**getRegExpValue](#getRegExpValue)
* [**getRepositoryClass](#getRepositoryClass)
* [**getSchemaGenerator](#getSchemaGenerator)
* [**getSchemaHelper](#getSchemaHelper)
* [**getSearchJsonPropertyKey](#getSearchJsonPropertyKey)
* [**getSearchJsonPropertySQL](#getSearchJsonPropertySQL)
* [**getSerializedPrimaryKeyField](#getSerializedPrimaryKeyField)
* [**getSmallIntTypeDeclarationSQL](#getSmallIntTypeDeclarationSQL)
* [**getTextTypeDeclarationSQL](#getTextTypeDeclarationSQL)
* [**getTimeTypeDeclarationSQL](#getTimeTypeDeclarationSQL)
* [**getTimezone](#getTimezone)
* [**getTinyIntTypeDeclarationSQL](#getTinyIntTypeDeclarationSQL)
* [**getUuidTypeDeclarationSQL](#getUuidTypeDeclarationSQL)
* [**getVarcharTypeDeclarationSQL](#getVarcharTypeDeclarationSQL)
* [**indexForeignKeys](#indexForeignKeys)
* [**isAllowedTopLevelOperator](#isAllowedTopLevelOperator)
* [**isBigIntProperty](#isBigIntProperty)
* [**isNumericColumn](#isNumericColumn)
* [**isNumericProperty](#isNumericProperty)
* [**isPopulated](#isPopulated)
* [**isRaw](#isRaw)
* [**lookupExtensions](#lookupExtensions)
* [**marshallArray](#marshallArray)
* [**normalizeColumnType](#normalizeColumnType)
* [**normalizePrimaryKey](#normalizePrimaryKey)
* [**parseDate](#parseDate)
* [**processDateProperty](#processDateProperty)
* [**quoteIdentifier](#quoteIdentifier)
* [**quoteValue](#quoteValue)
* [**quoteVersionValue](#quoteVersionValue)
* [**setConfig](#setConfig)
* [**shouldHaveColumn](#shouldHaveColumn)
* [**supportsCreatingFullTextIndex](#supportsCreatingFullTextIndex)
* [**supportsCustomPrimaryKeyNames](#supportsCustomPrimaryKeyNames)
* [**supportsDownMigrations](#supportsDownMigrations)
* [**supportsMultipleCascadePaths](#supportsMultipleCascadePaths)
* [**supportsMultipleStatements](#supportsMultipleStatements)
* [**supportsNativeEnums](#supportsNativeEnums)
* [**supportsTransactions](#supportsTransactions)
* [**supportsUnsigned](#supportsUnsigned)
* [**unmarshallArray](#unmarshallArray)
* [**usesBatchInserts](#usesBatchInserts)
* [**usesBatchUpdates](#usesBatchUpdates)
* [**usesCascadeStatement](#usesCascadeStatement)
* [**usesDefaultKeyword](#usesDefaultKeyword)
* [**usesDifferentSerializedPrimaryKey](#usesDifferentSerializedPrimaryKey)
* [**usesImplicitTransactions](#usesImplicitTransactions)
* [**usesOutputStatement](#usesOutputStatement)
* [**usesPivotTable](#usesPivotTable)
* [**usesReturningStatement](#usesReturningStatement)
* [**validateMetadata](#validateMetadata)

## Constructors<!-- -->[**](#Constructors)

### [**](#constructor)constructor

* ****new Platform**(): [Platform](https://mikro-orm.io/api/core/class/Platform.md)

- #### Returns [Platform](https://mikro-orm.io/api/core/class/Platform.md)

## Methods<!-- -->[**](#Methods)

### [**](#allowsComparingTuples)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L192)allowsComparingTuples

* ****allowsComparingTuples**(): boolean

- #### Returns boolean

### [**](#allowsMultiInsert)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L90)allowsMultiInsert

* ****allowsMultiInsert**(): boolean

- #### Returns boolean

### [**](#cloneEmbeddable)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L534)cloneEmbeddable

* ****cloneEmbeddable**\<T>(data): T

- #### Parameters

  * ##### data: T

  #### Returns T

### [**](#convertDateToJSValue)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L400)convertDateToJSValue

* ****convertDateToJSValue**(value): string

- #### Parameters

  * ##### value: string | Date

  #### Returns string

### [**](#convertIntervalToDatabaseValue)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L408)convertIntervalToDatabaseValue

* ****convertIntervalToDatabaseValue**(value): unknown

- #### Parameters

  * ##### value: unknown

  #### Returns unknown

### [**](#convertIntervalToJSValue)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L404)convertIntervalToJSValue

* ****convertIntervalToJSValue**(value): unknown

- #### Parameters

  * ##### value: string

  #### Returns unknown

### [**](#convertJsonToDatabaseValue)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L392)convertJsonToDatabaseValue

* ****convertJsonToDatabaseValue**(value, context): unknown

- #### Parameters

  * ##### value: unknown
  * ##### optionalcontext: [TransformContext](https://mikro-orm.io/api/core/interface/TransformContext.md)

  #### Returns unknown

### [**](#convertJsonToJSValue)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L396)convertJsonToJSValue

* ****convertJsonToJSValue**(value, context): unknown

- #### Parameters

  * ##### value: unknown
  * ##### optionalcontext: [TransformContext](https://mikro-orm.io/api/core/interface/TransformContext.md)

  #### Returns unknown

### [**](#convertsJsonAutomatically)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L388)convertsJsonAutomatically

* ****convertsJsonAutomatically**(): boolean

- #### Returns boolean

### [**](#denormalizePrimaryKey)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L122)denormalizePrimaryKey

* ****denormalizePrimaryKey**(data): IPrimaryKeyValue

- Converts scalar primary key representation to native driver wrapper (e.g. string to mongodb's ObjectId)

  ***

  #### Parameters

  * ##### data: IPrimaryKeyValue

  #### Returns IPrimaryKeyValue

### [**](#escape)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L487)escape

* ****escape**(value): string

- #### Parameters

  * ##### value: any

  #### Returns string

### [**](#extractSimpleType)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L276)extractSimpleType

* ****extractSimpleType**(type): string

- #### Parameters

  * ##### type: string

  #### Returns string

### [**](#formatQuery)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L491)formatQuery

* ****formatQuery**(sql, params): string

- #### Parameters

  * ##### sql: string
  * ##### params: readonly<!-- --> any\[]

  #### Returns string

### [**](#generateCustomOrder)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L641)generateCustomOrder

* ****generateCustomOrder**(escapedColumn, values): void

- Generates a custom order by statement given a set of in order values, eg. ORDER BY (CASE WHEN priority = 'low' THEN 1 WHEN priority = 'medium' THEN 2 ELSE NULL END)

  ***

  #### Parameters

  * ##### escapedColumn: string
  * ##### values: unknown\[]

  #### Returns void

### [**](#getArrayDeclarationSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L339)getArrayDeclarationSQL

* ****getArrayDeclarationSQL**(): string

- #### Returns string

### [**](#getBigIntTypeDeclarationSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L228)getBigIntTypeDeclarationSQL

* ****getBigIntTypeDeclarationSQL**(column): string

- #### Parameters

  * ##### column: { autoincrement?<!-- -->: boolean; length?<!-- -->: number; unsigned?<!-- -->: boolean }
    * ##### optionalautoincrement: boolean
    * ##### optionallength: number
    * ##### optionalunsigned: boolean

  #### Returns string

### [**](#getBlobDeclarationSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L355)getBlobDeclarationSQL

* ****getBlobDeclarationSQL**(): string

- #### Returns string

### [**](#getBooleanTypeDeclarationSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L208)getBooleanTypeDeclarationSQL

* ****getBooleanTypeDeclarationSQL**(): string

- #### Returns string

### [**](#getCharTypeDeclarationSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L232)getCharTypeDeclarationSQL

* ****getCharTypeDeclarationSQL**(column): string

- #### Parameters

  * ##### column: { length?<!-- -->: number }
    * ##### optionallength: number

  #### Returns string

### [**](#getConfig)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L553)getConfig

* ****getConfig**(): [Configuration](https://mikro-orm.io/api/core/class/Configuration.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>, [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>>

- #### Returns [Configuration](https://mikro-orm.io/api/core/class/Configuration.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>, [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>>

### [**](#getCurrentTimestampSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L140)getCurrentTimestampSQL

* ****getCurrentTimestampSQL**(length): string

- Returns the SQL specific for the platform to get the current timestamp

  ***

  #### Parameters

  * ##### optionallength: number

  #### Returns string

### [**](#getDateTimeTypeDeclarationSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L144)getDateTimeTypeDeclarationSQL

* ****getDateTimeTypeDeclarationSQL**(column): string

- #### Parameters

  * ##### column: { length?<!-- -->: number }
    * ##### optionallength: number

  #### Returns string

### [**](#getDateTypeDeclarationSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L160)getDateTypeDeclarationSQL

* ****getDateTypeDeclarationSQL**(length): string

- #### Parameters

  * ##### optionallength: number

  #### Returns string

### [**](#getDecimalTypeDeclarationSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L264)getDecimalTypeDeclarationSQL

* ****getDecimalTypeDeclarationSQL**(column): string

- #### Parameters

  * ##### column: { precision?<!-- -->: number; scale?<!-- -->: number }
    * ##### optionalprecision: number
    * ##### optionalscale: number

  #### Returns string

### [**](#getDefaultCharLength)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L156)getDefaultCharLength

* ****getDefaultCharLength**(): number

- #### Returns number

### [**](#getDefaultCharset)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L427)getDefaultCharset

* ****getDefaultCharset**(): string

- #### Returns string

### [**](#getDefaultDateTimeLength)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L148)getDefaultDateTimeLength

* ****getDefaultDateTimeLength**(): number

- #### Returns number

### [**](#getDefaultMappedType)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L292)getDefaultMappedType

* ****getDefaultMappedType**(type): [Type](https://mikro-orm.io/api/core/class/Type.md)\<unknown, unknown>

- #### Parameters

  * ##### type: string

  #### Returns [Type](https://mikro-orm.io/api/core/class/Type.md)\<unknown, unknown>

### [**](#getDefaultPrimaryName)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L582)getDefaultPrimaryName

* ****getDefaultPrimaryName**(tableName, columns): string

- #### Parameters

  * ##### tableName: string
  * ##### columns: string\[]

  #### Returns string

### [**](#getDefaultSchemaName)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L204)getDefaultSchemaName

* ****getDefaultSchemaName**(): undefined | string

- #### Returns undefined | string

### [**](#getDefaultVarcharLength)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L152)getDefaultVarcharLength

* ****getDefaultVarcharLength**(): number

- #### Returns number

### [**](#getDefaultVersionLength)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L188)getDefaultVersionLength

* ****getDefaultVersionLength**(): number

- #### Returns number

### [**](#getDoubleDeclarationSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L260)getDoubleDeclarationSQL

* ****getDoubleDeclarationSQL**(): string

- #### Returns string

### [**](#getEnumTypeDeclarationSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L248)getEnumTypeDeclarationSQL

* ****getEnumTypeDeclarationSQL**(column): string

- #### Parameters

  * ##### column: { autoincrement?<!-- -->: boolean; fieldNames: string\[]; items?<!-- -->: unknown\[]; length?<!-- -->: number; unsigned?<!-- -->: boolean }
    * ##### optionalautoincrement: boolean
    * ##### fieldNames: string\[]
    * ##### optionalitems: unknown\[]
    * ##### optionallength: number
    * ##### optionalunsigned: boolean

  #### Returns string

### [**](#getExceptionConverter)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L431)getExceptionConverter

* ****getExceptionConverter**(): [ExceptionConverter](https://mikro-orm.io/api/core/class/ExceptionConverter.md)

- #### Returns [ExceptionConverter](https://mikro-orm.io/api/core/class/ExceptionConverter.md)

### [**](#getExtension)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L447)getExtension

* ****getExtension**\<T>(extensionName, extensionKey, moduleName, em): T

- #### Parameters

  * ##### extensionName: string
  * ##### extensionKey: string
  * ##### moduleName: string
  * ##### em: [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>

  #### Returns T

### [**](#getFloatDeclarationSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L256)getFloatDeclarationSQL

* ****getFloatDeclarationSQL**(): string

- #### Returns string

### [**](#getFullTextIndexExpression)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L384)getFullTextIndexExpression

* ****getFullTextIndexExpression**(indexName, schemaName, tableName, columns): string

- #### Parameters

  * ##### indexName: string
  * ##### schemaName: undefined | string
  * ##### tableName: string
  * ##### columns: [SimpleColumnMeta](https://mikro-orm.io/api/core/interface/SimpleColumnMeta.md)\[]

  #### Returns string

### [**](#getFullTextWhereClause)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L376)getFullTextWhereClause

* ****getFullTextWhereClause**(prop): string

- #### Parameters

  * ##### prop: [EntityProperty](https://mikro-orm.io/api/core/interface/EntityProperty.md)\<any, any>

  #### Returns string

### [**](#getIndexName)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L577)getIndexName

* ****getIndexName**(tableName, columns, type): string

- Returns the default name of index for the given columns

  ***

  #### Parameters

  * ##### tableName: string
  * ##### columns: string\[]
  * ##### type: primary | index | unique | foreign | sequence

  #### Returns string

### [**](#getIntegerTypeDeclarationSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L212)getIntegerTypeDeclarationSQL

* ****getIntegerTypeDeclarationSQL**(column): string

- #### Parameters

  * ##### column: { autoincrement?<!-- -->: boolean; length?<!-- -->: number; unsigned?<!-- -->: boolean }
    * ##### optionalautoincrement: boolean
    * ##### optionallength: number
    * ##### optionalunsigned: boolean

  #### Returns string

### [**](#getIntervalTypeDeclarationSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L240)getIntervalTypeDeclarationSQL

* ****getIntervalTypeDeclarationSQL**(column): string

- #### Parameters

  * ##### column: { length?<!-- -->: number }
    * ##### optionallength: number

  #### Returns string

### [**](#getJsonDeclarationSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L359)getJsonDeclarationSQL

* ****getJsonDeclarationSQL**(): string

- #### Returns string

### [**](#getJsonIndexDefinition)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L372)getJsonIndexDefinition

* ****getJsonIndexDefinition**(index): string\[]

- #### Parameters

  * ##### index: { columnNames: string\[] }
    * ##### columnNames: string\[]

  #### Returns string\[]

### [**](#getMappedType)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L287)getMappedType

* ****getMappedType**(type): [Type](https://mikro-orm.io/api/core/class/Type.md)\<unknown, unknown>

- #### Parameters

  * ##### type: string

  #### Returns [Type](https://mikro-orm.io/api/core/class/Type.md)\<unknown, unknown>

### [**](#getMediumIntTypeDeclarationSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L220)getMediumIntTypeDeclarationSQL

* ****getMediumIntTypeDeclarationSQL**(column): string

- #### Parameters

  * ##### column: { autoincrement?<!-- -->: boolean; length?<!-- -->: number; unsigned?<!-- -->: boolean }
    * ##### optionalautoincrement: boolean
    * ##### optionallength: number
    * ##### optionalunsigned: boolean

  #### Returns string

### [**](#getNamingStrategy)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L61)getNamingStrategy

* ****getNamingStrategy**(): new () => [NamingStrategy](https://mikro-orm.io/api/core/interface/NamingStrategy.md)

- #### Returns new () => [NamingStrategy](https://mikro-orm.io/api/core/interface/NamingStrategy.md)

  * * **new (): [NamingStrategy](https://mikro-orm.io/api/core/interface/NamingStrategy.md)

    - #### Returns [NamingStrategy](https://mikro-orm.io/api/core/interface/NamingStrategy.md)

### [**](#getRegExpOperator)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L168)getRegExpOperator

* ****getRegExpOperator**(val, flags): string

- #### Parameters

  * ##### optionalval: unknown
  * ##### optionalflags: string

  #### Returns string

### [**](#getRegExpValue)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L172)getRegExpValue

* ****getRegExpValue**(val): { $flags?
  <!-- -->
  : string; $re: string }

- #### Parameters

  * ##### val: RegExp

  #### Returns { $flags?<!-- -->: string; $re: string }

  * ##### optional$flags?<!-- -->: string
  * ##### $re: string

### [**](#getRepositoryClass)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L423)getRepositoryClass

* ****getRepositoryClass**\<T>(): [Constructor](https://mikro-orm.io/api/core.md#Constructor)<[EntityRepository](https://mikro-orm.io/api/core/class/EntityRepository.md)\<T>>

- #### Returns [Constructor](https://mikro-orm.io/api/core.md#Constructor)<[EntityRepository](https://mikro-orm.io/api/core/class/EntityRepository.md)\<T>>

### [**](#getSchemaGenerator)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L470)getSchemaGenerator

* ****getSchemaGenerator**(driver, em): [ISchemaGenerator](https://mikro-orm.io/api/core/interface/ISchemaGenerator.md)

- #### Parameters

  * ##### driver: [IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>
  * ##### optionalem: [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>

  #### Returns [ISchemaGenerator](https://mikro-orm.io/api/core/interface/ISchemaGenerator.md)

### [**](#getSchemaHelper)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L82)getSchemaHelper

* ****getSchemaHelper**(): unknown

- #### Returns unknown

### [**](#getSearchJsonPropertyKey)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L367)getSearchJsonPropertyKey

* ****getSearchJsonPropertyKey**(path, type, aliased, value): string

- #### Parameters

  * ##### path: string\[]
  * ##### type: string
  * ##### aliased: boolean
  * ##### optionalvalue: unknown

  #### Returns string

### [**](#getSearchJsonPropertySQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L363)getSearchJsonPropertySQL

* ****getSearchJsonPropertySQL**(path, type, aliased): string

- #### Parameters

  * ##### path: string
  * ##### type: string
  * ##### aliased: boolean

  #### Returns string

### [**](#getSerializedPrimaryKeyField)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L129)getSerializedPrimaryKeyField

* ****getSerializedPrimaryKeyField**(field): string

- Used when serializing via toObject and toJSON methods, allows to use different PK field name (like `id` instead of `_id`)

  ***

  #### Parameters

  * ##### field: string

  #### Returns string

### [**](#getSmallIntTypeDeclarationSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L216)getSmallIntTypeDeclarationSQL

* ****getSmallIntTypeDeclarationSQL**(column): string

- #### Parameters

  * ##### column: { autoincrement?<!-- -->: boolean; length?<!-- -->: number; unsigned?<!-- -->: boolean }
    * ##### optionalautoincrement: boolean
    * ##### optionallength: number
    * ##### optionalunsigned: boolean

  #### Returns string

### [**](#getTextTypeDeclarationSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L244)getTextTypeDeclarationSQL

* ****getTextTypeDeclarationSQL**(\_column): string

- #### Parameters

  * ##### \_column: { length?<!-- -->: number }
    * ##### optionallength: number

  #### Returns string

### [**](#getTimeTypeDeclarationSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L164)getTimeTypeDeclarationSQL

* ****getTimeTypeDeclarationSQL**(length): string

- #### Parameters

  * ##### optionallength: number

  #### Returns string

### [**](#getTimezone)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L557)getTimezone

* ****getTimezone**(): undefined | string

- #### Returns undefined | string

### [**](#getTinyIntTypeDeclarationSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L224)getTinyIntTypeDeclarationSQL

* ****getTinyIntTypeDeclarationSQL**(column): string

- #### Parameters

  * ##### column: { autoincrement?<!-- -->: boolean; length?<!-- -->: number; unsigned?<!-- -->: boolean }
    * ##### optionalautoincrement: boolean
    * ##### optionallength: number
    * ##### optionalunsigned: boolean

  #### Returns string

### [**](#getUuidTypeDeclarationSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L271)getUuidTypeDeclarationSQL

* ****getUuidTypeDeclarationSQL**(column): string

- #### Parameters

  * ##### column: { length?<!-- -->: number }
    * ##### optionallength: number

  #### Returns string

### [**](#getVarcharTypeDeclarationSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L236)getVarcharTypeDeclarationSQL

* ****getVarcharTypeDeclarationSQL**(column): string

- #### Parameters

  * ##### column: { length?<!-- -->: number }
    * ##### optionallength: number

  #### Returns string

### [**](#indexForeignKeys)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L86)indexForeignKeys

* ****indexForeignKeys**(): boolean

- #### Returns boolean

### [**](#isAllowedTopLevelOperator)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L180)isAllowedTopLevelOperator

* ****isAllowedTopLevelOperator**(operator): boolean

- #### Parameters

  * ##### operator: string

  #### Returns boolean

### [**](#isBigIntProperty)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L196)isBigIntProperty

* ****isBigIntProperty**(prop): boolean

- #### Parameters

  * ##### prop: [EntityProperty](https://mikro-orm.io/api/core/interface/EntityProperty.md)\<any, any>

  #### Returns boolean

### [**](#isNumericColumn)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L566)isNumericColumn

* ****isNumericColumn**(mappedType): boolean

- #### Parameters

  * ##### mappedType: [Type](https://mikro-orm.io/api/core/class/Type.md)\<unknown, unknown>

  #### Returns boolean

### [**](#isNumericProperty)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L561)isNumericProperty

* ****isNumericProperty**(prop, ignoreCustomType): boolean

- #### Parameters

  * ##### prop: [EntityProperty](https://mikro-orm.io/api/core/interface/EntityProperty.md)\<any, any>
  * ##### ignoreCustomType: boolean = <!-- -->false

  #### Returns boolean

### [**](#isPopulated)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L590)isPopulated

* ****isPopulated**\<T>(key, populate): boolean

- #### Parameters

  * ##### key: string
  * ##### populate: boolean | [PopulateOptions](https://mikro-orm.io/api/core.md#PopulateOptions)\<T>\[]

  #### Returns boolean

### [**](#isRaw)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L200)isRaw

* ****isRaw**(value): boolean

- #### Parameters

  * ##### value: any

  #### Returns boolean

### [**](#lookupExtensions)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L438)lookupExtensions

* ****lookupExtensions**(orm): void

- Allows registering extensions of the driver automatically (e.g. `SchemaGenerator` extension in SQL drivers).

  ***

  #### Parameters

  * ##### orm: [MikroORM](https://mikro-orm.io/api/core/class/MikroORM.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>, [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>>

  #### Returns void

### [**](#marshallArray)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L343)marshallArray

* ****marshallArray**(values): string

- #### Parameters

  * ##### values: string\[]

  #### Returns string

### [**](#normalizeColumnType)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L283)normalizeColumnType

* ****normalizeColumnType**(type, options): string

- This should be used only to compare types, it can strip some information like the length.

  ***

  #### Parameters

  * ##### type: string
  * ##### options: { length?<!-- -->: number; precision?<!-- -->: number; scale?<!-- -->: number } = <!-- -->{}
    * ##### optionallength: number
    * ##### optionalprecision: number
    * ##### optionalscale: number

  #### Returns string

### [**](#normalizePrimaryKey)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L115)normalizePrimaryKey

* ****normalizePrimaryKey**\<T>(data): T

- Normalizes primary key wrapper to scalar value (e.g. mongodb's ObjectId to string)

  ***

  #### Parameters

  * ##### data: IPrimaryKeyValue | [Primary](https://mikro-orm.io/api/core.md#Primary)\<T>

  #### Returns T

### [**](#parseDate)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L412)parseDate

* ****parseDate**(value): Date

- #### Parameters

  * ##### value: string | number

  #### Returns Date

### [**](#processDateProperty)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L474)processDateProperty

* ****processDateProperty**(value): string | number | Date

- #### Parameters

  * ##### value: unknown

  #### Returns string | number | Date

### [**](#quoteIdentifier)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L478)quoteIdentifier

* ****quoteIdentifier**(id, quote): string

- #### Parameters

  * ##### id: string | { toString: () => string }
  * * ##### toString: () => string
    ##### quote: string = <!-- -->'\`'

  #### Returns string

### [**](#quoteValue)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L482)quoteValue

* ****quoteValue**(value): string

- #### Parameters

  * ##### value: any

  #### Returns string

### [**](#quoteVersionValue)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L184)quoteVersionValue

* ****quoteVersionValue**(value, prop): string | number | Date

- #### Parameters

  * ##### value: number | Date
  * ##### prop: [EntityProperty](https://mikro-orm.io/api/core/interface/EntityProperty.md)\<any, any>

  #### Returns string | number | Date

### [**](#setConfig)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L542)setConfig

* ****setConfig**(config): void

- #### Parameters

  * ##### config: [Configuration](https://mikro-orm.io/api/core/class/Configuration.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>, [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>>

  #### Returns void

### [**](#shouldHaveColumn)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L594)shouldHaveColumn

* ****shouldHaveColumn**\<T>(prop, populate, exclude, includeFormulas, ignoreInlineEmbeddables): boolean

- #### Parameters

  * ##### prop: [EntityProperty](https://mikro-orm.io/api/core/interface/EntityProperty.md)\<T, any>
  * ##### populate: boolean | [PopulateOptions](https://mikro-orm.io/api/core.md#PopulateOptions)\<T>\[]
  * ##### optionalexclude: string\[]
  * ##### includeFormulas: boolean = <!-- -->true
  * ##### ignoreInlineEmbeddables: boolean = <!-- -->true

  #### Returns boolean

### [**](#supportsCreatingFullTextIndex)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L380)supportsCreatingFullTextIndex

* ****supportsCreatingFullTextIndex**(): boolean

- #### Returns boolean

### [**](#supportsCustomPrimaryKeyNames)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L586)supportsCustomPrimaryKeyNames

* ****supportsCustomPrimaryKeyNames**(): boolean

- #### Returns boolean

### [**](#supportsDownMigrations)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L629)supportsDownMigrations

* ****supportsDownMigrations**(): boolean

- Currently not supported due to how knex does complex sqlite diffing (always based on current schema)

  ***

  #### Returns boolean

### [**](#supportsMultipleCascadePaths)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L331)supportsMultipleCascadePaths

* ****supportsMultipleCascadePaths**(): boolean

- #### Returns boolean

### [**](#supportsMultipleStatements)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L335)supportsMultipleStatements

* ****supportsMultipleStatements**(): boolean

- #### Returns boolean

### [**](#supportsNativeEnums)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L78)supportsNativeEnums

* ****supportsNativeEnums**(): boolean

- for postgres native enums

  ***

  #### Returns boolean

### [**](#supportsTransactions)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L53)supportsTransactions

* ****supportsTransactions**(): boolean

- #### Returns boolean

### [**](#supportsUnsigned)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L570)supportsUnsigned

* ****supportsUnsigned**(): boolean

- #### Returns boolean

### [**](#unmarshallArray)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L347)unmarshallArray

* ****unmarshallArray**(value): string\[]

- #### Parameters

  * ##### value: string

  #### Returns string\[]

### [**](#usesBatchInserts)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L97)usesBatchInserts

* ****usesBatchInserts**(): boolean

- Whether or not the driver supports retuning list of created PKs back when multi-inserting

  ***

  #### Returns boolean

### [**](#usesBatchUpdates)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L104)usesBatchUpdates

* ****usesBatchUpdates**(): boolean

- Whether or not the driver supports updating many records at once

  ***

  #### Returns boolean

### [**](#usesCascadeStatement)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L73)usesCascadeStatement

* ****usesCascadeStatement**(): boolean

- #### Returns boolean

### [**](#usesDefaultKeyword)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L108)usesDefaultKeyword

* ****usesDefaultKeyword**(): boolean

- #### Returns boolean

### [**](#usesDifferentSerializedPrimaryKey)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L133)usesDifferentSerializedPrimaryKey

* ****usesDifferentSerializedPrimaryKey**(): boolean

- #### Returns boolean

### [**](#usesImplicitTransactions)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L57)usesImplicitTransactions

* ****usesImplicitTransactions**(): boolean

- #### Returns boolean

### [**](#usesOutputStatement)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L69)usesOutputStatement

* ****usesOutputStatement**(): boolean

- #### Returns boolean

### [**](#usesPivotTable)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L49)usesPivotTable

* ****usesPivotTable**(): boolean

- #### Returns boolean

### [**](#usesReturningStatement)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L65)usesReturningStatement

* ****usesReturningStatement**(): boolean

- #### Returns boolean

### [**](#validateMetadata)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L633)validateMetadata

* ****validateMetadata**(meta): void

- #### Parameters

  * ##### meta: [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<any>

  #### Returns void
