# Source: https://mikro-orm.io/api/postgresql/class/PostgreSqlSchemaHelper.md

# PostgreSqlSchemaHelper<!-- -->

### Hierarchy

* [SchemaHelper](https://mikro-orm.io/api/knex/class/SchemaHelper.md)
  * *PostgreSqlSchemaHelper*

## Index[**](#Index)

### Constructors

* [**constructor](#constructor)

### Properties

* [**DEFAULT\_VALUES](#DEFAULT_VALUES)

### Accessors

* [**knex](#knex)
* [**options](#options)

### Methods

* [**configureColumn](#configureColumn)
* [**configureColumnDefault](#configureColumnDefault)
* [**createCheck](#createCheck)
* [**createForeignKey](#createForeignKey)
* [**createIndex](#createIndex)
* [**createSchemaBuilder](#createSchemaBuilder)
* [**createTable](#createTable)
* [**createTableColumn](#createTableColumn)
* [**databaseExists](#databaseExists)
* [**disableForeignKeysSQL](#disableForeignKeysSQL)
* [**dump](#dump)
* [**enableForeignKeysSQL](#enableForeignKeysSQL)
* [**finalizeTable](#finalizeTable)
* [**getAllChecks](#getAllChecks)
* [**getAllColumns](#getAllColumns)
* [**getAllForeignKeys](#getAllForeignKeys)
* [**getAllIndexes](#getAllIndexes)
* [**getAlterColumnAutoincrement](#getAlterColumnAutoincrement)
* [**getAlterNativeEnumSQL](#getAlterNativeEnumSQL)
* [**getAlterTable](#getAlterTable)
* [**getChangeColumnCommentSQL](#getChangeColumnCommentSQL)
* [**getChecks](#getChecks)
* [**getColumns](#getColumns)
* [**getCreateDatabaseSQL](#getCreateDatabaseSQL)
* [**getCreateIndexSQL](#getCreateIndexSQL)
* [**getCreateNamespaceSQL](#getCreateNamespaceSQL)
* [**getCreateNativeEnumSQL](#getCreateNativeEnumSQL)
* [**getDatabaseExistsSQL](#getDatabaseExistsSQL)
* [**getDatabaseNotExistsError](#getDatabaseNotExistsError)
* [**getDefaultEmptyString](#getDefaultEmptyString)
* [**getDropColumnsSQL](#getDropColumnsSQL)
* [**getDropDatabaseSQL](#getDropDatabaseSQL)
* [**getDropIndexSQL](#getDropIndexSQL)
* [**getDropNamespaceSQL](#getDropNamespaceSQL)
* [**getDropNativeEnumSQL](#getDropNativeEnumSQL)
* [**getEnumDefinitions](#getEnumDefinitions)
* [**getForeignKeys](#getForeignKeys)
* [**getForeignKeysSQL](#getForeignKeysSQL)
* [**getIndexes](#getIndexes)
* [**getListTablesSQL](#getListTablesSQL)
* [**getManagementDbName](#getManagementDbName)
* [**getNamespaces](#getNamespaces)
* [**getNativeEnumDefinitions](#getNativeEnumDefinitions)
* [**getPostAlterTable](#getPostAlterTable)
* [**getPreAlterTable](#getPreAlterTable)
* [**getPrimaryKeys](#getPrimaryKeys)
* [**getReferencedTableName](#getReferencedTableName)
* [**getRenameColumnSQL](#getRenameColumnSQL)
* [**getRenameIndexSQL](#getRenameIndexSQL)
* [**getSchemaBeginning](#getSchemaBeginning)
* [**getSchemaEnd](#getSchemaEnd)
* [**getTablesGroupedBySchemas](#getTablesGroupedBySchemas)
* [**hasNonDefaultPrimaryKeyName](#hasNonDefaultPrimaryKeyName)
* [**inferLengthFromColumnType](#inferLengthFromColumnType)
* [**loadInformationSchema](#loadInformationSchema)
* [**mapForeignKeys](#mapForeignKeys)
* [**normalizeDefaultValue](#normalizeDefaultValue)
* [**pushTableQuery](#pushTableQuery)
* [**splitTableName](#splitTableName)
* [**supportsSchemaConstraints](#supportsSchemaConstraints)

## Constructors<!-- -->[**](#Constructors)

### [**](#constructor)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaHelper.ts#L18)constructor

* ****new PostgreSqlSchemaHelper**(platform): [PostgreSqlSchemaHelper](https://mikro-orm.io/api/postgresql/class/PostgreSqlSchemaHelper.md)

- Inherited from SchemaHelper.constructor

  #### Parameters

  * ##### platform: [AbstractSqlPlatform](https://mikro-orm.io/api/knex/class/AbstractSqlPlatform.md)

  #### Returns [PostgreSqlSchemaHelper](https://mikro-orm.io/api/postgresql/class/PostgreSqlSchemaHelper.md)

## Properties<!-- -->[**](#Properties)

### [**](#DEFAULT_VALUES)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/postgresql/src/PostgreSqlSchemaHelper.ts#L18)staticreadonlyDEFAULT\_VALUES

**DEFAULT\_VALUES: { ('now'::text)::timestamp(?) with time zone: string\[]; ('now'::text)::timestamp(?) without time zone: string\[]; current\_timestamp(?): string\[]; now(): string\[]; null::character varying: string\[]; null::timestamp with time zone: string\[]; null::timestamp without time zone: string\[] } =

<!-- -->

...

#### Type declaration

* ##### ('now'::text)::timestamp(?) with time zone: string\[]
* ##### ('now'::text)::timestamp(?) without time zone: string\[]
* ##### current\_timestamp(?): string\[]
* ##### now(): string\[]
* ##### null::character varying: string\[]
* ##### null::timestamp with time zone: string\[]
* ##### null::timestamp without time zone: string\[]

## Accessors<!-- -->[**](#Accessors)

### [**](#knex)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaHelper.ts#L535)inheritedknex

* **get knex(): [Knex](https://mikro-orm.io/api/knex/interface/Knex.md)\<any, any\[]>

- Inherited from SchemaHelper.knex

  #### Returns [Knex](https://mikro-orm.io/api/knex/interface/Knex.md)\<any, any\[]>

### [**](#options)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaHelper.ts#L540)inheritedoptions

* **get options(): { createForeignKeyConstraints?
  <!-- -->
  : boolean; disableForeignKeys?
  <!-- -->
  : boolean; ignoreSchema?
  <!-- -->
  : string\[]; managementDbName?
  <!-- -->
  : string; skipColumns?
  <!-- -->
  : [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)<(string | RegExp)\[]>; skipTables?
  <!-- -->
  : (string | RegExp)\[] }

- Inherited from SchemaHelper.options

  #### Returns { createForeignKeyConstraints?<!-- -->: boolean; disableForeignKeys?<!-- -->: boolean; ignoreSchema?<!-- -->: string\[]; managementDbName?<!-- -->: string; skipColumns?<!-- -->: [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)<(string | RegExp)\[]>; skipTables?<!-- -->: (string | RegExp)\[] }

  * ##### optionalcreateForeignKeyConstraints?<!-- -->: boolean
  * ##### optionaldisableForeignKeys?<!-- -->: boolean
  * ##### optionalignoreSchema?<!-- -->: string\[]
  * ##### optionalmanagementDbName?<!-- -->: string
  * ##### optionalskipColumns?<!-- -->: [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)<(string | RegExp)\[]>
  * ##### optionalskipTables?<!-- -->: (string | RegExp)\[]

## Methods<!-- -->[**](#Methods)

### [**](#configureColumn)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/postgresql/src/PostgreSqlSchemaHelper.ts#L492)configureColumn

* ****configureColumn**(column, col, knex, changedProperties): ColumnBuilder

- Overrides SchemaHelper.configureColumn

  #### Parameters

  * ##### column: [Column](https://mikro-orm.io/api/knex/interface/Column.md)
  * ##### col: ColumnBuilder
  * ##### knex: [Knex](https://mikro-orm.io/api/knex/interface/Knex.md)\<any, any\[]>
  * ##### optionalchangedProperties: Set\<string>

  #### Returns ColumnBuilder

### [**](#configureColumnDefault)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaHelper.ts#L212)inheritedconfigureColumnDefault

* ****configureColumnDefault**(column, col, knex, changedProperties): ColumnBuilder

- Inherited from SchemaHelper.configureColumnDefault

  #### Parameters

  * ##### column: [Column](https://mikro-orm.io/api/knex/interface/Column.md)
  * ##### col: ColumnBuilder
  * ##### knex: [Knex](https://mikro-orm.io/api/knex/interface/Knex.md)\<any, any\[]>
  * ##### optionalchangedProperties: Set\<string>

  #### Returns ColumnBuilder

### [**](#createCheck)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaHelper.ts#L507)inheritedcreateCheck

* ****createCheck**(table, check): void

- Inherited from SchemaHelper.createCheck

  #### Parameters

  * ##### table: CreateTableBuilder
  * ##### check: [CheckDef](https://mikro-orm.io/api/knex/interface/CheckDef.md)\<unknown>

  #### Returns void

### [**](#createForeignKey)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaHelper.ts#L422)inheritedcreateForeignKey

* ****createForeignKey**(table, foreignKey, schema): void

- Inherited from SchemaHelper.createForeignKey

  #### Parameters

  * ##### table: CreateTableBuilder
  * ##### foreignKey: [ForeignKey](https://mikro-orm.io/api/knex/interface/ForeignKey.md)
  * ##### optionalschema: string

  #### Returns void

### [**](#createIndex)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaHelper.ts#L472)inheritedcreateIndex

* ****createIndex**(table, index, tableDef, createPrimary): void

- Inherited from SchemaHelper.createIndex

  #### Parameters

  * ##### table: CreateTableBuilder
  * ##### index: [IndexDef](https://mikro-orm.io/api/knex/interface/IndexDef.md)
  * ##### tableDef: DatabaseTable
  * ##### createPrimary: boolean = <!-- -->false

  #### Returns void

### [**](#createSchemaBuilder)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaHelper.ts#L511)inheritedcreateSchemaBuilder

* ****createSchemaBuilder**(schema): SchemaBuilder

- Inherited from SchemaHelper.createSchemaBuilder

  #### Parameters

  * ##### optionalschema: string

  #### Returns SchemaBuilder

### [**](#createTable)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaHelper.ts#L391)inheritedcreateTable

* ****createTable**(tableDef, alter): SchemaBuilder

- Inherited from SchemaHelper.createTable

  #### Parameters

  * ##### tableDef: DatabaseTable
  * ##### optionalalter: boolean

  #### Returns SchemaBuilder

### [**](#createTableColumn)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/postgresql/src/PostgreSqlSchemaHelper.ts#L414)createTableColumn

* ****createTableColumn**(table, column, fromTable, changedProperties, alter): undefined | ColumnBuilder

- Overrides SchemaHelper.createTableColumn

  #### Parameters

  * ##### table: TableBuilder
  * ##### column: [Column](https://mikro-orm.io/api/knex/interface/Column.md)
  * ##### fromTable: DatabaseTable
  * ##### optionalchangedProperties: Set\<string>
  * ##### optionalalter: boolean

  #### Returns undefined | ColumnBuilder

### [**](#databaseExists)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaHelper.ts#L353)inheriteddatabaseExists

* ****databaseExists**(connection, name): Promise\<boolean>

- Inherited from SchemaHelper.databaseExists

  #### Parameters

  * ##### connection: [Connection](https://mikro-orm.io/api/core/class/Connection.md)
  * ##### name: string

  #### Returns Promise\<boolean>

### [**](#disableForeignKeysSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/postgresql/src/PostgreSqlSchemaHelper.ts#L625)disableForeignKeysSQL

* ****disableForeignKeysSQL**(): string

- Overrides SchemaHelper.disableForeignKeysSQL

  #### Returns string

### [**](#dump)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaHelper.ts#L373)inheriteddump

* ****dump**(builder, append): Promise\<string>

- Inherited from SchemaHelper.dump

  #### Parameters

  * ##### builder: string | SchemaBuilder
  * ##### append: string

  #### Returns Promise\<string>

### [**](#enableForeignKeysSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/postgresql/src/PostgreSqlSchemaHelper.ts#L629)enableForeignKeysSQL

* ****enableForeignKeysSQL**(): string

- Overrides SchemaHelper.enableForeignKeysSQL

  #### Returns string

### [**](#finalizeTable)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaHelper.ts#L44)inheritedfinalizeTable

* ****finalizeTable**(table, charset, collate): void

- Inherited from SchemaHelper.finalizeTable

  #### Parameters

  * ##### table: TableBuilder
  * ##### charset: string
  * ##### optionalcollate: string

  #### Returns void

### [**](#getAllChecks)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/postgresql/src/PostgreSqlSchemaHelper.ts#L226)getAllChecks

* ****getAllChecks**(connection, tablesBySchemas): Promise<[Dictionary](https://mikro-orm.io/api/core.md#Dictionary)<[CheckDef](https://mikro-orm.io/api/knex/interface/CheckDef.md)\<unknown>\[]>>

- #### Parameters

  * ##### connection: [AbstractSqlConnection](https://mikro-orm.io/api/knex/class/AbstractSqlConnection.md)
  * ##### tablesBySchemas: Map\<undefined | string, [Table](https://mikro-orm.io/api/knex/interface/Table.md)\[]>

  #### Returns Promise<[Dictionary](https://mikro-orm.io/api/core.md#Dictionary)<[CheckDef](https://mikro-orm.io/api/knex/interface/CheckDef.md)\<unknown>\[]>>

### [**](#getAllColumns)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/postgresql/src/PostgreSqlSchemaHelper.ts#L143)getAllColumns

* ****getAllColumns**(connection, tablesBySchemas, nativeEnums): Promise<[Dictionary](https://mikro-orm.io/api/core.md#Dictionary)<[Column](https://mikro-orm.io/api/knex/interface/Column.md)\[]>>

- #### Parameters

  * ##### connection: [AbstractSqlConnection](https://mikro-orm.io/api/knex/class/AbstractSqlConnection.md)
  * ##### tablesBySchemas: Map\<undefined | string, [Table](https://mikro-orm.io/api/knex/interface/Table.md)\[]>
  * ##### optionalnativeEnums: [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)<{ items: string\[]; name: string; schema?<!-- -->: string }>

  #### Returns Promise<[Dictionary](https://mikro-orm.io/api/core.md#Dictionary)<[Column](https://mikro-orm.io/api/knex/interface/Column.md)\[]>>

### [**](#getAllForeignKeys)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/postgresql/src/PostgreSqlSchemaHelper.ts#L247)getAllForeignKeys

* ****getAllForeignKeys**(connection, tablesBySchemas): Promise<[Dictionary](https://mikro-orm.io/api/core.md#Dictionary)<[Dictionary](https://mikro-orm.io/api/core.md#Dictionary)<[ForeignKey](https://mikro-orm.io/api/knex/interface/ForeignKey.md)>>>

- #### Parameters

  * ##### connection: [AbstractSqlConnection](https://mikro-orm.io/api/knex/class/AbstractSqlConnection.md)
  * ##### tablesBySchemas: Map\<undefined | string, [Table](https://mikro-orm.io/api/knex/interface/Table.md)\[]>

  #### Returns Promise<[Dictionary](https://mikro-orm.io/api/core.md#Dictionary)<[Dictionary](https://mikro-orm.io/api/core.md#Dictionary)<[ForeignKey](https://mikro-orm.io/api/knex/interface/ForeignKey.md)>>>

### [**](#getAllIndexes)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/postgresql/src/PostgreSqlSchemaHelper.ts#L106)getAllIndexes

* ****getAllIndexes**(connection, tables): Promise<[Dictionary](https://mikro-orm.io/api/core.md#Dictionary)<[IndexDef](https://mikro-orm.io/api/knex/interface/IndexDef.md)\[]>>

- #### Parameters

  * ##### connection: [AbstractSqlConnection](https://mikro-orm.io/api/knex/class/AbstractSqlConnection.md)
  * ##### tables: [Table](https://mikro-orm.io/api/knex/interface/Table.md)\[]

  #### Returns Promise<[Dictionary](https://mikro-orm.io/api/core.md#Dictionary)<[IndexDef](https://mikro-orm.io/api/knex/interface/IndexDef.md)\[]>>

### [**](#getAlterColumnAutoincrement)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/postgresql/src/PostgreSqlSchemaHelper.ts#L570)getAlterColumnAutoincrement

* ****getAlterColumnAutoincrement**(tableName, column, schemaName): string

- Overrides SchemaHelper.getAlterColumnAutoincrement

  #### Parameters

  * ##### tableName: string
  * ##### column: [Column](https://mikro-orm.io/api/knex/interface/Column.md)
  * ##### optionalschemaName: string

  #### Returns string

### [**](#getAlterNativeEnumSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/postgresql/src/PostgreSqlSchemaHelper.ts#L355)getAlterNativeEnumSQL

* ****getAlterNativeEnumSQL**(name, schema, value, items, oldItems): string

- Overrides SchemaHelper.getAlterNativeEnumSQL

  #### Parameters

  * ##### name: string
  * ##### optionalschema: string
  * ##### optionalvalue: string
  * ##### optionalitems: string\[]
  * ##### optionaloldItems: string\[]

  #### Returns string

### [**](#getAlterTable)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaHelper.ts#L533)optionalinheritedgetAlterTable

* ****getAlterTable**(changedTable, wrap): Promise\<string>

- Inherited from SchemaHelper.getAlterTable

  #### Parameters

  * ##### changedTable: [TableDifference](https://mikro-orm.io/api/knex/interface/TableDifference.md)
  * ##### optionalwrap: boolean

  #### Returns Promise\<string>

### [**](#getChangeColumnCommentSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/postgresql/src/PostgreSqlSchemaHelper.ts#L589)getChangeColumnCommentSQL

* ****getChangeColumnCommentSQL**(tableName, to, schemaName): string

- Overrides SchemaHelper.getChangeColumnCommentSQL

  #### Parameters

  * ##### tableName: string
  * ##### to: [Column](https://mikro-orm.io/api/knex/interface/Column.md)
  * ##### optionalschemaName: string

  #### Returns string

### [**](#getChecks)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/postgresql/src/PostgreSqlSchemaHelper.ts#L669)getChecks

* ****getChecks**(connection, tableName, schemaName, columns): Promise<[CheckDef](https://mikro-orm.io/api/knex/interface/CheckDef.md)\<unknown>\[]>

- Overrides SchemaHelper.getChecks

  #### Parameters

  * ##### connection: [AbstractSqlConnection](https://mikro-orm.io/api/knex/class/AbstractSqlConnection.md)
  * ##### tableName: string
  * ##### schemaName: string
  * ##### optionalcolumns: [Column](https://mikro-orm.io/api/knex/interface/Column.md)\[]

  #### Returns Promise<[CheckDef](https://mikro-orm.io/api/knex/interface/CheckDef.md)\<unknown>\[]>

### [**](#getColumns)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/postgresql/src/PostgreSqlSchemaHelper.ts#L675)getColumns

* ****getColumns**(connection, tableName, schemaName): Promise<[Column](https://mikro-orm.io/api/knex/interface/Column.md)\[]>

- Overrides SchemaHelper.getColumns

  #### Parameters

  * ##### connection: [AbstractSqlConnection](https://mikro-orm.io/api/knex/class/AbstractSqlConnection.md)
  * ##### tableName: string
  * ##### optionalschemaName: string

  #### Returns Promise<[Column](https://mikro-orm.io/api/knex/interface/Column.md)\[]>

### [**](#getCreateDatabaseSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/postgresql/src/PostgreSqlSchemaHelper.ts#L36)getCreateDatabaseSQL

* ****getCreateDatabaseSQL**(name): string

- Overrides SchemaHelper.getCreateDatabaseSQL

  #### Parameters

  * ##### name: string

  #### Returns string

### [**](#getCreateIndexSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaHelper.ts#L130)inheritedgetCreateIndexSQL

* ****getCreateIndexSQL**(tableName, index, partialExpression): string

- Inherited from SchemaHelper.getCreateIndexSQL

  #### Parameters

  * ##### tableName: string
  * ##### index: [IndexDef](https://mikro-orm.io/api/knex/interface/IndexDef.md)
  * ##### partialExpression: boolean = <!-- -->false

  #### Returns string

### [**](#getCreateNamespaceSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaHelper.ts#L328)inheritedgetCreateNamespaceSQL

* ****getCreateNamespaceSQL**(name): string

- Inherited from SchemaHelper.getCreateNamespaceSQL

  #### Parameters

  * ##### name: string

  #### Returns string

### [**](#getCreateNativeEnumSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/postgresql/src/PostgreSqlSchemaHelper.ts#L339)getCreateNativeEnumSQL

* ****getCreateNativeEnumSQL**(name, values, schema): string

- Overrides SchemaHelper.getCreateNativeEnumSQL

  #### Parameters

  * ##### name: string
  * ##### values: unknown\[]
  * ##### optionalschema: string

  #### Returns string

### [**](#getDatabaseExistsSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/postgresql/src/PostgreSqlSchemaHelper.ts#L613)getDatabaseExistsSQL

* ****getDatabaseExistsSQL**(name): string

- Overrides SchemaHelper.getDatabaseExistsSQL

  #### Parameters

  * ##### name: string

  #### Returns string

### [**](#getDatabaseNotExistsError)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/postgresql/src/PostgreSqlSchemaHelper.ts#L617)getDatabaseNotExistsError

* ****getDatabaseNotExistsError**(dbName): string

- Overrides SchemaHelper.getDatabaseNotExistsError

  #### Parameters

  * ##### dbName: string

  #### Returns string

### [**](#getDefaultEmptyString)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaHelper.ts#L349)inheritedgetDefaultEmptyString

* ****getDefaultEmptyString**(): string

- Inherited from SchemaHelper.getDefaultEmptyString

  #### Returns string

### [**](#getDropColumnsSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaHelper.ts#L155)inheritedgetDropColumnsSQL

* ****getDropColumnsSQL**(tableName, columns, schemaName): string

- Inherited from SchemaHelper.getDropColumnsSQL

  #### Parameters

  * ##### tableName: string
  * ##### columns: [Column](https://mikro-orm.io/api/knex/interface/Column.md)\[]
  * ##### optionalschemaName: string

  #### Returns string

### [**](#getDropDatabaseSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaHelper.ts#L323)inheritedgetDropDatabaseSQL

* ****getDropDatabaseSQL**(name): string

- Inherited from SchemaHelper.getDropDatabaseSQL

  #### Parameters

  * ##### name: string

  #### Returns string

### [**](#getDropIndexSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaHelper.ts#L147)inheritedgetDropIndexSQL

* ****getDropIndexSQL**(tableName, index): string

- Inherited from SchemaHelper.getDropIndexSQL

  #### Parameters

  * ##### tableName: string
  * ##### index: [IndexDef](https://mikro-orm.io/api/knex/interface/IndexDef.md)

  #### Returns string

### [**](#getDropNamespaceSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaHelper.ts#L333)inheritedgetDropNamespaceSQL

* ****getDropNamespaceSQL**(name): string

- Inherited from SchemaHelper.getDropNamespaceSQL

  #### Parameters

  * ##### name: string

  #### Returns string

### [**](#getDropNativeEnumSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/postgresql/src/PostgreSqlSchemaHelper.ts#L347)getDropNativeEnumSQL

* ****getDropNativeEnumSQL**(name, schema): string

- Overrides SchemaHelper.getDropNativeEnumSQL

  #### Parameters

  * ##### name: string
  * ##### optionalschema: string

  #### Returns string

### [**](#getEnumDefinitions)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/postgresql/src/PostgreSqlSchemaHelper.ts#L375)getEnumDefinitions

* ****getEnumDefinitions**(connection, checks, tableName, schemaName): Promise<[Dictionary](https://mikro-orm.io/api/core.md#Dictionary)\<string\[]>>

- Overrides SchemaHelper.getEnumDefinitions

  #### Parameters

  * ##### connection: [AbstractSqlConnection](https://mikro-orm.io/api/knex/class/AbstractSqlConnection.md)
  * ##### checks: [CheckDef](https://mikro-orm.io/api/knex/interface/CheckDef.md)\<unknown>\[]
  * ##### optionaltableName: string
  * ##### optionalschemaName: string

  #### Returns Promise<[Dictionary](https://mikro-orm.io/api/core.md#Dictionary)\<string\[]>>

### [**](#getForeignKeys)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaHelper.ts#L66)inheritedgetForeignKeys

* ****getForeignKeys**(connection, tableName, schemaName): Promise<[Dictionary](https://mikro-orm.io/api/core.md#Dictionary)>

- Inherited from SchemaHelper.getForeignKeys

  #### Parameters

  * ##### connection: [AbstractSqlConnection](https://mikro-orm.io/api/knex/class/AbstractSqlConnection.md)
  * ##### tableName: string
  * ##### optionalschemaName: string

  #### Returns Promise<[Dictionary](https://mikro-orm.io/api/core.md#Dictionary)>

### [**](#getForeignKeysSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaHelper.ts#L271)inheritedgetForeignKeysSQL

* ****getForeignKeysSQL**(tableName, schemaName): string

- Inherited from SchemaHelper.getForeignKeysSQL

  #### Parameters

  * ##### tableName: string
  * ##### optionalschemaName: string

  #### Returns string

### [**](#getIndexes)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/postgresql/src/PostgreSqlSchemaHelper.ts#L681)getIndexes

* ****getIndexes**(connection, tableName, schemaName): Promise<[IndexDef](https://mikro-orm.io/api/knex/interface/IndexDef.md)\[]>

- Overrides SchemaHelper.getIndexes

  #### Parameters

  * ##### connection: [AbstractSqlConnection](https://mikro-orm.io/api/knex/class/AbstractSqlConnection.md)
  * ##### tableName: string
  * ##### optionalschemaName: string

  #### Returns Promise<[IndexDef](https://mikro-orm.io/api/knex/interface/IndexDef.md)\[]>

### [**](#getListTablesSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/postgresql/src/PostgreSqlSchemaHelper.ts#L40)getListTablesSQL

* ****getListTablesSQL**(): string

- Overrides SchemaHelper.getListTablesSQL

  #### Returns string

### [**](#getManagementDbName)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/postgresql/src/PostgreSqlSchemaHelper.ts#L621)getManagementDbName

* ****getManagementDbName**(): string

- Overrides SchemaHelper.getManagementDbName

  #### Returns string

### [**](#getNamespaces)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/postgresql/src/PostgreSqlSchemaHelper.ts#L51)getNamespaces

* ****getNamespaces**(connection): Promise\<string\[]>

- Overrides SchemaHelper.getNamespaces

  #### Parameters

  * ##### connection: [AbstractSqlConnection](https://mikro-orm.io/api/knex/class/AbstractSqlConnection.md)

  #### Returns Promise\<string\[]>

### [**](#getNativeEnumDefinitions)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/postgresql/src/PostgreSqlSchemaHelper.ts#L305)getNativeEnumDefinitions

* ****getNativeEnumDefinitions**(connection, schemas): Promise<[Dictionary](https://mikro-orm.io/api/core.md#Dictionary)<{ items: string\[]; name: string; schema?
  <!-- -->
  : string }>>

- #### Parameters

  * ##### connection: [AbstractSqlConnection](https://mikro-orm.io/api/knex/class/AbstractSqlConnection.md)
  * ##### schemas: string\[]

  #### Returns Promise<[Dictionary](https://mikro-orm.io/api/core.md#Dictionary)<{ items: string\[]; name: string; schema?<!-- -->: string }>>

### [**](#getPostAlterTable)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/postgresql/src/PostgreSqlSchemaHelper.ts#L544)getPostAlterTable

* ****getPostAlterTable**(tableDiff, safe): string

- Overrides SchemaHelper.getPostAlterTable

  #### Parameters

  * ##### tableDiff: [TableDifference](https://mikro-orm.io/api/knex/interface/TableDifference.md)
  * ##### safe: boolean

  #### Returns string

### [**](#getPreAlterTable)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/postgresql/src/PostgreSqlSchemaHelper.ts#L504)getPreAlterTable

* ****getPreAlterTable**(tableDiff, safe): string

- Overrides SchemaHelper.getPreAlterTable

  #### Parameters

  * ##### tableDiff: [TableDifference](https://mikro-orm.io/api/knex/interface/TableDifference.md)
  * ##### safe: boolean

  #### Returns string

### [**](#getPrimaryKeys)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaHelper.ts#L52)inheritedgetPrimaryKeys

* ****getPrimaryKeys**(connection, indexes, tableName, schemaName): Promise\<string\[]>

- Inherited from SchemaHelper.getPrimaryKeys

  #### Parameters

  * ##### connection: [AbstractSqlConnection](https://mikro-orm.io/api/knex/class/AbstractSqlConnection.md)
  * ##### indexes: [IndexDef](https://mikro-orm.io/api/knex/interface/IndexDef.md)\[] = <!-- -->\[]
  * ##### tableName: string
  * ##### optionalschemaName: string

  #### Returns Promise\<string\[]>

### [**](#getReferencedTableName)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaHelper.ts#L456)inheritedgetReferencedTableName

* ****getReferencedTableName**(referencedTableName, schema): string

- Inherited from SchemaHelper.getReferencedTableName

  #### Parameters

  * ##### referencedTableName: string
  * ##### optionalschema: string

  #### Returns string

### [**](#getRenameColumnSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaHelper.ts#L119)inheritedgetRenameColumnSQL

* ****getRenameColumnSQL**(tableName, oldColumnName, to, schemaName): string

- Inherited from SchemaHelper.getRenameColumnSQL

  #### Parameters

  * ##### tableName: string
  * ##### oldColumnName: string
  * ##### to: [Column](https://mikro-orm.io/api/knex/interface/Column.md)
  * ##### optionalschemaName: string

  #### Returns string

### [**](#getRenameIndexSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/postgresql/src/PostgreSqlSchemaHelper.ts#L633)getRenameIndexSQL

* ****getRenameIndexSQL**(tableName, index, oldIndexName): string

- Overrides SchemaHelper.getRenameIndexSQL

  #### Parameters

  * ##### tableName: string
  * ##### index: [IndexDef](https://mikro-orm.io/api/knex/interface/IndexDef.md)
  * ##### oldIndexName: string

  #### Returns string

### [**](#getSchemaBeginning)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/postgresql/src/PostgreSqlSchemaHelper.ts#L28)getSchemaBeginning

* ****getSchemaBeginning**(charset, disableForeignKeys): string

- Overrides SchemaHelper.getSchemaBeginning

  #### Parameters

  * ##### charset: string
  * ##### optionaldisableForeignKeys: boolean

  #### Returns string

### [**](#getSchemaEnd)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaHelper.ts#L36)inheritedgetSchemaEnd

* ****getSchemaEnd**(disableForeignKeys): string

- Inherited from SchemaHelper.getSchemaEnd

  #### Parameters

  * ##### optionaldisableForeignKeys: boolean

  #### Returns string

### [**](#getTablesGroupedBySchemas)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaHelper.ts#L521)inheritedgetTablesGroupedBySchemas

* ****getTablesGroupedBySchemas**(tables): Map\<undefined | string, [Table](https://mikro-orm.io/api/knex/interface/Table.md)\[]>

- Inherited from SchemaHelper.getTablesGroupedBySchemas

  #### Parameters

  * ##### tables: [Table](https://mikro-orm.io/api/knex/interface/Table.md)\[]

  #### Returns Map\<undefined | string, [Table](https://mikro-orm.io/api/knex/interface/Table.md)\[]>

### [**](#hasNonDefaultPrimaryKeyName)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaHelper.ts#L162)inheritedhasNonDefaultPrimaryKeyName

* ****hasNonDefaultPrimaryKeyName**(table): boolean

- Inherited from SchemaHelper.hasNonDefaultPrimaryKeyName

  #### Parameters

  * ##### table: DatabaseTable

  #### Returns boolean

### [**](#inferLengthFromColumnType)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/postgresql/src/PostgreSqlSchemaHelper.ts#L686)inferLengthFromColumnType

* ****inferLengthFromColumnType**(type): undefined | number

- Overrides SchemaHelper.inferLengthFromColumnType

  #### Parameters

  * ##### type: string

  #### Returns undefined | number

### [**](#loadInformationSchema)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/postgresql/src/PostgreSqlSchemaHelper.ts#L78)loadInformationSchema

* ****loadInformationSchema**(schema, connection, tables, schemas): Promise\<void>

- Overrides SchemaHelper.loadInformationSchema

  #### Parameters

  * ##### schema: DatabaseSchema
  * ##### connection: [AbstractSqlConnection](https://mikro-orm.io/api/knex/class/AbstractSqlConnection.md)
  * ##### tables: [Table](https://mikro-orm.io/api/knex/interface/Table.md)\[]
  * ##### optionalschemas: string\[]

  #### Returns Promise\<void>

### [**](#mapForeignKeys)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaHelper.ts#L275)inheritedmapForeignKeys

* ****mapForeignKeys**(fks, tableName, schemaName): [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)

- Inherited from SchemaHelper.mapForeignKeys

  #### Parameters

  * ##### fks: any\[]
  * ##### tableName: string
  * ##### optionalschemaName: string

  #### Returns [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)

### [**](#normalizeDefaultValue)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/postgresql/src/PostgreSqlSchemaHelper.ts#L595)normalizeDefaultValue

* ****normalizeDefaultValue**(defaultValue, length): string | number

- Overrides SchemaHelper.normalizeDefaultValue

  #### Parameters

  * ##### defaultValue: string
  * ##### length: number

  #### Returns string | number

### [**](#pushTableQuery)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaHelper.ts#L369)inheritedpushTableQuery

* ****pushTableQuery**(table, expression, grouping): void

- Inherited from SchemaHelper.pushTableQuery

  Uses `raw` method injected in `AbstractSqlConnection` to allow adding custom queries inside alter statements.

  ***

  #### Parameters

  * ##### table: TableBuilder
  * ##### expression: string
  * ##### grouping: string = <!-- -->'alterTable'

  #### Returns void

### [**](#splitTableName)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaHelper.ts#L448)inheritedsplitTableName

* ****splitTableName**(name): \[undefined | string, string]

- Inherited from SchemaHelper.splitTableName

  #### Parameters

  * ##### name: string

  #### Returns \[undefined | string, string]

### [**](#supportsSchemaConstraints)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaHelper.ts#L48)inheritedsupportsSchemaConstraints

* ****supportsSchemaConstraints**(): boolean

- Inherited from SchemaHelper.supportsSchemaConstraints

  #### Returns boolean
