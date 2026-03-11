# Source: https://mikro-orm.io/api/core/class/Platform.md

# abstractPlatform<!-- -->

### Hierarchy

* *Platform*

  * [AbstractSqlPlatform](https://mikro-orm.io/api/sql/class/AbstractSqlPlatform.md)
  * [MongoPlatform](https://mikro-orm.io/api/mongodb/class/MongoPlatform.md)

## Index[**](#index)

### Constructors

* [**constructor](#constructor)

### Methods

* [**allowsComparingTuples](#allowscomparingtuples)
* [**cloneEmbeddable](#cloneembeddable)
* [**compareUuids](#compareuuids)
* [**convertDateToJSValue](#convertdatetojsvalue)
* [**convertIntervalToDatabaseValue](#convertintervaltodatabasevalue)
* [**convertIntervalToJSValue](#convertintervaltojsvalue)
* [**convertJsonToDatabaseValue](#convertjsontodatabasevalue)
* [**convertJsonToJSValue](#convertjsontojsvalue)
* [**convertsJsonAutomatically](#convertsjsonautomatically)
* [**convertUuidToDatabaseValue](#convertuuidtodatabasevalue)
* [**convertUuidToJSValue](#convertuuidtojsvalue)
* [**convertVersionValue](#convertversionvalue)
* [**denormalizePrimaryKey](#denormalizeprimarykey)
* [**escape](#escape)
* [**extractSimpleType](#extractsimpletype)
* [**formatQuery](#formatquery)
* [**generateCustomOrder](#generatecustomorder)
* [**getArrayDeclarationSQL](#getarraydeclarationsql)
* [**getBigIntTypeDeclarationSQL](#getbiginttypedeclarationsql)
* [**getBlobDeclarationSQL](#getblobdeclarationsql)
* [**getBooleanTypeDeclarationSQL](#getbooleantypedeclarationsql)
* [**getConfig](#getconfig)
* [**getCurrentTimestampSQL](#getcurrenttimestampsql)
* [**getDateTimeTypeDeclarationSQL](#getdatetimetypedeclarationsql)
* [**getDateTypeDeclarationSQL](#getdatetypedeclarationsql)
* [**getDecimalTypeDeclarationSQL](#getdecimaltypedeclarationsql)
* [**getDefaultClientUrl](#getdefaultclienturl)
* [**getDefaultDateTimeLength](#getdefaultdatetimelength)
* [**getDefaultCharLength](#getdefaultcharlength)
* [**getDefaultCharset](#getdefaultcharset)
* [**getDefaultMappedType](#getdefaultmappedtype)
* [**getDefaultPrimaryName](#getdefaultprimaryname)
* [**getDefaultSchemaName](#getdefaultschemaname)
* [**getDefaultVarcharLength](#getdefaultvarcharlength)
* [**getDefaultVersionLength](#getdefaultversionlength)
* [**getDoubleDeclarationSQL](#getdoubledeclarationsql)
* [**getEnumTypeDeclarationSQL](#getenumtypedeclarationsql)
* [**getExceptionConverter](#getexceptionconverter)
* [**getExtension](#getextension)
* [**getFloatDeclarationSQL](#getfloatdeclarationsql)
* [**getFullTextIndexExpression](#getfulltextindexexpression)
* [**getFullTextWhereClause](#getfulltextwhereclause)
* [**getCharTypeDeclarationSQL](#getchartypedeclarationsql)
* [**getIndexName](#getindexname)
* [**getIntegerTypeDeclarationSQL](#getintegertypedeclarationsql)
* [**getIntervalTypeDeclarationSQL](#getintervaltypedeclarationsql)
* [**getJsonDeclarationSQL](#getjsondeclarationsql)
* [**getJsonIndexDefinition](#getjsonindexdefinition)
* [**getMappedType](#getmappedtype)
* [**getMediumIntTypeDeclarationSQL](#getmediuminttypedeclarationsql)
* [**getNamingStrategy](#getnamingstrategy)
* [**getRegExpOperator](#getregexpoperator)
* [**getRegExpValue](#getregexpvalue)
* [**getRepositoryClass](#getrepositoryclass)
* [**getSearchJsonPropertyKey](#getsearchjsonpropertykey)
* [**getSearchJsonPropertySQL](#getsearchjsonpropertysql)
* [**getSchemaGenerator](#getschemagenerator)
* [**getSchemaHelper](#getschemahelper)
* [**getSmallIntTypeDeclarationSQL](#getsmallinttypedeclarationsql)
* [**getTextTypeDeclarationSQL](#gettexttypedeclarationsql)
* [**getTimeTypeDeclarationSQL](#gettimetypedeclarationsql)
* [**getTimezone](#gettimezone)
* [**getTinyIntTypeDeclarationSQL](#gettinyinttypedeclarationsql)
* [**getUuidTypeDeclarationSQL](#getuuidtypedeclarationsql)
* [**getVarcharTypeDeclarationSQL](#getvarchartypedeclarationsql)
* [**indexForeignKeys](#indexforeignkeys)
* [**isAllowedTopLevelOperator](#isallowedtopleveloperator)
* [**isBigIntProperty](#isbigintproperty)
* [**isNumericColumn](#isnumericcolumn)
* [**isNumericProperty](#isnumericproperty)
* [**isPopulated](#ispopulated)
* [**lookupExtensions](#lookupextensions)
* [**mapRegExpCondition](#mapregexpcondition)
* [**marshallArray](#marshallarray)
* [**normalizeColumnType](#normalizecolumntype)
* [**normalizePrimaryKey](#normalizeprimarykey)
* [**parseDate](#parsedate)
* [**processDateProperty](#processdateproperty)
* [**processJsonCondition](#processjsoncondition)
* [**quoteIdentifier](#quoteidentifier)
* [**quoteValue](#quotevalue)
* [**setConfig](#setconfig)
* [**shouldHaveColumn](#shouldhavecolumn)
* [**supportsCreatingFullTextIndex](#supportscreatingfulltextindex)
* [**supportsCustomPrimaryKeyNames](#supportscustomprimarykeynames)
* [**supportsDeferredUniqueConstraints](#supportsdeferreduniqueconstraints)
* [**supportsDownMigrations](#supportsdownmigrations)
* [**supportsMaterializedViews](#supportsmaterializedviews)
* [**supportsMultipleCascadePaths](#supportsmultiplecascadepaths)
* [**supportsMultipleStatements](#supportsmultiplestatements)
* [**supportsNativeEnums](#supportsnativeenums)
* [**supportsOnUpdate](#supportsonupdate)
* [**supportsTransactions](#supportstransactions)
* [**supportsUnionWhere](#supportsunionwhere)
* [**supportsUnsigned](#supportsunsigned)
* [**unmarshallArray](#unmarshallarray)
* [**usesAsKeyword](#usesaskeyword)
* [**usesBatchInserts](#usesbatchinserts)
* [**usesBatchUpdates](#usesbatchupdates)
* [**usesCascadeStatement](#usescascadestatement)
* [**usesDefaultKeyword](#usesdefaultkeyword)
* [**usesEnumCheckConstraints](#usesenumcheckconstraints)
* [**usesImplicitTransactions](#usesimplicittransactions)
* [**usesOutputStatement](#usesoutputstatement)
* [**usesPivotTable](#usespivottable)
* [**usesReturningStatement](#usesreturningstatement)
* [**validateMetadata](#validatemetadata)

## Constructors<!-- -->[**](#constructors)

### [**](#constructor)constructor

* ****new Platform**(): [Platform](https://mikro-orm.io/api/core/class/Platform.md)

* #### Returns [Platform](https://mikro-orm.io/api/core/class/Platform.md)

## Methods<!-- -->[**](#methods)

### [**](#allowscomparingtuples)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L210)allowsComparingTuples

* ****allowsComparingTuples**(): boolean

* #### Returns boolean

### [**](#cloneembeddable)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L649)cloneEmbeddable

* ****cloneEmbeddable**\<T>(data): T

* #### Parameters

  * ##### data: T

  #### Returns T

### [**](#compareuuids)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L518)compareUuids

* ****compareUuids**(): string

* Determines how UUID values are compared in the change set tracking. Return `'string'` for inline string comparison (fast), or `'any'` for deep comparison via type methods.

  ***

  #### Returns string

### [**](#convertdatetojsvalue)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L498)convertDateToJSValue

* ****convertDateToJSValue**(value): string

* #### Parameters

  * ##### value: string | Date

  #### Returns string

### [**](#convertintervaltodatabasevalue)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L506)convertIntervalToDatabaseValue

* ****convertIntervalToDatabaseValue**(value): unknown

* #### Parameters

  * ##### value: unknown

  #### Returns unknown

### [**](#convertintervaltojsvalue)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L502)convertIntervalToJSValue

* ****convertIntervalToJSValue**(value): unknown

* #### Parameters

  * ##### value: string

  #### Returns unknown

### [**](#convertjsontodatabasevalue)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L490)convertJsonToDatabaseValue

* ****convertJsonToDatabaseValue**(value, context): unknown

* #### Parameters

  * ##### value: unknown

  * ##### optionalcontext: [TransformContext](https://mikro-orm.io/api/core/interface/TransformContext.md)

  #### Returns unknown

### [**](#convertjsontojsvalue)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L494)convertJsonToJSValue

* ****convertJsonToJSValue**(value, context): unknown

* #### Parameters

  * ##### value: unknown

  * ##### optionalcontext: [TransformContext](https://mikro-orm.io/api/core/interface/TransformContext.md)

  #### Returns unknown

### [**](#convertsjsonautomatically)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L486)convertsJsonAutomatically

* ****convertsJsonAutomatically**(): boolean

* #### Returns boolean

### [**](#convertuuidtodatabasevalue)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L526)convertUuidToDatabaseValue

* ****convertUuidToDatabaseValue**(value): unknown

* #### Parameters

  * ##### value: unknown

  #### Returns unknown

### [**](#convertuuidtojsvalue)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L522)convertUuidToJSValue

* ****convertUuidToJSValue**(value): unknown

* #### Parameters

  * ##### value: unknown

  #### Returns unknown

### [**](#convertversionvalue)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L199)convertVersionValue

* ****convertVersionValue**(value, prop): string | number | Date | { $in: (string | number)\[] }

* #### Parameters

  * ##### value: number | Date

  * ##### prop: [EntityProperty](https://mikro-orm.io/api/core/interface/EntityProperty.md)\<any, any>

  #### Returns string | number | Date | { $in: (string | number)\[] }

### [**](#denormalizeprimarykey)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L141)denormalizePrimaryKey

* ****denormalizePrimaryKey**(data): IPrimaryKeyValue

* Converts scalar primary key representation to native driver wrapper (e.g. string to mongodb's ObjectId)

  ***

  #### Parameters

  * ##### data: IPrimaryKeyValue

  #### Returns IPrimaryKeyValue

### [**](#escape)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L602)escape

* ****escape**(value): string

* #### Parameters

  * ##### value: any

  #### Returns string

### [**](#extractsimpletype)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L296)extractSimpleType

* ****extractSimpleType**(type): string

* #### Parameters

  * ##### type: string

  #### Returns string

### [**](#formatquery)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L606)formatQuery

* ****formatQuery**(sql, params): string

* #### Parameters

  * ##### sql: string

  * ##### params: readonly<!-- --> any\[]

  #### Returns string

### [**](#generatecustomorder)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L769)generateCustomOrder

* ****generateCustomOrder**(escapedColumn, values): void

* Generates a custom order by statement given a set of in order values, eg. ORDER BY (CASE WHEN priority = 'low' THEN 1 WHEN priority = 'medium' THEN 2 ELSE NULL END)

  ***

  #### Parameters

  * ##### escapedColumn: string

  * ##### values: unknown\[]

  #### Returns void

### [**](#getarraydeclarationsql)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L394)getArrayDeclarationSQL

* ****getArrayDeclarationSQL**(): string

* #### Returns string

### [**](#getbiginttypedeclarationsql)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L242)getBigIntTypeDeclarationSQL

* ****getBigIntTypeDeclarationSQL**(column): string

* #### Parameters

  * ##### column: { autoincrement?<!-- -->: boolean; length?<!-- -->: number; unsigned?<!-- -->: boolean }

    * ##### optionalautoincrement: boolean

    * ##### optionallength: number

    * ##### optionalunsigned: boolean

  #### Returns string

### [**](#getblobdeclarationsql)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L410)getBlobDeclarationSQL

* ****getBlobDeclarationSQL**(): string

* #### Returns string

### [**](#getbooleantypedeclarationsql)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L222)getBooleanTypeDeclarationSQL

* ****getBooleanTypeDeclarationSQL**(): string

* #### Returns string

### [**](#getconfig)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L668)getConfig

* ****getConfig**(): [Configuration](https://mikro-orm.io/api/core/class/Configuration.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>, [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>>

* #### Returns [Configuration](https://mikro-orm.io/api/core/class/Configuration.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>, [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>>

### [**](#getcurrenttimestampsql)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L148)getCurrentTimestampSQL

* ****getCurrentTimestampSQL**(length): string

* Returns the SQL specific for the platform to get the current timestamp

  ***

  #### Parameters

  * ##### optionallength: number

  #### Returns string

### [**](#getdatetimetypedeclarationsql)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L152)getDateTimeTypeDeclarationSQL

* ****getDateTimeTypeDeclarationSQL**(column): string

* #### Parameters

  * ##### column: { length?<!-- -->: number }

    * ##### optionallength: number

  #### Returns string

### [**](#getdatetypedeclarationsql)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L168)getDateTypeDeclarationSQL

* ****getDateTypeDeclarationSQL**(length): string

* #### Parameters

  * ##### optionallength: number

  #### Returns string

### [**](#getdecimaltypedeclarationsql)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L284)getDecimalTypeDeclarationSQL

* ****getDecimalTypeDeclarationSQL**(column): string

* #### Parameters

  * ##### column: { precision?<!-- -->: number; scale?<!-- -->: number }

    * ##### optionalprecision: number

    * ##### optionalscale: number

  #### Returns string

### [**](#getdefaultclienturl)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L776)getDefaultClientUrl

* ****getDefaultClientUrl**(): string

* Returns default client url for given driver (e.g. mongodb://127.0.0.1:27017 for mongodb)

  ***

  #### Returns string

### [**](#getdefaultdatetimelength)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L156)getDefaultDateTimeLength

* ****getDefaultDateTimeLength**(): number

* #### Returns number

### [**](#getdefaultcharlength)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L164)getDefaultCharLength

* ****getDefaultCharLength**(): number

* #### Returns number

### [**](#getdefaultcharset)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L545)getDefaultCharset

* ****getDefaultCharset**(): string

* #### Returns string

### [**](#getdefaultmappedtype)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L312)getDefaultMappedType

* ****getDefaultMappedType**(type): [Type](https://mikro-orm.io/api/core/class/Type.md)\<unknown, unknown>

* #### Parameters

  * ##### type: string

  #### Returns [Type](https://mikro-orm.io/api/core/class/Type.md)\<unknown, unknown>

### [**](#getdefaultprimaryname)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L700)getDefaultPrimaryName

* ****getDefaultPrimaryName**(tableName, columns): string

* #### Parameters

  * ##### tableName: string

  * ##### columns: string\[]

  #### Returns string

### [**](#getdefaultschemaname)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L218)getDefaultSchemaName

* ****getDefaultSchemaName**(): undefined | string

* #### Returns undefined | string

### [**](#getdefaultvarcharlength)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L160)getDefaultVarcharLength

* ****getDefaultVarcharLength**(): number

* #### Returns number

### [**](#getdefaultversionlength)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L206)getDefaultVersionLength

* ****getDefaultVersionLength**(): number

* #### Returns number

### [**](#getdoubledeclarationsql)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L280)getDoubleDeclarationSQL

* ****getDoubleDeclarationSQL**(): string

* #### Returns string

### [**](#getenumtypedeclarationsql)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L262)getEnumTypeDeclarationSQL

* ****getEnumTypeDeclarationSQL**(column): string

* #### Parameters

  * ##### column: { autoincrement?<!-- -->: boolean; fieldNames: string\[]; items?<!-- -->: unknown\[]; length?<!-- -->: number; unsigned?<!-- -->: boolean }

    * ##### optionalautoincrement: boolean

    * ##### fieldNames: string\[]

    * ##### optionalitems: unknown\[]

    * ##### optionallength: number

    * ##### optionalunsigned: boolean

  #### Returns string

### [**](#getexceptionconverter)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L549)getExceptionConverter

* ****getExceptionConverter**(): [ExceptionConverter](https://mikro-orm.io/api/core/class/ExceptionConverter.md)

* #### Returns [ExceptionConverter](https://mikro-orm.io/api/core/class/ExceptionConverter.md)

### [**](#getextension)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L565)getExtension

* ****getExtension**\<T>(extensionName, extensionKey, moduleName, em): T

* #### Parameters

  * ##### extensionName: string

  * ##### extensionKey: string

  * ##### moduleName: string

  * ##### em: [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>

  #### Returns T

### [**](#getfloatdeclarationsql)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L276)getFloatDeclarationSQL

* ****getFloatDeclarationSQL**(): string

* #### Returns string

### [**](#getfulltextindexexpression)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L477)getFullTextIndexExpression

* ****getFullTextIndexExpression**(indexName, schemaName, tableName, columns): string

* #### Parameters

  * ##### indexName: string

  * ##### schemaName: undefined | string

  * ##### tableName: string

  * ##### columns: [SimpleColumnMeta](https://mikro-orm.io/api/core/interface/SimpleColumnMeta.md)\[]

  #### Returns string

### [**](#getfulltextwhereclause)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L469)getFullTextWhereClause

* ****getFullTextWhereClause**(prop): string

* #### Parameters

  * ##### prop: [EntityProperty](https://mikro-orm.io/api/core/interface/EntityProperty.md)\<any, any>

  #### Returns string

### [**](#getchartypedeclarationsql)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L246)getCharTypeDeclarationSQL

* ****getCharTypeDeclarationSQL**(column): string

* #### Parameters

  * ##### column: { length?<!-- -->: number }

    * ##### optionallength: number

  #### Returns string

### [**](#getindexname)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L692)getIndexName

* ****getIndexName**(tableName, columns, type): string

* Returns the default name of index for the given columns

  ***

  #### Parameters

  * ##### tableName: string

  * ##### columns: string\[]

  * ##### type: primary | index | unique | foreign | sequence

  #### Returns string

### [**](#getintegertypedeclarationsql)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L226)getIntegerTypeDeclarationSQL

* ****getIntegerTypeDeclarationSQL**(column): string

* #### Parameters

  * ##### column: { autoincrement?<!-- -->: boolean; length?<!-- -->: number; unsigned?<!-- -->: boolean }

    * ##### optionalautoincrement: boolean

    * ##### optionallength: number

    * ##### optionalunsigned: boolean

  #### Returns string

### [**](#getintervaltypedeclarationsql)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L254)getIntervalTypeDeclarationSQL

* ****getIntervalTypeDeclarationSQL**(column): string

* #### Parameters

  * ##### column: { length?<!-- -->: number }

    * ##### optionallength: number

  #### Returns string

### [**](#getjsondeclarationsql)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L414)getJsonDeclarationSQL

* ****getJsonDeclarationSQL**(): string

* #### Returns string

### [**](#getjsonindexdefinition)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L465)getJsonIndexDefinition

* ****getJsonIndexDefinition**(index): string\[]

* #### Parameters

  * ##### index: { columnNames: string\[] }

    * ##### columnNames: string\[]

  #### Returns string\[]

### [**](#getmappedtype)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L307)getMappedType

* ****getMappedType**(type): [Type](https://mikro-orm.io/api/core/class/Type.md)\<unknown, unknown>

* #### Parameters

  * ##### type: string

  #### Returns [Type](https://mikro-orm.io/api/core/class/Type.md)\<unknown, unknown>

### [**](#getmediuminttypedeclarationsql)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L234)getMediumIntTypeDeclarationSQL

* ****getMediumIntTypeDeclarationSQL**(column): string

* #### Parameters

  * ##### column: { autoincrement?<!-- -->: boolean; length?<!-- -->: number; unsigned?<!-- -->: boolean }

    * ##### optionalautoincrement: boolean

    * ##### optionallength: number

    * ##### optionalunsigned: boolean

  #### Returns string

### [**](#getnamingstrategy)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L75)getNamingStrategy

* ****getNamingStrategy**(): new () => [NamingStrategy](https://mikro-orm.io/api/core/interface/NamingStrategy.md)

* #### Returns new () => [NamingStrategy](https://mikro-orm.io/api/core/interface/NamingStrategy.md)

  * * **new (): [NamingStrategy](https://mikro-orm.io/api/core/interface/NamingStrategy.md)

    * #### Returns [NamingStrategy](https://mikro-orm.io/api/core/interface/NamingStrategy.md)

### [**](#getregexpoperator)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L176)getRegExpOperator

* ****getRegExpOperator**(val, flags): string

* #### Parameters

  * ##### optionalval: unknown

  * ##### optionalflags: string

  #### Returns string

### [**](#getregexpvalue)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L187)getRegExpValue

* ****getRegExpValue**(val): { $flags?
  <!-- -->
  : string; $re: string }

* #### Parameters

  * ##### val: RegExp

  #### Returns { $flags?<!-- -->: string; $re: string }

  * ##### optional$flags?<!-- -->: string

  * ##### $re: string

### [**](#getrepositoryclass)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L541)getRepositoryClass

* ****getRepositoryClass**\<T>(): [Constructor](https://mikro-orm.io/api/core.md#Constructor)<[EntityRepository](https://mikro-orm.io/api/core/class/EntityRepository.md)\<T>>

* #### Returns [Constructor](https://mikro-orm.io/api/core.md#Constructor)<[EntityRepository](https://mikro-orm.io/api/core/class/EntityRepository.md)\<T>>

### [**](#getsearchjsonpropertykey)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L422)getSearchJsonPropertyKey

* ****getSearchJsonPropertyKey**(path, type, aliased, value): string | [RawQueryFragment](https://mikro-orm.io/api/core/class/RawQueryFragment.md)\<string>

* #### Parameters

  * ##### path: string\[]

  * ##### type: string

  * ##### aliased: boolean

  * ##### optionalvalue: unknown

  #### Returns string | [RawQueryFragment](https://mikro-orm.io/api/core/class/RawQueryFragment.md)\<string>

### [**](#getsearchjsonpropertysql)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L418)getSearchJsonPropertySQL

* ****getSearchJsonPropertySQL**(path, type, aliased): string | [RawQueryFragment](https://mikro-orm.io/api/core/class/RawQueryFragment.md)\<string>

* #### Parameters

  * ##### path: string

  * ##### type: string

  * ##### aliased: boolean

  #### Returns string | [RawQueryFragment](https://mikro-orm.io/api/core/class/RawQueryFragment.md)\<string>

### [**](#getschemagenerator)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L579)getSchemaGenerator

* ****getSchemaGenerator**(driver, em): [ISchemaGenerator](https://mikro-orm.io/api/core/interface/ISchemaGenerator.md)

* #### Parameters

  * ##### driver: [IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>

  * ##### optionalem: [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>

  #### Returns [ISchemaGenerator](https://mikro-orm.io/api/core/interface/ISchemaGenerator.md)

### [**](#getschemahelper)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L105)getSchemaHelper

* ****getSchemaHelper**(): unknown

* #### Returns unknown

### [**](#getsmallinttypedeclarationsql)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L230)getSmallIntTypeDeclarationSQL

* ****getSmallIntTypeDeclarationSQL**(column): string

* #### Parameters

  * ##### column: { autoincrement?<!-- -->: boolean; length?<!-- -->: number; unsigned?<!-- -->: boolean }

    * ##### optionalautoincrement: boolean

    * ##### optionallength: number

    * ##### optionalunsigned: boolean

  #### Returns string

### [**](#gettexttypedeclarationsql)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L258)getTextTypeDeclarationSQL

* ****getTextTypeDeclarationSQL**(\_column): string

* #### Parameters

  * ##### \_column: { length?<!-- -->: number }

    * ##### optionallength: number

  #### Returns string

### [**](#gettimetypedeclarationsql)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L172)getTimeTypeDeclarationSQL

* ****getTimeTypeDeclarationSQL**(length): string

* #### Parameters

  * ##### optionallength: number

  #### Returns string

### [**](#gettimezone)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L672)getTimezone

* ****getTimezone**(): undefined | string

* #### Returns undefined | string

### [**](#gettinyinttypedeclarationsql)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L238)getTinyIntTypeDeclarationSQL

* ****getTinyIntTypeDeclarationSQL**(column): string

* #### Parameters

  * ##### column: { autoincrement?<!-- -->: boolean; length?<!-- -->: number; unsigned?<!-- -->: boolean }

    * ##### optionalautoincrement: boolean

    * ##### optionallength: number

    * ##### optionalunsigned: boolean

  #### Returns string

### [**](#getuuidtypedeclarationsql)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L291)getUuidTypeDeclarationSQL

* ****getUuidTypeDeclarationSQL**(column): string

* #### Parameters

  * ##### column: { length?<!-- -->: number }

    * ##### optionallength: number

  #### Returns string

### [**](#getvarchartypedeclarationsql)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L250)getVarcharTypeDeclarationSQL

* ****getVarcharTypeDeclarationSQL**(column): string

* #### Parameters

  * ##### column: { length?<!-- -->: number }

    * ##### optionallength: number

  #### Returns string

### [**](#indexforeignkeys)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L109)indexForeignKeys

* ****indexForeignKeys**(): boolean

* #### Returns boolean

### [**](#isallowedtopleveloperator)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L195)isAllowedTopLevelOperator

* ****isAllowedTopLevelOperator**(operator): boolean

* #### Parameters

  * ##### operator: string

  #### Returns boolean

### [**](#isbigintproperty)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L214)isBigIntProperty

* ****isBigIntProperty**(prop): boolean

* #### Parameters

  * ##### prop: [EntityProperty](https://mikro-orm.io/api/core/interface/EntityProperty.md)\<any, any>

  #### Returns boolean

### [**](#isnumericcolumn)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L681)isNumericColumn

* ****isNumericColumn**(mappedType): boolean

* #### Parameters

  * ##### mappedType: [Type](https://mikro-orm.io/api/core/class/Type.md)\<unknown, unknown>

  #### Returns boolean

### [**](#isnumericproperty)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L676)isNumericProperty

* ****isNumericProperty**(prop, ignoreCustomType): boolean

* #### Parameters

  * ##### prop: [EntityProperty](https://mikro-orm.io/api/core/interface/EntityProperty.md)\<any, any>

  * ##### ignoreCustomType: boolean = <!-- -->false

  #### Returns boolean

### [**](#ispopulated)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L708)isPopulated

* ****isPopulated**\<T>(key, populate): boolean

* #### Parameters

  * ##### key: string

  * ##### populate: boolean | readonly<!-- --> [PopulateOptions](https://mikro-orm.io/api/core.md#PopulateOptions)\<T>\[]

  #### Returns boolean

### [**](#lookupextensions)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L556)lookupExtensions

* ****lookupExtensions**(orm): void

* Allows registering extensions of the driver automatically (e.g. `SchemaGenerator` extension in SQL drivers).

  ***

  #### Parameters

  * ##### orm: [MikroORM](https://mikro-orm.io/api/core/class/MikroORM.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>, [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>, (string | [EntitySchema](https://mikro-orm.io/api/core/class/EntitySchema.md)\<any, never, [EntityCtor](https://mikro-orm.io/api/core.md#EntityCtor)\<any>> | [EntityClass](https://mikro-orm.io/api/core.md#EntityClass)\<Partial\<any>>)\[]>

  #### Returns void

### [**](#mapregexpcondition)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L180)mapRegExpCondition

* ****mapRegExpCondition**(mappedKey, value): { params: unknown\[]; sql: string }

* #### Parameters

  * ##### mappedKey: string

  * ##### value: { $flags?<!-- -->: string; $re: string }

    * ##### optional$flags: string

    * ##### $re: string

  #### Returns { params: unknown\[]; sql: string }

  * ##### params: unknown\[]

  * ##### sql: string

### [**](#marshallarray)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L398)marshallArray

* ****marshallArray**(values): string

* #### Parameters

  * ##### values: string\[]

  #### Returns string

### [**](#normalizecolumntype)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L303)normalizeColumnType

* ****normalizeColumnType**(type, options): string

* This should be used only to compare types, it can strip some information like the length.

  ***

  #### Parameters

  * ##### type: string

  * ##### options: { length?<!-- -->: number; precision?<!-- -->: number; scale?<!-- -->: number }

    * ##### optionallength: number

    * ##### optionalprecision: number

    * ##### optionalscale: number

  #### Returns string

### [**](#normalizeprimarykey)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L134)normalizePrimaryKey

* ****normalizePrimaryKey**\<T>(data): T

* Normalizes primary key wrapper to scalar value (e.g. mongodb's ObjectId to string)

  ***

  #### Parameters

  * ##### data: IPrimaryKeyValue | [Primary](https://mikro-orm.io/api/core.md#Primary)\<T>

  #### Returns T

### [**](#parsedate)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L530)parseDate

* ****parseDate**(value): Date

* #### Parameters

  * ##### value: string | number

  #### Returns Date

### [**](#processdateproperty)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L583)processDateProperty

* ****processDateProperty**(value): string | number | Date

* #### Parameters

  * ##### value: unknown

  #### Returns string | number | Date

### [**](#processjsoncondition)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L426)processJsonCondition

* ****processJsonCondition**\<T>(o, value, path, alias): [FilterQuery](https://mikro-orm.io/api/core.md#FilterQuery)\<T>

* #### Parameters

  * ##### o: [FilterQuery](https://mikro-orm.io/api/core.md#FilterQuery)\<T>

  * ##### value: [EntityValue](https://mikro-orm.io/api/core.md#EntityValue)\<T>

  * ##### path: [EntityKey](https://mikro-orm.io/api/core.md#EntityKey)\<T>\[]

  * ##### alias: boolean

  #### Returns [FilterQuery](https://mikro-orm.io/api/core.md#FilterQuery)\<T>

### [**](#quoteidentifier)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L587)quoteIdentifier

* ****quoteIdentifier**(id, quote): string

* #### Parameters

  * ##### id: string | { toString: () => string }

  * * ##### toString: () => string

    ##### quote: string = <!-- -->'\`'

  #### Returns string

### [**](#quotevalue)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L597)quoteValue

* ****quoteValue**(value): string

* #### Parameters

  * ##### value: any

  #### Returns string

### [**](#setconfig)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L657)setConfig

* ****setConfig**(config): void

* #### Parameters

  * ##### config: [Configuration](https://mikro-orm.io/api/core/class/Configuration.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>, [EntityManager](https://mikro-orm.io/api/core/class/EntityManager.md)<[IDatabaseDriver](https://mikro-orm.io/api/core/interface/IDatabaseDriver.md)<[Connection](https://mikro-orm.io/api/core/class/Connection.md)>>>

  #### Returns void

### [**](#shouldhavecolumn)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L712)shouldHaveColumn

* ****shouldHaveColumn**\<T>(prop, populate, exclude, includeFormulas, ignoreInlineEmbeddables): boolean

* #### Parameters

  * ##### prop: [EntityProperty](https://mikro-orm.io/api/core/interface/EntityProperty.md)\<T, any>

  * ##### populate: boolean | readonly<!-- --> [PopulateOptions](https://mikro-orm.io/api/core.md#PopulateOptions)\<T>\[]

  * ##### optionalexclude: string\[]

  * ##### includeFormulas: boolean = <!-- -->true

  * ##### ignoreInlineEmbeddables: boolean = <!-- -->true

  #### Returns boolean

### [**](#supportscreatingfulltextindex)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L473)supportsCreatingFullTextIndex

* ****supportsCreatingFullTextIndex**(): boolean

* #### Returns boolean

### [**](#supportscustomprimarykeynames)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L704)supportsCustomPrimaryKeyNames

* ****supportsCustomPrimaryKeyNames**(): boolean

* #### Returns boolean

### [**](#supportsdeferreduniqueconstraints)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L757)supportsDeferredUniqueConstraints

* ****supportsDeferredUniqueConstraints**(): boolean

* #### Returns boolean

### [**](#supportsdownmigrations)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L753)supportsDownMigrations

* ****supportsDownMigrations**(): boolean

* Currently not supported due to how knex does complex sqlite diffing (always based on current schema)

  ***

  #### Returns boolean

### [**](#supportsmaterializedviews)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L101)supportsMaterializedViews

* ****supportsMaterializedViews**(): boolean

* #### Returns boolean

### [**](#supportsmultiplecascadepaths)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L374)supportsMultipleCascadePaths

* ****supportsMultipleCascadePaths**(): boolean

* #### Returns boolean

### [**](#supportsmultiplestatements)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L386)supportsMultipleStatements

* ****supportsMultipleStatements**(): boolean

* #### Returns boolean

### [**](#supportsnativeenums)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L92)supportsNativeEnums

* ****supportsNativeEnums**(): boolean

* for postgres native enums

  ***

  #### Returns boolean

### [**](#supportsonupdate)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L382)supportsOnUpdate

* ****supportsOnUpdate**(): boolean

* Returns true if the platform supports ON UPDATE foreign key rules. Oracle doesn't support ON UPDATE rules.

  ***

  #### Returns boolean

### [**](#supportstransactions)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L67)supportsTransactions

* ****supportsTransactions**(): boolean

* #### Returns boolean

### [**](#supportsunionwhere)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L390)supportsUnionWhere

* ****supportsUnionWhere**(): boolean

* #### Returns boolean

### [**](#supportsunsigned)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L685)supportsUnsigned

* ****supportsUnsigned**(): boolean

* #### Returns boolean

### [**](#unmarshallarray)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L402)unmarshallArray

* ****unmarshallArray**(value): string\[]

* #### Parameters

  * ##### value: string

  #### Returns string\[]

### [**](#usesaskeyword)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L510)usesAsKeyword

* ****usesAsKeyword**(): boolean

* #### Returns boolean

### [**](#usesbatchinserts)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L116)usesBatchInserts

* ****usesBatchInserts**(): boolean

* Whether or not the driver supports retuning list of created PKs back when multi-inserting

  ***

  #### Returns boolean

### [**](#usesbatchupdates)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L123)usesBatchUpdates

* ****usesBatchUpdates**(): boolean

* Whether or not the driver supports updating many records at once

  ***

  #### Returns boolean

### [**](#usescascadestatement)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L87)usesCascadeStatement

* ****usesCascadeStatement**(): boolean

* #### Returns boolean

### [**](#usesdefaultkeyword)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L127)usesDefaultKeyword

* ****usesDefaultKeyword**(): boolean

* #### Returns boolean

### [**](#usesenumcheckconstraints)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L97)usesEnumCheckConstraints

* ****usesEnumCheckConstraints**(): boolean

* for postgres text enums (default)

  ***

  #### Returns boolean

### [**](#usesimplicittransactions)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L71)usesImplicitTransactions

* ****usesImplicitTransactions**(): boolean

* #### Returns boolean

### [**](#usesoutputstatement)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L83)usesOutputStatement

* ****usesOutputStatement**(): boolean

* #### Returns boolean

### [**](#usespivottable)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L63)usesPivotTable

* ****usesPivotTable**(): boolean

* #### Returns boolean

### [**](#usesreturningstatement)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L79)usesReturningStatement

* ****usesReturningStatement**(): boolean

* #### Returns boolean

### [**](#validatemetadata)[**](https://github.com/mikro-orm/mikro-orm/blob/2d81de2234119ed7f17968f65d36b3a7d165bb5c/packages/core/src/platforms/Platform.ts#L761)validateMetadata

* ****validateMetadata**(meta): void

* #### Parameters

  * ##### meta: [EntityMetadata](https://mikro-orm.io/api/core/class/EntityMetadata.md)\<any, [EntityCtor](https://mikro-orm.io/api/core.md#EntityCtor)\<any>>

  #### Returns void
