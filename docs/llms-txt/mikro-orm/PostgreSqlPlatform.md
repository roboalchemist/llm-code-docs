# Source: https://mikro-orm.io/api/postgresql/class/PostgreSqlPlatform.md

# PostgreSqlPlatform<!-- -->

### Hierarchy

* [AbstractSqlPlatform](https://mikro-orm.io/api/knex/class/AbstractSqlPlatform.md)
  * *PostgreSqlPlatform*

## Index[**](#Index)

### Constructors

* [**constructor](#constructor)

### Methods

* [**allowsComparingTuples](#allowsComparingTuples)
* [**allowsMultiInsert](#allowsMultiInsert)
* [**castColumn](#castColumn)
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

* ****new PostgreSqlPlatform**(): [PostgreSqlPlatform](https://mikro-orm.io/api/postgresql/class/PostgreSqlPlatform.md)

- Inherited from AbstractSqlPlatform.constructor

  #### Returns [PostgreSqlPlatform](https://mikro-orm.io/api/postgresql/class/PostgreSqlPlatform.md)

## Methods<!-- -->[**](#Methods)

### [**](#allowsComparingTuples)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L192)inheritedallowsComparingTuples

* ****allowsComparingTuples**(): boolean

- Inherited from AbstractSqlPlatform.allowsComparingTuples

  #### Returns boolean

### [**](#allowsMultiInsert)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L90)inheritedallowsMultiInsert

* ****allowsMultiInsert**(): boolean

- Inherited from AbstractSqlPlatform.allowsMultiInsert

  #### Returns boolean

### [**](#castColumn)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/postgresql/src/PostgreSqlPlatform.ts#L467)castColumn

* ****castColumn**(prop): string

- Overrides AbstractSqlPlatform.castColumn

  * **@inheritDoc**

  ***

  #### Parameters

  * ##### optionalprop: { columnTypes?<!-- -->: string\[] }
    * ##### optionalcolumnTypes: string\[]

  #### Returns string

### [**](#cloneEmbeddable)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L534)inheritedcloneEmbeddable

* ****cloneEmbeddable**\<T>(data): T

- Inherited from AbstractSqlPlatform.cloneEmbeddable

  #### Parameters

  * ##### data: T

  #### Returns T

### [**](#convertDateToJSValue)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L400)inheritedconvertDateToJSValue

* ****convertDateToJSValue**(value): string

- Inherited from AbstractSqlPlatform.convertDateToJSValue

  #### Parameters

  * ##### value: string | Date

  #### Returns string

### [**](#convertIntervalToDatabaseValue)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/postgresql/src/PostgreSqlPlatform.ts#L66)convertIntervalToDatabaseValue

* ****convertIntervalToDatabaseValue**(value): unknown

- Overrides AbstractSqlPlatform.convertIntervalToDatabaseValue

  #### Parameters

  * ##### value: IPostgresInterval

  #### Returns unknown

### [**](#convertIntervalToJSValue)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/postgresql/src/PostgreSqlPlatform.ts#L62)convertIntervalToJSValue

* ****convertIntervalToJSValue**(value): unknown

- Overrides AbstractSqlPlatform.convertIntervalToJSValue

  #### Parameters

  * ##### value: string

  #### Returns unknown

### [**](#convertJsonToDatabaseValue)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L392)inheritedconvertJsonToDatabaseValue

* ****convertJsonToDatabaseValue**(value, context): unknown

- Inherited from AbstractSqlPlatform.convertJsonToDatabaseValue

  #### Parameters

  * ##### value: unknown
  * ##### optionalcontext: [TransformContext](https://mikro-orm.io/api/core/interface/TransformContext.md)

  #### Returns unknown

### [**](#convertJsonToJSValue)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L396)inheritedconvertJsonToJSValue

* ****convertJsonToJSValue**(value, context): unknown

- Inherited from AbstractSqlPlatform.convertJsonToJSValue

  #### Parameters

  * ##### value: unknown
  * ##### optionalcontext: [TransformContext](https://mikro-orm.io/api/core/interface/TransformContext.md)

  #### Returns unknown

### [**](#convertsJsonAutomatically)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L388)inheritedconvertsJsonAutomatically

* ****convertsJsonAutomatically**(): boolean

- Inherited from AbstractSqlPlatform.convertsJsonAutomatically

  #### Returns boolean

### [**](#denormalizePrimaryKey)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L122)inheriteddenormalizePrimaryKey

* ****denormalizePrimaryKey**(data): IPrimaryKeyValue

- Inherited from AbstractSqlPlatform.denormalizePrimaryKey

  Converts scalar primary key representation to native driver wrapper (e.g. string to mongodb's ObjectId)

  ***

  #### Parameters

  * ##### data: IPrimaryKeyValue

  #### Returns IPrimaryKeyValue

### [**](#escape)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/postgresql/src/PostgreSqlPlatform.ts#L339)escape

* ****escape**(value): string

- Overrides AbstractSqlPlatform.escape

  #### Parameters

  * ##### value: any

  #### Returns string

### [**](#extractSimpleType)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L276)inheritedextractSimpleType

* ****extractSimpleType**(type): string

- Inherited from AbstractSqlPlatform.extractSimpleType

  #### Parameters

  * ##### type: string

  #### Returns string

### [**](#formatQuery)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L491)inheritedformatQuery

* ****formatQuery**(sql, params): string

- Inherited from AbstractSqlPlatform.formatQuery

  #### Parameters

  * ##### sql: string
  * ##### params: readonly<!-- --> any\[]

  #### Returns string

### [**](#generateCustomOrder)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/AbstractSqlPlatform.ts#L121)inheritedgenerateCustomOrder

* ****generateCustomOrder**(escapedColumn, values): string

- Inherited from AbstractSqlPlatform.generateCustomOrder

  Generates a custom order by statement given a set of in order values, eg. ORDER BY (CASE WHEN priority = 'low' THEN 1 WHEN priority = 'medium' THEN 2 ELSE NULL END)

  ***

  #### Parameters

  * ##### escapedColumn: string
  * ##### values: unknown\[]

  #### Returns string

### [**](#getArrayDeclarationSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/postgresql/src/PostgreSqlPlatform.ts#L201)getArrayDeclarationSQL

* ****getArrayDeclarationSQL**(): string

- Overrides AbstractSqlPlatform.getArrayDeclarationSQL

  #### Returns string

### [**](#getBeginTransactionSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/postgresql/src/PostgreSqlPlatform.ts#L230)getBeginTransactionSQL

* ****getBeginTransactionSQL**(options): string\[]

- Overrides AbstractSqlPlatform.getBeginTransactionSQL

  #### Parameters

  * ##### optionaloptions: { isolationLevel?<!-- -->: [IsolationLevel](https://mikro-orm.io/api/core/enum/IsolationLevel.md); readOnly?<!-- -->: boolean }
    * ##### optionalisolationLevel: [IsolationLevel](https://mikro-orm.io/api/core/enum/IsolationLevel.md)
    * ##### optionalreadOnly: boolean

  #### Returns string\[]

### [**](#getBigIntTypeDeclarationSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/postgresql/src/PostgreSqlPlatform.ts#L86)getBigIntTypeDeclarationSQL

* ****getBigIntTypeDeclarationSQL**(column): string

- Overrides AbstractSqlPlatform.getBigIntTypeDeclarationSQL

  #### Parameters

  * ##### column: { autoincrement?<!-- -->: boolean }
    * ##### optionalautoincrement: boolean

  #### Returns string

### [**](#getBlobDeclarationSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/postgresql/src/PostgreSqlPlatform.ts#L283)getBlobDeclarationSQL

* ****getBlobDeclarationSQL**(): string

- Overrides AbstractSqlPlatform.getBlobDeclarationSQL

  #### Returns string

### [**](#getBooleanTypeDeclarationSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L208)inheritedgetBooleanTypeDeclarationSQL

* ****getBooleanTypeDeclarationSQL**(): string

- Inherited from AbstractSqlPlatform.getBooleanTypeDeclarationSQL

  #### Returns string

### [**](#getCharTypeDeclarationSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/postgresql/src/PostgreSqlPlatform.ts#L272)getCharTypeDeclarationSQL

* ****getCharTypeDeclarationSQL**(column): string

- Overrides AbstractSqlPlatform.getCharTypeDeclarationSQL

  #### Parameters

  * ##### column: { length?<!-- -->: number }
    * ##### optionallength: number

  #### Returns string

### [**](#getCommitTransactionSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/AbstractSqlPlatform.ts#L45)inheritedgetCommitTransactionSQL

* ****getCommitTransactionSQL**(): string

- Inherited from AbstractSqlPlatform.getCommitTransactionSQL

  #### Returns string

### [**](#getConfig)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L553)inheritedgetConfig

* ****getConfig**(): [Configuration](https://mikro-orm.io/api/core/class/Configuration.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>, [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>>

- Inherited from AbstractSqlPlatform.getConfig

  #### Returns [Configuration](https://mikro-orm.io/api/core/class/Configuration.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>, [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>>

### [**](#getCurrentTimestampSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/postgresql/src/PostgreSqlPlatform.ts#L49)getCurrentTimestampSQL

* ****getCurrentTimestampSQL**(length): string

- Overrides AbstractSqlPlatform.getCurrentTimestampSQL

  Returns the SQL specific for the platform to get the current timestamp

  ***

  #### Parameters

  * ##### length: number

  #### Returns string

### [**](#getDateTimeTypeDeclarationSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/postgresql/src/PostgreSqlPlatform.ts#L53)getDateTimeTypeDeclarationSQL

* ****getDateTimeTypeDeclarationSQL**(column): string

- Overrides AbstractSqlPlatform.getDateTimeTypeDeclarationSQL

  #### Parameters

  * ##### column: { length?<!-- -->: number }
    * ##### optionallength: number

  #### Returns string

### [**](#getDateTypeDeclarationSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L160)inheritedgetDateTypeDeclarationSQL

* ****getDateTypeDeclarationSQL**(length): string

- Inherited from AbstractSqlPlatform.getDateTypeDeclarationSQL

  #### Parameters

  * ##### optionallength: number

  #### Returns string

### [**](#getDecimalTypeDeclarationSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L264)inheritedgetDecimalTypeDeclarationSQL

* ****getDecimalTypeDeclarationSQL**(column): string

- Inherited from AbstractSqlPlatform.getDecimalTypeDeclarationSQL

  #### Parameters

  * ##### column: { precision?<!-- -->: number; scale?<!-- -->: number }
    * ##### optionalprecision: number
    * ##### optionalscale: number

  #### Returns string

### [**](#getDefaultCharLength)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L156)inheritedgetDefaultCharLength

* ****getDefaultCharLength**(): number

- Inherited from AbstractSqlPlatform.getDefaultCharLength

  #### Returns number

### [**](#getDefaultCharset)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L427)inheritedgetDefaultCharset

* ****getDefaultCharset**(): string

- Inherited from AbstractSqlPlatform.getDefaultCharset

  #### Returns string

### [**](#getDefaultDateTimeLength)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/postgresql/src/PostgreSqlPlatform.ts#L58)getDefaultDateTimeLength

* ****getDefaultDateTimeLength**(): number

- Overrides AbstractSqlPlatform.getDefaultDateTimeLength

  #### Returns number

### [**](#getDefaultMappedType)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/postgresql/src/PostgreSqlPlatform.ts#L404)getDefaultMappedType

* ****getDefaultMappedType**(type): [Type](https://mikro-orm.io/api/core/class/Type.md)\<unknown, unknown>

- Overrides AbstractSqlPlatform.getDefaultMappedType

  #### Parameters

  * ##### type: string

  #### Returns [Type](https://mikro-orm.io/api/core/class/Type.md)\<unknown, unknown>

### [**](#getDefaultPrimaryName)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/postgresql/src/PostgreSqlPlatform.ts#L454)getDefaultPrimaryName

* ****getDefaultPrimaryName**(tableName, columns): string

- Overrides AbstractSqlPlatform.getDefaultPrimaryName

  #### Parameters

  * ##### tableName: string
  * ##### columns: string\[]

  #### Returns string

### [**](#getDefaultSchemaName)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/postgresql/src/PostgreSqlPlatform.ts#L436)getDefaultSchemaName

* ****getDefaultSchemaName**(): undefined | string

- Overrides AbstractSqlPlatform.getDefaultSchemaName

  #### Returns undefined | string

### [**](#getDefaultVarcharLength)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L152)inheritedgetDefaultVarcharLength

* ****getDefaultVarcharLength**(): number

- Inherited from AbstractSqlPlatform.getDefaultVarcharLength

  #### Returns number

### [**](#getDefaultVersionLength)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L188)inheritedgetDefaultVersionLength

* ****getDefaultVersionLength**(): number

- Inherited from AbstractSqlPlatform.getDefaultVersionLength

  #### Returns number

### [**](#getDoubleDeclarationSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/postgresql/src/PostgreSqlPlatform.ts#L209)getDoubleDeclarationSQL

* ****getDoubleDeclarationSQL**(): string

- Overrides AbstractSqlPlatform.getDoubleDeclarationSQL

  #### Returns string

### [**](#getEnumTypeDeclarationSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/postgresql/src/PostgreSqlPlatform.ts#L213)getEnumTypeDeclarationSQL

* ****getEnumTypeDeclarationSQL**(column): string

- Overrides AbstractSqlPlatform.getEnumTypeDeclarationSQL

  #### Parameters

  * ##### column: { fieldNames: string\[]; items?<!-- -->: unknown\[]; nativeEnumName?<!-- -->: string }
    * ##### fieldNames: string\[]
    * ##### optionalitems: unknown\[]
    * ##### optionalnativeEnumName: string

  #### Returns string

### [**](#getExceptionConverter)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L431)inheritedgetExceptionConverter

* ****getExceptionConverter**(): [ExceptionConverter](https://mikro-orm.io/api/core/class/ExceptionConverter.md)

- Inherited from AbstractSqlPlatform.getExceptionConverter

  #### Returns [ExceptionConverter](https://mikro-orm.io/api/core/class/ExceptionConverter.md)

### [**](#getExtension)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L447)inheritedgetExtension

* ****getExtension**\<T>(extensionName, extensionKey, moduleName, em): T

- Inherited from AbstractSqlPlatform.getExtension

  #### Parameters

  * ##### extensionName: string
  * ##### extensionKey: string
  * ##### moduleName: string
  * ##### em: [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>

  #### Returns T

### [**](#getFloatDeclarationSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/postgresql/src/PostgreSqlPlatform.ts#L205)getFloatDeclarationSQL

* ****getFloatDeclarationSQL**(): string

- Overrides AbstractSqlPlatform.getFloatDeclarationSQL

  #### Returns string

### [**](#getFullTextIndexExpression)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/postgresql/src/PostgreSqlPlatform.ts#L120)getFullTextIndexExpression

* ****getFullTextIndexExpression**(indexName, schemaName, tableName, columns): string

- Overrides AbstractSqlPlatform.getFullTextIndexExpression

  #### Parameters

  * ##### indexName: string
  * ##### schemaName: undefined | string
  * ##### tableName: string
  * ##### columns: [SimpleColumnMeta](https://mikro-orm.io/api/core/interface/SimpleColumnMeta.md)\[]

  #### Returns string

### [**](#getFullTextWhereClause)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/postgresql/src/PostgreSqlPlatform.ts#L103)getFullTextWhereClause

* ****getFullTextWhereClause**(prop): string

- Overrides AbstractSqlPlatform.getFullTextWhereClause

  #### Parameters

  * ##### prop: [EntityProperty](https://mikro-orm.io/api/core/interface/EntityProperty.md)\<any, any>

  #### Returns string

### [**](#getIndexName)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/postgresql/src/PostgreSqlPlatform.ts#L444)getIndexName

* ****getIndexName**(tableName, columns, type): string

- Overrides AbstractSqlPlatform.getIndexName

  Returns the default name of index for the given columns cannot go past 63 character length for identifiers in MySQL

  ***

  #### Parameters

  * ##### tableName: string
  * ##### columns: string\[]
  * ##### type: primary | index | unique | foreign | sequence

  #### Returns string

### [**](#getIntegerTypeDeclarationSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/postgresql/src/PostgreSqlPlatform.ts#L78)getIntegerTypeDeclarationSQL

* ****getIntegerTypeDeclarationSQL**(column): string

- Overrides AbstractSqlPlatform.getIntegerTypeDeclarationSQL

  #### Parameters

  * ##### column: { autoincrement?<!-- -->: boolean; generated?<!-- -->: string; length?<!-- -->: number }
    * ##### optionalautoincrement: boolean
    * ##### optionalgenerated: string
    * ##### optionallength: number

  #### Returns string

### [**](#getIntervalTypeDeclarationSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/postgresql/src/PostgreSqlPlatform.ts#L279)getIntervalTypeDeclarationSQL

* ****getIntervalTypeDeclarationSQL**(column): string

- Overrides AbstractSqlPlatform.getIntervalTypeDeclarationSQL

  #### Parameters

  * ##### column: { length?<!-- -->: number }
    * ##### optionallength: number

  #### Returns string

### [**](#getJsonDeclarationSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/postgresql/src/PostgreSqlPlatform.ts#L287)getJsonDeclarationSQL

* ****getJsonDeclarationSQL**(): string

- Overrides AbstractSqlPlatform.getJsonDeclarationSQL

  #### Returns string

### [**](#getJsonIndexDefinition)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/postgresql/src/PostgreSqlPlatform.ts#L316)getJsonIndexDefinition

* ****getJsonIndexDefinition**(index): string\[]

- Overrides AbstractSqlPlatform.getJsonIndexDefinition

  #### Parameters

  * ##### index: [IndexDef](https://mikro-orm.io/api/knex/interface/IndexDef.md)

  #### Returns string\[]

### [**](#getMappedType)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/postgresql/src/PostgreSqlPlatform.ts#L171)getMappedType

* ****getMappedType**(type): [Type](https://mikro-orm.io/api/core/class/Type.md)\<unknown, unknown>

- Overrides AbstractSqlPlatform.getMappedType

  #### Parameters

  * ##### type: string

  #### Returns [Type](https://mikro-orm.io/api/core/class/Type.md)\<unknown, unknown>

### [**](#getMediumIntTypeDeclarationSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L220)inheritedgetMediumIntTypeDeclarationSQL

* ****getMediumIntTypeDeclarationSQL**(column): string

- Inherited from AbstractSqlPlatform.getMediumIntTypeDeclarationSQL

  #### Parameters

  * ##### column: { autoincrement?<!-- -->: boolean; length?<!-- -->: number; unsigned?<!-- -->: boolean }
    * ##### optionalautoincrement: boolean
    * ##### optionallength: number
    * ##### optionalunsigned: boolean

  #### Returns string

### [**](#getNamingStrategy)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L61)inheritedgetNamingStrategy

* ****getNamingStrategy**(): new () => [NamingStrategy](https://mikro-orm.io/api/core/interface/NamingStrategy.md)

- Inherited from AbstractSqlPlatform.getNamingStrategy

  #### Returns new () => [NamingStrategy](https://mikro-orm.io/api/core/interface/NamingStrategy.md)

  * * **new (): [NamingStrategy](https://mikro-orm.io/api/core/interface/NamingStrategy.md)

    - #### Returns [NamingStrategy](https://mikro-orm.io/api/core/interface/NamingStrategy.md)

### [**](#getRegExpOperator)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/postgresql/src/PostgreSqlPlatform.ts#L178)getRegExpOperator

* ****getRegExpOperator**(val, flags): string

- Overrides AbstractSqlPlatform.getRegExpOperator

  #### Parameters

  * ##### optionalval: unknown
  * ##### optionalflags: string

  #### Returns string

### [**](#getRegExpValue)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/postgresql/src/PostgreSqlPlatform.ts#L187)getRegExpValue

* ****getRegExpValue**(val): { $flags?
  <!-- -->
  : string; $re: string }

- Overrides AbstractSqlPlatform.getRegExpValue

  #### Parameters

  * ##### val: RegExp

  #### Returns { $flags?<!-- -->: string; $re: string }

  * ##### optional$flags?<!-- -->: string
  * ##### $re: string

### [**](#getReleaseSavepointSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/AbstractSqlPlatform.ts#L61)inheritedgetReleaseSavepointSQL

* ****getReleaseSavepointSQL**(savepointName): string

- Inherited from AbstractSqlPlatform.getReleaseSavepointSQL

  #### Parameters

  * ##### savepointName: string

  #### Returns string

### [**](#getRepositoryClass)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/AbstractSqlPlatform.ts#L19)inheritedgetRepositoryClass

* ****getRepositoryClass**\<T>(): [Constructor](https://mikro-orm.io/api/core.md#Constructor)<[EntityRepository](https://mikro-orm.io/api/core/class/EntityRepository.md)\<T>>

- Inherited from AbstractSqlPlatform.getRepositoryClass

  #### Returns [Constructor](https://mikro-orm.io/api/core.md#Constructor)<[EntityRepository](https://mikro-orm.io/api/core/class/EntityRepository.md)\<T>>

### [**](#getRollbackToSavepointSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/AbstractSqlPlatform.ts#L57)inheritedgetRollbackToSavepointSQL

* ****getRollbackToSavepointSQL**(savepointName): string

- Inherited from AbstractSqlPlatform.getRollbackToSavepointSQL

  #### Parameters

  * ##### savepointName: string

  #### Returns string

### [**](#getRollbackTransactionSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/AbstractSqlPlatform.ts#L49)inheritedgetRollbackTransactionSQL

* ****getRollbackTransactionSQL**(): string

- Inherited from AbstractSqlPlatform.getRollbackTransactionSQL

  #### Returns string

### [**](#getSavepointSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/AbstractSqlPlatform.ts#L53)inheritedgetSavepointSQL

* ****getSavepointSQL**(savepointName): string

- Inherited from AbstractSqlPlatform.getSavepointSQL

  #### Parameters

  * ##### savepointName: string

  #### Returns string

### [**](#getSchemaGenerator)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/AbstractSqlPlatform.ts#L33)inheritedgetSchemaGenerator

* ****getSchemaGenerator**(driver, em): [SqlSchemaGenerator](https://mikro-orm.io/api/knex/class/SqlSchemaGenerator.md)

- Inherited from AbstractSqlPlatform.getSchemaGenerator

  #### Parameters

  * ##### driver: [IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>
  * ##### optionalem: [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>

  #### Returns [SqlSchemaGenerator](https://mikro-orm.io/api/knex/class/SqlSchemaGenerator.md)

### [**](#getSchemaHelper)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/AbstractSqlPlatform.ts#L23)inheritedgetSchemaHelper

* ****getSchemaHelper**(): undefined | [SchemaHelper](https://mikro-orm.io/api/knex/class/SchemaHelper.md)

- Inherited from AbstractSqlPlatform.getSchemaHelper

  #### Returns undefined | [SchemaHelper](https://mikro-orm.io/api/knex/class/SchemaHelper.md)

### [**](#getSearchJsonPropertyKey)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/postgresql/src/PostgreSqlPlatform.ts#L291)getSearchJsonPropertyKey

* ****getSearchJsonPropertyKey**(path, type, aliased, value): string

- Overrides AbstractSqlPlatform.getSearchJsonPropertyKey

  #### Parameters

  * ##### path: string\[]
  * ##### type: undefined | string | [Type](https://mikro-orm.io/api/core/class/Type.md)\<string, string>
  * ##### aliased: boolean
  * ##### optionalvalue: unknown

  #### Returns string

### [**](#getSearchJsonPropertySQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/AbstractSqlPlatform.ts#L85)inheritedgetSearchJsonPropertySQL

* ****getSearchJsonPropertySQL**(path, type, aliased): string

- Inherited from AbstractSqlPlatform.getSearchJsonPropertySQL

  #### Parameters

  * ##### path: string
  * ##### type: string
  * ##### aliased: boolean

  #### Returns string

### [**](#getSerializedPrimaryKeyField)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L129)inheritedgetSerializedPrimaryKeyField

* ****getSerializedPrimaryKeyField**(field): string

- Inherited from AbstractSqlPlatform.getSerializedPrimaryKeyField

  Used when serializing via toObject and toJSON methods, allows to use different PK field name (like `id` instead of `_id`)

  ***

  #### Parameters

  * ##### field: string

  #### Returns string

### [**](#getSmallIntTypeDeclarationSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L216)inheritedgetSmallIntTypeDeclarationSQL

* ****getSmallIntTypeDeclarationSQL**(column): string

- Inherited from AbstractSqlPlatform.getSmallIntTypeDeclarationSQL

  #### Parameters

  * ##### column: { autoincrement?<!-- -->: boolean; length?<!-- -->: number; unsigned?<!-- -->: boolean }
    * ##### optionalautoincrement: boolean
    * ##### optionallength: number
    * ##### optionalunsigned: boolean

  #### Returns string

### [**](#getTextTypeDeclarationSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L244)inheritedgetTextTypeDeclarationSQL

* ****getTextTypeDeclarationSQL**(\_column): string

- Inherited from AbstractSqlPlatform.getTextTypeDeclarationSQL

  #### Parameters

  * ##### \_column: { length?<!-- -->: number }
    * ##### optionallength: number

  #### Returns string

### [**](#getTimeTypeDeclarationSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/postgresql/src/PostgreSqlPlatform.ts#L74)getTimeTypeDeclarationSQL

* ****getTimeTypeDeclarationSQL**(): string

- Overrides AbstractSqlPlatform.getTimeTypeDeclarationSQL

  #### Returns string

### [**](#getTimezone)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L557)inheritedgetTimezone

* ****getTimezone**(): undefined | string

- Inherited from AbstractSqlPlatform.getTimezone

  #### Returns undefined | string

### [**](#getTinyIntTypeDeclarationSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/postgresql/src/PostgreSqlPlatform.ts#L95)getTinyIntTypeDeclarationSQL

* ****getTinyIntTypeDeclarationSQL**(column): string

- Overrides AbstractSqlPlatform.getTinyIntTypeDeclarationSQL

  #### Parameters

  * ##### column: { autoincrement?<!-- -->: boolean; length?<!-- -->: number; unsigned?<!-- -->: boolean }
    * ##### optionalautoincrement: boolean
    * ##### optionallength: number
    * ##### optionalunsigned: boolean

  #### Returns string

### [**](#getUuidTypeDeclarationSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/postgresql/src/PostgreSqlPlatform.ts#L99)getUuidTypeDeclarationSQL

* ****getUuidTypeDeclarationSQL**(column): string

- Overrides AbstractSqlPlatform.getUuidTypeDeclarationSQL

  #### Parameters

  * ##### column: { length?<!-- -->: number }
    * ##### optionallength: number

  #### Returns string

### [**](#getVarcharTypeDeclarationSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/postgresql/src/PostgreSqlPlatform.ts#L265)getVarcharTypeDeclarationSQL

* ****getVarcharTypeDeclarationSQL**(column): string

- Overrides AbstractSqlPlatform.getVarcharTypeDeclarationSQL

  #### Parameters

  * ##### column: { length?<!-- -->: number }
    * ##### optionallength: number

  #### Returns string

### [**](#indexForeignKeys)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/postgresql/src/PostgreSqlPlatform.ts#L400)indexForeignKeys

* ****indexForeignKeys**(): boolean

- Overrides AbstractSqlPlatform.indexForeignKeys

  #### Returns boolean

### [**](#isAllowedTopLevelOperator)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L180)inheritedisAllowedTopLevelOperator

* ****isAllowedTopLevelOperator**(operator): boolean

- Inherited from AbstractSqlPlatform.isAllowedTopLevelOperator

  #### Parameters

  * ##### operator: string

  #### Returns boolean

### [**](#isBigIntProperty)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/postgresql/src/PostgreSqlPlatform.ts#L197)isBigIntProperty

* ****isBigIntProperty**(prop): boolean

- Overrides AbstractSqlPlatform.isBigIntProperty

  #### Parameters

  * ##### prop: [EntityProperty](https://mikro-orm.io/api/core/interface/EntityProperty.md)\<any, any>

  #### Returns boolean

### [**](#isNumericColumn)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L566)inheritedisNumericColumn

* ****isNumericColumn**(mappedType): boolean

- Inherited from AbstractSqlPlatform.isNumericColumn

  #### Parameters

  * ##### mappedType: [Type](https://mikro-orm.io/api/core/class/Type.md)\<unknown, unknown>

  #### Returns boolean

### [**](#isNumericProperty)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L561)inheritedisNumericProperty

* ****isNumericProperty**(prop, ignoreCustomType): boolean

- Inherited from AbstractSqlPlatform.isNumericProperty

  #### Parameters

  * ##### prop: [EntityProperty](https://mikro-orm.io/api/core/interface/EntityProperty.md)\<any, any>
  * ##### ignoreCustomType: boolean = <!-- -->false

  #### Returns boolean

### [**](#isPopulated)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L590)inheritedisPopulated

* ****isPopulated**\<T>(key, populate): boolean

- Inherited from AbstractSqlPlatform.isPopulated

  #### Parameters

  * ##### key: string
  * ##### populate: boolean | [PopulateOptions](https://mikro-orm.io/api/core.md#PopulateOptions)\<T>\[]

  #### Returns boolean

### [**](#isRaw)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/AbstractSqlPlatform.ts#L112)inheritedisRaw

* ****isRaw**(value): boolean

- Inherited from AbstractSqlPlatform.isRaw

  #### Parameters

  * ##### value: any

  #### Returns boolean

### [**](#lookupExtensions)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/AbstractSqlPlatform.ts#L28)inheritedlookupExtensions

* ****lookupExtensions**(orm): void

- Inherited from AbstractSqlPlatform.lookupExtensions

  Allows registering extensions of the driver automatically (e.g. `SchemaGenerator` extension in SQL drivers).

  ***

  #### Parameters

  * ##### orm: [MikroORM](https://mikro-orm.io/api/core/class/MikroORM.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>, [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>>

  #### Returns void

### [**](#marshallArray)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/postgresql/src/PostgreSqlPlatform.ts#L242)marshallArray

* ****marshallArray**(values): string

- Overrides AbstractSqlPlatform.marshallArray

  #### Parameters

  * ##### values: string\[]

  #### Returns string

### [**](#normalizeColumnType)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/postgresql/src/PostgreSqlPlatform.ts#L133)normalizeColumnType

* ****normalizeColumnType**(type, options): string

- Overrides AbstractSqlPlatform.normalizeColumnType

  This should be used only to compare types, it can strip some information like the length.

  ***

  #### Parameters

  * ##### type: string
  * ##### options: { autoincrement?<!-- -->: boolean; length?<!-- -->: number; precision?<!-- -->: number; scale?<!-- -->: number } = <!-- -->{}
    * ##### optionalautoincrement: boolean
    * ##### optionallength: number
    * ##### optionalprecision: number
    * ##### optionalscale: number

  #### Returns string

### [**](#normalizePrimaryKey)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L115)inheritednormalizePrimaryKey

* ****normalizePrimaryKey**\<T>(data): T

- Inherited from AbstractSqlPlatform.normalizePrimaryKey

  Normalizes primary key wrapper to scalar value (e.g. mongodb's ObjectId to string)

  ***

  #### Parameters

  * ##### data: IPrimaryKeyValue | [Primary](https://mikro-orm.io/api/core.md#Primary)\<T>

  #### Returns T

### [**](#parseDate)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/postgresql/src/PostgreSqlPlatform.ts#L478)parseDate

* ****parseDate**(value): Date

- Overrides AbstractSqlPlatform.parseDate

  * **@inheritDoc**

  ***

  #### Parameters

  * ##### value: string | number

  #### Returns Date

### [**](#processDateProperty)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L474)inheritedprocessDateProperty

* ****processDateProperty**(value): string | number | Date

- Inherited from AbstractSqlPlatform.processDateProperty

  #### Parameters

  * ##### value: unknown

  #### Returns string | number | Date

### [**](#quoteIdentifier)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/postgresql/src/PostgreSqlPlatform.ts#L335)quoteIdentifier

* ****quoteIdentifier**(id, quote): string

- Overrides AbstractSqlPlatform.quoteIdentifier

  #### Parameters

  * ##### id: string | { toString: () => string }
  * * ##### toString: () => string
    ##### quote: string = <!-- -->'"'

  #### Returns string

### [**](#quoteValue)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/AbstractSqlPlatform.ts#L65)inheritedquoteValue

* ****quoteValue**(value): string

- Inherited from AbstractSqlPlatform.quoteValue

  #### Parameters

  * ##### value: any

  #### Returns string

### [**](#quoteVersionValue)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L184)inheritedquoteVersionValue

* ****quoteVersionValue**(value, prop): string | number | Date

- Inherited from AbstractSqlPlatform.quoteVersionValue

  #### Parameters

  * ##### value: number | Date
  * ##### prop: [EntityProperty](https://mikro-orm.io/api/core/interface/EntityProperty.md)\<any, any>

  #### Returns string | number | Date

### [**](#setConfig)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/postgresql/src/PostgreSqlPlatform.ts#L25)setConfig

* ****setConfig**(config): void

- Overrides AbstractSqlPlatform.setConfig

  #### Parameters

  * ##### config: [Configuration](https://mikro-orm.io/api/core/class/Configuration.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>, [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>>

  #### Returns void

### [**](#shouldHaveColumn)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L594)inheritedshouldHaveColumn

* ****shouldHaveColumn**\<T>(prop, populate, exclude, includeFormulas, ignoreInlineEmbeddables): boolean

- Inherited from AbstractSqlPlatform.shouldHaveColumn

  #### Parameters

  * ##### prop: [EntityProperty](https://mikro-orm.io/api/core/interface/EntityProperty.md)\<T, any>
  * ##### populate: boolean | [PopulateOptions](https://mikro-orm.io/api/core.md#PopulateOptions)\<T>\[]
  * ##### optionalexclude: string\[]
  * ##### includeFormulas: boolean = <!-- -->true
  * ##### ignoreInlineEmbeddables: boolean = <!-- -->true

  #### Returns boolean

### [**](#supportsCreatingFullTextIndex)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/postgresql/src/PostgreSqlPlatform.ts#L116)supportsCreatingFullTextIndex

* ****supportsCreatingFullTextIndex**(): boolean

- Overrides AbstractSqlPlatform.supportsCreatingFullTextIndex

  #### Returns boolean

### [**](#supportsCustomPrimaryKeyNames)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/postgresql/src/PostgreSqlPlatform.ts#L45)supportsCustomPrimaryKeyNames

* ****supportsCustomPrimaryKeyNames**(): boolean

- Overrides AbstractSqlPlatform.supportsCustomPrimaryKeyNames

  #### Returns boolean

### [**](#supportsDownMigrations)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L629)inheritedsupportsDownMigrations

* ****supportsDownMigrations**(): boolean

- Inherited from AbstractSqlPlatform.supportsDownMigrations

  Currently not supported due to how knex does complex sqlite diffing (always based on current schema)

  ***

  #### Returns boolean

### [**](#supportsMultipleCascadePaths)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L331)inheritedsupportsMultipleCascadePaths

* ****supportsMultipleCascadePaths**(): boolean

- Inherited from AbstractSqlPlatform.supportsMultipleCascadePaths

  #### Returns boolean

### [**](#supportsMultipleStatements)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/postgresql/src/PostgreSqlPlatform.ts#L226)supportsMultipleStatements

* ****supportsMultipleStatements**(): boolean

- Overrides AbstractSqlPlatform.supportsMultipleStatements

  #### Returns boolean

### [**](#supportsNativeEnums)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/postgresql/src/PostgreSqlPlatform.ts#L41)supportsNativeEnums

* ****supportsNativeEnums**(): boolean

- Overrides AbstractSqlPlatform.supportsNativeEnums

  for postgres native enums

  ***

  #### Returns boolean

### [**](#supportsSchemas)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/postgresql/src/PostgreSqlPlatform.ts#L432)supportsSchemas

* ****supportsSchemas**(): boolean

- Overrides AbstractSqlPlatform.supportsSchemas

  #### Returns boolean

### [**](#supportsTransactions)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L53)inheritedsupportsTransactions

* ****supportsTransactions**(): boolean

- Inherited from AbstractSqlPlatform.supportsTransactions

  #### Returns boolean

### [**](#supportsUnsigned)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L570)inheritedsupportsUnsigned

* ****supportsUnsigned**(): boolean

- Inherited from AbstractSqlPlatform.supportsUnsigned

  #### Returns boolean

### [**](#unmarshallArray)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/postgresql/src/PostgreSqlPlatform.ts#L247)unmarshallArray

* ****unmarshallArray**(value): string\[]

- Overrides AbstractSqlPlatform.unmarshallArray

  #### Parameters

  * ##### value: string

  #### Returns string\[]

### [**](#usesBatchInserts)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L97)inheritedusesBatchInserts

* ****usesBatchInserts**(): boolean

- Inherited from AbstractSqlPlatform.usesBatchInserts

  Whether or not the driver supports retuning list of created PKs back when multi-inserting

  ***

  #### Returns boolean

### [**](#usesBatchUpdates)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L104)inheritedusesBatchUpdates

* ****usesBatchUpdates**(): boolean

- Inherited from AbstractSqlPlatform.usesBatchUpdates

  Whether or not the driver supports updating many records at once

  ***

  #### Returns boolean

### [**](#usesCascadeStatement)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/postgresql/src/PostgreSqlPlatform.ts#L37)usesCascadeStatement

* ****usesCascadeStatement**(): boolean

- Overrides AbstractSqlPlatform.usesCascadeStatement

  #### Returns boolean

### [**](#usesDefaultKeyword)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L108)inheritedusesDefaultKeyword

* ****usesDefaultKeyword**(): boolean

- Inherited from AbstractSqlPlatform.usesDefaultKeyword

  #### Returns boolean

### [**](#usesDifferentSerializedPrimaryKey)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L133)inheritedusesDifferentSerializedPrimaryKey

* ****usesDifferentSerializedPrimaryKey**(): boolean

- Inherited from AbstractSqlPlatform.usesDifferentSerializedPrimaryKey

  #### Returns boolean

### [**](#usesImplicitTransactions)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L57)inheritedusesImplicitTransactions

* ****usesImplicitTransactions**(): boolean

- Inherited from AbstractSqlPlatform.usesImplicitTransactions

  #### Returns boolean

### [**](#usesOutputStatement)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L69)inheritedusesOutputStatement

* ****usesOutputStatement**(): boolean

- Inherited from AbstractSqlPlatform.usesOutputStatement

  #### Returns boolean

### [**](#usesPivotTable)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/AbstractSqlPlatform.ts#L11)inheritedusesPivotTable

* ****usesPivotTable**(): boolean

- Inherited from AbstractSqlPlatform.usesPivotTable

  #### Returns boolean

### [**](#usesReturningStatement)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/postgresql/src/PostgreSqlPlatform.ts#L33)usesReturningStatement

* ****usesReturningStatement**(): boolean

- Overrides AbstractSqlPlatform.usesReturningStatement

  #### Returns boolean

### [**](#validateMetadata)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/core/src/platforms/Platform.ts#L633)inheritedvalidateMetadata

* ****validateMetadata**(meta): void

- Inherited from AbstractSqlPlatform.validateMetadata

  #### Parameters

  * ##### meta: [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<any>

  #### Returns void
