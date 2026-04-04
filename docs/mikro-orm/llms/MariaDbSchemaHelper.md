# Source: https://mikro-orm.io/api/mariadb/class/MariaDbSchemaHelper.md

# MariaDbSchemaHelper<!-- -->

### Hierarchy

* [MySqlSchemaHelper](https://mikro-orm.io/api/knex/class/MySqlSchemaHelper.md)
  * *MariaDbSchemaHelper*

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
* [**getAllEnumDefinitions](#getAllEnumDefinitions)
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

* ****new MariaDbSchemaHelper**(platform): [MariaDbSchemaHelper](https://mikro-orm.io/api/mariadb/class/MariaDbSchemaHelper.md)

- Inherited from MySqlSchemaHelper.constructor

  #### Parameters

  * ##### platform: [AbstractSqlPlatform](https://mikro-orm.io/api/knex/class/AbstractSqlPlatform.md)

  #### Returns [MariaDbSchemaHelper](https://mikro-orm.io/api/mariadb/class/MariaDbSchemaHelper.md)

## Properties<!-- -->[**](#Properties)

### [**](#DEFAULT_VALUES)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/dialects/mysql/MySqlSchemaHelper.ts#L13)staticreadonlyinheritedDEFAULT\_VALUES

**DEFAULT\_VALUES: { 0: string\[]; current\_timestamp(?): string\[]; now(): string\[] } =

<!-- -->

...

Inherited from MySqlSchemaHelper.DEFAULT\_VALUES

#### Type declaration

* ##### 0: string\[]
* ##### current\_timestamp(?): string\[]
* ##### now(): string\[]

## Accessors<!-- -->[**](#Accessors)

### [**](#knex)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaHelper.ts#L535)inheritedknex

* **get knex(): [Knex](https://mikro-orm.io/api/knex/interface/Knex.md)\<any, any\[]>

- Inherited from MySqlSchemaHelper.knex

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

- Inherited from MySqlSchemaHelper.options

  #### Returns { createForeignKeyConstraints?<!-- -->: boolean; disableForeignKeys?<!-- -->: boolean; ignoreSchema?<!-- -->: string\[]; managementDbName?<!-- -->: string; skipColumns?<!-- -->: [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)<(string | RegExp)\[]>; skipTables?<!-- -->: (string | RegExp)\[] }

  * ##### optionalcreateForeignKeyConstraints?<!-- -->: boolean
  * ##### optionaldisableForeignKeys?<!-- -->: boolean
  * ##### optionalignoreSchema?<!-- -->: string\[]
  * ##### optionalmanagementDbName?<!-- -->: string
  * ##### optionalskipColumns?<!-- -->: [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)<(string | RegExp)\[]>
  * ##### optionalskipTables?<!-- -->: (string | RegExp)\[]

## Methods<!-- -->[**](#Methods)

### [**](#configureColumn)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaHelper.ts#L200)inheritedconfigureColumn

* ****configureColumn**(column, col, knex, changedProperties): ColumnBuilder

- Inherited from MySqlSchemaHelper.configureColumn

  #### Parameters

  * ##### column: [Column](https://mikro-orm.io/api/knex/interface/Column.md)
  * ##### col: ColumnBuilder
  * ##### knex: [Knex](https://mikro-orm.io/api/knex/interface/Knex.md)\<any, any\[]>
  * ##### optionalchangedProperties: Set\<string>

  #### Returns ColumnBuilder

### [**](#configureColumnDefault)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/dialects/mysql/MySqlSchemaHelper.ts#L248)inheritedconfigureColumnDefault

* ****configureColumnDefault**(column, col, knex, changedProperties): ColumnBuilder

- Inherited from MySqlSchemaHelper.configureColumnDefault

  #### Parameters

  * ##### column: [Column](https://mikro-orm.io/api/knex/interface/Column.md)
  * ##### col: ColumnBuilder
  * ##### knex: [Knex](https://mikro-orm.io/api/knex/interface/Knex.md)\<any, any\[]>
  * ##### optionalchangedProperties: Set\<string>

  #### Returns ColumnBuilder

### [**](#createCheck)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaHelper.ts#L507)inheritedcreateCheck

* ****createCheck**(table, check): void

- Inherited from MySqlSchemaHelper.createCheck

  #### Parameters

  * ##### table: CreateTableBuilder
  * ##### check: [CheckDef](https://mikro-orm.io/api/knex/interface/CheckDef.md)\<unknown>

  #### Returns void

### [**](#createForeignKey)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaHelper.ts#L422)inheritedcreateForeignKey

* ****createForeignKey**(table, foreignKey, schema): void

- Inherited from MySqlSchemaHelper.createForeignKey

  #### Parameters

  * ##### table: CreateTableBuilder
  * ##### foreignKey: [ForeignKey](https://mikro-orm.io/api/knex/interface/ForeignKey.md)
  * ##### optionalschema: string

  #### Returns void

### [**](#createIndex)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaHelper.ts#L472)inheritedcreateIndex

* ****createIndex**(table, index, tableDef, createPrimary): void

- Inherited from MySqlSchemaHelper.createIndex

  #### Parameters

  * ##### table: CreateTableBuilder
  * ##### index: [IndexDef](https://mikro-orm.io/api/knex/interface/IndexDef.md)
  * ##### tableDef: DatabaseTable
  * ##### createPrimary: boolean = <!-- -->false

  #### Returns void

### [**](#createSchemaBuilder)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaHelper.ts#L511)inheritedcreateSchemaBuilder

* ****createSchemaBuilder**(schema): SchemaBuilder

- Inherited from MySqlSchemaHelper.createSchemaBuilder

  #### Parameters

  * ##### optionalschema: string

  #### Returns SchemaBuilder

### [**](#createTable)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaHelper.ts#L391)inheritedcreateTable

* ****createTable**(tableDef, alter): SchemaBuilder

- Inherited from MySqlSchemaHelper.createTable

  #### Parameters

  * ##### tableDef: DatabaseTable
  * ##### optionalalter: boolean

  #### Returns SchemaBuilder

### [**](#createTableColumn)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/dialects/mysql/MySqlSchemaHelper.ts#L222)inheritedcreateTableColumn

* ****createTableColumn**(table, column, fromTable, changedProperties, alter): undefined | ColumnBuilder

- Inherited from MySqlSchemaHelper.createTableColumn

  #### Parameters

  * ##### table: [MySqlTableBuilder](https://mikro-orm.io/api/knex/interface/MySqlTableBuilder.md)
  * ##### column: [Column](https://mikro-orm.io/api/knex/interface/Column.md)
  * ##### fromTable: DatabaseTable
  * ##### optionalchangedProperties: Set\<string>
  * ##### optionalalter: boolean

  #### Returns undefined | ColumnBuilder

### [**](#databaseExists)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaHelper.ts#L353)inheriteddatabaseExists

* ****databaseExists**(connection, name): Promise\<boolean>

- Inherited from MySqlSchemaHelper.databaseExists

  #### Parameters

  * ##### connection: [Connection](https://mikro-orm.io/api/core/class/Connection.md)
  * ##### name: string

  #### Returns Promise\<boolean>

### [**](#disableForeignKeysSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/dialects/mysql/MySqlSchemaHelper.ts#L27)inheriteddisableForeignKeysSQL

* ****disableForeignKeysSQL**(): string

- Inherited from MySqlSchemaHelper.disableForeignKeysSQL

  #### Returns string

### [**](#dump)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaHelper.ts#L373)inheriteddump

* ****dump**(builder, append): Promise\<string>

- Inherited from MySqlSchemaHelper.dump

  #### Parameters

  * ##### builder: string | SchemaBuilder
  * ##### append: string

  #### Returns Promise\<string>

### [**](#enableForeignKeysSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/dialects/mysql/MySqlSchemaHelper.ts#L31)inheritedenableForeignKeysSQL

* ****enableForeignKeysSQL**(): string

- Inherited from MySqlSchemaHelper.enableForeignKeysSQL

  #### Returns string

### [**](#finalizeTable)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/dialects/mysql/MySqlSchemaHelper.ts#L35)inheritedfinalizeTable

* ****finalizeTable**(table, charset, collate): void

- Inherited from MySqlSchemaHelper.finalizeTable

  #### Parameters

  * ##### table: CreateTableBuilder
  * ##### charset: string
  * ##### optionalcollate: string

  #### Returns void

### [**](#getAllChecks)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/mariadb/src/MariaDbSchemaHelper.ts#L117)getAllChecks

* ****getAllChecks**(connection, tables, columns): Promise<[Dictionary](https://mikro-orm.io/api/core.md#Dictionary)<[CheckDef](https://mikro-orm.io/api/knex/interface/CheckDef.md)\<unknown>\[]>>

- Overrides MySqlSchemaHelper.getAllChecks

  #### Parameters

  * ##### connection: [AbstractSqlConnection](https://mikro-orm.io/api/knex/class/AbstractSqlConnection.md)
  * ##### tables: [Table](https://mikro-orm.io/api/knex/interface/Table.md)\[]
  * ##### optionalcolumns: [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)<[Column](https://mikro-orm.io/api/knex/interface/Column.md)\[]>

  #### Returns Promise<[Dictionary](https://mikro-orm.io/api/core.md#Dictionary)<[CheckDef](https://mikro-orm.io/api/knex/interface/CheckDef.md)\<unknown>\[]>>

### [**](#getAllColumns)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/mariadb/src/MariaDbSchemaHelper.ts#L61)getAllColumns

* ****getAllColumns**(connection, tables): Promise<[Dictionary](https://mikro-orm.io/api/core.md#Dictionary)<[Column](https://mikro-orm.io/api/knex/interface/Column.md)\[]>>

- Overrides MySqlSchemaHelper.getAllColumns

  #### Parameters

  * ##### connection: [AbstractSqlConnection](https://mikro-orm.io/api/knex/class/AbstractSqlConnection.md)
  * ##### tables: [Table](https://mikro-orm.io/api/knex/interface/Table.md)\[]

  #### Returns Promise<[Dictionary](https://mikro-orm.io/api/core.md#Dictionary)<[Column](https://mikro-orm.io/api/knex/interface/Column.md)\[]>>

### [**](#getAllEnumDefinitions)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/dialects/mysql/MySqlSchemaHelper.ts#L317)inheritedgetAllEnumDefinitions

* ****getAllEnumDefinitions**(connection, tables): Promise<[Dictionary](https://mikro-orm.io/api/core.md#Dictionary)<[Dictionary](https://mikro-orm.io/api/core.md#Dictionary)\<string\[]>>>

- Inherited from MySqlSchemaHelper.getAllEnumDefinitions

  #### Parameters

  * ##### connection: [AbstractSqlConnection](https://mikro-orm.io/api/knex/class/AbstractSqlConnection.md)
  * ##### tables: [Table](https://mikro-orm.io/api/knex/interface/Table.md)\[]

  #### Returns Promise<[Dictionary](https://mikro-orm.io/api/core.md#Dictionary)<[Dictionary](https://mikro-orm.io/api/core.md#Dictionary)\<string\[]>>>

### [**](#getAllForeignKeys)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/dialects/mysql/MySqlSchemaHelper.ts#L180)inheritedgetAllForeignKeys

* ****getAllForeignKeys**(connection, tables): Promise<[Dictionary](https://mikro-orm.io/api/core.md#Dictionary)<[Dictionary](https://mikro-orm.io/api/core.md#Dictionary)<[ForeignKey](https://mikro-orm.io/api/knex/interface/ForeignKey.md)>>>

- Inherited from MySqlSchemaHelper.getAllForeignKeys

  #### Parameters

  * ##### connection: [AbstractSqlConnection](https://mikro-orm.io/api/knex/class/AbstractSqlConnection.md)
  * ##### tables: [Table](https://mikro-orm.io/api/knex/interface/Table.md)\[]

  #### Returns Promise<[Dictionary](https://mikro-orm.io/api/core.md#Dictionary)<[Dictionary](https://mikro-orm.io/api/core.md#Dictionary)<[ForeignKey](https://mikro-orm.io/api/knex/interface/ForeignKey.md)>>>

### [**](#getAllIndexes)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/mariadb/src/MariaDbSchemaHelper.ts#L34)getAllIndexes

* ****getAllIndexes**(connection, tables): Promise<[Dictionary](https://mikro-orm.io/api/core.md#Dictionary)<[IndexDef](https://mikro-orm.io/api/knex/interface/IndexDef.md)\[]>>

- Overrides MySqlSchemaHelper.getAllIndexes

  #### Parameters

  * ##### connection: [AbstractSqlConnection](https://mikro-orm.io/api/knex/class/AbstractSqlConnection.md)
  * ##### tables: [Table](https://mikro-orm.io/api/knex/interface/Table.md)\[]

  #### Returns Promise<[Dictionary](https://mikro-orm.io/api/core.md#Dictionary)<[IndexDef](https://mikro-orm.io/api/knex/interface/IndexDef.md)\[]>>

### [**](#getAlterColumnAutoincrement)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaHelper.ts#L232)inheritedgetAlterColumnAutoincrement

* ****getAlterColumnAutoincrement**(tableName, column, schemaName): string

- Inherited from MySqlSchemaHelper.getAlterColumnAutoincrement

  #### Parameters

  * ##### tableName: string
  * ##### column: [Column](https://mikro-orm.io/api/knex/interface/Column.md)
  * ##### optionalschemaName: string

  #### Returns string

### [**](#getAlterNativeEnumSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaHelper.ts#L98)inheritedgetAlterNativeEnumSQL

* ****getAlterNativeEnumSQL**(name, schema, value, items, oldItems): string

- Inherited from MySqlSchemaHelper.getAlterNativeEnumSQL

  #### Parameters

  * ##### name: string
  * ##### optionalschema: string
  * ##### optionalvalue: string
  * ##### optionalitems: string\[]
  * ##### optionaloldItems: string\[]

  #### Returns string

### [**](#getAlterTable)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaHelper.ts#L533)optionalinheritedgetAlterTable

* ****getAlterTable**(changedTable, wrap): Promise\<string>

- Inherited from MySqlSchemaHelper.getAlterTable

  #### Parameters

  * ##### changedTable: [TableDifference](https://mikro-orm.io/api/knex/interface/TableDifference.md)
  * ##### optionalwrap: boolean

  #### Returns Promise\<string>

### [**](#getChangeColumnCommentSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/dialects/mysql/MySqlSchemaHelper.ts#L285)inheritedgetChangeColumnCommentSQL

* ****getChangeColumnCommentSQL**(tableName, to, schemaName): string

- Inherited from MySqlSchemaHelper.getChangeColumnCommentSQL

  #### Parameters

  * ##### tableName: string
  * ##### to: [Column](https://mikro-orm.io/api/knex/interface/Column.md)
  * ##### optionalschemaName: string

  #### Returns string

### [**](#getChecks)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/mariadb/src/MariaDbSchemaHelper.ts#L159)getChecks

* ****getChecks**(connection, tableName, schemaName, columns): Promise<[CheckDef](https://mikro-orm.io/api/knex/interface/CheckDef.md)\<unknown>\[]>

- Overrides MySqlSchemaHelper.getChecks

  #### Parameters

  * ##### connection: [AbstractSqlConnection](https://mikro-orm.io/api/knex/class/AbstractSqlConnection.md)
  * ##### tableName: string
  * ##### schemaName: string
  * ##### optionalcolumns: [Column](https://mikro-orm.io/api/knex/interface/Column.md)\[]

  #### Returns Promise<[CheckDef](https://mikro-orm.io/api/knex/interface/CheckDef.md)\<unknown>\[]>

### [**](#getColumns)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/dialects/mysql/MySqlSchemaHelper.ts#L365)inheritedgetColumns

* ****getColumns**(connection, tableName, schemaName): Promise<[Column](https://mikro-orm.io/api/knex/interface/Column.md)\[]>

- Inherited from MySqlSchemaHelper.getColumns

  #### Parameters

  * ##### connection: [AbstractSqlConnection](https://mikro-orm.io/api/knex/class/AbstractSqlConnection.md)
  * ##### tableName: string
  * ##### optionalschemaName: string

  #### Returns Promise<[Column](https://mikro-orm.io/api/knex/interface/Column.md)\[]>

### [**](#getCreateDatabaseSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaHelper.ts#L318)inheritedgetCreateDatabaseSQL

* ****getCreateDatabaseSQL**(name): string

- Inherited from MySqlSchemaHelper.getCreateDatabaseSQL

  #### Parameters

  * ##### name: string

  #### Returns string

### [**](#getCreateIndexSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaHelper.ts#L130)inheritedgetCreateIndexSQL

* ****getCreateIndexSQL**(tableName, index, partialExpression): string

- Inherited from MySqlSchemaHelper.getCreateIndexSQL

  #### Parameters

  * ##### tableName: string
  * ##### index: [IndexDef](https://mikro-orm.io/api/knex/interface/IndexDef.md)
  * ##### partialExpression: boolean = <!-- -->false

  #### Returns string

### [**](#getCreateNamespaceSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaHelper.ts#L328)inheritedgetCreateNamespaceSQL

* ****getCreateNamespaceSQL**(name): string

- Inherited from MySqlSchemaHelper.getCreateNamespaceSQL

  #### Parameters

  * ##### name: string

  #### Returns string

### [**](#getCreateNativeEnumSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaHelper.ts#L90)inheritedgetCreateNativeEnumSQL

* ****getCreateNativeEnumSQL**(name, values, schema): string

- Inherited from MySqlSchemaHelper.getCreateNativeEnumSQL

  #### Parameters

  * ##### name: string
  * ##### values: unknown\[]
  * ##### optionalschema: string

  #### Returns string

### [**](#getDatabaseExistsSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaHelper.ts#L337)inheritedgetDatabaseExistsSQL

* ****getDatabaseExistsSQL**(name): string

- Inherited from MySqlSchemaHelper.getDatabaseExistsSQL

  #### Parameters

  * ##### name: string

  #### Returns string

### [**](#getDatabaseNotExistsError)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaHelper.ts#L341)inheritedgetDatabaseNotExistsError

* ****getDatabaseNotExistsError**(dbName): string

- Inherited from MySqlSchemaHelper.getDatabaseNotExistsError

  #### Parameters

  * ##### dbName: string

  #### Returns string

### [**](#getDefaultEmptyString)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaHelper.ts#L349)inheritedgetDefaultEmptyString

* ****getDefaultEmptyString**(): string

- Inherited from MySqlSchemaHelper.getDefaultEmptyString

  #### Returns string

### [**](#getDropColumnsSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaHelper.ts#L155)inheritedgetDropColumnsSQL

* ****getDropColumnsSQL**(tableName, columns, schemaName): string

- Inherited from MySqlSchemaHelper.getDropColumnsSQL

  #### Parameters

  * ##### tableName: string
  * ##### columns: [Column](https://mikro-orm.io/api/knex/interface/Column.md)\[]
  * ##### optionalschemaName: string

  #### Returns string

### [**](#getDropDatabaseSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaHelper.ts#L323)inheritedgetDropDatabaseSQL

* ****getDropDatabaseSQL**(name): string

- Inherited from MySqlSchemaHelper.getDropDatabaseSQL

  #### Parameters

  * ##### name: string

  #### Returns string

### [**](#getDropIndexSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaHelper.ts#L147)inheritedgetDropIndexSQL

* ****getDropIndexSQL**(tableName, index): string

- Inherited from MySqlSchemaHelper.getDropIndexSQL

  #### Parameters

  * ##### tableName: string
  * ##### index: [IndexDef](https://mikro-orm.io/api/knex/interface/IndexDef.md)

  #### Returns string

### [**](#getDropNamespaceSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaHelper.ts#L333)inheritedgetDropNamespaceSQL

* ****getDropNamespaceSQL**(name): string

- Inherited from MySqlSchemaHelper.getDropNamespaceSQL

  #### Parameters

  * ##### name: string

  #### Returns string

### [**](#getDropNativeEnumSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaHelper.ts#L94)inheritedgetDropNativeEnumSQL

* ****getDropNativeEnumSQL**(name, schema): string

- Inherited from MySqlSchemaHelper.getDropNativeEnumSQL

  #### Parameters

  * ##### name: string
  * ##### optionalschema: string

  #### Returns string

### [**](#getEnumDefinitions)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/dialects/mysql/MySqlSchemaHelper.ts#L359)inheritedgetEnumDefinitions

* ****getEnumDefinitions**(connection, checks, tableName, schemaName): Promise<[Dictionary](https://mikro-orm.io/api/core.md#Dictionary)\<string\[]>>

- Inherited from MySqlSchemaHelper.getEnumDefinitions

  #### Parameters

  * ##### connection: [AbstractSqlConnection](https://mikro-orm.io/api/knex/class/AbstractSqlConnection.md)
  * ##### checks: [CheckDef](https://mikro-orm.io/api/knex/interface/CheckDef.md)\<unknown>\[]
  * ##### tableName: string
  * ##### optionalschemaName: string

  #### Returns Promise<[Dictionary](https://mikro-orm.io/api/core.md#Dictionary)\<string\[]>>

### [**](#getForeignKeys)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaHelper.ts#L66)inheritedgetForeignKeys

* ****getForeignKeys**(connection, tableName, schemaName): Promise<[Dictionary](https://mikro-orm.io/api/core.md#Dictionary)>

- Inherited from MySqlSchemaHelper.getForeignKeys

  #### Parameters

  * ##### connection: [AbstractSqlConnection](https://mikro-orm.io/api/knex/class/AbstractSqlConnection.md)
  * ##### tableName: string
  * ##### optionalschemaName: string

  #### Returns Promise<[Dictionary](https://mikro-orm.io/api/core.md#Dictionary)>

### [**](#getForeignKeysSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/dialects/mysql/MySqlSchemaHelper.ts#L310)inheritedgetForeignKeysSQL

* ****getForeignKeysSQL**(tableName, schemaName): string

- Inherited from MySqlSchemaHelper.getForeignKeysSQL

  #### Parameters

  * ##### tableName: string
  * ##### optionalschemaName: string

  #### Returns string

### [**](#getIndexes)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/dialects/mysql/MySqlSchemaHelper.ts#L371)inheritedgetIndexes

* ****getIndexes**(connection, tableName, schemaName): Promise<[IndexDef](https://mikro-orm.io/api/knex/interface/IndexDef.md)\[]>

- Inherited from MySqlSchemaHelper.getIndexes

  #### Parameters

  * ##### connection: [AbstractSqlConnection](https://mikro-orm.io/api/knex/class/AbstractSqlConnection.md)
  * ##### tableName: string
  * ##### optionalschemaName: string

  #### Returns Promise<[IndexDef](https://mikro-orm.io/api/knex/interface/IndexDef.md)\[]>

### [**](#getListTablesSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/dialects/mysql/MySqlSchemaHelper.ts#L44)inheritedgetListTablesSQL

* ****getListTablesSQL**(): string

- Inherited from MySqlSchemaHelper.getListTablesSQL

  #### Returns string

### [**](#getManagementDbName)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaHelper.ts#L345)inheritedgetManagementDbName

* ****getManagementDbName**(): string

- Inherited from MySqlSchemaHelper.getManagementDbName

  #### Returns string

### [**](#getNamespaces)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaHelper.ts#L240)inheritedgetNamespaces

* ****getNamespaces**(connection): Promise\<string\[]>

- Inherited from MySqlSchemaHelper.getNamespaces

  #### Parameters

  * ##### connection: [AbstractSqlConnection](https://mikro-orm.io/api/knex/class/AbstractSqlConnection.md)

  #### Returns Promise\<string\[]>

### [**](#getPostAlterTable)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaHelper.ts#L228)inheritedgetPostAlterTable

* ****getPostAlterTable**(tableDiff, safe): string

- Inherited from MySqlSchemaHelper.getPostAlterTable

  #### Parameters

  * ##### tableDiff: [TableDifference](https://mikro-orm.io/api/knex/interface/TableDifference.md)
  * ##### safe: boolean

  #### Returns string

### [**](#getPreAlterTable)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/dialects/mysql/MySqlSchemaHelper.ts#L206)inheritedgetPreAlterTable

* ****getPreAlterTable**(tableDiff, safe): string

- Inherited from MySqlSchemaHelper.getPreAlterTable

  #### Parameters

  * ##### tableDiff: [TableDifference](https://mikro-orm.io/api/knex/interface/TableDifference.md)
  * ##### safe: boolean

  #### Returns string

### [**](#getPrimaryKeys)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaHelper.ts#L52)inheritedgetPrimaryKeys

* ****getPrimaryKeys**(connection, indexes, tableName, schemaName): Promise\<string\[]>

- Inherited from MySqlSchemaHelper.getPrimaryKeys

  #### Parameters

  * ##### connection: [AbstractSqlConnection](https://mikro-orm.io/api/knex/class/AbstractSqlConnection.md)
  * ##### indexes: [IndexDef](https://mikro-orm.io/api/knex/interface/IndexDef.md)\[] = <!-- -->\[]
  * ##### tableName: string
  * ##### optionalschemaName: string

  #### Returns Promise\<string\[]>

### [**](#getReferencedTableName)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaHelper.ts#L456)inheritedgetReferencedTableName

* ****getReferencedTableName**(referencedTableName, schema): string

- Inherited from MySqlSchemaHelper.getReferencedTableName

  #### Parameters

  * ##### referencedTableName: string
  * ##### optionalschema: string

  #### Returns string

### [**](#getRenameColumnSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/dialects/mysql/MySqlSchemaHelper.ts#L269)inheritedgetRenameColumnSQL

* ****getRenameColumnSQL**(tableName, oldColumnName, to): string

- Inherited from MySqlSchemaHelper.getRenameColumnSQL

  #### Parameters

  * ##### tableName: string
  * ##### oldColumnName: string
  * ##### to: [Column](https://mikro-orm.io/api/knex/interface/Column.md)

  #### Returns string

### [**](#getRenameIndexSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/dialects/mysql/MySqlSchemaHelper.ts#L277)inheritedgetRenameIndexSQL

* ****getRenameIndexSQL**(tableName, index, oldIndexName): string

- Inherited from MySqlSchemaHelper.getRenameIndexSQL

  #### Parameters

  * ##### tableName: string
  * ##### index: [IndexDef](https://mikro-orm.io/api/knex/interface/IndexDef.md)
  * ##### oldIndexName: string

  #### Returns string

### [**](#getSchemaBeginning)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/dialects/mysql/MySqlSchemaHelper.ts#L19)inheritedgetSchemaBeginning

* ****getSchemaBeginning**(charset, disableForeignKeys): string

- Inherited from MySqlSchemaHelper.getSchemaBeginning

  #### Parameters

  * ##### charset: string
  * ##### optionaldisableForeignKeys: boolean

  #### Returns string

### [**](#getSchemaEnd)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaHelper.ts#L36)inheritedgetSchemaEnd

* ****getSchemaEnd**(disableForeignKeys): string

- Inherited from MySqlSchemaHelper.getSchemaEnd

  #### Parameters

  * ##### optionaldisableForeignKeys: boolean

  #### Returns string

### [**](#getTablesGroupedBySchemas)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaHelper.ts#L521)inheritedgetTablesGroupedBySchemas

* ****getTablesGroupedBySchemas**(tables): Map\<undefined | string, [Table](https://mikro-orm.io/api/knex/interface/Table.md)\[]>

- Inherited from MySqlSchemaHelper.getTablesGroupedBySchemas

  #### Parameters

  * ##### tables: [Table](https://mikro-orm.io/api/knex/interface/Table.md)\[]

  #### Returns Map\<undefined | string, [Table](https://mikro-orm.io/api/knex/interface/Table.md)\[]>

### [**](#hasNonDefaultPrimaryKeyName)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaHelper.ts#L162)inheritedhasNonDefaultPrimaryKeyName

* ****hasNonDefaultPrimaryKeyName**(table): boolean

- Inherited from MySqlSchemaHelper.hasNonDefaultPrimaryKeyName

  #### Parameters

  * ##### table: DatabaseTable

  #### Returns boolean

### [**](#inferLengthFromColumnType)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaHelper.ts#L57)inheritedinferLengthFromColumnType

* ****inferLengthFromColumnType**(type): undefined | number

- Inherited from MySqlSchemaHelper.inferLengthFromColumnType

  #### Parameters

  * ##### type: string

  #### Returns undefined | number

### [**](#loadInformationSchema)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/mariadb/src/MariaDbSchemaHelper.ts#L14)loadInformationSchema

* ****loadInformationSchema**(schema, connection, tables): Promise\<void>

- Overrides MySqlSchemaHelper.loadInformationSchema

  #### Parameters

  * ##### schema: DatabaseSchema
  * ##### connection: [AbstractSqlConnection](https://mikro-orm.io/api/knex/class/AbstractSqlConnection.md)
  * ##### tables: [Table](https://mikro-orm.io/api/knex/interface/Table.md)\[]

  #### Returns Promise\<void>

### [**](#mapForeignKeys)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaHelper.ts#L275)inheritedmapForeignKeys

* ****mapForeignKeys**(fks, tableName, schemaName): [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)

- Inherited from MySqlSchemaHelper.mapForeignKeys

  #### Parameters

  * ##### fks: any\[]
  * ##### tableName: string
  * ##### optionalschemaName: string

  #### Returns [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)

### [**](#normalizeDefaultValue)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/dialects/mysql/MySqlSchemaHelper.ts#L376)inheritednormalizeDefaultValue

* ****normalizeDefaultValue**(defaultValue, length): string | number

- Inherited from MySqlSchemaHelper.normalizeDefaultValue

  #### Parameters

  * ##### defaultValue: string
  * ##### length: number

  #### Returns string | number

### [**](#pushTableQuery)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaHelper.ts#L369)inheritedpushTableQuery

* ****pushTableQuery**(table, expression, grouping): void

- Inherited from MySqlSchemaHelper.pushTableQuery

  Uses `raw` method injected in `AbstractSqlConnection` to allow adding custom queries inside alter statements.

  ***

  #### Parameters

  * ##### table: TableBuilder
  * ##### expression: string
  * ##### grouping: string = <!-- -->'alterTable'

  #### Returns void

### [**](#splitTableName)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaHelper.ts#L448)inheritedsplitTableName

* ****splitTableName**(name): \[undefined | string, string]

- Inherited from MySqlSchemaHelper.splitTableName

  #### Parameters

  * ##### name: string

  #### Returns \[undefined | string, string]

### [**](#supportsSchemaConstraints)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaHelper.ts#L48)inheritedsupportsSchemaConstraints

* ****supportsSchemaConstraints**(): boolean

- Inherited from MySqlSchemaHelper.supportsSchemaConstraints

  #### Returns boolean
