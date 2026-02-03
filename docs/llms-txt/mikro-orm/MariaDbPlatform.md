# Source: https://mikro-orm.io/api/mariadb/class/MariaDbPlatform.md

# MariaDbPlatform<!-- -->

### Hierarchy

* [MySqlPlatform](https://mikro-orm.io/api/knex/class/MySqlPlatform.md)
  * *MariaDbPlatform*

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
* [**getBeginTransactionSQL](#getBeginTransactionSQL)
* [**getBigIntTypeDeclarationSQL](#getBigIntTypeDeclarationSQL)
* [**getBlobDeclarationSQL](#getBlobDeclarationSQL)
* [**getBooleanTypeDeclarationSQL](#getBooleanTypeDeclarationSQL)
* [**getCharTypeDeclarationSQL](#getCharTypeDeclarationSQL)
* [**getCommitTransactionSQL](#getCommitTransactionSQL)
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
* [**getReleaseSavepointSQL](#getReleaseSavepointSQL)
* [**getRepositoryClass](#getRepositoryClass)
* [**getRollbackToSavepointSQL](#getRollbackToSavepointSQL)
* [**getRollbackTransactionSQL](#getRollbackTransactionSQL)
* [**getSavepointSQL](#getSavepointSQL)
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
* [**supportsSchemas](#supportsSchemas)
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

* ****new MariaDbPlatform**(): [MariaDbPlatform](https://mikro-orm.io/api/mariadb/class/MariaDbPlatform.md)

- Inherited from MySqlPlatform.constructor

  #### Returns [MariaDbPlatform](https://mikro-orm.io/api/mariadb/class/MariaDbPlatform.md)

## Methods<!-- -->[**](#Methods)

### [**](#allowsComparingTuples)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L192)inheritedallowsComparingTuples

* ****allowsComparingTuples**(): boolean

- Inherited from MySqlPlatform.allowsComparingTuples

  #### Returns boolean

### [**](#allowsMultiInsert)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L90)inheritedallowsMultiInsert

* ****allowsMultiInsert**(): boolean

- Inherited from MySqlPlatform.allowsMultiInsert

  #### Returns boolean

### [**](#cloneEmbeddable)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L534)inheritedcloneEmbeddable

* ****cloneEmbeddable**\<T>(data): T

- Inherited from MySqlPlatform.cloneEmbeddable

  #### Parameters

  * ##### data: T

  #### Returns T

### [**](#convertDateToJSValue)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L400)inheritedconvertDateToJSValue

* ****convertDateToJSValue**(value): string

- Inherited from MySqlPlatform.convertDateToJSValue

  #### Parameters

  * ##### value: string | Date

  #### Returns string

### [**](#convertIntervalToDatabaseValue)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L408)inheritedconvertIntervalToDatabaseValue

* ****convertIntervalToDatabaseValue**(value): unknown

- Inherited from MySqlPlatform.convertIntervalToDatabaseValue

  #### Parameters

  * ##### value: unknown

  #### Returns unknown

### [**](#convertIntervalToJSValue)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L404)inheritedconvertIntervalToJSValue

* ****convertIntervalToJSValue**(value): unknown

- Inherited from MySqlPlatform.convertIntervalToJSValue

  #### Parameters

  * ##### value: string

  #### Returns unknown

### [**](#convertJsonToDatabaseValue)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/mariadb/src/MariaDbPlatform.ts#L14)convertJsonToDatabaseValue

* ****convertJsonToDatabaseValue**(value, context): unknown

- Overrides MySqlPlatform.convertJsonToDatabaseValue

  #### Parameters

  * ##### value: unknown
  * ##### optionalcontext: [TransformContext](https://mikro-orm.io/api/core/interface/TransformContext.md)

  #### Returns unknown

### [**](#convertJsonToJSValue)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L396)inheritedconvertJsonToJSValue

* ****convertJsonToJSValue**(value, context): unknown

- Inherited from MySqlPlatform.convertJsonToJSValue

  #### Parameters

  * ##### value: unknown
  * ##### optionalcontext: [TransformContext](https://mikro-orm.io/api/core/interface/TransformContext.md)

  #### Returns unknown

### [**](#convertsJsonAutomatically)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L388)inheritedconvertsJsonAutomatically

* ****convertsJsonAutomatically**(): boolean

- Inherited from MySqlPlatform.convertsJsonAutomatically

  #### Returns boolean

### [**](#denormalizePrimaryKey)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L122)inheriteddenormalizePrimaryKey

* ****denormalizePrimaryKey**(data): IPrimaryKeyValue

- Inherited from MySqlPlatform.denormalizePrimaryKey

  Converts scalar primary key representation to native driver wrapper (e.g. string to mongodb's ObjectId)

  ***

  #### Parameters

  * ##### data: IPrimaryKeyValue

  #### Returns IPrimaryKeyValue

### [**](#escape)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/AbstractSqlPlatform.ts#L81)inheritedescape

* ****escape**(value): string

- Inherited from MySqlPlatform.escape

  #### Parameters

  * ##### value: any

  #### Returns string

### [**](#extractSimpleType)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L276)inheritedextractSimpleType

* ****extractSimpleType**(type): string

- Inherited from MySqlPlatform.extractSimpleType

  #### Parameters

  * ##### type: string

  #### Returns string

### [**](#formatQuery)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L491)inheritedformatQuery

* ****formatQuery**(sql, params): string

- Inherited from MySqlPlatform.formatQuery

  #### Parameters

  * ##### sql: string
  * ##### params: readonly<!-- --> any\[]

  #### Returns string

### [**](#generateCustomOrder)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/AbstractSqlPlatform.ts#L121)inheritedgenerateCustomOrder

* ****generateCustomOrder**(escapedColumn, values): string

- Inherited from MySqlPlatform.generateCustomOrder

  Generates a custom order by statement given a set of in order values, eg. ORDER BY (CASE WHEN priority = 'low' THEN 1 WHEN priority = 'medium' THEN 2 ELSE NULL END)

  ***

  #### Parameters

  * ##### escapedColumn: string
  * ##### values: unknown\[]

  #### Returns string

### [**](#getArrayDeclarationSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L339)inheritedgetArrayDeclarationSQL

* ****getArrayDeclarationSQL**(): string

- Inherited from MySqlPlatform.getArrayDeclarationSQL

  #### Returns string

### [**](#getBeginTransactionSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/dialects/mysql/MySqlPlatform.ts#L32)inheritedgetBeginTransactionSQL

* ****getBeginTransactionSQL**(options): string\[]

- Inherited from MySqlPlatform.getBeginTransactionSQL

  #### Parameters

  * ##### optionaloptions: { isolationLevel?<!-- -->: [IsolationLevel](https://mikro-orm.io/api/core/enum/IsolationLevel.md); readOnly?<!-- -->: boolean }
    * ##### optionalisolationLevel: [IsolationLevel](https://mikro-orm.io/api/core/enum/IsolationLevel.md)
    * ##### optionalreadOnly: boolean

  #### Returns string\[]

### [**](#getBigIntTypeDeclarationSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L228)inheritedgetBigIntTypeDeclarationSQL

* ****getBigIntTypeDeclarationSQL**(column): string

- Inherited from MySqlPlatform.getBigIntTypeDeclarationSQL

  #### Parameters

  * ##### column: { autoincrement?<!-- -->: boolean; length?<!-- -->: number; unsigned?<!-- -->: boolean }
    * ##### optionalautoincrement: boolean
    * ##### optionallength: number
    * ##### optionalunsigned: boolean

  #### Returns string

### [**](#getBlobDeclarationSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L355)inheritedgetBlobDeclarationSQL

* ****getBlobDeclarationSQL**(): string

- Inherited from MySqlPlatform.getBlobDeclarationSQL

  #### Returns string

### [**](#getBooleanTypeDeclarationSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/dialects/mysql/MySqlPlatform.ts#L72)inheritedgetBooleanTypeDeclarationSQL

* ****getBooleanTypeDeclarationSQL**(): string

- Inherited from MySqlPlatform.getBooleanTypeDeclarationSQL

  #### Returns string

### [**](#getCharTypeDeclarationSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L232)inheritedgetCharTypeDeclarationSQL

* ****getCharTypeDeclarationSQL**(column): string

- Inherited from MySqlPlatform.getCharTypeDeclarationSQL

  #### Parameters

  * ##### column: { length?<!-- -->: number }
    * ##### optionallength: number

  #### Returns string

### [**](#getCommitTransactionSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/AbstractSqlPlatform.ts#L45)inheritedgetCommitTransactionSQL

* ****getCommitTransactionSQL**(): string

- Inherited from MySqlPlatform.getCommitTransactionSQL

  #### Returns string

### [**](#getConfig)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L553)inheritedgetConfig

* ****getConfig**(): [Configuration](https://mikro-orm.io/api/core/class/Configuration.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>, [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>>

- Inherited from MySqlPlatform.getConfig

  #### Returns [Configuration](https://mikro-orm.io/api/core/class/Configuration.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>, [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>>

### [**](#getCurrentTimestampSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L140)inheritedgetCurrentTimestampSQL

* ****getCurrentTimestampSQL**(length): string

- Inherited from MySqlPlatform.getCurrentTimestampSQL

  Returns the SQL specific for the platform to get the current timestamp

  ***

  #### Parameters

  * ##### optionallength: number

  #### Returns string

### [**](#getDateTimeTypeDeclarationSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L144)inheritedgetDateTimeTypeDeclarationSQL

* ****getDateTimeTypeDeclarationSQL**(column): string

- Inherited from MySqlPlatform.getDateTimeTypeDeclarationSQL

  #### Parameters

  * ##### column: { length?<!-- -->: number }
    * ##### optionallength: number

  #### Returns string

### [**](#getDateTypeDeclarationSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L160)inheritedgetDateTypeDeclarationSQL

* ****getDateTypeDeclarationSQL**(length): string

- Inherited from MySqlPlatform.getDateTypeDeclarationSQL

  #### Parameters

  * ##### optionallength: number

  #### Returns string

### [**](#getDecimalTypeDeclarationSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L264)inheritedgetDecimalTypeDeclarationSQL

* ****getDecimalTypeDeclarationSQL**(column): string

- Inherited from MySqlPlatform.getDecimalTypeDeclarationSQL

  #### Parameters

  * ##### column: { precision?<!-- -->: number; scale?<!-- -->: number }
    * ##### optionalprecision: number
    * ##### optionalscale: number

  #### Returns string

### [**](#getDefaultCharLength)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L156)inheritedgetDefaultCharLength

* ****getDefaultCharLength**(): number

- Inherited from MySqlPlatform.getDefaultCharLength

  #### Returns number

### [**](#getDefaultCharset)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/mariadb/src/MariaDbPlatform.ts#L10)getDefaultCharset

* ****getDefaultCharset**(): string

- Overrides MySqlPlatform.getDefaultCharset

  #### Returns string

### [**](#getDefaultDateTimeLength)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L148)inheritedgetDefaultDateTimeLength

* ****getDefaultDateTimeLength**(): number

- Inherited from MySqlPlatform.getDefaultDateTimeLength

  #### Returns number

### [**](#getDefaultMappedType)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/dialects/mysql/MySqlPlatform.ts#L86)inheritedgetDefaultMappedType

* ****getDefaultMappedType**(type): [Type](https://mikro-orm.io/api/core/class/Type.md)\<unknown, unknown>

- Inherited from MySqlPlatform.getDefaultMappedType

  #### Parameters

  * ##### type: string

  #### Returns [Type](https://mikro-orm.io/api/core/class/Type.md)\<unknown, unknown>

### [**](#getDefaultPrimaryName)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/dialects/mysql/MySqlPlatform.ts#L121)inheritedgetDefaultPrimaryName

* ****getDefaultPrimaryName**(tableName, columns): string

- Inherited from MySqlPlatform.getDefaultPrimaryName

  #### Parameters

  * ##### tableName: string
  * ##### columns: string\[]

  #### Returns string

### [**](#getDefaultSchemaName)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L204)inheritedgetDefaultSchemaName

* ****getDefaultSchemaName**(): undefined | string

- Inherited from MySqlPlatform.getDefaultSchemaName

  #### Returns undefined | string

### [**](#getDefaultVarcharLength)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L152)inheritedgetDefaultVarcharLength

* ****getDefaultVarcharLength**(): number

- Inherited from MySqlPlatform.getDefaultVarcharLength

  #### Returns number

### [**](#getDefaultVersionLength)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L188)inheritedgetDefaultVersionLength

* ****getDefaultVersionLength**(): number

- Inherited from MySqlPlatform.getDefaultVersionLength

  #### Returns number

### [**](#getDoubleDeclarationSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L260)inheritedgetDoubleDeclarationSQL

* ****getDoubleDeclarationSQL**(): string

- Inherited from MySqlPlatform.getDoubleDeclarationSQL

  #### Returns string

### [**](#getEnumTypeDeclarationSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L248)inheritedgetEnumTypeDeclarationSQL

* ****getEnumTypeDeclarationSQL**(column): string

- Inherited from MySqlPlatform.getEnumTypeDeclarationSQL

  #### Parameters

  * ##### column: { autoincrement?<!-- -->: boolean; fieldNames: string\[]; items?<!-- -->: unknown\[]; length?<!-- -->: number; unsigned?<!-- -->: boolean }
    * ##### optionalautoincrement: boolean
    * ##### fieldNames: string\[]
    * ##### optionalitems: unknown\[]
    * ##### optionallength: number
    * ##### optionalunsigned: boolean

  #### Returns string

### [**](#getExceptionConverter)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L431)inheritedgetExceptionConverter

* ****getExceptionConverter**(): [ExceptionConverter](https://mikro-orm.io/api/core/class/ExceptionConverter.md)

- Inherited from MySqlPlatform.getExceptionConverter

  #### Returns [ExceptionConverter](https://mikro-orm.io/api/core/class/ExceptionConverter.md)

### [**](#getExtension)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L447)inheritedgetExtension

* ****getExtension**\<T>(extensionName, extensionKey, moduleName, em): T

- Inherited from MySqlPlatform.getExtension

  #### Parameters

  * ##### extensionName: string
  * ##### extensionKey: string
  * ##### moduleName: string
  * ##### em: [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>

  #### Returns T

### [**](#getFloatDeclarationSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L256)inheritedgetFloatDeclarationSQL

* ****getFloatDeclarationSQL**(): string

- Inherited from MySqlPlatform.getFloatDeclarationSQL

  #### Returns string

### [**](#getFullTextIndexExpression)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/dialects/mysql/MySqlPlatform.ts#L133)inheritedgetFullTextIndexExpression

* ****getFullTextIndexExpression**(indexName, schemaName, tableName, columns): string

- Inherited from MySqlPlatform.getFullTextIndexExpression

  #### Parameters

  * ##### indexName: string
  * ##### schemaName: undefined | string
  * ##### tableName: string
  * ##### columns: [SimpleColumnMeta](https://mikro-orm.io/api/core/interface/SimpleColumnMeta.md)\[]

  #### Returns string

### [**](#getFullTextWhereClause)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/dialects/mysql/MySqlPlatform.ts#L129)inheritedgetFullTextWhereClause

* ****getFullTextWhereClause**(): string

- Inherited from MySqlPlatform.getFullTextWhereClause

  #### Returns string

### [**](#getIndexName)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/dialects/mysql/MySqlPlatform.ts#L106)inheritedgetIndexName

* ****getIndexName**(tableName, columns, type): string

- Inherited from MySqlPlatform.getIndexName

  Returns the default name of index for the given columns cannot go past 64 character length for identifiers in MySQL

  ***

  #### Parameters

  * ##### tableName: string
  * ##### columns: string\[]
  * ##### type: primary | index | unique | foreign | sequence

  #### Returns string

### [**](#getIntegerTypeDeclarationSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L212)inheritedgetIntegerTypeDeclarationSQL

* ****getIntegerTypeDeclarationSQL**(column): string

- Inherited from MySqlPlatform.getIntegerTypeDeclarationSQL

  #### Parameters

  * ##### column: { autoincrement?<!-- -->: boolean; length?<!-- -->: number; unsigned?<!-- -->: boolean }
    * ##### optionalautoincrement: boolean
    * ##### optionallength: number
    * ##### optionalunsigned: boolean

  #### Returns string

### [**](#getIntervalTypeDeclarationSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L240)inheritedgetIntervalTypeDeclarationSQL

* ****getIntervalTypeDeclarationSQL**(column): string

- Inherited from MySqlPlatform.getIntervalTypeDeclarationSQL

  #### Parameters

  * ##### column: { length?<!-- -->: number }
    * ##### optionallength: number

  #### Returns string

### [**](#getJsonDeclarationSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L359)inheritedgetJsonDeclarationSQL

* ****getJsonDeclarationSQL**(): string

- Inherited from MySqlPlatform.getJsonDeclarationSQL

  #### Returns string

### [**](#getJsonIndexDefinition)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/dialects/mysql/MySqlPlatform.ts#L60)inheritedgetJsonIndexDefinition

* ****getJsonIndexDefinition**(index): string\[]

- Inherited from MySqlPlatform.getJsonIndexDefinition

  #### Parameters

  * ##### index: [IndexDef](https://mikro-orm.io/api/knex/interface/IndexDef.md)

  #### Returns string\[]

### [**](#getMappedType)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L287)inheritedgetMappedType

* ****getMappedType**(type): [Type](https://mikro-orm.io/api/core/class/Type.md)\<unknown, unknown>

- Inherited from MySqlPlatform.getMappedType

  #### Parameters

  * ##### type: string

  #### Returns [Type](https://mikro-orm.io/api/core/class/Type.md)\<unknown, unknown>

### [**](#getMediumIntTypeDeclarationSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L220)inheritedgetMediumIntTypeDeclarationSQL

* ****getMediumIntTypeDeclarationSQL**(column): string

- Inherited from MySqlPlatform.getMediumIntTypeDeclarationSQL

  #### Parameters

  * ##### column: { autoincrement?<!-- -->: boolean; length?<!-- -->: number; unsigned?<!-- -->: boolean }
    * ##### optionalautoincrement: boolean
    * ##### optionallength: number
    * ##### optionalunsigned: boolean

  #### Returns string

### [**](#getNamingStrategy)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L61)inheritedgetNamingStrategy

* ****getNamingStrategy**(): new () => [NamingStrategy](https://mikro-orm.io/api/core/interface/NamingStrategy.md)

- Inherited from MySqlPlatform.getNamingStrategy

  #### Returns new () => [NamingStrategy](https://mikro-orm.io/api/core/interface/NamingStrategy.md)

  * * **new (): [NamingStrategy](https://mikro-orm.io/api/core/interface/NamingStrategy.md)

    - #### Returns [NamingStrategy](https://mikro-orm.io/api/core/interface/NamingStrategy.md)

### [**](#getRegExpOperator)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L168)inheritedgetRegExpOperator

* ****getRegExpOperator**(val, flags): string

- Inherited from MySqlPlatform.getRegExpOperator

  #### Parameters

  * ##### optionalval: unknown
  * ##### optionalflags: string

  #### Returns string

### [**](#getRegExpValue)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L172)inheritedgetRegExpValue

* ****getRegExpValue**(val): { $flags?
  <!-- -->
  : string; $re: string }

- Inherited from MySqlPlatform.getRegExpValue

  #### Parameters

  * ##### val: RegExp

  #### Returns { $flags?<!-- -->: string; $re: string }

  * ##### optional$flags?<!-- -->: string
  * ##### $re: string

### [**](#getReleaseSavepointSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/AbstractSqlPlatform.ts#L61)inheritedgetReleaseSavepointSQL

* ****getReleaseSavepointSQL**(savepointName): string

- Inherited from MySqlPlatform.getReleaseSavepointSQL

  #### Parameters

  * ##### savepointName: string

  #### Returns string

### [**](#getRepositoryClass)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/AbstractSqlPlatform.ts#L19)inheritedgetRepositoryClass

* ****getRepositoryClass**\<T>(): [Constructor](https://mikro-orm.io/api/core.md#Constructor)<[EntityRepository](https://mikro-orm.io/api/core/class/EntityRepository.md)\<T>>

- Inherited from MySqlPlatform.getRepositoryClass

  #### Returns [Constructor](https://mikro-orm.io/api/core.md#Constructor)<[EntityRepository](https://mikro-orm.io/api/core/class/EntityRepository.md)\<T>>

### [**](#getRollbackToSavepointSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/AbstractSqlPlatform.ts#L57)inheritedgetRollbackToSavepointSQL

* ****getRollbackToSavepointSQL**(savepointName): string

- Inherited from MySqlPlatform.getRollbackToSavepointSQL

  #### Parameters

  * ##### savepointName: string

  #### Returns string

### [**](#getRollbackTransactionSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/AbstractSqlPlatform.ts#L49)inheritedgetRollbackTransactionSQL

* ****getRollbackTransactionSQL**(): string

- Inherited from MySqlPlatform.getRollbackTransactionSQL

  #### Returns string

### [**](#getSavepointSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/AbstractSqlPlatform.ts#L53)inheritedgetSavepointSQL

* ****getSavepointSQL**(savepointName): string

- Inherited from MySqlPlatform.getSavepointSQL

  #### Parameters

  * ##### savepointName: string

  #### Returns string

### [**](#getSchemaGenerator)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/AbstractSqlPlatform.ts#L33)inheritedgetSchemaGenerator

* ****getSchemaGenerator**(driver, em): [SqlSchemaGenerator](https://mikro-orm.io/api/knex/class/SqlSchemaGenerator.md)

- Inherited from MySqlPlatform.getSchemaGenerator

  #### Parameters

  * ##### driver: [IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>
  * ##### optionalem: [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>

  #### Returns [SqlSchemaGenerator](https://mikro-orm.io/api/knex/class/SqlSchemaGenerator.md)

### [**](#getSchemaHelper)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/AbstractSqlPlatform.ts#L23)inheritedgetSchemaHelper

* ****getSchemaHelper**(): undefined | [SchemaHelper](https://mikro-orm.io/api/knex/class/SchemaHelper.md)

- Inherited from MySqlPlatform.getSchemaHelper

  #### Returns undefined | [SchemaHelper](https://mikro-orm.io/api/knex/class/SchemaHelper.md)

### [**](#getSearchJsonPropertyKey)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/AbstractSqlPlatform.ts#L89)inheritedgetSearchJsonPropertyKey

* ****getSearchJsonPropertyKey**(path, type, aliased, value): string

- Inherited from MySqlPlatform.getSearchJsonPropertyKey

  #### Parameters

  * ##### path: string\[]
  * ##### type: string
  * ##### aliased: boolean
  * ##### optionalvalue: unknown

  #### Returns string

### [**](#getSearchJsonPropertySQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/AbstractSqlPlatform.ts#L85)inheritedgetSearchJsonPropertySQL

* ****getSearchJsonPropertySQL**(path, type, aliased): string

- Inherited from MySqlPlatform.getSearchJsonPropertySQL

  #### Parameters

  * ##### path: string
  * ##### type: string
  * ##### aliased: boolean

  #### Returns string

### [**](#getSerializedPrimaryKeyField)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L129)inheritedgetSerializedPrimaryKeyField

* ****getSerializedPrimaryKeyField**(field): string

- Inherited from MySqlPlatform.getSerializedPrimaryKeyField

  Used when serializing via toObject and toJSON methods, allows to use different PK field name (like `id` instead of `_id`)

  ***

  #### Parameters

  * ##### field: string

  #### Returns string

### [**](#getSmallIntTypeDeclarationSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L216)inheritedgetSmallIntTypeDeclarationSQL

* ****getSmallIntTypeDeclarationSQL**(column): string

- Inherited from MySqlPlatform.getSmallIntTypeDeclarationSQL

  #### Parameters

  * ##### column: { autoincrement?<!-- -->: boolean; length?<!-- -->: number; unsigned?<!-- -->: boolean }
    * ##### optionalautoincrement: boolean
    * ##### optionallength: number
    * ##### optionalunsigned: boolean

  #### Returns string

### [**](#getTextTypeDeclarationSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L244)inheritedgetTextTypeDeclarationSQL

* ****getTextTypeDeclarationSQL**(\_column): string

- Inherited from MySqlPlatform.getTextTypeDeclarationSQL

  #### Parameters

  * ##### \_column: { length?<!-- -->: number }
    * ##### optionallength: number

  #### Returns string

### [**](#getTimeTypeDeclarationSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L164)inheritedgetTimeTypeDeclarationSQL

* ****getTimeTypeDeclarationSQL**(length): string

- Inherited from MySqlPlatform.getTimeTypeDeclarationSQL

  #### Parameters

  * ##### optionallength: number

  #### Returns string

### [**](#getTimezone)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L557)inheritedgetTimezone

* ****getTimezone**(): undefined | string

- Inherited from MySqlPlatform.getTimezone

  #### Returns undefined | string

### [**](#getTinyIntTypeDeclarationSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L224)inheritedgetTinyIntTypeDeclarationSQL

* ****getTinyIntTypeDeclarationSQL**(column): string

- Inherited from MySqlPlatform.getTinyIntTypeDeclarationSQL

  #### Parameters

  * ##### column: { autoincrement?<!-- -->: boolean; length?<!-- -->: number; unsigned?<!-- -->: boolean }
    * ##### optionalautoincrement: boolean
    * ##### optionallength: number
    * ##### optionalunsigned: boolean

  #### Returns string

### [**](#getUuidTypeDeclarationSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L271)inheritedgetUuidTypeDeclarationSQL

* ****getUuidTypeDeclarationSQL**(column): string

- Inherited from MySqlPlatform.getUuidTypeDeclarationSQL

  #### Parameters

  * ##### column: { length?<!-- -->: number }
    * ##### optionallength: number

  #### Returns string

### [**](#getVarcharTypeDeclarationSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L236)inheritedgetVarcharTypeDeclarationSQL

* ****getVarcharTypeDeclarationSQL**(column): string

- Inherited from MySqlPlatform.getVarcharTypeDeclarationSQL

  #### Parameters

  * ##### column: { length?<!-- -->: number }
    * ##### optionallength: number

  #### Returns string

### [**](#indexForeignKeys)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/AbstractSqlPlatform.ts#L15)inheritedindexForeignKeys

* ****indexForeignKeys**(): boolean

- Inherited from MySqlPlatform.indexForeignKeys

  #### Returns boolean

### [**](#isAllowedTopLevelOperator)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L180)inheritedisAllowedTopLevelOperator

* ****isAllowedTopLevelOperator**(operator): boolean

- Inherited from MySqlPlatform.isAllowedTopLevelOperator

  #### Parameters

  * ##### operator: string

  #### Returns boolean

### [**](#isBigIntProperty)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L196)inheritedisBigIntProperty

* ****isBigIntProperty**(prop): boolean

- Inherited from MySqlPlatform.isBigIntProperty

  #### Parameters

  * ##### prop: [EntityProperty](https://mikro-orm.io/api/core/interface/EntityProperty.md)\<any, any>

  #### Returns boolean

### [**](#isNumericColumn)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/dialects/mysql/MySqlPlatform.ts#L94)inheritedisNumericColumn

* ****isNumericColumn**(mappedType): boolean

- Inherited from MySqlPlatform.isNumericColumn

  #### Parameters

  * ##### mappedType: [Type](https://mikro-orm.io/api/core/class/Type.md)\<unknown, unknown>

  #### Returns boolean

### [**](#isNumericProperty)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L561)inheritedisNumericProperty

* ****isNumericProperty**(prop, ignoreCustomType): boolean

- Inherited from MySqlPlatform.isNumericProperty

  #### Parameters

  * ##### prop: [EntityProperty](https://mikro-orm.io/api/core/interface/EntityProperty.md)\<any, any>
  * ##### ignoreCustomType: boolean = <!-- -->false

  #### Returns boolean

### [**](#isPopulated)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L590)inheritedisPopulated

* ****isPopulated**\<T>(key, populate): boolean

- Inherited from MySqlPlatform.isPopulated

  #### Parameters

  * ##### key: string
  * ##### populate: boolean | [PopulateOptions](https://mikro-orm.io/api/core.md#PopulateOptions)\<T>\[]

  #### Returns boolean

### [**](#isRaw)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/AbstractSqlPlatform.ts#L112)inheritedisRaw

* ****isRaw**(value): boolean

- Inherited from MySqlPlatform.isRaw

  #### Parameters

  * ##### value: any

  #### Returns boolean

### [**](#lookupExtensions)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/AbstractSqlPlatform.ts#L28)inheritedlookupExtensions

* ****lookupExtensions**(orm): void

- Inherited from MySqlPlatform.lookupExtensions

  Allows registering extensions of the driver automatically (e.g. `SchemaGenerator` extension in SQL drivers).

  ***

  #### Parameters

  * ##### orm: [MikroORM](https://mikro-orm.io/api/core/class/MikroORM.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>, [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>>

  #### Returns void

### [**](#marshallArray)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L343)inheritedmarshallArray

* ****marshallArray**(values): string

- Inherited from MySqlPlatform.marshallArray

  #### Parameters

  * ##### values: string\[]

  #### Returns string

### [**](#normalizeColumnType)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/dialects/mysql/MySqlPlatform.ts#L76)inheritednormalizeColumnType

* ****normalizeColumnType**(type, options): string

- Inherited from MySqlPlatform.normalizeColumnType

  This should be used only to compare types, it can strip some information like the length.

  ***

  #### Parameters

  * ##### type: string
  * ##### options: { length?<!-- -->: number; precision?<!-- -->: number; scale?<!-- -->: number } = <!-- -->{}
    * ##### optionallength: number
    * ##### optionalprecision: number
    * ##### optionalscale: number

  #### Returns string

### [**](#normalizePrimaryKey)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L115)inheritednormalizePrimaryKey

* ****normalizePrimaryKey**\<T>(data): T

- Inherited from MySqlPlatform.normalizePrimaryKey

  Normalizes primary key wrapper to scalar value (e.g. mongodb's ObjectId to string)

  ***

  #### Parameters

  * ##### data: IPrimaryKeyValue | [Primary](https://mikro-orm.io/api/core.md#Primary)\<T>

  #### Returns T

### [**](#parseDate)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L412)inheritedparseDate

* ****parseDate**(value): Date

- Inherited from MySqlPlatform.parseDate

  #### Parameters

  * ##### value: string | number

  #### Returns Date

### [**](#processDateProperty)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L474)inheritedprocessDateProperty

* ****processDateProperty**(value): string | number | Date

- Inherited from MySqlPlatform.processDateProperty

  #### Parameters

  * ##### value: unknown

  #### Returns string | number | Date

### [**](#quoteIdentifier)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L478)inheritedquoteIdentifier

* ****quoteIdentifier**(id, quote): string

- Inherited from MySqlPlatform.quoteIdentifier

  #### Parameters

  * ##### id: string | { toString: () => string }
  * * ##### toString: () => string
    ##### quote: string = <!-- -->'\`'

  #### Returns string

### [**](#quoteValue)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/AbstractSqlPlatform.ts#L65)inheritedquoteValue

* ****quoteValue**(value): string

- Inherited from MySqlPlatform.quoteValue

  #### Parameters

  * ##### value: any

  #### Returns string

### [**](#quoteVersionValue)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L184)inheritedquoteVersionValue

* ****quoteVersionValue**(value, prop): string | number | Date

- Inherited from MySqlPlatform.quoteVersionValue

  #### Parameters

  * ##### value: number | Date
  * ##### prop: [EntityProperty](https://mikro-orm.io/api/core/interface/EntityProperty.md)\<any, any>

  #### Returns string | number | Date

### [**](#setConfig)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L542)inheritedsetConfig

* ****setConfig**(config): void

- Inherited from MySqlPlatform.setConfig

  #### Parameters

  * ##### config: [Configuration](https://mikro-orm.io/api/core/class/Configuration.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>, [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>>

  #### Returns void

### [**](#shouldHaveColumn)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L594)inheritedshouldHaveColumn

* ****shouldHaveColumn**\<T>(prop, populate, exclude, includeFormulas, ignoreInlineEmbeddables): boolean

- Inherited from MySqlPlatform.shouldHaveColumn

  #### Parameters

  * ##### prop: [EntityProperty](https://mikro-orm.io/api/core/interface/EntityProperty.md)\<T, any>
  * ##### populate: boolean | [PopulateOptions](https://mikro-orm.io/api/core.md#PopulateOptions)\<T>\[]
  * ##### optionalexclude: string\[]
  * ##### includeFormulas: boolean = <!-- -->true
  * ##### ignoreInlineEmbeddables: boolean = <!-- -->true

  #### Returns boolean

### [**](#supportsCreatingFullTextIndex)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/dialects/mysql/MySqlPlatform.ts#L125)inheritedsupportsCreatingFullTextIndex

* ****supportsCreatingFullTextIndex**(): boolean

- Inherited from MySqlPlatform.supportsCreatingFullTextIndex

  #### Returns boolean

### [**](#supportsCustomPrimaryKeyNames)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L586)inheritedsupportsCustomPrimaryKeyNames

* ****supportsCustomPrimaryKeyNames**(): boolean

- Inherited from MySqlPlatform.supportsCustomPrimaryKeyNames

  #### Returns boolean

### [**](#supportsDownMigrations)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L629)inheritedsupportsDownMigrations

* ****supportsDownMigrations**(): boolean

- Inherited from MySqlPlatform.supportsDownMigrations

  Currently not supported due to how knex does complex sqlite diffing (always based on current schema)

  ***

  #### Returns boolean

### [**](#supportsMultipleCascadePaths)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L331)inheritedsupportsMultipleCascadePaths

* ****supportsMultipleCascadePaths**(): boolean

- Inherited from MySqlPlatform.supportsMultipleCascadePaths

  #### Returns boolean

### [**](#supportsMultipleStatements)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L335)inheritedsupportsMultipleStatements

* ****supportsMultipleStatements**(): boolean

- Inherited from MySqlPlatform.supportsMultipleStatements

  #### Returns boolean

### [**](#supportsNativeEnums)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L78)inheritedsupportsNativeEnums

* ****supportsNativeEnums**(): boolean

- Inherited from MySqlPlatform.supportsNativeEnums

  for postgres native enums

  ***

  #### Returns boolean

### [**](#supportsSchemas)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/AbstractSqlPlatform.ts#L116)inheritedsupportsSchemas

* ****supportsSchemas**(): boolean

- Inherited from MySqlPlatform.supportsSchemas

  #### Returns boolean

### [**](#supportsTransactions)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L53)inheritedsupportsTransactions

* ****supportsTransactions**(): boolean

- Inherited from MySqlPlatform.supportsTransactions

  #### Returns boolean

### [**](#supportsUnsigned)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/dialects/mysql/MySqlPlatform.ts#L98)inheritedsupportsUnsigned

* ****supportsUnsigned**(): boolean

- Inherited from MySqlPlatform.supportsUnsigned

  #### Returns boolean

### [**](#unmarshallArray)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L347)inheritedunmarshallArray

* ****unmarshallArray**(value): string\[]

- Inherited from MySqlPlatform.unmarshallArray

  #### Parameters

  * ##### value: string

  #### Returns string\[]

### [**](#usesBatchInserts)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L97)inheritedusesBatchInserts

* ****usesBatchInserts**(): boolean

- Inherited from MySqlPlatform.usesBatchInserts

  Whether or not the driver supports retuning list of created PKs back when multi-inserting

  ***

  #### Returns boolean

### [**](#usesBatchUpdates)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L104)inheritedusesBatchUpdates

* ****usesBatchUpdates**(): boolean

- Inherited from MySqlPlatform.usesBatchUpdates

  Whether or not the driver supports updating many records at once

  ***

  #### Returns boolean

### [**](#usesCascadeStatement)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L73)inheritedusesCascadeStatement

* ****usesCascadeStatement**(): boolean

- Inherited from MySqlPlatform.usesCascadeStatement

  #### Returns boolean

### [**](#usesDefaultKeyword)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L108)inheritedusesDefaultKeyword

* ****usesDefaultKeyword**(): boolean

- Inherited from MySqlPlatform.usesDefaultKeyword

  #### Returns boolean

### [**](#usesDifferentSerializedPrimaryKey)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L133)inheritedusesDifferentSerializedPrimaryKey

* ****usesDifferentSerializedPrimaryKey**(): boolean

- Inherited from MySqlPlatform.usesDifferentSerializedPrimaryKey

  #### Returns boolean

### [**](#usesImplicitTransactions)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L57)inheritedusesImplicitTransactions

* ****usesImplicitTransactions**(): boolean

- Inherited from MySqlPlatform.usesImplicitTransactions

  #### Returns boolean

### [**](#usesOutputStatement)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L69)inheritedusesOutputStatement

* ****usesOutputStatement**(): boolean

- Inherited from MySqlPlatform.usesOutputStatement

  #### Returns boolean

### [**](#usesPivotTable)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/AbstractSqlPlatform.ts#L11)inheritedusesPivotTable

* ****usesPivotTable**(): boolean

- Inherited from MySqlPlatform.usesPivotTable

  #### Returns boolean

### [**](#usesReturningStatement)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L65)inheritedusesReturningStatement

* ****usesReturningStatement**(): boolean

- Inherited from MySqlPlatform.usesReturningStatement

  #### Returns boolean

### [**](#validateMetadata)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L633)inheritedvalidateMetadata

* ****validateMetadata**(meta): void

- Inherited from MySqlPlatform.validateMetadata

  #### Parameters

  * ##### meta: [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<any>

  #### Returns void
