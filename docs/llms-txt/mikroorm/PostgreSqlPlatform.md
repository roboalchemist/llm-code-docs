# Source: https://mikro-orm.io/api/postgresql/class/PostgreSqlPlatform.md

# PostgreSqlPlatform<!-- -->

### Hierarchy

* [BasePostgreSqlPlatform](https://mikro-orm.io/api/sql/class/BasePostgreSqlPlatform.md)
  * *PostgreSqlPlatform*

## Index[**](#index)

### Constructors

* [**constructor](#constructor)

### Methods

* [**allowsComparingTuples](#allowsComparingTuples)
* [**castColumn](#castColumn)
* [**cloneEmbeddable](#cloneEmbeddable)
* [**compareUuids](#compareUuids)
* [**convertDateToJSValue](#convertDateToJSValue)
* [**convertIntervalToDatabaseValue](#convertintervaltodatabasevalue)
* [**convertIntervalToJSValue](#convertintervaltojsvalue)
* [**convertJsonToDatabaseValue](#convertJsonToDatabaseValue)
* [**convertJsonToJSValue](#convertJsonToJSValue)
* [**convertsJsonAutomatically](#convertsJsonAutomatically)
* [**convertUuidToDatabaseValue](#convertUuidToDatabaseValue)
* [**convertUuidToJSValue](#convertUuidToJSValue)
* [**convertVersionValue](#convertVersionValue)
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
* [**getCommitTransactionSQL](#getCommitTransactionSQL)
* [**getConfig](#getConfig)
* [**getCurrentTimestampSQL](#getCurrentTimestampSQL)
* [**getDateTimeTypeDeclarationSQL](#getDateTimeTypeDeclarationSQL)
* [**getDateTypeDeclarationSQL](#getDateTypeDeclarationSQL)
* [**getDecimalTypeDeclarationSQL](#getDecimalTypeDeclarationSQL)
* [**getDefaultClientUrl](#getDefaultClientUrl)
* [**getDefaultDateTimeLength](#getDefaultDateTimeLength)
* [**getDefaultCharLength](#getDefaultCharLength)
* [**getDefaultCharset](#getDefaultCharset)
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
* [**getCharTypeDeclarationSQL](#getCharTypeDeclarationSQL)
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
* [**getSearchJsonPropertyKey](#getSearchJsonPropertyKey)
* [**getSearchJsonPropertySQL](#getSearchJsonPropertySQL)
* [**getSchemaGenerator](#getSchemaGenerator)
* [**getSchemaHelper](#getSchemaHelper)
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
* [**lookupExtensions](#lookupExtensions)
* [**mapRegExpCondition](#mapRegExpCondition)
* [**marshallArray](#marshallArray)
* [**normalizeColumnType](#normalizeColumnType)
* [**normalizePrimaryKey](#normalizePrimaryKey)
* [**parseDate](#parsedate)
* [**processDateProperty](#processDateProperty)
* [**processJsonCondition](#processJsonCondition)
* [**quoteIdentifier](#quoteIdentifier)
* [**quoteValue](#quoteValue)
* [**setConfig](#setConfig)
* [**shouldHaveColumn](#shouldHaveColumn)
* [**supportsCreatingFullTextIndex](#supportsCreatingFullTextIndex)
* [**supportsCustomPrimaryKeyNames](#supportsCustomPrimaryKeyNames)
* [**supportsDeferredUniqueConstraints](#supportsDeferredUniqueConstraints)
* [**supportsDownMigrations](#supportsDownMigrations)
* [**supportsMaterializedViews](#supportsMaterializedViews)
* [**supportsMultipleCascadePaths](#supportsMultipleCascadePaths)
* [**supportsMultipleStatements](#supportsMultipleStatements)
* [**supportsNativeEnums](#supportsNativeEnums)
* [**supportsOnUpdate](#supportsOnUpdate)
* [**supportsSchemas](#supportsSchemas)
* [**supportsTransactions](#supportsTransactions)
* [**supportsUnionWhere](#supportsUnionWhere)
* [**supportsUnsigned](#supportsUnsigned)
* [**unmarshallArray](#unmarshallarray)
* [**usesAsKeyword](#usesAsKeyword)
* [**usesBatchInserts](#usesBatchInserts)
* [**usesBatchUpdates](#usesBatchUpdates)
* [**usesCascadeStatement](#usesCascadeStatement)
* [**usesDefaultKeyword](#usesDefaultKeyword)
* [**usesEnumCheckConstraints](#usesEnumCheckConstraints)
* [**usesImplicitTransactions](#usesImplicitTransactions)
* [**usesOutputStatement](#usesOutputStatement)
* [**usesPivotTable](#usesPivotTable)
* [**usesReturningStatement](#usesReturningStatement)
* [**validateMetadata](#validateMetadata)

## Constructors<!-- -->[**](#constructors)

### [**](#constructor)constructor

* ****new PostgreSqlPlatform**(): [PostgreSqlPlatform](https://mikro-orm.io/api/postgresql/class/PostgreSqlPlatform.md)

* Inherited from BasePostgreSqlPlatform.constructor

  #### Returns [PostgreSqlPlatform](https://mikro-orm.io/api/postgresql/class/PostgreSqlPlatform.md)

## Methods<!-- -->[**](#methods)

### [**](#allowsComparingTuples)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L210)inheritedallowsComparingTuples

* ****allowsComparingTuples**(): boolean

* Inherited from BasePostgreSqlPlatform.allowsComparingTuples

  #### Returns boolean

### [**](#castColumn)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/dialects/postgresql/BasePostgreSqlPlatform.ts#L478)inheritedcastColumn

* ****castColumn**(prop): string

* Inherited from BasePostgreSqlPlatform.castColumn

  * **@inheritDoc**

  ***

  #### Parameters

  * ##### optionalprop: { columnTypes?<!-- -->: string\[] }

    * ##### optionalcolumnTypes: string\[]

  #### Returns string

### [**](#cloneEmbeddable)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L649)inheritedcloneEmbeddable

* ****cloneEmbeddable**\<T>(data): T

* Inherited from BasePostgreSqlPlatform.cloneEmbeddable

  #### Parameters

  * ##### data: T

  #### Returns T

### [**](#compareUuids)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L518)inheritedcompareUuids

* ****compareUuids**(): string

* Inherited from BasePostgreSqlPlatform.compareUuids

  Determines how UUID values are compared in the change set tracking. Return `'string'` for inline string comparison (fast), or `'any'` for deep comparison via type methods.

  ***

  #### Returns string

### [**](#convertDateToJSValue)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L498)inheritedconvertDateToJSValue

* ****convertDateToJSValue**(value): string

* Inherited from BasePostgreSqlPlatform.convertDateToJSValue

  #### Parameters

  * ##### value: string | Date

  #### Returns string

### [**](#convertintervaltodatabasevalue)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/postgresql/src/PostgreSqlPlatform.ts#L12)convertIntervalToDatabaseValue

* ****convertIntervalToDatabaseValue**(value): unknown

* Overrides BasePostgreSqlPlatform.convertIntervalToDatabaseValue

  #### Parameters

  * ##### value: IPostgresInterval

  #### Returns unknown

### [**](#convertintervaltojsvalue)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/postgresql/src/PostgreSqlPlatform.ts#L8)convertIntervalToJSValue

* ****convertIntervalToJSValue**(value): unknown

* Overrides BasePostgreSqlPlatform.convertIntervalToJSValue

  #### Parameters

  * ##### value: string

  #### Returns unknown

### [**](#convertJsonToDatabaseValue)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L490)inheritedconvertJsonToDatabaseValue

* ****convertJsonToDatabaseValue**(value, context): unknown

* Inherited from BasePostgreSqlPlatform.convertJsonToDatabaseValue

  #### Parameters

  * ##### value: unknown

  * ##### optionalcontext: [TransformContext](https://mikro-orm.io/api/core/interface/TransformContext.md)

  #### Returns unknown

### [**](#convertJsonToJSValue)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L494)inheritedconvertJsonToJSValue

* ****convertJsonToJSValue**(value, context): unknown

* Inherited from BasePostgreSqlPlatform.convertJsonToJSValue

  #### Parameters

  * ##### value: unknown

  * ##### optionalcontext: [TransformContext](https://mikro-orm.io/api/core/interface/TransformContext.md)

  #### Returns unknown

### [**](#convertsJsonAutomatically)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L486)inheritedconvertsJsonAutomatically

* ****convertsJsonAutomatically**(): boolean

* Inherited from BasePostgreSqlPlatform.convertsJsonAutomatically

  #### Returns boolean

### [**](#convertUuidToDatabaseValue)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L526)inheritedconvertUuidToDatabaseValue

* ****convertUuidToDatabaseValue**(value): unknown

* Inherited from BasePostgreSqlPlatform.convertUuidToDatabaseValue

  #### Parameters

  * ##### value: unknown

  #### Returns unknown

### [**](#convertUuidToJSValue)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L522)inheritedconvertUuidToJSValue

* ****convertUuidToJSValue**(value): unknown

* Inherited from BasePostgreSqlPlatform.convertUuidToJSValue

  #### Parameters

  * ##### value: unknown

  #### Returns unknown

### [**](#convertVersionValue)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L199)inheritedconvertVersionValue

* ****convertVersionValue**(value, prop): string | number | Date | { $in: (string | number)\[] }

* Inherited from BasePostgreSqlPlatform.convertVersionValue

  #### Parameters

  * ##### value: number | Date

  * ##### prop: [EntityProperty](https://mikro-orm.io/api/core/interface/EntityProperty.md)\<any, any>

  #### Returns string | number | Date | { $in: (string | number)\[] }

### [**](#denormalizePrimaryKey)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L141)inheriteddenormalizePrimaryKey

* ****denormalizePrimaryKey**(data): IPrimaryKeyValue

* Inherited from BasePostgreSqlPlatform.denormalizePrimaryKey

  Converts scalar primary key representation to native driver wrapper (e.g. string to mongodb's ObjectId)

  ***

  #### Parameters

  * ##### data: IPrimaryKeyValue

  #### Returns IPrimaryKeyValue

### [**](#escape)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/postgresql/src/PostgreSqlPlatform.ts#L24)escape

* ****escape**(value): string

* Overrides BasePostgreSqlPlatform.escape

  #### Parameters

  * ##### value: any

  #### Returns string

### [**](#extractSimpleType)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L296)inheritedextractSimpleType

* ****extractSimpleType**(type): string

* Inherited from BasePostgreSqlPlatform.extractSimpleType

  #### Parameters

  * ##### type: string

  #### Returns string

### [**](#formatQuery)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L606)inheritedformatQuery

* ****formatQuery**(sql, params): string

* Inherited from BasePostgreSqlPlatform.formatQuery

  #### Parameters

  * ##### sql: string

  * ##### params: readonly<!-- --> any\[]

  #### Returns string

### [**](#generateCustomOrder)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/AbstractSqlPlatform.ts#L148)inheritedgenerateCustomOrder

* ****generateCustomOrder**(escapedColumn, values): string

* Inherited from BasePostgreSqlPlatform.generateCustomOrder

  Generates a custom order by statement given a set of in order values, eg. ORDER BY (CASE WHEN priority = 'low' THEN 1 WHEN priority = 'medium' THEN 2 ELSE NULL END)

  ***

  #### Parameters

  * ##### escapedColumn: string

  * ##### values: unknown\[]

  #### Returns string

### [**](#getArrayDeclarationSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/dialects/postgresql/BasePostgreSqlPlatform.ts#L212)inheritedgetArrayDeclarationSQL

* ****getArrayDeclarationSQL**(): string

* Inherited from BasePostgreSqlPlatform.getArrayDeclarationSQL

  #### Returns string

### [**](#getBeginTransactionSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/dialects/postgresql/BasePostgreSqlPlatform.ts#L245)inheritedgetBeginTransactionSQL

* ****getBeginTransactionSQL**(options): string\[]

* Inherited from BasePostgreSqlPlatform.getBeginTransactionSQL

  #### Parameters

  * ##### optionaloptions: { isolationLevel?<!-- -->: [IsolationLevel](https://mikro-orm.io/api/core/enum/IsolationLevel.md); readOnly?<!-- -->: boolean }

    * ##### optionalisolationLevel: [IsolationLevel](https://mikro-orm.io/api/core/enum/IsolationLevel.md)

    * ##### optionalreadOnly: boolean

  #### Returns string\[]

### [**](#getBigIntTypeDeclarationSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/dialects/postgresql/BasePostgreSqlPlatform.ts#L84)inheritedgetBigIntTypeDeclarationSQL

* ****getBigIntTypeDeclarationSQL**(column): string

* Inherited from BasePostgreSqlPlatform.getBigIntTypeDeclarationSQL

  #### Parameters

  * ##### column: { autoincrement?<!-- -->: boolean }

    * ##### optionalautoincrement: boolean

  #### Returns string

### [**](#getBlobDeclarationSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/dialects/postgresql/BasePostgreSqlPlatform.ts#L302)inheritedgetBlobDeclarationSQL

* ****getBlobDeclarationSQL**(): string

* Inherited from BasePostgreSqlPlatform.getBlobDeclarationSQL

  #### Returns string

### [**](#getBooleanTypeDeclarationSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L222)inheritedgetBooleanTypeDeclarationSQL

* ****getBooleanTypeDeclarationSQL**(): string

* Inherited from BasePostgreSqlPlatform.getBooleanTypeDeclarationSQL

  #### Returns string

### [**](#getCommitTransactionSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/AbstractSqlPlatform.ts#L66)inheritedgetCommitTransactionSQL

* ****getCommitTransactionSQL**(): string

* Inherited from BasePostgreSqlPlatform.getCommitTransactionSQL

  #### Returns string

### [**](#getConfig)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L668)inheritedgetConfig

* ****getConfig**(): [Configuration](https://mikro-orm.io/api/core/class/Configuration.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>, [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>>

* Inherited from BasePostgreSqlPlatform.getConfig

  #### Returns [Configuration](https://mikro-orm.io/api/core/class/Configuration.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>, [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>>

### [**](#getCurrentTimestampSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/dialects/postgresql/BasePostgreSqlPlatform.ts#L55)inheritedgetCurrentTimestampSQL

* ****getCurrentTimestampSQL**(length): string

* Inherited from BasePostgreSqlPlatform.getCurrentTimestampSQL

  Returns the SQL specific for the platform to get the current timestamp

  ***

  #### Parameters

  * ##### length: number

  #### Returns string

### [**](#getDateTimeTypeDeclarationSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/dialects/postgresql/BasePostgreSqlPlatform.ts#L59)inheritedgetDateTimeTypeDeclarationSQL

* ****getDateTimeTypeDeclarationSQL**(column): string

* Inherited from BasePostgreSqlPlatform.getDateTimeTypeDeclarationSQL

  #### Parameters

  * ##### column: { length?<!-- -->: number }

    * ##### optionallength: number

  #### Returns string

### [**](#getDateTypeDeclarationSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L168)inheritedgetDateTypeDeclarationSQL

* ****getDateTypeDeclarationSQL**(length): string

* Inherited from BasePostgreSqlPlatform.getDateTypeDeclarationSQL

  #### Parameters

  * ##### optionallength: number

  #### Returns string

### [**](#getDecimalTypeDeclarationSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L284)inheritedgetDecimalTypeDeclarationSQL

* ****getDecimalTypeDeclarationSQL**(column): string

* Inherited from BasePostgreSqlPlatform.getDecimalTypeDeclarationSQL

  #### Parameters

  * ##### column: { precision?<!-- -->: number; scale?<!-- -->: number }

    * ##### optionalprecision: number

    * ##### optionalscale: number

  #### Returns string

### [**](#getDefaultClientUrl)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/dialects/postgresql/BasePostgreSqlPlatform.ts#L499)inheritedgetDefaultClientUrl

* ****getDefaultClientUrl**(): string

* Inherited from BasePostgreSqlPlatform.getDefaultClientUrl

  Returns default client url for given driver (e.g. mongodb://127.0.0.1:27017 for mongodb)

  ***

  #### Returns string

### [**](#getDefaultDateTimeLength)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/dialects/postgresql/BasePostgreSqlPlatform.ts#L64)inheritedgetDefaultDateTimeLength

* ****getDefaultDateTimeLength**(): number

* Inherited from BasePostgreSqlPlatform.getDefaultDateTimeLength

  #### Returns number

### [**](#getDefaultCharLength)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L164)inheritedgetDefaultCharLength

* ****getDefaultCharLength**(): number

* Inherited from BasePostgreSqlPlatform.getDefaultCharLength

  #### Returns number

### [**](#getDefaultCharset)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L545)inheritedgetDefaultCharset

* ****getDefaultCharset**(): string

* Inherited from BasePostgreSqlPlatform.getDefaultCharset

  #### Returns string

### [**](#getDefaultMappedType)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/dialects/postgresql/BasePostgreSqlPlatform.ts#L410)inheritedgetDefaultMappedType

* ****getDefaultMappedType**(type): [Type](https://mikro-orm.io/api/core/class/Type.md)\<unknown, unknown>

* Inherited from BasePostgreSqlPlatform.getDefaultMappedType

  #### Parameters

  * ##### type: string

  #### Returns [Type](https://mikro-orm.io/api/core/class/Type.md)\<unknown, unknown>

### [**](#getDefaultPrimaryName)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/dialects/postgresql/BasePostgreSqlPlatform.ts#L465)inheritedgetDefaultPrimaryName

* ****getDefaultPrimaryName**(tableName, columns): string

* Inherited from BasePostgreSqlPlatform.getDefaultPrimaryName

  #### Parameters

  * ##### tableName: string

  * ##### columns: string\[]

  #### Returns string

### [**](#getDefaultSchemaName)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/dialects/postgresql/BasePostgreSqlPlatform.ts#L442)inheritedgetDefaultSchemaName

* ****getDefaultSchemaName**(): undefined | string

* Inherited from BasePostgreSqlPlatform.getDefaultSchemaName

  #### Returns undefined | string

### [**](#getDefaultVarcharLength)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L160)inheritedgetDefaultVarcharLength

* ****getDefaultVarcharLength**(): number

* Inherited from BasePostgreSqlPlatform.getDefaultVarcharLength

  #### Returns number

### [**](#getDefaultVersionLength)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L206)inheritedgetDefaultVersionLength

* ****getDefaultVersionLength**(): number

* Inherited from BasePostgreSqlPlatform.getDefaultVersionLength

  #### Returns number

### [**](#getDoubleDeclarationSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/dialects/postgresql/BasePostgreSqlPlatform.ts#L220)inheritedgetDoubleDeclarationSQL

* ****getDoubleDeclarationSQL**(): string

* Inherited from BasePostgreSqlPlatform.getDoubleDeclarationSQL

  #### Returns string

### [**](#getEnumTypeDeclarationSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/dialects/postgresql/BasePostgreSqlPlatform.ts#L224)inheritedgetEnumTypeDeclarationSQL

* ****getEnumTypeDeclarationSQL**(column): string

* Inherited from BasePostgreSqlPlatform.getEnumTypeDeclarationSQL

  #### Parameters

  * ##### column: { fieldNames: string\[]; items?<!-- -->: unknown\[]; nativeEnumName?<!-- -->: string }

    * ##### fieldNames: string\[]

    * ##### optionalitems: unknown\[]

    * ##### optionalnativeEnumName: string

  #### Returns string

### [**](#getExceptionConverter)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L549)inheritedgetExceptionConverter

* ****getExceptionConverter**(): [ExceptionConverter](https://mikro-orm.io/api/core/class/ExceptionConverter.md)

* Inherited from BasePostgreSqlPlatform.getExceptionConverter

  #### Returns [ExceptionConverter](https://mikro-orm.io/api/core/class/ExceptionConverter.md)

### [**](#getExtension)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L565)inheritedgetExtension

* ****getExtension**\<T>(extensionName, extensionKey, moduleName, em): T

* Inherited from BasePostgreSqlPlatform.getExtension

  #### Parameters

  * ##### extensionName: string

  * ##### extensionKey: string

  * ##### moduleName: string

  * ##### em: [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>

  #### Returns T

### [**](#getFloatDeclarationSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/dialects/postgresql/BasePostgreSqlPlatform.ts#L216)inheritedgetFloatDeclarationSQL

* ****getFloatDeclarationSQL**(): string

* Inherited from BasePostgreSqlPlatform.getFloatDeclarationSQL

  #### Returns string

### [**](#getFullTextIndexExpression)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/dialects/postgresql/BasePostgreSqlPlatform.ts#L122)inheritedgetFullTextIndexExpression

* ****getFullTextIndexExpression**(indexName, schemaName, tableName, columns): string

* Inherited from BasePostgreSqlPlatform.getFullTextIndexExpression

  #### Parameters

  * ##### indexName: string

  * ##### schemaName: undefined | string

  * ##### tableName: string

  * ##### columns: [SimpleColumnMeta](https://mikro-orm.io/api/core/interface/SimpleColumnMeta.md)\[]

  #### Returns string

### [**](#getFullTextWhereClause)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/dialects/postgresql/BasePostgreSqlPlatform.ts#L105)inheritedgetFullTextWhereClause

* ****getFullTextWhereClause**(prop): string

* Inherited from BasePostgreSqlPlatform.getFullTextWhereClause

  #### Parameters

  * ##### prop: [EntityProperty](https://mikro-orm.io/api/core/interface/EntityProperty.md)\<any, any>

  #### Returns string

### [**](#getCharTypeDeclarationSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/dialects/postgresql/BasePostgreSqlPlatform.ts#L291)inheritedgetCharTypeDeclarationSQL

* ****getCharTypeDeclarationSQL**(column): string

* Inherited from BasePostgreSqlPlatform.getCharTypeDeclarationSQL

  #### Parameters

  * ##### column: { length?<!-- -->: number }

    * ##### optionallength: number

  #### Returns string

### [**](#getIndexName)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/dialects/postgresql/BasePostgreSqlPlatform.ts#L450)inheritedgetIndexName

* ****getIndexName**(tableName, columns, type): string

* Inherited from BasePostgreSqlPlatform.getIndexName

  Returns the default name of index for the given columns cannot go past 63 character length for identifiers in MySQL

  ***

  #### Parameters

  * ##### tableName: string

  * ##### columns: string\[]

  * ##### type: primary | index | unique | foreign | sequence

  #### Returns string

### [**](#getIntegerTypeDeclarationSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/dialects/postgresql/BasePostgreSqlPlatform.ts#L72)inheritedgetIntegerTypeDeclarationSQL

* ****getIntegerTypeDeclarationSQL**(column): string

* Inherited from BasePostgreSqlPlatform.getIntegerTypeDeclarationSQL

  #### Parameters

  * ##### column: { autoincrement?<!-- -->: boolean; generated?<!-- -->: string; length?<!-- -->: number }

    * ##### optionalautoincrement: boolean

    * ##### optionalgenerated: string

    * ##### optionallength: number

  #### Returns string

### [**](#getIntervalTypeDeclarationSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/dialects/postgresql/BasePostgreSqlPlatform.ts#L298)inheritedgetIntervalTypeDeclarationSQL

* ****getIntervalTypeDeclarationSQL**(column): string

* Inherited from BasePostgreSqlPlatform.getIntervalTypeDeclarationSQL

  #### Parameters

  * ##### column: { length?<!-- -->: number }

    * ##### optionallength: number

  #### Returns string

### [**](#getJsonDeclarationSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/dialects/postgresql/BasePostgreSqlPlatform.ts#L306)inheritedgetJsonDeclarationSQL

* ****getJsonDeclarationSQL**(): string

* Inherited from BasePostgreSqlPlatform.getJsonDeclarationSQL

  #### Returns string

### [**](#getJsonIndexDefinition)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/dialects/postgresql/BasePostgreSqlPlatform.ts#L339)inheritedgetJsonIndexDefinition

* ****getJsonIndexDefinition**(index): string\[]

* Inherited from BasePostgreSqlPlatform.getJsonIndexDefinition

  #### Parameters

  * ##### index: [IndexDef](https://mikro-orm.io/api/sql/interface/IndexDef.md)

  #### Returns string\[]

### [**](#getMappedType)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/dialects/postgresql/BasePostgreSqlPlatform.ts#L181)inheritedgetMappedType

* ****getMappedType**(type): [Type](https://mikro-orm.io/api/core/class/Type.md)\<unknown, unknown>

* Inherited from BasePostgreSqlPlatform.getMappedType

  #### Parameters

  * ##### type: string

  #### Returns [Type](https://mikro-orm.io/api/core/class/Type.md)\<unknown, unknown>

### [**](#getMediumIntTypeDeclarationSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L234)inheritedgetMediumIntTypeDeclarationSQL

* ****getMediumIntTypeDeclarationSQL**(column): string

* Inherited from BasePostgreSqlPlatform.getMediumIntTypeDeclarationSQL

  #### Parameters

  * ##### column: { autoincrement?<!-- -->: boolean; length?<!-- -->: number; unsigned?<!-- -->: boolean }

    * ##### optionalautoincrement: boolean

    * ##### optionallength: number

    * ##### optionalunsigned: boolean

  #### Returns string

### [**](#getNamingStrategy)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L75)inheritedgetNamingStrategy

* ****getNamingStrategy**(): new () => [NamingStrategy](https://mikro-orm.io/api/core/interface/NamingStrategy.md)

* Inherited from BasePostgreSqlPlatform.getNamingStrategy

  #### Returns new () => [NamingStrategy](https://mikro-orm.io/api/core/interface/NamingStrategy.md)

  * * **new (): [NamingStrategy](https://mikro-orm.io/api/core/interface/NamingStrategy.md)

    * #### Returns [NamingStrategy](https://mikro-orm.io/api/core/interface/NamingStrategy.md)

### [**](#getRegExpOperator)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/dialects/postgresql/BasePostgreSqlPlatform.ts#L190)inheritedgetRegExpOperator

* ****getRegExpOperator**(val, flags): string

* Inherited from BasePostgreSqlPlatform.getRegExpOperator

  #### Parameters

  * ##### optionalval: unknown

  * ##### optionalflags: string

  #### Returns string

### [**](#getRegExpValue)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/dialects/postgresql/BasePostgreSqlPlatform.ts#L200)inheritedgetRegExpValue

* ****getRegExpValue**(val): { $flags?
  <!-- -->
  : string; $re: string }

* Inherited from BasePostgreSqlPlatform.getRegExpValue

  #### Parameters

  * ##### val: RegExp

  #### Returns { $flags?<!-- -->: string; $re: string }

  * ##### optional$flags?<!-- -->: string

  * ##### $re: string

### [**](#getReleaseSavepointSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/AbstractSqlPlatform.ts#L82)inheritedgetReleaseSavepointSQL

* ****getReleaseSavepointSQL**(savepointName): string

* Inherited from BasePostgreSqlPlatform.getReleaseSavepointSQL

  #### Parameters

  * ##### savepointName: string

  #### Returns string

### [**](#getRepositoryClass)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/AbstractSqlPlatform.ts#L34)inheritedgetRepositoryClass

* ****getRepositoryClass**\<T>(): [Constructor](https://mikro-orm.io/api/core.md#Constructor)<[EntityRepository](https://mikro-orm.io/api/core/class/EntityRepository.md)\<T>>

* Inherited from BasePostgreSqlPlatform.getRepositoryClass

  #### Returns [Constructor](https://mikro-orm.io/api/core.md#Constructor)<[EntityRepository](https://mikro-orm.io/api/core/class/EntityRepository.md)\<T>>

### [**](#getRollbackToSavepointSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/AbstractSqlPlatform.ts#L78)inheritedgetRollbackToSavepointSQL

* ****getRollbackToSavepointSQL**(savepointName): string

* Inherited from BasePostgreSqlPlatform.getRollbackToSavepointSQL

  #### Parameters

  * ##### savepointName: string

  #### Returns string

### [**](#getRollbackTransactionSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/AbstractSqlPlatform.ts#L70)inheritedgetRollbackTransactionSQL

* ****getRollbackTransactionSQL**(): string

* Inherited from BasePostgreSqlPlatform.getRollbackTransactionSQL

  #### Returns string

### [**](#getSavepointSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/AbstractSqlPlatform.ts#L74)inheritedgetSavepointSQL

* ****getSavepointSQL**(savepointName): string

* Inherited from BasePostgreSqlPlatform.getSavepointSQL

  #### Parameters

  * ##### savepointName: string

  #### Returns string

### [**](#getSearchJsonPropertyKey)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/dialects/postgresql/BasePostgreSqlPlatform.ts#L310)inheritedgetSearchJsonPropertyKey

* ****getSearchJsonPropertyKey**(path, type, aliased, value): string | [RawQueryFragment](https://mikro-orm.io/api/core/class/RawQueryFragment.md)\<string>

* Inherited from BasePostgreSqlPlatform.getSearchJsonPropertyKey

  #### Parameters

  * ##### path: string\[]

  * ##### type: undefined | string | [Type](https://mikro-orm.io/api/core/class/Type.md)\<string, string>

  * ##### aliased: boolean

  * ##### optionalvalue: unknown

  #### Returns string | [RawQueryFragment](https://mikro-orm.io/api/core/class/RawQueryFragment.md)\<string>

### [**](#getSearchJsonPropertySQL)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/AbstractSqlPlatform.ts#L98)inheritedgetSearchJsonPropertySQL

* ****getSearchJsonPropertySQL**(path, type, aliased): string | [RawQueryFragment](https://mikro-orm.io/api/core/class/RawQueryFragment.md)\<string>

* Inherited from BasePostgreSqlPlatform.getSearchJsonPropertySQL

  #### Parameters

  * ##### path: string

  * ##### type: string

  * ##### aliased: boolean

  #### Returns string | [RawQueryFragment](https://mikro-orm.io/api/core/class/RawQueryFragment.md)\<string>

### [**](#getSchemaGenerator)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/AbstractSqlPlatform.ts#L48)inheritedgetSchemaGenerator

* ****getSchemaGenerator**(driver, em): [SqlSchemaGenerator](https://mikro-orm.io/api/sql/class/SqlSchemaGenerator.md)

* Inherited from BasePostgreSqlPlatform.getSchemaGenerator

  #### Parameters

  * ##### driver: [IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>

  * ##### optionalem: [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>

  #### Returns [SqlSchemaGenerator](https://mikro-orm.io/api/sql/class/SqlSchemaGenerator.md)

### [**](#getSchemaHelper)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/AbstractSqlPlatform.ts#L38)inheritedgetSchemaHelper

* ****getSchemaHelper**(): undefined | [SchemaHelper](https://mikro-orm.io/api/sql/class/SchemaHelper.md)

* Inherited from BasePostgreSqlPlatform.getSchemaHelper

  #### Returns undefined | [SchemaHelper](https://mikro-orm.io/api/sql/class/SchemaHelper.md)

### [**](#getSmallIntTypeDeclarationSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L230)inheritedgetSmallIntTypeDeclarationSQL

* ****getSmallIntTypeDeclarationSQL**(column): string

* Inherited from BasePostgreSqlPlatform.getSmallIntTypeDeclarationSQL

  #### Parameters

  * ##### column: { autoincrement?<!-- -->: boolean; length?<!-- -->: number; unsigned?<!-- -->: boolean }

    * ##### optionalautoincrement: boolean

    * ##### optionallength: number

    * ##### optionalunsigned: boolean

  #### Returns string

### [**](#getTextTypeDeclarationSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L258)inheritedgetTextTypeDeclarationSQL

* ****getTextTypeDeclarationSQL**(\_column): string

* Inherited from BasePostgreSqlPlatform.getTextTypeDeclarationSQL

  #### Parameters

  * ##### \_column: { length?<!-- -->: number }

    * ##### optionallength: number

  #### Returns string

### [**](#getTimeTypeDeclarationSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/dialects/postgresql/BasePostgreSqlPlatform.ts#L68)inheritedgetTimeTypeDeclarationSQL

* ****getTimeTypeDeclarationSQL**(): string

* Inherited from BasePostgreSqlPlatform.getTimeTypeDeclarationSQL

  #### Returns string

### [**](#getTimezone)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L672)inheritedgetTimezone

* ****getTimezone**(): undefined | string

* Inherited from BasePostgreSqlPlatform.getTimezone

  #### Returns undefined | string

### [**](#getTinyIntTypeDeclarationSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/dialects/postgresql/BasePostgreSqlPlatform.ts#L93)inheritedgetTinyIntTypeDeclarationSQL

* ****getTinyIntTypeDeclarationSQL**(column): string

* Inherited from BasePostgreSqlPlatform.getTinyIntTypeDeclarationSQL

  #### Parameters

  * ##### column: { autoincrement?<!-- -->: boolean; length?<!-- -->: number; unsigned?<!-- -->: boolean }

    * ##### optionalautoincrement: boolean

    * ##### optionallength: number

    * ##### optionalunsigned: boolean

  #### Returns string

### [**](#getUuidTypeDeclarationSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/dialects/postgresql/BasePostgreSqlPlatform.ts#L101)inheritedgetUuidTypeDeclarationSQL

* ****getUuidTypeDeclarationSQL**(column): string

* Inherited from BasePostgreSqlPlatform.getUuidTypeDeclarationSQL

  #### Parameters

  * ##### column: { length?<!-- -->: number }

    * ##### optionallength: number

  #### Returns string

### [**](#getVarcharTypeDeclarationSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/dialects/postgresql/BasePostgreSqlPlatform.ts#L284)inheritedgetVarcharTypeDeclarationSQL

* ****getVarcharTypeDeclarationSQL**(column): string

* Inherited from BasePostgreSqlPlatform.getVarcharTypeDeclarationSQL

  #### Parameters

  * ##### column: { length?<!-- -->: number }

    * ##### optionallength: number

  #### Returns string

### [**](#indexForeignKeys)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/dialects/postgresql/BasePostgreSqlPlatform.ts#L406)inheritedindexForeignKeys

* ****indexForeignKeys**(): boolean

* Inherited from BasePostgreSqlPlatform.indexForeignKeys

  #### Returns boolean

### [**](#isAllowedTopLevelOperator)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L195)inheritedisAllowedTopLevelOperator

* ****isAllowedTopLevelOperator**(operator): boolean

* Inherited from BasePostgreSqlPlatform.isAllowedTopLevelOperator

  #### Parameters

  * ##### operator: string

  #### Returns boolean

### [**](#isBigIntProperty)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/dialects/postgresql/BasePostgreSqlPlatform.ts#L208)inheritedisBigIntProperty

* ****isBigIntProperty**(prop): boolean

* Inherited from BasePostgreSqlPlatform.isBigIntProperty

  #### Parameters

  * ##### prop: [EntityProperty](https://mikro-orm.io/api/core/interface/EntityProperty.md)\<any, any>

  #### Returns boolean

### [**](#isNumericColumn)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L681)inheritedisNumericColumn

* ****isNumericColumn**(mappedType): boolean

* Inherited from BasePostgreSqlPlatform.isNumericColumn

  #### Parameters

  * ##### mappedType: [Type](https://mikro-orm.io/api/core/class/Type.md)\<unknown, unknown>

  #### Returns boolean

### [**](#isNumericProperty)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L676)inheritedisNumericProperty

* ****isNumericProperty**(prop, ignoreCustomType): boolean

* Inherited from BasePostgreSqlPlatform.isNumericProperty

  #### Parameters

  * ##### prop: [EntityProperty](https://mikro-orm.io/api/core/interface/EntityProperty.md)\<any, any>

  * ##### ignoreCustomType: boolean = <!-- -->false

  #### Returns boolean

### [**](#isPopulated)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L708)inheritedisPopulated

* ****isPopulated**\<T>(key, populate): boolean

* Inherited from BasePostgreSqlPlatform.isPopulated

  #### Parameters

  * ##### key: string

  * ##### populate: boolean | readonly<!-- --> [PopulateOptions](https://mikro-orm.io/api/core.md#PopulateOptions)\<T>\[]

  #### Returns boolean

### [**](#lookupExtensions)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/AbstractSqlPlatform.ts#L43)inheritedlookupExtensions

* ****lookupExtensions**(orm): void

* Inherited from BasePostgreSqlPlatform.lookupExtensions

  Allows registering extensions of the driver automatically (e.g. `SchemaGenerator` extension in SQL drivers).

  ***

  #### Parameters

  * ##### orm: [MikroORM](https://mikro-orm.io/api/core/class/MikroORM.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>, [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>, (string | [EntitySchema](https://mikro-orm.io/api/core/class/EntitySchema.md)\<any, never, [EntityCtor](https://mikro-orm.io/api/core.md#EntityCtor)\<any>> | [EntityClass](https://mikro-orm.io/api/core.md#EntityClass)\<Partial\<any>>)\[]>

  #### Returns void

### [**](#mapRegExpCondition)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L180)inheritedmapRegExpCondition

* ****mapRegExpCondition**(mappedKey, value): { params: unknown\[]; sql: string }

* Inherited from BasePostgreSqlPlatform.mapRegExpCondition

  #### Parameters

  * ##### mappedKey: string

  * ##### value: { $flags?<!-- -->: string; $re: string }

    * ##### optional$flags: string

    * ##### $re: string

  #### Returns { params: unknown\[]; sql: string }

  * ##### params: unknown\[]

  * ##### sql: string

### [**](#marshallArray)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/dialects/postgresql/BasePostgreSqlPlatform.ts#L257)inheritedmarshallArray

* ****marshallArray**(values): string

* Inherited from BasePostgreSqlPlatform.marshallArray

  #### Parameters

  * ##### values: string\[]

  #### Returns string

### [**](#normalizeColumnType)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/dialects/postgresql/BasePostgreSqlPlatform.ts#L140)inheritednormalizeColumnType

* ****normalizeColumnType**(type, options): string

* Inherited from BasePostgreSqlPlatform.normalizeColumnType

  This should be used only to compare types, it can strip some information like the length.

  ***

  #### Parameters

  * ##### type: string

  * ##### options: { autoincrement?<!-- -->: boolean; length?<!-- -->: number; precision?<!-- -->: number; scale?<!-- -->: number }

    * ##### optionalautoincrement: boolean

    * ##### optionallength: number

    * ##### optionalprecision: number

    * ##### optionalscale: number

  #### Returns string

### [**](#normalizePrimaryKey)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L134)inheritednormalizePrimaryKey

* ****normalizePrimaryKey**\<T>(data): T

* Inherited from BasePostgreSqlPlatform.normalizePrimaryKey

  Normalizes primary key wrapper to scalar value (e.g. mongodb's ObjectId to string)

  ***

  #### Parameters

  * ##### data: IPrimaryKeyValue | [Primary](https://mikro-orm.io/api/core.md#Primary)\<T>

  #### Returns T

### [**](#parsedate)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/postgresql/src/PostgreSqlPlatform.ts#L51)parseDate

* ****parseDate**(value): Date

* Overrides BasePostgreSqlPlatform.parseDate

  * **@inheritDoc**

  ***

  #### Parameters

  * ##### value: string | number

  #### Returns Date

### [**](#processDateProperty)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L583)inheritedprocessDateProperty

* ****processDateProperty**(value): string | number | Date

* Inherited from BasePostgreSqlPlatform.processDateProperty

  #### Parameters

  * ##### value: unknown

  #### Returns string | number | Date

### [**](#processJsonCondition)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L426)inheritedprocessJsonCondition

* ****processJsonCondition**\<T>(o, value, path, alias): [FilterQuery](https://mikro-orm.io/api/core.md#FilterQuery)\<T>

* Inherited from BasePostgreSqlPlatform.processJsonCondition

  #### Parameters

  * ##### o: [FilterQuery](https://mikro-orm.io/api/core.md#FilterQuery)\<T>

  * ##### value: [EntityValue](https://mikro-orm.io/api/core.md#EntityValue)\<T>

  * ##### path: [EntityKey](https://mikro-orm.io/api/core.md#EntityKey)\<T>\[]

  * ##### alias: boolean

  #### Returns [FilterQuery](https://mikro-orm.io/api/core.md#FilterQuery)\<T>

### [**](#quoteIdentifier)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/dialects/postgresql/BasePostgreSqlPlatform.ts#L357)inheritedquoteIdentifier

* ****quoteIdentifier**(id, quote): string

* Inherited from BasePostgreSqlPlatform.quoteIdentifier

  #### Parameters

  * ##### id: string | { toString: () => string }

  * * ##### toString: () => string

    ##### quote: string = <!-- -->'"'

  #### Returns string

### [**](#quoteValue)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/AbstractSqlPlatform.ts#L86)inheritedquoteValue

* ****quoteValue**(value): string

* Inherited from BasePostgreSqlPlatform.quoteValue

  #### Parameters

  * ##### value: any

  #### Returns string

### [**](#setConfig)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L657)inheritedsetConfig

* ****setConfig**(config): void

* Inherited from BasePostgreSqlPlatform.setConfig

  #### Parameters

  * ##### config: [Configuration](https://mikro-orm.io/api/core/class/Configuration.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>, [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>>

  #### Returns void

### [**](#shouldHaveColumn)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L712)inheritedshouldHaveColumn

* ****shouldHaveColumn**\<T>(prop, populate, exclude, includeFormulas, ignoreInlineEmbeddables): boolean

* Inherited from BasePostgreSqlPlatform.shouldHaveColumn

  #### Parameters

  * ##### prop: [EntityProperty](https://mikro-orm.io/api/core/interface/EntityProperty.md)\<T, any>

  * ##### populate: boolean | readonly<!-- --> [PopulateOptions](https://mikro-orm.io/api/core.md#PopulateOptions)\<T>\[]

  * ##### optionalexclude: string\[]

  * ##### includeFormulas: boolean = <!-- -->true

  * ##### ignoreInlineEmbeddables: boolean = <!-- -->true

  #### Returns boolean

### [**](#supportsCreatingFullTextIndex)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/dialects/postgresql/BasePostgreSqlPlatform.ts#L118)inheritedsupportsCreatingFullTextIndex

* ****supportsCreatingFullTextIndex**(): boolean

* Inherited from BasePostgreSqlPlatform.supportsCreatingFullTextIndex

  #### Returns boolean

### [**](#supportsCustomPrimaryKeyNames)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/dialects/postgresql/BasePostgreSqlPlatform.ts#L51)inheritedsupportsCustomPrimaryKeyNames

* ****supportsCustomPrimaryKeyNames**(): boolean

* Inherited from BasePostgreSqlPlatform.supportsCustomPrimaryKeyNames

  #### Returns boolean

### [**](#supportsDeferredUniqueConstraints)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L757)inheritedsupportsDeferredUniqueConstraints

* ****supportsDeferredUniqueConstraints**(): boolean

* Inherited from BasePostgreSqlPlatform.supportsDeferredUniqueConstraints

  #### Returns boolean

### [**](#supportsDownMigrations)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L753)inheritedsupportsDownMigrations

* ****supportsDownMigrations**(): boolean

* Inherited from BasePostgreSqlPlatform.supportsDownMigrations

  Currently not supported due to how knex does complex sqlite diffing (always based on current schema)

  ***

  #### Returns boolean

### [**](#supportsMaterializedViews)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/dialects/postgresql/BasePostgreSqlPlatform.ts#L47)inheritedsupportsMaterializedViews

* ****supportsMaterializedViews**(): boolean

* Inherited from BasePostgreSqlPlatform.supportsMaterializedViews

  #### Returns boolean

### [**](#supportsMultipleCascadePaths)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L374)inheritedsupportsMultipleCascadePaths

* ****supportsMultipleCascadePaths**(): boolean

* Inherited from BasePostgreSqlPlatform.supportsMultipleCascadePaths

  #### Returns boolean

### [**](#supportsMultipleStatements)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/dialects/postgresql/BasePostgreSqlPlatform.ts#L241)inheritedsupportsMultipleStatements

* ****supportsMultipleStatements**(): boolean

* Inherited from BasePostgreSqlPlatform.supportsMultipleStatements

  #### Returns boolean

### [**](#supportsNativeEnums)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/dialects/postgresql/BasePostgreSqlPlatform.ts#L39)inheritedsupportsNativeEnums

* ****supportsNativeEnums**(): boolean

* Inherited from BasePostgreSqlPlatform.supportsNativeEnums

  for postgres native enums

  ***

  #### Returns boolean

### [**](#supportsOnUpdate)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L382)inheritedsupportsOnUpdate

* ****supportsOnUpdate**(): boolean

* Inherited from BasePostgreSqlPlatform.supportsOnUpdate

  Returns true if the platform supports ON UPDATE foreign key rules. Oracle doesn't support ON UPDATE rules.

  ***

  #### Returns boolean

### [**](#supportsSchemas)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/dialects/postgresql/BasePostgreSqlPlatform.ts#L438)inheritedsupportsSchemas

* ****supportsSchemas**(): boolean

* Inherited from BasePostgreSqlPlatform.supportsSchemas

  #### Returns boolean

### [**](#supportsTransactions)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L67)inheritedsupportsTransactions

* ****supportsTransactions**(): boolean

* Inherited from BasePostgreSqlPlatform.supportsTransactions

  #### Returns boolean

### [**](#supportsUnionWhere)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/AbstractSqlPlatform.ts#L139)inheritedsupportsUnionWhere

* ****supportsUnionWhere**(): boolean

* Inherited from BasePostgreSqlPlatform.supportsUnionWhere

  #### Returns boolean

### [**](#supportsUnsigned)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L685)inheritedsupportsUnsigned

* ****supportsUnsigned**(): boolean

* Inherited from BasePostgreSqlPlatform.supportsUnsigned

  #### Returns boolean

### [**](#unmarshallarray)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/postgresql/src/PostgreSqlPlatform.ts#L20)unmarshallArray

* ****unmarshallArray**(value): string\[]

* Overrides BasePostgreSqlPlatform.unmarshallArray

  #### Parameters

  * ##### value: string

  #### Returns string\[]

### [**](#usesAsKeyword)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L510)inheritedusesAsKeyword

* ****usesAsKeyword**(): boolean

* Inherited from BasePostgreSqlPlatform.usesAsKeyword

  #### Returns boolean

### [**](#usesBatchInserts)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L116)inheritedusesBatchInserts

* ****usesBatchInserts**(): boolean

* Inherited from BasePostgreSqlPlatform.usesBatchInserts

  Whether or not the driver supports retuning list of created PKs back when multi-inserting

  ***

  #### Returns boolean

### [**](#usesBatchUpdates)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L123)inheritedusesBatchUpdates

* ****usesBatchUpdates**(): boolean

* Inherited from BasePostgreSqlPlatform.usesBatchUpdates

  Whether or not the driver supports updating many records at once

  ***

  #### Returns boolean

### [**](#usesCascadeStatement)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/dialects/postgresql/BasePostgreSqlPlatform.ts#L35)inheritedusesCascadeStatement

* ****usesCascadeStatement**(): boolean

* Inherited from BasePostgreSqlPlatform.usesCascadeStatement

  #### Returns boolean

### [**](#usesDefaultKeyword)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L127)inheritedusesDefaultKeyword

* ****usesDefaultKeyword**(): boolean

* Inherited from BasePostgreSqlPlatform.usesDefaultKeyword

  #### Returns boolean

### [**](#usesEnumCheckConstraints)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/dialects/postgresql/BasePostgreSqlPlatform.ts#L43)inheritedusesEnumCheckConstraints

* ****usesEnumCheckConstraints**(): boolean

* Inherited from BasePostgreSqlPlatform.usesEnumCheckConstraints

  for postgres text enums (default)

  ***

  #### Returns boolean

### [**](#usesImplicitTransactions)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L71)inheritedusesImplicitTransactions

* ****usesImplicitTransactions**(): boolean

* Inherited from BasePostgreSqlPlatform.usesImplicitTransactions

  #### Returns boolean

### [**](#usesOutputStatement)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L83)inheritedusesOutputStatement

* ****usesOutputStatement**(): boolean

* Inherited from BasePostgreSqlPlatform.usesOutputStatement

  #### Returns boolean

### [**](#usesPivotTable)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/AbstractSqlPlatform.ts#L26)inheritedusesPivotTable

* ****usesPivotTable**(): boolean

* Inherited from BasePostgreSqlPlatform.usesPivotTable

  #### Returns boolean

### [**](#usesReturningStatement)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/dialects/postgresql/BasePostgreSqlPlatform.ts#L31)inheritedusesReturningStatement

* ****usesReturningStatement**(): boolean

* Inherited from BasePostgreSqlPlatform.usesReturningStatement

  #### Returns boolean

### [**](#validateMetadata)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L761)inheritedvalidateMetadata

* ****validateMetadata**(meta): void

* Inherited from BasePostgreSqlPlatform.validateMetadata

  #### Parameters

  * ##### meta: [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<any, [EntityCtor](https://mikro-orm.io/api/core.md#EntityCtor)\<any>>

  #### Returns void
