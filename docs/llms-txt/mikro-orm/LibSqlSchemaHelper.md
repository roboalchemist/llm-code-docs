# Source: https://mikro-orm.io/api/libsql/class/LibSqlSchemaHelper.md

# LibSqlSchemaHelper<!-- -->

### Hierarchy

* [BaseSqliteSchemaHelper](https://mikro-orm.io/api/knex/class/BaseSqliteSchemaHelper.md)
  * *LibSqlSchemaHelper*

## Index[**](#Index)

### Constructors

* [**constructor](#constructor)

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
* [**isImplicitIndex](#isImplicitIndex)
* [**loadInformationSchema](#loadInformationSchema)
* [**mapForeignKeys](#mapForeignKeys)
* [**normalizeDefaultValue](#normalizeDefaultValue)
* [**pushTableQuery](#pushTableQuery)
* [**splitTableName](#splitTableName)
* [**supportsSchemaConstraints](#supportsSchemaConstraints)

## Constructors<!-- -->[**](#Constructors)

### [**](#constructor)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaHelper.ts#L18)constructor

* ****new LibSqlSchemaHelper**(platform): [LibSqlSchemaHelper](https://mikro-orm.io/api/libsql/class/LibSqlSchemaHelper.md)

- Inherited from BaseSqliteSchemaHelper.constructor

  #### Parameters

  * ##### platform: [AbstractSqlPlatform](https://mikro-orm.io/api/knex/class/AbstractSqlPlatform.md)

  #### Returns [LibSqlSchemaHelper](https://mikro-orm.io/api/libsql/class/LibSqlSchemaHelper.md)

## Accessors<!-- -->[**](#Accessors)

### [**](#knex)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaHelper.ts#L535)inheritedknex

* **get knex(): [Knex](https://mikro-orm.io/api/knex/interface/Knex.md)\<any, any\[]>

- Inherited from BaseSqliteSchemaHelper.knex

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

- Inherited from BaseSqliteSchemaHelper.options

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

- Inherited from BaseSqliteSchemaHelper.configureColumn

  #### Parameters

  * ##### column: [Column](https://mikro-orm.io/api/knex/interface/Column.md)
  * ##### col: ColumnBuilder
  * ##### knex: [Knex](https://mikro-orm.io/api/knex/interface/Knex.md)\<any, any\[]>
  * ##### optionalchangedProperties: Set\<string>

  #### Returns ColumnBuilder

### [**](#configureColumnDefault)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaHelper.ts#L212)inheritedconfigureColumnDefault

* ****configureColumnDefault**(column, col, knex, changedProperties): ColumnBuilder

- Inherited from BaseSqliteSchemaHelper.configureColumnDefault

  #### Parameters

  * ##### column: [Column](https://mikro-orm.io/api/knex/interface/Column.md)
  * ##### col: ColumnBuilder
  * ##### knex: [Knex](https://mikro-orm.io/api/knex/interface/Knex.md)\<any, any\[]>
  * ##### optionalchangedProperties: Set\<string>

  #### Returns ColumnBuilder

### [**](#createCheck)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaHelper.ts#L507)inheritedcreateCheck

* ****createCheck**(table, check): void

- Inherited from BaseSqliteSchemaHelper.createCheck

  #### Parameters

  * ##### table: CreateTableBuilder
  * ##### check: [CheckDef](https://mikro-orm.io/api/knex/interface/CheckDef.md)\<unknown>

  #### Returns void

### [**](#createForeignKey)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaHelper.ts#L422)inheritedcreateForeignKey

* ****createForeignKey**(table, foreignKey, schema): void

- Inherited from BaseSqliteSchemaHelper.createForeignKey

  #### Parameters

  * ##### table: CreateTableBuilder
  * ##### foreignKey: [ForeignKey](https://mikro-orm.io/api/knex/interface/ForeignKey.md)
  * ##### optionalschema: string

  #### Returns void

### [**](#createIndex)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaHelper.ts#L472)inheritedcreateIndex

* ****createIndex**(table, index, tableDef, createPrimary): void

- Inherited from BaseSqliteSchemaHelper.createIndex

  #### Parameters

  * ##### table: CreateTableBuilder
  * ##### index: [IndexDef](https://mikro-orm.io/api/knex/interface/IndexDef.md)
  * ##### tableDef: DatabaseTable
  * ##### createPrimary: boolean = <!-- -->false

  #### Returns void

### [**](#createSchemaBuilder)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaHelper.ts#L511)inheritedcreateSchemaBuilder

* ****createSchemaBuilder**(schema): SchemaBuilder

- Inherited from BaseSqliteSchemaHelper.createSchemaBuilder

  #### Parameters

  * ##### optionalschema: string

  #### Returns SchemaBuilder

### [**](#createTable)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaHelper.ts#L391)inheritedcreateTable

* ****createTable**(tableDef, alter): SchemaBuilder

- Inherited from BaseSqliteSchemaHelper.createTable

  #### Parameters

  * ##### tableDef: DatabaseTable
  * ##### optionalalter: boolean

  #### Returns SchemaBuilder

### [**](#createTableColumn)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaHelper.ts#L174)inheritedcreateTableColumn

* ****createTableColumn**(table, column, fromTable, changedProperties, alter): undefined | ColumnBuilder

- Inherited from BaseSqliteSchemaHelper.createTableColumn

  #### Parameters

  * ##### table: TableBuilder
  * ##### column: [Column](https://mikro-orm.io/api/knex/interface/Column.md)
  * ##### fromTable: DatabaseTable
  * ##### optionalchangedProperties: Set\<string>
  * ##### optionalalter: boolean

  #### Returns undefined | ColumnBuilder

### [**](#databaseExists)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/dialects/sqlite/BaseSqliteSchemaHelper.ts#L196)inheriteddatabaseExists

* ****databaseExists**(connection, name): Promise\<boolean>

- Inherited from BaseSqliteSchemaHelper.databaseExists

  #### Parameters

  * ##### connection: [Connection](https://mikro-orm.io/api/core/class/Connection.md)
  * ##### name: string

  #### Returns Promise\<boolean>

### [**](#disableForeignKeysSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/dialects/sqlite/BaseSqliteSchemaHelper.ts#L8)inheriteddisableForeignKeysSQL

* ****disableForeignKeysSQL**(): string

- Inherited from BaseSqliteSchemaHelper.disableForeignKeysSQL

  #### Returns string

### [**](#dump)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaHelper.ts#L373)inheriteddump

* ****dump**(builder, append): Promise\<string>

- Inherited from BaseSqliteSchemaHelper.dump

  #### Parameters

  * ##### builder: string | SchemaBuilder
  * ##### append: string

  #### Returns Promise\<string>

### [**](#enableForeignKeysSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/dialects/sqlite/BaseSqliteSchemaHelper.ts#L12)inheritedenableForeignKeysSQL

* ****enableForeignKeysSQL**(): string

- Inherited from BaseSqliteSchemaHelper.enableForeignKeysSQL

  #### Returns string

### [**](#finalizeTable)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaHelper.ts#L44)inheritedfinalizeTable

* ****finalizeTable**(table, charset, collate): void

- Inherited from BaseSqliteSchemaHelper.finalizeTable

  #### Parameters

  * ##### table: TableBuilder
  * ##### charset: string
  * ##### optionalcollate: string

  #### Returns void

### [**](#getAlterColumnAutoincrement)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaHelper.ts#L232)inheritedgetAlterColumnAutoincrement

* ****getAlterColumnAutoincrement**(tableName, column, schemaName): string

- Inherited from BaseSqliteSchemaHelper.getAlterColumnAutoincrement

  #### Parameters

  * ##### tableName: string
  * ##### column: [Column](https://mikro-orm.io/api/knex/interface/Column.md)
  * ##### optionalschemaName: string

  #### Returns string

### [**](#getAlterNativeEnumSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaHelper.ts#L98)inheritedgetAlterNativeEnumSQL

* ****getAlterNativeEnumSQL**(name, schema, value, items, oldItems): string

- Inherited from BaseSqliteSchemaHelper.getAlterNativeEnumSQL

  #### Parameters

  * ##### name: string
  * ##### optionalschema: string
  * ##### optionalvalue: string
  * ##### optionalitems: string\[]
  * ##### optionaloldItems: string\[]

  #### Returns string

### [**](#getAlterTable)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/dialects/sqlite/BaseSqliteSchemaHelper.ts#L209)inheritedgetAlterTable

* ****getAlterTable**(changedTable, wrap): Promise\<string>

- Inherited from BaseSqliteSchemaHelper.getAlterTable

  #### Parameters

  * ##### changedTable: [TableDifference](https://mikro-orm.io/api/knex/interface/TableDifference.md)
  * ##### optionalwrap: boolean

  #### Returns Promise\<string>

### [**](#getChangeColumnCommentSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaHelper.ts#L236)inheritedgetChangeColumnCommentSQL

* ****getChangeColumnCommentSQL**(tableName, to, schemaName): string

- Inherited from BaseSqliteSchemaHelper.getChangeColumnCommentSQL

  #### Parameters

  * ##### tableName: string
  * ##### to: [Column](https://mikro-orm.io/api/knex/interface/Column.md)
  * ##### optionalschemaName: string

  #### Returns string

### [**](#getChecks)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/dialects/sqlite/BaseSqliteSchemaHelper.ts#L161)inheritedgetChecks

* ****getChecks**(connection, tableName, schemaName): Promise<[CheckDef](https://mikro-orm.io/api/knex/interface/CheckDef.md)\<unknown>\[]>

- Inherited from BaseSqliteSchemaHelper.getChecks

  #### Parameters

  * ##### connection: [AbstractSqlConnection](https://mikro-orm.io/api/knex/class/AbstractSqlConnection.md)
  * ##### tableName: string
  * ##### optionalschemaName: string

  #### Returns Promise<[CheckDef](https://mikro-orm.io/api/knex/interface/CheckDef.md)\<unknown>\[]>

### [**](#getColumns)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/dialects/sqlite/BaseSqliteSchemaHelper.ts#L67)inheritedgetColumns

* ****getColumns**(connection, tableName, schemaName): Promise\<any\[]>

- Inherited from BaseSqliteSchemaHelper.getColumns

  #### Parameters

  * ##### connection: [AbstractSqlConnection](https://mikro-orm.io/api/knex/class/AbstractSqlConnection.md)
  * ##### tableName: string
  * ##### optionalschemaName: string

  #### Returns Promise\<any\[]>

### [**](#getCreateDatabaseSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/dialects/sqlite/BaseSqliteSchemaHelper.ts#L192)inheritedgetCreateDatabaseSQL

* ****getCreateDatabaseSQL**(name): string

- Inherited from BaseSqliteSchemaHelper.getCreateDatabaseSQL

  #### Parameters

  * ##### name: string

  #### Returns string

### [**](#getCreateIndexSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaHelper.ts#L130)inheritedgetCreateIndexSQL

* ****getCreateIndexSQL**(tableName, index, partialExpression): string

- Inherited from BaseSqliteSchemaHelper.getCreateIndexSQL

  #### Parameters

  * ##### tableName: string
  * ##### index: [IndexDef](https://mikro-orm.io/api/knex/interface/IndexDef.md)
  * ##### partialExpression: boolean = <!-- -->false

  #### Returns string

### [**](#getCreateNamespaceSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaHelper.ts#L328)inheritedgetCreateNamespaceSQL

* ****getCreateNamespaceSQL**(name): string

- Inherited from BaseSqliteSchemaHelper.getCreateNamespaceSQL

  #### Parameters

  * ##### name: string

  #### Returns string

### [**](#getCreateNativeEnumSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaHelper.ts#L90)inheritedgetCreateNativeEnumSQL

* ****getCreateNativeEnumSQL**(name, values, schema): string

- Inherited from BaseSqliteSchemaHelper.getCreateNativeEnumSQL

  #### Parameters

  * ##### name: string
  * ##### values: unknown\[]
  * ##### optionalschema: string

  #### Returns string

### [**](#getDatabaseExistsSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaHelper.ts#L337)inheritedgetDatabaseExistsSQL

* ****getDatabaseExistsSQL**(name): string

- Inherited from BaseSqliteSchemaHelper.getDatabaseExistsSQL

  #### Parameters

  * ##### name: string

  #### Returns string

### [**](#getDatabaseNotExistsError)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaHelper.ts#L341)inheritedgetDatabaseNotExistsError

* ****getDatabaseNotExistsError**(dbName): string

- Inherited from BaseSqliteSchemaHelper.getDatabaseNotExistsError

  #### Parameters

  * ##### dbName: string

  #### Returns string

### [**](#getDefaultEmptyString)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaHelper.ts#L349)inheritedgetDefaultEmptyString

* ****getDefaultEmptyString**(): string

- Inherited from BaseSqliteSchemaHelper.getDefaultEmptyString

  #### Returns string

### [**](#getDropColumnsSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/dialects/sqlite/BaseSqliteSchemaHelper.ts#L34)inheritedgetDropColumnsSQL

* ****getDropColumnsSQL**(tableName, columns, schemaName): string

- Inherited from BaseSqliteSchemaHelper.getDropColumnsSQL

  #### Parameters

  * ##### tableName: string
  * ##### columns: [Column](https://mikro-orm.io/api/knex/interface/Column.md)\[]
  * ##### optionalschemaName: string

  #### Returns string

### [**](#getDropDatabaseSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/dialects/sqlite/BaseSqliteSchemaHelper.ts#L25)inheritedgetDropDatabaseSQL

* ****getDropDatabaseSQL**(name): string

- Inherited from BaseSqliteSchemaHelper.getDropDatabaseSQL

  #### Parameters

  * ##### name: string

  #### Returns string

### [**](#getDropIndexSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaHelper.ts#L147)inheritedgetDropIndexSQL

* ****getDropIndexSQL**(tableName, index): string

- Inherited from BaseSqliteSchemaHelper.getDropIndexSQL

  #### Parameters

  * ##### tableName: string
  * ##### index: [IndexDef](https://mikro-orm.io/api/knex/interface/IndexDef.md)

  #### Returns string

### [**](#getDropNamespaceSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaHelper.ts#L333)inheritedgetDropNamespaceSQL

* ****getDropNamespaceSQL**(name): string

- Inherited from BaseSqliteSchemaHelper.getDropNamespaceSQL

  #### Parameters

  * ##### name: string

  #### Returns string

### [**](#getDropNativeEnumSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaHelper.ts#L94)inheritedgetDropNativeEnumSQL

* ****getDropNativeEnumSQL**(name, schema): string

- Inherited from BaseSqliteSchemaHelper.getDropNativeEnumSQL

  #### Parameters

  * ##### name: string
  * ##### optionalschema: string

  #### Returns string

### [**](#getEnumDefinitions)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/dialects/sqlite/BaseSqliteSchemaHelper.ts#L105)inheritedgetEnumDefinitions

* ****getEnumDefinitions**(connection, checks, tableName, schemaName): Promise<[Dictionary](https://mikro-orm.io/api/core.md#Dictionary)\<string\[]>>

- Inherited from BaseSqliteSchemaHelper.getEnumDefinitions

  #### Parameters

  * ##### connection: [AbstractSqlConnection](https://mikro-orm.io/api/knex/class/AbstractSqlConnection.md)
  * ##### checks: [CheckDef](https://mikro-orm.io/api/knex/interface/CheckDef.md)\<unknown>\[]
  * ##### tableName: string
  * ##### schemaName: string

  #### Returns Promise<[Dictionary](https://mikro-orm.io/api/core.md#Dictionary)\<string\[]>>

### [**](#getForeignKeys)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaHelper.ts#L66)inheritedgetForeignKeys

* ****getForeignKeys**(connection, tableName, schemaName): Promise<[Dictionary](https://mikro-orm.io/api/core.md#Dictionary)>

- Inherited from BaseSqliteSchemaHelper.getForeignKeys

  #### Parameters

  * ##### connection: [AbstractSqlConnection](https://mikro-orm.io/api/knex/class/AbstractSqlConnection.md)
  * ##### tableName: string
  * ##### optionalschemaName: string

  #### Returns Promise<[Dictionary](https://mikro-orm.io/api/core.md#Dictionary)>

### [**](#getForeignKeysSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/dialects/sqlite/BaseSqliteSchemaHelper.ts#L166)inheritedgetForeignKeysSQL

* ****getForeignKeysSQL**(tableName): string

- Inherited from BaseSqliteSchemaHelper.getForeignKeysSQL

  #### Parameters

  * ##### tableName: string

  #### Returns string

### [**](#getIndexes)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/dialects/sqlite/BaseSqliteSchemaHelper.ts#L131)inheritedgetIndexes

* ****getIndexes**(connection, tableName, schemaName): Promise<[IndexDef](https://mikro-orm.io/api/knex/interface/IndexDef.md)\[]>

- Inherited from BaseSqliteSchemaHelper.getIndexes

  #### Parameters

  * ##### connection: [AbstractSqlConnection](https://mikro-orm.io/api/knex/class/AbstractSqlConnection.md)
  * ##### tableName: string
  * ##### optionalschemaName: string

  #### Returns Promise<[IndexDef](https://mikro-orm.io/api/knex/interface/IndexDef.md)\[]>

### [**](#getListTablesSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/dialects/sqlite/BaseSqliteSchemaHelper.ts#L20)inheritedgetListTablesSQL

* ****getListTablesSQL**(): string

- Inherited from BaseSqliteSchemaHelper.getListTablesSQL

  #### Returns string

### [**](#getManagementDbName)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/dialects/sqlite/BaseSqliteSchemaHelper.ts#L188)inheritedgetManagementDbName

* ****getManagementDbName**(): string

- Inherited from BaseSqliteSchemaHelper.getManagementDbName

  #### Returns string

### [**](#getNamespaces)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaHelper.ts#L240)inheritedgetNamespaces

* ****getNamespaces**(connection): Promise\<string\[]>

- Inherited from BaseSqliteSchemaHelper.getNamespaces

  #### Parameters

  * ##### connection: [AbstractSqlConnection](https://mikro-orm.io/api/knex/class/AbstractSqlConnection.md)

  #### Returns Promise\<string\[]>

### [**](#getPostAlterTable)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaHelper.ts#L228)inheritedgetPostAlterTable

* ****getPostAlterTable**(tableDiff, safe): string

- Inherited from BaseSqliteSchemaHelper.getPostAlterTable

  #### Parameters

  * ##### tableDiff: [TableDifference](https://mikro-orm.io/api/knex/interface/TableDifference.md)
  * ##### safe: boolean

  #### Returns string

### [**](#getPreAlterTable)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaHelper.ts#L224)inheritedgetPreAlterTable

* ****getPreAlterTable**(tableDiff, safe): string

- Inherited from BaseSqliteSchemaHelper.getPreAlterTable

  #### Parameters

  * ##### tableDiff: [TableDifference](https://mikro-orm.io/api/knex/interface/TableDifference.md)
  * ##### safe: boolean

  #### Returns string

### [**](#getPrimaryKeys)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/dialects/sqlite/BaseSqliteSchemaHelper.ts#L124)inheritedgetPrimaryKeys

* ****getPrimaryKeys**(connection, indexes, tableName, schemaName): Promise\<string\[]>

- Inherited from BaseSqliteSchemaHelper.getPrimaryKeys

  #### Parameters

  * ##### connection: [AbstractSqlConnection](https://mikro-orm.io/api/knex/class/AbstractSqlConnection.md)
  * ##### indexes: [IndexDef](https://mikro-orm.io/api/knex/interface/IndexDef.md)\[]
  * ##### tableName: string
  * ##### optionalschemaName: string

  #### Returns Promise\<string\[]>

### [**](#getReferencedTableName)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaHelper.ts#L456)inheritedgetReferencedTableName

* ****getReferencedTableName**(referencedTableName, schema): string

- Inherited from BaseSqliteSchemaHelper.getReferencedTableName

  #### Parameters

  * ##### referencedTableName: string
  * ##### optionalschema: string

  #### Returns string

### [**](#getRenameColumnSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaHelper.ts#L119)inheritedgetRenameColumnSQL

* ****getRenameColumnSQL**(tableName, oldColumnName, to, schemaName): string

- Inherited from BaseSqliteSchemaHelper.getRenameColumnSQL

  #### Parameters

  * ##### tableName: string
  * ##### oldColumnName: string
  * ##### to: [Column](https://mikro-orm.io/api/knex/interface/Column.md)
  * ##### optionalschemaName: string

  #### Returns string

### [**](#getRenameIndexSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaHelper.ts#L151)inheritedgetRenameIndexSQL

* ****getRenameIndexSQL**(tableName, index, oldIndexName): string

- Inherited from BaseSqliteSchemaHelper.getRenameIndexSQL

  #### Parameters

  * ##### tableName: string
  * ##### index: [IndexDef](https://mikro-orm.io/api/knex/interface/IndexDef.md)
  * ##### oldIndexName: string

  #### Returns string

### [**](#getSchemaBeginning)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaHelper.ts#L20)inheritedgetSchemaBeginning

* ****getSchemaBeginning**(charset, disableForeignKeys): string

- Inherited from BaseSqliteSchemaHelper.getSchemaBeginning

  #### Parameters

  * ##### charset: string
  * ##### optionaldisableForeignKeys: boolean

  #### Returns string

### [**](#getSchemaEnd)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaHelper.ts#L36)inheritedgetSchemaEnd

* ****getSchemaEnd**(disableForeignKeys): string

- Inherited from BaseSqliteSchemaHelper.getSchemaEnd

  #### Parameters

  * ##### optionaldisableForeignKeys: boolean

  #### Returns string

### [**](#getTablesGroupedBySchemas)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaHelper.ts#L521)inheritedgetTablesGroupedBySchemas

* ****getTablesGroupedBySchemas**(tables): Map\<undefined | string, [Table](https://mikro-orm.io/api/knex/interface/Table.md)\[]>

- Inherited from BaseSqliteSchemaHelper.getTablesGroupedBySchemas

  #### Parameters

  * ##### tables: [Table](https://mikro-orm.io/api/knex/interface/Table.md)\[]

  #### Returns Map\<undefined | string, [Table](https://mikro-orm.io/api/knex/interface/Table.md)\[]>

### [**](#hasNonDefaultPrimaryKeyName)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaHelper.ts#L162)inheritedhasNonDefaultPrimaryKeyName

* ****hasNonDefaultPrimaryKeyName**(table): boolean

- Inherited from BaseSqliteSchemaHelper.hasNonDefaultPrimaryKeyName

  #### Parameters

  * ##### table: DatabaseTable

  #### Returns boolean

### [**](#inferLengthFromColumnType)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaHelper.ts#L57)inheritedinferLengthFromColumnType

* ****inferLengthFromColumnType**(type): undefined | number

- Inherited from BaseSqliteSchemaHelper.inferLengthFromColumnType

  #### Parameters

  * ##### type: string

  #### Returns undefined | number

### [**](#isImplicitIndex)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/dialects/sqlite/BaseSqliteSchemaHelper.ts#L204)inheritedisImplicitIndex

* ****isImplicitIndex**(name): boolean

- Inherited from BaseSqliteSchemaHelper.isImplicitIndex

  Implicit indexes will be ignored when diffing

  ***

  #### Parameters

  * ##### name: string

  #### Returns boolean

### [**](#loadInformationSchema)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaHelper.ts#L102)inheritedloadInformationSchema

* ****loadInformationSchema**(schema, connection, tables, schemas): Promise\<void>

- Inherited from BaseSqliteSchemaHelper.loadInformationSchema

  #### Parameters

  * ##### schema: DatabaseSchema
  * ##### connection: [AbstractSqlConnection](https://mikro-orm.io/api/knex/class/AbstractSqlConnection.md)
  * ##### tables: [Table](https://mikro-orm.io/api/knex/interface/Table.md)\[]
  * ##### optionalschemas: string\[]

  #### Returns Promise\<void>

### [**](#mapForeignKeys)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/dialects/sqlite/BaseSqliteSchemaHelper.ts#L170)inheritedmapForeignKeys

* ****mapForeignKeys**(fks, tableName): [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)

- Inherited from BaseSqliteSchemaHelper.mapForeignKeys

  #### Parameters

  * ##### fks: any\[]
  * ##### tableName: string

  #### Returns [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)

### [**](#normalizeDefaultValue)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaHelper.ts#L297)inheritednormalizeDefaultValue

* ****normalizeDefaultValue**(defaultValue, length, defaultValues): string | number

- Inherited from BaseSqliteSchemaHelper.normalizeDefaultValue

  #### Parameters

  * ##### defaultValue: string
  * ##### optionallength: number
  * ##### defaultValues: [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)\<string\[]> = <!-- -->{}

  #### Returns string | number

### [**](#pushTableQuery)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaHelper.ts#L369)inheritedpushTableQuery

* ****pushTableQuery**(table, expression, grouping): void

- Inherited from BaseSqliteSchemaHelper.pushTableQuery

  Uses `raw` method injected in `AbstractSqlConnection` to allow adding custom queries inside alter statements.

  ***

  #### Parameters

  * ##### table: TableBuilder
  * ##### expression: string
  * ##### grouping: string = <!-- -->'alterTable'

  #### Returns void

### [**](#splitTableName)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaHelper.ts#L448)inheritedsplitTableName

* ****splitTableName**(name): \[undefined | string, string]

- Inherited from BaseSqliteSchemaHelper.splitTableName

  #### Parameters

  * ##### name: string

  #### Returns \[undefined | string, string]

### [**](#supportsSchemaConstraints)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/dialects/sqlite/BaseSqliteSchemaHelper.ts#L16)inheritedsupportsSchemaConstraints

* ****supportsSchemaConstraints**(): boolean

- Inherited from BaseSqliteSchemaHelper.supportsSchemaConstraints

  #### Returns boolean
