# Source: https://mikro-orm.io/api/sql/class/BaseMySqlPlatform.md

# BaseMySqlPlatform<!-- -->

### Hierarchy

* [AbstractSqlPlatform](https://mikro-orm.io/api/sql/class/AbstractSqlPlatform.md)
  * *BaseMySqlPlatform*
    * [MySqlPlatform](https://mikro-orm.io/api/mysql/class/MySqlPlatform.md)

## Index[**](#index)

### Constructors

* [**constructor](#constructor)

### Methods

* [**allowsComparingTuples](#allowsComparingTuples)
* [**cloneEmbeddable](#cloneEmbeddable)
* [**compareUuids](#compareUuids)
* [**convertDateToJSValue](#convertDateToJSValue)
* [**convertIntervalToDatabaseValue](#convertIntervalToDatabaseValue)
* [**convertIntervalToJSValue](#convertIntervalToJSValue)
* [**convertJsonToDatabaseValue](#convertjsontodatabasevalue)
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
* [**getBeginTransactionSQL](#getbegintransactionsql)
* [**getBigIntTypeDeclarationSQL](#getBigIntTypeDeclarationSQL)
* [**getBlobDeclarationSQL](#getBlobDeclarationSQL)
* [**getBooleanTypeDeclarationSQL](#getbooleantypedeclarationsql)
* [**getCommitTransactionSQL](#getCommitTransactionSQL)
* [**getConfig](#getConfig)
* [**getCurrentTimestampSQL](#getCurrentTimestampSQL)
* [**getDateTimeTypeDeclarationSQL](#getDateTimeTypeDeclarationSQL)
* [**getDateTypeDeclarationSQL](#getDateTypeDeclarationSQL)
* [**getDecimalTypeDeclarationSQL](#getDecimalTypeDeclarationSQL)
* [**getDefaultClientUrl](#getdefaultclienturl)
* [**getDefaultDateTimeLength](#getDefaultDateTimeLength)
* [**getDefaultCharLength](#getDefaultCharLength)
* [**getDefaultCharset](#getdefaultcharset)
* [**getDefaultMappedType](#getdefaultmappedtype)
* [**getDefaultPrimaryName](#getdefaultprimaryname)
* [**getDefaultSchemaName](#getDefaultSchemaName)
* [**getDefaultVarcharLength](#getDefaultVarcharLength)
* [**getDefaultVersionLength](#getDefaultVersionLength)
* [**getDoubleDeclarationSQL](#getDoubleDeclarationSQL)
* [**getEnumTypeDeclarationSQL](#getEnumTypeDeclarationSQL)
* [**getExceptionConverter](#getExceptionConverter)
* [**getExtension](#getExtension)
* [**getFloatDeclarationSQL](#getFloatDeclarationSQL)
* [**getFullTextIndexExpression](#getfulltextindexexpression)
* [**getFullTextWhereClause](#getfulltextwhereclause)
* [**getCharTypeDeclarationSQL](#getCharTypeDeclarationSQL)
* [**getIndexName](#getindexname)
* [**getIntegerTypeDeclarationSQL](#getIntegerTypeDeclarationSQL)
* [**getIntervalTypeDeclarationSQL](#getIntervalTypeDeclarationSQL)
* [**getJsonDeclarationSQL](#getJsonDeclarationSQL)
* [**getJsonIndexDefinition](#getjsonindexdefinition)
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
* [**isNumericColumn](#isnumericcolumn)
* [**isNumericProperty](#isNumericProperty)
* [**isPopulated](#isPopulated)
* [**lookupExtensions](#lookupExtensions)
* [**mapRegExpCondition](#mapRegExpCondition)
* [**marshallArray](#marshallArray)
* [**normalizeColumnType](#normalizecolumntype)
* [**normalizePrimaryKey](#normalizePrimaryKey)
* [**parseDate](#parseDate)
* [**processDateProperty](#processDateProperty)
* [**processJsonCondition](#processJsonCondition)
* [**quoteIdentifier](#quoteIdentifier)
* [**quoteValue](#quoteValue)
* [**setConfig](#setConfig)
* [**shouldHaveColumn](#shouldHaveColumn)
* [**supportsCreatingFullTextIndex](#supportscreatingfulltextindex)
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
* [**supportsUnsigned](#supportsunsigned)
* [**unmarshallArray](#unmarshallArray)
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

* ****new BaseMySqlPlatform**(): [BaseMySqlPlatform](https://mikro-orm.io/api/sql/class/BaseMySqlPlatform.md)

* Inherited from AbstractSqlPlatform.constructor

  #### Returns [BaseMySqlPlatform](https://mikro-orm.io/api/sql/class/BaseMySqlPlatform.md)

## Methods<!-- -->[**](#methods)

### [**](#allowsComparingTuples)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L210)inheritedallowsComparingTuples

* ****allowsComparingTuples**(): boolean

* Inherited from AbstractSqlPlatform.allowsComparingTuples

  #### Returns boolean

### [**](#cloneEmbeddable)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L649)inheritedcloneEmbeddable

* ****cloneEmbeddable**\<T>(data): T

* Inherited from AbstractSqlPlatform.cloneEmbeddable

  #### Parameters

  * ##### data: T

  #### Returns T

### [**](#compareUuids)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L518)inheritedcompareUuids

* ****compareUuids**(): string

* Inherited from AbstractSqlPlatform.compareUuids

  Determines how UUID values are compared in the change set tracking. Return `'string'` for inline string comparison (fast), or `'any'` for deep comparison via type methods.

  ***

  #### Returns string

### [**](#convertDateToJSValue)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L498)inheritedconvertDateToJSValue

* ****convertDateToJSValue**(value): string

* Inherited from AbstractSqlPlatform.convertDateToJSValue

  #### Parameters

  * ##### value: string | Date

  #### Returns string

### [**](#convertIntervalToDatabaseValue)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L506)inheritedconvertIntervalToDatabaseValue

* ****convertIntervalToDatabaseValue**(value): unknown

* Inherited from AbstractSqlPlatform.convertIntervalToDatabaseValue

  #### Parameters

  * ##### value: unknown

  #### Returns unknown

### [**](#convertIntervalToJSValue)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L502)inheritedconvertIntervalToJSValue

* ****convertIntervalToJSValue**(value): unknown

* Inherited from AbstractSqlPlatform.convertIntervalToJSValue

  #### Parameters

  * ##### value: string

  #### Returns unknown

### [**](#convertjsontodatabasevalue)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/dialects/mysql/BaseMySqlPlatform.ts#L69)convertJsonToDatabaseValue

* ****convertJsonToDatabaseValue**(value, context): unknown

* Overrides AbstractSqlPlatform.convertJsonToDatabaseValue

  #### Parameters

  * ##### value: unknown

  * ##### optionalcontext: [TransformContext](https://mikro-orm.io/api/core/interface/TransformContext.md)

  #### Returns unknown

### [**](#convertJsonToJSValue)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L494)inheritedconvertJsonToJSValue

* ****convertJsonToJSValue**(value, context): unknown

* Inherited from AbstractSqlPlatform.convertJsonToJSValue

  #### Parameters

  * ##### value: unknown

  * ##### optionalcontext: [TransformContext](https://mikro-orm.io/api/core/interface/TransformContext.md)

  #### Returns unknown

### [**](#convertsJsonAutomatically)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L486)inheritedconvertsJsonAutomatically

* ****convertsJsonAutomatically**(): boolean

* Inherited from AbstractSqlPlatform.convertsJsonAutomatically

  #### Returns boolean

### [**](#convertUuidToDatabaseValue)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L526)inheritedconvertUuidToDatabaseValue

* ****convertUuidToDatabaseValue**(value): unknown

* Inherited from AbstractSqlPlatform.convertUuidToDatabaseValue

  #### Parameters

  * ##### value: unknown

  #### Returns unknown

### [**](#convertUuidToJSValue)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L522)inheritedconvertUuidToJSValue

* ****convertUuidToJSValue**(value): unknown

* Inherited from AbstractSqlPlatform.convertUuidToJSValue

  #### Parameters

  * ##### value: unknown

  #### Returns unknown

### [**](#convertVersionValue)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L199)inheritedconvertVersionValue

* ****convertVersionValue**(value, prop): string | number | Date | { $in: (string | number)\[] }

* Inherited from AbstractSqlPlatform.convertVersionValue

  #### Parameters

  * ##### value: number | Date

  * ##### prop: [EntityProperty](https://mikro-orm.io/api/core/interface/EntityProperty.md)\<any, any>

  #### Returns string | number | Date | { $in: (string | number)\[] }

### [**](#denormalizePrimaryKey)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L141)inheriteddenormalizePrimaryKey

* ****denormalizePrimaryKey**(data): IPrimaryKeyValue

* Inherited from AbstractSqlPlatform.denormalizePrimaryKey

  Converts scalar primary key representation to native driver wrapper (e.g. string to mongodb's ObjectId)

  ***

  #### Parameters

  * ##### data: IPrimaryKeyValue

  #### Returns IPrimaryKeyValue

### [**](#escape)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L602)inheritedescape

* ****escape**(value): string

* Inherited from AbstractSqlPlatform.escape

  #### Parameters

  * ##### value: any

  #### Returns string

### [**](#extractSimpleType)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L296)inheritedextractSimpleType

* ****extractSimpleType**(type): string

* Inherited from AbstractSqlPlatform.extractSimpleType

  #### Parameters

  * ##### type: string

  #### Returns string

### [**](#formatQuery)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L606)inheritedformatQuery

* ****formatQuery**(sql, params): string

* Inherited from AbstractSqlPlatform.formatQuery

  #### Parameters

  * ##### sql: string

  * ##### params: readonly<!-- --> any\[]

  #### Returns string

### [**](#generateCustomOrder)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/AbstractSqlPlatform.ts#L148)inheritedgenerateCustomOrder

* ****generateCustomOrder**(escapedColumn, values): string

* Inherited from AbstractSqlPlatform.generateCustomOrder

  Generates a custom order by statement given a set of in order values, eg. ORDER BY (CASE WHEN priority = 'low' THEN 1 WHEN priority = 'medium' THEN 2 ELSE NULL END)

  ***

  #### Parameters

  * ##### escapedColumn: string

  * ##### values: unknown\[]

  #### Returns string

### [**](#getArrayDeclarationSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L394)inheritedgetArrayDeclarationSQL

* ****getArrayDeclarationSQL**(): string

* Inherited from AbstractSqlPlatform.getArrayDeclarationSQL

  #### Returns string

### [**](#getbegintransactionsql)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/dialects/mysql/BaseMySqlPlatform.ts#L49)getBeginTransactionSQL

* ****getBeginTransactionSQL**(options): string\[]

* Overrides AbstractSqlPlatform.getBeginTransactionSQL

  #### Parameters

  * ##### optionaloptions: { isolationLevel?<!-- -->: [IsolationLevel](https://mikro-orm.io/api/core/enum/IsolationLevel.md); readOnly?<!-- -->: boolean }

    * ##### optionalisolationLevel: [IsolationLevel](https://mikro-orm.io/api/core/enum/IsolationLevel.md)

    * ##### optionalreadOnly: boolean

  #### Returns string\[]

### [**](#getBigIntTypeDeclarationSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L242)inheritedgetBigIntTypeDeclarationSQL

* ****getBigIntTypeDeclarationSQL**(column): string

* Inherited from AbstractSqlPlatform.getBigIntTypeDeclarationSQL

  #### Parameters

  * ##### column: { autoincrement?<!-- -->: boolean; length?<!-- -->: number; unsigned?<!-- -->: boolean }

    * ##### optionalautoincrement: boolean

    * ##### optionallength: number

    * ##### optionalunsigned: boolean

  #### Returns string

### [**](#getBlobDeclarationSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L410)inheritedgetBlobDeclarationSQL

* ****getBlobDeclarationSQL**(): string

* Inherited from AbstractSqlPlatform.getBlobDeclarationSQL

  #### Returns string

### [**](#getbooleantypedeclarationsql)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/dialects/mysql/BaseMySqlPlatform.ts#L88)getBooleanTypeDeclarationSQL

* ****getBooleanTypeDeclarationSQL**(): string

* Overrides AbstractSqlPlatform.getBooleanTypeDeclarationSQL

  #### Returns string

### [**](#getCommitTransactionSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/AbstractSqlPlatform.ts#L66)inheritedgetCommitTransactionSQL

* ****getCommitTransactionSQL**(): string

* Inherited from AbstractSqlPlatform.getCommitTransactionSQL

  #### Returns string

### [**](#getConfig)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L668)inheritedgetConfig

* ****getConfig**(): [Configuration](https://mikro-orm.io/api/core/class/Configuration.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>, [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>>

* Inherited from AbstractSqlPlatform.getConfig

  #### Returns [Configuration](https://mikro-orm.io/api/core/class/Configuration.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>, [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>>

### [**](#getCurrentTimestampSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L148)inheritedgetCurrentTimestampSQL

* ****getCurrentTimestampSQL**(length): string

* Inherited from AbstractSqlPlatform.getCurrentTimestampSQL

  Returns the SQL specific for the platform to get the current timestamp

  ***

  #### Parameters

  * ##### optionallength: number

  #### Returns string

### [**](#getDateTimeTypeDeclarationSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L152)inheritedgetDateTimeTypeDeclarationSQL

* ****getDateTimeTypeDeclarationSQL**(column): string

* Inherited from AbstractSqlPlatform.getDateTimeTypeDeclarationSQL

  #### Parameters

  * ##### column: { length?<!-- -->: number }

    * ##### optionallength: number

  #### Returns string

### [**](#getDateTypeDeclarationSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L168)inheritedgetDateTypeDeclarationSQL

* ****getDateTypeDeclarationSQL**(length): string

* Inherited from AbstractSqlPlatform.getDateTypeDeclarationSQL

  #### Parameters

  * ##### optionallength: number

  #### Returns string

### [**](#getDecimalTypeDeclarationSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L284)inheritedgetDecimalTypeDeclarationSQL

* ****getDecimalTypeDeclarationSQL**(column): string

* Inherited from AbstractSqlPlatform.getDecimalTypeDeclarationSQL

  #### Parameters

  * ##### column: { precision?<!-- -->: number; scale?<!-- -->: number }

    * ##### optionalprecision: number

    * ##### optionalscale: number

  #### Returns string

### [**](#getdefaultclienturl)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/dialects/mysql/BaseMySqlPlatform.ts#L197)getDefaultClientUrl

* ****getDefaultClientUrl**(): string

* Overrides AbstractSqlPlatform.getDefaultClientUrl

  Returns default client url for given driver (e.g. mongodb://127.0.0.1:27017 for mongodb)

  ***

  #### Returns string

### [**](#getDefaultDateTimeLength)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L156)inheritedgetDefaultDateTimeLength

* ****getDefaultDateTimeLength**(): number

* Inherited from AbstractSqlPlatform.getDefaultDateTimeLength

  #### Returns number

### [**](#getDefaultCharLength)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L164)inheritedgetDefaultCharLength

* ****getDefaultCharLength**(): number

* Inherited from AbstractSqlPlatform.getDefaultCharLength

  #### Returns number

### [**](#getdefaultcharset)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/dialects/mysql/BaseMySqlPlatform.ts#L40)getDefaultCharset

* ****getDefaultCharset**(): string

* Overrides AbstractSqlPlatform.getDefaultCharset

  #### Returns string

### [**](#getdefaultmappedtype)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/dialects/mysql/BaseMySqlPlatform.ts#L102)getDefaultMappedType

* ****getDefaultMappedType**(type): [Type](https://mikro-orm.io/api/core/class/Type.md)\<unknown, unknown>

* Overrides AbstractSqlPlatform.getDefaultMappedType

  #### Parameters

  * ##### type: string

  #### Returns [Type](https://mikro-orm.io/api/core/class/Type.md)\<unknown, unknown>

### [**](#getdefaultprimaryname)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/dialects/mysql/BaseMySqlPlatform.ts#L140)getDefaultPrimaryName

* ****getDefaultPrimaryName**(tableName, columns): string

* Overrides AbstractSqlPlatform.getDefaultPrimaryName

  #### Parameters

  * ##### tableName: string

  * ##### columns: string\[]

  #### Returns string

### [**](#getDefaultSchemaName)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L218)inheritedgetDefaultSchemaName

* ****getDefaultSchemaName**(): undefined | string

* Inherited from AbstractSqlPlatform.getDefaultSchemaName

  #### Returns undefined | string

### [**](#getDefaultVarcharLength)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L160)inheritedgetDefaultVarcharLength

* ****getDefaultVarcharLength**(): number

* Inherited from AbstractSqlPlatform.getDefaultVarcharLength

  #### Returns number

### [**](#getDefaultVersionLength)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L206)inheritedgetDefaultVersionLength

* ****getDefaultVersionLength**(): number

* Inherited from AbstractSqlPlatform.getDefaultVersionLength

  #### Returns number

### [**](#getDoubleDeclarationSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L280)inheritedgetDoubleDeclarationSQL

* ****getDoubleDeclarationSQL**(): string

* Inherited from AbstractSqlPlatform.getDoubleDeclarationSQL

  #### Returns string

### [**](#getEnumTypeDeclarationSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L262)inheritedgetEnumTypeDeclarationSQL

* ****getEnumTypeDeclarationSQL**(column): string

* Inherited from AbstractSqlPlatform.getEnumTypeDeclarationSQL

  #### Parameters

  * ##### column: { autoincrement?<!-- -->: boolean; fieldNames: string\[]; items?<!-- -->: unknown\[]; length?<!-- -->: number; unsigned?<!-- -->: boolean }

    * ##### optionalautoincrement: boolean

    * ##### fieldNames: string\[]

    * ##### optionalitems: unknown\[]

    * ##### optionallength: number

    * ##### optionalunsigned: boolean

  #### Returns string

### [**](#getExceptionConverter)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L549)inheritedgetExceptionConverter

* ****getExceptionConverter**(): [ExceptionConverter](https://mikro-orm.io/api/core/class/ExceptionConverter.md)

* Inherited from AbstractSqlPlatform.getExceptionConverter

  #### Returns [ExceptionConverter](https://mikro-orm.io/api/core/class/ExceptionConverter.md)

### [**](#getExtension)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L565)inheritedgetExtension

* ****getExtension**\<T>(extensionName, extensionKey, moduleName, em): T

* Inherited from AbstractSqlPlatform.getExtension

  #### Parameters

  * ##### extensionName: string

  * ##### extensionKey: string

  * ##### moduleName: string

  * ##### em: [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>

  #### Returns T

### [**](#getFloatDeclarationSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L276)inheritedgetFloatDeclarationSQL

* ****getFloatDeclarationSQL**(): string

* Inherited from AbstractSqlPlatform.getFloatDeclarationSQL

  #### Returns string

### [**](#getfulltextindexexpression)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/dialects/mysql/BaseMySqlPlatform.ts#L152)getFullTextIndexExpression

* ****getFullTextIndexExpression**(indexName, schemaName, tableName, columns): string

* Overrides AbstractSqlPlatform.getFullTextIndexExpression

  #### Parameters

  * ##### indexName: string

  * ##### schemaName: undefined | string

  * ##### tableName: string

  * ##### columns: [SimpleColumnMeta](https://mikro-orm.io/api/core/interface/SimpleColumnMeta.md)\[]

  #### Returns string

### [**](#getfulltextwhereclause)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/dialects/mysql/BaseMySqlPlatform.ts#L148)getFullTextWhereClause

* ****getFullTextWhereClause**(): string

* Overrides AbstractSqlPlatform.getFullTextWhereClause

  #### Returns string

### [**](#getCharTypeDeclarationSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L246)inheritedgetCharTypeDeclarationSQL

* ****getCharTypeDeclarationSQL**(column): string

* Inherited from AbstractSqlPlatform.getCharTypeDeclarationSQL

  #### Parameters

  * ##### column: { length?<!-- -->: number }

    * ##### optionallength: number

  #### Returns string

### [**](#getindexname)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/dialects/mysql/BaseMySqlPlatform.ts#L122)getIndexName

* ****getIndexName**(tableName, columns, type): string

* Overrides AbstractSqlPlatform.getIndexName

  Returns the default name of index for the given columns cannot go past 64 character length for identifiers in MySQL

  ***

  #### Parameters

  * ##### tableName: string

  * ##### columns: string\[]

  * ##### type: primary | index | unique | foreign | sequence

  #### Returns string

### [**](#getIntegerTypeDeclarationSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L226)inheritedgetIntegerTypeDeclarationSQL

* ****getIntegerTypeDeclarationSQL**(column): string

* Inherited from AbstractSqlPlatform.getIntegerTypeDeclarationSQL

  #### Parameters

  * ##### column: { autoincrement?<!-- -->: boolean; length?<!-- -->: number; unsigned?<!-- -->: boolean }

    * ##### optionalautoincrement: boolean

    * ##### optionallength: number

    * ##### optionalunsigned: boolean

  #### Returns string

### [**](#getIntervalTypeDeclarationSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L254)inheritedgetIntervalTypeDeclarationSQL

* ****getIntervalTypeDeclarationSQL**(column): string

* Inherited from AbstractSqlPlatform.getIntervalTypeDeclarationSQL

  #### Parameters

  * ##### column: { length?<!-- -->: number }

    * ##### optionallength: number

  #### Returns string

### [**](#getJsonDeclarationSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L414)inheritedgetJsonDeclarationSQL

* ****getJsonDeclarationSQL**(): string

* Inherited from AbstractSqlPlatform.getJsonDeclarationSQL

  #### Returns string

### [**](#getjsonindexdefinition)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/dialects/mysql/BaseMySqlPlatform.ts#L77)getJsonIndexDefinition

* ****getJsonIndexDefinition**(index): string\[]

* Overrides AbstractSqlPlatform.getJsonIndexDefinition

  #### Parameters

  * ##### index: [IndexDef](https://mikro-orm.io/api/sql/interface/IndexDef.md)

  #### Returns string\[]

### [**](#getMappedType)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L307)inheritedgetMappedType

* ****getMappedType**(type): [Type](https://mikro-orm.io/api/core/class/Type.md)\<unknown, unknown>

* Inherited from AbstractSqlPlatform.getMappedType

  #### Parameters

  * ##### type: string

  #### Returns [Type](https://mikro-orm.io/api/core/class/Type.md)\<unknown, unknown>

### [**](#getMediumIntTypeDeclarationSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L234)inheritedgetMediumIntTypeDeclarationSQL

* ****getMediumIntTypeDeclarationSQL**(column): string

* Inherited from AbstractSqlPlatform.getMediumIntTypeDeclarationSQL

  #### Parameters

  * ##### column: { autoincrement?<!-- -->: boolean; length?<!-- -->: number; unsigned?<!-- -->: boolean }

    * ##### optionalautoincrement: boolean

    * ##### optionallength: number

    * ##### optionalunsigned: boolean

  #### Returns string

### [**](#getNamingStrategy)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L75)inheritedgetNamingStrategy

* ****getNamingStrategy**(): new () => [NamingStrategy](https://mikro-orm.io/api/core/interface/NamingStrategy.md)

* Inherited from AbstractSqlPlatform.getNamingStrategy

  #### Returns new () => [NamingStrategy](https://mikro-orm.io/api/core/interface/NamingStrategy.md)

  * * **new (): [NamingStrategy](https://mikro-orm.io/api/core/interface/NamingStrategy.md)

    * #### Returns [NamingStrategy](https://mikro-orm.io/api/core/interface/NamingStrategy.md)

### [**](#getRegExpOperator)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L176)inheritedgetRegExpOperator

* ****getRegExpOperator**(val, flags): string

* Inherited from AbstractSqlPlatform.getRegExpOperator

  #### Parameters

  * ##### optionalval: unknown

  * ##### optionalflags: string

  #### Returns string

### [**](#getRegExpValue)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L187)inheritedgetRegExpValue

* ****getRegExpValue**(val): { $flags?
  <!-- -->
  : string; $re: string }

* Inherited from AbstractSqlPlatform.getRegExpValue

  #### Parameters

  * ##### val: RegExp

  #### Returns { $flags?<!-- -->: string; $re: string }

  * ##### optional$flags?<!-- -->: string

  * ##### $re: string

### [**](#getReleaseSavepointSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/AbstractSqlPlatform.ts#L82)inheritedgetReleaseSavepointSQL

* ****getReleaseSavepointSQL**(savepointName): string

* Inherited from AbstractSqlPlatform.getReleaseSavepointSQL

  #### Parameters

  * ##### savepointName: string

  #### Returns string

### [**](#getRepositoryClass)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/AbstractSqlPlatform.ts#L34)inheritedgetRepositoryClass

* ****getRepositoryClass**\<T>(): [Constructor](https://mikro-orm.io/api/core.md#Constructor)<[EntityRepository](https://mikro-orm.io/api/core/class/EntityRepository.md)\<T>>

* Inherited from AbstractSqlPlatform.getRepositoryClass

  #### Returns [Constructor](https://mikro-orm.io/api/core.md#Constructor)<[EntityRepository](https://mikro-orm.io/api/core/class/EntityRepository.md)\<T>>

### [**](#getRollbackToSavepointSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/AbstractSqlPlatform.ts#L78)inheritedgetRollbackToSavepointSQL

* ****getRollbackToSavepointSQL**(savepointName): string

* Inherited from AbstractSqlPlatform.getRollbackToSavepointSQL

  #### Parameters

  * ##### savepointName: string

  #### Returns string

### [**](#getRollbackTransactionSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/AbstractSqlPlatform.ts#L70)inheritedgetRollbackTransactionSQL

* ****getRollbackTransactionSQL**(): string

* Inherited from AbstractSqlPlatform.getRollbackTransactionSQL

  #### Returns string

### [**](#getSavepointSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/AbstractSqlPlatform.ts#L74)inheritedgetSavepointSQL

* ****getSavepointSQL**(savepointName): string

* Inherited from AbstractSqlPlatform.getSavepointSQL

  #### Parameters

  * ##### savepointName: string

  #### Returns string

### [**](#getSearchJsonPropertyKey)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/AbstractSqlPlatform.ts#L102)inheritedgetSearchJsonPropertyKey

* ****getSearchJsonPropertyKey**(path, type, aliased, value): string | [RawQueryFragment](https://mikro-orm.io/api/core/class/RawQueryFragment.md)\<string>

* Inherited from AbstractSqlPlatform.getSearchJsonPropertyKey

  #### Parameters

  * ##### path: string\[]

  * ##### type: string

  * ##### aliased: boolean

  * ##### optionalvalue: unknown

  #### Returns string | [RawQueryFragment](https://mikro-orm.io/api/core/class/RawQueryFragment.md)\<string>

### [**](#getSearchJsonPropertySQL)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/AbstractSqlPlatform.ts#L98)inheritedgetSearchJsonPropertySQL

* ****getSearchJsonPropertySQL**(path, type, aliased): string | [RawQueryFragment](https://mikro-orm.io/api/core/class/RawQueryFragment.md)\<string>

* Inherited from AbstractSqlPlatform.getSearchJsonPropertySQL

  #### Parameters

  * ##### path: string

  * ##### type: string

  * ##### aliased: boolean

  #### Returns string | [RawQueryFragment](https://mikro-orm.io/api/core/class/RawQueryFragment.md)\<string>

### [**](#getSchemaGenerator)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/AbstractSqlPlatform.ts#L48)inheritedgetSchemaGenerator

* ****getSchemaGenerator**(driver, em): [SqlSchemaGenerator](https://mikro-orm.io/api/sql/class/SqlSchemaGenerator.md)

* Inherited from AbstractSqlPlatform.getSchemaGenerator

  #### Parameters

  * ##### driver: [IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>

  * ##### optionalem: [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>

  #### Returns [SqlSchemaGenerator](https://mikro-orm.io/api/sql/class/SqlSchemaGenerator.md)

### [**](#getSchemaHelper)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/AbstractSqlPlatform.ts#L38)inheritedgetSchemaHelper

* ****getSchemaHelper**(): undefined | [SchemaHelper](https://mikro-orm.io/api/sql/class/SchemaHelper.md)

* Inherited from AbstractSqlPlatform.getSchemaHelper

  #### Returns undefined | [SchemaHelper](https://mikro-orm.io/api/sql/class/SchemaHelper.md)

### [**](#getSmallIntTypeDeclarationSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L230)inheritedgetSmallIntTypeDeclarationSQL

* ****getSmallIntTypeDeclarationSQL**(column): string

* Inherited from AbstractSqlPlatform.getSmallIntTypeDeclarationSQL

  #### Parameters

  * ##### column: { autoincrement?<!-- -->: boolean; length?<!-- -->: number; unsigned?<!-- -->: boolean }

    * ##### optionalautoincrement: boolean

    * ##### optionallength: number

    * ##### optionalunsigned: boolean

  #### Returns string

### [**](#getTextTypeDeclarationSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L258)inheritedgetTextTypeDeclarationSQL

* ****getTextTypeDeclarationSQL**(\_column): string

* Inherited from AbstractSqlPlatform.getTextTypeDeclarationSQL

  #### Parameters

  * ##### \_column: { length?<!-- -->: number }

    * ##### optionallength: number

  #### Returns string

### [**](#getTimeTypeDeclarationSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L172)inheritedgetTimeTypeDeclarationSQL

* ****getTimeTypeDeclarationSQL**(length): string

* Inherited from AbstractSqlPlatform.getTimeTypeDeclarationSQL

  #### Parameters

  * ##### optionallength: number

  #### Returns string

### [**](#getTimezone)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L672)inheritedgetTimezone

* ****getTimezone**(): undefined | string

* Inherited from AbstractSqlPlatform.getTimezone

  #### Returns undefined | string

### [**](#getTinyIntTypeDeclarationSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L238)inheritedgetTinyIntTypeDeclarationSQL

* ****getTinyIntTypeDeclarationSQL**(column): string

* Inherited from AbstractSqlPlatform.getTinyIntTypeDeclarationSQL

  #### Parameters

  * ##### column: { autoincrement?<!-- -->: boolean; length?<!-- -->: number; unsigned?<!-- -->: boolean }

    * ##### optionalautoincrement: boolean

    * ##### optionallength: number

    * ##### optionalunsigned: boolean

  #### Returns string

### [**](#getUuidTypeDeclarationSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L291)inheritedgetUuidTypeDeclarationSQL

* ****getUuidTypeDeclarationSQL**(column): string

* Inherited from AbstractSqlPlatform.getUuidTypeDeclarationSQL

  #### Parameters

  * ##### column: { length?<!-- -->: number }

    * ##### optionallength: number

  #### Returns string

### [**](#getVarcharTypeDeclarationSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L250)inheritedgetVarcharTypeDeclarationSQL

* ****getVarcharTypeDeclarationSQL**(column): string

* Inherited from AbstractSqlPlatform.getVarcharTypeDeclarationSQL

  #### Parameters

  * ##### column: { length?<!-- -->: number }

    * ##### optionallength: number

  #### Returns string

### [**](#indexForeignKeys)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/AbstractSqlPlatform.ts#L30)inheritedindexForeignKeys

* ****indexForeignKeys**(): boolean

* Inherited from AbstractSqlPlatform.indexForeignKeys

  #### Returns boolean

### [**](#isAllowedTopLevelOperator)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L195)inheritedisAllowedTopLevelOperator

* ****isAllowedTopLevelOperator**(operator): boolean

* Inherited from AbstractSqlPlatform.isAllowedTopLevelOperator

  #### Parameters

  * ##### operator: string

  #### Returns boolean

### [**](#isBigIntProperty)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L214)inheritedisBigIntProperty

* ****isBigIntProperty**(prop): boolean

* Inherited from AbstractSqlPlatform.isBigIntProperty

  #### Parameters

  * ##### prop: [EntityProperty](https://mikro-orm.io/api/core/interface/EntityProperty.md)\<any, any>

  #### Returns boolean

### [**](#isnumericcolumn)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/dialects/mysql/BaseMySqlPlatform.ts#L110)isNumericColumn

* ****isNumericColumn**(mappedType): boolean

* Overrides AbstractSqlPlatform.isNumericColumn

  #### Parameters

  * ##### mappedType: [Type](https://mikro-orm.io/api/core/class/Type.md)\<unknown, unknown>

  #### Returns boolean

### [**](#isNumericProperty)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L676)inheritedisNumericProperty

* ****isNumericProperty**(prop, ignoreCustomType): boolean

* Inherited from AbstractSqlPlatform.isNumericProperty

  #### Parameters

  * ##### prop: [EntityProperty](https://mikro-orm.io/api/core/interface/EntityProperty.md)\<any, any>

  * ##### ignoreCustomType: boolean = <!-- -->false

  #### Returns boolean

### [**](#isPopulated)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L708)inheritedisPopulated

* ****isPopulated**\<T>(key, populate): boolean

* Inherited from AbstractSqlPlatform.isPopulated

  #### Parameters

  * ##### key: string

  * ##### populate: boolean | readonly<!-- --> [PopulateOptions](https://mikro-orm.io/api/core.md#PopulateOptions)\<T>\[]

  #### Returns boolean

### [**](#lookupExtensions)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/AbstractSqlPlatform.ts#L43)inheritedlookupExtensions

* ****lookupExtensions**(orm): void

* Inherited from AbstractSqlPlatform.lookupExtensions

  Allows registering extensions of the driver automatically (e.g. `SchemaGenerator` extension in SQL drivers).

  ***

  #### Parameters

  * ##### orm: [MikroORM](https://mikro-orm.io/api/core/class/MikroORM.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>, [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>, (string | [EntitySchema](https://mikro-orm.io/api/core/class/EntitySchema.md)\<any, never, [EntityCtor](https://mikro-orm.io/api/core.md#EntityCtor)\<any>> | [EntityClass](https://mikro-orm.io/api/core.md#EntityClass)\<Partial\<any>>)\[]>

  #### Returns void

### [**](#mapRegExpCondition)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L180)inheritedmapRegExpCondition

* ****mapRegExpCondition**(mappedKey, value): { params: unknown\[]; sql: string }

* Inherited from AbstractSqlPlatform.mapRegExpCondition

  #### Parameters

  * ##### mappedKey: string

  * ##### value: { $flags?<!-- -->: string; $re: string }

    * ##### optional$flags: string

    * ##### $re: string

  #### Returns { params: unknown\[]; sql: string }

  * ##### params: unknown\[]

  * ##### sql: string

### [**](#marshallArray)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L398)inheritedmarshallArray

* ****marshallArray**(values): string

* Inherited from AbstractSqlPlatform.marshallArray

  #### Parameters

  * ##### values: string\[]

  #### Returns string

### [**](#normalizecolumntype)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/dialects/mysql/BaseMySqlPlatform.ts#L92)normalizeColumnType

* ****normalizeColumnType**(type, options): string

* Overrides AbstractSqlPlatform.normalizeColumnType

  This should be used only to compare types, it can strip some information like the length.

  ***

  #### Parameters

  * ##### type: string

  * ##### options: { length?<!-- -->: number; precision?<!-- -->: number; scale?<!-- -->: number }

    * ##### optionallength: number

    * ##### optionalprecision: number

    * ##### optionalscale: number

  #### Returns string

### [**](#normalizePrimaryKey)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L134)inheritednormalizePrimaryKey

* ****normalizePrimaryKey**\<T>(data): T

* Inherited from AbstractSqlPlatform.normalizePrimaryKey

  Normalizes primary key wrapper to scalar value (e.g. mongodb's ObjectId to string)

  ***

  #### Parameters

  * ##### data: IPrimaryKeyValue | [Primary](https://mikro-orm.io/api/core.md#Primary)\<T>

  #### Returns T

### [**](#parseDate)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L530)inheritedparseDate

* ****parseDate**(value): Date

* Inherited from AbstractSqlPlatform.parseDate

  #### Parameters

  * ##### value: string | number

  #### Returns Date

### [**](#processDateProperty)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L583)inheritedprocessDateProperty

* ****processDateProperty**(value): string | number | Date

* Inherited from AbstractSqlPlatform.processDateProperty

  #### Parameters

  * ##### value: unknown

  #### Returns string | number | Date

### [**](#processJsonCondition)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L426)inheritedprocessJsonCondition

* ****processJsonCondition**\<T>(o, value, path, alias): [FilterQuery](https://mikro-orm.io/api/core.md#FilterQuery)\<T>

* Inherited from AbstractSqlPlatform.processJsonCondition

  #### Parameters

  * ##### o: [FilterQuery](https://mikro-orm.io/api/core.md#FilterQuery)\<T>

  * ##### value: [EntityValue](https://mikro-orm.io/api/core.md#EntityValue)\<T>

  * ##### path: [EntityKey](https://mikro-orm.io/api/core.md#EntityKey)\<T>\[]

  * ##### alias: boolean

  #### Returns [FilterQuery](https://mikro-orm.io/api/core.md#FilterQuery)\<T>

### [**](#quoteIdentifier)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L587)inheritedquoteIdentifier

* ****quoteIdentifier**(id, quote): string

* Inherited from AbstractSqlPlatform.quoteIdentifier

  #### Parameters

  * ##### id: string | { toString: () => string }

  * * ##### toString: () => string

    ##### quote: string = <!-- -->'\`'

  #### Returns string

### [**](#quoteValue)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/AbstractSqlPlatform.ts#L86)inheritedquoteValue

* ****quoteValue**(value): string

* Inherited from AbstractSqlPlatform.quoteValue

  #### Parameters

  * ##### value: any

  #### Returns string

### [**](#setConfig)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L657)inheritedsetConfig

* ****setConfig**(config): void

* Inherited from AbstractSqlPlatform.setConfig

  #### Parameters

  * ##### config: [Configuration](https://mikro-orm.io/api/core/class/Configuration.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>, [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>>

  #### Returns void

### [**](#shouldHaveColumn)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L712)inheritedshouldHaveColumn

* ****shouldHaveColumn**\<T>(prop, populate, exclude, includeFormulas, ignoreInlineEmbeddables): boolean

* Inherited from AbstractSqlPlatform.shouldHaveColumn

  #### Parameters

  * ##### prop: [EntityProperty](https://mikro-orm.io/api/core/interface/EntityProperty.md)\<T, any>

  * ##### populate: boolean | readonly<!-- --> [PopulateOptions](https://mikro-orm.io/api/core.md#PopulateOptions)\<T>\[]

  * ##### optionalexclude: string\[]

  * ##### includeFormulas: boolean = <!-- -->true

  * ##### ignoreInlineEmbeddables: boolean = <!-- -->true

  #### Returns boolean

### [**](#supportscreatingfulltextindex)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/dialects/mysql/BaseMySqlPlatform.ts#L144)supportsCreatingFullTextIndex

* ****supportsCreatingFullTextIndex**(): boolean

* Overrides AbstractSqlPlatform.supportsCreatingFullTextIndex

  #### Returns boolean

### [**](#supportsCustomPrimaryKeyNames)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L704)inheritedsupportsCustomPrimaryKeyNames

* ****supportsCustomPrimaryKeyNames**(): boolean

* Inherited from AbstractSqlPlatform.supportsCustomPrimaryKeyNames

  #### Returns boolean

### [**](#supportsDeferredUniqueConstraints)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L757)inheritedsupportsDeferredUniqueConstraints

* ****supportsDeferredUniqueConstraints**(): boolean

* Inherited from AbstractSqlPlatform.supportsDeferredUniqueConstraints

  #### Returns boolean

### [**](#supportsDownMigrations)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L753)inheritedsupportsDownMigrations

* ****supportsDownMigrations**(): boolean

* Inherited from AbstractSqlPlatform.supportsDownMigrations

  Currently not supported due to how knex does complex sqlite diffing (always based on current schema)

  ***

  #### Returns boolean

### [**](#supportsMaterializedViews)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L101)inheritedsupportsMaterializedViews

* ****supportsMaterializedViews**(): boolean

* Inherited from AbstractSqlPlatform.supportsMaterializedViews

  #### Returns boolean

### [**](#supportsMultipleCascadePaths)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L374)inheritedsupportsMultipleCascadePaths

* ****supportsMultipleCascadePaths**(): boolean

* Inherited from AbstractSqlPlatform.supportsMultipleCascadePaths

  #### Returns boolean

### [**](#supportsMultipleStatements)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L386)inheritedsupportsMultipleStatements

* ****supportsMultipleStatements**(): boolean

* Inherited from AbstractSqlPlatform.supportsMultipleStatements

  #### Returns boolean

### [**](#supportsNativeEnums)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L92)inheritedsupportsNativeEnums

* ****supportsNativeEnums**(): boolean

* Inherited from AbstractSqlPlatform.supportsNativeEnums

  for postgres native enums

  ***

  #### Returns boolean

### [**](#supportsOnUpdate)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L382)inheritedsupportsOnUpdate

* ****supportsOnUpdate**(): boolean

* Inherited from AbstractSqlPlatform.supportsOnUpdate

  Returns true if the platform supports ON UPDATE foreign key rules. Oracle doesn't support ON UPDATE rules.

  ***

  #### Returns boolean

### [**](#supportsSchemas)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/AbstractSqlPlatform.ts#L143)inheritedsupportsSchemas

* ****supportsSchemas**(): boolean

* Inherited from AbstractSqlPlatform.supportsSchemas

  #### Returns boolean

### [**](#supportsTransactions)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L67)inheritedsupportsTransactions

* ****supportsTransactions**(): boolean

* Inherited from AbstractSqlPlatform.supportsTransactions

  #### Returns boolean

### [**](#supportsUnionWhere)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/AbstractSqlPlatform.ts#L139)inheritedsupportsUnionWhere

* ****supportsUnionWhere**(): boolean

* Inherited from AbstractSqlPlatform.supportsUnionWhere

  #### Returns boolean

### [**](#supportsunsigned)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/dialects/mysql/BaseMySqlPlatform.ts#L114)supportsUnsigned

* ****supportsUnsigned**(): boolean

* Overrides AbstractSqlPlatform.supportsUnsigned

  #### Returns boolean

### [**](#unmarshallArray)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L402)inheritedunmarshallArray

* ****unmarshallArray**(value): string\[]

* Inherited from AbstractSqlPlatform.unmarshallArray

  #### Parameters

  * ##### value: string

  #### Returns string\[]

### [**](#usesAsKeyword)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L510)inheritedusesAsKeyword

* ****usesAsKeyword**(): boolean

* Inherited from AbstractSqlPlatform.usesAsKeyword

  #### Returns boolean

### [**](#usesBatchInserts)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L116)inheritedusesBatchInserts

* ****usesBatchInserts**(): boolean

* Inherited from AbstractSqlPlatform.usesBatchInserts

  Whether or not the driver supports retuning list of created PKs back when multi-inserting

  ***

  #### Returns boolean

### [**](#usesBatchUpdates)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L123)inheritedusesBatchUpdates

* ****usesBatchUpdates**(): boolean

* Inherited from AbstractSqlPlatform.usesBatchUpdates

  Whether or not the driver supports updating many records at once

  ***

  #### Returns boolean

### [**](#usesCascadeStatement)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L87)inheritedusesCascadeStatement

* ****usesCascadeStatement**(): boolean

* Inherited from AbstractSqlPlatform.usesCascadeStatement

  #### Returns boolean

### [**](#usesDefaultKeyword)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L127)inheritedusesDefaultKeyword

* ****usesDefaultKeyword**(): boolean

* Inherited from AbstractSqlPlatform.usesDefaultKeyword

  #### Returns boolean

### [**](#usesEnumCheckConstraints)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L97)inheritedusesEnumCheckConstraints

* ****usesEnumCheckConstraints**(): boolean

* Inherited from AbstractSqlPlatform.usesEnumCheckConstraints

  for postgres text enums (default)

  ***

  #### Returns boolean

### [**](#usesImplicitTransactions)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L71)inheritedusesImplicitTransactions

* ****usesImplicitTransactions**(): boolean

* Inherited from AbstractSqlPlatform.usesImplicitTransactions

  #### Returns boolean

### [**](#usesOutputStatement)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L83)inheritedusesOutputStatement

* ****usesOutputStatement**(): boolean

* Inherited from AbstractSqlPlatform.usesOutputStatement

  #### Returns boolean

### [**](#usesPivotTable)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/AbstractSqlPlatform.ts#L26)inheritedusesPivotTable

* ****usesPivotTable**(): boolean

* Inherited from AbstractSqlPlatform.usesPivotTable

  #### Returns boolean

### [**](#usesReturningStatement)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L79)inheritedusesReturningStatement

* ****usesReturningStatement**(): boolean

* Inherited from AbstractSqlPlatform.usesReturningStatement

  #### Returns boolean

### [**](#validateMetadata)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L761)inheritedvalidateMetadata

* ****validateMetadata**(meta): void

* Inherited from AbstractSqlPlatform.validateMetadata

  #### Parameters

  * ##### meta: [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<any, [EntityCtor](https://mikro-orm.io/api/core.md#EntityCtor)\<any>>

  #### Returns void
