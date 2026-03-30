# Source: https://mikro-orm.io/api/oracledb/class/OraclePlatform.md

# OraclePlatform<!-- -->

### Hierarchy

* [AbstractSqlPlatform](https://mikro-orm.io/api/sql/class/AbstractSqlPlatform.md)
  * *OraclePlatform*

## Index[**](#index)

### Constructors

* [**constructor](#constructor)

### Methods

* [**allowsComparingTuples](#allowscomparingtuples)
* [**cloneEmbeddable](#cloneEmbeddable)
* [**compareUuids](#compareuuids)
* [**convertDateToJSValue](#convertDateToJSValue)
* [**convertIntervalToDatabaseValue](#convertIntervalToDatabaseValue)
* [**convertIntervalToJSValue](#convertIntervalToJSValue)
* [**convertJsonToDatabaseValue](#convertJsonToDatabaseValue)
* [**convertJsonToJSValue](#convertJsonToJSValue)
* [**convertsJsonAutomatically](#convertsjsonautomatically)
* [**convertUuidToDatabaseValue](#convertuuidtodatabasevalue)
* [**convertUuidToJSValue](#convertuuidtojsvalue)
* [**convertVersionValue](#convertVersionValue)
* [**createOutBindings](#createoutbindings)
* [**denormalizePrimaryKey](#denormalizePrimaryKey)
* [**escape](#escape)
* [**extractSimpleType](#extractSimpleType)
* [**formatQuery](#formatQuery)
* [**generateCustomOrder](#generateCustomOrder)
* [**getArrayDeclarationSQL](#getarraydeclarationsql)
* [**getBeginTransactionSQL](#getbegintransactionsql)
* [**getBigIntTypeDeclarationSQL](#getbiginttypedeclarationsql)
* [**getBlobDeclarationSQL](#getblobdeclarationsql)
* [**getBooleanTypeDeclarationSQL](#getbooleantypedeclarationsql)
* [**getCommitTransactionSQL](#getCommitTransactionSQL)
* [**getConfig](#getConfig)
* [**getCurrentTimestampSQL](#getcurrenttimestampsql)
* [**getDateTimeTypeDeclarationSQL](#getdatetimetypedeclarationsql)
* [**getDateTypeDeclarationSQL](#getdatetypedeclarationsql)
* [**getDecimalTypeDeclarationSQL](#getdecimaltypedeclarationsql)
* [**getDefaultClientUrl](#getdefaultclienturl)
* [**getDefaultDateTimeLength](#getdefaultdatetimelength)
* [**getDefaultCharLength](#getDefaultCharLength)
* [**getDefaultCharset](#getDefaultCharset)
* [**getDefaultMappedType](#getdefaultmappedtype)
* [**getDefaultPrimaryName](#getDefaultPrimaryName)
* [**getDefaultSchemaName](#getdefaultschemaname)
* [**getDefaultVarcharLength](#getDefaultVarcharLength)
* [**getDefaultVersionLength](#getDefaultVersionLength)
* [**getDoubleDeclarationSQL](#getdoubledeclarationsql)
* [**getEnumTypeDeclarationSQL](#getenumtypedeclarationsql)
* [**getExceptionConverter](#getExceptionConverter)
* [**getExtension](#getExtension)
* [**getFloatDeclarationSQL](#getfloatdeclarationsql)
* [**getFullTextIndexExpression](#getFullTextIndexExpression)
* [**getFullTextWhereClause](#getFullTextWhereClause)
* [**getCharTypeDeclarationSQL](#getCharTypeDeclarationSQL)
* [**getIndexName](#getIndexName)
* [**getIntegerTypeDeclarationSQL](#getintegertypedeclarationsql)
* [**getIntervalTypeDeclarationSQL](#getIntervalTypeDeclarationSQL)
* [**getJsonDeclarationSQL](#getjsondeclarationsql)
* [**getJsonIndexDefinition](#getJsonIndexDefinition)
* [**getMappedType](#getMappedType)
* [**getMediumIntTypeDeclarationSQL](#getmediuminttypedeclarationsql)
* [**getNamingStrategy](#getNamingStrategy)
* [**getRegExpOperator](#getregexpoperator)
* [**getRegExpValue](#getRegExpValue)
* [**getReleaseSavepointSQL](#getReleaseSavepointSQL)
* [**getRepositoryClass](#getRepositoryClass)
* [**getRollbackToSavepointSQL](#getrollbacktosavepointsql)
* [**getRollbackTransactionSQL](#getRollbackTransactionSQL)
* [**getSavepointSQL](#getsavepointsql)
* [**getSearchJsonPropertyKey](#getsearchjsonpropertykey)
* [**getSearchJsonPropertySQL](#getSearchJsonPropertySQL)
* [**getSchemaGenerator](#getschemagenerator)
* [**getSchemaHelper](#getSchemaHelper)
* [**getSmallIntTypeDeclarationSQL](#getsmallinttypedeclarationsql)
* [**getTextTypeDeclarationSQL](#gettexttypedeclarationsql)
* [**getTimeTypeDeclarationSQL](#gettimetypedeclarationsql)
* [**getTimezone](#getTimezone)
* [**getTinyIntTypeDeclarationSQL](#gettinyinttypedeclarationsql)
* [**getUuidTypeDeclarationSQL](#getuuidtypedeclarationsql)
* [**getVarcharTypeDeclarationSQL](#getvarchartypedeclarationsql)
* [**indexForeignKeys](#indexforeignkeys)
* [**isAllowedTopLevelOperator](#isAllowedTopLevelOperator)
* [**isBigIntProperty](#isBigIntProperty)
* [**isNumericColumn](#isNumericColumn)
* [**isNumericProperty](#isNumericProperty)
* [**isPopulated](#isPopulated)
* [**lookupExtensions](#lookupextensions)
* [**mapRegExpCondition](#mapregexpcondition)
* [**mapToOracleType](#maptooracletype)
* [**marshallArray](#marshallArray)
* [**normalizeColumnType](#normalizecolumntype)
* [**normalizePrimaryKey](#normalizePrimaryKey)
* [**parseDate](#parseDate)
* [**processDateProperty](#processDateProperty)
* [**processJsonCondition](#processjsoncondition)
* [**quoteIdentifier](#quoteidentifier)
* [**quoteValue](#quoteValue)
* [**setConfig](#setConfig)
* [**shouldHaveColumn](#shouldHaveColumn)
* [**supportsCreatingFullTextIndex](#supportsCreatingFullTextIndex)
* [**supportsCustomPrimaryKeyNames](#supportsCustomPrimaryKeyNames)
* [**supportsDeferredUniqueConstraints](#supportsDeferredUniqueConstraints)
* [**supportsDownMigrations](#supportsDownMigrations)
* [**supportsMaterializedViews](#supportsMaterializedViews)
* [**supportsMultipleCascadePaths](#supportsmultiplecascadepaths)
* [**supportsMultipleStatements](#supportsmultiplestatements)
* [**supportsNativeEnums](#supportsNativeEnums)
* [**supportsOnUpdate](#supportsonupdate)
* [**supportsSchemas](#supportsschemas)
* [**supportsTransactions](#supportsTransactions)
* [**supportsUnionWhere](#supportsUnionWhere)
* [**supportsUnsigned](#supportsUnsigned)
* [**unmarshallArray](#unmarshallArray)
* [**usesAsKeyword](#usesaskeyword)
* [**usesBatchInserts](#usesBatchInserts)
* [**usesBatchUpdates](#usesBatchUpdates)
* [**usesCascadeStatement](#usescascadestatement)
* [**usesDefaultKeyword](#usesDefaultKeyword)
* [**usesEnumCheckConstraints](#usesenumcheckconstraints)
* [**usesImplicitTransactions](#usesImplicitTransactions)
* [**usesOutputStatement](#usesoutputstatement)
* [**usesPivotTable](#usesPivotTable)
* [**usesReturningStatement](#usesreturningstatement)
* [**validateMetadata](#validateMetadata)

## Constructors<!-- -->[**](#constructors)

### [**](#constructor)constructor

* ****new OraclePlatform**(): [OraclePlatform](https://mikro-orm.io/api/oracledb/class/OraclePlatform.md)

* Inherited from AbstractSqlPlatform.constructor

  #### Returns [OraclePlatform](https://mikro-orm.io/api/oracledb/class/OraclePlatform.md)

## Methods<!-- -->[**](#methods)

### [**](#allowscomparingtuples)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/oracledb/src/OraclePlatform.ts#L408)allowsComparingTuples

* ****allowsComparingTuples**(): boolean

* Overrides AbstractSqlPlatform.allowsComparingTuples

  #### Returns boolean

### [**](#cloneEmbeddable)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L649)inheritedcloneEmbeddable

* ****cloneEmbeddable**\<T>(data): T

* Inherited from AbstractSqlPlatform.cloneEmbeddable

  #### Parameters

  * ##### data: T

  #### Returns T

### [**](#compareuuids)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/oracledb/src/OraclePlatform.ts#L81)compareUuids

* ****compareUuids**(): string

* Overrides AbstractSqlPlatform.compareUuids

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

### [**](#convertJsonToDatabaseValue)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L490)inheritedconvertJsonToDatabaseValue

* ****convertJsonToDatabaseValue**(value, context): unknown

* Inherited from AbstractSqlPlatform.convertJsonToDatabaseValue

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

### [**](#convertsjsonautomatically)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/oracledb/src/OraclePlatform.ts#L118)convertsJsonAutomatically

* ****convertsJsonAutomatically**(): boolean

* Overrides AbstractSqlPlatform.convertsJsonAutomatically

  #### Returns boolean

### [**](#convertuuidtodatabasevalue)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/oracledb/src/OraclePlatform.ts#L93)convertUuidToDatabaseValue

* ****convertUuidToDatabaseValue**(value): Buffer\<ArrayBufferLike>

* Overrides AbstractSqlPlatform.convertUuidToDatabaseValue

  #### Parameters

  * ##### value: string

  #### Returns Buffer\<ArrayBufferLike>

### [**](#convertuuidtojsvalue)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/oracledb/src/OraclePlatform.ts#L85)convertUuidToJSValue

* ****convertUuidToJSValue**(value): string

* Overrides AbstractSqlPlatform.convertUuidToJSValue

  #### Parameters

  * ##### value: Buffer\<ArrayBufferLike>

  #### Returns string

### [**](#convertVersionValue)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L199)inheritedconvertVersionValue

* ****convertVersionValue**(value, prop): string | number | Date | { $in: (string | number)\[] }

* Inherited from AbstractSqlPlatform.convertVersionValue

  #### Parameters

  * ##### value: number | Date

  * ##### prop: [EntityProperty](https://mikro-orm.io/api/core/interface/EntityProperty.md)\<any, any>

  #### Returns string | number | Date | { $in: (string | number)\[] }

### [**](#createoutbindings)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/oracledb/src/OraclePlatform.ts#L425)createOutBindings

* ****createOutBindings**(map): [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)

* #### Parameters

  * ##### map: [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)\<string>

  #### Returns [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)

### [**](#denormalizePrimaryKey)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L141)inheriteddenormalizePrimaryKey

* ****denormalizePrimaryKey**(data): IPrimaryKeyValue

* Inherited from AbstractSqlPlatform.denormalizePrimaryKey

  Converts scalar primary key representation to native driver wrapper (e.g. string to mongodb's ObjectId)

  ***

  #### Parameters

  * ##### data: IPrimaryKeyValue

  #### Returns IPrimaryKeyValue

### [**](#escape)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/oracledb/src/OraclePlatform.ts#L376)escape

* ****escape**(value): string

* Overrides AbstractSqlPlatform.escape

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

### [**](#getarraydeclarationsql)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/oracledb/src/OraclePlatform.ts#L240)getArrayDeclarationSQL

* ****getArrayDeclarationSQL**(): string

* Overrides AbstractSqlPlatform.getArrayDeclarationSQL

  #### Returns string

### [**](#getbegintransactionsql)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/oracledb/src/OraclePlatform.ts#L59)getBeginTransactionSQL

* ****getBeginTransactionSQL**(options): string\[]

* Overrides AbstractSqlPlatform.getBeginTransactionSQL

  #### Parameters

  * ##### optionaloptions: { isolationLevel?<!-- -->: [IsolationLevel](https://mikro-orm.io/api/core/enum/IsolationLevel.md); readOnly?<!-- -->: boolean }

    * ##### optionalisolationLevel: [IsolationLevel](https://mikro-orm.io/api/core/enum/IsolationLevel.md)

    * ##### optionalreadOnly: boolean

  #### Returns string\[]

### [**](#getbiginttypedeclarationsql)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/oracledb/src/OraclePlatform.ts#L208)getBigIntTypeDeclarationSQL

* ****getBigIntTypeDeclarationSQL**(column): string

* Overrides AbstractSqlPlatform.getBigIntTypeDeclarationSQL

  * **@inheritDoc**

  ***

  #### Parameters

  * ##### column: { autoincrement?<!-- -->: boolean; length?<!-- -->: number; unsigned?<!-- -->: boolean }

    * ##### optionalautoincrement: boolean

    * ##### optionallength: number

    * ##### optionalunsigned: boolean

  #### Returns string

### [**](#getblobdeclarationsql)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/oracledb/src/OraclePlatform.ts#L173)getBlobDeclarationSQL

* ****getBlobDeclarationSQL**(): string

* Overrides AbstractSqlPlatform.getBlobDeclarationSQL

  #### Returns string

### [**](#getbooleantypedeclarationsql)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/oracledb/src/OraclePlatform.ts#L154)getBooleanTypeDeclarationSQL

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

### [**](#getcurrenttimestampsql)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/oracledb/src/OraclePlatform.ts#L130)getCurrentTimestampSQL

* ****getCurrentTimestampSQL**(length): string

* Overrides AbstractSqlPlatform.getCurrentTimestampSQL

  Returns the SQL specific for the platform to get the current timestamp

  ***

  #### Parameters

  * ##### length: number

  #### Returns string

### [**](#getdatetimetypedeclarationsql)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/oracledb/src/OraclePlatform.ts#L134)getDateTimeTypeDeclarationSQL

* ****getDateTimeTypeDeclarationSQL**(column): string

* Overrides AbstractSqlPlatform.getDateTimeTypeDeclarationSQL

  #### Parameters

  * ##### column: { length?<!-- -->: number }

    * ##### optionallength: number

  #### Returns string

### [**](#getdatetypedeclarationsql)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/oracledb/src/OraclePlatform.ts#L189)getDateTypeDeclarationSQL

* ****getDateTypeDeclarationSQL**(length): string

* Overrides AbstractSqlPlatform.getDateTypeDeclarationSQL

  #### Parameters

  * ##### optionallength: number

  #### Returns string

### [**](#getdecimaltypedeclarationsql)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/oracledb/src/OraclePlatform.ts#L150)getDecimalTypeDeclarationSQL

* ****getDecimalTypeDeclarationSQL**(column): string

* Overrides AbstractSqlPlatform.getDecimalTypeDeclarationSQL

  #### Parameters

  * ##### column: { precision?<!-- -->: number; scale?<!-- -->: number }

    * ##### optionalprecision: number

    * ##### optionalscale: number

  #### Returns string

### [**](#getdefaultclienturl)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/oracledb/src/OraclePlatform.ts#L412)getDefaultClientUrl

* ****getDefaultClientUrl**(): string

* Overrides AbstractSqlPlatform.getDefaultClientUrl

  Returns default client url for given driver (e.g. mongodb://127.0.0.1:27017 for mongodb)

  ***

  #### Returns string

### [**](#getdefaultdatetimelength)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/oracledb/src/OraclePlatform.ts#L138)getDefaultDateTimeLength

* ****getDefaultDateTimeLength**(): number

* Overrides AbstractSqlPlatform.getDefaultDateTimeLength

  #### Returns number

### [**](#getDefaultCharLength)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L164)inheritedgetDefaultCharLength

* ****getDefaultCharLength**(): number

* Inherited from AbstractSqlPlatform.getDefaultCharLength

  #### Returns number

### [**](#getDefaultCharset)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L545)inheritedgetDefaultCharset

* ****getDefaultCharset**(): string

* Inherited from AbstractSqlPlatform.getDefaultCharset

  #### Returns string

### [**](#getdefaultmappedtype)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/oracledb/src/OraclePlatform.ts#L278)getDefaultMappedType

* ****getDefaultMappedType**(type): [Type](https://mikro-orm.io/api/core/class/Type.md)\<unknown, unknown>

* Overrides AbstractSqlPlatform.getDefaultMappedType

  #### Parameters

  * ##### type: string

  #### Returns [Type](https://mikro-orm.io/api/core/class/Type.md)\<unknown, unknown>

### [**](#getDefaultPrimaryName)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L700)inheritedgetDefaultPrimaryName

* ****getDefaultPrimaryName**(tableName, columns): string

* Inherited from AbstractSqlPlatform.getDefaultPrimaryName

  #### Parameters

  * ##### tableName: string

  * ##### columns: string\[]

  #### Returns string

### [**](#getdefaultschemaname)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/oracledb/src/OraclePlatform.ts#L181)getDefaultSchemaName

* ****getDefaultSchemaName**(): undefined | string

* Overrides AbstractSqlPlatform.getDefaultSchemaName

  #### Returns undefined | string

### [**](#getDefaultVarcharLength)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L160)inheritedgetDefaultVarcharLength

* ****getDefaultVarcharLength**(): number

* Inherited from AbstractSqlPlatform.getDefaultVarcharLength

  #### Returns number

### [**](#getDefaultVersionLength)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L206)inheritedgetDefaultVersionLength

* ****getDefaultVersionLength**(): number

* Inherited from AbstractSqlPlatform.getDefaultVersionLength

  #### Returns number

### [**](#getdoubledeclarationsql)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/oracledb/src/OraclePlatform.ts#L146)getDoubleDeclarationSQL

* ****getDoubleDeclarationSQL**(): string

* Overrides AbstractSqlPlatform.getDoubleDeclarationSQL

  #### Returns string

### [**](#getenumtypedeclarationsql)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/oracledb/src/OraclePlatform.ts#L244)getEnumTypeDeclarationSQL

* ****getEnumTypeDeclarationSQL**(column): string

* Overrides AbstractSqlPlatform.getEnumTypeDeclarationSQL

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

### [**](#getfloatdeclarationsql)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/oracledb/src/OraclePlatform.ts#L142)getFloatDeclarationSQL

* ****getFloatDeclarationSQL**(): string

* Overrides AbstractSqlPlatform.getFloatDeclarationSQL

  #### Returns string

### [**](#getFullTextIndexExpression)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L477)inheritedgetFullTextIndexExpression

* ****getFullTextIndexExpression**(indexName, schemaName, tableName, columns): string

* Inherited from AbstractSqlPlatform.getFullTextIndexExpression

  #### Parameters

  * ##### indexName: string

  * ##### schemaName: undefined | string

  * ##### tableName: string

  * ##### columns: [SimpleColumnMeta](https://mikro-orm.io/api/core/interface/SimpleColumnMeta.md)\[]

  #### Returns string

### [**](#getFullTextWhereClause)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L469)inheritedgetFullTextWhereClause

* ****getFullTextWhereClause**(prop): string

* Inherited from AbstractSqlPlatform.getFullTextWhereClause

  #### Parameters

  * ##### prop: [EntityProperty](https://mikro-orm.io/api/core/interface/EntityProperty.md)\<any, any>

  #### Returns string

### [**](#getCharTypeDeclarationSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L246)inheritedgetCharTypeDeclarationSQL

* ****getCharTypeDeclarationSQL**(column): string

* Inherited from AbstractSqlPlatform.getCharTypeDeclarationSQL

  #### Parameters

  * ##### column: { length?<!-- -->: number }

    * ##### optionallength: number

  #### Returns string

### [**](#getIndexName)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L692)inheritedgetIndexName

* ****getIndexName**(tableName, columns, type): string

* Inherited from AbstractSqlPlatform.getIndexName

  Returns the default name of index for the given columns

  ***

  #### Parameters

  * ##### tableName: string

  * ##### columns: string\[]

  * ##### type: primary | index | unique | foreign | sequence

  #### Returns string

### [**](#getintegertypedeclarationsql)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/oracledb/src/OraclePlatform.ts#L197)getIntegerTypeDeclarationSQL

* ****getIntegerTypeDeclarationSQL**(column): string

* Overrides AbstractSqlPlatform.getIntegerTypeDeclarationSQL

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

### [**](#getjsondeclarationsql)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/oracledb/src/OraclePlatform.ts#L177)getJsonDeclarationSQL

* ****getJsonDeclarationSQL**(): string

* Overrides AbstractSqlPlatform.getJsonDeclarationSQL

  #### Returns string

### [**](#getJsonIndexDefinition)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/AbstractSqlPlatform.ts#L128)inheritedgetJsonIndexDefinition

* ****getJsonIndexDefinition**(index): string\[]

* Inherited from AbstractSqlPlatform.getJsonIndexDefinition

  #### Parameters

  * ##### index: [IndexDef](https://mikro-orm.io/api/sql/interface/IndexDef.md)

  #### Returns string\[]

### [**](#getMappedType)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L307)inheritedgetMappedType

* ****getMappedType**(type): [Type](https://mikro-orm.io/api/core/class/Type.md)\<unknown, unknown>

* Inherited from AbstractSqlPlatform.getMappedType

  #### Parameters

  * ##### type: string

  #### Returns [Type](https://mikro-orm.io/api/core/class/Type.md)\<unknown, unknown>

### [**](#getmediuminttypedeclarationsql)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/oracledb/src/OraclePlatform.ts#L216)getMediumIntTypeDeclarationSQL

* ****getMediumIntTypeDeclarationSQL**(column): string

* Overrides AbstractSqlPlatform.getMediumIntTypeDeclarationSQL

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

### [**](#getregexpoperator)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/oracledb/src/OraclePlatform.ts#L158)getRegExpOperator

* ****getRegExpOperator**(): string

* Overrides AbstractSqlPlatform.getRegExpOperator

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

### [**](#getrollbacktosavepointsql)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/oracledb/src/OraclePlatform.ts#L51)getRollbackToSavepointSQL

* ****getRollbackToSavepointSQL**(savepointName): string

* Overrides AbstractSqlPlatform.getRollbackToSavepointSQL

  #### Parameters

  * ##### savepointName: string

  #### Returns string

### [**](#getRollbackTransactionSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/AbstractSqlPlatform.ts#L70)inheritedgetRollbackTransactionSQL

* ****getRollbackTransactionSQL**(): string

* Inherited from AbstractSqlPlatform.getRollbackTransactionSQL

  #### Returns string

### [**](#getsavepointsql)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/oracledb/src/OraclePlatform.ts#L55)getSavepointSQL

* ****getSavepointSQL**(savepointName): string

* Overrides AbstractSqlPlatform.getSavepointSQL

  #### Parameters

  * ##### savepointName: string

  #### Returns string

### [**](#getsearchjsonpropertykey)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/oracledb/src/OraclePlatform.ts#L307)getSearchJsonPropertyKey

* ****getSearchJsonPropertyKey**(path, type, aliased, value): string

* Overrides AbstractSqlPlatform.getSearchJsonPropertyKey

  #### Parameters

  * ##### path: string\[]

  * ##### type: string

  * ##### aliased: boolean

  * ##### optionalvalue: unknown

  #### Returns string

### [**](#getSearchJsonPropertySQL)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/AbstractSqlPlatform.ts#L98)inheritedgetSearchJsonPropertySQL

* ****getSearchJsonPropertySQL**(path, type, aliased): string | [RawQueryFragment](https://mikro-orm.io/api/core/class/RawQueryFragment.md)\<string>

* Inherited from AbstractSqlPlatform.getSearchJsonPropertySQL

  #### Parameters

  * ##### path: string

  * ##### type: string

  * ##### aliased: boolean

  #### Returns string | [RawQueryFragment](https://mikro-orm.io/api/core/class/RawQueryFragment.md)\<string>

### [**](#getschemagenerator)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/oracledb/src/OraclePlatform.ts#L404)getSchemaGenerator

* ****getSchemaGenerator**(driver, em): [OracleSchemaGenerator](https://mikro-orm.io/api/oracledb/class/OracleSchemaGenerator.md)

* Overrides AbstractSqlPlatform.getSchemaGenerator

  #### Parameters

  * ##### driver: [IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>

  * ##### optionalem: [SqlEntityManager](https://mikro-orm.io/api/sql/class/EntityManager.md)<[AbstractSqlDriver](https://mikro-orm.io/api/sql/class/AbstractSqlDriver.md)<[AbstractSqlConnection](https://mikro-orm.io/api/sql/class/AbstractSqlConnection.md), [AbstractSqlPlatform](https://mikro-orm.io/api/sql/class/AbstractSqlPlatform.md)>>

  #### Returns [OracleSchemaGenerator](https://mikro-orm.io/api/oracledb/class/OracleSchemaGenerator.md)

### [**](#getSchemaHelper)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/AbstractSqlPlatform.ts#L38)inheritedgetSchemaHelper

* ****getSchemaHelper**(): undefined | [SchemaHelper](https://mikro-orm.io/api/sql/class/SchemaHelper.md)

* Inherited from AbstractSqlPlatform.getSchemaHelper

  #### Returns undefined | [SchemaHelper](https://mikro-orm.io/api/sql/class/SchemaHelper.md)

### [**](#getsmallinttypedeclarationsql)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/oracledb/src/OraclePlatform.ts#L232)getSmallIntTypeDeclarationSQL

* ****getSmallIntTypeDeclarationSQL**(column): string

* Overrides AbstractSqlPlatform.getSmallIntTypeDeclarationSQL

  #### Parameters

  * ##### column: { autoincrement?<!-- -->: boolean; length?<!-- -->: number; unsigned?<!-- -->: boolean }

    * ##### optionalautoincrement: boolean

    * ##### optionallength: number

    * ##### optionalunsigned: boolean

  #### Returns string

### [**](#gettexttypedeclarationsql)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/oracledb/src/OraclePlatform.ts#L259)getTextTypeDeclarationSQL

* ****getTextTypeDeclarationSQL**(\_column): string

* Overrides AbstractSqlPlatform.getTextTypeDeclarationSQL

  #### Parameters

  * ##### \_column: { length?<!-- -->: number }

    * ##### optionallength: number

  #### Returns string

### [**](#gettimetypedeclarationsql)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/oracledb/src/OraclePlatform.ts#L193)getTimeTypeDeclarationSQL

* ****getTimeTypeDeclarationSQL**(length): string

* Overrides AbstractSqlPlatform.getTimeTypeDeclarationSQL

  #### Parameters

  * ##### optionallength: number

  #### Returns string

### [**](#getTimezone)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L672)inheritedgetTimezone

* ****getTimezone**(): undefined | string

* Inherited from AbstractSqlPlatform.getTimezone

  #### Returns undefined | string

### [**](#gettinyinttypedeclarationsql)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/oracledb/src/OraclePlatform.ts#L224)getTinyIntTypeDeclarationSQL

* ****getTinyIntTypeDeclarationSQL**(column): string

* Overrides AbstractSqlPlatform.getTinyIntTypeDeclarationSQL

  #### Parameters

  * ##### column: { autoincrement?<!-- -->: boolean; length?<!-- -->: number; unsigned?<!-- -->: boolean }

    * ##### optionalautoincrement: boolean

    * ##### optionallength: number

    * ##### optionalunsigned: boolean

  #### Returns string

### [**](#getuuidtypedeclarationsql)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/oracledb/src/OraclePlatform.ts#L298)getUuidTypeDeclarationSQL

* ****getUuidTypeDeclarationSQL**(column): string

* Overrides AbstractSqlPlatform.getUuidTypeDeclarationSQL

  #### Parameters

  * ##### column: { length?<!-- -->: number }

    * ##### optionallength: number

  #### Returns string

### [**](#getvarchartypedeclarationsql)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/oracledb/src/OraclePlatform.ts#L185)getVarcharTypeDeclarationSQL

* ****getVarcharTypeDeclarationSQL**(column): string

* Overrides AbstractSqlPlatform.getVarcharTypeDeclarationSQL

  #### Parameters

  * ##### column: { length?<!-- -->: number }

    * ##### optionallength: number

  #### Returns string

### [**](#indexforeignkeys)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/oracledb/src/OraclePlatform.ts#L122)indexForeignKeys

* ****indexForeignKeys**(): boolean

* Overrides AbstractSqlPlatform.indexForeignKeys

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

### [**](#isNumericColumn)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L681)inheritedisNumericColumn

* ****isNumericColumn**(mappedType): boolean

* Inherited from AbstractSqlPlatform.isNumericColumn

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

### [**](#lookupextensions)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/oracledb/src/OraclePlatform.ts#L47)lookupExtensions

* ****lookupExtensions**(orm): void

* Overrides AbstractSqlPlatform.lookupExtensions

  Allows registering extensions of the driver automatically (e.g. `SchemaGenerator` extension in SQL drivers).

  ***

  #### Parameters

  * ##### orm: [MikroORM](https://mikro-orm.io/api/core/class/MikroORM.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>, [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>, (string | [EntitySchema](https://mikro-orm.io/api/core/class/EntitySchema.md)\<any, never, [EntityCtor](https://mikro-orm.io/api/core.md#EntityCtor)\<any>> | [EntityClass](https://mikro-orm.io/api/core.md#EntityClass)\<Partial\<any>>)\[]>

  #### Returns void

### [**](#mapregexpcondition)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/oracledb/src/OraclePlatform.ts#L162)mapRegExpCondition

* ****mapRegExpCondition**(mappedKey, value): { params: unknown\[]; sql: string }

* Overrides AbstractSqlPlatform.mapRegExpCondition

  #### Parameters

  * ##### mappedKey: string

  * ##### value: { $flags?<!-- -->: string; $re: string }

    * ##### optional$flags: string

    * ##### $re: string

  #### Returns { params: unknown\[]; sql: string }

  * ##### params: unknown\[]

  * ##### sql: string

### [**](#maptooracletype)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/oracledb/src/OraclePlatform.ts#L421)mapToOracleType

* ****mapToOracleType**(type): unknown

* #### Parameters

  * ##### type: string

  #### Returns unknown

### [**](#marshallArray)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L398)inheritedmarshallArray

* ****marshallArray**(values): string

* Inherited from AbstractSqlPlatform.marshallArray

  #### Parameters

  * ##### values: string\[]

  #### Returns string

### [**](#normalizecolumntype)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/oracledb/src/OraclePlatform.ts#L263)normalizeColumnType

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

### [**](#processjsoncondition)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/oracledb/src/OraclePlatform.ts#L318)processJsonCondition

* ****processJsonCondition**\<T>(o, value, path, alias): [FilterQuery](https://mikro-orm.io/api/core.md#FilterQuery)\<T>

* Overrides AbstractSqlPlatform.processJsonCondition

  #### Parameters

  * ##### o: [FilterQuery](https://mikro-orm.io/api/core.md#FilterQuery)\<T>

  * ##### value: [EntityValue](https://mikro-orm.io/api/core.md#EntityValue)\<T>

  * ##### path: [EntityKey](https://mikro-orm.io/api/core.md#EntityKey)\<T>\[]

  * ##### alias: boolean

  #### Returns [FilterQuery](https://mikro-orm.io/api/core.md#FilterQuery)\<T>

### [**](#quoteidentifier)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/oracledb/src/OraclePlatform.ts#L372)quoteIdentifier

* ****quoteIdentifier**(id): string

* Overrides AbstractSqlPlatform.quoteIdentifier

  #### Parameters

  * ##### id: string

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

### [**](#supportsCreatingFullTextIndex)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L473)inheritedsupportsCreatingFullTextIndex

* ****supportsCreatingFullTextIndex**(): boolean

* Inherited from AbstractSqlPlatform.supportsCreatingFullTextIndex

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

### [**](#supportsmultiplecascadepaths)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/oracledb/src/OraclePlatform.ts#L359)supportsMultipleCascadePaths

* ****supportsMultipleCascadePaths**(): boolean

* Overrides AbstractSqlPlatform.supportsMultipleCascadePaths

  #### Returns boolean

### [**](#supportsmultiplestatements)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/oracledb/src/OraclePlatform.ts#L368)supportsMultipleStatements

* ****supportsMultipleStatements**(): boolean

* Overrides AbstractSqlPlatform.supportsMultipleStatements

  #### Returns boolean

### [**](#supportsNativeEnums)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L92)inheritedsupportsNativeEnums

* ****supportsNativeEnums**(): boolean

* Inherited from AbstractSqlPlatform.supportsNativeEnums

  for postgres native enums

  ***

  #### Returns boolean

### [**](#supportsonupdate)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/oracledb/src/OraclePlatform.ts#L364)supportsOnUpdate

* ****supportsOnUpdate**(): boolean

* Overrides AbstractSqlPlatform.supportsOnUpdate

  Returns true if the platform supports ON UPDATE foreign key rules. Oracle doesn't support ON UPDATE rules.

  ***

  #### Returns boolean

### [**](#supportsschemas)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/oracledb/src/OraclePlatform.ts#L126)supportsSchemas

* ****supportsSchemas**(): boolean

* Overrides AbstractSqlPlatform.supportsSchemas

  #### Returns boolean

### [**](#supportsTransactions)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L67)inheritedsupportsTransactions

* ****supportsTransactions**(): boolean

* Inherited from AbstractSqlPlatform.supportsTransactions

  #### Returns boolean

### [**](#supportsUnionWhere)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/AbstractSqlPlatform.ts#L139)inheritedsupportsUnionWhere

* ****supportsUnionWhere**(): boolean

* Inherited from AbstractSqlPlatform.supportsUnionWhere

  #### Returns boolean

### [**](#supportsUnsigned)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L685)inheritedsupportsUnsigned

* ****supportsUnsigned**(): boolean

* Inherited from AbstractSqlPlatform.supportsUnsigned

  #### Returns boolean

### [**](#unmarshallArray)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L402)inheritedunmarshallArray

* ****unmarshallArray**(value): string\[]

* Inherited from AbstractSqlPlatform.unmarshallArray

  #### Parameters

  * ##### value: string

  #### Returns string\[]

### [**](#usesaskeyword)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/oracledb/src/OraclePlatform.ts#L77)usesAsKeyword

* ****usesAsKeyword**(): boolean

* Overrides AbstractSqlPlatform.usesAsKeyword

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

### [**](#usescascadestatement)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/oracledb/src/OraclePlatform.ts#L303)usesCascadeStatement

* ****usesCascadeStatement**(): boolean

* Overrides AbstractSqlPlatform.usesCascadeStatement

  #### Returns boolean

### [**](#usesDefaultKeyword)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L127)inheritedusesDefaultKeyword

* ****usesDefaultKeyword**(): boolean

* Inherited from AbstractSqlPlatform.usesDefaultKeyword

  #### Returns boolean

### [**](#usesenumcheckconstraints)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/oracledb/src/OraclePlatform.ts#L355)usesEnumCheckConstraints

* ****usesEnumCheckConstraints**(): boolean

* Overrides AbstractSqlPlatform.usesEnumCheckConstraints

  for postgres text enums (default)

  ***

  #### Returns boolean

### [**](#usesImplicitTransactions)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L71)inheritedusesImplicitTransactions

* ****usesImplicitTransactions**(): boolean

* Inherited from AbstractSqlPlatform.usesImplicitTransactions

  #### Returns boolean

### [**](#usesoutputstatement)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/oracledb/src/OraclePlatform.ts#L110)usesOutputStatement

* ****usesOutputStatement**(): boolean

* Overrides AbstractSqlPlatform.usesOutputStatement

  #### Returns boolean

### [**](#usesPivotTable)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/sql/src/AbstractSqlPlatform.ts#L26)inheritedusesPivotTable

* ****usesPivotTable**(): boolean

* Inherited from AbstractSqlPlatform.usesPivotTable

  #### Returns boolean

### [**](#usesreturningstatement)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/oracledb/src/OraclePlatform.ts#L114)usesReturningStatement

* ****usesReturningStatement**(): boolean

* Overrides AbstractSqlPlatform.usesReturningStatement

  #### Returns boolean

### [**](#validateMetadata)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L761)inheritedvalidateMetadata

* ****validateMetadata**(meta): void

* Inherited from AbstractSqlPlatform.validateMetadata

  #### Parameters

  * ##### meta: [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<any, [EntityCtor](https://mikro-orm.io/api/core.md#EntityCtor)\<any>>

  #### Returns void
