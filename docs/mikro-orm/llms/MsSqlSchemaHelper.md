# Source: https://mikro-orm.io/api/mssql/class/MsSqlSchemaHelper.md

# MsSqlSchemaHelper<!-- -->

### Hierarchy

* [SchemaHelper](https://mikro-orm.io/api/knex/class/SchemaHelper.md)
  * *MsSqlSchemaHelper*

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
* [**getPostAlterTable](#getPostAlterTable)
* [**getPreAlterTable](#getPreAlterTable)
* [**getPrimaryKeys](#getPrimaryKeys)
* [**getReferencedTableName](#getReferencedTableName)
* [**getRenameColumnSQL](#getRenameColumnSQL)
* [**getRenameIndexSQL](#getRenameIndexSQL)
* [**getSchemaBeginning](#getSchemaBeginning)
* [**getSchemaEnd](#getSchemaEnd)
* [**getTablesGroupedBySchemas](#getTablesGroupedBySchemas)
* [**handleMultilineComment](#handleMultilineComment)
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

* ****new MsSqlSchemaHelper**(platform): [MsSqlSchemaHelper](https://mikro-orm.io/api/mssql/class/MsSqlSchemaHelper.md)

- Inherited from SchemaHelper.constructor

  #### Parameters

  * ##### platform: [AbstractSqlPlatform](https://mikro-orm.io/api/knex/class/AbstractSqlPlatform.md)

  #### Returns [MsSqlSchemaHelper](https://mikro-orm.io/api/mssql/class/MsSqlSchemaHelper.md)

## Properties<!-- -->[**](#Properties)

### [**](#DEFAULT_VALUES)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/mssql/src/MsSqlSchemaHelper.ts#L24)staticreadonlyDEFAULT\_VALUES

**DEFAULT\_VALUES: { false: string\[]; getdate(): string\[]; true: string\[] } =

<!-- -->

...

#### Type declaration

* ##### false: string\[]
* ##### getdate(): string\[]
* ##### true: string\[]

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

### [**](#configureColumn)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaHelper.ts#L200)inheritedconfigureColumn

* ****configureColumn**(column, col, knex, changedProperties): ColumnBuilder

- Inherited from SchemaHelper.configureColumn

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

### [**](#createTableColumn)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/mssql/src/MsSqlSchemaHelper.ts#L427)createTableColumn

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

### [**](#disableForeignKeysSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/mssql/src/MsSqlSchemaHelper.ts#L34)disableForeignKeysSQL

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

### [**](#enableForeignKeysSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/mssql/src/MsSqlSchemaHelper.ts#L38)enableForeignKeysSQL

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

### [**](#getAllChecks)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/mssql/src/MsSqlSchemaHelper.ts#L281)getAllChecks

* ****getAllChecks**(connection, tablesBySchemas): Promise<[Dictionary](https://mikro-orm.io/api/core.md#Dictionary)<[CheckDef](https://mikro-orm.io/api/knex/interface/CheckDef.md)\<unknown>\[]>>

- #### Parameters

  * ##### connection: [AbstractSqlConnection](https://mikro-orm.io/api/knex/class/AbstractSqlConnection.md)
  * ##### tablesBySchemas: Map\<undefined | string, [Table](https://mikro-orm.io/api/knex/interface/Table.md)\[]>

  #### Returns Promise<[Dictionary](https://mikro-orm.io/api/core.md#Dictionary)<[CheckDef](https://mikro-orm.io/api/knex/interface/CheckDef.md)\<unknown>\[]>>

### [**](#getAllColumns)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/mssql/src/MsSqlSchemaHelper.ts#L82)getAllColumns

* ****getAllColumns**(connection, tablesBySchemas): Promise<[Dictionary](https://mikro-orm.io/api/core.md#Dictionary)<[Column](https://mikro-orm.io/api/knex/interface/Column.md)\[]>>

- #### Parameters

  * ##### connection: [AbstractSqlConnection](https://mikro-orm.io/api/knex/class/AbstractSqlConnection.md)
  * ##### tablesBySchemas: Map\<undefined | string, [Table](https://mikro-orm.io/api/knex/interface/Table.md)\[]>

  #### Returns Promise<[Dictionary](https://mikro-orm.io/api/core.md#Dictionary)<[Column](https://mikro-orm.io/api/knex/interface/Column.md)\[]>>

### [**](#getAllForeignKeys)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/mssql/src/MsSqlSchemaHelper.ts#L211)getAllForeignKeys

* ****getAllForeignKeys**(connection, tablesBySchemas): Promise<[Dictionary](https://mikro-orm.io/api/core.md#Dictionary)<[Dictionary](https://mikro-orm.io/api/core.md#Dictionary)<[ForeignKey](https://mikro-orm.io/api/knex/interface/ForeignKey.md)>>>

- #### Parameters

  * ##### connection: [AbstractSqlConnection](https://mikro-orm.io/api/knex/class/AbstractSqlConnection.md)
  * ##### tablesBySchemas: Map\<undefined | string, [Table](https://mikro-orm.io/api/knex/interface/Table.md)\[]>

  #### Returns Promise<[Dictionary](https://mikro-orm.io/api/core.md#Dictionary)<[Dictionary](https://mikro-orm.io/api/core.md#Dictionary)<[ForeignKey](https://mikro-orm.io/api/knex/interface/ForeignKey.md)>>>

### [**](#getAllIndexes)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/mssql/src/MsSqlSchemaHelper.ts#L156)getAllIndexes

* ****getAllIndexes**(connection, tablesBySchemas): Promise<[Dictionary](https://mikro-orm.io/api/core.md#Dictionary)<[IndexDef](https://mikro-orm.io/api/knex/interface/IndexDef.md)\[]>>

- #### Parameters

  * ##### connection: [AbstractSqlConnection](https://mikro-orm.io/api/knex/class/AbstractSqlConnection.md)
  * ##### tablesBySchemas: Map\<undefined | string, [Table](https://mikro-orm.io/api/knex/interface/Table.md)\[]>

  #### Returns Promise<[Dictionary](https://mikro-orm.io/api/core.md#Dictionary)<[IndexDef](https://mikro-orm.io/api/knex/interface/IndexDef.md)\[]>>

### [**](#getAlterColumnAutoincrement)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaHelper.ts#L232)inheritedgetAlterColumnAutoincrement

* ****getAlterColumnAutoincrement**(tableName, column, schemaName): string

- Inherited from SchemaHelper.getAlterColumnAutoincrement

  #### Parameters

  * ##### tableName: string
  * ##### column: [Column](https://mikro-orm.io/api/knex/interface/Column.md)
  * ##### optionalschemaName: string

  #### Returns string

### [**](#getAlterNativeEnumSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaHelper.ts#L98)inheritedgetAlterNativeEnumSQL

* ****getAlterNativeEnumSQL**(name, schema, value, items, oldItems): string

- Inherited from SchemaHelper.getAlterNativeEnumSQL

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

### [**](#getChangeColumnCommentSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaHelper.ts#L236)inheritedgetChangeColumnCommentSQL

* ****getChangeColumnCommentSQL**(tableName, to, schemaName): string

- Inherited from SchemaHelper.getChangeColumnCommentSQL

  #### Parameters

  * ##### tableName: string
  * ##### to: [Column](https://mikro-orm.io/api/knex/interface/Column.md)
  * ##### optionalschemaName: string

  #### Returns string

### [**](#getChecks)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaHelper.ts#L252)inheritedgetChecks

* ****getChecks**(connection, tableName, schemaName, columns): Promise<[CheckDef](https://mikro-orm.io/api/knex/interface/CheckDef.md)\<unknown>\[]>

- Inherited from SchemaHelper.getChecks

  #### Parameters

  * ##### connection: [AbstractSqlConnection](https://mikro-orm.io/api/knex/class/AbstractSqlConnection.md)
  * ##### tableName: string
  * ##### optionalschemaName: string
  * ##### optionalcolumns: [Column](https://mikro-orm.io/api/knex/interface/Column.md)\[]

  #### Returns Promise<[CheckDef](https://mikro-orm.io/api/knex/interface/CheckDef.md)\<unknown>\[]>

### [**](#getColumns)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaHelper.ts#L244)inheritedgetColumns

* ****getColumns**(connection, tableName, schemaName): Promise<[Column](https://mikro-orm.io/api/knex/interface/Column.md)\[]>

- Inherited from SchemaHelper.getColumns

  #### Parameters

  * ##### connection: [AbstractSqlConnection](https://mikro-orm.io/api/knex/class/AbstractSqlConnection.md)
  * ##### tableName: string
  * ##### optionalschemaName: string

  #### Returns Promise<[Column](https://mikro-orm.io/api/knex/interface/Column.md)\[]>

### [**](#getCreateDatabaseSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaHelper.ts#L318)inheritedgetCreateDatabaseSQL

* ****getCreateDatabaseSQL**(name): string

- Inherited from SchemaHelper.getCreateDatabaseSQL

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

### [**](#getCreateNamespaceSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/mssql/src/MsSqlSchemaHelper.ts#L386)getCreateNamespaceSQL

* ****getCreateNamespaceSQL**(name): string

- Overrides SchemaHelper.getCreateNamespaceSQL

  #### Parameters

  * ##### name: string

  #### Returns string

### [**](#getCreateNativeEnumSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaHelper.ts#L90)inheritedgetCreateNativeEnumSQL

* ****getCreateNativeEnumSQL**(name, values, schema): string

- Inherited from SchemaHelper.getCreateNativeEnumSQL

  #### Parameters

  * ##### name: string
  * ##### values: unknown\[]
  * ##### optionalschema: string

  #### Returns string

### [**](#getDatabaseExistsSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/mssql/src/MsSqlSchemaHelper.ts#L42)getDatabaseExistsSQL

* ****getDatabaseExistsSQL**(name): string

- Overrides SchemaHelper.getDatabaseExistsSQL

  #### Parameters

  * ##### name: string

  #### Returns string

### [**](#getDatabaseNotExistsError)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaHelper.ts#L341)inheritedgetDatabaseNotExistsError

* ****getDatabaseNotExistsError**(dbName): string

- Inherited from SchemaHelper.getDatabaseNotExistsError

  #### Parameters

  * ##### dbName: string

  #### Returns string

### [**](#getDefaultEmptyString)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaHelper.ts#L349)inheritedgetDefaultEmptyString

* ****getDefaultEmptyString**(): string

- Inherited from SchemaHelper.getDefaultEmptyString

  #### Returns string

### [**](#getDropColumnsSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/mssql/src/MsSqlSchemaHelper.ts#L398)getDropColumnsSQL

* ****getDropColumnsSQL**(tableName, columns, schemaName): string

- Overrides SchemaHelper.getDropColumnsSQL

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

### [**](#getDropIndexSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/mssql/src/MsSqlSchemaHelper.ts#L394)getDropIndexSQL

* ****getDropIndexSQL**(tableName, index): string

- Overrides SchemaHelper.getDropIndexSQL

  #### Parameters

  * ##### tableName: string
  * ##### index: [IndexDef](https://mikro-orm.io/api/knex/interface/IndexDef.md)

  #### Returns string

### [**](#getDropNamespaceSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/mssql/src/MsSqlSchemaHelper.ts#L390)getDropNamespaceSQL

* ****getDropNamespaceSQL**(name): string

- Overrides SchemaHelper.getDropNamespaceSQL

  #### Parameters

  * ##### name: string

  #### Returns string

### [**](#getDropNativeEnumSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaHelper.ts#L94)inheritedgetDropNativeEnumSQL

* ****getDropNativeEnumSQL**(name, schema): string

- Inherited from SchemaHelper.getDropNativeEnumSQL

  #### Parameters

  * ##### name: string
  * ##### optionalschema: string

  #### Returns string

### [**](#getEnumDefinitions)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/mssql/src/MsSqlSchemaHelper.ts#L240)getEnumDefinitions

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

### [**](#getIndexes)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaHelper.ts#L248)inheritedgetIndexes

* ****getIndexes**(connection, tableName, schemaName): Promise<[IndexDef](https://mikro-orm.io/api/knex/interface/IndexDef.md)\[]>

- Inherited from SchemaHelper.getIndexes

  #### Parameters

  * ##### connection: [AbstractSqlConnection](https://mikro-orm.io/api/knex/class/AbstractSqlConnection.md)
  * ##### tableName: string
  * ##### optionalschemaName: string

  #### Returns Promise<[IndexDef](https://mikro-orm.io/api/knex/interface/IndexDef.md)\[]>

### [**](#getListTablesSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/mssql/src/MsSqlSchemaHelper.ts#L46)getListTablesSQL

* ****getListTablesSQL**(): string

- Overrides SchemaHelper.getListTablesSQL

  #### Returns string

### [**](#getManagementDbName)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/mssql/src/MsSqlSchemaHelper.ts#L30)getManagementDbName

* ****getManagementDbName**(): string

- Overrides SchemaHelper.getManagementDbName

  #### Returns string

### [**](#getNamespaces)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/mssql/src/MsSqlSchemaHelper.ts#L54)getNamespaces

* ****getNamespaces**(connection): Promise\<string\[]>

- Overrides SchemaHelper.getNamespaces

  #### Parameters

  * ##### connection: [AbstractSqlConnection](https://mikro-orm.io/api/knex/class/AbstractSqlConnection.md)

  #### Returns Promise\<string\[]>

### [**](#getPostAlterTable)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/mssql/src/MsSqlSchemaHelper.ts#L363)getPostAlterTable

* ****getPostAlterTable**(tableDiff, safe): string

- Overrides SchemaHelper.getPostAlterTable

  #### Parameters

  * ##### tableDiff: [TableDifference](https://mikro-orm.io/api/knex/interface/TableDifference.md)
  * ##### safe: boolean

  #### Returns string

### [**](#getPreAlterTable)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/mssql/src/MsSqlSchemaHelper.ts#L321)getPreAlterTable

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

### [**](#getRenameColumnSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/mssql/src/MsSqlSchemaHelper.ts#L419)getRenameColumnSQL

* ****getRenameColumnSQL**(tableName, oldColumnName, to, schemaName): string

- Overrides SchemaHelper.getRenameColumnSQL

  #### Parameters

  * ##### tableName: string
  * ##### oldColumnName: string
  * ##### to: [Column](https://mikro-orm.io/api/knex/interface/Column.md)
  * ##### optionalschemaName: string

  #### Returns string

### [**](#getRenameIndexSQL)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaHelper.ts#L151)inheritedgetRenameIndexSQL

* ****getRenameIndexSQL**(tableName, index, oldIndexName): string

- Inherited from SchemaHelper.getRenameIndexSQL

  #### Parameters

  * ##### tableName: string
  * ##### index: [IndexDef](https://mikro-orm.io/api/knex/interface/IndexDef.md)
  * ##### oldIndexName: string

  #### Returns string

### [**](#getSchemaBeginning)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaHelper.ts#L20)inheritedgetSchemaBeginning

* ****getSchemaBeginning**(charset, disableForeignKeys): string

- Inherited from SchemaHelper.getSchemaBeginning

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

### [**](#handleMultilineComment)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/mssql/src/MsSqlSchemaHelper.ts#L473)handleMultilineComment

* ****handleMultilineComment**(comment): string

- Overrides SchemaHelper.handleMultilineComment

  MSSQL supports `\n` in SQL and stores `\\n` literally. This method overrides the parent behavior to prevent replacing `\n` with `\\n`.

  ***

  #### Parameters

  * ##### comment: string

  #### Returns string

### [**](#hasNonDefaultPrimaryKeyName)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/knex/src/schema/SchemaHelper.ts#L162)inheritedhasNonDefaultPrimaryKeyName

* ****hasNonDefaultPrimaryKeyName**(table): boolean

- Inherited from SchemaHelper.hasNonDefaultPrimaryKeyName

  #### Parameters

  * ##### table: DatabaseTable

  #### Returns boolean

### [**](#inferLengthFromColumnType)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/mssql/src/MsSqlSchemaHelper.ts#L450)inferLengthFromColumnType

* ****inferLengthFromColumnType**(type): undefined | number

- Overrides SchemaHelper.inferLengthFromColumnType

  #### Parameters

  * ##### type: string

  #### Returns undefined | number

### [**](#loadInformationSchema)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/mssql/src/MsSqlSchemaHelper.ts#L300)loadInformationSchema

* ****loadInformationSchema**(schema, connection, tables): Promise\<void>

- Overrides SchemaHelper.loadInformationSchema

  #### Parameters

  * ##### schema: DatabaseSchema
  * ##### connection: [AbstractSqlConnection](https://mikro-orm.io/api/knex/class/AbstractSqlConnection.md)
  * ##### tables: [Table](https://mikro-orm.io/api/knex/interface/Table.md)\[]

  #### Returns Promise\<void>

### [**](#mapForeignKeys)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/mssql/src/MsSqlSchemaHelper.ts#L200)mapForeignKeys

* ****mapForeignKeys**(fks, tableName, schemaName): [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)

- Overrides SchemaHelper.mapForeignKeys

  #### Parameters

  * ##### fks: any\[]
  * ##### tableName: string
  * ##### optionalschemaName: string

  #### Returns [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)

### [**](#normalizeDefaultValue)[**](https://github.com/mikro-orm/mikro-orm/blob/master/packages/mssql/src/MsSqlSchemaHelper.ts#L60)normalizeDefaultValue

* ****normalizeDefaultValue**(defaultValue, length, defaultValues, stripQuotes): string | number

- Overrides SchemaHelper.normalizeDefaultValue

  #### Parameters

  * ##### defaultValue: string
  * ##### length: number
  * ##### defaultValues: [Dictionary](https://mikro-orm.io/api/core.md#Dictionary)\<string\[]> = <!-- -->{}
  * ##### stripQuotes: boolean = <!-- -->false

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
